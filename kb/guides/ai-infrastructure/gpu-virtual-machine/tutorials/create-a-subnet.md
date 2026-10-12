# Create a Subnet (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/ai-infrastructure/gpu-virtual-machine/tutorials/create-a-subnet/

# Create a Subnet

## Overview​

A subnet represents a distinct CIDR block containing a range of IP addresses within a VPC. All resources deployed in a VPC must reside on subnets.

Key points:

  * Instances across different subnets within the same VPC can communicate by default.
  * Once created, a subnet's CIDR block is immutable. Subnets sharing a VPC must not have overlapping CIDR ranges.
  * Creating a GPU VM requires an active Subnet in the VPC. The system auto-assigns a Private IP from that subnet to the VM.

## Step-by-Step​

**Step 1:** Navigate to **Networking → Subnets** in the left-side menu, then select **Create Subnet**.

**Step 2:** Enter a name for the subnet in the Name field.

**Step 3:** Choose the subnet type. Two types are supported:

  * **Routed** : The subnet is routed to the internet via a NAT gateway.
  * **Isolated** : The subnet has no internet routing.

**Step 4:** Define the IP range using CIDR notation (e.g., 172.30.65.0/24) in the Network Address (CIDR) field.

**Step 5:** Specify the default gateway IP within the subnet via Gateway IP. Typically the first usable IP (e.g., 172.30.65.1).

**Step 6:** Define a Static IP Pool — a reserved range of IPs designated for static assignments.

**Step 7:** Configure DNS settings by specifying DNS server IPs for domain resolution:

  * **Primary DNS** : Required server for resolving domain names.
  * **Secondary DNS** (optional): Fallback server if the primary becomes unavailable.

**Step 8:** Assign a Tag to help categorize or organize the subnet.
