# Browse the Model Catalog (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/fpt-ai-factory/services/serverless-inference/tutorials/browse-model-catalog/

# Browse the Model Catalog

The Model Catalog lists every model available through Serverless Inference. Use it to find the right model and note its name for your API requests.

* * *

## Open the Model Catalog​

In the left sidebar under **Serverless Inference** , click **Models**.

* * *

## Read a model card​

Each card in the catalog shows:

Field| Description| **Model name**|  The name to pass as the `model` parameter in API requests| **Provider**|  The organization that published the model (e.g. Meta, Mistral AI, Google)| **Context window**|  Maximum number of tokens the model can process in a single request (input + output combined)| **Input price**|  Cost per 1 million input (prompt) tokens| **Output price**|  Cost per 1 million output (completion) tokens  
---|---  
  
* * *

## Filter and search​

Use the search bar above the catalog to filter by model name or provider. Click a model card to open its detail view with the full model description and gateway URL.

* * *

## What's next​

  * Create an API Key — generate a key to authenticate your requests.
  * Call the Inference API — make your first API call with the model you chose.
