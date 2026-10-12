# 2. TERMINOLOGY (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/fpt-ai-factory/sla/terminology/

# 2\. TERMINOLOGY

FPT Smart Cloud| Means FPT Smart Cloud Company Limited; Address: 

  * Tokyo: 33F, Sumitomo Fudosan Tokyo Mita Garden Tower, 3-5-19 Mita, Minato-ku 
  * Hanoi: No. 10 Pham Van Bach, Cau Giay Ward 

| FPT AI Factory| Means the all-inclusive stack of High-Performance Infrastructure, Platform, and AI applications for end-to-end AI product lifecycle provided by **FPT Smart Cloud** on the **FPT AI Factory**.| Metal Cloud| **Metal Cloud** is a form of cloud service in which the user rents a physical server with a built-in GPU component. This bare metal server is dedicated only to you, and you'll have full access (root access) to the physical infrastructure. | GPU Virtual Machine  | Means a high-performance computing resource that functions as an isolated system with its own GPU, CPU, memory, network interface, and storage, created from a pool of hardware resources. It is also called GPU VM for an acronym. | GPU Cluster| A **GPU Cluster** with Managed Kubernetes (K8S) is divided into two (02) components: 

  * Control plane nodes provide the core Kubernetes services and orchestration of application workloads. 
  * Worker Nodes run application workloads. They can be **Bare Metal GPU** servers or **GPU Virtual machines**. 

| GPU Container| **GPU Container** delivers high-performance, isolated GPU compute environments optimized for AI workloads, eliminating the need for users to manage underlying server infrastructure. (Container-as-a-Service) | File Storage - High performance Tier| Provide a high-performance storage solution with extremely high IOPS and low latency for customers using services in the AI Infrastructure group within the **FPT AI Factory** , such as **Metal Cloud**.| FPT AI Inference| Provides AI models as APIs, allowing companies to integrate pre-trained AI models into applications, without needing to develop, train, or manage AI models.| AI Notebook| **AI Notebook** is a Jupyter lab-based development environment running on FPT’s AI Factory infrastructure. It runs in an isolated, containerized environment connected to FPT’s GPU/CPU infrastructure.| FPT AI Studio| **AI Studio** is a no-code platform for end-to-end generative AI development, covering key stages of the model lifecycle such as data processing, pretraining, fine-tuning, and model management through a centralized registry.| Model Finetuning| A service within **AI Studio** for customizing foundation models with domain-specific data to improve task performance.| Model Hub| Centralized model registry in **AI Studio** that enables teams to manage, version, and govern models across the AI lifecycle.| Model Testing > Interactive Session| An **AI Studio** service that provides a chat-based interface for rapid model testing, exploration, and validation.| Model Testing > Test Jobs| Test Jobs is a service within **AI Studio** for evaluating AI models using standard LLM and VLM benchmark suites. It automatically hosts the model and runs performance-optimized test cases, eliminating the need for manual setup and execution.| Data Hub| **Data Hub** is a service within AI Studio for storing, organizing, and managing datasets used across the AI model lifecycle.| Client (or Customer)| Means the contracting subject to use **FPT Smart Cloud's FPT AI Factory** computing service.| User| Means the registered customer and be assigned with accounts and passwords to access online service at **FPT Smart Cloud’s portals**. Users include but are not limited to: IT staff, accounting staff, finance staff, leader...| Contract| Means the **Service Contract FPT AI Factory** or the **FPT AI Factory Service Terms** and **Conditions** that are mutually agreed by **FPT Smart Cloud and Client**.| Maximum Available Minutes| Means the charged time in a month in minutes. (e.g. June has 30 days, the applicable time is 30 (days) * 24 (hours) * 60 (minutes) = 43.200 minutes.| Monthly Service Fee| Means the sum of the committed or actual usage fees applied to a billing period that Client must pay for.| Monthly Uptime Percentage| Means during a month, the service uptime percentage per month achieved by the service given in this SLA.| Planned Downtime| Means downtimes related to network, hardware, maintenance, service upgrade or at the request of state agencies. **FPT Smart Cloud** shall announce or notify the **Customer** at least two (02) days or at least 24 hours in case of emergency before carrying out the above activities.| Malware| Refers to viruses, worms, time bombs, trojans and other unprofitable or malicious code, files, programs.| Incident| Means one or more events beyond **FPT Smart Cloud's control** that cause the Downtime.| Management Portal| Means the web interface provided by **FPT Smart Cloud** , comprises: https://fptcloud.com/, https://neo.fpt.ai/ and https://marketplace.fptcloud.com/, through which Client can manage the FPT AI Factory service.| Service level| Means the performance indicator of the service set forth in this SLA that **FPT Smart Cloud** agrees to meet in providing the Services  
---|---  
  
* * *

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:
    
    
    GET https://ai-docs.fptcloud.com/service-level-agreement/2.-terminology.md?ask=<question>  
    

The question should be specific, self-contained, and written in natural language. The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
