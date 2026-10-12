# Block Storage (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/ai-infrastructure/gpu-virtual-machine/tutorials/block-storage/

# Block Storage

## Overview​

**Block Storage** provides block-based storage volumes for GPU Virtual Machines. Each disk functions like a physical hard drive when connected to a VM, enabling fast, consistent, and high-throughput data access. Compared to local NVMe storage, Block storage delivers greater durability, scalability, and persistence, ensuring data stays available even if a VM is deleted or stopped.

Two types of Block Storage disks exist:

  * **Root disk:** the primary system disk containing the OS and essential system files needed for boot and runtime. It is automatically created along with the VM during provisioning.
  * **External disk:** an independent data disk for expanding a VM's storage capacity. External disks can be detached from one VM and reattached to another, enabling flexible data reuse across workloads.

To access this service, navigate to **Main Menu** > **Compute Engine** > **Storage disks.** This page displays all Storage Disks created within the VPC, showing details such as **Name** , **Tags** , **Storage type** , **Storage policy** , **Size** , **Created At** , and **Attached** (associated VM).

## Create Storage Disks​

To create a Storage disk in FPT Cloud, first determine the disk type needed:

  * **Root disk** is automatically created with the virtual machine. References: Create a GPU VM
  * **External disk** can be created independently and attached to a virtual machine later.

You can create an **External disk** using either of the following methods:

### Method 1: Create an External disk from a Virtual machine detail page​

  1. Access the **Storage** section:

     * From the main menu, go to **Compute Engine** > **Instance management**
     * Select the desired virtual machine from the list, then click the **Storage** tab
     * Click **Create disk**
  2. Enter the required configuration:

     * **Storage policy** : Select the storage type or performance tier.
     * **Size** : Define the storage capacity.
  3. Create the disk:

     * Click **Create disk**
     * The system initializes the new disk and notifies you upon completion.
     * After success, the new External disk appears in the **Storage** tabs.

### Method 2: Create an External disk from the Storage disks page​

  1. Access the **Storage disks** page:

     * From the main menu, go to **Compute Engine** > **Storage disks**
     * Click **Create storage**
  2. Enter the required configuration:

     * **Name** : Specify the storage disk name.
     * **Type** : Choose **General** to create a new empty disk or **Snapshot** to restore from an existing snapshot.
     * **Storage policy** : Select the storage type or performance tier.
     * **Size** : Define the storage capacity.
     * **Applied instance (optional)** : Choose a VM to attach the disk to (can be done later).
  3. Create the disk:

     * Click **Create storage disk**
     * The system initializes the new disk and notifies you upon completion.
     * After success, the new External disk appears on the **Storage disks** page.

## Attach External Disks to GPU VMs​

After creation, if an External disk is not yet attached to any virtual machine, you can manually attach it. Storage disks are compatible with all OSs supported on FPT Cloud.

  1. Select the External disk you want to attach. Then click **Actions** > **Attach**.

  2. Choose the target virtual machine from the popup window and click **Attach storage disk**.

warning

  * Each Storage disk can only be attached to one virtual machine at a time.
  * For Windows virtual machines, additional configuration steps are required before the new disk becomes usable.

## Detach External Disks from GPU VMs​

You can detach an External disk from a virtual machine when it is no longer needed. After detachment, all data on the disk remains intact, and the disk can be reattached to another VM at any time.

  1. Select the External disk you want to detach from the list, then click **Actions** > **Detach**.

  2. Review the confirmation popup, then click **Detach** to confirm.

## Edit Storage Disks​

You can edit the details of a Storage disk when it is not attached to any virtual machine.

  1. Select the Storage disk you want to modify from the list, then click **Actions** > **Edit**.

  2. In the **Edit** popup, update the necessary information, then click **Edit root disk** / **Edit storage disk** to save changes.

     * **Name** : the name of the storage disk.
     * **Storage policy** : the storage type or performance tier.
     * **Size** : the capacity of the storage disk.

note

The new size must be greater than the current size — reducing disk size is not supported.

## Create Volume Snapshots​

  1. Select the Storage disk you want to back up from the list, then click **Actions** > **Create volume snapshots**.

  2. In the **Create volume snapshot** pop-up, update the necessary information, then click **Create volume snapshot**.

     * **Snapshot name** : the name for the snapshot
     * **Add tag (optional)** : tags for the snapshot

warning

  * The snapshot will contain data from the selected storage disk.
  * Creating a snapshot from an attached volume may cause data inconsistency in some cases. It's recommended to detach the disk or stop the VM before taking a snapshot for critical workloads.
  * Snapshots are stored in the **Snapshot** section and can be used to create new disks or restore data later.

## Delete Storage Disk​

A Storage disk can be automatically or manually deleted depending on its type and attachment status.

  * **Root disk** : automatically deleted together with the virtual machine it is attached to. No manual action is required.
  * **External disk** : not deleted when the associated virtual machine is removed. The disk remains available in the **Storage disks** feature and can be reattached to another VM as needed.

You can also manually delete an **External disk** at any time to avoid additional storage costs by following these steps:

warning

  * Only detached External disks (not attached to any instance) can be deleted.
  * Once deleted, all data on the disk cannot be recovered. Please proceed with caution.

  1. Select the External disk you want to delete from the list, then click **Actions** > **Delete**.

  2. Review the warning message in the confirmation pop-up and click **Delete storage disk** to confirm.

The External disk will be permanently removed from your VPC.
