# Snapshot (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/ai-infrastructure/gpu-virtual-machine/tutorials/snapshot/

# Snapshot

Snapshots are on-demand disk images of GPU VMs and volumes saved to your account. They let you create new GPU VMs and volumes with identical contents.

warning

This feature only supports GPU VMs using Block storage - Persistent disk.

## Create a Snapshot​

The snapshot feature captures the current state of a VM, allowing quick recovery or rollback after system changes or failures.

**Step 1:** Open **Instance management** on the Side menu

**Step 2:** Locate the GPU VM for which you want a snapshot and click the 3-dot icon.

**Step 3:** Create an instance snapshot by providing a snapshot name and tag (optional)

Created snapshots will appear in the **Snapshot** section.

## Use a Snapshot​

**Step 1:** Open **Snapshot** on the Side menu

**Step 2:** Find the snapshot you want to use and click the 3-dot icon. Only active snapshots can be used.

**Step 3:** Available actions include:

  * **Launch as an instance** : Create a new VM directly from this snapshot
  * **Create storage disk** : Generate a new storage volume based on the snapshot's data
  * **Manage tags** : Add or edit tags to organize the snapshot
  * **Delete image** : Permanently delete the snapshot

## Delete a Snapshot​

**Step 1:** Select **Snapshot** from the menu, then under the snapshot's **Actions** menu, click **Delete Image**.

**Step 2:** Click **Delete Snapshot**.

Once confirmed, the system deletes the image and frees up snapshot resources used by the VPC. You'll be notified upon completion.

If you check the option **"Delete all volume snapshots attached to this image"** , all snapshots from the storage disk attached to that VM will also be deleted.
