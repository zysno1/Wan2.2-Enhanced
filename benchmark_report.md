# Wan2.2 Benchmark Report

| Case                   | Res        | Offload |  Time(s) | s/step | Mem(GB) | SM(%) |   Load |
|------------------------|------------|---------|----------|--------|---------|-------|--------|
| 01_5B_Speed_Preview_704p | 1280*704   | True    |   143.25 |   0.00 |   31.27 |   0.0 |  11546 |
| 01_Speed_Preview_480p  | 1280*704   | True    |   114.94 |   0.00 |   31.27 |   0.0 |  11672 |
| 01_Speed_Preview_704p  | 1280*704   | True    |   126.51 |   6.91 |   31.27 |  98.9 |      0 |
| 02_5B_Efficiency_Mode_704p | 1280*704   | True    |   151.58 |   0.00 |   31.27 |   0.0 |  18624 |
| 02_Efficiency_Mode_720p | 1280*704   | True    |   187.44 |   0.00 |   31.27 |   0.0 |  18702 |
| 02_Efficiency_Quality_704p | 1280*704   | True    |   298.33 |   6.88 |   31.27 |  99.7 |      0 |
| 03_5B_Performance_Mode_704p | 1280*704   | False   |   146.27 |   0.00 |   42.17 |   0.0 |  18587 |
| 03_Max_Quality_704p    | 1280*704   | Unknown |   792.82 |  13.89 |   31.27 |  30.0 |      0 |
| 03_Performance_Mode_720p | 1280*704   | False   |   154.41 |   0.00 |   31.27 |   0.0 |  18325 |
| 04_14B_Speed_Preview_480p | 1280*704   | True    |   342.30 |   0.00 |   82.60 |   0.0 |  39080 |

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

- **Total Duration**: 126.51 s
- **Peak GPU Memory**: 31.27 GB
- **Total Compute Load**: 0

### Stage Breakdown

| Stage | Time (s) | GPU Mem (GB) | CPU (%) | Sys Mem (GB) | SM Act (%) | Comp Load |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Model_Initialization | 38.80 | 2.63 | 14.4 | 171.74 | 87.9 | 0 |
| TI2V_Preprocess | 0.00 | 2.63 | 0.0 | 0.00 | 0.0 | 0 |
| T5_Encoding | 13.06 | 2.63 | 22.4 | 163.32 | 42.8 | 0 |
| Step_0_Loading | 0.00 | 21.34 | 0.0 | 0.00 | 0.0 | 0 |
| Step_0_Inference | 7.02 | 31.12 | 12.4 | 141.39 | 95.2 | 0 |
| Step_1_Loading | 0.00 | 21.48 | 0.0 | 0.00 | 0.0 | 0 |
| Step_1_Inference | 6.87 | 31.22 | 11.5 | 131.84 | 99.7 | 0 |
| Step_2_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_2_Inference | 6.90 | 31.27 | 8.1 | 133.45 | 100.0 | 0 |
| Step_3_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_3_Inference | 6.87 | 31.27 | 13.8 | 133.38 | 99.6 | 0 |
| Step_4_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_4_Inference | 6.88 | 31.27 | 12.2 | 132.75 | 99.8 | 0 |
| VAE_Decoding | 23.93 | 23.54 | 11.5 | 150.65 | 98.4 | 0 |
| Total_Execution | 121.19 | 31.27 | 13.7 | 171.74 | 82.1 | 0 |

### Inference Statistics

- **Avg Time per Step**: 6.91 s
- **Avg SM Activity**: 98.9 %
- **Avg CPU Utilization**: 11.6 %
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

- **Total Duration**: 298.33 s
- **Peak GPU Memory**: 31.27 GB
- **Total Compute Load**: 0

### Stage Breakdown

