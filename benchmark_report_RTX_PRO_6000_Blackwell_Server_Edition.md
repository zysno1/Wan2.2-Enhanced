# Wan2.2 Benchmark Report

| Case                   | Res        | Offload |  Time(s) | s/step | Mem(GB) | SM(%) |   Load |
|------------------------|------------|---------|----------|--------|---------|-------|--------|
| 01_Speed_Preview_480p  | 1280*704   | True    |   114.94 |   6.87 |   31.27 |  99.8 |  11672 |
| 02_Efficiency_Mode_720p | 1280*704   | True    |   147.19 |   6.86 |   31.27 |  98.7 |  18453 |
| 03_Performance_Mode_720p | 1280*704   | True    |   149.29 |   6.86 |   31.27 |  98.9 |  18494 |

# Detailed Breakdown

## Case: 01_5B_Speed_Preview_704p

- **Total Duration**: 143.25 s
- **Peak GPU Memory**: 31.27 GB
- **Total Compute Load**: 11546

### Stage Breakdown

| Stage | Time (s) | GPU Mem (GB) | CPU (%) | Sys Mem (GB) | SM Act (%) | Comp Load |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Model_Initialization | 43.78 | 2.63 | 0.0 | 0.00 | 0.0 | 0 |
| TI2V_Preprocess | 0.00 | 2.63 | 0.0 | 0.00 | 0.0 | 0 |
| T5_Encoding | 14.34 | 2.63 | 0.0 | 0.00 | 0.0 | 0 |
| Step_0_Loading | 0.01 | 21.34 | 0.0 | 0.00 | 0.0 | 0 |
| Step_0_Inference | 7.10 | 31.12 | 0.0 | 0.00 | 100.0 | 710 |
| Step_1_Loading | 0.00 | 21.48 | 0.0 | 0.00 | 0.0 | 0 |
| Step_1_Inference | 6.84 | 31.22 | 0.0 | 0.00 | 100.0 | 684 |
| Step_2_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_2_Inference | 6.90 | 31.27 | 0.0 | 0.00 | 100.0 | 690 |
| Step_3_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_3_Inference | 6.85 | 31.27 | 0.0 | 0.00 | 97.1 | 665 |
| Step_4_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_4_Inference | 6.85 | 31.27 | 0.0 | 0.00 | 100.0 | 685 |
| VAE_Decoding | 23.84 | 23.54 | 0.0 | 0.00 | 96.4 | 2299 |
| Total_Execution | 143.10 | 31.27 | 0.0 | 0.00 | 40.6 | 5813 |

### Inference Statistics

- **Avg Time per Step**: 6.91 s
- **Avg SM Activity**: 99.4 %
- **Avg CPU Utilization**: 0.0 %
- **Total Inference Load**: 3435

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
| Model_Initialization | 35.26 | 2.63 | 5.8 | 301.34 | 0.0 | 0 |
| TI2V_Preprocess | 0.00 | 2.63 | 0.0 | 0.00 | 0.0 | 0 |
| T5_Encoding | 12.90 | 2.63 | 14.9 | 298.49 | 0.0 | 0 |
| Step_0_Loading | 0.00 | 21.34 | 0.0 | 0.00 | 0.0 | 0 |
| Step_0_Inference | 6.99 | 31.12 | 5.1 | 298.61 | 99.4 | 695 |
| Step_1_Loading | 0.00 | 21.48 | 0.0 | 0.00 | 0.0 | 0 |
| Step_1_Inference | 6.83 | 31.22 | 5.9 | 298.43 | 100.0 | 683 |
| Step_2_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_2_Inference | 6.86 | 31.27 | 5.8 | 298.41 | 100.0 | 686 |
| Step_3_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_3_Inference | 6.84 | 31.27 | 9.4 | 300.61 | 100.0 | 684 |
| Step_4_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_4_Inference | 6.84 | 31.27 | 4.1 | 300.37 | 99.7 | 682 |
| VAE_Decoding | 23.74 | 23.54 | 3.4 | 318.29 | 100.0 | 2374 |
| Total_Execution | 114.80 | 31.27 | 6.3 | 318.96 | 51.1 | 5868 |

### Inference Statistics

