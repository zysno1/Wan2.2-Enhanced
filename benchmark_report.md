# Wan2.2 Benchmark Report

## Hardware Group A: NVIDIA L40S (48GB)

| Case | Res | Offload | Time(s) | s/step | Mem(GB) | SM(%) | Load |
|:---|:---|:---|:---|:---|:---|:---|:---|
| 01_Speed_Preview_480p | 1280*704 | True | 265.59 | 12.55 | 31.27 | 99.2 | 21795 |
| 02_Efficiency_Mode_720p | 1280*704 | True | 331.14 | 12.62 | 31.27 | 99.1 | 34636 |
| 03_Performance_Mode_720p | 1280*704 | True* | 324.00 | 12.64 | 31.27 | 99.2 | 34637 |

## Hardware Group B: NVIDIA RTX PRO 6000 Blackwell (96GB)

| Case | Res | Offload | Time(s) | s/step | Mem(GB) | SM(%) | Load |
|:---|:---|:---|:---|:---|:---|:---|:---|
| 01_Speed_Preview_480p | 1280*704 | True | 126.25 | 6.87 | 31.27 | 100.0 | 11685 |
| 02_Efficiency_Mode_720p | 1280*704 | True | 168.78 | 6.86 | 31.27 | 99.9 | 18511 |
| 03_Performance_Mode_720p | 1280*704 | False | 150.43 | 6.87 | 42.17 | 98.5 | 18358 |

# Detailed Breakdown (L40S)

## Case: 01_Speed_Preview_480p (L40S)

- **Total Duration**: 265.59 s
- **Peak Memory**: 31.27 GB
- **Total Compute Load**: 21795

### Stage Breakdown

| Stage | Time (s) | Peak Mem (GB) | SM Act (%) | Comp Load |
| :--- | :--- | :--- | :--- | :--- |
| Model_Initialization | 86.56 | 2.63 | 0.0 | 3 |
| TI2V_Preprocess | 0.00 | 2.63 | 0.0 | 0 |
| T5_Encoding | 46.27 | 2.63 | 0.0 | 0 |
| Step_0_Loading | 0.01 | 21.34 | 0.0 | 0 |
| Step_0_Inference | 12.68 | 31.12 | 99.4 | 1260 |
| Step_1_Loading | 0.00 | 21.48 | 0.0 | 0 |
| Step_1_Inference | 12.41 | 31.22 | 99.6 | 1236 |
| Step_2_Loading | 0.00 | 21.55 | 0.0 | 0 |
| Step_2_Inference | 12.52 | 31.27 | 99.2 | 1241 |
| Step_3_Loading | 0.00 | 21.56 | 0.0 | 0 |
| Step_3_Inference | 12.55 | 31.27 | 97.8 | 1228 |
| Step_4_Loading | 0.00 | 21.56 | 0.0 | 0 |
| Step_4_Inference | 12.60 | 31.27 | 100.0 | 1260 |
| VAE_Decoding | 45.70 | 23.54 | 99.9 | 4566 |
| Total_Execution | 265.43 | 31.27 | 41.4 | 11000 |

### Inference Statistics

- **Avg Time per Step**: 12.55 s
- **Avg SM Activity**: 99.2 %
- **Total Inference Load**: 6226

---

## Case: 02_Efficiency_Mode_720p (L40S)

- **Total Duration**: 331.14 s
- **Peak Memory**: 31.27 GB
- **Total Compute Load**: 34636

### Stage Breakdown

