# FAQ (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/fpt-ai-factory/services/dedicated-inference/faq/

# FAQ

### Billing​

**1\. How am I billed for Dedicated Inference?**

Billing has two components billed independently:

Component| When charged| **Compute (GPU)**|  Only while the endpoint is in **Running** state| **Storage**|  At all times until the endpoint is **deleted**  
---|---  
  
Compute billing is per-minute with a minimum of 60 seconds, rounded up. Token usage (TOKENS IN / TOKENS OUT) is tracked for analytics only and is not billed.

**2\. Do storage fees apply when my endpoint is paused (Stopped)?**

Yes. When you stop an endpoint, GPU charges stop immediately, but **storage fees continue**. The model weights remain on the attached NVMe disk while the endpoint is Stopped, so the storage reservation is still active.

Storage fees stop only when you **delete** the endpoint. The endpoint lifecycle is: **Creating → Running → Stopped → Deleted**.

**3\. What happens if my balance runs out?**

Behavior depends on the endpoint type:

Endpoint type| When balance reaches zero| Supports scale-to-zero| 30-second grace period to drain in-flight requests, then replicas scale to 0| Always-on| New requests are rejected with `402`, in-flight requests complete normally  
---|---  
  
Top up your balance to resume immediately. Storage fees continue to accrue while the endpoint is in Stopped state.

warning

If the balance remains severely negative for an extended period, a hard stop may be applied — all traffic is rejected immediately including in-flight requests. Resuming requires a manual operation and account top-up.

**4\. Can I set a spending limit?**

Yes. Go to **My endpoints → Usage & Billing** and click **Set budget alert** to configure a monthly spend threshold notification.

* * *

### Endpoints​

**5\. How long does it take for an endpoint to start?**

Startup time depends on the model size. For example, a 7B model (e.g. Mistral 7B) typically starts in about 3 minutes. Larger models take longer.

**6\. Can I change the GPU type or model after creating an endpoint?**

No. GPU type and model cannot be changed on an existing endpoint. To use a different GPU or model, delete the endpoint and create a new one.

The available endpoint actions are: **start, stop, scale, redeploy, delete**. There is no in-place update or change-config action.

**7\. What does the Deploying status mean?**

The endpoint is being provisioned. GPU is being allocated and model weights are being downloaded. Click the endpoint name to open the detail page and check the deployment logs for progress.

**8\. Can I run multiple models on one endpoint?**

No. Each endpoint serves exactly one model. To serve multiple models simultaneously, create a separate endpoint for each.

* * *

### API Keys​

**9\. Where can I create API keys?**

Go to **Dedicated Inference → API keys** to create and copy your keys. See Create and Manage API Keys for step-by-step instructions.

* * *

### API & Integration​

**10\. Can I use a standard HTTP client or Python library to call the API?**

Yes. The endpoint exposes the standard chat completions API. You will find the gateway URL on the endpoint detail page after it reaches **Running** status.

**11\. I'm getting 429 Too Many Requests. What are the rate limits?**

Rate limits are enforced across three dimensions: requests per minute (RPM), tokens per minute (TPM), and concurrent requests. When a limit is exceeded, the gateway returns `429 rate_limited`. Contact support to request a limit increase.

**12\. Can I use the endpoint for streaming responses?**

Yes. Set `"stream": true` in your request body. The API returns Server-Sent Events (SSE). See Call the Inference API for a streaming code example.