- **Avg Time per Step**: 6.87 s
- **Avg SM Activity**: 99.8 %
- **Avg CPU Utilization**: 6.1 %
- **Total Inference Load**: 3431

### Performance Analysis

No significant bottlenecks detected. GPU utilization is healthy.

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
| Model_Initialization | 36.67 | 2.63 | 0.0 | 0.00 | 0.0 | 0 |
| TI2V_Preprocess | 0.00 | 2.63 | 0.0 | 0.00 | 0.0 | 0 |
| T5_Encoding | 12.55 | 2.63 | 0.0 | 0.00 | 0.0 | 0 |
| Step_0_Loading | 0.00 | 21.34 | 0.0 | 0.00 | 0.0 | 0 |
| Step_0_Inference | 7.00 | 31.12 | 0.0 | 0.00 | 100.0 | 700 |
| Step_1_Loading | 0.00 | 21.48 | 0.0 | 0.00 | 0.0 | 0 |
| Step_1_Inference | 6.84 | 31.22 | 0.0 | 0.00 | 100.0 | 684 |
| Step_2_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_2_Inference | 6.87 | 31.27 | 0.0 | 0.00 | 99.9 | 686 |
| Step_3_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_3_Inference | 6.85 | 31.27 | 0.0 | 0.00 | 100.0 | 685 |
| Step_4_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_4_Inference | 6.86 | 31.27 | 0.0 | 0.00 | 100.0 | 686 |
| Step_5_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_5_Inference | 6.86 | 31.27 | 0.0 | 0.00 | 99.3 | 681 |
| Step_6_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_6_Inference | 6.86 | 31.27 | 0.0 | 0.00 | 99.9 | 685 |
| Step_7_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_7_Inference | 6.86 | 31.27 | 0.0 | 0.00 | 100.0 | 686 |
| Step_8_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_8_Inference | 6.86 | 31.27 | 0.0 | 0.00 | 100.0 | 686 |
| Step_9_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_9_Inference | 6.86 | 31.27 | 0.0 | 0.00 | 100.0 | 686 |
| VAE_Decoding | 23.91 | 23.54 | 0.0 | 0.00 | 100.0 | 2391 |
| Total_Execution | 151.44 | 31.27 | 0.0 | 0.00 | 61.9 | 9368 |

### Inference Statistics

- **Avg Time per Step**: 6.87 s
- **Avg SM Activity**: 99.9 %
- **Avg CPU Utilization**: 0.0 %
- **Total Inference Load**: 6865

### Performance Analysis

No significant bottlenecks detected. GPU utilization is healthy.

**Resource Usage Overview:**
- Peak GPU Memory reached 31.27 GB. VRAM usage is within safe margins.
---

## Case: 02_Efficiency_Mode_720p

- **Total Duration**: 147.19 s
- **Peak GPU Memory**: 31.27 GB
- **Total Compute Load**: 18453

### Stage Breakdown

| Stage | Time (s) | GPU Mem (GB) | CPU (%) | Sys Mem (GB) | SM Act (%) | Comp Load |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Model_Initialization | 34.47 | 2.63 | 5.0 | 311.19 | 0.0 | 0 |
| TI2V_Preprocess | 0.00 | 2.63 | 0.0 | 0.00 | 0.0 | 0 |
| T5_Encoding | 11.49 | 2.63 | 13.2 | 300.12 | 0.0 | 0 |
| Step_0_Loading | 0.00 | 21.34 | 0.0 | 0.00 | 0.0 | 0 |
| Step_0_Inference | 6.96 | 31.12 | 3.4 | 299.84 | 86.9 | 605 |
| Step_1_Loading | 0.00 | 21.48 | 0.0 | 0.00 | 0.0 | 0 |
| Step_1_Inference | 6.84 | 31.22 | 3.6 | 299.79 | 100.0 | 684 |
| Step_2_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_2_Inference | 6.87 | 31.27 | 3.4 | 299.70 | 99.9 | 686 |
| Step_3_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_3_Inference | 6.85 | 31.27 | 3.9 | 299.71 | 100.0 | 685 |
| Step_4_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 100.0 | 0 |
| Step_4_Inference | 6.85 | 31.27 | 3.5 | 299.74 | 100.0 | 685 |
| Step_5_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_5_Inference | 6.85 | 31.27 | 3.7 | 299.66 | 100.0 | 685 |
| Step_6_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_6_Inference | 6.85 | 31.27 | 4.5 | 311.84 | 100.0 | 685 |
| Step_7_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_7_Inference | 6.85 | 31.27 | 4.4 | 300.97 | 99.9 | 684 |
| Step_8_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_8_Inference | 6.85 | 31.27 | 4.5 | 288.10 | 100.0 | 685 |
| Step_9_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_9_Inference | 6.85 | 31.27 | 3.6 | 288.10 | 100.0 | 685 |
| VAE_Decoding | 23.83 | 23.54 | 3.9 | 305.72 | 100.0 | 2383 |
| Total_Execution | 147.06 | 31.27 | 4.9 | 311.84 | 63.3 | 9302 |

