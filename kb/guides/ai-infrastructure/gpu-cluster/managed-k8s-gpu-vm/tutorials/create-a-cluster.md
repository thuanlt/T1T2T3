# Create a cluster (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/ai-infrastructure/gpu-cluster/managed-k8s-gpu-vm/tutorials/create-a-cluster/

# Create a cluster

FPT Cloud supports the following cards:

  * In the Hanoi 2 and Japan regions, the following GPU cards are supported: **H100 SXM5, H200 SXM5**

## Requirements​

  * CPU, GPU, RAM, Storage, and Instance quotas: Must be sufficient for the desired Kubernetes cluster configuration. If using Autoscale, the number of GPUs must meet the desired maximum node count (note the Min node and Max node settings).
  * 01 Network subnet: Network used for Kubernetes Nodes, the subnet must have a Static IP Pool.

## Step-by-Step​

### **GPU H100 SXM5**​

**Step 1** : On the FPT Cloud Portal menu, select **Containers** > **Kubernetes** > **Create a Kubernetes Engine**.

**Step 2** : Enter the basic information for the cluster, then click the **Next** button:

#### Basic Information:​

  * Name: Enter the cluster name.

  * **Net** work: Subnet used to deploy Kubernetes Cluster Virtual Machines (VMs). 
    * **Version** : Select the version of the Kubernetes Cluster.
    * **Cluster Endpoint Access** : Select the Kubernetes cluster endpoint access option.

Step 3: Configure the Nodes Pool according to your needs, then click the **Next** button:

For the H100 card, the portal does not support creating GPU workers as the base worker group. Customers should create GPU workers starting from worker group 2 onwards.

#### Base worker group:​

  * Instance Type: Select the General Instance type
  * Type: Select the configuration (CPU & Memory) for the **Worker Nodes**.
  * Container Runtime: Select **Containerd**.
  * Policy: Select the **Storage Policy** type (corresponding to IOPS) for the Worker Node Disk.
  * Disk: Select the root disk capacity for the **Worker Nodes**.
  * Scale min: Minimum number of Worker Node VM instances for the k8s cluster. The recommended minimum is 03 Nodes for the Production environment.
  * Scale max: The maximum number of Worker Node VM instances for a worker group in the k8s cluster.
  * Label: Apply a label to **the Worker Group.**

#### Worker Group n:​

  * Select instance type: GPU
  * Select GPU type: NVIDIA H100 SXM5
  * Select GPU sharing configuration
  * Select GPU type configuration (CPU/RAM/GPU RAM)

**Note:**

  1. In the "GPU Driver Installation Type" section, there are two options: **Pre-install** and **User-install**.
  2. A driver is a program that allows the operating system to communicate with the hardware, specifically in this case between the worker's operating system (Windows, Ubuntu, etc.) and the GPU. The operating system cannot use the GPU without a driver.
  3. For the "Pre-install" option, the customer's cluster will have the Nvidia GPU driver automatically added.
  4. For the "User-install" option, customers can manually install the GPU driver to select the appropriate driver version.

**Step 4** : Click Create and review the initialization information.

**Step 5** : Monitor the Kubernetes cluster creation status. Once the status shows "Successed (Running)," proceed to use and deploy the application.

### **GPU H200 SXM5**​

**Step 1** : On the FPT Portal menu, select **Containers** > **Kubernetes** > **Create a Kubernetes Engine**.

Step 2: Enter the basic information for the cluster, then click the **Next** button:

#### Basic Information:​

  * **Name** : Enter the Cluster name.
  * **Network** : Subnet used to deploy Kubernetes Cluster Virtual Machines (VMs).
  * **Version** : Select the version of the Kubernetes Cluster.
  * **Cluster Endpoint Access** : Option to access the Kubernetes cluster endpoint.

#### Note:​

  * Customers need to select the appropriate Cluster Endpoint Access based on the security requirements and network architecture of the system.
  * If Public & Private or Private is selected, an additional Allow CIDR field will appear to enter a list of IP address ranges that have access to the Kubernetes Cluster Endpoint.

**Step 3** : Configure the Nodes Pool according to your usage needs, then click the **Next** button:

For the GPU H200, the portal does not support creating GPU workers as worker group bases. Customers are kindly requested to create GPU workers starting from worker group 2 onwards.

#### Worker Group base:​

  * Instance Type: Select General Instance Type
  * Type: Select the configuration (CPU & Memory) for the **Worker Nodes**.
  * Container Runtime: Select **Containerd**.
  * Policy: Select the **Storage Policy** type (corresponding to IOPS) for the Worker Node Disk.
  * Disk: Select the root disk capacity for **Worker Nodes**.
  * Scale min: Minimum number of Worker Node VM instances for the k8s cluster. The recommended minimum is 03 Nodes for the Production environment.
  * Scale max: The maximum number of Worker Node VM instances for a worker group in the cluster.

#### Worker Group n:​

  * Label: Assign a label to **the Worker Group**
  * Select instance type: GPU
  * Select GPU type: NVIDIA H200 SXM5
  * Select GPU sharing configuration
  * Select GPU configuration type (CPU/RAM/GPU RAM)

**Note:**

  1. In the "GPU Driver Installation Type" section, there are two options: **Pre-install** and **User-install**.
  2. A driver is a program that allows the operating system to communicate with hardware, specifically in this case between the worker's operating system (Windows, Ubuntu, etc.) and the GPU. The operating system cannot use the GPU without a driver.
  3. For the "Pre-install" option, the customer's cluster will have the Nvidia GPU driver automatically added.
  4. For the "User-install" option, customers can manually install the GPU driver to choose the appropriate driver version.

**Step 4** : Click Create and review the initialization information.

**Step 5** : Monitor the Kubernetes cluster creation status. Once the status shows Successed (Running), proceed to use and deploy the application.

* * *

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:
    
    
    GET https://ai-docs.fptcloud.com/fpt-gpu-cloud/gpu-cluster/managed-k8s-with-gpu-virtual-machine/tutorial/create-a-cluster.md?ask=<question>  
    

The question should be specific, self-contained, and written in natural language. The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
