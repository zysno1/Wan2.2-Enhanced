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

## 3. 测试场景
测试对象为 **Wan2.2-TI2V-5B** (图生视频任务)，覆盖以下典型应用场景：

1.  **Speed Preview (快速预览)**
    *   分辨率: 480p (832x480)
    *   采样步数: 5 Steps
    *   策略: Offload=True (显存优化)
    *   *目的: 快速验证提示词效果*

2.  **Efficiency Mode (效率模式)**
    *   分辨率: 720p (1280x720)
    *   采样步数: 10 Steps
    *   策略: Offload=True (开启显存卸载)
    *   *目的: 在有限显存下生成标准质量视频*

3.  **Performance Mode (高性能模式)**
    *   分辨率: 720p (1280x720)
    *   采样步数: 10 Steps
    *   策略: Offload=False (关闭显存卸载)
    *   *目的: 测试最大显存占用与最低延迟*

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
| **03_Performance_Mode** | 1280*704 | ✅ True* | 324.00 | 31.27 | 99.2 | 34,637 |

> *注: 由于 L40S (48GB) 无法在 Offload=False 模式下运行 720p 生成 (OOM)，因此 Case 03 调整为 Offload=True，其表现与 Case 02 基本一致。*

### Group B: NVIDIA RTX PRO 6000 Blackwell (96GB)

| Case | Res | Offload | Time (s) | Mem (GB) | SM Act (%) | Compute Load |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **01_Speed_Preview** | 1280*704 | ✅ True | 126.25 | 31.27 | 100.0 | 11,685 |
| **02_Efficiency_Mode** | 1280*704 | ✅ True | 168.78 | 31.27 | 99.9 | 18,511 |
| **03_Performance_Mode** | 1280*704 | ❌ False | 150.43 | 42.17 | 98.5 | 18,358 |

> **详细分析报告**: 请参阅 [benchmark_report.md](./benchmark_report.md) 获取各阶段（编码、推理、解码）的详细耗时与算力分析。

## 6. 综合对比分析 (Summary)

根据 `benchmark_report.md` 的详细分析，以下是 L40S 与 RTX PRO 6000 的核心对比结论：

### 6.1 性能对比 (Performance)

RTX PRO 6000 展现出显著的性能优势，整体生成速度约为 L40S 的 **2.1倍 - 2.3倍**。

| 测试场景 (Case) | 分辨率 | L40S 耗时 (s) | RTX 6000 耗时 (s) | 兑换比 (Speedup) |
| :--- | :--- | :--- | :--- | :--- |
| **01_Speed_Preview_704p** | 1280*704 | 269.38 | 114.94 | **2.34x** |
| **02_Efficiency_Mode_720p** | 1280*704 | 322.66 | 147.19 | **2.19x** |
| **03_Performance_Mode_720p** | 1280*704 | 319.90 | 149.29 | **2.14x** |

### 6.2 显存占用与硬件建议 (Memory & Recommendations)

*   **常规场景 (Safe Range)**: 在 480p/720p 且开启 `Offload=True` 的情况下，显存占用约为 **31.27 GB**。L40S (48GB) 可以轻松应对。
*   **高性能/大模型场景 (High Memory)**:
    *   **Case 03 (Performance Mode)**: 显存峰值达到 **42.17 GB**，已接近 L40S 的物理上限，建议生产环境预留更多余量。
    *   **Case 04 (14B Model)**: 显存峰值高达 **82.60 GB**，**L40S 无法运行**，必须使用 RTX PRO 6000 (96GB) 或 A100/H100 (80GB) 等大显存卡。

---
> **Note**: 本项目由 **Trae** + **Gemini-3-Pro** 生成。
