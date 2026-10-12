# Floating IPs (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/ai-infrastructure/gpu-virtual-machine/tutorials/floating-ips/

# Floating IPs

## Overview​

A **Floating IP** (or **Public IP**) is a publicly reachable **static IPv4 address**. It can be **assigned or reassigned** to a **GPU Virtual Machine** for internet accessibility, and **removed** whenever external access is no longer needed.

## Attach Floating IPs​

Once a **GPU VM** is created, you can assign a **Floating IP** to enable internet connectivity.

### Step 1: Access the Allocate IP Address Feature​

Two methods are available:

**Method 1:** Navigate to **Networking → Floating IPs** in the left menu, then click **Allocate IP Address**.

**Method 2:** Go to **Instance Management** in the left menu, select the target VM, and click the **Floating IP** button.

### Step 2: Fill in IP Address Information​

A pop-up appears with the following fields:

Fields| Description| **IP Address**|  Choose an available reserved IP, or select "Allocate new from pool" if quota permits.| **Resource**|  Pick **Instance** , then choose the GPU VM name. If launched from Instance Management, the VM is pre-filled. Select "Not assign IP to instance" to reserve without attaching.| **IP Port**|  The external port on the Floating IP for forwarding traffic. NAT rules can be configured per port; each port on one IP must be unique. Leaving it blank forwards all ports.| **Instance Port**|  The internal port receiving forwarded traffic. NAT rules apply similarly; uniqueness is required. Blank means all ports forwarded.| **Add Tag**|  Optional field for resource categorization and management.  
---|---  
  
warning

For GPU VMs using an **Ephemeral (NVMe) disk** , port settings are mandatory — set IP Port and Instance Port to **22** for SSH. Additional ports can be added. For **Block Storage - Persistent disk** , port configuration is optional.

### Step 3: Confirm Allocation​

Click **Allocate Floating IP** to confirm. The new Floating IP appears in the list and can be attached to a VM.

## Detach Floating IPs​

To detach a Floating IP for reassignment or removal:

**Step 1:** On the **Floating IP Management** page, find the IP and select **Disconnect Instance** under Actions.

**Step 2:** A confirmation pop-up appears; click **Disconnect** to proceed.

## Release Floating IPs from the VPC​

To permanently remove an unused Floating IP:

**Step 1:** On the **Floating IP Management** page, locate the IP and choose **Release IP** under Actions.

**Step 2:** Confirm by clicking **Release** in the pop-up.
