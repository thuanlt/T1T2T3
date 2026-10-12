# FAQ (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/ai-infrastructure/metal-cloud/faq/

# FAQ

## General​

  1. **What is Metal Cloud?** Metal Cloud is a service from FPT offering dedicated physical servers with built-in GPU components. Unlike virtualized cloud offerings, these servers are fully dedicated, giving users complete hardware control with no virtualization layer, maximizing performance for demanding tasks.

  2. **How does Metal Cloud differ from Cloud server (Virtual Machine) instances?** Cloud server instances are virtualized and shared, whereas Metal Cloud provides direct access to dedicated physical hardware. This removes "noisy neighbors" risks and delivers superior performance for intensive workloads such as AI/ML and HPC.

  3. **How does Metal Cloud work?** It provisions a physical, dedicated server including GPU components, suited for high-demand applications like AI/ML model training, custom orchestration, or any workload requiring stable and high-performance infrastructure.

  4. **How long does it take to deploy a Bare Metal GPU server?** Deployment takes roughly 20 minutes with FPT images. Custom image size or high demand may affect timing.

  5. **What advanced use cases does Metal Cloud support?**

     * **AI/ML Workloads:** Training, fine-tuning, and inference at scale.
     * **Custom Orchestrations:** Kubernetes containers, Slurm workload management, and complex application setups.
     * **High-Performance Computing:** Simulations, scientific computations, and real-time data processing.

## Features​

  6. **Which features does Metal Cloud currently support?**

     * **Operating System Images:** FPT-provided AI-specific images.
     * **Startup Scripts:** For automating initial configurations.
     * **SSH Key Preloading & Password Setup:** For simplified access and security.
     * **Networking:** Additional IPs, subnets, and network ACLs for security.
     * More features are noted as coming soon.
  7. **What storage options are available for Metal Cloud?**

     * **NVMe Local Storage:** Available on Bare Metal GPU servers.
     * **File Storage (High-Performance Tier):** Supported.
     * Block Storage is not supported.
  8. **Does Bare Metal Cloud support RAID?** Yes — local storage supports RAID 0 and RAID 1 via a hardware RAID controller through the FPT Cloud Portal GUI. RAID 5 is available upon request from FPT engineers.

  9. **Where is Metal Cloud available?** Currently available in:

     * **Hanoi 2, Vietnam**
     * **Tokyo, Japan**

## Billing​

  10. **How is Metal Cloud billed?** It uses a reservation-based pricing model where you pay a fixed price for a set amount of resources. Billing can be upfront (partially or fully) or recurring, with periods typically ranging from months to years.
