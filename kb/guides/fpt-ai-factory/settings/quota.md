# Quotas (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/fpt-ai-factory/settings/quota/

# Quotas

Quotas let you cap how much credit is spent across your Organization, within each Workspace, and per Service. This page explains how quotas relate to each other and what to do when quota conflicts arise.

Organization-level quotas are configured in **Settings → Organization** (accessible via **Go to Organization** in the sidebar). Workspace-level quotas are configured in **Settings → Workspaces → Edit Workspace**.

* * *

## Core concepts​

### Quota hierarchy​

Quotas follow a strict hierarchy — a child quota can never exceed its parent:
    
    
    Organization quota  
    └── Workspace quota  (must be ≤ org quota)  
        └── Service quota  (must be ≤ workspace quota and ≤ org quota)  
    

**Example:**

  * Org quota: $1,000/month
  * Workspace A quota: $400/month (valid, ≤ $1,000)
  * Service quota in Workspace A: $100/month (valid, ≤ $400)

### Period compatibility​

Each quota has a period — **Daily** or **Monthly**. The period at a parent level constrains what child levels can use:

Org period| Workspace period allowed| Service period allowed| Monthly| Monthly or Daily| Monthly or Daily| Daily| Daily only| Daily only| No quota| Monthly or Daily| Monthly or Daily  
---|---|---  
  
**Key rule:** A child level can never have a longer period than its parent. If the org quota is Daily, all workspaces and services must be Daily.

* * *

## When conflicts happen​

When you save a quota that violates the hierarchy or period rules, the portal shows a **Quota conflict detected** modal. The modal explains the conflict and which quotas are affected so you know what to adjust.

### Conflict types​

Scenario| What happens| Example| **Child exceeds parent**|  You try to set a child quota higher than its parent| Set Workspace quota to $500/month when Org quota is $400/month| **Period mismatch**|  You try to set a child period longer than parent| Set Workspace to Monthly when Org quota is Daily| **Parent decreased**|  You lower a parent quota below existing child quotas| Lower Org quota from $1,000 to $300, but Workspace A already has $400 quota| **Parent period changed**|  You change parent period to a shorter one| Change Org from Monthly to Daily, but Workspace B is set to Monthly  
---|---|---  
  
### How to resolve​

When a conflict modal appears, you have two options:

  1. **Adjust the conflicting quotas** — Lower child quotas or change their periods to match the parent, then save again.
  2. **Cancel the change** — Close the modal and keep the current quota settings.

### Examples​

**Example 1: Child exceeds parent (value)**

You're setting Workspace A quota to $800/month, but the Org quota is only $700/month.

> **Quota conflict detected**
> 
> Workspace quota ($800/month) exceeds Organization quota ($700/month).
> 
> **Action:** Lower the Workspace quota to ≤ $700/month, or increase the Organization quota first.

**Example 2: Period mismatch**

You're setting Workspace B to Monthly, but the Org quota is Daily.

> **Quota conflict detected**
> 
> Workspace period (Monthly) cannot be longer than Organization period (Daily).
> 
> **Action:** Change Workspace quota period to Daily.

**Example 3: Parent decreased (affects children)**

You're lowering the Org quota from $1,000/month to $300/month, but existing workspaces already have higher quotas.

> **Quota conflict detected**
> 
> **Conflicts with children:**
> 
> Workspace A — $400/month (exceeds new org limit)  
>  Workspace C — $350/month (exceeds new org limit)  
>  Service X in Workspace B — $320/month (exceeds new org limit)
> 
> **Action:** Lower the conflicting child quotas first, then save the organization quota again.

* * *

## Advanced: All valid combinations​

The table below is a complete reference showing all 25 possible period combinations and their validation rules. Use this when setting up complex multi-level quotas.

Org| Workspace| Service| Rule| Valid?| Monthly| Monthly| Monthly| Service ≤ WS ≤ Org (all monthly)| ✅| Monthly| Monthly| Daily| Service daily ≤ WS monthly ÷ 30; WS ≤ Org| ✅| Monthly| Monthly| No limit| WS ≤ Org; Service uncapped but blocked at runtime by WS and Org| ✅| Monthly| Daily| Monthly| ❌ Service monthly violates WS daily period| ❌| Monthly| Daily| Daily| Service daily ≤ WS daily; WS daily ≤ Org monthly ÷ 30| ✅| Monthly| Daily| No limit| WS daily ≤ Org monthly ÷ 30; Service blocked at runtime| ✅| Monthly| No limit| Monthly| Service monthly ≤ Org monthly; WS uncapped but blocked at runtime| ✅| Monthly| No limit| Daily| Service daily ≤ Org monthly ÷ 30| ✅| Monthly| No limit| No limit| All uncapped; blocked at runtime by Org| ✅| Daily| Monthly| —| ❌ WS monthly violates Org daily period| ❌| Daily| Daily| Monthly| ❌ Service monthly violates WS daily period| ❌| Daily| Daily| Daily| Service daily ≤ WS daily ≤ Org daily| ✅| Daily| Daily| No limit| WS daily ≤ Org daily; Service blocked at runtime| ✅| Daily| No limit| Monthly| ❌ Service monthly violates Org daily period| ❌| Daily| No limit| Daily| Service daily ≤ Org daily; WS blocked at runtime| ✅| Daily| No limit| No limit| All uncapped; blocked at runtime by Org| ✅| No limit| Monthly| Monthly| Service monthly ≤ WS monthly| ✅| No limit| Monthly| Daily| Service daily ≤ WS monthly ÷ 30| ✅| No limit| Monthly| No limit| Service uncapped but blocked at runtime by WS| ✅| No limit| Daily| Monthly| ❌ Service monthly violates WS daily period| ❌| No limit| Daily| Daily| Service daily ≤ WS daily| ✅| No limit| Daily| No limit| Service uncapped but blocked at runtime by WS| ✅| No limit| No limit| Monthly| No validation — Service quota is free| ✅| No limit| No limit| Daily| No validation — Service quota is free| ✅| No limit| No limit| No limit| No validation — fully uncapped| ✅  
---|---|---|---|---  
  
note

"No limit" means no spending cap is enforced at save time, but spending is still bounded at runtime by any parent quota that is set.

* * *

## What's next​

  * Organization — set the organization-level budget quota.
  * Workspaces — set workspace-level quotas and per-service quotas.
  * Understanding billing — how credits are consumed and how the Wallet works.