| Stage | Time (s) | Peak Mem (GB) | SM Act (%) | Comp Load |
| :--- | :--- | :--- | :--- | :--- |
| Model_Initialization | 89.46 | 2.63 | 0.3 | 29 |
| TI2V_Preprocess | 0.00 | 2.63 | 0.0 | 0 |
| T5_Encoding | 46.57 | 2.63 | 0.0 | 0 |
| Step_0_Loading | 0.01 | 21.34 | 0.0 | 0 |
| Step_0_Inference | 12.65 | 31.12 | 92.6 | 1172 |
| Step_1_Loading | 0.00 | 21.48 | 0.0 | 0 |
| Step_1_Inference | 12.46 | 31.22 | 100.0 | 1246 |
| Step_2_Loading | 0.00 | 21.55 | 0.0 | 0 |
| Step_2_Inference | 12.57 | 31.27 | 100.0 | 1257 |
| Step_3_Loading | 0.00 | 21.56 | 0.0 | 0 |
| Step_3_Inference | 12.60 | 31.27 | 100.0 | 1260 |
| Step_4_Loading | 0.00 | 21.56 | 0.0 | 0 |
| Step_4_Inference | 12.64 | 31.27 | 99.4 | 1256 |
| Step_5_Loading | 0.00 | 21.56 | 0.0 | 0 |
| Step_5_Inference | 12.62 | 31.27 | 100.0 | 1262 |
| Step_6_Loading | 0.00 | 21.55 | 0.0 | 0 |
| Step_6_Inference | 12.63 | 31.27 | 99.8 | 1261 |
| Step_7_Loading | 0.00 | 21.56 | 0.0 | 0 |
| Step_7_Inference | 12.67 | 31.27 | 99.6 | 1262 |
| Step_8_Loading | 0.00 | 21.56 | 0.0 | 0 |
| Step_8_Inference | 12.69 | 31.27 | 100.0 | 1269 |
| Step_9_Loading | 0.00 | 21.56 | 0.0 | 0 |
| Step_9_Inference | 12.65 | 31.27 | 99.8 | 1263 |
| VAE_Decoding | 45.92 | 23.54 | 100.0 | 4592 |
| Total_Execution | 330.92 | 31.27 | 52.9 | 17506 |

### Inference Statistics

- **Avg Time per Step**: 12.62 s
- **Avg SM Activity**: 99.1 %
- **Total Inference Load**: 12509

---

## Case: 03_Performance_Mode_720p (L40S)

- **Total Duration**: 324.00 s
- **Peak Memory**: 31.27 GB
- **Total Compute Load**: 34637

### Stage Breakdown

| Stage | Time (s) | Peak Mem (GB) | SM Act (%) | Comp Load |
| :--- | :--- | :--- | :--- | :--- |
| Model_Initialization | 83.91 | 2.63 | 0.0 | 0 |
| TI2V_Preprocess | 0.00 | 2.63 | 0.0 | 0 |
| T5_Encoding | 46.10 | 2.63 | 0.0 | 0 |
| ... (Steps similar to Case 02) ... | ... | ... | ... | ... |
| VAE_Decoding | 46.12 | 23.54 | 99.8 | 4602 |

*Note: Case 03 on L40S uses Offload=True, so performance is identical to Case 02.*

---

# Detailed Breakdown (RTX PRO 6000 Blackwell)

## Case: 01_Speed_Preview_480p

- **Total Duration**: 126.25 s
- **Peak Memory**: 31.27 GB
- **Total Compute Load**: 11685

### Stage Breakdown

| Stage | Time (s) | Peak Mem (GB) | SM Act (%) | Comp Load |
| :--- | :--- | :--- | :--- | :--- |
| Model_Initialization | 42.28 | 2.63 | 0.6 | 27 |
| TI2V_Preprocess | 0.00 | 2.63 | 0.0 | 0 |
| T5_Encoding | 12.10 | 2.63 | 0.0 | 0 |
| Step_0_Loading | 0.00 | 21.34 | 0.0 | 0 |
| Step_0_Inference | 6.97 | 31.12 | 100.0 | 697 |
| Step_1_Loading | 0.00 | 21.48 | 0.0 | 0 |
| Step_1_Inference | 6.83 | 31.22 | 100.0 | 683 |
| Step_2_Loading | 0.00 | 21.55 | 0.0 | 0 |
| Step_2_Inference | 6.87 | 31.27 | 100.0 | 687 |
| Step_3_Loading | 0.00 | 21.56 | 0.0 | 0 |
| Step_3_Inference | 6.84 | 31.27 | 100.0 | 684 |
| Step_4_Loading | 0.00 | 21.56 | 0.0 | 0 |
| Step_4_Inference | 6.84 | 31.27 | 100.0 | 684 |
| VAE_Decoding | 23.78 | 23.54 | 98.2 | 2335 |
| Total_Execution | 126.14 | 31.27 | 46.7 | 5887 |

### Inference Statistics

- **Avg Time per Step**: 6.87 s
- **Avg SM Activity**: 100.0 %
- **Total Inference Load**: 3435

---

## Case: 02_Efficiency_Mode_720p

- **Total Duration**: 168.78 s
- **Peak Memory**: 31.27 GB
- **Total Compute Load**: 18511

### Stage Breakdown

