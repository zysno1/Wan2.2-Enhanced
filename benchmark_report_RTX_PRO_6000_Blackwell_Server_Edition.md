# Wan2.2 Benchmark Report

| Case                   | Res        | Offload |  Time(s) | s/step | Mem(GB) | SM(%) |   Load |
|------------------------|------------|---------|----------|--------|---------|-------|--------|
| 01_Speed_Preview_704p  | 1280*704   | True    |   144.27 |   6.93 |   31.27 |  98.7 |      0 |
| 02_Efficiency_Quality_704p | 1280*704   | True    |   569.13 |  15.06 |   31.27 | 100.0 |      0 |
| 04_15s_50steps_720p    | 1280*704   | True    |  2197.13 |  41.53 |   43.46 | 100.0 |      0 |

# Detailed Breakdown

## Case: 01_Speed_Preview_704p

- **Total Duration**: 144.27 s
- **Peak GPU Memory**: 31.27 GB
- **Total Compute Load**: 0

### Stage Breakdown

| Stage | Time (s) | GPU Mem (GB) | CPU (%) | Sys Mem (GB) | SM Act (%) | Comp Load |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Model_Initialization | 39.39 | 2.63 | 9.1 | 329.50 | 80.6 | 0 |
| TI2V_Preprocess | 0.00 | 2.63 | 0.0 | 0.00 | 0.0 | 0 |
| T5_Encoding | 13.05 | 2.63 | 16.9 | 319.59 | 23.3 | 0 |
| Step_0_Loading | 0.00 | 21.34 | 0.0 | 0.00 | 0.0 | 0 |
| Step_0_Inference | 7.09 | 31.12 | 7.8 | 288.23 | 93.8 | 0 |
| Step_1_Loading | 0.00 | 21.48 | 0.0 | 0.00 | 0.0 | 0 |
| Step_1_Inference | 6.88 | 31.22 | 8.0 | 294.19 | 99.9 | 0 |
| Step_2_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_2_Inference | 6.90 | 31.27 | 8.0 | 302.96 | 99.9 | 0 |
| Step_3_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_3_Inference | 6.88 | 31.27 | 13.3 | 309.59 | 100.0 | 0 |
| Step_4_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_4_Inference | 6.88 | 31.27 | 17.0 | 310.43 | 100.0 | 0 |
| VAE_Decoding | 42.39 | 23.54 | 12.9 | 330.96 | 99.5 | 0 |
| Total_Execution | 143.96 | 31.27 | 12.2 | 330.96 | 80.0 | 0 |

### Inference Statistics

- **Avg Time per Step**: 6.93 s
- **Avg SM Activity**: 98.7 %
- **Avg CPU Utilization**: 10.8 %
- **Total Inference Load**: 0

### Performance Analysis

**Bottlenecks Detected:**
- Low overall GPU utilization (0.0%), suggesting potential CPU bottlenecks or data loading overhead.

**Resource Usage Overview:**
- Peak GPU Memory reached 31.27 GB. VRAM usage is within safe margins.
---

## Case: 02_Efficiency_Quality_704p

- **Total Duration**: 569.13 s
- **Peak GPU Memory**: 31.27 GB
- **Total Compute Load**: 0

### Stage Breakdown

