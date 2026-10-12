# FPT AI Factory Portal (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/fpt-ai-factory/overview/

# FPT AI Factory Portal

FPT AI Factory Portal is a cloud platform for provisioning and managing AI/ML infrastructure and related resources within a governed, cost-visible environment.

* * *

## What the portal gives you​

  * **One Organization** — the top-level account that owns all Workspaces, Members, Billing, and Policies. Only one Organization Owner exists per Organization.
  * **A shared Wallet** — a single credit balance at the Organization level, drawn down by all Workspaces. Billing is centralized; teams don't need separate accounts.
  * **Multiple Workspaces** — isolated environments for teams or projects, each with its own Services, Quota, Policies, and Member list.
  * **Role-based access** — every Member has a Role (Owner, Admin, or Member) that defines exactly what they can see and do, across both Organization and Workspace levels.
  * **Services per Workspace** — each Workspace can run GPU Virtual Machine, Dedicated Inference, and Serverless Inference simultaneously, each independently enabled and region-scoped.

## Roles and permissions​

There are three roles in the portal. Each role has a clearly defined scope.

Action| Organization Owner| Workspace Admin| Workspace Member| Manage organization settings| ✅| —| —| Create / delete workspaces| ✅| —| —| Edit workspaces| ✅| ✅| —| Enable services per workspace| ✅| ✅| —| Set workspace quota| ✅| ✅| —| Create / manage policies| ✅| —| —| Invite / remove members| ✅| ✅| —| Full billing access (org-level)| ✅| —| —| View workspace spend| ✅| ✅| —| View audit logs| ✅ (all scopes)| ✅ (workspace only)| ✅ (workspace only)| Use enabled services| ✅| ✅| ✅| View pricing| ✅| ✅| ✅  
---|---|---|---  
  
* * *

## Glossary​

Term| Definition| **Actions**|  Operations that can be permitted or denied by a Policy statement. Actions are Service-specific (e.g. `notebook:create`, `notebook:stop`). A statement can target all actions for a Service using **All actions**.| **Audit log**|  A read-only record of all user and system events in the Organization. Organization Owners see the full log; Workspace Admins and Members see Workspace-scoped events only.| **Billing currency**|  The currency used for all payments, invoices, and credit balances in an Organization. Set once and cannot be changed afterward. Supported: VND, USD, JPY.| **Billing plans**|  Credits from an active subscription plan purchased separately through FPT. Consumed first, before Voucher and top-up credits.| **Credits**|  Prepaid balance that funds resource usage. Credits do not expire and are non-refundable. The Wallet holds three types of credits: Billing plans, Voucher, and top-up — consumed in that order.| **Dedicated Inference**|  A GPU-backed service for deploying AI models as dedicated, always-on inference endpoints with predictable latency.| **Effect**|  The outcome of a Policy statement — either **Allow** or **Deny**. Deny takes precedence over Allow when statements overlap.| **GPU flavor**|  The specific GPU hardware type and quantity available in a region. Examples: H100 SXM5 (Hà Nội), H200 SXM5 (Tokyo).| **GPU Virtual Machine**|  A full virtual machine with dedicated GPU for custom OS configurations and software stacks.| **Organization**|  The top-level account entity in the portal. An Organization has one Owner, a single Wallet, and any number of Workspaces.| **Policy**|  A named set of statements defining what actions are allowed or denied for a specific Service and region. Policies are created by the Organization Owner and attached to Workspaces.| **Policy statement**|  A single rule inside a Policy specifying a Service, region, effect (Allow or Deny), and a list of actions.| **Quota**|  A credit spending limit that can be configured at three levels: Organization (total credits across all Workspaces), Workspace (budget per Workspace, in USD per day or per month, must not exceed the org quota), and Service (budget per service within a Workspace). When a limit is reached, new resource creation is blocked until the period resets.| **Scope**|  A classification in Audit Logs grouping events by area: Organization, Billing, Workspace, or Service.| **Serverless Inference**|  A pay-per-token AI model inference service. No infrastructure to manage — select a model and start calling the API immediately.| **Service**|  A GPU-backed product available in the portal: GPU Virtual Machine, Dedicated Inference, or Serverless Inference. Each Service must be explicitly enabled per Workspace before Members can see or use it.| **Top-up**|  A direct credit purchase made through the portal. Payment methods vary by billing currency: VNPay or Stripe for VND; PayPal or Stripe for USD/JPY.| **Voucher**|  Promotional credits provided by FPT, added via a Voucher code. Vouchers expire automatically and may be scoped to a specific Service.| **Wallet**|  The Organization-level credit balance shared across all Workspaces. Holds three balance types — Billing plans, Voucher, and top-up — consumed in that order.| **Workspace**|  An isolated environment within an Organization for a team or project. Each Workspace has its own Services, Quota, Policies, and Member list.  
---|---  
  
* * *

## What's next​

  * New User to Portal — step-by-step setup from first login to your first resource.
  * Organization — manage your Organization name, quota, and workspaces.
  * Workspaces — create and configure Workspaces for your teams.
  * Policies — control what actions Members can take in each Workspace.
