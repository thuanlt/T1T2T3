# Initial Setup (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/ai-infrastructure/gpu-cluster/managed-k8s-metal-cloud/initial-setup/

# Initial Setup

### 1\. Register a new account​

Then select the **Sign Up** and enter the information according to the system instructions. The support team will contact you shortly thereafter to confirm the information and create your account.

To log in to the FPT Portal, please visit console.fptcloud.com or console.fptcloud.jp.

After logging in with your assigned account and password, select the correct Tenant, Region, and VPC.

If you are unsure about the above information or the system returns an error after 3 attempts, please contact our Support team immediately for assistance.

**Note** : Your account must have two-factor authentication (MFA) enabled to use the AI Factory product.

### 2\. Create Subnets for Bare Metal GPU Servers used in Managed GPU Clusters​

To create a Managed GPU Cluster, you first need a subnet range on Bare Metal GPU Servers. These computers will act as Worker nodes in the K8s Cluster. IPv4 addresses for the Worker Bare Metal GPUs will be dynamically assigned from this subnet.

**Step 1:** Go to [AI Infrastructure] > select [Subnets] > select [Create Subnet]

**Step 2** : Enter the desired name for the subnet

**Step 3:** Enter a name for the Network ACL associated with the subnet

**Step 4** : Click [Create Subnet] to complete the subnet creation process for Bare Metal GPU

**Note** : The Network ACL created by default for the subnet will block all inbound traffic and allow all outbound traffic. To use Load Balancer for Managed GPU Cluster, you need to open the appropriate Rules for the Load Balancer subnet range to allow connections.

### 3\. Create Subnets for Load Balancer​

Managed GPU Clusters only work with Subnets that have the Static Pool option enabled, so you need to create a Subnet with Static Pool following these instructions:

**Step 1:** In the **Network** section, select the **Subnets** tab

**Step 2** : Select **Create Subnet** on the **Subnets Management** page

**Step 3:** Enter the following information:

**Name:** Enter a memorable name for the Subnet

**CIDR** : Enter a valid CIDR

Check the **Advanced settings** option

**Static IP Pool** : Enter a valid IP range obtained from CIDR.

Select **Save** to create a new Subnet. The system will process and notify you of the result.

### 4\. Request to activate the Managed GPU Cluster service and allocate resource quotas.​

If this is your first time using FPT Cloud, some services may not yet be available for your account. Please contact our support team and provide information about the services and desired configuration. We will provide you with the necessary resources such as RAM, CPU, Storage, Public IP, etc., so you can start using the Managed GPU Cluster service.

Contact our support team via:

**Hotline** : 18006139

**Email** : support@fptcloud.com

**Note:** Certain mandatory conditions apply for this operation:

  * Quota Metal Cloud (Bare Metal HPC) must meet the desired number of clusters. At least 01 BM server Network
  * At least 01 Network for Load Balancer

* * *

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:
    
    
    GET https://ai-docs.fptcloud.com/fpt-gpu-cloud/gpu-cluster/managed-k8s-with-metal-cloud/initial-setup.md?ask=<question>  
    

The question should be specific, self-contained, and written in natural language. The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
