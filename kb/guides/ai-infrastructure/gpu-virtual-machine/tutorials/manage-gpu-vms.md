# Manage GPU VMs (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/ai-infrastructure/gpu-virtual-machine/tutorials/manage-gpu-vms/

# Manage GPU VMs

## Power off​

  1. Open the **Instance management**
  2. Find the GPU VM you want to power off and click the 3-dot icon.
  3. Select **Power off** action

## Power on​

  1. Open the **Instance management**
  2. Find the GPU VM you want to power on and click the 3-dot icon.
  3. Select the **Power on** action

## Reboot​

warning

The reboot function performs a hard reboot, which may cause data loss, corrupted software, or other issues.

  1. Open the **Instance management**
  2. Find the GPU VM you want to reboot and click the 3-dot icon.
  3. Select **Reboot** action

## Rename​

  1. Open the **Instance management**
  2. Find the GPU VM you want to rename and click the 3-dot icon.
  3. Select **Rename** action
  4. Rename your VM and click **Rename instance**

## Reset password​

  1. Open the **Instance management**
  2. Find the GPU VM you want to reset the password for and click the 3-dot icon.
  3. Select the **Reset password** action, and an email with the new password will be sent to your email address.

## Edit GPU plan​

You can update the GPU plan of an existing GPU VM that uses Block Storage (Persistent Disk) while it is in Running status.

  1. Navigate to **Instance Management** or the Instance Details page.
  2. Open the **Actions** menu next to your running instance and select **Edit GPU Plan**.
  3. Choose one of the following options in the pop-up window: 
     * **Hold GPU (Default):** Retains the GPU when the VM is stopped, guaranteeing instant availability upon restart.
     * **Detach GPU:** Releases the GPU when the VM is stopped. Availability is not guaranteed when restarting.
  4. Save your changes. The billing system will automatically adjust charges based on the selected plan and VM state.

note

If your instance is stopped or restarting, the Edit GPU Plan option will be disabled.

## Lock a GPU VM​

Users can lock a VM to prevent deletion, helping avoid accidentally removing an active VM instead of a test machine. This feature reduces the risk of user error and protects data on virtual machines. To lock a VM:

  1. Open the **Instance management**
  2. Find the GPU VM you want to lock and click the 3-dot icon.
  3. Select **Lock** action.
  4. A warning dialog appears showing the VM name and asking for confirmation. Click **Lock Instance Deletion** to proceed. Once locked, the system prevents the VM from being deleted until unlocked.

## Unlock a GPU VM​

To delete a VM, users must first unlock it. Follow these steps:

  1. In the menu, select **Instance Management** , then under **Actions** , click **Unlock Deletion**.
  2. A warning dialog appears showing the VM name and asking for confirmation. Click **Unlock Instance Deletion** to unlock. Once unlocked, the system allows the VM to be deleted normally.

## Delete a GPU VM​

warning

Deleting a VM permanently removes all data and cannot be undone. Back up important data before proceeding.

  1. Open the **Instance management**
  2. Find the GPU VM you want to delete and click the 3-dot icon.
  3. Confirm by entering **delete** in the text field and clicking **Delete instance**.
