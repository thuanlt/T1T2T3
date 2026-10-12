# Create a GPU VM (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/ai-infrastructure/gpu-virtual-machine/tutorials/create-a-gpu-vm/

# Create a GPU VM

GPU Virtual machines are Linux-based VMs running on virtualized hardware with high-end GPUs. Each VM created serves as a new virtual server usable standalone or within a larger cloud infrastructure.

### Step 1: Open Instance Management​

Navigate via the side menu to **Compute Engine → Instance Management** , then select **Create Instance**.

### Step 2: Configure the Instance​

  1. **Instance Name:** Provide a unique name for the GPU VM.
  2. **Instance Type:** Choose the instance type. **GPU** is optimized for high-performance computing, machine learning, and other intensive tasks. Supported GPUs include **NVIDIA H100 SXM5** and **NVIDIA H200 SXM**.
  3. **Disk type:** Only one disk type selectable during creation: **Ephemeral Disk (NVMe) or Persistent Disk (Block storage)**
  4. **Image:** Use either the default Ubuntu base image or a custom image. 
     * OS: Currently supports UBUNTU 22.04 GPU
     * Custom image: Upload under **Custom Images** ; it then appears in the selection list. (File type is QCOW)
  5. **Resource type:** Each GPU VM has different configurations for vCPU, RAM, and number of attached GPUs. Choose the configuration that fits your needs.

### Step 3: Configure the Storage disk​

  * **Storage Policy:** Specifies the storage type for the GPU VM.

    * GPU VMs with **Ephemeral Disk (NVMe)** support only **NVMe-SSD**.
    * GPU VMs with **Persistent Disk** support only **Premium SSD** , offering IOPS between 3,000 and 10,000 depending on service quota.

**Size:**

    * **Ephemeral Disk (NVMe):** Fixed capacity per GPU instance, depending on GPU count in the selected Resource type.
    * **Persistent Disk:** Scalable starting from 100GB.

### Step 4: Configure the Network Settings​

  * **Subnet:** Select the appropriate subnet for internal and external connectivity.
  * **Advanced network:**
    * **Private IP:** Enter manually or let the system auto-assign based on the selected subnet.
    * **Floating IP:** For Ephemeral disk NVMe, floating IP is configured only after the VM is successfully created.
    * **Security group:** Assign a security group to manage inbound/outbound traffic.

### Step 5: Set Authentication Method​

Choose one of the following:

  * **SSH Key:** The system automatically uses your latest SSH key (changeable if needed).
  * **Password:** Set a password and store it securely for console access.

### Step 6: Advanced Settings​

#### Backup Job​

Only supports GPU VMs using Block storage - Persistent disk. You can schedule automatic backups with defined frequency and timing.

**Backup Options:**

  * **Daily Full Backup** – Full backup every day.
  * **Daily Incremental, Weekly Active Full** – Daily incremental with weekly full.
  * **Daily Incremental, Monthly Active Full** – Daily incremental with monthly full.

**Backup Time:** Set the specific time for backup execution.

#### Tags​

Assign existing tags to manage and categorize resources.

#### User Data (Cloud-init Script)​

The User Data field allows adding cloud-init scripts. When the VM starts, cloud-init reads metadata and auto-configures the system including users, SSH keys, and network settings.

**Sample Cloud-init Script:** Creates user "testcloudinit" with password "Abc123" and user "testcloudinit2" with password "P@ssw0rd!".
    
    
    users:  
    - name: testcloudinit  
      sudo: ALL=(ALL) NOPASSWD:ALL  
      lock_passwd: false  
      shell: /bin/bash  
      passwd: $6$rounds=4096$V6anciWl30$xKbcljqks1gUkMiM80pyKzhvyhn7U1n.jXcGCUfkUlX.rnllUWKUrmDEzekhhhP8aERSylRuC7gfDhJ32Xv0A1  
    - name: testcloudinit2  
      groups: sudo  
      lock_passwd: false  
      shell: /bin/bash  
      plain_text_passwd: P@ssw0rd!  
    - hostname: testcloudinit  
    

### Step 7: Billing Plans​

When creating a GPU VM with Persistent Disk, choose from two billing plans:

Billing plans| Description| **Reserved**|  GPU availability is guaranteed. Charges apply even when the VM is powered off.| **PAYG**|  When powered off, the GPU is automatically detached — no GPU charges while stopped. Only storage and floating IP costs continue. GPU availability is not guaranteed when powering back on.  
---|---  
  
You can update the billing plan after creation as long as the VM is in the **Running** state. Changes take effect immediately and reflect in your bill.

### Step 8: Create the Instance​

Click **Create Instance** to deploy and start the GPU VM.

Once created successfully, view details in the **Instance Management** dashboard.
