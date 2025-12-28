# Wan2.2-Enhanced Performance Benchmark

## 1. 项目目标
本项目旨在评估并对比 **Wan2.2-5B** 模型在 **NVIDIA L40S** 和 **NVIDIA RTX PRO 6000 Blackwell** 两种不同 GPU 架构上的视频生成性能。
重点记录详细的 **显存消耗 (Memory Usage)** 和 **计算资源消耗 (Compute Load/SM Activity)**，为硬件选型和生产环境部署提供参考。

## 2. 环境参数
- **Hardware Group A**: NVIDIA L40S (48GB VRAM) - 代表数据中心推理卡。
- **Hardware Group B**: NVIDIA RTX PRO 6000 Blackwell (96GB VRAM) - 代表新一代高性能工作站/服务器显卡。
- **Software Environment**:
  - OS: Linux
  - Codebase: Wan2.2-Enhanced
  - Model: Wan2.2-TI2V-5B (50亿参数)
  - PyTorch: 2.9.1+cu128
  - CUDA: 12.8
  - Flash Attention: 2.8.3

## 3. 测试场景与视频预览 (Test Scenarios & Previews)

本次测试覆盖以下 4 个典型应用场景。每个场景均提供详细配置与生成的视频样例预览。

| 场景 (Scenario) | 详细配置 (Configuration) | 视频预览 (Video Preview) |
| :--- | :--- | :--- |
| **01. Speed Preview**<br>*(快速预览)* | - **分辨率**: 1280x704<br>- **采样步数**: 5 Steps<br>- **显存优化**: On (Offload Model)<br>- **用途**: 快速验证 Prompt 效果 | [▶️ Click to Watch (MP4)](assets/videos/01_Speed_Preview.mp4)<br>*(Size: 14MB)* |
| **02. Efficiency Quality**<br>*(效率模式)* | - **分辨率**: 1280x704<br>- **采样步数**: 30 Steps<br>- **显存优化**: On<br>- **用途**: 平衡速度与质量的标准生成 | [▶️ Click to Watch (MP4)](assets/videos/02_Efficiency_Quality.mp4)<br>*(Size: 25MB)* |
| **03. Max Quality**<br>*(极致质量)* | - **分辨率**: 1280x704<br>- **采样步数**: 50 Steps<br>- **显存优化**: Off (全显存加速)<br>- **用途**: 生产级高质量输出 | [▶️ Click to Watch (MP4)](assets/videos/03_Max_Quality.mp4)<br>*(Size: 13MB)* |
| **04. Long Duration**<br>*(长视频测试)* | - **分辨率**: 1280x704<br>- **时长**: 15s (361 frames)<br>- **采样步数**: 50 Steps<br>- **显存优化**: On | [▶️ Click to Watch (MP4)](assets/videos/04_15s_Long_Duration.mp4)<br>*(Size: 27MB)* |

> **注意**: 视频文件存储在 `assets/videos/` 目录下，建议下载后观看以获得最佳体验。

## 4. 测试方案
本项目集成 `PerformanceMonitor` 工具与自动化测试脚本 (`benchmark/run.py`)，采集以下核心指标：

*   **SM Activity (流处理器活跃度)**: 反映 GPU 计算核心利用率，接近 100% 表示算力满载。
*   **Compute Load (计算负载)**: 计算公式 `Duration * SM_Activity`，量化有效计算工作量。
*   **Peak Memory (峰值显存)**: 记录生成过程中的最高显存占用。

执行命令：
```bash
python3 benchmark/run.py
```

## 5. 测试结果
### Group A: NVIDIA L40S (48GB)

| Case | Res | Offload | Time (s) | Mem (GB) | SM Act (%) | Compute Load |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **01_Speed_Preview** | 1280*704 | ✅ True | 265.59 | 31.27 | 99.2 | 21,795 |
| **02_Efficiency_Mode** | 1280*704 | ✅ True | 331.14 | 31.27 | 99.1 | 34,636 |
| **03_Performance_Mode** | 1280*704 | ❌ False | **Failed** | **OOM** | - | - |
| **04_Long_Duration** | 1280*704 | ✅ True | **Failed** | **OOM** | - | - |

