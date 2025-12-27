# Wan2.2 Benchmark Report

| Case                   | Res        | Offload |  Time(s) | s/step | Mem(GB) | SM(%) |   Load |
|------------------------|------------|---------|----------|--------|---------|-------|--------|
| 01_Speed_Preview_704p  | 1280*704   | True    |   125.39 |   6.88 |   31.27 |  98.5 |      0 |
| 02_Efficiency_Quality_704p | 1280*704   | True    |   295.03 |   6.88 |   31.27 |  99.8 |      0 |
| 03_Max_Quality_704p    | 1280*704   | False   |   420.81 |   6.88 |   52.76 |  99.8 |      0 |
| 04_15s_50steps_720p    | 1280*704   | True    |  1238.48 |  22.32 |   43.46 |  99.9 |      0 |

# Detailed Breakdown

## Case: 01_5B_Speed_Preview_704p

- **Total Duration**: 143.25 s
- **Peak GPU Memory**: 31.27 GB
- **Total Compute Load**: 11546

### Stage Breakdown

| Stage | Time (s) | GPU Mem (GB) | CPU (%) | Sys Mem (GB) | SM Act (%) | Comp Load |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Unknown | 0.00 | 2.63 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 2.63 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 2.63 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 21.34 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.12 | 0.0 | 0.00 | 100.0 | 710 |
| Unknown | 0.00 | 21.48 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.22 | 0.0 | 0.00 | 100.0 | 684 |
| Unknown | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.27 | 0.0 | 0.00 | 100.0 | 690 |
| Unknown | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.27 | 0.0 | 0.00 | 97.1 | 665 |
| Unknown | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.27 | 0.0 | 0.00 | 100.0 | 685 |
| Unknown | 0.00 | 23.54 | 0.0 | 0.00 | 96.4 | 2299 |
| Unknown | 0.00 | 31.27 | 0.0 | 0.00 | 40.6 | 5813 |

### Performance Analysis

No significant bottlenecks detected. GPU utilization is healthy.

**Resource Usage Overview:**
- Peak GPU Memory reached 31.27 GB. VRAM usage is within safe margins.
---

## Case: 01_Speed_Preview_480p

- **Total Duration**: 114.94 s
- **Peak GPU Memory**: 31.27 GB
- **Total Compute Load**: 11672

### Stage Breakdown

| Stage | Time (s) | GPU Mem (GB) | CPU (%) | Sys Mem (GB) | SM Act (%) | Comp Load |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Unknown | 0.00 | 2.63 | 5.8 | 301.34 | 0.0 | 0 |
| Unknown | 0.00 | 2.63 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 2.63 | 14.9 | 298.49 | 0.0 | 0 |
| Unknown | 0.00 | 21.34 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.12 | 5.1 | 298.61 | 99.4 | 695 |
| Unknown | 0.00 | 21.48 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.22 | 5.9 | 298.43 | 100.0 | 683 |
| Unknown | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.27 | 5.8 | 298.41 | 100.0 | 686 |
| Unknown | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.27 | 9.4 | 300.61 | 100.0 | 684 |
| Unknown | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.27 | 4.1 | 300.37 | 99.7 | 682 |
| Unknown | 0.00 | 23.54 | 3.4 | 318.29 | 100.0 | 2374 |
| Unknown | 0.00 | 31.27 | 6.3 | 318.96 | 51.1 | 5868 |

### Performance Analysis

No significant bottlenecks detected. GPU utilization is healthy.

**Resource Usage Overview:**
- Peak GPU Memory reached 31.27 GB. VRAM usage is within safe margins.
---

## Case: 01_Speed_Preview_704p

- **Total Duration**: 125.39 s
- **Peak GPU Memory**: 31.27 GB
- **Total Compute Load**: 0

### Stage Breakdown

