# Server actions (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/ai-infrastructure/metal-cloud/tutorials/server-actions/

# Server actions

## Attach a Floating IP​

  1. Go to **AI Infrastructure** → **Metal Cloud** in the sidebar to see the Server list
  2. Select a server, then click the **Actions** icon > **Attach Floating IP**
  3. Pick the **Bare metal GPU server** option under **Resources**
  4. Choose an available reserved IP, or select **Allocate new from pool** to get a new one (subject to quota)

## Power on & Power off a server​

  1. Go to **AI Infrastructure** → **Metal Cloud** in the sidebar to see the Server list
  2. Select a server and click **Actions**
  3. Click **Power off** for a running server or **Power on** for a stopped one
  4. Confirm the action

## Delete a server​

_Deleting a server permanently erases all data on its disks and**cannot be undone**. Ensure you are deleting correctly._

  1. Go to **AI Infrastructure** → **Metal Cloud** in the sidebar to see the Server list
  2. Select a server and click **Actions**
  3. Click **Delete**
  4. Confirm by typing **DELETE**

## Update name​

_A server name is**unique** and **cannot be duplicated** with existing names._

  1. Go to **AI Infrastructure** → **Metal Cloud** in the sidebar to see the Server list
  2. Select a server and click **Actions**
  3. Click **Rename**
  4. Enter a new name following the rule: up to 63 characters, only letters, numbers, and dashes allowed
  5. Click **Rename server**
