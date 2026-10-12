# Managed K8s with Metal Cloud (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/ai-infrastructure/gpu-cluster/managed-k8s-metal-cloud/overview/

# Managed K8s with Metal Cloud

## Overview​

**Managed GPU Cluster (Kubernetes)**

**FPT Managed GPU Cluster** is based on the open-source K8s platform, helping to automate the deployment, scaling, and management of containerized applications. FPT Managed GPU Cluster fully integrates the following components: Container Orchestration, Storage, Networking, Security, and PaaS, providing customers with the best environment for developing and deploying applications on the Cloud.

**FPT Managed GPU Cluster** is a Managed GPU Cluster service model provided by FKE. With MANAGED GPU CLUSTER, FPT Cloud manages all control-plane components, while users deploy and manage Worker Nodes. MANAGED GPU CLUSTER allows users to focus on application deployment without having to spend resources on managing K8s Clusters.

**FPT Managed GPU Cluster** is a service model based on the open-source Kubernetes platform, helping to automate the deployment, scaling, and management of containerized applications. The FPT Managed GPU Cluster product not only fully integrates components such as Container Orchestration, Storage, Networking, Security, and PaaS, but also provides GPU resources to support complex computing operations.

What should you consider before using **Managed GPU Cluster**?

  * **Location of the Managed GPU Cluster** : The geographic location (Region) may affect the access speed to the server during use. You should choose the Region closest to the traffic source to optimize speed.
  * **Number of Nodes and configuration of each Node to use** : All FPT Cloud accounts are allocated a certain quota for resources such as RAM, CPU, Storage, IP, etc. Therefore, customers should determine the amount of resources needed and the maximum limits to be met so that FPT Cloud can best support you.

If this is your first time using MANAGED GPU CLUSTER, first check and complete the following tasks:

* * *

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:
    
    
    GET https://ai-docs.fptcloud.com/fpt-gpu-cloud/gpu-cluster/managed-k8s-with-metal-cloud.md?ask=<question>  
    

The question should be specific, self-contained, and written in natural language. The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