| Stage | Time (s) | GPU Mem (GB) | CPU (%) | Sys Mem (GB) | SM Act (%) | Comp Load |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Model_Initialization | 39.07 | 2.63 | 16.1 | 155.45 | 0.0 | 0 |
| TI2V_Preprocess | 0.00 | 2.63 | 0.0 | 0.00 | 0.0 | 0 |
| T5_Encoding | 12.92 | 2.63 | 23.7 | 144.21 | 0.6 | 0 |
| Step_0_Loading | 0.00 | 21.34 | 0.0 | 0.00 | 0.0 | 0 |
| Step_0_Inference | 6.99 | 31.12 | 13.4 | 144.23 | 93.8 | 0 |
| Step_1_Loading | 0.00 | 21.48 | 0.0 | 0.00 | 0.0 | 0 |
| Step_1_Inference | 6.84 | 31.22 | 12.9 | 143.99 | 100.0 | 0 |
| Step_2_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_2_Inference | 6.88 | 31.27 | 13.1 | 143.05 | 99.8 | 0 |
| Step_3_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_3_Inference | 6.85 | 31.27 | 13.1 | 142.73 | 99.1 | 0 |
| Step_4_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_4_Inference | 6.86 | 31.27 | 13.4 | 141.76 | 100.0 | 0 |
| VAE_Decoding | 23.86 | 23.54 | 13.6 | 185.53 | 99.2 | 0 |
| Total_Execution | 120.18 | 31.27 | 15.5 | 185.53 | 49.6 | 0 |

### Inference Statistics

- **Avg Time per Step**: 6.88 s
- **Avg SM Activity**: 98.5 %
- **Avg CPU Utilization**: 13.2 %
- **Total Inference Load**: 0

### Performance Analysis

**Bottlenecks Detected:**
- Low overall GPU utilization (0.0%), suggesting potential CPU bottlenecks or data loading overhead.

**Resource Usage Overview:**
- Peak GPU Memory reached 31.27 GB. VRAM usage is within safe margins.
---

## Case: 02_5B_Efficiency_Mode_704p

- **Total Duration**: 151.58 s
- **Peak GPU Memory**: 31.27 GB
- **Total Compute Load**: 18624

### Stage Breakdown

| Stage | Time (s) | GPU Mem (GB) | CPU (%) | Sys Mem (GB) | SM Act (%) | Comp Load |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Unknown | 0.00 | 2.63 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 2.63 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 2.63 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 21.34 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.12 | 0.0 | 0.00 | 100.0 | 700 |
| Unknown | 0.00 | 21.48 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.22 | 0.0 | 0.00 | 100.0 | 684 |
| Unknown | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.27 | 0.0 | 0.00 | 99.9 | 686 |
| Unknown | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.27 | 0.0 | 0.00 | 100.0 | 685 |
| Unknown | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.27 | 0.0 | 0.00 | 100.0 | 686 |
| Unknown | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.27 | 0.0 | 0.00 | 99.3 | 681 |
| Unknown | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.27 | 0.0 | 0.00 | 99.9 | 685 |
| Unknown | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.27 | 0.0 | 0.00 | 100.0 | 686 |
| Unknown | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.27 | 0.0 | 0.00 | 100.0 | 686 |
| Unknown | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.27 | 0.0 | 0.00 | 100.0 | 686 |
| Unknown | 0.00 | 23.54 | 0.0 | 0.00 | 100.0 | 2391 |
| Unknown | 0.00 | 31.27 | 0.0 | 0.00 | 61.9 | 9368 |

### Performance Analysis

No significant bottlenecks detected. GPU utilization is healthy.

**Resource Usage Overview:**
- Peak GPU Memory reached 31.27 GB. VRAM usage is within safe margins.
---

## Case: 02_Efficiency_Mode_720p

- **Total Duration**: 187.44 s
- **Peak GPU Memory**: 31.27 GB
- **Total Compute Load**: 18702

### Stage Breakdown

| Stage | Time (s) | GPU Mem (GB) | CPU (%) | Sys Mem (GB) | SM Act (%) | Comp Load |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Unknown | 0.00 | 2.63 | 13.9 | 132.90 | 0.1 | 4 |
| Unknown | 0.00 | 2.63 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 2.63 | 22.9 | 122.48 | 0.0 | 0 |
| Unknown | 0.00 | 21.34 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.12 | 12.6 | 121.66 | 100.0 | 721 |
| Unknown | 0.00 | 21.48 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.22 | 12.9 | 121.23 | 100.0 | 684 |
| Unknown | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.27 | 12.3 | 120.96 | 100.0 | 694 |
| Unknown | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.27 | 12.3 | 121.16 | 100.0 | 685 |
| Unknown | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.27 | 12.1 | 121.60 | 99.3 | 680 |
| Unknown | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.27 | 11.8 | 120.99 | 100.0 | 686 |
| Unknown | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.27 | 7.7 | 120.02 | 100.0 | 686 |
| Unknown | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.27 | 9.0 | 122.60 | 100.0 | 686 |
| Unknown | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.27 | 13.6 | 122.35 | 100.0 | 687 |
| Unknown | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.27 | 12.1 | 121.08 | 100.0 | 687 |
| Unknown | 0.00 | 23.54 | 11.7 | 139.83 | 99.8 | 2413 |
| Unknown | 0.00 | 31.27 | 13.2 | 140.19 | 50.1 | 9390 |

