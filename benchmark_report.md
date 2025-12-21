# Wan2.2 Benchmark Report: Multi-GPU Comparison

## Performance Summary: L40S vs RTX PRO 6000

| Case | Resolution | L40S Time(s) | RTX 6000 Time(s) | Speedup (RTX vs L40S) |
|------|------------|--------------|------------------|-----------------------|
| 01_Speed_Preview_480p | 1280*704 | 269.38 | 114.94 | **2.34x** |
| 02_Efficiency_Mode_720p | 1280*704 | 322.66 | 147.19 | **2.19x** |
| 03_Performance_Mode_720p | 1280*704 | 319.90 | 149.29 | **2.14x** |

---

# Detailed Reports

## RTX PRO 6000 Blackwell Server Edition

| Case | Res | Offload | Time(s) | s/step | Mem(GB) | SM(%) | Load |
|------|-----|---------|---------|--------|---------|-------|------|
| 01_Speed_Preview_480p | 1280*704 | True | 114.94 | 6.87 | 31.27 | 99.8 | 11672 |
| 02_Efficiency_Mode_720p | 1280*704 | True | 147.19 | 6.86 | 31.27 | 98.7 | 18453 |
| 03_Performance_Mode_720p | 1280*704 | True | 149.29 | 6.86 | 31.27 | 98.9 | 18494 |

### Detailed Breakdown

#### Case: 01_5B_Speed_Preview_704p

- **Total Duration**: 143.25 s
- **Peak GPU Memory**: 31.27 GB
- **Total Compute Load**: 11546

##### Stage Breakdown

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

##### Inference Statistics

- **Avg Time per Step**: 6.91 s
- **Avg SM Activity**: 99.4 %
- **Avg CPU Utilization**: 0.0 %
- **Total Inference Load**: 3435

##### Performance Analysis

No significant bottlenecks detected. GPU utilization is healthy.

**Resource Usage Overview:**
- Peak GPU Memory reached 31.27 GB. VRAM usage is within safe margins.
---

#### Case: 01_Speed_Preview_480p

- **Total Duration**: 114.94 s
- **Peak GPU Memory**: 31.27 GB
- **Total Compute Load**: 11672

##### Stage Breakdown

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

##### Inference Statistics

- **Avg Time per Step**: 6.87 s
- **Avg SM Activity**: 99.8 %
- **Avg CPU Utilization**: 6.1 %
- **Total Inference Load**: 3431

##### Performance Analysis

No significant bottlenecks detected. GPU utilization is healthy.

**Resource Usage Overview:**
- Peak GPU Memory reached 31.27 GB. VRAM usage is within safe margins.
---

#### Case: 02_5B_Efficiency_Mode_704p

- **Total Duration**: 151.58 s
- **Peak GPU Memory**: 31.27 GB
- **Total Compute Load**: 18624

##### Stage Breakdown

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

##### Inference Statistics

- **Avg Time per Step**: 6.87 s
- **Avg SM Activity**: 99.9 %
- **Avg CPU Utilization**: 0.0 %
- **Total Inference Load**: 6865

##### Performance Analysis

No significant bottlenecks detected. GPU utilization is healthy.

**Resource Usage Overview:**
- Peak GPU Memory reached 31.27 GB. VRAM usage is within safe margins.
---

#### Case: 02_Efficiency_Mode_720p

- **Total Duration**: 147.19 s
- **Peak GPU Memory**: 31.27 GB
- **Total Compute Load**: 18453

##### Stage Breakdown

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

##### Inference Statistics

- **Avg Time per Step**: 6.86 s
- **Avg SM Activity**: 98.7 %
- **Avg CPU Utilization**: 3.9 %
- **Total Inference Load**: 6768

##### Performance Analysis

**Bottlenecks Detected:**
- Inference stage 'Step_0_Inference' has low SM activity (86.86%), check kernel efficiency.

**Resource Usage Overview:**
- Peak GPU Memory reached 31.27 GB. VRAM usage is within safe margins.
---

#### Case: 03_5B_Performance_Mode_704p

- **Total Duration**: 146.27 s
- **Peak GPU Memory**: 42.17 GB
- **Total Compute Load**: 18587

##### Stage Breakdown

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

##### Inference Statistics

- **Avg Time per Step**: 6.87 s
- **Avg SM Activity**: 99.9 %
- **Avg CPU Utilization**: 0.0 %
- **Total Inference Load**: 6870

##### Performance Analysis

No significant bottlenecks detected. GPU utilization is healthy.

**Resource Usage Overview:**
- Peak GPU Memory reached 42.17 GB. High VRAM usage, close to 48GB limit on L40S.
---

#### Case: 03_Performance_Mode_720p

- **Total Duration**: 149.29 s
- **Peak GPU Memory**: 31.27 GB
- **Total Compute Load**: 18494