| Stage | Time (s) | GPU Mem (GB) | CPU (%) | Sys Mem (GB) | SM Act (%) | Comp Load |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Model_Initialization | 39.00 | 2.63 | 13.7 | 142.42 | 0.1 | 0 |
| TI2V_Preprocess | 0.00 | 2.63 | 0.0 | 0.00 | 0.0 | 0 |
| T5_Encoding | 13.56 | 2.63 | 22.8 | 132.22 | 0.3 | 0 |
| Step_0_Loading | 0.00 | 21.34 | 0.0 | 0.00 | 0.0 | 0 |
| Step_0_Inference | 6.98 | 31.12 | 12.2 | 132.51 | 95.4 | 0 |
| Step_1_Loading | 0.00 | 21.48 | 0.0 | 0.00 | 0.0 | 0 |
| Step_1_Inference | 6.84 | 31.22 | 12.0 | 132.11 | 99.7 | 0 |
| Step_2_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_2_Inference | 6.88 | 31.27 | 11.7 | 132.00 | 99.8 | 0 |
| Step_3_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_3_Inference | 6.85 | 31.27 | 12.5 | 132.20 | 100.0 | 0 |
| Step_4_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_4_Inference | 6.85 | 31.27 | 10.0 | 132.02 | 100.0 | 0 |
| Step_5_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_5_Inference | 6.85 | 31.27 | 9.0 | 133.08 | 99.9 | 0 |
| Step_6_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_6_Inference | 6.86 | 31.27 | 13.9 | 132.88 | 99.9 | 0 |
| Step_7_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_7_Inference | 6.87 | 31.27 | 12.1 | 132.39 | 100.0 | 0 |
| Step_8_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_8_Inference | 6.87 | 31.27 | 13.0 | 132.73 | 99.8 | 0 |
| Step_9_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_9_Inference | 6.87 | 31.27 | 12.3 | 132.30 | 99.9 | 0 |
| Step_10_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_10_Inference | 6.87 | 31.27 | 12.3 | 131.61 | 100.0 | 0 |
| Step_11_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_11_Inference | 6.87 | 31.27 | 11.4 | 132.09 | 99.8 | 0 |
| Step_12_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_12_Inference | 6.88 | 31.27 | 12.4 | 132.09 | 100.0 | 0 |
| Step_13_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_13_Inference | 6.87 | 31.27 | 12.3 | 131.86 | 99.9 | 0 |
| Step_14_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_14_Inference | 6.88 | 31.27 | 12.5 | 131.75 | 99.8 | 0 |
| Step_15_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_15_Inference | 6.88 | 31.27 | 12.3 | 131.91 | 100.0 | 0 |
| Step_16_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_16_Inference | 6.88 | 31.27 | 12.2 | 131.91 | 100.0 | 0 |
| Step_17_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_17_Inference | 6.88 | 31.27 | 9.9 | 131.36 | 99.8 | 0 |
| Step_18_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_18_Inference | 6.88 | 31.27 | 12.4 | 130.44 | 100.0 | 0 |
| Step_19_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_19_Inference | 6.88 | 31.27 | 12.9 | 130.80 | 100.0 | 0 |
| Step_20_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_20_Inference | 6.88 | 31.27 | 11.6 | 131.11 | 99.8 | 0 |
| Step_21_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_21_Inference | 6.88 | 31.27 | 12.4 | 130.91 | 100.0 | 0 |
| Step_22_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_22_Inference | 6.88 | 31.27 | 12.3 | 131.26 | 99.8 | 0 |
| Step_23_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_23_Inference | 6.88 | 31.27 | 12.3 | 131.27 | 100.0 | 0 |
| Step_24_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_24_Inference | 6.88 | 31.27 | 12.8 | 131.19 | 99.8 | 0 |
| Step_25_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_25_Inference | 6.89 | 31.27 | 12.4 | 131.69 | 100.0 | 0 |
| Step_26_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_26_Inference | 6.88 | 31.27 | 12.1 | 131.77 | 99.9 | 0 |
| Step_27_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_27_Inference | 6.88 | 31.27 | 12.2 | 131.67 | 99.8 | 0 |
| Step_28_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_28_Inference | 6.88 | 31.27 | 6.3 | 131.99 | 100.0 | 0 |
| Step_29_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_29_Inference | 6.88 | 31.27 | 13.5 | 133.05 | 99.8 | 0 |
| VAE_Decoding | 23.96 | 23.54 | 12.3 | 150.79 | 99.2 | 0 |
| Total_Execution | 293.13 | 31.27 | 12.7 | 150.79 | 79.3 | 0 |