### Performance Analysis

No significant bottlenecks detected. GPU utilization is healthy.

**Resource Usage Overview:**
- Peak GPU Memory reached 31.27 GB. VRAM usage is within safe margins.
---

## Case: 02_Efficiency_Quality_704p

- **Total Duration**: 295.03 s
- **Peak GPU Memory**: 31.27 GB
- **Total Compute Load**: 0

### Stage Breakdown

| Stage | Time (s) | GPU Mem (GB) | CPU (%) | Sys Mem (GB) | SM Act (%) | Comp Load |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Model_Initialization | 37.07 | 2.63 | 15.8 | 180.03 | 0.2 | 0 |
| TI2V_Preprocess | 0.00 | 2.63 | 0.0 | 0.00 | 0.0 | 0 |
| T5_Encoding | 12.73 | 2.63 | 24.4 | 146.29 | 0.3 | 0 |
| Step_0_Loading | 0.00 | 21.34 | 0.0 | 0.00 | 0.0 | 0 |
| Step_0_Inference | 6.98 | 31.12 | 16.9 | 156.79 | 96.7 | 0 |
| Step_1_Loading | 0.00 | 21.48 | 0.0 | 0.00 | 0.0 | 0 |
| Step_1_Inference | 6.84 | 31.22 | 14.5 | 156.77 | 99.8 | 0 |
| Step_2_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_2_Inference | 6.89 | 31.27 | 13.5 | 157.93 | 99.9 | 0 |
| Step_3_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_3_Inference | 6.85 | 31.27 | 15.6 | 157.44 | 100.0 | 0 |
| Step_4_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_4_Inference | 6.86 | 31.27 | 17.7 | 157.06 | 99.9 | 0 |
| Step_5_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_5_Inference | 6.86 | 31.27 | 14.2 | 157.52 | 99.9 | 0 |
| Step_6_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_6_Inference | 6.87 | 31.27 | 14.7 | 157.65 | 100.0 | 0 |
| Step_7_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_7_Inference | 6.87 | 31.27 | 13.0 | 157.86 | 100.0 | 0 |
| Step_8_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_8_Inference | 6.87 | 31.27 | 19.6 | 157.72 | 99.8 | 0 |
| Step_9_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_9_Inference | 6.88 | 31.27 | 13.0 | 157.78 | 100.0 | 0 |
| Step_10_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_10_Inference | 6.87 | 31.27 | 12.3 | 157.70 | 99.8 | 0 |
| Step_11_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_11_Inference | 6.88 | 31.27 | 13.3 | 157.04 | 99.9 | 0 |
| Step_12_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_12_Inference | 6.88 | 31.27 | 13.4 | 157.46 | 100.0 | 0 |
| Step_13_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_13_Inference | 6.88 | 31.27 | 13.0 | 157.59 | 99.9 | 0 |
| Step_14_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_14_Inference | 6.88 | 31.27 | 13.3 | 157.39 | 99.9 | 0 |
| Step_15_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_15_Inference | 6.88 | 31.27 | 13.1 | 157.74 | 100.0 | 0 |
| Step_16_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_16_Inference | 6.88 | 31.27 | 12.2 | 183.40 | 100.0 | 0 |
| Step_17_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_17_Inference | 6.87 | 31.27 | 8.8 | 183.59 | 99.9 | 0 |
| Step_18_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_18_Inference | 6.88 | 31.27 | 13.8 | 159.78 | 100.0 | 0 |
| Step_19_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_19_Inference | 6.88 | 31.27 | 12.9 | 159.55 | 99.8 | 0 |
| Step_20_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_20_Inference | 6.88 | 31.27 | 13.1 | 159.31 | 100.0 | 0 |
| Step_21_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_21_Inference | 6.88 | 31.27 | 13.4 | 158.52 | 99.9 | 0 |
| Step_22_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_22_Inference | 6.88 | 31.27 | 14.4 | 158.67 | 99.8 | 0 |
| Step_23_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_23_Inference | 6.88 | 31.27 | 16.3 | 158.39 | 100.0 | 0 |
| Step_24_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_24_Inference | 6.88 | 31.27 | 12.6 | 157.78 | 99.9 | 0 |
| Step_25_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_25_Inference | 6.88 | 31.27 | 12.7 | 157.63 | 100.0 | 0 |
| Step_26_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_26_Inference | 6.88 | 31.27 | 13.5 | 157.63 | 99.8 | 0 |
| Step_27_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_27_Inference | 6.88 | 31.27 | 12.1 | 157.63 | 100.0 | 0 |
| Step_28_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_28_Inference | 6.88 | 31.27 | 13.0 | 157.12 | 100.0 | 0 |
| Step_29_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_29_Inference | 6.88 | 31.27 | 13.1 | 157.14 | 99.8 | 0 |
| VAE_Decoding | 23.95 | 23.54 | 12.9 | 201.86 | 98.5 | 0 |
| Total_Execution | 289.85 | 31.27 | 14.4 | 201.86 | 80.1 | 0 |

