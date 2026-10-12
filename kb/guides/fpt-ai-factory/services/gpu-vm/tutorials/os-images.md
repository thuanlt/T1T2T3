# OS Images (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/fpt-ai-factory/services/gpu-vm/tutorials/os-images/

# OS Images

An FPT public image is built by FPT so you can get started quickly on any available GPU VM. Each image uses Ubuntu as the operating system and comes with the components needed for AI workloads.

The versions of the installed dependencies are optimized for compatibility and might not be the latest versions available.

Image name| Description| Dependencies| **Ubuntu 22.04**|  Ubuntu version 22.04 and essential NVIDIA GPU drivers.| NVIDIA Driver 560.35.03  
NVIDIA CUDA Toolkit 12.6.85  
NVIDIA Fabric Manager (NVSwitch Driver) 560.35  
NVIDIA Datacenter GPU Manager 3.3.9| **Ubuntu 24.04**|  Ubuntu version 24.04 and essential NVIDIA GPU drivers.| NVIDIA Driver 575  
NVIDIA CUDA Toolkit 12.9  
NVIDIA Container Toolkit 1.18.2| **Ubuntu 24.04 (8x GPUs)**|  Ubuntu version 24.04 and essential software for AI/ML workloads. Features NVLink interconnect on 8x GPU flavors.| NVIDIA Driver 575  
NVIDIA CUDA Toolkit 12.9  
NVIDIA Container Toolkit 1.18.2  
NVIDIA Fabric Manager 575| **Ubuntu 24.04 - Inference Optimized**|  Ubuntu version 24.04. Deploy any model faster with production-grade performance.| NVIDIA Driver 575.51.03  
NVIDIA CUDA Toolkit 12.9  
NVIDIA Container Toolkit 1.18.2  
Docker CE  
vLLM 0.10.2| **Ubuntu 24.04 - Inference Optimized (8x GPUs)**|  Ubuntu version 24.04. Deploy any model faster with production-grade performance. Features NVLink interconnect on 8x GPU flavors.| NVIDIA Driver 575  
NVIDIA CUDA Toolkit 12.9  
NVIDIA Container Toolkit 1.18.2  
NVIDIA Fabric Manager 575| **Ubuntu 24.04 v1.1**|  Ubuntu 24.04, optimized for NVIDIA Blackwell GPUs and pre-built for out-of-the-box AI and deep learning acceleration.| NVIDIA Driver 595  
NVIDIA CUDA Compute library  
NVIDIA DKMS kernel module  
NVIDIA GPU kernel driver  
CUDA Toolkit 13.1| **Ubuntu 24.04 Inference Optimized v1.1**|  Ubuntu version 24.04, with the vLLM inference engine for high-throughput, production-grade model serving.| NVIDIA Driver 595  
NVIDIA CUDA Compute library  
NVIDIA DKMS kernel module  
NVIDIA GPU kernel driver  
CUDA Toolkit 13.1  
vLLM v0.20.2  
---|---|---  
  
* * *

## What's next​

  * Create a GPU VM — select an OS image when you configure your VM.