| Stage | Time (s) | GPU Mem (GB) | CPU (%) | Sys Mem (GB) | SM Act (%) | Comp Load |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Model_Initialization | 40.03 | 2.63 | 8.0 | 295.15 | 99.9 | 0 |
| TI2V_Preprocess | 0.00 | 2.63 | 0.0 | 0.00 | 0.0 | 0 |
| T5_Encoding | 12.62 | 2.63 | 16.5 | 286.37 | 98.6 | 0 |
| Step_0_Loading | 0.01 | 21.34 | 0.0 | 0.00 | 0.0 | 0 |
| Step_0_Inference | 15.22 | 31.12 | 6.7 | 285.67 | 100.0 | 0 |
| Step_1_Loading | 0.00 | 21.48 | 0.0 | 0.00 | 0.0 | 0 |
| Step_1_Inference | 15.07 | 31.22 | 6.7 | 285.45 | 100.0 | 0 |
| Step_2_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_2_Inference | 15.10 | 31.27 | 6.9 | 285.22 | 100.0 | 0 |
| Step_3_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_3_Inference | 15.06 | 31.27 | 7.5 | 285.06 | 100.0 | 0 |
| Step_4_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_4_Inference | 15.07 | 31.27 | 7.4 | 285.11 | 100.0 | 0 |
| Step_5_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_5_Inference | 15.06 | 31.27 | 7.6 | 285.14 | 100.0 | 0 |
| Step_6_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_6_Inference | 15.06 | 31.27 | 8.1 | 284.99 | 100.0 | 0 |
| Step_7_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_7_Inference | 15.06 | 31.27 | 7.2 | 284.96 | 100.0 | 0 |
| Step_8_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_8_Inference | 15.06 | 31.27 | 7.2 | 284.73 | 100.0 | 0 |
| Step_9_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_9_Inference | 15.06 | 31.27 | 7.6 | 284.63 | 100.0 | 0 |
| Step_10_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_10_Inference | 15.06 | 31.27 | 7.8 | 284.69 | 100.0 | 0 |
| Step_11_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_11_Inference | 15.05 | 31.27 | 7.8 | 284.66 | 100.0 | 0 |
| Step_12_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_12_Inference | 15.05 | 31.27 | 7.5 | 284.72 | 100.0 | 0 |
| Step_13_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_13_Inference | 15.06 | 31.27 | 7.7 | 284.70 | 100.0 | 0 |
| Step_14_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_14_Inference | 15.06 | 31.27 | 7.7 | 284.80 | 100.0 | 0 |
| Step_15_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_15_Inference | 15.05 | 31.27 | 7.9 | 284.84 | 100.0 | 0 |
| Step_16_Loading | 0.00 | 21.56 | 7.1 | 284.76 | 0.0 | 0 |
| Step_16_Inference | 15.06 | 31.27 | 7.5 | 284.85 | 100.0 | 0 |
| Step_17_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_17_Inference | 15.05 | 31.27 | 7.7 | 284.75 | 100.0 | 0 |
| Step_18_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_18_Inference | 15.06 | 31.27 | 7.8 | 284.76 | 100.0 | 0 |
| Step_19_Loading | 0.00 | 21.56 | 7.1 | 284.68 | 100.0 | 0 |
| Step_19_Inference | 15.06 | 31.27 | 8.1 | 284.79 | 100.0 | 0 |
| Step_20_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_20_Inference | 15.06 | 31.27 | 7.9 | 285.02 | 100.0 | 0 |
| Step_21_Loading | 0.00 | 21.56 | 7.4 | 284.87 | 0.0 | 0 |
| Step_21_Inference | 15.05 | 31.27 | 8.0 | 284.91 | 100.0 | 0 |
| Step_22_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_22_Inference | 15.05 | 31.27 | 7.9 | 284.86 | 100.0 | 0 |
| Step_23_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_23_Inference | 15.06 | 31.27 | 8.0 | 284.82 | 100.0 | 0 |
| Step_24_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_24_Inference | 15.06 | 31.27 | 6.9 | 284.70 | 100.0 | 0 |
| Step_25_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_25_Inference | 15.06 | 31.27 | 6.8 | 284.69 | 100.0 | 0 |
| Step_26_Loading | 0.00 | 21.55 | 0.0 | 0.00 | 0.0 | 0 |
| Step_26_Inference | 15.05 | 31.27 | 7.4 | 286.97 | 100.0 | 0 |
| Step_27_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_27_Inference | 15.05 | 31.27 | 7.3 | 287.00 | 100.0 | 0 |
| Step_28_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_28_Inference | 15.05 | 31.27 | 6.6 | 286.77 | 100.0 | 0 |
| Step_29_Loading | 0.00 | 21.56 | 0.0 | 0.00 | 0.0 | 0 |
| Step_29_Inference | 15.04 | 31.27 | 8.0 | 289.11 | 100.0 | 0 |
| VAE_Decoding | 52.16 | 23.54 | 7.5 | 307.34 | 100.0 | 0 |
| Total_Execution | 568.90 | 31.27 | 7.7 | 308.03 | 100.0 | 0 |

### Inference Statistics

- **Avg Time per Step**: 15.06 s
- **Avg SM Activity**: 100.0 %
- **Avg CPU Utilization**: 7.5 %
- **Total Inference Load**: 0

### Performance Analysis

