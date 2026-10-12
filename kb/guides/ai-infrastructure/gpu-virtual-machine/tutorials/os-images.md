# OS Images (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/ai-infrastructure/gpu-virtual-machine/tutorials/os-images/

# OS Images

## FPT Images​

FPT Image is a custom image built by FPT that helps users get started quickly with any GPU VM. It uses Ubuntu as the OS and includes components needed for AI workloads. The dependency versions are optimized for compatibility and might not be the latest versions available.

Image name| Description| Dependencies| UBUNTU 22.04 GPU| Ubuntu 22.04 with essential NVIDIA GPU drivers| NVIDIA Driver 560.35.03, NVIDIA CUDA Toolkit 12.6.85, NVIDIA Fabric Manager (NVSwitch Driver) 560.35, NVIDIA Datacenter GPU Manager 3.3.9| AIML UBUNTU 24.04| Ubuntu 24.04 with essential NVIDIA GPU drivers| NVIDIA Driver 575, NVIDIA CUDA Toolkit 12.9, NVIDIA Container Toolkit 1.18.2| AIML UBUNTU 24.04 8GPU| Ubuntu 24.04 with essential AI/ML software. Features NVLink interconnect on **8x GPU flavors.**|  NVIDIA Driver 575, NVIDIA CUDA Toolkit 12.9, NVIDIA Container Toolkit 1.18.2, NVIDIA Fabric Manager 575| INFERENCE UBUNTU 24.04| Ubuntu 24.04 — deploy models faster with production-grade performance| NVIDIA Driver 575.51.03, NVIDIA CUDA Toolkit 12.9, NVIDIA Container Toolkit 1.18.2, Docker CE, vLLM 0.10.2| INFERENCE UBUNTU 24.04 8GPU| Ubuntu 24.04 with production-grade inference performance. Features NVLink interconnect on **8x GPU flavors.**|  NVIDIA Driver 575, NVIDIA CUDA Toolkit 12.9, NVIDIA Container Toolkit 1.18.2, NVIDIA Fabric Manager 575| INFERENCE UBUNTU 24.04 BLACKWELL v.1.1| Ubuntu 24.04 with vLLM inference engine for high-throughput, production-grade model serving| NVIDIA Driver 595, NVIDIA CUDA Compute library, NVIDIA DKMS kernel module, NVIDIA GPU kernel driver, CUDA Toolkit 13.1, vLLM v0.20.2  
---|---|---  
  
## Custom Images​

You can create GPU VMs based on custom images, enabling workload migration and scaling without recreating environments from scratch.

### Upload a Custom Image​

Only the **QCOW** file format is supported for uploading GPU VMs here. For other formats, contact support for assistance.

**Step 1:** From the menu, select **Compute Engine > Custom Image**. Then click **Upload Image**.

**Step 2:** Enter the required information and choose the file from your machine. Click **Upload** to begin the upload process.

### Delete a Custom Image​

If a Custom Image is no longer needed, you can delete it:

**Step 1:** From the menu, select **Custom Image** , then under the **Actions** menu for the image you wish to delete, click **Delete**.

**Step 2:** A confirmation pop-up will appear. To proceed with the deletion, click **Delete Custom Image**.
