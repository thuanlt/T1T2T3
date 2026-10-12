# Managed K8s with GPU Virtual Machine (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/ai-infrastructure/gpu-cluster/managed-k8s-gpu-vm/overview/

# Managed K8s with GPU Virtual Machine

## Overview​

FPT Cloud provides Kubernetes using NVIDIA GPUs with the following key features:

  * Flexible GPU configuration with multiple GPU types, optional GPU memory, applied per Worker Group.

  * Automated management and provisioning of GPU resources in Kubernetes with NVIDIA Operator.

Visualization and monitoring of GPUs using NVIDIA DCGM.

  * Automatically scale containers/nodes with Autoscaler when application demand for GPU resources increases/decreases.

  * Support GPU sharing with the Multi-Instance mechanism, helping to optimize GPU resource and cost usage.

FPT Cloud uses NVIDIA GPU Operator to provide tools for automatically managing all the software components needed to use GPUs on Kubernetes. GPU Operator allows users to use GPU resources just like they use CPUs in a Kubernetes cluster.

The Operator's components include:

  * NVIDIA Drivers (CUDA, MIG, etc.)
  * NVIDIA Device Plugin
  * NVIDIA Container Toolkit
  * NVIDIA GPU Feature Discovery
  * NVIDIA Data Center GPU Manager (Monitoring)

In the Hanoi 2 and Japan regions, FPT Cloud currently supports Kubernetes using Nvidia H100 GPUs and Nvidia H200 GPUs

**No.**| **GPU H100 SXM5**| **Strategy**| **Number instance**| **Instance resource**|  1| all-1g.10gb| single| 7| 1g.10gb| 2| all-1g.20gb| single| 4| 1g.20gb| 3| all-2g.20gb| single| 3| 2g.20gb| 4| all-3g.40gb| single| 2| 3g.40gb| 5| all-4g.40gb| single| 1| 4g.40gb| 6| all-7g.80gb| single| 1| 7g.80gb| 7| all-balanced| mixed| 2  
1  
1| 1g.10gb  
2g.20gb  
3g.40gb| 8| none (no label)| none| 0| 0 (Entire)  
---|---|---|---|---  
  
**No.**| **GPU H200 SXM5**| **Strategy**| **Number instance**| **Instance resource**|  1| all-1g.18gb| single| 7| 1g.18gb| 2| all-1g.35gb| single| 4| 1g.35gb| 3| all-2g.25gb| single| 3| 2g.25gb| 4| all-3g.71gb| single| 2| 3g.71gb| 5| all-4g.71gb| single| 1| 4g.71gb| 6| all-7g.141gb| single| 1| 7g.141gb| 7| all-balanced| mixed| 2  
1  
1| 1g.18gb  
2g.35gb  
3g.71gb| 8| none (no label)| none| 0| 0 (Entire)  
---|---|---|---|---  
  
_**Example:**_

  * If you select the single strategy configuration: all-1g.10gb, the H100 GPU card on the worker is divided into 7 mig-devices with logical GPU resources (equal to 1/7 of the physical GPU) and 10GB of GPU RAM.

**Note:**

MIG configuration applies to all cards attached to the worker. The MIG strategy on worker groups within the same cluster must be the same type (single/mixed/none).

### Terminology and Definitions[TP1]​

| |  **Terminology**|  **Definition**|  **K8s**|  Kubernetes|  **FKE**|  FPT Kubernetes Engine|  **D-FKE**|  Dedicated – FPT Kubernetes Engine|  **M-FKE**|  Managed – FPT Kubernetes Engine|  **Master Node**|  Nodes containing control plane components|  **Worker nodes**|  Nodes used for executing workloads|  **Automatic scaling of nodes**|  Automatic scaling of worker nodes (increase/decrease)|  **K8S cluster**|  A collection of nodes (VMs) configured as a Kubernetes cluster.|  **NFS persistent storage**|  A "persistent" storage partition on NFS.|  **Pod**|  The smallest unit managed by Kubernetes. A Pod contains one or more containers.|  **Pod network**|  The network/subnet used to assign IP addresses to Pods.|  **Service Network**|  The network/subnet used to assign IP addresses to services.  
---|---  
  
* * *

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:
    
    
    GET https://ai-docs.fptcloud.com/fpt-gpu-cloud/gpu-cluster/managed-k8s-with-gpu-virtual-machine.md?ask=<question>  
    

The question should be specific, self-contained, and written in natural language. The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