### Inference Statistics

- **Avg Time per Step**: 6.86 s
- **Avg SM Activity**: 98.7 %
- **Avg CPU Utilization**: 3.9 %
- **Total Inference Load**: 6768

### Performance Analysis

**Bottlenecks Detected:**
- Inference stage 'Step_0_Inference' has low SM activity (86.86%), check kernel efficiency.

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
| Model_Initialization | 37.41 | 2.63 | 0.0 | 0.00 | 0.0 | 0 |
| TI2V_Preprocess | 0.00 | 2.63 | 0.0 | 0.00 | 0.0 | 0 |
| T5_Encoding | 12.47 | 2.63 | 0.0 | 0.00 | 0.0 | 0 |
| Step_0_Loading | 0.00 | 21.34 | 0.0 | 0.00 | 0.0 | 0 |
| Step_0_Inference | 7.02 | 31.12 | 0.0 | 0.00 | 100.0 | 702 |
| Step_1_Loading | 0.00 | 21.48 | 0.0 | 0.00 | 0.0 | 0 |
| Step_1_Inference | 6.84 | 31.22 | 0.0 | 0.00 | 100.0 | 684 |
| Step_2_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_2_Inference | 6.88 | 31.27 | 0.0 | 0.00 | 100.0 | 688 |
| Step_3_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_3_Inference | 6.85 | 31.27 | 0.0 | 0.00 | 100.0 | 685 |
| Step_4_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_4_Inference | 6.86 | 31.27 | 0.0 | 0.00 | 99.4 | 682 |
| Step_5_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_5_Inference | 6.86 | 31.27 | 0.0 | 0.00 | 100.0 | 686 |
| Step_6_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_6_Inference | 6.86 | 31.27 | 0.0 | 0.00 | 100.0 | 686 |
| Step_7_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_7_Inference | 6.86 | 31.27 | 0.0 | 0.00 | 100.0 | 686 |
| Step_8_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_8_Inference | 6.86 | 31.27 | 0.0 | 0.00 | 100.0 | 686 |
| Step_9_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_9_Inference | 6.86 | 31.27 | 0.0 | 0.00 | 100.0 | 686 |
| VAE_Decoding | 23.95 | 42.17 | 0.0 | 0.00 | 100.0 | 2395 |
| Total_Execution | 146.14 | 42.17 | 0.0 | 0.00 | 63.8 | 9322 |

### Inference Statistics

- **Avg Time per Step**: 6.87 s
- **Avg SM Activity**: 99.9 %
- **Avg CPU Utilization**: 0.0 %
- **Total Inference Load**: 6870

### Performance Analysis

No significant bottlenecks detected. GPU utilization is healthy.

**Resource Usage Overview:**
- Peak GPU Memory reached 42.17 GB. High VRAM usage, close to 48GB limit on L40S.
---

## Case: 03_Performance_Mode_720p

- **Total Duration**: 149.29 s
- **Peak GPU Memory**: 31.27 GB
- **Total Compute Load**: 18494

### Stage Breakdown