### Inference Statistics

- **Avg Time per Step**: 6.88 s
- **Avg SM Activity**: 99.7 %
- **Avg CPU Utilization**: 11.9 %
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

- **Total Duration**: 792.82 s
- **Peak GPU Memory**: 31.27 GB
- **Total Compute Load**: 0

### Stage Breakdown

| Stage | Time (s) | GPU Mem (GB) | CPU (%) | Sys Mem (GB) | SM Act (%) | Comp Load |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Model_Initialization | 39.56 | 2.63 | 13.5 | 153.51 | 99.7 | 0 |
| TI2V_Preprocess | 0.00 | 2.63 | 0.0 | 0.00 | 0.0 | 0 |
| T5_Encoding | 16.78 | 2.63 | 22.8 | 144.13 | 98.5 | 0 |
| Step_0_Loading | 0.01 | 21.34 | 0.0 | 0.00 | 0.0 | 0 |
| Step_0_Inference | 15.19 | 31.12 | 12.6 | 144.17 | 100.0 | 0 |
| Step_1_Loading | 0.00 | 21.48 | 0.0 | 0.00 | 0.0 | 0 |
| Step_1_Inference | 15.04 | 31.22 | 13.0 | 143.30 | 100.0 | 0 |
| Step_2_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_2_Inference | 15.08 | 31.27 | 13.2 | 143.50 | 100.0 | 0 |
| Step_3_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_3_Inference | 15.02 | 31.27 | 13.2 | 143.24 | 100.0 | 0 |
| Step_4_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_4_Inference | 15.02 | 31.27 | 13.0 | 143.76 | 100.0 | 0 |
| Step_5_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 100.0 | 0 |
| Step_5_Inference | 15.02 | 31.27 | 13.1 | 143.95 | 100.0 | 0 |
| Step_6_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_6_Inference | 15.03 | 31.27 | 13.5 | 143.93 | 100.0 | 0 |
| Step_7_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_7_Inference | 15.04 | 31.27 | 14.8 | 143.27 | 100.0 | 0 |
| Step_8_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_8_Inference | 15.04 | 31.27 | 11.8 | 142.27 | 100.0 | 0 |
| Step_9_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_9_Inference | 15.03 | 31.27 | 16.0 | 142.35 | 100.0 | 0 |
| Step_10_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_10_Inference | 15.03 | 31.27 | 13.5 | 143.23 | 100.0 | 0 |
| Step_11_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_11_Inference | 15.04 | 31.27 | 13.1 | 143.11 | 100.0 | 0 |
| Step_12_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_12_Inference | 15.04 | 31.27 | 13.1 | 142.69 | 100.0 | 0 |
| Step_13_Loading | 0.00 | 21.56 | 13.9 | 141.79 | 0.0 | 0 |
| Step_13_Inference | 15.04 | 31.27 | 13.0 | 142.94 | 100.0 | 0 |
| Step_14_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_14_Inference | 15.04 | 31.27 | 13.3 | 142.96 | 100.0 | 0 |
| Step_15_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_15_Inference | 15.03 | 31.27 | 13.1 | 143.12 | 0.0 | 0 |
| Step_16_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_16_Inference | 15.05 | 31.27 | 12.7 | 143.25 | 0.0 | 0 |
| Step_17_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_17_Inference | 15.04 | 31.27 | 10.9 | 143.52 | 0.0 | 0 |
| Step_18_Loading | 0.00 | 21.55 | 18.7 | 143.34 | 0.0 | 0 |
| Step_18_Inference | 15.04 | 31.27 | 12.3 | 143.30 | 0.0 | 0 |
| Step_19_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_19_Inference | 15.03 | 31.27 | 12.9 | 143.51 | 0.0 | 0 |
| Step_20_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_20_Inference | 15.03 | 31.27 | 12.9 | 143.26 | 0.0 | 0 |
| Step_21_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_21_Inference | 15.03 | 31.27 | 12.9 | 142.90 | 0.0 | 0 |
| Step_22_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_22_Inference | 15.03 | 31.27 | 13.4 | 142.83 | 0.0 | 0 |
| Step_23_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_23_Inference | 15.03 | 31.27 | 13.1 | 142.61 | 0.0 | 0 |
| Step_24_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_24_Inference | 15.03 | 31.27 | 13.1 | 143.07 | 0.0 | 0 |
| Step_25_Loading | 0.00 | 21.56 | 13.7 | 142.33 | 0.0 | 0 |
| Step_25_Inference | 15.04 | 31.27 | 13.1 | 143.05 | 0.0 | 0 |
| Step_26_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_26_Inference | 15.03 | 31.27 | 13.0 | 142.85 | 0.0 | 0 |
| Step_27_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_27_Inference | 15.03 | 31.27 | 13.0 | 142.74 | 0.0 | 0 |
| Step_28_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_28_Inference | 15.03 | 31.27 | 11.2 | 144.02 | 0.0 | 0 |
| Step_29_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_29_Inference | 15.03 | 31.27 | 13.2 | 143.77 | 0.0 | 0 |
| Step_30_Loading | 0.00 | 21.55 | 11.4 | 142.58 | 0.0 | 0 |
| Step_30_Inference | 15.04 | 31.27 | 12.6 | 143.18 | 0.0 | 0 |
| Step_31_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_31_Inference | 15.03 | 31.27 | 12.6 | 143.10 | 0.0 | 0 |
| Step_32_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_32_Inference | 15.04 | 31.27 | 12.5 | 143.30 | 0.0 | 0 |
| Step_33_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_33_Inference | 15.03 | 31.27 | 12.9 | 143.15 | 0.0 | 0 |
| Step_34_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_34_Inference | 15.03 | 31.27 | 12.9 | 143.17 | 0.0 | 0 |
| Step_35_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_35_Inference | 15.03 | 31.27 | 12.9 | 143.04 | 0.0 | 0 |
| Step_36_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_36_Inference | 15.03 | 31.27 | 11.6 | 143.07 | 0.0 | 0 |
| Step_37_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_37_Inference | 15.03 | 31.27 | 13.2 | 143.00 | 0.0 | 0 |
| Step_38_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_38_Inference | 15.02 | 31.27 | 13.0 | 142.88 | 0.0 | 0 |
| Step_39_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_39_Inference | 10.83 | 31.27 | 10.4 | 155.15 | 0.0 | 0 |
| Step_40_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_40_Inference | 12.98 | 31.27 | 13.0 | 162.84 | 0.0 | 0 |
| Step_41_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_41_Inference | 15.07 | 31.27 | 12.9 | 162.49 | 0.0 | 0 |
| Step_42_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_42_Inference | 15.07 | 31.27 | 13.3 | 162.52 | 0.0 | 0 |
| Step_43_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_43_Inference | 12.62 | 31.27 | 13.4 | 162.56 | 0.0 | 0 |
| Step_44_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_44_Inference | 6.89 | 31.27 | 13.6 | 162.80 | 0.0 | 0 |
| Step_45_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_45_Inference | 6.88 | 31.27 | 12.0 | 132.20 | 0.0 | 0 |
| Step_46_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_46_Inference | 6.88 | 31.27 | 13.9 | 132.67 | 0.0 | 0 |
| Step_47_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_47_Inference | 6.89 | 31.27 | 12.6 | 132.79 | 0.0 | 0 |
| Step_48_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_48_Inference | 6.89 | 31.27 | 13.0 | 141.47 | 0.0 | 0 |
| Step_49_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_49_Inference | 6.88 | 31.27 | 13.2 | 151.26 | 0.0 | 0 |
| VAE_Decoding | 24.00 | 23.54 | 17.5 | 171.85 | 0.0 | 0 |
| Total_Execution | 792.57 | 31.27 | 13.3 | 171.85 | 99.9 | 0 |

### Inference Statistics

- **Avg Time per Step**: 13.89 s
- **Avg SM Activity**: 30.0 %
- **Avg CPU Utilization**: 12.9 %
- **Total Inference Load**: 0

### Performance Analysis

**Bottlenecks Detected:**
- Low overall GPU utilization (0.0%), suggesting potential CPU bottlenecks or data loading overhead.

**Resource Usage Overview:**
- Peak GPU Memory reached 31.27 GB. VRAM usage is within safe margins.
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

