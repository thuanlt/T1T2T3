# 3. SERVICE AVAILABILITY COMMITMENT (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/fpt-ai-factory/sla/service-availability/

# 3\. SERVICE AVAILABILITY COMMITMENT

**FPT AI Factory** will use commercially reasonable efforts to ensure that each service identified below is "Available" during a given calendar month equal to the "**Monthly Uptime Percentage** " for such **FPT AI Factory Service** as set forth in the table below.

## 3.1 Metal Cloud​

No.| Service| Monthly Uptime Percentage| Unit| 1| Metal Cloud| 99%*| Bare metal GPU server  
---|---|---|---  
  
_*** Data stored on Local NVMe Storage is excluded from the scope of this SLA.**_

_**Local NVMe Storage is provided for temporary data storage to support high-performance workloads. In the event of data has been corrupted or damaged resulting from hardware failure, FPT Smart Cloud shall have no obligation to recover, restore, or provide any form of compensation, indemnification, or remedy for the affected data.**_

  * It is determined by the following formula: 

**Monthly Uptime Percentage = (Total Time of Service Duration – Service Unavailable Duration) / Total time of month x 100%**

It being specified that: 

  * **Service Duration** : In the relevant month 
  * **Time unit** : Number of minutes 
  * “**Service Unavailable Duration** ”: refers to a period during which there is a complete loss of external connectivity to the running resource, or when the server is non-operational due to a fault caused by FPT Smart Cloud for a continuous period of at least two (2) minutes. 

Partial minutes or intermittent Downtime for a period of less than two (2) minutes will not be counted towards any of Service Unavailability. 

It excludes circumstances resulting directly or indirectly from any SLA Exclusions (as defined under Section 6.1 below). 

## 3.2 GPU Virtual machine​

No.| Service| Monthly Uptime Percentage| Unit| 1| GPU Virtual machine - Ephemeral Storage NVMe| 99.5%*| Virtual machine| 2| GPU Virtual machine – Block Storage| 99.95%| Virtual machine  
---|---|---|---  
  
_*** Data stored on Ephemeral Storage NVMe is excluded from the scope of this SLA.**_   
  
_**Ephemeral Storage NVMe is provided for temporary data storage to support high-performance workloads. In the event of data has been corrupted or damaged resulting from hardware failure, FPT Smart Cloud shall have no obligation to recover, restore, or provide any form of compensation, indemnification, or remedy for the affected data.**_

  * It is determined by the following formula: 

**Monthly Uptime Percentage = (Total Time of Service Duration – Service Unavailable Duration) / Total time of month x 100%**

It being specified that: 

  * **Service Duration:** In the relevant month 
  * **Time unit:** Number of minutes 
  * “**Service Unavailable Duration** ”: refers to a period during which there is a complete loss of external connectivity to the running resource, or when the server is non-operational due to a fault caused by FPT Smart Cloud for a continuous period of at least two (2) minutes. 

Partial minutes or intermittent Downtime for a period of less than two (2) minutes will not be counted towards any of Service Unavailability. 

It excludes circumstances resulting directly or indirectly from any SLA Exclusions (as defined under Section 6.1 below). 

## 3.3 GPU Cluster ​

No.| Service| Monthly Uptime Percentage| Unit| 1| GPU Cluster -   
Kubernetes Control Plane* | 99.95%| Cluster  
---|---|---|---  
  
* It does not apply to worker nodes. 

  * It is determined by the following formula: 

**Monthly Uptime Percentage = (Total Time of Service Duration – Service Unavailable Duration) / Total time of month x 100%**

It being specified that: 

  * **Service Duration** : In the relevant month 
  * **Time unit** : Number of minutes 
  * “**Service Unavailable Duration** ”: refers to the period during which there is a complete loss of external connectivity to the Kubernetes control plane, or the Customer is unable to access all applicable running clusters, for a continuous period of at least two (2) minutes. 

Partial minutes or intermittent Downtime for a period of less than two (2) minutes will not be counted towards any of Service Unavailability. 

It excludes circumstances resulting directly or indirectly from any SLA Exclusions (as defined under Section 6.1 below). 

## 3.4 GPU Container ​

No.| Service| Monthly Uptime Percentage| Unit| 1| GPU Container| 99.95%| Container  
---|---|---|---  
  
  * It is determined by the following formula: 

**Monthly Uptime Percentage = (Total Time of Service Duration – Service Unavailable Duration) / Total time of month x 100%**

It being specified that: 

  * **Service Duration** : In the relevant month 
  * **Time unit** : Number of minutes 
  * “**Service Unavailable Duration** ”: refers to a period during which there is a complete loss of external connectivity to Container for a continuous period of at least two (2) minutes.   
Partial minutes or intermittent Downtime for a period of less than two (2) minutes will not be counted towards any of Service Unavailability. 