| Stage | Time (s) | GPU Mem (GB) | CPU (%) | Sys Mem (GB) | SM Act (%) | Comp Load |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Model_Initialization | 35.68 | 2.63 | 5.2 | 297.47 | 0.0 | 0 |
| TI2V_Preprocess | 0.00 | 2.63 | 0.0 | 0.00 | 0.0 | 0 |
| T5_Encoding | 12.73 | 2.63 | 14.1 | 299.52 | 0.0 | 0 |
| Step_0_Loading | 0.00 | 21.34 | 0.0 | 0.00 | 0.0 | 0 |
| Step_0_Inference | 6.96 | 31.12 | 4.5 | 300.57 | 89.6 | 623 |
| Step_1_Loading | 0.00 | 21.48 | 0.0 | 0.00 | 0.0 | 0 |
| Step_1_Inference | 6.84 | 31.22 | 4.2 | 300.69 | 100.0 | 684 |
| Step_2_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_2_Inference | 6.87 | 31.27 | 3.6 | 300.70 | 100.0 | 687 |
| Step_3_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_3_Inference | 6.84 | 31.27 | 3.8 | 300.59 | 100.0 | 684 |
| Step_4_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_4_Inference | 6.85 | 31.27 | 4.6 | 312.48 | 100.0 | 685 |
| Step_5_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_5_Inference | 6.85 | 31.27 | 4.6 | 301.65 | 99.3 | 680 |
| Step_6_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_6_Inference | 6.85 | 31.27 | 4.5 | 301.41 | 100.0 | 685 |
| Step_7_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_7_Inference | 6.85 | 31.27 | 3.6 | 301.12 | 100.0 | 685 |
| Step_8_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_8_Inference | 6.85 | 31.27 | 3.9 | 300.91 | 100.0 | 685 |
| Step_9_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_9_Inference | 6.85 | 31.27 | 3.7 | 300.77 | 100.0 | 685 |
| VAE_Decoding | 23.81 | 23.54 | 3.8 | 319.33 | 100.0 | 2381 |
| Total_Execution | 149.16 | 31.27 | 5.2 | 319.73 | 62.5 | 9330 |

### Inference Statistics

- **Avg Time per Step**: 6.86 s
- **Avg SM Activity**: 98.9 %
- **Avg CPU Utilization**: 4.1 %
- **Total Inference Load**: 6782

### Performance Analysis

**Bottlenecks Detected:**
- Inference stage 'Step_0_Inference' has low SM activity (89.57%), check kernel efficiency.

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
| Model_Initialization | 37.49 | 0.49 | 0.0 | 0.00 | 0.2 | 9 |
| T2V_Preprocess | 0.00 | 0.49 | 0.0 | 0.00 | 0.0 | 0 |
| T5_Encoding | 16.31 | 0.50 | 0.0 | 0.00 | 0.0 | 0 |
| Step_0_Loading | 4.62 | 53.74 | 0.0 | 0.00 | 22.0 | 102 |
| Step_0_Inference | 36.40 | 82.51 | 0.0 | 0.00 | 97.6 | 3552 |
| Step_1_Loading | 0.00 | 53.83 | 0.0 | 0.00 | 0.0 | 0 |
| Step_1_Inference | 36.47 | 82.57 | 0.0 | 0.00 | 100.0 | 3647 |
| Step_2_Loading | 0.00 | 53.87 | 0.0 | 0.00 | 0.0 | 0 |
| Step_2_Inference | 36.64 | 82.60 | 0.0 | 0.00 | 100.0 | 3664 |
| Step_3_Loading | 0.00 | 53.87 | 0.0 | 0.00 | 0.0 | 0 |
| Step_3_Inference | 36.64 | 82.60 | 0.0 | 0.00 | 100.0 | 3664 |
| Step_4_Loading | 69.81 | 53.87 | 0.0 | 0.00 | 4.5 | 316 |
| Step_4_Inference | 36.35 | 82.60 | 0.0 | 0.00 | 100.0 | 3635 |
| VAE_Decoding | 9.14 | 8.64 | 0.0 | 0.00 | 99.9 | 913 |
| Total_Execution | 342.16 | 82.60 | 0.0 | 0.00 | 57.2 | 19578 |

### Inference Statistics

- **Avg Time per Step**: 36.50 s
- **Avg SM Activity**: 99.5 %
- **Avg CPU Utilization**: 0.0 %
- **Total Inference Load**: 18162

### Performance Analysis

No significant bottlenecks detected. GPU utilization is healthy.

**Resource Usage Overview:**
- Peak GPU Memory reached 82.60 GB. High VRAM usage, close to 48GB limit on L40S.
---

