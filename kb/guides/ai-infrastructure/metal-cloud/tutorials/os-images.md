# Custom image (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/ai-infrastructure/metal-cloud/tutorials/os-images/

# Custom image

## FPT Images​

FPT Image is a custom image built by FPT for quick starts with GPU servers. It includes components for AI workloads and uses Ubuntu as the OS.

Dependency versions are optimized for compatibility rather than being the latest available.

### Vietnam region​

Image names| Ubuntu 22.04 GPU| AI/ML Ready| OS base| Ubuntu 22.04| Ubuntu 22.04| NVIDIA Driver| 560.35.03| 560.35.03| NVIDIA CUDA Toolkit| 12.6.85| 12.6.85| NVIDIA Fabric Manager (NVSwitch Driver)| 560.35| 560.35| MLNX_OFED (InfiniBand Driver)| 24.10| 24.10| DOCA OFED (Mellanox IB Driver)| ❌| ❌| NVIDIA Datacenter GPU Manager| 3.3.9| 3.3.9| VAST Data Client| 4.0.32| 4.0.32| Python| 3.10.12| 3.10.12| NVIDIA Container Toolkit| ❌| 1.17.4| NVIDIA cuDNN| ❌| 9.7.1.26| Docker| ❌| 28.0.1| PyTorch| ❌| 2.6.0+cu12.6  
---|---|---  
  
### Japan region​

Image names| Ubuntu 22.04 GPU| Ubuntu 24.04 GPU| AI/ML Ready| OS base| Ubuntu 22.04| Ubuntu 24.04| Ubuntu 22.04| NVIDIA Driver| 560.35.03| 580.95.05| 580.95.05| NVIDIA CUDA Toolkit| 12.6.85| 13.1.0| 13.1.0| NVIDIA Fabric Manager (NVSwitch Driver)| 560.35| 580.95.05| 580.95.05| MLNX_OFED (InfiniBand Driver)| 24.10| ❌| 24.10| DOCA OFED (Mellanox IB Driver)| ❌| 3.2.0| ❌| NVIDIA Datacenter GPU Manager| 3.3.9| 3.3.9| 3.3.9| DDN Storage Client| 2.14.0| 2.14.0| 2.14.0| Python| 3.10.12| 3.12.3| 3.12.3| NVIDIA Container Toolkit| ❌| 1.18.1-1| 1.18.1-1| NVIDIA cuDNN| ❌| ❌| 9.7.1.26| Docker| ❌| 29.1.2| 28.0.1| PyTorch| ❌| ❌| 2.6.0+cu12.6  
---|---|---|---  
  
Custom image templates let you capture an image of a Bare Metal GPU server to replicate its configuration with minimal changes. Image templates work for all Bare Metal GPU servers regardless of OS. Once complete, the template can be used to create another server.

## Upload an image​

  1. Sign in to your FPT Cloud account, select a **Tenant** , a **Region** and a **VPC.** (If you have more than one of them.)
  2. Navigate to **AI Infrastructure** and **Custom images** in the sidebar, then click **Upload image.**
  3. To upload, click to **choose a file from your computer** , or **drag and drop your file.**
  4. Enter the **image name**
  5. Click **Upload image**

_You cannot create a new server with this image until the imaging process is complete. Processing time varies based on available resources and how much data is captured._

## Resume processing​

You may resume file processing if it fails.

  1. In the Custom image list, Click **Actions** for the custom image with **Failed** status
  2. Choose **Resume**

## Delete an image​

  1. In the Custom image list, Click **Actions** for the custom image you want to delete, then choose **Delete**
  2. A confirmation window titled **Delete custom image** opens. Click **Delete image** to confirm

_Deleting the image from your account does not delete servers created from that image. You can destroy the Bare Metal GPU server from the FPT Customer portal separately._