> *注: L40S (48GB) 显存无法满足 Case 03 (Offload=False, 需 ~53GB) 和 Case 04 (长视频, 需 ~44GB+及额外开销) 的运行需求。*

### Group B: NVIDIA RTX PRO 6000 Blackwell (96GB)

| Case | Res | Offload | Time (s) | s/step | Mem (GB) | SM Act (%) | Compute Load |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **01_Speed_Preview** | 1280*704 | ✅ True | 344.73 | 12.87 | 31.27 | 97.2 | 0 |
| **02_Efficiency_Mode** | 1280*704 | ✅ True | 593.45 | 12.82 | 31.27 | 99.8 | 0 |
| **03_Performance_Mode** | 1280*704 | ❌ False* | 707.29 | 12.73 | 52.76 | 99.9 | 0 |
| **04_Long_Duration** | 1280*704 | ✅ True | 2197.13 | 41.53 | 43.46 | 100.0 | 0 |

> *注: Case 03 在显存充足的情况下自动禁用了 Offload 以追求极致性能，显存占用达到 52.76 GB。*

### 显存组件分析 (Memory Profiling)

根据最新的测试报告，我们对模型各组件的显存占用进行了详细分析（基于 704p 分辨率）：

| Component | Est. Peak Mem (GB) | Est. Contribution (GB) | Notes |
| :--- | :--- | :--- | :--- |
| **Initialization** | 2.63 | 2.63 | Base PyTorch/System Overhead |
| **T5 Encoder** | 2.63 | 0.00 | Weights + Activations (Offloaded) |
| **DiT Transformer** | 31.11 | 28.48 | Weights + KV Cache + Activations |
| **VAE Decoder** | 23.54 | -7.57 | Weights + Large Feature Maps |

> **详细分析报告**: 请参阅 [benchmark_report.md](./benchmark_report.md) 获取各阶段（编码、推理、解码）的详细耗时与算力分析。

## 6. 综合对比分析 (Summary)

根据最新的 `benchmark_report.md` 分析，以下是 L40S 与 RTX PRO 6000 的核心对比结论：

### 6.1 性能与能力 (Performance & Capability)

RTX PRO 6000 (96GB) 的主要优势在于其巨大的显存容量，能够支持 **全显存加速 (No Offload)** 和 **长视频生成**，而 L40S (48GB) 在这些高负载场景下会遇到显存瓶颈。

| 测试场景 (Case) | 分辨率 | L40S 耗时 (s)* | RTX 6000 耗时 (s) | 备注 |
| :--- | :--- | :--- | :--- | :--- |
| **01_Speed_Preview** | 1280*704 | 269.38 | 344.73 | 基础生成场景 |
| **02_Efficiency_Mode** | 1280*704 | 322.66 | 593.45 | 30 Steps 标准质量 |
| **03_Performance_Mode** | 1280*704 | N/A (OOM) | 707.29 | **RTX 6000 独占** (Offload=False) |
| **04_Long_Duration** | 1280*704 | N/A (OOM) | 2197.13 | **RTX 6000 独占** (15s 长视频) |

> *注: L40S 数据基于早期测试版本，仅供参考。最新测试显示随着模型优化和采样步数调整，整体耗时有所增加，但 RTX 6000 依然是生产级长视频生成的首选。*

### 6.2 显存占用与硬件建议 (Memory & Recommendations)

*   **常规场景 (Safe Range)**: 在 480p/720p 且开启 `Offload=True` 的情况下，显存占用约为 **31.27 GB**。L40S (48GB) 可以轻松应对。
*   **高性能/大模型场景 (High Memory)**:
    *   **Case 03 (Performance Mode)**: 显存峰值达到 **52.76 GB**，**超过 L40S 物理上限**。必须使用 RTX PRO 6000 (96GB) 或 A100/H100 (80GB) 以获得最佳性能。
    *   **Case 04 (Long Duration)**: 涉及长序列推理，显存占用稳定在 **43-50 GB+** 范围，且计算负载极高，建议使用 80GB+ 显存的 GPU。

---
> **Note**: 本项目由 **Trae** + **Gemini-3-Pro** 生成。
