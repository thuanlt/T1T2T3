# Network ACL (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/ai-infrastructure/metal-cloud/tutorials/network-acl/

# Network ACL

Network ACL (Access Control List) or NACL is a crucial part of network security. It helps control and manage traffic flow in and out of subnets by applying rules that either allow or deny access.

  * A network ACL is automatically created with a subnet.
  * Each subnet must be associated with a NACL.
  * NACLs contain inbound and outbound rules. Priority values are evaluated in ascending order, and once a match is found, further rules are not evaluated.
  * **Each NACL has a maximum limit of 100 rules (both inbound & outbound rules).**

## A Network ACL rules​

You can modify the default network ACL by adding or removing rules. Any changes made to the rules of a network ACL are automatically applied to the associated subnets.

The components of a network ACL rule include:

Components| Description| **Priority**|  Rules are processed in ascending order by priority number. Once a rule matches, it is applied even if higher-numbered priority rules conflict. The system auto-increments the priority number, but users can change it as long as it doesn't duplicate an existing number.| **Type**|  Specifies the type of traffic, such as HTTP, HTTPS, or ALL.| **Protocol**|  NACL supports TCP, UDP, ICMP, or any protocols.| **Port**|  The specific port of the traffic is targeted from 1 to 65535.| **Source**|  For inbound rules, this specifies the origin of the traffic (CIDR range)| **Destination**|  For outbound rules, this specifies the target of the traffic (CIDR range)| **Traffic action**|  The specified traffic is permitted with Allow or Deny  
---|---  
  
### Notices​

  * The default rule is automatically created with a NACL that allows all outbound traffic, and you can delete it.

Priority| Type| Protocol| Port| Source| Traffic Action| 100| ALL| ALL| ALL| 0.0.0.0/0| ALLOW  
---|---|---|---|---|---  
  
  * If you delete the above default rule, you need to add the following outbound rules to create and deploy the server:

Priority| Type| Protocol| Port| Source| Traffic Action| 1| HTTP| TCP| 80| 0.0.0.0/0| ALLOW| 2| HTTPS| TCP| 443| 0.0.0.0/0| ALLOW| 3| DNS (UDP)| UDP| 53| 0.0.0.0/0| ALLOW  
---|---|---|---|---|---  
  
## What you can do with a Network ACL​

### Create new rules​

Creating an additional Network ACL allows (ALLOW) or denies (DENY) all or specific types of inbound and outbound traffic.

To create one or more Network ACL rules, follow these steps:

  1. Sign in to your FPT Cloud account, select a **Tenant** , a **Region** and a **VPC;** (If you have more than one of them)
  2. Navigate to **AI Infrastructure** /**Network ACL** in the sidebar;
  3. Choose a network ACL by clicking a **NACL name** or **Actions/Manage rules** in the list;
  4. Choose an **Outbound or Inbound Tab;** (if user want to create the corresponding traffic rule)
  5. Click the button **Create new rule;**
  6. Enter the Priority, Type, Protocol, Port, Source/Destination, and Traffic Action fields;
  7. You can create multiple new rules and choose **Apply** to save changes.

### Modify existing rules​

To modify one or more Network ACL rules, follow these steps:

  * Choose a network ACL by clicking a **NACL name** or **Actions/Manage rules** in the list;
  * Click on the **Edit** icon in the rule you want to modify;
  * Change the rule value to your desire;
  * You can repeat and modify multiple existing rules and choose **Apply** to save changes.

### Remove rules​

To remove one or more Network ACL rules, follow these steps:

  * Choose a network ACL by clicking a **NACL name** or **Actions/Manage rules** in the list;
  * Click on the **Delete** icon in the rule you want to remove;
  * You can repeat and delete multiple existing rules and choose **Apply** to save changes.