### Inference Statistics

- **Avg Time per Step**: 6.88 s
- **Avg SM Activity**: 99.8 %
- **Avg CPU Utilization**: 13.8 %
- **Total Inference Load**: 0

### Performance Analysis

**Bottlenecks Detected:**
- Low overall GPU utilization (0.0%), suggesting potential CPU bottlenecks or data loading overhead.

**Resource Usage Overview:**
- Peak GPU Memory reached 31.27 GB. VRAM usage is within safe margins.
---

## Case: 03_5B_Performance_Mode_704p

- **Total Duration**: 146.27 s
- **Peak GPU Memory**: 42.17 GB
- **Total Compute Load**: 18587

### Stage Breakdown

| Stage | Time (s) | GPU Mem (GB) | CPU (%) | Sys Mem (GB) | SM Act (%) | Comp Load |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Unknown | 0.00 | 2.63 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 2.63 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 2.63 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 21.34 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.12 | 0.0 | 0.00 | 100.0 | 702 |
| Unknown | 0.00 | 21.48 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.22 | 0.0 | 0.00 | 100.0 | 684 |
| Unknown | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.27 | 0.0 | 0.00 | 100.0 | 688 |
| Unknown | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.27 | 0.0 | 0.00 | 100.0 | 685 |
| Unknown | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.27 | 0.0 | 0.00 | 99.4 | 682 |
| Unknown | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.27 | 0.0 | 0.00 | 100.0 | 686 |
| Unknown | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.27 | 0.0 | 0.00 | 100.0 | 686 |
| Unknown | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.27 | 0.0 | 0.00 | 100.0 | 686 |
| Unknown | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.27 | 0.0 | 0.00 | 100.0 | 686 |
| Unknown | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.27 | 0.0 | 0.00 | 100.0 | 686 |
| Unknown | 0.00 | 42.17 | 0.0 | 0.00 | 100.0 | 2395 |
| Unknown | 0.00 | 42.17 | 0.0 | 0.00 | 63.8 | 9322 |

### Performance Analysis

No significant bottlenecks detected. GPU utilization is healthy.

**Resource Usage Overview:**
- Peak GPU Memory reached 42.17 GB. High VRAM usage, close to 48GB limit on L40S.
---

## Case: 03_Max_Quality_704p

- **Total Duration**: 420.81 s
- **Peak GPU Memory**: 52.76 GB
- **Total Compute Load**: 0

### Stage Breakdown

