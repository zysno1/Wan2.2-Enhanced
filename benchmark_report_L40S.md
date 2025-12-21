# Wan2.2 Benchmark Report

| Case                   | Res        | Offload |  Time(s) | s/step | Mem(GB) | SM(%) |   Load |
|------------------------|------------|---------|----------|--------|---------|-------|--------|
| 01_Speed_Preview_480p  | 1280*704   | True    |   269.38 |  12.57 |   31.27 |  99.4 |  21888 |
| 02_Efficiency_Mode_720p | 1280*704   | True    |   322.66 |  12.64 |   31.27 |  99.8 |  34674 |
| 03_Performance_Mode_720p | 1280*704   | True    |   319.90 |  12.66 |   31.27 |  99.7 |  34698 |

# Detailed Breakdown

## Case: 01_Speed_Preview_480p

- **Total Duration**: 269.38 s
- **Peak GPU Memory**: 31.27 GB
- **Total Compute Load**: 21888

### Stage Breakdown

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

### Inference Statistics

- **Avg Time per Step**: 12.57 s
- **Avg SM Activity**: 99.4 %
- **Avg CPU Utilization**: 24.3 %
- **Total Inference Load**: 6250

### Performance Analysis

No significant bottlenecks detected. GPU utilization is healthy.

**Resource Usage Overview:**
- Peak GPU Memory reached 31.27 GB. VRAM usage is within safe margins.
---

## Case: 02_Efficiency_Mode_720p

- **Total Duration**: 322.66 s
- **Peak GPU Memory**: 31.27 GB
- **Total Compute Load**: 34674

### Stage Breakdown

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

### Inference Statistics

- **Avg Time per Step**: 12.64 s
- **Avg SM Activity**: 99.8 %
- **Avg CPU Utilization**: 26.9 %
- **Total Inference Load**: 12617

### Performance Analysis

No significant bottlenecks detected. GPU utilization is healthy.

**Resource Usage Overview:**
- Peak GPU Memory reached 31.27 GB. VRAM usage is within safe margins.
---

## Case: 03_Performance_Mode_720p

- **Total Duration**: 319.90 s
- **Peak GPU Memory**: 31.27 GB
- **Total Compute Load**: 34698

### Stage Breakdown

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

### Inference Statistics

- **Avg Time per Step**: 12.66 s
- **Avg SM Activity**: 99.7 %
- **Avg CPU Utilization**: 26.9 %
- **Total Inference Load**: 12620

### Performance Analysis

No significant bottlenecks detected. GPU utilization is healthy.

**Resource Usage Overview:**
- Peak GPU Memory reached 31.27 GB. VRAM usage is within safe margins.
---