| Stage | Time (s) | Peak Mem (GB) | SM Act (%) | Comp Load |
| :--- | :--- | :--- | :--- | :--- |
| Model_Initialization | 43.59 | 2.63 | 0.0 | 1 |
| TI2V_Preprocess | 0.00 | 2.63 | 0.0 | 0 |
| T5_Encoding | 14.67 | 2.63 | 0.0 | 0 |
| Step_0_Loading | 0.00 | 21.34 | 0.0 | 0 |
| Step_0_Inference | 6.98 | 31.12 | 100.0 | 698 |
| Step_1_Loading | 0.00 | 21.48 | 0.0 | 0 |
| Step_1_Inference | 6.83 | 31.22 | 100.0 | 683 |
| Step_2_Loading | 0.00 | 21.55 | 0.0 | 0 |
| Step_2_Inference | 6.87 | 31.27 | 100.0 | 687 |
| Step_3_Loading | 0.00 | 21.56 | 0.0 | 0 |
| Step_3_Inference | 6.84 | 31.27 | 100.0 | 684 |
| Step_4_Loading | 0.00 | 21.56 | 0.0 | 0 |
| Step_4_Inference | 6.84 | 31.27 | 99.9 | 683 |
| Step_5_Loading | 0.00 | 21.56 | 0.0 | 0 |
| Step_5_Inference | 6.84 | 31.27 | 100.0 | 684 |
| Step_6_Loading | 0.00 | 21.55 | 0.0 | 0 |
| Step_6_Inference | 6.85 | 31.27 | 100.0 | 685 |
| Step_7_Loading | 0.00 | 21.56 | 0.0 | 0 |
| Step_7_Inference | 6.85 | 31.27 | 99.3 | 680 |
| Step_8_Loading | 0.00 | 21.56 | 0.0 | 0 |
| Step_8_Inference | 6.85 | 31.27 | 100.0 | 685 |
| Step_9_Loading | 0.00 | 21.56 | 0.0 | 0 |
| Step_9_Inference | 6.85 | 31.27 | 100.0 | 685 |
| VAE_Decoding | 23.80 | 23.54 | 98.1 | 2335 |
| Total_Execution | 168.68 | 31.27 | 55.2 | 9320 |

### Inference Statistics

- **Avg Time per Step**: 6.86 s
- **Avg SM Activity**: 99.9 %
- **Total Inference Load**: 6855

---

## Case: 03_Performance_Mode_720p

- **Total Duration**: 150.43 s
- **Peak Memory**: 42.17 GB
- **Total Compute Load**: 18358

### Stage Breakdown

| Stage | Time (s) | Peak Mem (GB) | SM Act (%) | Comp Load |
| :--- | :--- | :--- | :--- | :--- |
| Model_Initialization | 40.54 | 2.63 | 0.0 | 0 |
| TI2V_Preprocess | 0.00 | 2.63 | 0.0 | 0 |
| T5_Encoding | 12.68 | 2.63 | 0.0 | 0 |
| Step_0_Loading | 0.00 | 21.34 | 0.0 | 0 |
| Step_0_Inference | 6.98 | 31.12 | 86.0 | 600 |
| Step_1_Loading | 0.00 | 21.48 | 0.0 | 0 |
| Step_1_Inference | 6.85 | 31.22 | 100.0 | 685 |
| Step_2_Loading | 0.00 | 21.55 | 0.0 | 0 |
| Step_2_Inference | 6.88 | 31.27 | 100.0 | 688 |
| Step_3_Loading | 0.00 | 21.56 | 0.0 | 0 |
| Step_3_Inference | 6.85 | 31.27 | 100.0 | 685 |
| Step_4_Loading | 0.00 | 21.56 | 0.0 | 0 |
| Step_4_Inference | 6.85 | 31.27 | 100.0 | 685 |
| Step_5_Loading | 0.00 | 21.56 | 0.0 | 0 |
| Step_5_Inference | 6.85 | 31.27 | 99.0 | 678 |
| Step_6_Loading | 0.00 | 21.55 | 0.0 | 0 |
| Step_6_Inference | 6.85 | 31.27 | 100.0 | 685 |
| Step_7_Loading | 0.00 | 21.56 | 0.0 | 0 |
| Step_7_Inference | 6.85 | 31.27 | 100.0 | 685 |
| Step_8_Loading | 0.00 | 21.56 | 0.0 | 0 |
| Step_8_Inference | 6.85 | 31.27 | 100.0 | 685 |
| Step_9_Loading | 0.00 | 21.56 | 0.0 | 0 |
| Step_9_Inference | 6.85 | 31.27 | 100.0 | 685 |
| VAE_Decoding | 23.84 | 42.17 | 100.0 | 2384 |
| Total_Execution | 150.33 | 42.17 | 61.3 | 9214 |

### Inference Statistics

- **Avg Time per Step**: 6.87 s
- **Avg SM Activity**: 98.5 %
- **Total Inference Load**: 6760

---

