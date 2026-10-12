# Quickstart (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/ai-infrastructure/gpu-virtual-machine/quickstart/

# Quickstart

## Sign up for an account​

### Create an FPT Cloud account​

  * Visit fptcloud.com, click **Sign Up** , and follow instructions to enter your details.
  * The support team will contact you to verify information and activate your account.

### Log in to the FPT Portal​

  * Sign in to console.fptcloud.com (Vietnam) or console.fptcloud.jp (Japan) with your FPT Cloud credentials, depending on where your quota is provisioned. Select the correct **Tenant and Region**.
  * **Supported GPUs by Region:**
    * **Hanoi 2 (Vietnam):** NVIDIA H100 SXM, NVIDIA B300
    * **Tokyo (Japan):** NVIDIA H200 SXM
  * **Set up an SSH key:** Navigate to **SSH Management** to generate an SSH key for secure server access.

## Step-by-step​

### Create a Subnet​

A subnet is required before deploying your GPU VM.

  1. In the left-side menu, go to **Network → Subnets**.
  2. Click **Create Subnet** and complete the configuration.

Detailed guide: Create a Subnet

### Create a GPU VM​

  1. In the side menu, go to **Compute Engine** → **Instance Management**.
  2. Click **Create Instance** and configure the VM deployment. 
     * **Choose the instance type:** H100 instances on the .com site; H200 instances on the .jp site.
     * **Select a disk type:**
       * **Ephemeral Disk (NVMe)** – bundled with the instance, cannot be resized.
       * **Persistent Disk (Block Storage SSD)** – required, minimum size of **100 GB**.

Detailed guide: Create a GPU VM

### Allocate a public IP address (Floating IP)​

  1. In the left-side menu, go to **Network → Floating IPs**.
  2. Click **Allocate IP Address** and assign the IP to your VM. 
     * **Ephemeral Disk (NVMe):** Use **port forwarding (NAT)** to connect the floating IP with the VM, specifying both the **IP port** and the **Instance port.**

Detailed guide: Floating IPs

### Create Security Group​

By default, the Default Security Group allows all outbound traffic. You must create a new one to allow inbound rules to access the VM.

  1. Click on **Network** and select **Security Groups** in the Side menu.
  2. Choose **Create Security Group** and define inbound rules (e.g., allow SSH access on port 22 from your client's public IP).

Detailed guide: Security Group

### Access to GPU Virtual Machine​

After creating the GPU VM, you can access the server via SSH:

  1. **Terminal:** Open your terminal and enter the command with your SSH key.
  2. **Web Console:** Go to the server's detail page and click "Open at Console" to log in with a password through the web console.

The default username is `root`.

Detailed guide: Access a GPU VM
