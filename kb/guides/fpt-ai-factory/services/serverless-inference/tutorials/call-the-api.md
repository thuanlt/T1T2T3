# Call the Inference API (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/fpt-ai-factory/services/serverless-inference/tutorials/call-the-api/

# Call the Inference API

The serverless gateway exposes the standard `/v1/chat/completions` endpoint. Any HTTP client that supports this API format works without modification.

Before you start, you need:

  * A serverless API key — see Create an API Key
  * The gateway URL and model name from the **Model Catalog**

* * *

## Find the gateway URL and model name​

  1. In the left sidebar, click **Serverless Inference**.
  2. Click the **Model Catalog** tab.
  3. Click a model card to open its detail view.
  4. Copy the **Gateway URL** and the **Model name**.

* * *

## curl​
    
    
    curl https://<serverless-gateway-domain>/v1/chat/completions \  
      -H "Authorization: Bearer <your-api-key>" \  
      -H "Content-Type: application/json" \  
      -d '{  
        "model": "<model-name>",  
        "messages": [  
          {"role": "system", "content": "You are a helpful assistant."},  
          {"role": "user", "content": "Hello!"}  
        ],  
        "max_tokens": 256  
      }'  
    

* * *

## Python (requests)​
    
    
    import requests  
      
    response = requests.post(  
        "https://<serverless-gateway-domain>/v1/chat/completions",  
        headers={  
            "Authorization": "Bearer <your-api-key>",  
            "Content-Type": "application/json",  
        },  
        json={  
            "model": "<model-name>",  
            "messages": [  
                {"role": "system", "content": "You are a helpful assistant."},  
                {"role": "user", "content": "Hello!"},  
            ],  
            "max_tokens": 256,  
        },  
    )  
    print(response.json()["choices"][0]["message"]["content"])  
    

* * *

## OpenAI SDK (Python)​

The OpenAI SDK works directly — just set `base_url` to the serverless gateway and `api_key` to your serverless key.
    
    
    from openai import OpenAI  
      
    client = OpenAI(  
        base_url="https://<serverless-gateway-domain>/v1",  
        api_key="<your-api-key>",  
    )  
      
    response = client.chat.completions.create(  
        model="<model-name>",  
        messages=[  
            {"role": "system", "content": "You are a helpful assistant."},  
            {"role": "user", "content": "Hello!"},  
        ],  
        max_tokens=256,  
    )  
    print(response.choices[0].message.content)  
    

* * *

## Streaming​

Add `"stream": true` to receive tokens as they are generated. The gateway returns Server-Sent Events (SSE).
    
    
    from openai import OpenAI  
      
    client = OpenAI(  
        base_url="https://<serverless-gateway-domain>/v1",  
        api_key="<your-api-key>",  
    )  
      
    with client.chat.completions.stream(  
        model="<model-name>",  
        messages=[{"role": "user", "content": "Tell me a short story."}],  
        max_tokens=512,  
    ) as stream:  
        for text in stream.text_stream:  
            print(text, end="", flush=True)  
    

* * *

## Common errors​

HTTP status| Cause| Fix| `401 Unauthorized`| Invalid or missing API key| Check the `Authorization` header format: `Bearer <key>`| `402 Payment Required`| Wallet balance is zero| Top up your Wallet in **Billing**| `404 Not Found`| Model name not recognized| Check the model name against the **Model Catalog**| `429 Too Many Requests`| Rate limit exceeded| Wait and retry, or contact support for a limit increase  
---|---|---  
  
* * *

## What's next​

  * Monitor Usage & Billing — view token usage and cost per request.