##### Stage Breakdown

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

##### Inference Statistics

- **Avg Time per Step**: 6.86 s
- **Avg SM Activity**: 98.9 %
- **Avg CPU Utilization**: 4.1 %
- **Total Inference Load**: 6782

##### Performance Analysis

**Bottlenecks Detected:**
- Inference stage 'Step_0_Inference' has low SM activity (89.57%), check kernel efficiency.

**Resource Usage Overview:**
- Peak GPU Memory reached 31.27 GB. VRAM usage is within safe margins.
---

#### Case: 04_14B_Speed_Preview_480p

- **Total Duration**: 342.30 s
- **Peak GPU Memory**: 82.60 GB
- **Total Compute Load**: 39080

##### Stage Breakdown

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

##### Inference Statistics

- **Avg Time per Step**: 36.50 s
- **Avg SM Activity**: 99.5 %
- **Avg CPU Utilization**: 0.0 %
- **Total Inference Load**: 18162

##### Performance Analysis

No significant bottlenecks detected. GPU utilization is healthy.

**Resource Usage Overview:**
- Peak GPU Memory reached 82.60 GB. High VRAM usage, close to 48GB limit on L40S.
---

## L40S

| Case | Res | Offload | Time(s) | s/step | Mem(GB) | SM(%) | Load |
|------|-----|---------|---------|--------|---------|-------|------|
| 01_Speed_Preview_480p | 1280*704 | True | 269.38 | 12.57 | 31.27 | 99.4 | 21888 |
| 02_Efficiency_Mode_720p | 1280*704 | True | 322.66 | 12.64 | 31.27 | 99.8 | 34674 |
| 03_Performance_Mode_720p | 1280*704 | True | 319.90 | 12.66 | 31.27 | 99.7 | 34698 |

### Detailed Breakdown

#### Case: 01_Speed_Preview_480p

- **Total Duration**: 269.38 s
- **Peak GPU Memory**: 31.27 GB
- **Total Compute Load**: 21888

##### Stage Breakdown

| Stage | Time (s) | GPU Mem (GB) | CPU (%) | Sys Mem (GB) | SM Act (%) | Comp Load |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Model_Initialization | 88.49 | 2.63 | 24.6 | 146.31 | 0.3 | 25 |
| TI2V_Preprocess | 0.00 | 2.63 | 0.0 | 0.00 | 0.0 | 0 |
| T5_Encoding | 47.49 | 2.63 | 38.8 | 134.18 | 0.0 | 0 |
| Step_0_Loading | 0.01 | 21.34 | 0.0 | 133.60 | 0.0 | 0 |
| Step_0_Inference | 12.65 | 31.12 | 19.2 | 134.07 | 98.8 | 1249 |
| Step_1_Loading | 0.00 | 21.48 | 0.0 | 0.00 | 0.0 | 0 |
| Step_1_Inference | 12.47 | 31.22 | 34.9 | 134.38 | 99.1 | 1236 |
| Step_2_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_2_Inference | 12.56 | 31.27 | 35.5 | 134.42 | 99.3 | 1247 |
| Step_3_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_3_Inference | 12.56 | 31.27 | 21.9 | 134.47 | 100.0 | 1256 |
| Step_4_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_4_Inference | 12.62 | 31.27 | 9.9 | 133.83 | 100.0 | 1262 |
| VAE_Decoding | 45.60 | 23.54 | 23.7 | 153.07 | 99.9 | 4556 |
| Total_Execution | 269.21 | 31.27 | 26.4 | 153.66 | 41.1 | 11057 |

##### Inference Statistics

- **Avg Time per Step**: 12.57 s
- **Avg SM Activity**: 99.4 %
- **Avg CPU Utilization**: 24.3 %
- **Total Inference Load**: 6250

##### Performance Analysis

No significant bottlenecks detected. GPU utilization is healthy.

**Resource Usage Overview:**
- Peak GPU Memory reached 31.27 GB. VRAM usage is within safe margins.
---

#### Case: 02_Efficiency_Mode_720p

- **Total Duration**: 322.66 s
- **Peak GPU Memory**: 31.27 GB
- **Total Compute Load**: 34674

##### Stage Breakdown

