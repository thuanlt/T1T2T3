# Security Group (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/fpt-ai-factory/services/gpu-vm/tutorials/security-group/

# Security Group

### Overview​

A **Security Group** is a **network-based, stateful firewall service** for GPU virtual machines. It is provided **at no additional cost**.Security Groups control both inbound and outbound traffic — any traffic **not explicitly allowed** by a rule is **automatically blocked**.

### The default security group​

A default security group is automatically created with your account. It permits all inbound and outbound network traffic by default. You can modify the rules of this security group, but it cannot be deleted.

The following rules are added by default:

  * **Inbound**

Type| Protocol| Port range| Action| IP type| Inbound| All Traffic| All| All| ALLOW| IPv4| All  
---|---|---|---|---|---  
  
  * **Outbound**

Type| Protocol| Port range| Action| IP type| Destination| All Traffic| All| All| ALLOW| IPv4| All| All Traffic| All| All| ALLOW| IPv6| All  
---|---|---|---|---|---  
  
### Create a Security Group​

**Step 1** : On the Security Group creation page ( **AI Infrastructure** → **GPU Virtual machines** → **Security group Tab** **→** **Create Security Group),** set the configuration

**Step 2** : Enter the required information in the **Create security group:**

  * **Name** : Enter a name for the Security Group.
  * **Applied Instances** : Select the GPU VM name to associate it with the Security Group.
  * **Configure security rules** : Update Inbound and Outbound rules

**Step 3** : Confirm by clicking "**Create Security Group** ". The newly created Security Group will appear in the list.

### Manage rules​

A single Security Group can contain multiple Inbound and Outbound rules.

  1. **Inbound Rules:**

  * Control incoming traffic to the instance.
  * Define which **ports** on the instance are open and which **IP addresses** from the internet can access them (**Source**).

  2. **Outbound Rules:**

  * Control outgoing traffic from the instance.
  * Define which **ports** on the instance can send traffic out and to which **destination addresses**.

**Adding or Editing Rules**

**Step 1** : In the **Security Group list** page, select the Security Group you want to manage to open its details page, or click **Edit**.

**Step 2** : In the **Inbound Rules** or **Outbound Rules** section, click **Add rule**.

**Step 3** : Fill in the rule information:

  * **Port:** Select the port(s) to open. 
    * Choose **All Ports** to open all ports.
    * Choose **Customize Ports** to specify one or a range of ports.
    * The system provides quick options for common services like **SSH (22)** , **RDP (3389)** , **MySQL (3306)** , **HTTP (80)** , and **HTTPS (443)**.
  * **Sources / Destinations:** Enter the IP addresses allowed to connect to the specified ports. 
    * **All IPv4:** Allow connections from all IPs.
    * **My IP:** Allow only your current public IP.
    * **Custom:** Enter one or more specific IP addresses.

⚠️ For sensitive ports like 22 (SSH) or 3389 (RDP), the system will display a warning if you allow All IPv4. We recommend allowing SSH from trusted IPs only.  
---  
  
  * **Description:** Optional notes for the rule.

Click **Add Rule** to continue adding more, or **Edit Security Group** to save your changes.The system will process the configuration and display a result notification.

### Attach a GPU VM​

**Step 1:** In the **Security Group list** page, select the Security Group you want to attach to a virtual machine.

**Step 2** : In the **Apply To** section, select the virtual machines to attach.You can also specify a **CIDR range** to apply the Security Group to a network segment, click **Apply Instances** to confirm.

### Detach a GPU VM​

**Step 1** : In the **Security Group List** page, select the Security Group currently attached to the virtual machine.

**Step 2** : In the **Apply To** section, locate the instance you want to remove. Click the **X icon** next to it, then click **Apply Instances** to confirm.

### Delete a Security group​

If you no longer need a Security Group, you can delete it from the VPC.

**Step 1** : In the **Security Group List** page, select the Security Group you want to delete.

**Step 2** : Under the **Actions** column, select **Delete** for the Security Group you want to remove.

**Step 3** : A confirmation pop-up will appear, click **Delete Security Group** to confirm.
