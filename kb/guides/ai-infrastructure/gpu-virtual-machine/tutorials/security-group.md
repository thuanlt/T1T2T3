# Security Group (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/ai-infrastructure/gpu-virtual-machine/tutorials/security-group/

# Security Group

## Overview​

A Security Group functions as a network-based, stateful firewall service for GPU virtual machines, offered at no extra charge. It governs both inbound and outbound traffic — any traffic not explicitly allowed by a rule gets automatically blocked.

warning

The combined total of rules across all Security Groups is capped at 100. To raise this limit, contact FPT Smart Cloud support.

## The Default Security Group​

When a VPC is created, a default security group is generated automatically. It permits all outbound traffic, and its rules cannot be changed.

Default outbound rules include:

Type| Protocol| Port range| Action| IP type| Destination| Custom| UDP| 547| ALLOW| IPv6| ff02::1:2/128| HTTP| TCP| 80| ALLOW| IPv4| 169.254.169.254| Custom| UDP| 67| ALLOW| IPv4| All| HTTP| TCP| 80| ALLOW| IPv6| fe80::a9fe:a9fe/128  
---|---|---|---|---|---  
  
## Create a Security Group​

  1. Navigate via the left-side menu to **Networking → Security Group** , then select **Create Security Group**.

  2. Fill in the required fields on the creation form:

     * **Name** : Provide a name; a default name is auto-generated for quick setup.
     * **Applied Instances** : Pick the GPU VM to associate with the group.
     * **Add Tags** : Optional field for organizing resources.
     * **Configure security rules** : Adjust inbound and outbound rules as needed.
  3. Confirm by clicking **Create Security Group**. The new group will then appear in the list.

## Manage Rules​

A single Security Group can hold multiple inbound and outbound rules.

### Inbound Rules​

These control incoming traffic to the instance. They specify which **ports** are open and which **IP addresses** from the internet may reach them (the **Source**).

### Outbound Rules​

These control outgoing traffic from the instance. They specify which **ports** can send traffic out and to which **destination addresses**.

### Adding or Editing Rules​

  1. On the Security Group Management page, select the desired group to open its details.

  2. Under **Inbound Rules** or **Outbound Rules** , click **Add New**.

  3. Fill in the rule details:

     * **Port** : Choose which port(s) to open.

       * **All Ports** opens every port.
       * **Customize Ports** lets you specify individual ports or ranges.
       * Quick options exist for common services: SSH (22), RDP (3389), MySQL (3306), HTTP (80), and HTTPS (443).
     * **Sources / Destinations** : Specify permitted IP addresses.

       * **All IPv4** : Permits connections from any IP.
       * **My IP** : Restricts access to your current public IP.
       * **Custom** : Enter specific IP address(es).

warning

For sensitive ports like 22 (SSH) or 3389 (RDP), allowing All IPv4 triggers a warning: "We recommend allowing SSH from trusted IPs only."

     * **Description** : Optional notes about the rule.

Click **Add Rule** to keep adding, or **Edit Security Group** to save changes. The system processes the configuration and shows a result notification.

tip

Add an inbound rule for SSH (Type: SSH, Port: 22, Source: All IPv4), but for better security, allow only trusted IP addresses and avoid using 'All IPv4' (0.0.0.0/0).

## Attach a GPU VM​

  1. On the Security Group Management page, select the group you want to attach to a VM.

  2. In the **Apply To** section, choose the VMs to attach. You can also define a **CIDR range** to apply the group to a network segment. Click **Apply Instances** to confirm. The system processes and displays the result.

## Detach a GPU VM​

  1. On the Security Group Management page, select the group currently attached to the VM.

  2. In the **Apply To** section, find the instance to remove. Click the **X icon** beside it, then click **Apply Instances** to confirm. The system processes and shows the result.

## Delete a Security Group​

When a Security Group is no longer needed, it can be deleted from the VPC.

note

All rules must be deleted first before the Security Group itself can be removed.

  1. On the Security Group Management page, select the group to delete and open its details.

  2. Remove each rule by clicking the **trash icon** next to it and confirming deletion.

  3. After all rules are gone, return to the Security Group list. Under the **Actions** column, pick **Delete** for the target group.

  4. A confirmation dialog appears. Click **Delete Security Group** to confirm. The system processes and displays the result.
