# Wan2.2-Enhanced Benchmark Analysis Report

## 1. 核心结论 (Executive Summary)

本次测试对比了 **NVIDIA L40S (48GB)** 与 **NVIDIA RTX PRO 6000 Blackwell (96GB)** 在 Wan2.2-5B 模型下的性能表现。

*   **性能差距**: Blackwell 平台在端到端生成速度上表现出 **1.8x - 2.1x** 的巨大优势。
*   **关键瓶颈**:
    *   **L40S 平台**: 受限于 48GB 显存，720p 分辨率下必须开启 Offload，导致推理延迟增加；同时，该测试平台的 **CPU/系统性能** 显著弱于 Blackwell 平台，严重拖慢了初始化和 T5 编码阶段。
    *   **Blackwell 平台**: 96GB 大显存允许全量模型常驻 (Offload=False)，配合更强的算力，实现了极致的低延迟。
*   **算力饱和度**: 两个平台在推理阶段的 **SM Activity 均接近 100%**，表明 Wan2.2-5B 是典型的**计算密集型 (Compute Bound)** 任务，性能随 GPU 算力线性扩展。

## 2. 详细对比分析 (Detailed Analysis)

### 2.1 推理算力 (Diffusion Inference)

| 指标 | L40S (Ada) | Blackwell | 提升倍数 | 分析 |
| :--- | :--- | :--- | :--- | :--- |
| **Step Time** | ~12.60 s | ~6.87 s | **1.83x** | Blackwell 架构带来的核心算力提升。 |
| **SM Activity** | 99.2% | 100.0% | - | 此时 GPU 满载，无显存带宽瓶颈，纯拼 FP16/BF16 算力。 |

> **解读**: Blackwell 架构在 Transformer 类大规模矩阵运算上展现了代际优势，近 2 倍的单步推理速度直接缩短了生成耗时。

### 2.2 显存与 Offload 策略 (Memory & Offload)

*   **L40S (48GB)**:
    *   **困境**: 720p 任务峰值显存需求约 **42.2 GB** (参考 Blackwell 数据)。虽然物理显存有 48GB，但在 PyTorch 上下文、碎片化及系统预留影响下，**Offload=False 遭遇 OOM (Out of Memory)**。
    *   **代价**: 强制开启 Offload 引入了模型权重在 CPU-GPU 间的换入换出，虽然 `run.py` 优化了预取，但仍有隐性开销。
*   **Blackwell (96GB)**:
    *   **优势**: 96GB 显存游刃有余。Case 03 (Offload=False) 相比 Case 02 (Offload=True) 进一步减少了 **~18秒** 的总耗时 (主要来自 T5 和 VAE 阶段的显存常驻优势及通信减少)。

### 2.3 系统瓶颈揭秘 (System Bottlenecks)

除了 GPU 差异，**Host (宿主机)** 性能差异极大地影响了总耗时：

| 阶段 | L40S 平台耗时 | Blackwell 平台耗时 | 差距 | 原因推测 |
| :--- | :--- | :--- | :--- | :--- |
| **Model Init** | ~86.5 s | ~42.3 s | **2.0x** | 磁盘 I/O 读取模型速度、CPU 解压权重速度差异。 |
| **T5 Encoding** | ~46.3 s | ~12.1 s | **3.8x** | **严重瓶颈**。T5 通常在 CPU 运行 (Offload 模式下)，L40S 宿主机的 CPU 单核性能或内存带宽远弱于 Blackwell 宿主机。 |
| **VAE Decoding** | ~46.0 s | ~23.8 s | **1.9x** | VAE 解码主要依靠 GPU，符合 1.8x 的算力差距。 |

> **专家洞察**: L40S 组的 `T5_Encoding` 耗时异常高 (46s vs 12s)。建议检查 L40S 服务器的 CPU 负载、内存频率或是否开启了 T5 的 GPU 加速 (如果显存允许)。在当前配置下，**CPU 正在拖累 L40S 的后腿**。

## 3. 优化建议 (Recommendations)

1.  **针对 L40S 的优化**:
    *   **量化 (Quantization)**: 尝试 **FP8** 或 **INT8** 量化。将 5B 模型显存占用减半，可能使其在 48GB 显存下实现 `Offload=False`，从而避免通信开销。
    *   **CPU/T5 优化**: 检查 T5 运行设备。如果显存紧缺必须跑在 CPU，建议升级宿主机 CPU 或优化 PyTorch 线程设置 (`torch.set_num_threads`)。
    *   **Flash Attention**: 确认已启用 Flash Attention 2 (环境信息显示已安装)，这对长序列视频生成至关重要。

2.  **针对 Blackwell 的应用**:
    *   **高并发**: 96GB 显存不仅能跑得快，还能支持更大的 **Batch Size**。建议测试 Batch Size = 2 或 4，可能进一步压榨吞吐量。
    *   **长视频**: 巨大的显存空间非常适合生成超过 5秒 (129帧+) 的长视频。

3.  **总结**:
    *   **L40S**: 适合高性价比推理集群，但需配合强力 CPU，并强烈建议使用量化技术突破 48GB 显存墙。
    *   **Blackwell**: 极致性能之选，适合对延迟敏感的实时生成或高端创作工具。
