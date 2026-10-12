# How to Use HPS in Japan Region (DDN) (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/ai-infrastructure/high-performance-storage/tutorials/how-to-use-hps-in-japan-region-ddn/

# How to Use HPS in Japan Region (DDN)

## Initial Setup​

To begin using **File Storage - High Performance (HPS)** , contact the FPT Support team. After supplying the required info, your account will be activated and a quota assigned.

**Required Information**

#| Item| Unit| Required| Description| 1| Tenant/Region| —| Yes| The Tenant and Region where you want to enable the HPS service.| 2| Storage Quota| GB| Yes| The amount of storage capacity you plan to use.| 3| Subnet| Subnet CIDR| Yes| Provide the list of subnets needing access so FPT support can configure them.| 4| Performance| IOPS| No| Desired IOPS performance (default limit applied if not provided).| 5| Bandwidth| Gbps| No| Desired bandwidth (default limit applied if not provided).  
---|---|---|---|---  
  
## Use with Metal Cloud (a Bare Metal GPU server)​

note

Each subnet has its own endpoint for connecting to the file storage system. Always verify the endpoint and configuration details before performing the mount operation to avoid setup errors.

### Use FPT Images​

If using an image provided by **FPT** , the **DDN client** is pre-installed. Follow the steps below to mount the File Storage.

**Step 1: Create a Mount Point**
    
    
    mkdir /mnt/hps  
    

**Step 2: Mount the File System manually**
    
    
    mount -t lustre 100.69.252.1@o2ib,100.69.252.2@o2ib:100.69.252.3@o2ib,100.69.252.4@o2ib:100.69.252.5@o2ib,100.69.252.6@o2ib:100.69.252.7@o2ib,100.69.252.8@o2ib:/scratch /mnt/hps  
    

**Step 3: Auto-Mount Configuration**

To automatically mount the Lustre file system after reboot, add the following entry to `/etc/fstab`:
    
    
    ## LustreFS ##  
    100.69.252.1@o2ib,100.69.252.2@o2ib:100.69.252.3@o2ib,100.69.252.4@o2ib:100.69.252.5@o2ib,100.69.252.6@o2ib:100.69.252.7@o2ib,100.69.252.8@o2ib:/scratch /mnt/hps lustre flock,defaults 0 0  
    

**Explanation:**

  1. The addresses 100.69.252.1–100.69.252.8 are fixed endpoint addresses of the Lustre servers. `/scratch` is the filesystem path on the Lustre server.
  2. `/mnt/hps` is the mount point on the client (created in Step 1).

note

Run `mount -a` to verify that the mount configuration has no errors.

**Step 4: Verify**
    
    
    df -h -t lustre  
    

Expected output shows the filesystem mounted at `/mnt/hps` with approximately 11T size.

### Using Custom Images (Ubuntu)​

If using a custom image running Ubuntu, you must manually build the required packages by following these steps.

**Step 1: Build Lustre Client**

This step builds the Lustre Client package from source code when a prebuilt package compatible with your kernel version isn't available. Skip this step if a compatible package already exists on your system or if you've previously built the package for the same kernel version.
    
    
    wget https://s3-sgn10.fptcloud.com/file-storage-resource/exa-client-6.3.4.tar.gz  
    tar xzvf exa-client-6.3.4.tar.gz  
    cd exa-client  
    ./exa_client_deploy.py  
    

If your Ubuntu OS is running kernel version `5.15.0-130-generic`, you can skip the build and use prebuilt packages:
    
    
    wget https://s3-sgn10.fptcloud.com/package-pub/lustre-dev_2.14.0-ddn184-1_amd64.deb  
    wget https://s3-sgn10.fptcloud.com/package-pub/lustre-client-modules-5.15.0-130-generic_2.14.0-ddn184-1_amd64.deb  
    wget https://s3-sgn10.fptcloud.com/package-pub/lustre-client-utils_2.14.0-ddn184-1_amd64.deb  
    

**Step 2: Install Lustre Client**

Install the Lustre Client using `.deb` packages built in Step 1 or downloaded above. Only do this if matching `.deb` packages are available; otherwise return to Step 1. Kernel version mismatches may cause errors requiring a rebuild.
    
    
    sudo dpkg -i lustre-dev_2.14.0-ddn184-1_amd64.deb \  
                 lustre-client-modules-5.15.0-130-generic_2.14.0-ddn184-1_amd64.deb \  
                 lustre-client-utils_2.14.0-ddn184-1_amd64.deb  
    

**Step 3: Configure the Lustre Client**

Apply these configuration settings to optimize Lustre Client performance.

