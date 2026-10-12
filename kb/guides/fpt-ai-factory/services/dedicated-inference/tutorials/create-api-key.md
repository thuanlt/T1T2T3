# Create and Manage API Keys (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/fpt-ai-factory/services/dedicated-inference/tutorials/create-api-key/

# Create and Manage API Keys  
  
## Open the API Keys Tab​

In the **Dedicated Inference** page, click the **API keys** tab.

The table shows all API keys in the workspace. For each key you can see:

Column| Description| **Name**|  Friendly name and creation date| **Key**|  Masked key value (`fpt_•••••••••••xxxx`). Click the copy icon to copy the full key| **User**|  The user who created the key| **Tokens (MTD)**|  Tokens consumed in the current calendar month| **Last used**|  Timestamp of the most recent API call authenticated with this key| **Expiration**|  Expiry date, **Never** , or **EXPIRED** (shown in red)  
---|---  
  
## Create an API Key​

  1. Click **\+ Create new key** in the top-right corner.

  2. In the **Create an API Key** dialog, enter a descriptive **Name** for the key (for example, `production-app`).

  3. If you want the key to expire automatically, leave **Set expiration date** checked and pick a date and time in the **Expiration** field. To create a key that never expires, uncheck **Set expiration date**.

  4. Click **Generate Key**.

warning

The key is displayed **only once** immediately after generation. Copy it and store it somewhere safe before closing the dialog. You cannot retrieve the key value again.

## Use the Key in API Calls​

Pass the key as a Bearer token in the `Authorization` header of every request to your dedicated endpoint:
    
    
    curl https://<your-endpoint-url>/v1/chat/completions \  
      -H "Authorization: Bearer fpt_<your-key>" \  
      -H "Content-Type: application/json" \  
      -d '{  
        "model": "<model-name>",  
        "messages": [{"role": "user", "content": "Hello"}]  
      }'  
    

## Delete an API Key​

Click the **trash** icon in the **Actions** column next to the key you want to remove. Deletion is immediate and cannot be undone. Any application still using that key will receive `401 Unauthorized` errors.
