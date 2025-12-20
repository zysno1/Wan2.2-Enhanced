import json
import argparse
import sys
import math

def format_report(report_path):
    with open(report_path, 'r') as f:
        data = json.load(f)

    stages = data.get('stages', [])
    config = data.get('config', {})
    system_info = data.get('system_info', {})

    # ==============================================================================
    # 1. System & Context
    # ==============================================================================
    gpu_name = "Unknown GPU"
    gpu_mem = 0
    if system_info.get('gpu_info'):
        gpu_name = system_info['gpu_info'].get('name', 'Unknown')
        gpu_mem = system_info['gpu_info'].get('total_memory_gb', 0)
    
    cuda_ver = system_info.get('cuda_version', 'N/A')
    torch_ver = system_info.get('pytorch_version', 'N/A')

    # Config parsing
    task_name = config.get('task', 'Unknown')
    size_str = config.get('size', 'Unknown')
    frames = config.get('frame_num', 0)
    steps = config.get('sample_steps', 0)
    offload = config.get('offload_model', False)
    precision = "BF16" if "bf16" in str(config).lower() else "FP16/FP32" # Heuristic

    # ==============================================================================
    # 2. Performance Metrics Calculation
    # ==============================================================================
    
    # Latency Breakdown
    total_time = data.get('total_duration', 0)
    
    # Initialization (Model Load + Preprocess)
    init_stages = [s for s in stages if 'Initialization' in s['stage'] or 'Loading' in s['stage']]
    init_time = sum(s['duration_sec'] for s in init_stages)
    
    # Text Encoder (T5)
    t5_stages = [s for s in stages if 'T5' in s['stage']]
    t5_time = sum(s['duration_sec'] for s in t5_stages)
    
    # Denoising (DiT) - The Core Loop
    dit_stages = [s for s in stages if 'Inference' in s['stage'] and 'Step' in s['stage']]
    dit_total_time = sum(s['duration_sec'] for s in dit_stages)
    avg_step_time = dit_total_time / len(dit_stages) if dit_stages else 0
    steps_per_sec = 1.0 / avg_step_time if avg_step_time > 0 else 0
    
    # First Step Latency (Compilation Overhead)
    first_step_time = 0
    if dit_stages:
        first_step_time = dit_stages[0]['duration_sec']

    # VAE Decoding
    vae_stages = [s for s in stages if 'VAE' in s['stage']]
    vae_time = sum(s['duration_sec'] for s in vae_stages)
    
    # Throughput
    # Video Frames Per Second (Generation only, excluding init)
    generation_only_time = t5_time + dit_total_time + vae_time
    video_fps = frames / generation_only_time if generation_only_time > 0 else 0
    
    # Pixel Throughput (Megapixels / sec)
    try:
        w, h = map(int, size_str.replace('*', 'x').split('x'))
        pixels = w * h
        mpx_throughput = (pixels * frames) / generation_only_time / 1e6 if generation_only_time > 0 else 0
    except:
        mpx_throughput = 0

    # ==============================================================================
    # 3. Memory Profiling
    # ==============================================================================
    global_peak_mb = max((s['peak_memory_mb'] for s in stages), default=0)
    global_peak_gb = global_peak_mb / 1024
    
    # DiT Memory (Resident vs Dynamic)
    # Finding DiT Base (Resident) by looking for the jump before Step 0
    dit_base_mb = 0
    for i in range(len(stages)-1):
        prev = stages[i]
        curr = stages[i+1]
        if 'Step_0' in curr['stage']:
            diff = curr['start_memory_mb'] - prev['end_memory_mb']
            if diff > 1000: # Assuming jump > 1GB is the model
                dit_base_mb = diff
                break
    
    dit_act_mb = max((s.get('activation_memory_estimate_mb', 0) for s in dit_stages), default=0)

    # T5 Memory
    t5_peak = max((s['peak_memory_mb'] for s in t5_stages), default=0)
    # If offload=True, T5 is mostly dynamic
    t5_mem_type = "Dynamic (Offloaded)" if offload else "Resident"
    
    # VAE Memory
    vae_peak = max((s['peak_memory_mb'] for s in vae_stages), default=0)

    # ==============================================================================
    # 4. Report Output (Expert Format)
    # ==============================================================================
    print("================================================================================")
    print(f"🚀 Wan2.2 Performance Analysis Report (ViT-Optimized)")
    print("================================================================================")
    print("")
    print("[System Context]")
    print(f"Device:       {gpu_name} ({gpu_mem} GB)")
    print(f"Software:     CUDA {cuda_ver} | PyTorch {torch_ver}")
    print(f"Task Config:  {task_name} | {size_str} | {frames} Frames | {steps} Steps")
    print(f"Optimization: Offload={'ON' if offload else 'OFF'} | Precision={precision}")
    print("")
    
    print("[Executive Summary]")
    print("--------------------------------------------------------------------------------")
    print(f"✅ Total Latency:       {total_time:.2f} s")
    print(f"⚡ Generation Speed:    {avg_step_time:.2f} s/step ({steps_per_sec:.2f} steps/s)")
    print(f"📹 Video Throughput:    {video_fps:.2f} frames/s ({mpx_throughput:.2f} MPx/s)")
    # GPU Utilization
    # Weighted average utilization
    total_compute_score = sum(s.get('compute_efficiency', 0) for s in stages)
    avg_gpu_util = total_compute_score / total_time if total_time > 0 else 0

    print(f"💾 Peak Memory:         {global_peak_gb:.2f} GB ({global_peak_gb/gpu_mem*100:.1f}% of VRAM)")
    print(f"🌡️  Avg GPU Activity:    {avg_gpu_util:.1f}% (Compute Score: {total_compute_score:.1f})")
    print("")
    
    print("[Detailed Pipeline Latency]")
    print("--------------------------------------------------------------------------------")
    
    def print_stage(name, time_val, total):
        pct = (time_val / total) * 100 if total > 0 else 0
        print(f"{name:<22}: {time_val:>6.2f} s ({pct:>5.1f}%)")

    print_stage("1. Initialization", init_time, total_time)
    print_stage("2. Text Encoding (T5)", t5_time, total_time)
    print_stage("3. Denoising (DiT)", dit_total_time, total_time)
    print(f"   - First Step       : {first_step_time:.2f} s")
    print(f"   - Avg Step (Stable): {avg_step_time:.2f} s")
    print_stage("4. VAE Decoding", vae_time, total_time)
    print("")
    
    print("[Memory Telemetry]")
    print("--------------------------------------------------------------------------------")
    print(f"Allocation Strategy: [{'Offload Active' if offload else 'Resident Mode'}]")
    print(f"- DiT Weights (Static): {dit_base_mb/1024:.2f} GB")
    print(f"- DiT Activation Peak : {dit_act_mb/1024:.2f} GB")
    
    if t5_peak > 0:
        t5_peak_gb = t5_peak / 1024
        print(f"- T5 Peak Usage       : {t5_peak_gb:.2f} GB ({t5_mem_type})")
    
    if vae_peak > 0:
        vae_peak_gb = vae_peak / 1024
        print(f"- VAE Peak Usage      : {vae_peak_gb:.2f} GB")
        
    print("")
    print("[Expert Recommendations]")
    print("--------------------------------------------------------------------------------")
    
    # Recommendations Logic
    if init_time > total_time * 0.5:
        print(f"> ⚠️ Model loading takes {init_time/total_time*100:.1f}% of total time.")
        print("     Action: Keep model loaded (server mode) to eliminate this overhead.")
        
    if offload:
        print("> ℹ️ Offloading is active. This reduces VRAM but may increase latency slightly due to PCI-e transfers.")
        if global_peak_gb < gpu_mem * 0.5:
             print("     Action: You have plenty of VRAM. Disable offloading (--offload_model False) for faster generation.")
    
    if steps_per_sec < 1.0:
        print("> ℹ️ Step speed is < 1 step/s. Consider using Flash Attention 2 or FP8 quantization if supported.")

    print("")
    print("[Execution Trace Analysis]")
    print("-" * 145)
    print(f"{'Stage Name':<25} | {'Time (s)':>8} | {'SM %':>5} | {'Load':>6} | {'Mem Start':>9} | {'Mem End':>9} | {'Peak Mem':>9} | {'Mem Δ':>9} | {'Comment'}")
    print("-" * 145)
    
    # Trace Loop
    prev_mem = 0
    for s in stages:
        name = s['stage'].replace('Step_', 'S').replace('_Inference', '') # Abbreviate for table
        if len(name) > 25: name = name[:22] + "..."
        
        dur = s['duration_sec']
        sm = s.get('sm_activity', 0)
        load = s.get('compute_load', 0)
        
        start_mem = s['start_memory_mb'] / 1024
        end_mem = s['end_memory_mb'] / 1024
        peak_mem = s['peak_memory_mb'] / 1024
        delta = s['memory_delta_mb'] / 1024
        
        # Heuristic Comment
        comment = ""
        if "Loading" in s['stage'] and delta > 1.0:
            comment = "Model Load"
        elif "Inference" in s['stage'] and sm > 80:
            comment = "Compute Heavy"
        elif "VAE" in s['stage']:
            comment = "Decoding"
        elif "T5" in s['stage']:
            comment = "Text Enc"
        elif "Initialization" in s['stage']:
            comment = "Sys Init"
            
        if offload and "Loading" in s['stage'] and delta < 0.1:
             comment = "Cached/NoOp"

        print(f"{name:<25} | {dur:>8.2f} | {sm:>5.1f} | {load:>6.1f} | {start_mem:>9.2f} | {end_mem:>9.2f} | {peak_mem:>9.2f} | {delta:>9.2f} | {comment}")

    print("-" * 145)
    print("Legend: SM% = SM Activity | Load = Duration * SM% | Mem values in GB")
    print("================================================================================")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('report_file', help='Path to JSON report file')
    args = parser.parse_args()
    format_report(args.report_file)