**Bottlenecks Detected:**
- Low overall GPU utilization (0.0%), suggesting potential CPU bottlenecks or data loading overhead.

**Resource Usage Overview:**
- Peak GPU Memory reached 31.27 GB. VRAM usage is within safe margins.
---

## Case: 03_Max_Quality_704p

- **Total Duration**: 707.29 s
- **Peak GPU Memory**: 52.76 GB
- **Total Compute Load**: 0

### Stage Breakdown

| Stage | Time (s) | GPU Mem (GB) | CPU (%) | Sys Mem (GB) | SM Act (%) | Comp Load |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Model_Initialization | 39.83 | 2.63 | 14.5 | 330.96 | 77.2 | 0 |
| TI2V_Preprocess | 0.00 | 2.63 | 0.0 | 0.00 | 0.0 | 0 |
| T5_Encoding | 1.36 | 13.47 | 17.1 | 322.22 | 100.0 | 0 |
| Step_0_Loading | 0.01 | 31.94 | 0.0 | 0.00 | 0.0 | 0 |
| Step_0_Inference | 15.13 | 41.71 | 15.8 | 319.82 | 100.0 | 0 |
| Step_1_Loading | 0.00 | 32.07 | 8.5 | 311.73 | 0.0 | 0 |
| Step_1_Inference | 15.07 | 41.81 | 8.9 | 313.11 | 100.0 | 0 |
| Step_2_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_2_Inference | 8.84 | 41.86 | 8.1 | 303.01 | 100.0 | 0 |
| Step_3_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_3_Inference | 6.88 | 41.86 | 6.6 | 272.00 | 98.9 | 0 |
| Step_4_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_4_Inference | 6.89 | 41.86 | 6.7 | 280.49 | 100.0 | 0 |
| Step_5_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_5_Inference | 6.88 | 41.86 | 6.7 | 289.34 | 100.0 | 0 |
| Step_6_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_6_Inference | 6.88 | 41.86 | 6.7 | 293.25 | 99.9 | 0 |
| Step_7_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_7_Inference | 6.89 | 41.86 | 6.9 | 293.31 | 100.0 | 0 |
| Step_8_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_8_Inference | 6.92 | 41.86 | 13.9 | 295.18 | 100.0 | 0 |
| Step_9_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_9_Inference | 6.96 | 41.86 | 9.1 | 293.83 | 99.5 | 0 |
| Step_10_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_10_Inference | 7.00 | 41.86 | 16.9 | 286.37 | 98.4 | 0 |
| Step_11_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_11_Inference | 7.03 | 41.86 | 12.2 | 285.54 | 99.1 | 0 |
| Step_12_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_12_Inference | 13.63 | 41.86 | 6.7 | 285.67 | 100.0 | 0 |
| Step_13_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_13_Inference | 15.06 | 41.86 | 6.7 | 285.51 | 100.0 | 0 |
| Step_14_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_14_Inference | 15.06 | 41.86 | 6.9 | 285.27 | 100.0 | 0 |
| Step_15_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_15_Inference | 15.01 | 41.86 | 7.3 | 285.07 | 100.0 | 0 |
| Step_16_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_16_Inference | 15.05 | 41.86 | 7.5 | 285.04 | 100.0 | 0 |
| Step_17_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_17_Inference | 15.05 | 41.86 | 7.5 | 285.14 | 100.0 | 0 |
| Step_18_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_18_Inference | 15.06 | 41.86 | 8.1 | 284.99 | 100.0 | 0 |
| Step_19_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_19_Inference | 15.06 | 41.86 | 7.4 | 284.96 | 100.0 | 0 |
| Step_20_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_20_Inference | 15.06 | 41.86 | 7.0 | 284.77 | 100.0 | 0 |
| Step_21_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_21_Inference | 15.05 | 41.86 | 7.6 | 284.63 | 100.0 | 0 |
| Step_22_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_22_Inference | 15.05 | 41.86 | 7.9 | 284.69 | 100.0 | 0 |
| Step_23_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_23_Inference | 15.05 | 41.86 | 7.9 | 284.62 | 100.0 | 0 |
| Step_24_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 100.0 | 0 |
| Step_24_Inference | 15.05 | 41.86 | 7.5 | 284.71 | 100.0 | 0 |
| Step_25_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_25_Inference | 15.06 | 41.86 | 7.6 | 284.73 | 100.0 | 0 |
| Step_26_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_26_Inference | 15.05 | 41.86 | 7.8 | 284.80 | 100.0 | 0 |
| Step_27_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_27_Inference | 15.05 | 41.86 | 7.9 | 284.84 | 100.0 | 0 |
| Step_28_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_28_Inference | 15.05 | 41.86 | 7.4 | 284.85 | 100.0 | 0 |
| Step_29_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_29_Inference | 15.05 | 41.86 | 7.5 | 284.72 | 100.0 | 0 |
| Step_30_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_30_Inference | 15.06 | 41.86 | 8.0 | 284.77 | 100.0 | 0 |
| Step_31_Loading | 0.00 | 32.14 | 7.1 | 284.69 | 0.0 | 0 |
| Step_31_Inference | 15.06 | 41.86 | 8.1 | 284.75 | 100.0 | 0 |
| Step_32_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_32_Inference | 15.06 | 41.86 | 7.9 | 285.01 | 100.0 | 0 |
| Step_33_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_33_Inference | 15.06 | 41.86 | 7.9 | 284.92 | 100.0 | 0 |
| Step_34_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_34_Inference | 15.05 | 41.86 | 8.0 | 284.87 | 100.0 | 0 |
| Step_35_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_35_Inference | 15.06 | 41.86 | 8.0 | 284.83 | 100.0 | 0 |
| Step_36_Loading | 0.00 | 32.14 | 0.0 | 284.66 | 0.0 | 0 |
| Step_36_Inference | 15.05 | 41.86 | 7.1 | 284.68 | 100.0 | 0 |
| Step_37_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_37_Inference | 15.06 | 41.86 | 6.5 | 284.69 | 100.0 | 0 |
| Step_38_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_38_Inference | 15.05 | 41.86 | 6.8 | 284.60 | 100.0 | 0 |
| Step_39_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_39_Inference | 15.05 | 41.86 | 8.1 | 287.00 | 100.0 | 0 |
| Step_40_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_40_Inference | 15.05 | 41.86 | 6.6 | 286.78 | 100.0 | 0 |
| Step_41_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_41_Inference | 15.05 | 41.86 | 7.6 | 289.11 | 100.0 | 0 |
| Step_42_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_42_Inference | 8.44 | 41.86 | 7.9 | 306.06 | 100.0 | 0 |
| Step_43_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_43_Inference | 14.41 | 41.86 | 7.5 | 307.34 | 99.9 | 0 |
| Step_44_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_44_Inference | 15.08 | 41.86 | 7.6 | 307.24 | 100.0 | 0 |
| Step_45_Loading | 0.00 | 32.14 | 6.6 | 307.10 | 0.0 | 0 |
| Step_45_Inference | 15.08 | 41.86 | 7.5 | 307.10 | 100.0 | 0 |
| Step_46_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_46_Inference | 11.26 | 41.86 | 8.6 | 308.03 | 100.0 | 0 |
| Step_47_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_47_Inference | 6.89 | 41.86 | 7.5 | 278.01 | 99.7 | 0 |
| Step_48_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_48_Inference | 6.89 | 41.86 | 9.3 | 283.05 | 100.0 | 0 |
| Step_49_Loading | 0.00 | 32.14 | 0.0 | 0.00 | 0.0 | 0 |
| Step_49_Inference | 6.88 | 41.86 | 16.8 | 293.29 | 99.6 | 0 |
| VAE_Decoding | 24.08 | 52.76 | 18.8 | 302.98 | 99.3 | 0 |
| Total_Execution | 707.03 | 52.76 | 8.9 | 330.96 | 98.4 | 0 |

