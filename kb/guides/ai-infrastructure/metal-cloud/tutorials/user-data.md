# User data (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/ai-infrastructure/metal-cloud/tutorials/user-data/

# User data

User data (Cloud-init) automatically configures Bare Metal GPU servers after bootup. These scripts are typically used for initial configuration of a server and run on the first boot.

Deploying with user data lets you run arbitrary commands and modify various aspects of the server during provisioning.

Here are some examples of what you can do with user data scripts:

## Creating a user and installing basic packages​
    
    
    #cloud-config  
    users:  
      - name: cloud_user  
        ssh_authorized_keys:  
          - ssh-rsa AAAAB3Nz... user@domain  
        sudo: "ALL=(ALL) NOPASSWD:ALL"  
        groups: sudo  
        shell: /bin/bash  
    packages:  
      - git  
      - htop  
    

What this script does:

  1. Creates a user named cloud_user.
  2. Adds an SSH key to allow secure remote login.
  3. Installs packages like git (version control) and htop (system monitor).

How you can test it:

To login, use a command of this form:
    
    
    ssh -i /.ssh/id_rsa maas_user@10.192.226.195  
    

You can then test further by running htop and trying git commands.

## Setting up SSH keys for multiple users​
    
    
    #cloud-config  
    users:  
      - default  
      - name: user1  
        ssh_authorized_keys:  
          - ssh-rsa AAAAB3Nz... user1@domain  
      - name: user2  
        ssh_authorized_keys:  
          - ssh-rsa AAAAB3Nz... user2@domain  
    

What this script does:

  1. Sets up a default user.
  2. Creates user1 and user2 with their own SSH keys for secure login.

## Installing Docker​
    
    
    #cloud-config  
    packages:  
      - docker.io  
    runcmd:  
      - systemctl enable docker  
      - systemctl start docker  
    

What this script does:

  1. Installs Docker on the machine.
  2. Enables and starts Docker so it runs whenever the machine boots up.