| Stage | Time (s) | GPU Mem (GB) | CPU (%) | Sys Mem (GB) | SM Act (%) | Comp Load |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Model_Initialization | 84.80 | 2.63 | 29.6 | 145.86 | 0.0 | 0 |
| TI2V_Preprocess | 0.00 | 2.63 | 0.0 | 0.00 | 0.0 | 0 |
| T5_Encoding | 42.94 | 2.63 | 32.2 | 135.10 | 0.0 | 0 |
| Step_0_Loading | 0.01 | 21.34 | 0.0 | 0.00 | 0.0 | 0 |
| Step_0_Inference | 12.72 | 31.12 | 35.1 | 134.71 | 98.8 | 1257 |
| Step_1_Loading | 0.00 | 21.48 | 0.0 | 0.00 | 0.0 | 0 |
| Step_1_Inference | 12.50 | 31.22 | 12.3 | 134.58 | 100.0 | 1250 |
| Step_2_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_2_Inference | 12.60 | 31.27 | 21.8 | 134.59 | 99.8 | 1258 |
| Step_3_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_3_Inference | 12.63 | 31.27 | 34.4 | 134.75 | 100.0 | 1263 |
| Step_4_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_4_Inference | 12.64 | 31.27 | 34.4 | 134.86 | 100.0 | 1264 |
| Step_5_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_5_Inference | 12.64 | 31.27 | 22.2 | 134.84 | 99.5 | 1258 |
| Step_6_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_6_Inference | 12.63 | 31.27 | 9.4 | 134.20 | 100.0 | 1263 |
| Step_7_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_7_Inference | 12.71 | 31.27 | 31.0 | 134.31 | 99.9 | 1270 |
| Step_8_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_8_Inference | 12.69 | 31.27 | 34.6 | 134.37 | 100.0 | 1269 |
| Step_9_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_9_Inference | 12.64 | 31.27 | 34.3 | 134.51 | 100.0 | 1264 |
| VAE_Decoding | 45.88 | 23.54 | 30.1 | 153.41 | 99.9 | 4585 |
| Total_Execution | 322.50 | 31.27 | 27.9 | 154.17 | 54.2 | 17472 |

##### Inference Statistics

- **Avg Time per Step**: 12.64 s
- **Avg SM Activity**: 99.8 %
- **Avg CPU Utilization**: 26.9 %
- **Total Inference Load**: 12617

##### Performance Analysis

No significant bottlenecks detected. GPU utilization is healthy.

**Resource Usage Overview:**
- Peak GPU Memory reached 31.27 GB. VRAM usage is within safe margins.
---

#### Case: 03_Performance_Mode_720p

- **Total Duration**: 319.90 s
- **Peak GPU Memory**: 31.27 GB
- **Total Compute Load**: 34698

##### Stage Breakdown

| Stage | Time (s) | GPU Mem (GB) | CPU (%) | Sys Mem (GB) | SM Act (%) | Comp Load |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Model_Initialization | 86.19 | 2.63 | 27.0 | 145.80 | 0.3 | 23 |
| TI2V_Preprocess | 0.00 | 2.63 | 0.0 | 0.00 | 0.0 | 0 |
| T5_Encoding | 37.31 | 2.63 | 26.3 | 136.89 | 0.0 | 0 |
| Step_0_Loading | 0.01 | 21.34 | 0.0 | 0.00 | 0.0 | 0 |
| Step_0_Inference | 12.80 | 31.12 | 34.9 | 135.78 | 98.2 | 1256 |
| Step_1_Loading | 0.00 | 21.48 | 0.0 | 0.00 | 0.0 | 0 |
| Step_1_Inference | 12.52 | 31.22 | 34.4 | 135.73 | 99.3 | 1243 |
| Step_2_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_2_Inference | 12.63 | 31.27 | 26.4 | 135.73 | 100.0 | 1263 |
| Step_3_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_3_Inference | 12.61 | 31.27 | 9.8 | 134.89 | 100.0 | 1261 |
| Step_4_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_4_Inference | 12.61 | 31.27 | 28.5 | 134.99 | 99.9 | 1260 |
| Step_5_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_5_Inference | 12.63 | 31.27 | 33.3 | 134.74 | 99.8 | 1261 |
| Step_6_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_6_Inference | 12.68 | 31.27 | 35.0 | 134.83 | 100.0 | 1268 |
| Step_7_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_7_Inference | 12.69 | 31.27 | 12.0 | 134.82 | 99.9 | 1268 |
| Step_8_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_8_Inference | 12.70 | 31.27 | 19.9 | 134.17 | 100.0 | 1270 |
| Step_9_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_9_Inference | 12.70 | 31.27 | 34.7 | 134.33 | 100.0 | 1270 |
| VAE_Decoding | 45.90 | 23.54 | 24.1 | 153.30 | 100.0 | 4590 |
| Total_Execution | 319.75 | 31.27 | 26.9 | 153.64 | 54.6 | 17465 |

##### Inference Statistics

- **Avg Time per Step**: 12.66 s
- **Avg SM Activity**: 99.7 %
- **Avg CPU Utilization**: 26.9 %
- **Total Inference Load**: 12620

##### Performance Analysis

No significant bottlenecks detected. GPU utilization is healthy.

**Resource Usage Overview:**
- Peak GPU Memory reached 31.27 GB. VRAM usage is within safe margins.