It excludes circumstances resulting directly or indirectly from any SLA Exclusions (as defined under Section 6.1 below). 

## 3.5 File Storage ​

No.| Service| Monthly Uptime Percentage| Unit| 1| File Storage -   
High performance Tier | 99.9%| Mount point  
---|---|---|---  
  
  * It is determined by the following formula: 

**Monthly Uptime Percentage = (Total Time of Service Duration – Service Unavailable Duration) / Total time of month x 100%**

It being specified that: 

  * **Service Duration** : In the relevant month 
  * **Time unit** : Number of minutes 
  * “**Service Unavailable Duration** ”: refers to the period during which the service is unable to perform read/write operations due to a fault of FPT Smart Cloud, for a continuous period of at least two (2) minutes.   
Partial minutes or intermittent Downtime for a period of less than two (2) minutes will not be counted towards any of Service Unavailability. 

Downtime due to client-side errors or misconfigurations or indirectly from any SLA Exclusions (as defined under Section 6.1 below) is excluded. 

## 3.6 FPT AI Inference ​

No.| Service| Monthly Uptime Percentage| Unit| 1| FPT AI Inference   
(Providing AI Models via APIs) | 99.9%| AI Model  
---|---|---|---  
  
  * It is determined by the following formula: 

**Monthly Uptime Percentage = The average availability from each five-minute interval in the calendar month.**

  * **Availability** : The percentage of successful API requests during a five-minute interval. If no requests are made in a given five-minute interval, availability for that interval is assumed to be 100%. 
  * **Successful API Request** : Any API call that does not return a 5xx error code. Errors resulting from client-side issues, misconfigurations, or any circumstances falling under SLA Exclusions (as defined under Section 6.1 below) are excluded. 

## 3.7 AI Notebook ​

No.| Service| Monthly Uptime Percentage| Unit| 1| AI Notebook| 99.5%| AI Notebook  
---|---|---|---  
  
  * It is determined by the following formula: 

**Monthly Uptime Percentage = (Total Time of Service Duration – Service Unavailable Duration) / Total time of month x 100%**

It being specified that: 

  * **Service Duration:** In the relevant month 
  * **Time unit** : Number of minutes 
  * “**Service Unavailable Duration** ”: refers to a period during which there is a complete loss of external connectivity to AI Notebook for a continuous period of at least two (2) minutes.   
Partial minutes or intermittent Downtime for a period of less than two (2) minutes will not be counted towards any of Service Unavailability. 
  * It excludes circumstances resulting directly or indirectly from any SLA Exclusions (as defined under Section 6.1 below). 

## 3.8 AI Studio ​

No.| Service| Monthly Uptime Percentage| Unit| 1| AI Studio| 99.9%| Workspace| 2| Model Finetuning| 99.5%| Finetuning Job Service| 3| Model Hub| 99.9%| Model Registry| 4| Interactive Session| 99.5%| Session| 5| Test Jobs| 99.5%| Test Job Service| 6| Data Hub| 99.9%| Dataset Repository  
---|---|---|---  
  
  * For the services listed above, the Monthly Uptime Percentage is determined by the following formula: 

**Monthly Uptime Percentage = (Total Time of Service Duration – Service Unavailable Duration) / Total time of month x 100%**

It being specified that: 

  * **Service Duration** : In the relevant month 
  * **Time unit** : Number of minutes 
  * “**Service Unavailable Duration** ” refers to a period during which the relevant service is unavailable due to a fault of FPT Smart Cloud, for a continuous period of at least two (2) minutes. Partial minutes or intermittent Downtime for a period of less than two (2) minutes will not be counted towards any Service Unavailability. 

For this section, a service shall be deemed unavailable in the following cases: 

  * **AI Studio** : users are unable to access the AI Studio workspace, including the management console and core service functions. 
  * **Model Finetuning** : users are unable to create, submit, start, or monitor finetuning jobs. 
  * **Model Hub** : users are unable to register, store, retrieve, version, or manage models. 
  * **Interactive Session** : users are unable to access or use the interactive chat interface to test models, including sending prompts or receiving responses. 
  * **Test Jobs** : users are unable to create, submit, start, execute, or monitor model evaluation jobs using supported test suites. 
  * **Data Hub** : users are unable to store, retrieve, browse, or manage datasets. 
  * Downtime resulting directly or indirectly from client-side errors, misconfigurations, invalid inputs, unsupported configurations, customer-provided artifacts or datasets, third-party services, or any SLA Exclusions (as defined under Section 6.1 below) is excluded. 

* * *

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:
    
    
    GET https://ai-docs.fptcloud.com/service-level-agreement/3.-service-availability-commitment.md?ask=<question>  
    

The question should be specific, self-contained, and written in natural language. The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
