# Serverless Inference (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/fpt-ai-factory/services/serverless-inference/overview/

# Serverless Inference

### What is Serverless Inference?​

Serverless Inference is a managed AI API service that lets you call hosted language models instantly — no GPU allocation, no endpoint deployment, no infrastructure setup. Pick a model from the catalog, create an API key, and start calling the API.

### How does it work?​

Requests are routed to a shared GPU fleet managed by FPT AI Factory. You send a request to the serverless gateway URL with your API key and model name; the gateway handles queuing, GPU scheduling, and scaling automatically. You are billed only for the tokens you consume — input and output — with no base charge for idle time.

### Why Serverless Inference?​

  1. **Instant access** — no waiting for an endpoint to deploy. Call the API as soon as your API key is ready.
  2. **Pay per token** — billed only for what you use. No hourly GPU reservation, no cost when idle.
  3. **No ops overhead** — GPU provisioning, model loading, and scaling are fully managed.
  4. **Standard chat completions API** — compatible with any HTTP client, Python `requests`, or the OpenAI SDK; just change the base URL.
  5. **Built-in observability** — token usage and cost visible in the **Usage** tab.

### Serverless vs. Dedicated Inference​

| Serverless Inference| Dedicated Inference| **Setup**|  None — call API immediately| Deploy a private endpoint (minutes)| **Billing**|  Per input + output token| Per GPU-hour (compute) + storage| **GPU**|  Shared fleet| Reserved for your workspace only| **Latency**|  Variable (shared queue)| Consistent (no queue contention)| **Best for**|  Low-to-medium traffic, prototyping, batch jobs| Latency-sensitive production workloads  
---|---|---
