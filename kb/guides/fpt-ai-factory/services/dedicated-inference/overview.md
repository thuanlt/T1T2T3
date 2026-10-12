# Dedicated Inference (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/fpt-ai-factory/services/dedicated-inference/overview/

# Dedicated Inference

### What is Dedicated Inference?​

Dedicated Inference is a managed service that lets you deploy open-source AI models onto private GPU endpoints dedicated to your workspace. Each endpoint runs exclusively for you — no shared queues, no noisy neighbors.

### How does it work?​

You pick a model from the **Model Catalog** , choose a size, and deploy. FPT AI Factory provisions the GPU, downloads the model weights, and starts a vLLM inference server. Once the endpoint status is **Running** , you call it with an API key using the standard chat completions API.

### Why Dedicated Inference?​

  1. **Private GPU endpoint** — your model runs on GPUs reserved only for you, delivering consistent low-latency responses.
  2. **Full model control** — choose any Hugging Face model, deployment size, and Scale to zero setting.
  3. **Standard chat completions API** — works with any HTTP client or Python `requests` library; no special SDK needed.
  4. **Capacity-first billing** — billed by GPU-hours reserved, not per token. Token usage (TOKENS IN / TOKENS OUT) is tracked for analytics only.
  5. **Built-in observability** — token usage and cost tracking on the **Usage & Billing** tab.