| Stage | Time (s) | GPU Mem (GB) | CPU (%) | Sys Mem (GB) | SM Act (%) | Comp Load |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Model_Initialization | 41.95 | 2.63 | 15.0 | 169.58 | 0.0 | 0 |
| TI2V_Preprocess | 0.00 | 2.63 | 0.0 | 0.00 | 0.0 | 0 |
| T5_Encoding | 1.33 | 13.47 | 14.7 | 157.03 | 21.5 | 0 |
| Step_0_Loading | 0.00 | 31.94 | 0.0 | 0.00 | 0.0 | 0 |
| Step_0_Inference | 6.90 | 41.71 | 14.4 | 147.27 | 95.7 | 0 |
| Step_1_Loading | 0.00 | 32.07 | 0.0 | 0.00 | 0.0 | 0 |
| Step_1_Inference | 6.84 | 41.81 | 16.7 | 147.16 | 100.0 | 0 |
| Step_2_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_2_Inference | 6.88 | 41.86 | 16.7 | 146.97 | 99.9 | 0 |
| Step_3_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_3_Inference | 6.86 | 41.86 | 18.5 | 146.44 | 100.0 | 0 |
| Step_4_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_4_Inference | 6.86 | 41.86 | 15.8 | 169.83 | 99.8 | 0 |
| Step_5_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_5_Inference | 6.86 | 41.86 | 13.4 | 173.65 | 99.8 | 0 |
| Step_6_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_6_Inference | 6.86 | 41.86 | 13.1 | 149.90 | 100.0 | 0 |
| Step_7_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_7_Inference | 6.87 | 41.86 | 12.9 | 149.24 | 99.8 | 0 |
| Step_8_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_8_Inference | 6.87 | 41.86 | 12.6 | 148.59 | 99.8 | 0 |
| Step_9_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_9_Inference | 6.87 | 41.86 | 12.9 | 148.42 | 100.0 | 0 |
| Step_10_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_10_Inference | 6.87 | 41.86 | 13.0 | 148.58 | 99.8 | 0 |
| Step_11_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_11_Inference | 6.88 | 41.86 | 13.6 | 148.38 | 100.0 | 0 |
| Step_12_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_12_Inference | 6.88 | 41.86 | 13.1 | 148.06 | 100.0 | 0 |
| Step_13_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 100.0 | 0 |
| Step_13_Inference | 6.88 | 41.86 | 13.0 | 148.11 | 99.8 | 0 |
| Step_14_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_14_Inference | 6.88 | 41.86 | 13.1 | 147.98 | 100.0 | 0 |
| Step_15_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_15_Inference | 6.88 | 41.86 | 12.8 | 148.06 | 99.8 | 0 |
| Step_16_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_16_Inference | 6.88 | 41.86 | 12.6 | 147.82 | 100.0 | 0 |
| Step_17_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_17_Inference | 6.88 | 41.86 | 16.0 | 147.50 | 100.0 | 0 |
| Step_18_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_18_Inference | 6.88 | 41.86 | 19.1 | 148.55 | 99.8 | 0 |
| Step_19_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_19_Inference | 6.88 | 41.86 | 8.6 | 149.92 | 99.8 | 0 |
| Step_20_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_20_Inference | 6.88 | 41.86 | 14.7 | 149.88 | 100.0 | 0 |
| Step_21_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_21_Inference | 6.88 | 41.86 | 13.5 | 161.00 | 99.8 | 0 |
| Step_22_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_22_Inference | 6.88 | 41.86 | 12.7 | 174.62 | 99.8 | 0 |
| Step_23_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_23_Inference | 6.88 | 41.86 | 13.2 | 159.78 | 100.0 | 0 |
| Step_24_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_24_Inference | 6.88 | 41.86 | 12.9 | 149.64 | 99.8 | 0 |
| Step_25_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_25_Inference | 6.88 | 41.86 | 12.7 | 150.12 | 100.0 | 0 |
| Step_26_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_26_Inference | 6.88 | 41.86 | 13.3 | 149.95 | 99.8 | 0 |
| Step_27_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_27_Inference | 6.88 | 41.86 | 12.8 | 149.87 | 99.9 | 0 |
| Step_28_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_28_Inference | 6.88 | 41.86 | 13.3 | 150.19 | 100.0 | 0 |
| Step_29_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_29_Inference | 6.88 | 41.86 | 13.0 | 150.04 | 99.8 | 0 |
| Step_30_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_30_Inference | 6.88 | 41.86 | 13.0 | 149.29 | 100.0 | 0 |
| Step_31_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_31_Inference | 6.88 | 41.86 | 15.3 | 149.59 | 99.8 | 0 |
| Step_32_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_32_Inference | 6.88 | 41.86 | 18.7 | 149.21 | 100.0 | 0 |
| Step_33_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_33_Inference | 6.88 | 41.86 | 12.4 | 149.62 | 99.9 | 0 |
| Step_34_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_34_Inference | 6.88 | 41.86 | 12.9 | 149.05 | 100.0 | 0 |
| Step_35_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_35_Inference | 6.88 | 41.86 | 12.8 | 149.18 | 99.8 | 0 |
| Step_36_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_36_Inference | 6.88 | 41.86 | 13.3 | 148.78 | 100.0 | 0 |
| Step_37_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_37_Inference | 6.88 | 41.86 | 13.2 | 148.85 | 99.8 | 0 |
| Step_38_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_38_Inference | 6.88 | 41.86 | 13.3 | 149.16 | 100.0 | 0 |
| Step_39_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_39_Inference | 6.88 | 41.86 | 13.2 | 149.01 | 99.8 | 0 |
| Step_40_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_40_Inference | 6.88 | 41.86 | 13.2 | 148.26 | 100.0 | 0 |
| Step_41_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_41_Inference | 6.88 | 41.86 | 12.2 | 173.12 | 99.9 | 0 |
| Step_42_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_42_Inference | 6.88 | 41.86 | 6.8 | 172.78 | 99.8 | 0 |
| Step_43_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_43_Inference | 6.89 | 41.86 | 14.6 | 150.88 | 100.0 | 0 |
| Step_44_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_44_Inference | 6.89 | 41.86 | 13.1 | 149.94 | 99.8 | 0 |
| Step_45_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_45_Inference | 6.89 | 41.86 | 12.9 | 149.40 | 100.0 | 0 |
| Step_46_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_46_Inference | 6.89 | 41.86 | 13.7 | 149.12 | 99.7 | 0 |
| Step_47_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_47_Inference | 6.89 | 41.86 | 12.9 | 149.08 | 100.0 | 0 |
| Step_48_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_48_Inference | 6.89 | 41.86 | 14.5 | 148.89 | 99.7 | 0 |
| Step_49_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_49_Inference | 6.89 | 41.86 | 13.3 | 147.25 | 99.9 | 0 |
| VAE_Decoding | 24.04 | 52.76 | 13.0 | 147.83 | 99.4 | 0 |
| Total_Execution | 415.62 | 52.76 | 13.7 | 174.62 | 88.9 | 0 |

