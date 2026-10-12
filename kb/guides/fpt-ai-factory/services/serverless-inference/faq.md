# FAQ (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/fpt-ai-factory/services/serverless-inference/faq/

# FAQ

### Billing​

**1\. How am I billed for Serverless Inference?**

You are billed per token — input tokens and output tokens are counted separately and may have different rates. There is no base charge, no GPU reservation fee, and no cost when you are not making requests.

Billing is reflected in the **Usage & Billing** tab and deducted from your Organization Wallet.

**2\. What happens if my balance runs out mid-request?**

Requests that would exceed your remaining balance are rejected with a `402 Payment Required` response. In-flight requests that started before the balance reached zero complete normally. Top up your Wallet to resume sending requests immediately.

**3\. Where can I see token pricing for each model?**

Each model card in the **Model Catalog** shows the per-token price for input and output separately. You can also check the **Pricing** page in **Billing** — look for the **AI Inference → Serverless endpoint** tab.

* * *

### API & Integration​

**4\. Is the API compatible with the OpenAI SDK?**

Yes. The serverless gateway exposes the standard `/v1/chat/completions` endpoint. You can use the OpenAI Python SDK by setting `base_url` to the gateway URL and `api_key` to your serverless API key.
    
    
    from openai import OpenAI  
      
    client = OpenAI(  
        base_url="https://<serverless-gateway-domain>/v1",  
        api_key="<your-api-key>",  
    )  
      
    response = client.chat.completions.create(  
        model="<model-name>",  
        messages=[{"role": "user", "content": "Hello!"}],  
    )  
    print(response.choices[0].message.content)  
    

**5\. Does the API support streaming?**

Yes. Set `"stream": true` in your request body. The gateway returns Server-Sent Events (SSE). See Call the Inference API for a streaming example.

**6\. I'm getting 429 Too Many Requests. What are the rate limits?**

Rate limits apply per API key across requests per minute (RPM), tokens per minute (TPM), and concurrent requests. When a limit is exceeded, the gateway returns `429 rate_limited`. Contact support to request a higher limit.

**7\. Can I use the same API key for both Serverless and Dedicated Inference?**

No. API keys are scoped to the service they are created in. Serverless Inference API keys only work with the serverless gateway, and Dedicated Inference API keys only work with dedicated endpoint gateways.

* * *

### Models​

**8\. Which models are available?**

The **Model Catalog** tab shows all currently available models. The catalog is updated periodically — check it for the latest list.

**9\. Can I use a private or custom model?**

No. Serverless Inference only serves models from the managed catalog. To deploy a private or custom Hugging Face model, use Dedicated Inference.

**10\. What context window sizes are supported?**

Each model card in the catalog shows the maximum context window. The value varies by model — check the catalog for details.

* * *

### API Keys​

**11\. How many API keys can I create?**

There is no hard limit on the number of API keys per workspace. Create separate keys for different applications or environments to make it easy to rotate or revoke individual keys without affecting others.

**12\. Can I see which key made a specific request?**

Yes. The **Usage & Billing** tab shows the API key associated with each request in the log.
