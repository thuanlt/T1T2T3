# 6. CLAIMS & COMPENSATION PLAN (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/fpt-ai-factory/sla/claims-and-compensation/

# 6\. CLAIMS & COMPENSATION PLAN

  * In case of claims, Client please submit claim information via documents or email to **FPT Smart Cloud**. Claim information must include: (i) the title must be Claim request by SLA; (ii) Client name; (iii) specific date and time that the service is unavailable; (iv) Name of the affected resource; and (v) error log or screenshots. 
  * For claims related to **FPT AI Factory, FPT Smart Cloud** must receive the claims within 60 (sixty) days from the date of the event mentioned in the claims. Upon expiry of the aforementioned period, FPT Smart Cloud shall have no obligation to accept or process any claims. 
  * **FPT Smart Cloud** will assess all available information reasonably and make the most impartial decision. **FPT Smart Cloud** shall use commercially reasonable efforts to resolve the claims within a maximum of 45 (forty-five) days of receipt of the claim and with sufficient information required. 

## 6.1 SLA Exclusions ​

**FPT Smart Cloud** does not commit SLA and/ or Service level affected by the following factors: 

### 6.1.1 Events of force majeure ​

  * Any event of force majeure including without limitation natural disasters such as earthquake, flood and plague, social events such as war, riot and government action, technology incidents such as disconnection of telecommunication trunk circuits, hacker attack and network congestion, technological adjustment by telecommunication authorities, and government regulation and control. 

### 6.1.2 Scheduled, recurring or zero impact maintenance ​

  * Any temporary downtime of the Service due to normal maintenance or upgrade of services by **FPT AI Factory Service Agreement**. 

### 6.1.3 Security ​

  * Hacker attack on a customer’s application. 
  * Any loss or leak of data, pin or password due to improper maintenance or confidentiality measures of a customer. 
  * Denial of service attacks, virus or hacking attacks, or bugs in code, hardware, or services for which there is no commercially reasonable, known solution (even if there is a known workaround) 
  * Due to unauthorized activity or lack of necessary actions or from employees, agents, contractors, provider of Client or anyone who obtains access to **FPT Smart Cloud's network** by methods using the Client’s password or device, or through Client’s fault by revealing the password. 

### 6.1.4 Hardware & System ​

  * Any hardware failure of out-of-service physical servers that the customer has chosen not to upgrade recommended drivers or patches by **FPT**. 
  * Any hardware failure of out-of-service hard disk drives. 
  * Any single point of hardware failure in a redundant configuration that does not affect the customer’s business, including but not limited to a single NIC failure in multi-NIC bonding, a single disk failure in a disk group with storage redundancy configuration, etc. 
  * Any start-up dependence on local disk and data stored herein, which data is removed due to system failure. 

### 6.1.5 Fault of Third-party service or facility providers or Customer ​

  * Unavailability that results from Your facilities, equipment, software, or other technology and/or third-party facilities, equipment, services, software, or other technology (other than third-party equipment within **FPT Smart Cloud's direct control**). 
  * Application: Any error caused by software installed by a customer, any other third-party software or configuration not directly operated by **FPT Smart Cloud**. 
  * Telecom service & Hardware: Unavailability including any telecom, internet, or other related service or facility provider, or packet loss, network or Internet problems beyond FPT AI Factory's border router supporting **FPT AI Factory's public internet** connectivity.

### 6.1.6 Failure of Customers’ Configuration or Actions ​

  * Any failure or configuration adjustment of any network or equipment that is not **FPT Smart Cloud** facility. 
  * Any failure by a customer to abide by documentation or suggestions for using **FPT AI Factory** products, for example, shutting down, restarting, or uninstalling cloud storage of a service via FPT AI Factory Portal, API, CLI or otherwise. 

### 6.1.7 Service Agreement Violation by Customers ​

Any suspension or termination of servers resulting from any violation by a customer of the **FPT AI Factory Service Agreement** , and the suspension of service or release of a Cloud server due to a customer’s delay in payment. 

## 6.2 Remedies for failure to meet the SLA ​

If the Service fails to achieve or maintain the committed service levels as described in Section 3 of this SLA, unless otherwise specified in the Agreement, the Customer will be eligible to receive a service credit as a percentage of the monthly service fee, proportionate to the portion of the Service affected during the month in which FPT Smart Cloud failed to meet the corresponding SLA.   
The specific service credit rates are as follows: 

Service Name| SLA Achievement Level| Service Credit Rate| Metal Cloud| Below 99%| 5%| GPU Cluster – Kubernetes Control Plane| Below 99.95%| 5%| GPU Virtual machine – Ephemeral Storage NVMe| From 99% to Below 99.5%| 5%| From 95% to Below 99%| 15%| | Below 95%| 50%| | GPU Virtual machine – Block Storage| From 99% to Below 99.95%| 5%| From 95% to Below 99%| 15%| | Below 95%| 50%| | GPU Container| From 99% to Below 99.95%| 5%| From 95% to Below 99%| 15%| | Below 95%| 50%| | File Storage – High performance Tier| Below 99.9%| 5%| FPT AI Inference (Providing AI Models via APIs)| Below 99.9%| 5%| AI Notebook| Below 99.5%| 5%| AI Studio| Below 99.9%| 5%| Model Hub| Below 99.9%| 5%| Data Hub| Below 99.9%| 5%| Model Finetuning| Below 99.5%| 5%| Interactive Session| Below 99.5%| 5%| Test Jobs| Below 99.5%| 5%  
---|---|---  
  
_**The service credit: (1) will be applied to the balance of the Customer’s registered account for use with FPT AI Factory services in subsequent billing cycles; and (2) will not be refunded in cash, transferred, or applied to any other account.**_

* * *

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:
    
    
    GET https://ai-docs.fptcloud.com/service-level-agreement/6.-claims-and-compensation-plan.md?ask=<question>  
    

The question should be specific, self-contained, and written in natural language. The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
