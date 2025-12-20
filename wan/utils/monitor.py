import time
import json
import torch
import logging
import threading
import subprocess
import sys
import os
import os

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
        
        # Try DCGM first
        if DCGM_AVAILABLE:
            try:
                # Connect to DCGM host engine (assumes it's running)
                dcgm_agent.dcgmInit()
                self.dcgm_handle = dcgm_agent.dcgmConnect("127.0.0.1:5555")
                
                # Create a group
                device_index = torch.cuda.current_device() if torch.cuda.is_available() else 0
                group_name = f"wan_monitor_group_{str(time.time())}"
                self.dcgm_group = dcgm_agent.dcgmGroupCreate(self.dcgm_handle, dcgm_structs.DCGM_GROUP_EMPTY, group_name)
                
                # Add GPU to group
                dcgm_agent.dcgmGroupAddEntity(self.dcgm_handle, self.dcgm_group, dcgm_fields.DCGM_FE_GPU, device_index)
                
                # Watch SM Activity field
                self.sm_field_id = dcgm_fields.DCGM_FI_PROF_SM_ACTIVE
                update_freq = 100000 # 100ms in microseconds
                max_keep_age = 3600.0
                max_keep_samples = 0
                
                dcgm_agent.dcgmWatchFields(self.dcgm_handle, self.dcgm_group, 
                                          [self.sm_field_id], 
                                          update_freq, max_keep_age, max_keep_samples)
                
                self.using_dcgm = True
                self.sm_thread = threading.Thread(target=self._monitor_sm_loop_dcgm, daemon=True)
                self.sm_thread.start()
                logging.info("DCGM SM Activity monitoring initialized successfully.")
                return
            except Exception as e:
                logging.warning(f"Failed to initialize DCGM SM monitor: {e}. Falling back to nvidia-smi dmon.")
                self.dcgm_handle = None
                self.dcgm_group = None

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
        if not hasattr(self, 'dcgm_handle') or not self.dcgm_handle:
            return
            
        device_index = torch.cuda.current_device() if torch.cuda.is_available() else 0
        
        while self.running:
            try:
                dcgm_agent.dcgmUpdateAllFields(self.dcgm_handle, 1)
                values = dcgm_agent.dcgmGetLatestValues(self.dcgm_handle, self.dcgm_group, self.sm_field_id)
                
                for val in values:
                    if val.entityId == device_index and val.fieldId == self.sm_field_id:
                        if val.status == 0: # DCGM_ST_OK
                            # SM Active is a ratio (0.0 - 1.0)
                            sm_val = val.value.dbl * 100.0
                            self.sm_samples.append((time.time(), sm_val))
                        break
            except Exception as e:
                pass
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
            if self.gpu_handle:
                try:
                    util = pynvml.nvmlDeviceGetUtilizationRates(self.gpu_handle)
                    self.gpu_samples.append((time.time(), util.gpu))
                except:
                    pass
            time.sleep(0.05) # 50ms sampling

    def __del__(self):
        self.running = False
        
        # Cleanup DCGM
        if hasattr(self, 'dcgm_handle') and self.dcgm_handle:
            try:
                if hasattr(self, 'dcgm_group') and self.dcgm_group:
                    dcgm_agent.dcgmGroupDestroy(self.dcgm_handle, self.dcgm_group)
                dcgm_agent.dcgmDisconnect(self.dcgm_handle)
            except:
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
        # Only reset peak stats if this is a top-level stage or we want to track peak within this specific stage
        # However, resetting peak stats affects global state. 
        # For nested stages, resetting peak stats might hide peaks from parent stages if not careful.
        # But we want accurate peak for *this* stage.
        # Strategy: Record current peak so far? No, simply reset is the standard way to measure peak *during* a window.
        # But for nested:
        # Parent Start -> Reset -> 0
        #   Child Start -> Reset -> 0 (Parent's peak history lost!)
        # So we cannot easily nest peak memory tracking using reset_peak_memory_stats() naively.
        #
        # Better approach: Read max_memory_allocated() at end, but we need to know the baseline.
        # 
        # If we want to support nesting, we should probably NOT reset peak stats on every start,
        # OR we accept that 'peak_memory' is only valid for the innermost active stage if we reset.
        # 
        # Given the requirement, I will stick to a stack but be careful about resetting.
        # Actually, for "Activation Memory", we want the peak delta.
        # 
        # Let's use a simpler approach: 
        # We will NOT reset peak memory stats on nested calls. Only on top level?
        # Or simply don't reset and just record `torch.cuda.max_memory_allocated()`. 
        # But `max_memory_allocated` is monotonic increasing unless reset.
        # If we don't reset, `peak` will be the global peak since last reset.
        
        # Compromise: We reset peak stats when starting a stage, but we need to handle the parent.
        # Actually, for this task, the nesting is: Total -> [Preprocess, Encoding, Loop -> [Step]].
        # The steps are sequential, not nested deep inside each other (except inside the loop).
        # The "Total" wraps everything.
        # If I reset at "Total" start, then "Step 1" start resets again, "Total" loses its peak info.
        
        # Modified Logic:
        # We will maintain the stack.
        # We will ONLY reset peak stats if the stack is empty (fresh start) or if explicitly requested.
        # BUT, if we don't reset for inner stages, we can't measure the peak *specific* to that inner stage if a previous stage had a higher peak.
        # 
        # Solution: 
        # We will reset peak stats at every start_stage.
        # When a child stage finishes, we must bubble up its peak memory to the parent.
        # Parent.peak = max(Parent.peak, Child.peak)
        
        if torch.cuda.is_available():
             torch.cuda.synchronize()
        
        # Before resetting, if there is a parent, update its peak so far? 
        # No, because we are about to reset the counter. The hardware counter is global.
        # If we reset, the parent's view of "max memory since parent start" is cleared.
        # So we must store the "max memory seen so far" in the parent object manually.
        
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
                    # If duration < 1s, we might not have samples. 
                    # Try to take the last known sample before end_time if close enough?
                    # Or just 0.
                    stage.sm_activity = 0.0

            # Capture the peak observed during *this* stage execution (since its start)
            current_peak = self._get_max_memory_allocated()
            stage.peak_memory = max(stage.peak_memory, current_peak)
            
            self.events.append(stage)
            
            # If there is a parent, propagate the peak to it
            if self.stage_stack:
                parent = self.stage_stack[-1]
                parent.peak_memory = max(parent.peak_memory, stage.peak_memory)
                
                # Also, we need to consider that the 'reset' happened at the start of this child.
                # So the 'peak' we just measured is valid. 
                # But for the parent, there might have been a higher peak *before* the child started.
                # We handled that in start_stage by saving `current_max` to parent.
                # So parent.peak_memory is now max(peak_before_child, peak_during_child).
                # This seems correct.
            
            return stage
        return None

    @contextmanager
    def trace(self, name: str):
        self.start_stage(name)
        try:
            yield
        finally:
            self.end_stage()

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
                "stage": stage.name,
                "duration_sec": round(stage.duration, 4),
                "start_memory_mb": round(stage.start_memory / (1024**2), 2),
                "end_memory_mb": round(stage.end_memory / (1024**2), 2),
                "peak_memory_mb": round(stage.peak_memory / (1024**2), 2),
                "memory_delta_mb": round(stage.memory_delta / (1024**2), 2),
                "activation_memory_estimate_mb": round(stage.activation_memory / (1024**2), 2),
                "gpu_utilization": round(stage.gpu_utilization, 2),
                "sm_activity": round(stage.sm_activity, 2),
                "compute_efficiency": round(stage.compute_efficiency, 2),
                "compute_load": round(stage.compute_load, 2)
            }
            report["stages"].append(stage_data)
            max_mem_used = max(max_mem_used, stage.peak_memory)

        report["max_memory_used_gb"] = round(max_mem_used / (1024**3), 2)
        return report

    def save_report(self, filepath: str, args=None):
        report = self.get_report(args)
        try:
            with open(filepath, 'w') as f:
                json.dump(report, f, indent=4)
            logging.info(f"Performance report saved to {filepath}")
        except Exception as e:
            logging.error(f"Failed to save performance report: {e}")
