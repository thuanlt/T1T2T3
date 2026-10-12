# Create server (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/ai-infrastructure/metal-cloud/tutorials/create-server/

# Create server

You can deploy a Bare Metal Server through the FPT Customer Portal. FPT handles provisioning, OS installation, and configuration based on user-selected settings. After deployment, servers are accessible via SSH using a key or password.

  1. Sign in to your FPT Cloud account, select a **Tenant** , a **Region** and a **VPC** (if you have more than one of them).
  2. Navigate to **AI Infrastructure** and **Metal Cloud** in the sidebar, then click **Create server**.
  3. Pick a **Flavor** — availability varies by region.
  4. Specify the **number of servers** to deploy simultaneously (max depends on quota).
  5. Provide **server names**.
  6. Choose an **Operating System** — custom images are supported if the desired OS isn't offered.
  7. Select an available **Subnet** — required; you cannot deploy a server without a subnet.
  8. Optionally attach a **Floating IP**.
  9. For authentication, pick either an **SSH key** (existing or add new) or a **Console password**.
  10. Optionally configure **RAID**.
  11. Optionally select or create a **User Data** script — these run automatically on the server's first boot through the cloud-init process.
  12. Click **Create server**.