### Inference Statistics

- **Avg Time per Step**: 12.73 s
- **Avg SM Activity**: 99.9 %
- **Avg CPU Utilization**: 8.3 %
- **Total Inference Load**: 0

### Performance Analysis

**Bottlenecks Detected:**
- Low overall GPU utilization (0.0%), suggesting potential CPU bottlenecks or data loading overhead.

**Resource Usage Overview:**
- Peak GPU Memory reached 52.76 GB. High VRAM usage, close to 48GB limit on L40S.
---

## Case: 04_15s_50steps_720p

- **Total Duration**: 2197.13 s
- **Peak GPU Memory**: 43.46 GB
- **Total Compute Load**: 0

### Stage Breakdown

| Stage | Time (s) | GPU Mem (GB) | CPU (%) | Sys Mem (GB) | SM Act (%) | Comp Load |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Model_Initialization | 39.22 | 2.63 | 9.0 | 350.93 | 99.9 | 0 |
| TI2V_Preprocess | 0.00 | 2.63 | 0.0 | 0.00 | 0.0 | 0 |
| T5_Encoding | 13.03 | 2.63 | 16.9 | 341.71 | 98.7 | 0 |
| Step_0_Loading | 0.01 | 21.43 | 0.0 | 0.00 | 0.0 | 0 |
| Step_0_Inference | 48.78 | 43.12 | 7.5 | 341.37 | 100.0 | 0 |
| Step_1_Loading | 0.00 | 21.73 | 0.0 | 0.00 | 0.0 | 0 |
| Step_1_Inference | 48.54 | 43.34 | 9.5 | 344.41 | 100.0 | 0 |
| Step_2_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_2_Inference | 48.55 | 43.46 | 7.9 | 344.47 | 100.0 | 0 |
| Step_3_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_3_Inference | 48.40 | 43.46 | 6.0 | 342.47 | 100.0 | 0 |
| Step_4_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_4_Inference | 48.38 | 43.46 | 6.3 | 342.33 | 100.0 | 0 |
| Step_5_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_5_Inference | 48.45 | 43.46 | 13.3 | 342.44 | 100.0 | 0 |
| Step_6_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_6_Inference | 48.51 | 43.46 | 13.4 | 344.61 | 100.0 | 0 |
| Step_7_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_7_Inference | 48.50 | 43.46 | 7.8 | 325.70 | 100.0 | 0 |
| Step_8_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_8_Inference | 48.48 | 43.46 | 8.6 | 329.68 | 100.0 | 0 |
| Step_9_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_9_Inference | 48.44 | 43.46 | 10.2 | 331.55 | 100.0 | 0 |
| Step_10_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_10_Inference | 48.46 | 43.46 | 12.1 | 332.37 | 100.0 | 0 |
| Step_11_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_11_Inference | 48.45 | 43.46 | 13.7 | 341.52 | 100.0 | 0 |
| Step_12_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_12_Inference | 48.48 | 43.46 | 7.8 | 326.37 | 100.0 | 0 |
| Step_13_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_13_Inference | 48.47 | 43.46 | 8.0 | 326.06 | 100.0 | 0 |
| Step_14_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_14_Inference | 48.47 | 43.46 | 8.0 | 326.01 | 100.0 | 0 |
| Step_15_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_15_Inference | 48.47 | 43.46 | 8.0 | 325.96 | 100.0 | 0 |
| Step_16_Loading | 0.00 | 21.90 | 7.2 | 325.88 | 0.0 | 0 |
| Step_16_Inference | 48.47 | 43.46 | 8.0 | 326.02 | 100.0 | 0 |
| Step_17_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_17_Inference | 48.48 | 43.46 | 7.8 | 325.98 | 100.0 | 0 |
| Step_18_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_18_Inference | 48.49 | 43.46 | 8.8 | 326.03 | 100.0 | 0 |
| Step_19_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_19_Inference | 48.47 | 43.46 | 9.5 | 327.52 | 100.0 | 0 |
| Step_20_Loading | 0.00 | 21.90 | 12.7 | 326.19 | 0.0 | 0 |
| Step_20_Inference | 48.47 | 43.46 | 7.9 | 326.21 | 100.0 | 0 |
| Step_21_Loading | 0.00 | 21.90 | 0.0 | 326.08 | 0.0 | 0 |
| Step_21_Inference | 48.45 | 43.46 | 8.1 | 328.75 | 100.0 | 0 |
| Step_22_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_22_Inference | 48.48 | 43.46 | 8.5 | 330.91 | 100.0 | 0 |
| Step_23_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 100.0 | 0 |
| Step_23_Inference | 48.50 | 43.46 | 8.8 | 330.73 | 100.0 | 0 |
| Step_24_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_24_Inference | 48.49 | 43.46 | 16.9 | 341.52 | 100.0 | 0 |
| Step_25_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_25_Inference | 48.51 | 43.46 | 8.0 | 326.62 | 100.0 | 0 |
| Step_26_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_26_Inference | 48.51 | 43.46 | 7.8 | 326.45 | 100.0 | 0 |
| Step_27_Loading | 0.00 | 21.90 | 0.0 | 326.22 | 0.0 | 0 |
| Step_27_Inference | 48.53 | 43.46 | 8.0 | 326.24 | 100.0 | 0 |
| Step_28_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_28_Inference | 48.54 | 43.46 | 7.9 | 326.19 | 100.0 | 0 |
| Step_29_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_29_Inference | 48.55 | 43.46 | 8.0 | 326.19 | 100.0 | 0 |
| Step_30_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_30_Inference | 48.53 | 43.46 | 8.0 | 326.29 | 100.0 | 0 |
| Step_31_Loading | 0.00 | 21.90 | 0.0 | 326.29 | 0.0 | 0 |
| Step_31_Inference | 48.52 | 43.46 | 9.0 | 327.40 | 100.0 | 0 |
| Step_32_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_32_Inference | 48.52 | 43.46 | 7.7 | 327.81 | 100.0 | 0 |
| Step_33_Loading | 0.00 | 21.90 | 0.0 | 327.76 | 0.0 | 0 |
| Step_33_Inference | 48.53 | 43.46 | 7.1 | 328.14 | 100.0 | 0 |
| Step_34_Loading | 0.00 | 21.90 | 0.0 | 327.77 | 0.0 | 0 |
| Step_34_Inference | 42.16 | 43.46 | 7.4 | 346.63 | 100.0 | 0 |
| Step_35_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_35_Inference | 48.57 | 43.46 | 8.0 | 351.51 | 100.0 | 0 |
| Step_36_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 100.0 | 0 |
| Step_36_Inference | 45.07 | 43.46 | 11.2 | 370.40 | 100.0 | 0 |
| Step_37_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_37_Inference | 22.43 | 43.46 | 8.8 | 352.13 | 99.9 | 0 |
| Step_38_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_38_Inference | 22.44 | 43.46 | 15.6 | 321.91 | 100.0 | 0 |
| Step_39_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_39_Inference | 22.45 | 43.46 | 16.6 | 330.62 | 100.0 | 0 |
| Step_40_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_40_Inference | 22.46 | 43.46 | 7.3 | 327.41 | 99.8 | 0 |
| Step_41_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_41_Inference | 22.46 | 43.46 | 6.0 | 315.35 | 100.0 | 0 |
| Step_42_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_42_Inference | 22.46 | 43.46 | 6.2 | 334.36 | 100.0 | 0 |
| Step_43_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_43_Inference | 22.47 | 43.46 | 7.5 | 334.31 | 100.0 | 0 |
| Step_44_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_44_Inference | 22.47 | 43.46 | 10.2 | 335.46 | 100.0 | 0 |
| Step_45_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_45_Inference | 22.47 | 43.46 | 6.2 | 335.36 | 99.9 | 0 |
| Step_46_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_46_Inference | 22.46 | 43.46 | 5.5 | 300.44 | 99.8 | 0 |
| Step_47_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_47_Inference | 22.44 | 43.46 | 10.1 | 301.14 | 100.0 | 0 |
| Step_48_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_48_Inference | 22.43 | 43.46 | 5.8 | 291.42 | 100.0 | 0 |
| Step_49_Loading | 0.00 | 21.90 | 0.0 | 0.00 | 0.0 | 0 |
| Step_49_Inference | 22.42 | 43.46 | 5.5 | 281.75 | 99.8 | 0 |
| VAE_Decoding | 54.03 | 25.97 | 5.7 | 300.66 | 99.6 | 0 |
| Total_Execution | 2196.92 | 43.46 | 8.8 | 370.40 | 99.6 | 0 |

### Inference Statistics

- **Avg Time per Step**: 41.53 s
- **Avg SM Activity**: 100.0 %
- **Avg CPU Utilization**: 8.8 %
- **Total Inference Load**: 0

### Performance Analysis

**Bottlenecks Detected:**
- Low overall GPU utilization (0.0%), suggesting potential CPU bottlenecks or data loading overhead.

**Resource Usage Overview:**
- Peak GPU Memory reached 43.46 GB. High VRAM usage, close to 48GB limit on L40S.
---

