# Wan2.2-Enhanced Performance Benchmark

## 1. 项目目标
本项目旨在评估并对比 **Wan2.2-5B** 模型在 **NVIDIA RTX 4090** 和 **NVIDIA RTX PRO 6000 Blackwell** 两种不同 GPU 架构上的视频生成性能。
重点记录详细的 **显存消耗 (Memory Usage)** 和 **计算资源消耗 (Compute Load/SM Activity)**，为硬件选型和生产环境部署提供参考。

## 2. 环境参数
- **Hardware Group A**: NVIDIA RTX 4090 (24GB VRAM) - 代表消费级旗舰。
- **Hardware Group B**: NVIDIA RTX PRO 6000 Blackwell (96GB VRAM) - 代表新一代高性能工作站/服务器显卡。
- **Software Environment**:
  - OS: Linux
  - Codebase: Wan2.2-Enhanced
  - Model: Wan2.2-TI2V-5B (50亿参数)

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
以下为 **Group B (RTX PRO 6000 Blackwell)** 的实测数据：

| Case | Res | Offload | Time (s) | Mem (GB) | SM Act (%) | Compute Load |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **01_Speed_Preview** | 1280*704 | ✅ True | 122.62 | 31.27 | 97.0 | 11,533 |
| **02_Efficiency_Mode** | 1280*704 | ✅ True | 156.46 | 31.27 | 99.9 | 18,662 |
| **03_Performance_Mode** | 1280*704 | ❌ False | 146.78 | 42.17 | 100.0 | 18,589 |

> **详细分析报告**: 请参阅 [benchmark_report.md](./benchmark_report.md) 获取各阶段（编码、推理、解码）的详细耗时与算力分析。
