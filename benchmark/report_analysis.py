import json
import os
import glob
import sys

def analyze_reports(report_dir="benchmark/reports", output_file="benchmark_report.md", summary_data=None):
    json_files = sorted(glob.glob(os.path.join(report_dir, "*.json")))
    
    if not json_files:
        print("No report files found.")
        return

    # If summary_data is not provided, reconstruct it from JSONs
    if not summary_data:
        summary_data = []
        for json_file in json_files:
            try:
                with open(json_file, 'r') as f:
                    data = json.load(f)
                
                # Try to extract args from filename or data if available
                # Note: This is a best-effort reconstruction. 
                # Ideally, run.py should pass the exact args.
                case_name = os.path.basename(json_file).replace(".json", "")
                
                stages = data.get("stages", [])
                total_dur = data.get("total_duration", 0)
                peak_mem = max([s.get("peak_memory_mb", 0) for s in stages]) / 1024 if stages else 0
                total_load = sum([s.get("compute_load", 0) for s in stages])
                
                inference_stages = [s for s in stages if 'Inference' in s['stage']]
                steps = len(inference_stages)
                total_infer_time = sum(s['duration_sec'] for s in inference_stages)
                s_per_step = total_infer_time / steps if steps > 0 else 0
                
                sm_values = [s.get('sm_activity', 0) for s in inference_stages]
                avg_sm = sum(sm_values) / len(sm_values) if sm_values else 0
                
                # Guess resolution/offload from name if not in json
                # (Future improvement: save args in report json)
                res = "1280*704" # Default for this run
                offload = "Unknown"
                if "Speed_Preview" in case_name or "Efficiency" in case_name:
                    offload = True
                elif "Performance" in case_name:
                    offload = False
                
                summary_data.append({
                    "Case": case_name,
                    "Res": res,
                    "Steps": steps,
                    "Offload": offload,
                    "Time(s)": total_dur,
                    "Speed(s/step)": s_per_step,
                    "PeakMem(GB)": peak_mem,
                    "Avg SM(%)": avg_sm,
                    "CompLoad": total_load
                })
            except Exception as e:
                print(f"Error processing summary for {json_file}: {e}")

    # 1. Generate Summary Content
    unified_content = "# Wan2.2 Benchmark Report\n\n"
    
    if summary_data:
        # Generate Summary Table from data
        header = f"| {'Case':<22} | {'Res':<10} | {'Offload':<7} | {'Time(s)':>8} | {'s/step':>6} | {'Mem(GB)':>7} | {'SM(%)':>5} | {'Load':>6} |"
        unified_content += header + "\n"
        unified_content += "|" + "-"*24 + "|" + "-"*12 + "|" + "-"*9 + "|" + "-"*10 + "|" + "-"*8 + "|" + "-"*9 + "|" + "-"*7 + "|" + "-"*8 + "|" + "\n"
        
        for r in summary_data:
            line = f"| {r['Case']:<22} | {r['Res']:<10} | {str(r['Offload']):<7} | {r['Time(s)']:>8.2f} | {r['Speed(s/step)']:>6.2f} | {r['PeakMem(GB)']:>7.2f} | {r['Avg SM(%)']:>5.1f} | {r['CompLoad']:>6.0f} |"
            unified_content += line + "\n"
        unified_content += "\n"
    
    unified_content += "# Detailed Breakdown\n\n"
    
    # 2. Generate Detailed Analysis
    for json_file in json_files:
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
        except Exception as e:
            print(f"Error reading {json_file}: {e}")
            continue
            
        case_name = os.path.basename(json_file).replace(".json", "")
        stages = data.get("stages", [])
        total_duration = data.get("total_duration", 0)
        
        # Calculate summary stats
        peak_mem_gb = max([s.get("peak_memory_mb", 0) for s in stages]) / 1024 if stages else 0
        total_load = sum([s.get("compute_load", 0) for s in stages])
        
        # Section Header
        unified_content += f"## Case: {case_name}\n\n"
        unified_content += f"- **Total Duration**: {total_duration:.2f} s\n"
        unified_content += f"- **Peak GPU Memory**: {peak_mem_gb:.2f} GB\n"
        unified_content += f"- **Total Compute Load**: {total_load:.0f}\n\n"
        
        # Detailed Table
        unified_content += "### Stage Breakdown\n\n"
        header = "| Stage | Time (s) | GPU Mem (GB) | CPU (%) | Sys Mem (GB) | SM Act (%) | Comp Load |\n"
        separator = "| :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n"
        unified_content += header + separator
        
        inference_steps = []
        
        for stage in stages:
            name = stage.get("stage", "Unknown")
            duration = stage.get("duration_sec", 0)
            mem_mb = stage.get("peak_memory_mb", 0)
            sm = stage.get("sm_activity", 0)
            load = stage.get("compute_load", 0)
            cpu = stage.get("cpu_utilization", 0)
            sys_mem_gb = stage.get("system_memory_peak_gb", 0)
            
            # Formatting
            mem_gb = mem_mb / 1024
            
            row = f"| {name} | {duration:.2f} | {mem_gb:.2f} | {cpu:.1f} | {sys_mem_gb:.2f} | {sm:.1f} | {load:.0f} |\n"
            unified_content += row
            
            if "Inference" in name:
                inference_steps.append(stage)

        unified_content += "\n"
        
        # Inference Statistics
        if inference_steps:
            avg_step_time = sum(s['duration_sec'] for s in inference_steps) / len(inference_steps)
            avg_step_sm = sum(s['sm_activity'] for s in inference_steps) / len(inference_steps)
            avg_step_cpu = sum(s.get('cpu_utilization', 0) for s in inference_steps) / len(inference_steps)
            total_step_load = sum(s['compute_load'] for s in inference_steps)
            
            unified_content += "### Inference Statistics\n\n"
            unified_content += f"- **Avg Time per Step**: {avg_step_time:.2f} s\n"
            unified_content += f"- **Avg SM Activity**: {avg_step_sm:.1f} %\n"
            unified_content += f"- **Avg CPU Utilization**: {avg_step_cpu:.1f} %\n"
            unified_content += f"- **Total Inference Load**: {total_step_load:.0f}\n\n"
            
        # Automated Analysis
        unified_content += "### Performance Analysis\n\n"
        
        # 1. Bottleneck Identification
        bottlenecks = []
        if total_duration > 0:
            avg_sm_total = sum(s.get('sm_activity', 0) * s.get('duration_sec', 0) for s in stages) / total_duration
            if avg_sm_total < 80:
                bottlenecks.append(f"Low overall GPU utilization ({avg_sm_total:.1f}%), suggesting potential CPU bottlenecks or data loading overhead.")
        
        # Check specific stages
        for stage in stages:
            if "Inference" in stage.get("stage", "") and stage.get("sm_activity", 0) < 90:
                bottlenecks.append(f"Inference stage '{stage['stage']}' has low SM activity ({stage['sm_activity']}%), check kernel efficiency.")
        
        if bottlenecks:
            unified_content += "**Bottlenecks Detected:**\n"
            for b in bottlenecks:
                unified_content += f"- {b}\n"
            unified_content += "\n"
        else:
            unified_content += "No significant bottlenecks detected. GPU utilization is healthy.\n\n"
            
        # 2. Resource Usage
        unified_content += "**Resource Usage Overview:**\n"
        unified_content += f"- Peak GPU Memory reached {peak_mem_gb:.2f} GB. "
        if peak_mem_gb > 40:
             unified_content += "High VRAM usage, close to 48GB limit on L40S.\n"
        else:
             unified_content += "VRAM usage is within safe margins.\n"
             
        unified_content += "---\n\n"

    # 3. Write Unified Report
    with open(output_file, "w") as f:
        f.write(unified_content)
    
    print(f"Unified benchmark report saved to {output_file}")

    # Optional: Remove the separate files if desired, but keeping them is fine too.

if __name__ == "__main__":
    analyze_reports()