Edit `/etc/modprobe.d/lustre.conf`:
    
    
    options lnet networks=o2ib(bond0)  
    options ko2iblnd peer_credits=32 peer_credits_hiw=16 concurrent_sends=64  
    

Edit `/etc/lustre_client`:
    
    
    IF1=bond0  
    IF2=none  
    IF3=none  
    IF4=none  
    IF5=none  
    IF6=none  
    IF7=none  
    IF8=none  
    

**Step 4: Create a mountpoint in the OS**
    
    
    mkdir /mnt/hps  
    

**Step 5: Mount the File System manually**
    
    
    mount -t lustre 100.69.252.1@o2ib,100.69.252.2@o2ib:100.69.252.3@o2ib,100.69.252.4@o2ib:100.69.252.5@o2ib,100.69.252.6@o2ib:100.69.252.7@o2ib,100.69.252.8@o2ib:/scratch /mnt/hps  
    

**Step 6: Auto-Mount Configuration**

To automatically mount after reboot, add the following entry to `/etc/fstab`:
    
    
    ##LustreFS##  
    100.69.252.1@o2ib,100.69.252.2@o2ib:100.69.252.3@o2ib,100.69.252.4@o2ib:100.69.252.5@o2ib,100.69.252.6@o2ib:100.69.252.7@o2ib,100.69.252.8@o2ib:/scratch /mnt/hps lustre flock,defaults 0 0  
    

The addresses 100.69.252.1–100.69.252.8 are fixed Lustre server endpoints; `/scratch` is the server filesystem path. `/mnt/hps` is the client mount point from Step 4.

note

Run `mount -a` to verify the mount configuration has no errors.

**Step 7: Verify**
    
    
    df -h -t lustre  
    

Expected output shows the filesystem mounted at `/mnt/hps` with approximately 11T size.

## Use with a GPU Virtual Machine​

**Step 1: Attach Network Interface and Configure IP Address**

To connect to HPS Storage for H200, use the pre-created subnet named `vm-gpu-hps-net-xxx` located under **Network > Subnets**.

To attach the Network Interface:

  1. Navigate to **Instance Management**
  2. Select your target VM GPU
  3. Open the **Network Interface** tab
  4. Click **Create NIC**
  5. Select the network named `vm-gpu-hps-net-xxx`

After attaching the interface, access your server and configure the network settings manually if DHCP is not enabled for that interface.

**Step 2: Build and Install Lustre Client**

This step builds and installs the Lustre Client package from source code.
    
    
    wget https://s3-sgn10.fptcloud.com/file-storage-resource/exa-client-6.3.4.tar.gz  
    tar xzvf exa-client-6.3.4.tar.gz  
    cd exa-client  
    ./exa_client_deploy.py  
    

**Step 3: Configure the Lustre Client**

Apply these configuration settings to optimize Lustre Client performance.

Edit `/etc/modprobe.d/lustre.conf`:
    
    
    options lnet networks=tcp(eth1)  
    options ko2iblnd peer_credits=32 peer_credits_hiw=16 concurrent_sends=64  
    

Edit `/etc/lustre_client`:
    
    
    IF1=eth1  
    IF2=none  
    IF3=none  
    IF4=none  
    IF5=none  
    IF6=none  
    IF7=none  
    IF8=none  
    

**Step 4: Create a mountpoint in the OS**
    
    
    mkdir /mnt/hps  
    

**Step 5: Mount the File System manually**
    
    
    mount -t lustre 100.69.252.1@tcp,100.69.252.2@tcp:100.69.252.3@tcp,100.69.252.4@tcp:100.69.252.5@tcp,100.69.252.6@tcp:100.69.252.7@tcp,100.69.252.8@tcp:/scratch /mnt/hps  
    

**Step 6: Auto-Mount Configuration**

To automatically mount after reboot, add the following entry to `/etc/fstab`:
    
    
    ##LustreFS##  
    100.69.252.1@tcp,100.69.252.2@tcp:100.69.252.3@tcp,100.69.252.4@tcp:100.69.252.5@tcp,100.69.252.6@tcp:100.69.252.7@tcp,100.69.252.8@tcp:/scratch /mnt/hps lustre flock,defaults 0 0  
    

The addresses 100.69.252.1–100.69.252.8 are fixed Lustre server endpoints; `/scratch` is the server filesystem path. `/mnt/hps` is the client mount point from Step 4.

note

Run `mount -a` to verify the mount configuration has no errors.

**Step 7: Verify**
    
    
    df -h -t lustre  
    

Expected output shows the filesystem mounted at `/mnt/hps` with approximately 11T size.
