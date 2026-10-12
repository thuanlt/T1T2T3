# Access a cluster (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/ai-infrastructure/gpu-cluster/managed-k8s-metal-cloud/tutorials/access-a-cluster/

# Access a cluster

**Step 1** : In the menu, select **Managed GPU Cluster** , and the system will display the **Managed GPU Management** page. Select the Cluster for which you want to view detailed information.

**Step 2** : The **Essential Properties** tab will display the Cluster's information.

  1. **Cluster Information** : Basic information about the cluster includes:

  * Cluster Name: The name assigned when the cluster was created
  * Version: The version of the cluster
  * Configuration: Allows you to download kube-config to communicate with the cluster
  * Network: The subnet range selected when creating the cluster
  * Status: The actual status of the cluster
  * SSH public key: The public key information selected when creating the cluster

  1. **GPU Software List:**Displays all GPU software installed on the cluster
  2. **Load Balancer Service** : Information about the Internal LB Subnet entered
  3. **API** : API URL leading to the cluster

**Step 3** : The **Node Pools** tab displays all Worker Groups belonging to the cluster and the configuration information for each Worker Group.

  * **Name** : Worker Group name
  * **Is Based** : Display (✅) if it is a Worker base, and (✘) if it is not a Worker Base
  * **Flavor Type** : Displays the selected resource flavor
  * **Number of Servers** : Number of metal cloud servers for the Worker

* * *

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:
    
    
    GET https://ai-docs.fptcloud.com/fpt-gpu-cloud/gpu-cluster/managed-k8s-with-metal-cloud/tutorial/access-a-cluster.md?ask=<question>  
    

The question should be specific, self-contained, and written in natural language. The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
