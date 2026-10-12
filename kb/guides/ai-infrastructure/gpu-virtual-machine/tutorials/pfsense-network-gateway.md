# pfSense Network Gateway (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/ai-infrastructure/gpu-virtual-machine/tutorials/pfsense-network-gateway/

# pfSense Network Gateway

Redundant Configuration (HA) Setup Procedure

This article covers building a highly available network gateway with pfSense, a FreeBSD-based open source tool for stable network environments.

## What is pfSense?​

pfSense is open source router/firewall software built on FreeBSD, capable of implementing router, firewall, VPN, and proxy functions. The official documentation describes virtual network gateway configuration for ExpressRoute/Site-to-Site VPN, making it suitable for many corporate environments.

## File Preparation​

### Step 1: Download pfSense ISO file​

Visit the official pfSense website and download the latest ISO image.

### Step 2: Login to FPT Cloud Console​

Go to the FPT Cloud Console URL and log in with provided credentials.

### Step 3: Uploading an ISO file​

Select the downloaded pfSense ISO and upload it to the portal. A confirmation message appears upon completion.

## Network Environment Preparation​

### Step 1: Create a new subnet​

In the FPT Cloud Console, create a new subnet per your requirements, enabling assignment of necessary IP addresses to pfSense network interfaces.

### Step 2: Creating a security group​

Define security rules and create appropriate security groups to control communication and network traffic between pfSense virtual machines.

## Creating a pfSense Virtual Machine​

### Step 1: Compute Engine​

Navigate to the Compute menu in the FPT Cloud console and click **Create Instance**.

### Step 2: Basic information settings​

Set an instance name (e.g., pfsense-master or pfsense-slave) and select the uploaded pfSense ISO in the ISO image option.

### Step 3: Resource and network configuration​

Choose appropriate resource size (CPU/RAM) for your needs and connect the necessary networks.

### Step 4: Attaching a security group​

Attach the previously created security group and create the virtual machine.

## HA (High Availability) Requirements​

Minimum Requirements for HA Implementation:

  * At least three IPs per subnet on the pfSense network interface — one for master, one for slave, and a virtual IP for external communication
  * Layer 2 devices must support multicast
  * The upstream/ISP/router involved must have access to the virtual IP used by CARP

## Configuring the pfSense Interface​

### New Network: Adding a card​

  * Select **Assignment** from the **Interface** menu and click **Add** to add a new interface.
  * Double-click the OPT1 interface and enter the required information.
  * After setting, click **Save** then **Apply Changes**.

### Firewall: Creating rules​

  * Select **Rules** from the **Firewall** menu and switch to the **Sync** tab.
  * Click **Add** to create a new rule and enter the required information.
  * Once done, click **Save and Apply Changes**.
  * Perform the same configuration on both pfSense servers.

## Configuring CARP (High Availability Protocol)​

### Configuring CARP on the Master​

  * Select **High Availability Synchronization** from the **System** menu and enter the required information.
  * The username and password for the remote system should specify credentials of a high-privileged user on the pfSense slave VM.

### Configuring CARP on the Slave​

  * Similarly, select **High Availability Synchronization** from the **System** menu and enter the required information.
  * Settings differ from the master, so follow instructions to configure appropriately.
