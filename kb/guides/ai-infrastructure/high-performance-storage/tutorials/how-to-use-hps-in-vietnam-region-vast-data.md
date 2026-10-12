# How to Use HPS in Vietnam Region (VAST Data) (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/ai-infrastructure/high-performance-storage/tutorials/how-to-use-hps-in-vietnam-region-vast-data/

# How to Use HPS in Vietnam Region (VAST Data)

## Initial Setup​

To start using **File Storage - High Performance (HPS)** , contact the FPT Support team. After providing required info, your account gets activated, a quota is assigned, and the feature is enabled on the **FPT Cloud console**.

**Required Information**

#| Item| Unit| Required| Description| 1| Tenant/Region| —| Yes| The Tenant and Region where you want to enable the HPS service.| 2| Storage Quota| GB| Yes| The amount of storage capacity you plan to use.| 3| Subnet| Subnet CIDR| No (Metal Cloud) / **Yes (GPU VM)**|  Provide subnets needing access so support can configure them.| 4| Performance| IOPS| No| Desired IOPS (default limit applied if not provided).| 5| Bandwidth| Gbps| No| Desired bandwidth (default limit applied if not provided).  
---|---|---|---|---  
  
## Use with Metal Cloud (a Bare Metal GPU server)​

note

Each subnet has its own endpoint. Always verify endpoint and config details before mounting.

### Use FPT Images​

If using an FPT-provided image, the VAST client is pre-installed.

**Step 1: Create a Mount Point in OS**

Create the directory, e.g.:
    
    
    mkdir /mnt/hps  
    

**Step 2: Mount the File System manually**

Mount via TCP — use `mount -o proto=tcp,vers=3` with the endpoint IP and mount point path. For improved performance, add `nconnect=16`.

Mount via RDMA — use `mount -o proto=rdma,port=20049,vers=3` with the endpoint and path. With nconnect: add `nconnect=16` to the options.

Mount via Multi-Path RDMA — use options including `vers=3,proto=rdma,port=20049,spread_reads,spread_writes,nconnect=16` along with `localports` and `remoteports` parameters specifying the relevant IP ranges.

**Step 3: Auto-Mount Configuration**

To auto-mount after reboot, add an entry to `/etc/fstab` with the same NFS mount options (e.g., `vers=3,proto=rdma,port=20049,spread_reads,spread_writes,nconnect=16` plus local/remote ports), followed by `0 0`. Then verify with `mount -a`.

### Use custom images​

**Step 1: Install VAST NFS Client**

Install prerequisites:
    
    
    apt update && apt install -y nfs-common dpkg-dev autotools-dev debhelper curl  
    

Download and build the client: run the download script from the FPT S3 URL, extract the tarball, run `./build.sh bin`, install the resulting .deb package, then run `depmod -a`, `update-initramfs`, reinstall nfs-common, and reboot.

**Step 2: Create a Mount Point**
    
    
    mkdir /mnt/hps  
    

**Step 3: Mount the File System**

note

Replace `10.101.33.1` with the endpoint provided by the support team.

Same mount options as described above for TCP, RDMA, and Multi-Path RDMA.

**Step 4: Auto-Mount Configuration**

Add the appropriate entry to `/etc/fstab` matching your mount options, then verify with `mount -a`.

## Use with a GPU Virtual Machine​

**Step 1: Attach a Network Interface and Configure the IP Address**

To connect to HPS Storage for H100, attach a NIC using the pre-created subnet `vm-gpu-hps-net-xxx` found under **Network > Subnets**.

  1. Go to **Instance Management**.
  2. Select your target VM GPU.
  3. Open the **Network Interface** tab.
  4. Click **Create NIC**.
  5. Select the network named `vm-gpu-hps-net-xxx`.

After attaching the interface, log in and manually configure network settings if DHCP is not enabled for that interface.

**Step 2: Install the NFS Client**
    
    
    sudo apt update  
    sudo apt install nfs-common -y  
    sudo reboot  
    

**Step 3: Create a Mount Point**
    
    
    mkdir /mnt/hps  
    

**Step 4: Mount the File System**

note

Replace `10.101.33.1` with the endpoint provided by the support team.

Mount via TCP using `mount -o proto=tcp,vers=3` with the endpoint and path. With nconnect, add `nconnect=16`.

**Step 5: Auto-Mount Configuration**

Add an entry to `/etc/fstab` such as:
    
    
    10.101.33.1:/test /mnt/hps nfs vers=3 0 0  
    

Then verify with `mount -a`.
