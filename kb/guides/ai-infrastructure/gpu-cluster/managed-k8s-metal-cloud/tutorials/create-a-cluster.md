# Create a cluster (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/ai-infrastructure/gpu-cluster/managed-k8s-metal-cloud/tutorials/create-a-cluster/

# Create a cluster

**Step 1** : On the **FPT Portal** menu, select **AI Infrastructure** > **Managed GPU Cluster** >Create a Managed GPU Cluster.

**Step 2** : Enter the information in the General Information tab of the Cluster, then click the **Next button** :

  1. General Information:

  * **Name** : Enter the Cluster name. Cluster names must be unique and follow the rules.
  * **Network** : Select from the subnet range created for Bare Metal GPU Servers
  * **Version** : Select the Kubernetes version compatible with the customer's current application.

  2. Load Balancer Service:

  * **Internal LB Subnet** : Configure the private IP range for the Load Balancer service type.

  3. Nodes Credentials:

  * **SSH Public Key** : SSH Key to SSH into the Cluster's Worker node

  4. GPU Information:

The **GPU Information section** allows you to configure the GPU software to install for your Kubernetes cluster. This is necessary if the cluster has nodes that use GPUs to accelerate workloads such as AI/ML, HPC, etc.

  * GPU Software: Select the type of GPU software to install for the cluster. Current options: 
    * GPU Operator: GPU Operator helps manage GPUs and NVIDIA drivers on Kubernetes.
    * Network Operator: Supports installing GPU Direct RDMA for high-speed data transfer over the network.

**Step 3** : Enter the information in the Nodes Pool tab of the Cluster, then click the **Next** button: Important points to note when creating a MANAGED GPU CLUSTER:

  * **Managed GPU Cluster** manages Worker nodes through Worker Groups, which are groups consisting of Worker nodes with identical configurations. Users can divide Worker Groups for appropriate applications. The system requires a minimum of one Worker Group (Base), which users cannot delete.
  * In the Worker Group configuration section, users can assign labels to the desired Worker Group. This label will be applied to all Worker nodes belonging to the Worker Group. Users can add or remove labels, as well as edit the key/value of existing labels. These labels make it easy for users to deploy applications on separate Worker Groups as needed.

**Worker Group 1 (Base):**

  *     * **Group Name** : Name the Worker Group to distinguish it from other Worker Groups.
    * **Runtime** : Select the container runtime; currently, the system only supports the Containerd container runtime.
    * **Number of Servers** : The number of Metal Cloud Servers created to run Workers in the Cluster.
    * **Flavor** : The flavor type of the Metal Cloud GPU server, default is H100.
    * **Worker MIG Strategy:**

MIG = Multi-Instance GPU: Split a physical GPU (such as H100) into multiple smaller GPUs multiple applications/Pods to share.

  * **None** : No GPU splitting - each Pod uses the entire physical GPU.
  * **Single** : Each GPU is divided into smaller portions.
  * MIG-single-7x1g.10gb: Divide the physical GPU into 7 instances of 1g.10gb
  * MIG-single-4x1g.20gb: Split the physical GPU into 4 instances of 1g.20gb
  * MIG-single-3x2g.2gb: Divides the physical GPU into 3 instances of 2g.20gb
  * MIG-single-2x3g.40gb: Divides the physical GPU into 2 instances of 3g.40gb
  * MIG-single-1x4g.40gb: Split the physical GPU into 1 instance of 4g.40gb
  * MIG-single-1.7g.80gb: Split the physical GPU into 1 instance of 7g.80gb

→ If you do not need to split the GPU, select **None**.

  *     * **GPU Driver** : Allows the operating system to recognize and use the hardware GPU. (Example: NVIDIA Driver)
  * **Pre-Install** : The NVIDIA driver has been **pre-installed** on the virtual machine by FPT Cloud.
  * **Driver Version** : FPT Cloud supports driver version 550.90.07 - CUDA 12.4 
    * **Label** : Apply a label in Kubernetes to all workers in the worker group.

Users can add worker groups when creating a k8s cluster by clicking the **ADD WORKER GROUP** button.

Additionally, starting from Worker Group 2, users can configure taints for worker groups to schedule applications on worker nodes. Taints can also be easily added, removed, or edited.

**Note** : When configuring labels/taints for a worker group on Unify Portal, users will not be able to remove labels/taints for nodes in that worker group using kubectl (the system will automatically reapply labels/taints to nodes according to the configuration on Unify Portal). Therefore, it is necessary to remove the label/taint configuration on Unify Portal.

Learn more about Taints here

**Note** : When configuring labels/taints for a Worker Group on the Portal, users will not be able to remove labels/taints for nodes in that Worker Group using kubectl (the system will automatically reapply labels/taints to nodes based on the configuration on the Portal). Therefore, it is necessary to remove the label/taint configuration on the Portal.

**Step 4** : The **Advanced** section contains advanced settings

  * **Pod Network** : The network used for Pods in the Cluster.
  * **Service Network** : Network used for Services in the Cluster.
  * **Network Node Prefix** : Maximum number of Pods per Managed GPU Node.
  * **Max Pod per Node** : The CNI type installed for the Cluster, only supports Calico.

**Step 5:** The Review & Create screen will display the cluster information that the user has configured previously, and the system will automatically check whether the Bare Metal GPU server quota is sufficient to create the cluster.

After the system successfully checks the resources, click the Create a Managed GPU Cluster button

to proceed with creating the cluster.

You can view and manage the list of GPU Clusters you have created on the Managed GPU Cluster page.

Management page. To open the Management page, follow these steps:

On **the FPT Portal** , select **AI Infrastructure** > **Managed GPU Cluster** from the menu. The system will display a list of created Clusters with important information such as: **Name** , **Version** , **Worker Group** , **Status** , **Created At** , **Actions**.

* * *

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:
    
    
    GET https://ai-docs.fptcloud.com/fpt-gpu-cloud/gpu-cluster/managed-k8s-with-metal-cloud/tutorial/create-a-cluster.md?ask=<question>  
    

The question should be specific, self-contained, and written in natural language. The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
