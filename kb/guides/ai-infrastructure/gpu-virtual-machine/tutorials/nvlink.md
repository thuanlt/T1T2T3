# NVLink (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/ai-infrastructure/gpu-virtual-machine/tutorials/nvlink/

# NVLink

## About NVLink​

NVLink is supported **only** on instance flavors with **8× NVIDIA H100 or H200 GPUs**. In this setup, NVLink delivers high-bandwidth, low-latency GPU-to-GPU communication, enabling:

  * **Faster model training** , particularly for large models needing frequent inter-GPU data exchange
  * **Improved scaling efficiency** with distributed training frameworks (e.g., Megatron-LM, DeepSpeed, PyTorch FSDP)
  * **Reduced communication bottlenecks** compared to PCIe-only GPU connectivity
  * **Higher overall compute throughput** for workloads relying on multi-GPU synchronization

Instances with fewer than 8 GPUs do **not** support NVLink.

## Enable NVLink for 8x GPUs Flavors​

note

NVLink is **not enabled by default** in FPT-provided images. Users must manually enable it if required.

**To enable NVLink support** , follow these steps:

  1. Open the file: **`/etc/default/grub.d/00-fci-grub.cfg`**
  2. Locate the following line and **remove or comment it out** :

    
    
    GRUB_CMDLINE_LINUX_DEFAULT="nvidia.NVreg_NvLinkDisable=1"  
    

  3. Update the GRUB configuration:

    
    
    sudo update-grub  
    

  4. Reboot the instance for the changes to take effect.

## Verification​

To verify NVLink has been enabled successfully, run the following commands.

### 1\. Check NVLink status​
    
    
    nvidia-smi nvlink --status  
    

The output should show **active NVLink connections** with their link speeds (e.g., **25 GB/s per lane**).

### 2\. Check GPU topology​
    
    
    nvidia-smi topo -m  
    

The output should display **NVLink (NV##)** connections between all GPUs, similar to:
    
    
            GPU0   GPU1   GPU2   GPU3   GPU4   GPU5   GPU6   GPU7   CPU Affinity   NUMA Affinity  
    GPU0     X    NV18   NV18   NV18   NV18   NV18   NV18   NV18   0-127          0-1  
    GPU1   NV18     X    NV18   NV18   NV18   NV18   NV18   NV18   0-127          0-1  
    GPU2   NV18   NV18     X    NV18   NV18   NV18   NV18   NV18   0-127          0-1  
    GPU3   NV18   NV18   NV18     X    NV18   NV18   NV18   NV18   0-127          0-1  
    GPU4   NV18   NV18   NV18   NV18     X    NV18   NV18   NV18   0-127          0-1  
    GPU5   NV18   NV18   NV18   NV18   NV18     X    NV18   NV18   0-127          0-1  
    GPU6   NV18   NV18   NV18   NV18   NV18   NV18     X    NV18   0-127          0-1  
    GPU7   NV18   NV18   NV18   NV18   NV18   NV18   NV18     X    0-127          0-1  
    

**Legend:**

Symbol| Meaning| **X**|  Same GPU| **SYS**|  PCIe + inter-NUMA interconnect| **NODE**|  PCIe + interconnect within one NUMA node| **PHB**|  PCIe Host Bridge| **PXB**|  Multiple PCIe bridges| **PIX**|  Single PCIe bridge| **NV#**|  NVLink connection with # bonded links  
---|---  
  
## Troubleshooting​

If you encounter errors such as:

  * `system not yet initialized`
  * Issues when calling `torch.cuda.device_count()` or `torch.cuda.get_device_name(i)`

Restart the NVIDIA Fabric Manager:
    
    
    sudo systemctl restart nvidia-fabricmanager  
    

Then retry your application or verification steps.