### Inference Statistics

- **Avg Time per Step**: 6.88 s
- **Avg SM Activity**: 99.8 %
- **Avg CPU Utilization**: 13.6 %
- **Total Inference Load**: 0

### Performance Analysis

**Bottlenecks Detected:**
- Low overall GPU utilization (0.0%), suggesting potential CPU bottlenecks or data loading overhead.

**Resource Usage Overview:**
- Peak GPU Memory reached 52.76 GB. High VRAM usage, close to 48GB limit on L40S.
---

## Case: 03_Performance_Mode_720p

- **Total Duration**: 154.41 s
- **Peak GPU Memory**: 31.27 GB
- **Total Compute Load**: 18325

### Stage Breakdown

| Stage | Time (s) | GPU Mem (GB) | CPU (%) | Sys Mem (GB) | SM Act (%) | Comp Load |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Unknown | 0.00 | 2.63 | 13.6 | 130.49 | 0.0 | 0 |
| Unknown | 0.00 | 2.63 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 2.63 | 22.6 | 121.38 | 0.0 | 0 |
| Unknown | 0.00 | 21.34 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.12 | 12.2 | 121.25 | 85.7 | 600 |
| Unknown | 0.00 | 21.48 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.22 | 12.2 | 120.96 | 100.0 | 684 |
| Unknown | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.27 | 12.3 | 120.96 | 99.1 | 682 |
| Unknown | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.27 | 12.6 | 121.12 | 100.0 | 685 |
| Unknown | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.27 | 11.8 | 121.09 | 100.0 | 685 |
| Unknown | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.27 | 6.7 | 121.22 | 100.0 | 685 |
| Unknown | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.27 | 14.3 | 122.50 | 100.0 | 686 |
| Unknown | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.27 | 11.6 | 121.23 | 100.0 | 686 |
| Unknown | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.27 | 12.7 | 120.74 | 100.0 | 687 |
| Unknown | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 31.27 | 12.2 | 120.23 | 100.0 | 687 |
| Unknown | 0.00 | 23.54 | 12.3 | 139.49 | 96.2 | 2300 |
| Unknown | 0.00 | 31.27 | 13.4 | 140.88 | 60.0 | 9259 |

### Performance Analysis

**Bottlenecks Detected:**
- Inference stage 'Step_0_Inference' has low SM activity (85.71%), check kernel efficiency.

**Resource Usage Overview:**
- Peak GPU Memory reached 31.27 GB. VRAM usage is within safe margins.
---

## Case: 04_14B_Speed_Preview_480p

- **Total Duration**: 342.30 s
- **Peak GPU Memory**: 82.60 GB
- **Total Compute Load**: 39080

### Stage Breakdown

