import json
import os
import glob
import sys

def analyze_reports(report_dir="benchmark/reports", output_file="benchmark_report.md", summary_file="benchmark_summary.md"):
    json_files = sorted(glob.glob(os.path.join(report_dir, "*.json")))
    
    if not json_files:
        print("No report files found.")
        return

    # 1. Read Summary Content
    unified_content = ""
    if os.path.exists(summary_file):
        try:
            with open(summary_file, 'r') as f:
                unified_content = f.read()
            unified_content += "\n\n"
        except Exception as e:
            print(f"Warning: Could not read summary file: {e}")
            unified_content = "# Wan2.2 Benchmark Report\n\n"
    else:
        unified_content = "# Wan2.2 Benchmark Report\n\n"

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
        unified_content += f"- **Peak Memory**: {peak_mem_gb:.2f} GB\n"
        unified_content += f"- **Total Compute Load**: {total_load:.0f}\n\n"
        
        # Detailed Table
        unified_content += "### Stage Breakdown\n\n"
        header = "| Stage | Time (s) | Peak Mem (GB) | SM Act (%) | Comp Load |\n"
        separator = "| :--- | :--- | :--- | :--- | :--- |\n"
        unified_content += header + separator
        
        inference_steps = []
        
        for stage in stages:
            name = stage.get("stage", "Unknown")
            duration = stage.get("duration_sec", 0)
            mem_mb = stage.get("peak_memory_mb", 0)
            sm = stage.get("sm_activity", 0)
            load = stage.get("compute_load", 0)
            
            # Formatting
            mem_gb = mem_mb / 1024
            
            row = f"| {name} | {duration:.2f} | {mem_gb:.2f} | {sm:.1f} | {load:.0f} |\n"
            unified_content += row
            
            if "Inference" in name:
                inference_steps.append(stage)

        unified_content += "\n"
        
        # Inference Analysis (if steps exist)
        if inference_steps:
            avg_step_time = sum(s['duration_sec'] for s in inference_steps) / len(inference_steps)
            avg_step_sm = sum(s['sm_activity'] for s in inference_steps) / len(inference_steps)
            total_step_load = sum(s['compute_load'] for s in inference_steps)
            
            unified_content += "### Inference Statistics\n\n"
            unified_content += f"- **Avg Time per Step**: {avg_step_time:.2f} s\n"
            unified_content += f"- **Avg SM Activity**: {avg_step_sm:.1f} %\n"
            unified_content += f"- **Total Inference Load**: {total_step_load:.0f}\n\n"
            
        unified_content += "---\n\n"

    # 3. Write Unified Report
    with open(output_file, "w") as f:
        f.write(unified_content)
    
    print(f"Unified benchmark report saved to {output_file}")

    # Optional: Remove the separate files if desired, but keeping them is fine too.

if __name__ == "__main__":
    analyze_reports()
