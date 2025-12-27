import time
import json
import torch
import logging
import threading
import subprocess
import sys
import os
import psutil

# Add DCGM bindings to path
dcgm_path = '/usr/local/dcgm/bindings/python3'
if os.path.exists(dcgm_path) and dcgm_path not in sys.path:
    sys.path.append(dcgm_path)

try:
    import pydcgm
    import dcgm_structs
    import dcgm_fields
    import dcgm_agent
    DCGM_AVAILABLE = True
except ImportError:
    DCGM_AVAILABLE = False
    logging.warning("DCGM python bindings not found. SM Activity monitoring will be disabled.")

import pynvml
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from contextlib import contextmanager

@dataclass
class StageMetrics:
    name: str
    start_time: float
    end_time: float = 0.0
    start_memory: int = 0
    peak_memory: int = 0
    end_memory: int = 0
    gpu_utilization: float = 0.0
    sm_activity: float = 0.0  # New field for SM Activity
    tensor_core_utilization: float = 0.0 # New field for Tensor Core Utilization
    cpu_utilization: float = 0.0 # New field for CPU Usage
    system_memory_peak: int = 0 # New field for System RAM Peak (bytes)
    
    @property
    def duration(self):
        return self.end_time - self.start_time

    @property
    def memory_delta(self):
        return self.end_memory - self.start_memory

    @property
    def activation_memory(self):
        """Estimate activation memory as Peak - Start."""
        return max(0, self.peak_memory - self.start_memory)
    
    @property
    def compute_efficiency(self):
        """Estimate compute efficiency (GFLOPs proxy) = Time * Utilization"""
        return self.duration * self.gpu_utilization

    @property
    def compute_load(self):
        """Estimate computational load = Time * SM Activity"""
        return self.duration * self.sm_activity