| Stage | Time (s) | GPU Mem (GB) | CPU (%) | Sys Mem (GB) | SM Act (%) | Comp Load |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Unknown | 0.00 | 0.49 | 0.0 | 0.00 | 0.2 | 9 |
| Unknown | 0.00 | 0.49 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 0.50 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 53.74 | 0.0 | 0.00 | 22.0 | 102 |
| Unknown | 0.00 | 82.51 | 0.0 | 0.00 | 97.6 | 3552 |
| Unknown | 0.00 | 53.83 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 82.57 | 0.0 | 0.00 | 100.0 | 3647 |
| Unknown | 0.00 | 53.87 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 82.60 | 0.0 | 0.00 | 100.0 | 3664 |
| Unknown | 0.00 | 53.87 | 0.0 | 0.00 | 0.0 | 0 |
| Unknown | 0.00 | 82.60 | 0.0 | 0.00 | 100.0 | 3664 |
| Unknown | 0.00 | 53.87 | 0.0 | 0.00 | 4.5 | 316 |
| Unknown | 0.00 | 82.60 | 0.0 | 0.00 | 100.0 | 3635 |
| Unknown | 0.00 | 8.64 | 0.0 | 0.00 | 99.9 | 913 |
| Unknown | 0.00 | 82.60 | 0.0 | 0.00 | 57.2 | 19578 |

### Performance Analysis

No significant bottlenecks detected. GPU utilization is healthy.

**Resource Usage Overview:**
- Peak GPU Memory reached 82.60 GB. High VRAM usage, close to 48GB limit on L40S.
---

## Case: 04_15s_50steps_720p

- **Total Duration**: 1238.48 s
- **Peak GPU Memory**: 43.46 GB
- **Total Compute Load**: 0

### Stage Breakdown

