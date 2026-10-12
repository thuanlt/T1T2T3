# Access a GPU VM (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/ai-infrastructure/gpu-virtual-machine/tutorials/access-a-gpu-vm/

# Access a GPU VM

When a GPU VM running Ubuntu is created on the FPT Portal, users can access it through the **built-in Web Console**. They can also connect externally using **SSH clients** or **third-party software like PuTTY or Bitvise**.

## Connect to a GPU VM via Web Console​

The **Web Console** enables control of all GPU VMs on **FPT Cloud** , even those lacking a **Public IP**.

**Step 1:** On the Side menu, go to **Instance Management** , find the desired VM, and under **Actions** , select **Console.**

**Step 2:** The browser opens a new window displaying the server screen, giving full control and interaction with the connected server.

## SSH to Connect to a GPU VM​

You can connect using an SSH client, typically from a terminal. You need three pieces of information:

  * **The public IP address:** Displayed in the GPU VM list or details pages after allocation
  * **The username** during initial creation is `root`
  * **The authentication method:** SSH keys (strongly recommended for additional security) or password authentication

### Step 1: Open your terminal​

  * **Linux/macOS** : Launch the Terminal app
  * **Windows** : Use CMD, PowerShell, Git Bash, or WSL

### Step 2: Connecting to your VM​

Two connection methods: password or SSH key (.pem file).

**Connect Using a Password:**

Enter the following command:
    
    
    ssh <username>@<VM_IP>  
    

**Connect Using an SSH Key (.pem file):**

  1. Navigate to the directory containing your .pem file:

    
    
    cd <path_to_pem_file_directory>  
    

  2. Use the SSH key to connect:

    
    
    ssh -i "<your_key_file.pem>" <username>@<VM_IP>  
    

  3. On first connection, type `yes` to verify the host's fingerprint and continue.

  4. You have successfully connected. Type `exit` to close the SSH session and return to your local shell.

warning

If you see the error `WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!`, the saved SSH fingerprint has changed. Remove the old fingerprint by running:
    
    
    ssh-keygen -R "<VM_IP>"
