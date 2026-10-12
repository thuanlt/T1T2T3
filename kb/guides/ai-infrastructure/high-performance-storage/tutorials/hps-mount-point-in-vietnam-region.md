# HPS Mount Point in Vietnam Region (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/ai-infrastructure/high-performance-storage/tutorials/hps-mount-point-in-vietnam-region/

# HPS Mount Point in Vietnam Region

## What is a Mount Point?​

In File Storage – High Performance, a mount point serves as a logical access point enabling users to connect to a specific directory (path) within the storage pool.

To access data from a Bare Metal Server or GPU Virtual Machine, you must create a mount point defining how the server connects to the file storage system.

## Mount Point Configuration​

Configuration| Description| **Path**|  The directory path in the storage system to be mounted.| **Access Protocol**|  Supported protocols such as **NFSv3** or **NFSv4**.| **Access Subnet**|  Only servers within the specified subnet are allowed to mount. Servers outside this range will be denied access.  
---|---  
  
## Role of the Mount Point​

Component| Role| **Mount Point**|  Acts as the access interface from the internal network to the file storage system via NFSv3, NFSv4, or S3.| **Client (Server)**|  Mounts the file storage and displays it as a local drive.| **QoS Policy**|  Associates performance control such as IOPS or throughput limits with the mount point.  
---|---  
  
## Mount Point Structure​

Field| Description| **Name**|  Display name shown in the portal.| **Path**|  Actual directory path (e.g., `/ml-data`).| **Protocol**|  NFS protocol version (NFSv3 or NFSv4).| **Subnet**|  CIDR network range allowed to access.| **Endpoint Range**|  Connection endpoint for client access.| **QoS Policy**|  Defines performance and throughput limits.| **NFS Alias**|  An optional alias name is displayed in the operating system.  
---|---  
  
## Relationship with Other Components​

  * **VPC & Subnet:** A mount point can be assigned to multiple subnets within the same or different VPCs. Only servers in the assigned subnets can access it.
  * **QoS Policy:** Used to control performance through: 
    * Maximum Throughput (MB/s)
    * Maximum IOPS
    * Burst Limit
  * **NFS Protocol Support:**
    * **TCP:** Standard and widely used protocol.
    * **RDMA:** Provides higher performance and lower latency.
    * **Multi-Path RDMA:** Recommended for large-scale or high-throughput workloads.

warning

This feature for managing mount points in the FPT Cloud console is currently supported only in the Vietnam (Hanoi2) region and can be used exclusively with the Metal Cloud service (Bare Metal GPU servers). For HPS used with GPU VM or in Japan regions, FPT will provide a mount point to use.

## Create a Mount Point​

### Key Principles​

  * **Subnet Association:** The mount point must be assigned to a specific subnet; only servers in that subnet can connect.
  * **Avoid Root Path (`/`):** Create mount points only for subdirectories (e.g., `/project-a`, `/team1/data`).
  * **One Path – One Mount Point:** Each path can only be assigned to a single mount point (no duplicates).
  * **Unlimited Mount Points:** You can create multiple mount points as long as paths do not overlap.
  * **NFSv4 Path Export Rule:** All parent directories of the target path must also be exported. Example: To export `/project-a/team1/data`, the paths `/project-a` and `/project-a/team1` must also be exported.

### Step-by-Step​

  1. Go to **High-performance** under **File Storage** in the left-side menu, and click **Create Mount Point**.

  2. Enter the required information:

     * **Region:** Select the desired region.
     * **VPC / Subnet:** Choose the subnet containing the target server.
     * **Mount Point Name:** 3–63 characters (letters, numbers, underscores). Cannot start or end with a special character.
     * **Protocol:** Choose **NFSv3** or **NFSv4**. 
       * _NFSv3:_ You may set an NFS Alias.
       * _NFSv4:_ Ensure all parent directories are also exported.
     * **Path:** Must start with "/", cannot end with "/" or contain spaces. Optionally, check **Create new directory** if the path does not exist.
     * **QoS Policy:** Select an existing policy or create a new one.
  3. Click **Create** to complete setup.

     * **Success:** The mount point appears in the portal and is available to servers in the assigned subnet.
     * **Failure:** Review and correct the configuration parameters, then retry.

## View Details of a Mount Point​

After creating a Mount Point, you should review its configuration details in the portal to verify that all parameters are correct before starting to use it.

### Step-by-Step​

  1. In the **FPT Cloud console** , go to the **Resource** tab.
  2. In the mount point list, click a mount point name.
  3. It will show the mount point configuration and the guide to mount it with Bare Metal servers (Metal Cloud).

## Delete a Mount Point​

You can delete a mount point when it is no longer needed to:

  * Revoke access permissions.
  * Safely disconnect servers from the storage system.
  * Reconfigure network or storage settings.

### Step-by-Step​

  1. In the **FPT Cloud console** , go to the **Resource** tab.
  2. Locate the target mount point and select **Action > Delete**.
  3. Confirm the deletion when prompted.

warning

  * Ensure all clients have unmounted the storage before deletion.
  * Deleting a mount point does **not** delete the underlying data in the directory path.
