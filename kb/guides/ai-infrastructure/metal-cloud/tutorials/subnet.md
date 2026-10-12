# Create a subnet (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/ai-infrastructure/metal-cloud/tutorials/subnet/

# Create a subnet

A subnet is a range of IP addresses in a cloud network. Addresses from this range will be assigned to one or multiple servers in the Metal Cloud. Only IPv4 is supported.

_A CIDR range is allocated automatically. It will be held for 60 seconds and be updated to the new one after that on the screen. A network ACL is required when creating a subnet. By default, only outbound traffic from the Bare Metal GPU server to the internet will be allowed. The quota of subnet is equal to the quota of the Bare Metal GPU server._

  1. Sign in to your FPT Cloud account, select a **Tenant** , a **Region** and a **VPC.** (If you have more than one of them.)
  2. Navigate to **AI Infrastructure** and **Subnet for Metal Cloud** in the sidebar, then click **Create subnet**
  3. Enter a **Subnet name**
  4. Enter a **Network ACL name**
  5. Enter the **Network ACL description** (Optional)
  6. Click **Create Subnet**

## Delete a subnet​

_You cannot delete a subnet that is associated with other resources._

  1. Navigate to **AI Infrastructure** and **Subnet for Metal Cloud** in the sidebar to view the Server list
  2. Choose a subnet and click **Actions**
  3. Click **Delete**
  4. Confirm the deletion by typing **DELETE** text

## Update a subnet name​

_A subnet name**can be duplicated** with existing names._

  1. Choose a subnet and click **Actions**
  2. Click **Rename**
  3. Enter the new subnet name that complies with the rule: Name limits up to 32 characters, and only letters, numbers, and dashes are allowed
  4. Click **Rename subnet**

## Update a subnet description​

  1. Choose a subnet and click **Actions**
  2. Click **Update description**
  3. Enter the new description. The length must be less than or equal to 63 characters long
  4. Click **Save**
