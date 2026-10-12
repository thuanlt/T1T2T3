# On FPT Cloud Console (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/ai-infrastructure/gpu-virtual-machine/overview/

# On FPT Cloud Console

## What is GPU Virtual Machine?​

GPU Virtual Machine (GPU VM) lets users deploy and manage high-performance GPU servers. It uses passthrough GPU to provide a dedicated GPU, with applications accessing it through the layers of a guest OS and hypervisor. Other critical resources like RAM, storage, and networking are also virtualized.

Two VM types are offered, each with different storage:

GPU VM Type| Storage Type| Key Features of Storage| **Type #1**| **Block Storage – Ephemeral Disk (NVMe)**|  Fixed capacity per GPU instance; optimized for high-performance training workloads; not suitable for long-term data; no automated backup/restore feature; data persists when VMs are stopped| **Type #2**| **Block Storage – Persistent Disk**|  Scalable, on-demand storage from 100 GB; ideal for long-term data retention; supports automated backup & restore; storage is billed separately from GPU instance cost  
---|---|---  
  
## How Does It Work?​

A GPU VM functions as a powerful cloud-based computer with a dedicated GPU for intensive workloads. Users can:

  * **Easily deploy a GPU VM** with the latest GPU generations in minutes via the FPT Cloud Portal.
  * **Run AI, machine learning, and data processing tasks** at high speed with GPU acceleration.
  * **Manage everything from a simple online portal** , with no need for in-house IT staff.

## Why GPU Virtual Machine?​

  * **One-click deployment** from the FPT Smart Cloud Portal.
  * **Simple configuration** of networking, storage, and security.
  * **Faster AI training & deep learning:** Cutting-edge GPUs deliver exceptional speed and efficiency for large-scale AI/ML models.
  * **Optimized for AI inference:** Process data and make real-time decisions faster than ever before.
