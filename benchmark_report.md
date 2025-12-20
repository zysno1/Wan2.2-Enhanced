# Wan2.2 Benchmark Report

| Case                   | Res        | Offload |  Time(s) | s/step | Mem(GB) | SM(%) |   Load |
|------------------------|------------|---------|----------|--------|---------|-------|--------|
| 01_Speed_Preview_480p  | 1280*704   | True    |   126.25 |   6.87 |   31.27 | 100.0 |  11685 |
| 02_Efficiency_Mode_720p | 1280*704   | True    |   168.78 |   6.86 |   31.27 |  99.9 |  18511 |
| 03_Performance_Mode_720p | 1280*704   | False   |   150.43 |   6.87 |   42.17 |  98.5 |  18358 |

# Detailed Breakdown

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

