# Console KVM (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/ai-infrastructure/metal-cloud/tutorials/access-server/

# Console KVM

You can connect to the Bare Metal GPU server using SSH keys or a password. The SSH protocol (also referred to as Secure Shell) is a method for secure remote login from one server to another. To connect via SSH, make sure that all the necessary rules for incoming traffic are in the Network ACL settings set.

  1. Navigate to **AI Infrastructure** and **Metal Cloud** in the sidebar to view the Server list
  2. Choose a server in the list or view the details of a server
  3. Click **Actions** , then **Console** , or Click **Open** at Console item in the Server details page
  4. Use the **default username:** clouduser and your password, which you entered when creating the server to log in.

_The SSH key is selected when you create and deploy servers. Please refer toSSH key management._

## Prerequisites before connecting from Windows 10​

  1. Open **Windows Settings**.
  2. Go to the **Apps & features** section and click **Optional features**.
  3. Find **OpenSSH Client** and click to expand the detailed description.
  4. Click **Install**.
  5. Wait for the installation to be completed. After SSH Client is installed, restart your computer to apply the settings correctly. SSH utility will become available for cmd.

## Connect from Windows 10, Linux OS, macOS​

  1. Open the command prompt.

Authentication methods| Command| A password| `ssh username@192.168.1.92`| SSH keys| `ssh username@192.168.1.92 -i "C:\Users\username\.ssh\id_rsa"`  
---|---  
  
In there:

  * Replace "username" with your username or the **default username (clouduser)** for the first login
  * Replace "192.168.1.92" with the Floating IP address of your server
  * Replace "C:\Users\username.ssh\id_rsa" with the path to your private key file in PEM format on your computer.

_If you created a Bare Metal GPU server with only a private interface, create a floating IP address and use it when connecting to the Bare Metal over ssh._

  2. The utility will warn you that you're trying to connect to an unknown device and ask if you want to continue. Type **"yes"** and press **Enter**.

  3. (Step for connecting using a password only) enter the password you configured while creating the Bare Metal.

## Use a Bastion host (jump server)​

A jump host is an intermediate server between an originating machine and the Bare Metal GPU server you're trying to connect to. It acts like a gate between two trusted networks: You can access a destination server, but only after the jump host has allowed access.

  1. Create a Cloud instance with a subnet and a floating IP
  2. Configure Security groups