class PerformanceMonitor:
    def __init__(self):
        self.events: List[StageMetrics] = []
        self.stage_stack: List[StageMetrics] = []
        self.start_time = time.time()
        self.system_info = self._get_system_info()
        
        # GPU Sampling
        self.gpu_samples = [] # (timestamp, util_percent)
        self.sm_samples = [] # (timestamp, sm_percent)
        self.tensor_samples = [] # (timestamp, tensor_percent)
        self.cpu_samples = [] # (timestamp, cpu_percent)
        self.ram_samples = [] # (timestamp, used_bytes)
        self.running = True
        self.gpu_handle = None
        
        # Initialize monitors
        self._init_gpu_monitor()
        self._init_sm_monitor()
        
    def _init_gpu_monitor(self):
        try:
            pynvml.nvmlInit()
            # Assume Device 0 for simplicity, or match torch.cuda.current_device()
            device_index = torch.cuda.current_device() if torch.cuda.is_available() else 0
            self.gpu_handle = pynvml.nvmlDeviceGetHandleByIndex(device_index)
            
            self.monitor_thread = threading.Thread(target=self._monitor_loop, daemon=True)
            self.monitor_thread.start()
        except Exception as e:
            logging.warning(f"Failed to initialize GPU monitor: {e}")
            self.gpu_handle = None

    def _init_sm_monitor(self):
        """Initialize SM activity monitoring using DCGM or fallback to nvidia-smi dmon"""
        self.using_dcgm = False
        self.dcgm_handle_obj = None
        self.dcgm_group_obj = None
        self.dcgm_field_group_obj = None
        
        # Try DCGM first
        if DCGM_AVAILABLE:
            try:
                # Initialize DCGM library (load .so)
                if hasattr(dcgm_structs, '_LoadDcgmLibrary'):
                    dcgm_structs._LoadDcgmLibrary()
                
                # Connect to DCGM host engine (assumes it's running)
                # Try standalone first
                try:
                    self.dcgm_handle_obj = pydcgm.DcgmHandle(ipAddress="127.0.0.1:5555")
                    logging.info("Connected to standalone DCGM host engine.")
                except Exception:
                    logging.info("Could not connect to standalone DCGM, starting embedded agent...")
                    self.dcgm_handle_obj = pydcgm.DcgmHandle(ipAddress=None)
                    logging.info("Started embedded DCGM agent.")
                
                # Get System and Group
                self.dcgm_system_obj = self.dcgm_handle_obj.GetSystem()
                device_index = torch.cuda.current_device() if torch.cuda.is_available() else 0
                
                # Create a group with the device
                group_name = f"wan_monitor_group_{str(time.time())}"
                self.dcgm_group_obj = self.dcgm_system_obj.GetGroupWithGpuIds(group_name, [device_index])
                
                # Define Fields
                # We want Profiling fields: SM_ACTIVE and TENSOR_ACTIVE
                # But they might fail if profiling module is not loaded.
                
                self.sm_field_id = dcgm_fields.DCGM_FI_PROF_SM_ACTIVE
                self.tensor_field_id = dcgm_fields.DCGM_FI_PROF_PIPE_TENSOR_ACTIVE
                
                # Try to watch profiling fields first
                try:
                    field_ids = [self.sm_field_id, self.tensor_field_id]
                    field_group_name = f"wan_field_group_prof_{str(time.time())}"
                    self.dcgm_field_group_obj = pydcgm.DcgmFieldGroup(self.dcgm_handle_obj, field_group_name, field_ids)
                    
                    update_freq = 100000 # 100ms
                    max_keep_age = 3600.0
                    max_keep_samples = 0
                    
                    self.dcgm_group_obj.samples.WatchFields(self.dcgm_field_group_obj, update_freq, max_keep_age, max_keep_samples)
                    logging.info("DCGM: Profiling fields (SM, Tensor) enabled.")
                    self.profiling_enabled = True
                    
                except Exception as e:
                    logging.warning(f"DCGM Profiling fields failed (Tensor Core not available): {e}")
                    logging.info("Falling back to standard metrics (GPU Util) for SM Activity.")
                    
                    # Fallback to standard GPU Util for SM Activity
                    self.sm_field_id = dcgm_fields.DCGM_FI_DEV_GPU_UTIL
                    self.tensor_field_id = None # Not available
                    self.profiling_enabled = False
                    
                    field_ids = [self.sm_field_id]
                    field_group_name = f"wan_field_group_std_{str(time.time())}"
                    self.dcgm_field_group_obj = pydcgm.DcgmFieldGroup(self.dcgm_handle_obj, field_group_name, field_ids)
                    
                    self.dcgm_group_obj.samples.WatchFields(self.dcgm_field_group_obj, 100000, 3600.0, 0)
                
                # Start Monitoring Thread
                self.using_dcgm = True
                self.sm_thread = threading.Thread(target=self._monitor_sm_loop_dcgm, daemon=True)
                self.sm_thread.start()
                logging.info("DCGM monitoring initialized successfully.")
                return
                
            except Exception as e:
                logging.warning(f"Failed to initialize DCGM monitor: {e}. Falling back to nvidia-smi dmon.")
                self.using_dcgm = False

        # Fallback to nvidia-smi dmon
        try:
            device_index = torch.cuda.current_device() if torch.cuda.is_available() else 0
            self.sm_process = subprocess.Popen(
                ["nvidia-smi", "dmon", "-i", str(device_index), "-d", "1"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1
            )
            self.sm_thread = threading.Thread(target=self._monitor_sm_loop_dmon, daemon=True)
            self.sm_thread.start()
            logging.info("nvidia-smi dmon SM Activity monitoring initialized (fallback).")
        except Exception as e:
            logging.warning(f"Failed to initialize SM monitor fallback: {e}")
            self.sm_process = None

    def _monitor_sm_loop_dcgm(self):
        """Loop to poll DCGM fields"""
        if not self.using_dcgm:
            return
            
        device_index = torch.cuda.current_device() if torch.cuda.is_available() else 0
        
        while self.running:
            try:
                # Update fields
                # Use dcgm_agent directly if Handle method is missing
                dcgm_agent.dcgmUpdateAllFields(self.dcgm_handle_obj.handle, 1)
                
                # Get Latest Values
                data = self.dcgm_group_obj.samples.GetLatest(self.dcgm_field_group_obj)
                
                # Parse
                if device_index in data.values:
                    gpu_data = data.values[device_index]
                    
                    # SM Activity
                    if self.sm_field_id in gpu_data:
                        val = gpu_data[self.sm_field_id][0]
                        if not val.isBlank:
                            # If profiling (SM_ACTIVE), it's ratio 0.0-1.0. 
                            # If dev (GPU_UTIL), it's percent 0-100.
                            if self.profiling_enabled:
                                self.sm_samples.append((time.time(), val.value * 100.0))
                            else:
                                self.sm_samples.append((time.time(), float(val.value)))
                    
                    # Tensor Core
                    if self.tensor_field_id and self.tensor_field_id in gpu_data:
                        val = gpu_data[self.tensor_field_id][0]
                        if not val.isBlank:
                            self.tensor_samples.append((time.time(), val.value * 100.0))
                            
            except Exception as e:
                logging.error(f"Error in DCGM loop: {e}")
                time.sleep(1) # Backoff
            time.sleep(0.1)

    def _monitor_sm_loop_dmon(self):
        """Loop to parse nvidia-smi dmon output"""
        if not self.sm_process:
            return
            
        try:
            while self.running and self.sm_process.poll() is None:
                line = self.sm_process.stdout.readline()
                if not line:
                    break
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                try:
                    parts = line.split()
                    if len(parts) >= 5:
                        sm_util = float(parts[4])
                        self.sm_samples.append((time.time(), sm_util))
                except ValueError:
                    continue
        except Exception:
            pass
        finally:
            if self.sm_process:
                self.sm_process.terminate()

    def _monitor_loop(self):
        while self.running:
            # GPU Utilization
            if self.gpu_handle:
                try:
                    util = pynvml.nvmlDeviceGetUtilizationRates(self.gpu_handle)
                    self.gpu_samples.append((time.time(), util.gpu))
                except:
                    pass
            
            # CPU & RAM
            try:
                self.cpu_samples.append((time.time(), psutil.cpu_percent()))
                self.ram_samples.append((time.time(), psutil.virtual_memory().used))
            except:
                pass

            time.sleep(0.05) # 50ms sampling

    def __del__(self):
        self.running = False
        
        # Cleanup DCGM
        # pydcgm handles cleanup via destructors usually, but we can be explicit if needed.
        pass
        
        try:
            pynvml.nvmlShutdown()
        except:
            pass

    def _get_system_info(self):
        info = {
            "pytorch_version": torch.__version__,
            "cuda_version": torch.version.cuda if torch.cuda.is_available() else "N/A",
            "gpu_info": None
        }
        if torch.cuda.is_available():
            info["gpu_info"] = {
                "name": torch.cuda.get_device_name(0),
                "total_memory_gb": round(torch.cuda.get_device_properties(0).total_memory / (1024**3), 2)
            }
        else:
            info["gpu_info"] = {"name": "CPU", "total_memory_gb": 0}
        return info

    def _get_memory_allocated(self):
        if torch.cuda.is_available():
            return torch.cuda.memory_allocated()
        return 0

    def _get_max_memory_allocated(self):
        if torch.cuda.is_available():
            return torch.cuda.max_memory_allocated()
        return 0

    def start_stage(self, name: str):
        if torch.cuda.is_available():
             torch.cuda.synchronize()
        
        current_max = self._get_max_memory_allocated()
        if self.stage_stack:
            parent = self.stage_stack[-1]
            parent.peak_memory = max(parent.peak_memory, current_max)
        
        if torch.cuda.is_available():
            torch.cuda.reset_peak_memory_stats()
            
        start_mem = self._get_memory_allocated()
        stage = StageMetrics(
            name=name,
            start_time=time.time(),
            start_memory=start_mem,
            peak_memory=start_mem # Initialize with current
        )
        self.stage_stack.append(stage)
        return stage

    def end_stage(self):
        if self.stage_stack:
            if torch.cuda.is_available():
                torch.cuda.synchronize()
            
            stage = self.stage_stack.pop()
            stage.end_time = time.time()
            stage.end_memory = self._get_memory_allocated()
            
            # Calculate GPU Utilization for this stage
            if self.gpu_samples:
                # Filter samples within stage duration
                samples = [util for t, util in self.gpu_samples 
                          if t >= stage.start_time and t <= stage.end_time]
                if samples:
                    stage.gpu_utilization = sum(samples) / len(samples)
                else:
                    # Fallback: if short duration, take the closest sample
                    stage.gpu_utilization = 0.0 
            
            # Calculate SM Activity for this stage
            if self.sm_samples:
                sm_samples_stage = [util for t, util in self.sm_samples
                                   if t >= stage.start_time and t <= stage.end_time]
                if sm_samples_stage:
                    stage.sm_activity = sum(sm_samples_stage) / len(sm_samples_stage)
                else:
                    stage.sm_activity = 0.0

            # Calculate Tensor Core Utilization for this stage
            if self.tensor_samples:
                tensor_samples_stage = [util for t, util in self.tensor_samples
                                       if t >= stage.start_time and t <= stage.end_time]
                if tensor_samples_stage:
                    stage.tensor_core_utilization = sum(tensor_samples_stage) / len(tensor_samples_stage)
                else:
                    stage.tensor_core_utilization = 0.0

            # Calculate CPU Utilization
            if self.cpu_samples:
                cpu_samples_stage = [util for t, util in self.cpu_samples
                                    if t >= stage.start_time and t <= stage.end_time]
                if cpu_samples_stage:
                    stage.cpu_utilization = sum(cpu_samples_stage) / len(cpu_samples_stage)
            
            # Calculate System RAM Peak
            if self.ram_samples:
                ram_samples_stage = [used for t, used in self.ram_samples
                                    if t >= stage.start_time and t <= stage.end_time]
                if ram_samples_stage:
                    stage.system_memory_peak = max(ram_samples_stage)

            # Capture the peak observed during *this* stage execution (since its start)
            current_peak = self._get_max_memory_allocated()
            stage.peak_memory = max(stage.peak_memory, current_peak)
            
            self.events.append(stage)
            
            # If there is a parent, propagate the peak to it
            if self.stage_stack:
                parent = self.stage_stack[-1]
                parent.peak_memory = max(parent.peak_memory, stage.peak_memory)
            
            return stage
        return None

    @contextmanager
    def trace(self, name: str):
        self.start_stage(name)
        try:
            yield
        finally:
            self.end_stage()

    def save_report(self, filename, args=None):
        report = self.get_report(args)
        
        # Ensure directory exists
        if os.path.dirname(filename):
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            
        try:
            with open(filename, 'w') as f:
                json.dump(report, f, indent=4)
            logging.info(f"Performance report saved to {filename}")
        except Exception as e:
            logging.error(f"Failed to save performance report: {e}")

    def get_report(self, args=None):
        report = {
            "system_info": self.system_info,
            "total_duration": time.time() - self.start_time,
            "stages": []
        }
        
        if args:
            # Safely serialize args
            config_info = {}
            for k, v in vars(args).items():
                if isinstance(v, (str, int, float, bool, list, tuple)):
                    config_info[k] = v
            report["config"] = config_info

        max_mem_used = 0
        
        for stage in self.events:
            stage_data = {
                "name": stage.name,
                "duration": stage.duration,
                "memory_delta_mb": stage.memory_delta / (1024**2),
                "peak_memory_mb": stage.peak_memory / (1024**2),
                "activation_memory_mb": stage.activation_memory / (1024**2),
                "gpu_utilization": stage.gpu_utilization,
                "sm_activity": stage.sm_activity,
                "tensor_core_utilization": stage.tensor_core_utilization,
                "cpu_utilization": stage.cpu_utilization,
                "system_memory_peak_gb": stage.system_memory_peak / (1024**3),
                "compute_efficiency_gflops_proxy": stage.compute_efficiency
            }
            report["stages"].append(stage_data)
            max_mem_used = max(max_mem_used, stage.peak_memory)
            
        report["max_memory_used_mb"] = max_mem_used / (1024**2)
        return report
