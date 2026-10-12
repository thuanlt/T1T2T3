# FAQ (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/ai-infrastructure/gpu-virtual-machine/faq/

# FAQ

## General​

### 1\. What is GPU Virtual Machine?​

A GPU VM is an isolated system with dedicated GPU, CPU, memory, network interface, and storage, built from a GPU Cluster. It offers pre-configured VMs matching workload needs, with flexible options ranging from 1 to 8 GPUs per VM.

## Features​

### 2\. Can I resize a GPU instance (CPU, RAM, or Disk)?​

  * **Ephemeral Disk (NVMe):** Flavors are pre-configured and cannot be customized. Users should pick an appropriate config or contact FPT Cloud Support.
  * **Persistent Disk:** GPU, CPU, and RAM are fixed. Storage can be resized as needed, but not below 100 GB per instance.

### 3\. How can I allocate a public IP to my GPU instance?​

  * **Ephemeral Disk (NVMe):** A Floating IP can only be assigned after the instance is created. Port forwarding configuration is required.
  * **Persistent Disk:** A Floating IP can be allocated during instance creation or afterward.

### 4\. Which functions are not supported for GPU Virtual Machines with Ephemeral Disk (NVMe)?​

For VMs using Ephemeral Disk (NVMe) with NVIDIA Hopper (H100, H200) and NVIDIA Blackwell (B300), the following are unsupported: resizing instances, snapshots, creating templates from instances. Only backup instance with Veeam is supported.

### 5\. What storage options are available for GPU Virtual Machines?​

Two Block Storage types exist:

  1. **Ephemeral Disk (NVMe):** Fixed capacity per package (non-expandable), optimized for training workloads rather than long-term storage, and does not support automated backup or restore.
  2. **Persistent Disk:** Scalable on demand, optimized for long-term retention, supports automated backup and restore, with separate storage charges beyond the GPU instance cost.

File Storage (High-performance Tier) is currently only available in the Vietnam region.

### 6\. What regions are GPU Virtual Machines available?​

GPU VMs with NVIDIA Hopper (H100, H200) and NVIDIA Blackwell (B300) are offered in Hanoi 2 (Vietnam) and Tokyo (Japan).

## Billing​

### 7\. How can I be charged for GPU Virtual Machines?​

Two billing models:

  * **Reservation:** Fixed price with limited resources, billed upfront (partial or full) or afterward. Periods range from 3–9 months or 1–5 years.
  * **Pay-as-you-go (PAYG):** Unlimited resource usage with payment afterward, typically billed by the hour.

### 8\. Does FPT charge GPU Virtual Machines in the Stopped state?​

  * **Ephemeral Disk (NVMe):** Yes — stopped instances still reserve the server and incur charges. To stop accumulating charges, users must delete the instance via the FPT Cloud portal.
  * **Persistent Disk:** GPU, CPU, and RAM of stopped instances are not charged, but storage continues to be billed until deleted. Users must be on the Pay-As-You-Go (PAYG) billing plan to detach a GPU. Once detached, GPU usage isn't charged while off, but GPU availability isn't guaranteed upon powering back on since resources may be consumed by others.

Additional services and resources attached to any GPU instance also incur billing.
