# Wan2.2 Benchmark Report

| Case                   | Res        | Offload |  Time(s) | s/step | Mem(GB) | SM(%) |   Load |
|------------------------|------------|---------|----------|--------|---------|-------|--------|
| 01_Speed_Preview_480p  | 1280*704   | True    |   121.86 |   6.88 |   31.27 |  97.2 |  11692 |
| 02_Efficiency_Mode_720p | 1280*704   | True    |   155.61 |   6.86 |   31.27 |  99.9 |  18574 |
| 03_Performance_Mode_720p | 1280*704   | False   |   150.03 |   6.86 |   42.17 |  98.6 |  18388 |


# Detailed Breakdown

## Case: 01_Speed_Preview_480p

- **Total Duration**: 121.86 s
- **Peak Memory**: 31.27 GB
- **Total Compute Load**: 11692

### Stage Breakdown

| Stage | Time (s) | Peak Mem (GB) | SM Act (%) | Comp Load |
| :--- | :--- | :--- | :--- | :--- |
| Model_Initialization | 39.35 | 2.63 | 0.2 | 7 |
| TI2V_Preprocess | 0.00 | 2.63 | 0.0 | 0 |
| T5_Encoding | 11.79 | 2.64 | 0.0 | 0 |
| Step_0_Loading | 0.01 | 21.34 | 0.0 | 0 |
| Step_0_Inference | 7.02 | 31.12 | 86.9 | 610 |
| Step_1_Loading | 0.00 | 21.48 | 0.0 | 0 |
| Step_1_Inference | 6.83 | 31.22 | 99.0 | 676 |
| Step_2_Loading | 0.00 | 21.55 | 0.0 | 0 |
| Step_2_Inference | 6.86 | 31.27 | 100.0 | 686 |
| Step_3_Loading | 0.00 | 21.56 | 0.0 | 0 |
| Step_3_Inference | 6.84 | 31.27 | 100.0 | 684 |
| Step_4_Loading | 0.00 | 21.56 | 0.0 | 0 |
| Step_4_Inference | 6.84 | 31.27 | 100.0 | 684 |
| VAE_Decoding | 23.77 | 23.54 | 100.0 | 2377 |
| Total_Execution | 121.75 | 31.27 | 49.0 | 5968 |

### Inference Statistics

- **Avg Time per Step**: 6.88 s
- **Avg SM Activity**: 97.2 %
- **Total Inference Load**: 3340

---

## Case: 02_Efficiency_Mode_720p

- **Total Duration**: 155.61 s
- **Peak Memory**: 31.27 GB
- **Total Compute Load**: 18574

### Stage Breakdown

| Stage | Time (s) | Peak Mem (GB) | SM Act (%) | Comp Load |
| :--- | :--- | :--- | :--- | :--- |
| Model_Initialization | 39.73 | 2.63 | 0.0 | 0 |
| TI2V_Preprocess | 0.00 | 2.63 | 0.0 | 0 |
| T5_Encoding | 11.54 | 2.64 | 0.0 | 0 |
| Step_0_Loading | 0.00 | 21.34 | 0.0 | 0 |
| Step_0_Inference | 6.97 | 31.12 | 100.0 | 697 |
| Step_1_Loading | 0.00 | 21.48 | 0.0 | 0 |
| Step_1_Inference | 6.84 | 31.22 | 100.0 | 684 |
| Step_2_Loading | 0.00 | 21.55 | 0.0 | 0 |
| Step_2_Inference | 6.87 | 31.27 | 99.4 | 683 |
| Step_3_Loading | 0.00 | 21.56 | 0.0 | 0 |
| Step_3_Inference | 6.85 | 31.27 | 100.0 | 685 |
| Step_4_Loading | 0.00 | 21.56 | 0.0 | 0 |
| Step_4_Inference | 6.84 | 31.27 | 100.0 | 684 |
| Step_5_Loading | 0.00 | 21.56 | 0.0 | 0 |
| Step_5_Inference | 6.84 | 31.27 | 100.0 | 684 |
| Step_6_Loading | 0.00 | 21.55 | 0.0 | 0 |
| Step_6_Inference | 6.85 | 31.27 | 100.0 | 685 |
| Step_7_Loading | 0.00 | 21.56 | 0.0 | 0 |
| Step_7_Inference | 6.85 | 31.27 | 99.4 | 681 |
| Step_8_Loading | 0.00 | 21.56 | 0.0 | 0 |
| Step_8_Inference | 6.85 | 31.27 | 100.0 | 685 |
| Step_9_Loading | 0.00 | 21.56 | 0.0 | 0 |
| Step_9_Inference | 6.85 | 31.27 | 100.0 | 685 |
| VAE_Decoding | 23.79 | 23.54 | 100.0 | 2379 |
| Total_Execution | 155.51 | 31.27 | 60.1 | 9342 |

### Inference Statistics

- **Avg Time per Step**: 6.86 s
- **Avg SM Activity**: 99.9 %
- **Total Inference Load**: 6853

---

## Case: 03_Performance_Mode_720p

- **Total Duration**: 150.03 s
- **Peak Memory**: 42.17 GB
- **Total Compute Load**: 18388

### Stage Breakdown

| Stage | Time (s) | Peak Mem (GB) | SM Act (%) | Comp Load |
| :--- | :--- | :--- | :--- | :--- |
| Model_Initialization | 40.45 | 2.63 | 0.0 | 0 |
| TI2V_Preprocess | 0.00 | 2.63 | 0.0 | 0 |
| T5_Encoding | 13.64 | 2.64 | 0.0 | 0 |
| Step_0_Loading | 0.00 | 21.34 | 0.0 | 0 |
| Step_0_Inference | 6.97 | 31.12 | 86.7 | 604 |
| Step_1_Loading | 0.00 | 21.48 | 0.0 | 0 |
| Step_1_Inference | 6.84 | 31.22 | 100.0 | 684 |
| Step_2_Loading | 0.00 | 21.55 | 0.0 | 0 |
| Step_2_Inference | 6.87 | 31.27 | 100.0 | 687 |
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
| Step_9_Inference | 6.86 | 31.27 | 100.0 | 686 |
| VAE_Decoding | 23.85 | 42.17 | 100.0 | 2385 |
| Total_Execution | 149.93 | 42.17 | 61.6 | 9239 |

### Inference Statistics

- **Avg Time per Step**: 6.86 s
- **Avg SM Activity**: 98.6 %
- **Total Inference Load**: 6764

---