| Stage | Time (s) | GPU Mem (GB) | CPU (%) | Sys Mem (GB) | SM Act (%) | Comp Load |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Model_Initialization | 38.48 | 2.63 | 18.6 | 200.71 | 0.0 | 0 |
| TI2V_Preprocess | 0.00 | 2.63 | 0.0 | 0.00 | 0.0 | 0 |
| T5_Encoding | 13.26 | 2.63 | 31.6 | 225.08 | 0.4 | 0 |
| Step_0_Loading | 0.00 | 21.43 | 0.0 | 0.00 | 0.0 | 0 |
| Step_0_Inference | 22.21 | 43.12 | 12.6 | 206.54 | 98.2 | 0 |
| Step_1_Loading | 0.00 | 21.73 | 0.0 | 0.00 | 0.0 | 0 |
| Step_1_Inference | 22.16 | 43.35 | 14.6 | 203.14 | 100.0 | 0 |
| Step_2_Loading | 0.00 | 21.90 | 0.0 | 202.07 | 0.0 | 0 |
| Step_2_Inference | 22.28 | 43.46 | 13.1 | 228.78 | 100.0 | 0 |
| Step_3_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_3_Inference | 22.31 | 43.46 | 13.1 | 208.99 | 99.7 | 0 |
| Step_4_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_4_Inference | 22.34 | 43.46 | 16.0 | 203.86 | 99.9 | 0 |
| Step_5_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_5_Inference | 22.37 | 43.46 | 13.2 | 203.09 | 100.0 | 0 |
| Step_6_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_6_Inference | 22.38 | 43.46 | 13.1 | 228.57 | 100.0 | 0 |
| Step_7_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_7_Inference | 22.38 | 43.46 | 9.2 | 209.62 | 100.0 | 0 |
| Step_8_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_8_Inference | 22.35 | 43.46 | 3.7 | 176.88 | 100.0 | 0 |
| Step_9_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_9_Inference | 22.33 | 43.46 | 2.6 | 174.84 | 99.9 | 0 |
| Step_10_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_10_Inference | 22.34 | 43.46 | 2.7 | 199.84 | 100.0 | 0 |
| Step_11_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_11_Inference | 22.34 | 43.46 | 3.6 | 180.81 | 100.0 | 0 |
| Step_12_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_12_Inference | 22.35 | 43.46 | 5.0 | 174.29 | 99.9 | 0 |
| Step_13_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_13_Inference | 22.35 | 43.46 | 3.4 | 200.74 | 100.0 | 0 |
| Step_14_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_14_Inference | 22.36 | 43.46 | 2.6 | 175.67 | 100.0 | 0 |
| Step_15_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_15_Inference | 22.36 | 43.46 | 2.6 | 174.90 | 99.9 | 0 |
| Step_16_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_16_Inference | 22.36 | 43.46 | 2.6 | 174.54 | 99.9 | 0 |
| Step_17_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_17_Inference | 22.36 | 43.46 | 3.4 | 178.89 | 99.9 | 0 |
| Step_18_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_18_Inference | 22.36 | 43.46 | 4.9 | 181.26 | 99.9 | 0 |
| Step_19_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_19_Inference | 22.35 | 43.46 | 8.0 | 135.48 | 99.9 | 0 |
| Step_20_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_20_Inference | 22.33 | 43.46 | 2.7 | 157.90 | 100.0 | 0 |
| Step_21_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_21_Inference | 22.32 | 43.46 | 2.6 | 132.11 | 100.0 | 0 |
| Step_22_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_22_Inference | 22.32 | 43.46 | 3.7 | 131.52 | 99.9 | 0 |
| Step_23_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_23_Inference | 22.32 | 43.46 | 2.6 | 131.33 | 99.9 | 0 |
| Step_24_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_24_Inference | 22.32 | 43.46 | 2.5 | 157.04 | 99.9 | 0 |
| Step_25_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_25_Inference | 22.33 | 43.46 | 2.5 | 143.13 | 100.0 | 0 |
| Step_26_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_26_Inference | 22.34 | 43.46 | 4.7 | 131.40 | 99.9 | 0 |
| Step_27_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_27_Inference | 22.35 | 43.46 | 6.3 | 140.93 | 99.9 | 0 |
| Step_28_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_28_Inference | 22.34 | 43.46 | 2.6 | 157.84 | 100.0 | 0 |
| Step_29_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_29_Inference | 22.34 | 43.46 | 2.7 | 132.25 | 99.9 | 0 |
| Step_30_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_30_Inference | 22.33 | 43.46 | 2.6 | 131.75 | 100.0 | 0 |
| Step_31_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_31_Inference | 22.32 | 43.46 | 5.5 | 146.06 | 100.0 | 0 |
| Step_32_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_32_Inference | 22.31 | 43.46 | 4.2 | 156.52 | 99.9 | 0 |
| Step_33_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_33_Inference | 22.31 | 43.46 | 3.7 | 132.60 | 100.0 | 0 |
| Step_34_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_34_Inference | 22.30 | 43.46 | 2.6 | 131.80 | 99.9 | 0 |
| Step_35_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_35_Inference | 22.31 | 43.46 | 4.1 | 132.52 | 100.0 | 0 |
| Step_36_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_36_Inference | 22.31 | 43.46 | 2.6 | 157.54 | 99.9 | 0 |
| Step_37_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_37_Inference | 22.32 | 43.46 | 4.2 | 132.09 | 100.0 | 0 |
| Step_38_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_38_Inference | 22.32 | 43.46 | 5.5 | 131.89 | 99.9 | 0 |
| Step_39_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_39_Inference | 22.33 | 43.46 | 3.6 | 133.24 | 99.9 | 0 |
| Step_40_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 100.0 | 0 |
| Step_40_Inference | 22.33 | 43.46 | 3.2 | 132.51 | 100.0 | 0 |
| Step_41_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_41_Inference | 22.34 | 43.46 | 5.5 | 111.84 | 100.0 | 0 |
| Step_42_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_42_Inference | 22.33 | 43.46 | 3.5 | 117.97 | 100.0 | 0 |
| Step_43_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_43_Inference | 22.32 | 43.46 | 4.3 | 119.71 | 99.9 | 0 |
| Step_44_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_44_Inference | 22.30 | 43.46 | 1.9 | 119.43 | 99.9 | 0 |
| Step_45_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_45_Inference | 22.29 | 43.46 | 9.3 | 166.89 | 100.0 | 0 |
| Step_46_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_46_Inference | 22.29 | 43.46 | 3.2 | 162.72 | 99.9 | 0 |
| Step_47_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_47_Inference | 22.29 | 43.46 | 1.8 | 162.62 | 100.0 | 0 |
| Step_48_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_48_Inference | 22.29 | 43.46 | 2.1 | 162.86 | 100.0 | 0 |
| Step_49_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_49_Inference | 22.29 | 43.46 | 3.5 | 163.18 | 99.9 | 0 |
| VAE_Decoding | 53.75 | 25.97 | 3.5 | 186.73 | 99.8 | 0 |
| Total_Execution | 1233.26 | 43.46 | 5.8 | 228.78 | 95.1 | 0 |

### Inference Statistics

- **Avg Time per Step**: 22.32 s
- **Avg SM Activity**: 99.9 %
- **Avg CPU Utilization**: 5.2 %
- **Total Inference Load**: 0

### Performance Analysis

**Bottlenecks Detected:**
- Low overall GPU utilization (0.0%), suggesting potential CPU bottlenecks or data loading overhead.

**Resource Usage Overview:**
- Peak GPU Memory reached 43.46 GB. High VRAM usage, close to 48GB limit on L40S.
---

