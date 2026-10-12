# Quickstart (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/ai-infrastructure/metal-cloud/quickstart/

# Quickstart

Bare Metal GPUs servers are dedicated, single-tenant servers with 8 GPUs that can operate standalone or in multi-node clusters.

**Supported GPUs by Region**

  * **Hanoi 2 (Vietnam)** : NVIDIA H100 SXM, NVIDIA B300
  * **Tokyo (Japan)** : NVIDIA H200 SXM

## Sign Up for an Account​

  1. Access https://id.fptcloud.com/ and choose **Sign up**.
  2. Check your **Junk** email folder if the confirmation email isn't in your **Inbox**.
  3. Sign in to https://console.fptcloud.com/ for Vietnam region and https://console.fptcloud.jp/ for Japan region.

## Create a Subnet​

A subnet is required to create and deploy your Bare Metal GPU server.

  1. Click **AI Infrastructure** and select **Subnet** in the Sidemenu.
  2. Follow the detailed guide at fptcloud.com/en/documents/metal-cloud/?doc=subnet.

## Create Bare Metal GPU Servers​

  1. Click **AI Infrastructure** and select **Metal Cloud** in the Sidemenu.
  2. Choose **Create server** and configure the server deployment.
  3. Two FPT images for GPU and AI/ML are available; check software dependencies at their OS image doc.
  4. You may select a **Floating IP (Public IP)** during creation or attach it later under **Network/Floating IP**.
  5. Follow the detailed guide at fptcloud.com/en/documents/metal-cloud/?doc=create-server.

## Access to Servers​

  1. **Attach a Floating IP** if not chosen during creation (guide at server-action).
  2. Configure **Network ACL** (doc at network-acl) to create an inbound rule allowing your Public IPs.
  3. SSH into the server with your SSH key or password as configured during creation.
  4. You can also set a **Jump host** for additional security settings (guide at access-server doc).

_The default username is**`clouduser`**._

## Notices​

  * Check **Tenant & Region** after accessing the FPT Cloud Console. AI Factory is only supported in the **Hanoi 2** (Vietnam) and **Tokyo** (Japan) regions.

  * You may change the default **Network ACL** , but ensure other required rules are set for creating servers. The default outbound rule is:

Priority| Type| Protocol| Port| Destination| Traffic Action| 100| ALL| ALL| ALL| 0.0.0.0/0| ALLOW  
---|---|---|---|---|---  
  
If you delete that default rule, you must add these outbound rules to create and deploy the server:

Priority| Type| Protocol| Port| Source| Traffic Action| 1| HTTP| TCP| 80| 0.0.0.0/0| ALLOW| 2| HTTPS| TCP| 443| 0.0.0.0/0| ALLOW| 3| DNS (UDP)| UDP| 53| 0.0.0.0/0| ALLOW  
---|---|---|---|---|---  
  
  * FPT sets limitation (quota) for resource quantity according to your contracts/agreements. If you run out of resources, you cannot create new ones. Contact your salesman or FPT Smart Cloud Support.
