import json
import os
import subprocess
import sys
import time
from glob import glob

def run_benchmark(config_path="benchmark/config.json"):
    # 1. Load Configuration
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    global_settings = config.get("global_settings", {})
    test_cases = config.get("test_cases", [])
    
    print(f"🚀 Starting Benchmark Suite: {len(test_cases)} cases")
    print("="*60)
    
    results = []
    
    # Ensure reports directory exists
    os.makedirs("benchmark/reports", exist_ok=True)
    
    # Define boolean flags (action='store_true') based on generate.py
    BOOLEAN_FLAGS = {
        "t5_fsdp", "t5_cpu", "dit_fsdp", "use_prompt_extend", 
        "convert_model_dtype", "replace_flag", "use_relighting_lora",
        "enable_tts", "start_from_ref"
    }
    
    # 2. Execute Test Cases
    for case in test_cases:
        case_name = case['name']
        print(f"\n▶️  Running Case: {case_name}")
        print(f"   Description: {case.get('description', '')}")
        
        # Merge args
        args = case['args']
        cmd = [sys.executable, "generate.py"]
        
        # Add global settings
        cmd.extend(["--task", global_settings.get("task", "t2v-A14B")])
        cmd.extend(["--ckpt_dir", global_settings.get("ckpt_dir", "")])
        cmd.extend(["--prompt", global_settings.get("prompt", "")])
        if "base_seed" in global_settings:
            cmd.extend(["--base_seed", str(global_settings["base_seed"])])
            
        # Add case specific args
        for k, v in args.items():
            if k in BOOLEAN_FLAGS:
                if v: # Only add flag if True
                    cmd.append(f"--{k}")
            else:
                # Handle standard args (including offload_model which is str2bool)
                cmd.extend([f"--{k}", str(v)])
                
        # Set report file
        report_file = os.path.abspath(f"benchmark/reports/{case_name}.json")
        cmd.extend(["--report_file", report_file])
        
        # Run command
        try:
            start_time = time.time()
            subprocess.run(cmd, check=True)
            end_time = time.time()
            print(f"   ✅ Finished in {end_time - start_time:.2f}s")
            
            # 3. Analyze Result
            if os.path.exists(report_file):
                with open(report_file, 'r') as f:
                    report_data = json.load(f)
                
                # Extract key metrics
                stages = report_data.get('stages', [])
                total_dur = report_data.get('total_duration', 0)
                peak_mem = report_data.get('max_memory_used_gb', 0)
                
                # Calculate Inference Speed (s/step)
                inference_stages = [s for s in stages if 'Inference' in s['stage']]
                total_infer_time = sum(s['duration_sec'] for s in inference_stages)
                steps = args.get('sample_steps', 0)
                s_per_step = total_infer_time / steps if steps > 0 else 0
                
                # Calculate Compute Load
                total_load = sum(s.get('compute_load', 0) for s in stages)
                
                # Calculate Average SM Activity during Inference
                sm_values = [s.get('sm_activity', 0) for s in inference_stages]
                avg_sm = sum(sm_values) / len(sm_values) if sm_values else 0
                
                results.append({
                    "Case": case_name,
                    "Res": args.get('size'),
                    "Steps": steps,
                    "Offload": args.get('offload_model'),
                    "Time(s)": total_dur,
                    "Speed(s/step)": s_per_step,
                    "PeakMem(GB)": peak_mem,
                    "Avg SM(%)": avg_sm,
                    "CompLoad": total_load
                })
                
                # Generate detailed text report
                txt_report_path = f"benchmark/reports/{case_name}.txt"
                with open(txt_report_path, "w") as tf:
                    subprocess.run([sys.executable, "format_report.py", report_file], stdout=tf)
                
            else:
                print("   ❌ Report file not found!")
                
        except subprocess.CalledProcessError as e:
            print(f"   ❌ Failed: {e}")
        except Exception as e:
            print(f"   ❌ Error: {e}")

    # 4. Generate Summary Report
    print("\n" + "="*80)
    print("📊 BENCHMARK SUMMARY")
    print("="*80)
    
    # Markdown Table
    header = f"| {'Case':<22} | {'Res':<10} | {'Offload':<7} | {'Time(s)':>8} | {'s/step':>6} | {'Mem(GB)':>7} | {'SM(%)':>5} | {'Load':>6} |"
    print(header)
    print("|" + "-"*24 + "|" + "-"*12 + "|" + "-"*9 + "|" + "-"*10 + "|" + "-"*8 + "|" + "-"*9 + "|" + "-"*7 + "|" + "-"*8 + "|")
    
    summary_md = "# Wan2.2 Benchmark Report\n\n" + header + "\n" + "|" + "-"*24 + "|" + "-"*12 + "|" + "-"*9 + "|" + "-"*10 + "|" + "-"*8 + "|" + "-"*9 + "|" + "-"*7 + "|" + "-"*8 + "|" + "\n"
    
    for r in results:
        line = f"| {r['Case']:<22} | {r['Res']:<10} | {str(r['Offload']):<7} | {r['Time(s)']:>8.2f} | {r['Speed(s/step)']:>6.2f} | {r['PeakMem(GB)']:>7.2f} | {r['Avg SM(%)']:>5.1f} | {r['CompLoad']:>6.0f} |"
        print(line)
        summary_md += line + "\n"
        
    with open("benchmark_summary.md", "w") as f:
        f.write(summary_md)
    print("\n✅ Summary saved to benchmark_summary.md")

    # 5. Generate Detailed Analysis
    print("\nGenerating detailed analysis...")
    try:
        from benchmark.report_analysis import analyze_reports
        analyze_reports()
    except ImportError:
        # Fallback if running from a different cwd or module path issues
        subprocess.run([sys.executable, "benchmark/report_analysis.py"])
    except Exception as e:
        print(f"Failed to generate detailed analysis: {e}")

if __name__ == "__main__":
    run_benchmark()
