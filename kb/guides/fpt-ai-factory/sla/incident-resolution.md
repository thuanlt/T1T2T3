# 5. INCIDENT RESOLUTION (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/fpt-ai-factory/sla/incident-resolution/

# 5\. INCIDENT RESOLUTION

The incident resolution responds to an unplanned service interruption. Unexpected disruptions occur due to incidents like loss or degradation of network connectivity, a scheduled task (like a backup task) not being performed, etc. 

## 5.1 Incident priority levels ​

No.| Priority| Business impact| Example| 1| P1-Critical| A serious impact on business and operations that cause system disruption. Serious security vulnerabilities, data loss/intrusion, malware infection incidents. | Downtime, Power-related issues, a GPU server is broken need to replace.  | 2| P2-High| High priority issues that degrade the quality of business/ operations and systems but do not cause disruption. High-level security vulnerabilities that need to be fixed quickly. | Slow system operations, Interface errors System load increased abnormally at some point | 3| P3-Medium| Non-critical issues. Technical support requests, system resource additions, recovery requests, service feature requests. Issues that do not cause disruption, do not affect revenue, brand, customer experience, or service quality. | OS reinstalls, System upgrades, etc.  
---|---|---|---  
  
## 5.2 Incident response time ​

No.| Channel| Priority| First response (Within)| Periodic Updates (After)| 1|  Ticket | P1-Critical| 15 minutes| 1 hour| 2| P2-High| 30 minutes| 2 hours| | 3| P3-Medium| 1 hour| 4 hours|   
---|---|---|---|---  
  
_*** Periodic update is executed when the incident is not resolved.**_

## 5.3 Hardware failure response ​

  * In the event of hardware failures affecting **Metal Cloud** and **GPU Virtual Machines** (Ephemeral NVMe Storage) services, FPT Smart Cloud will provision replacement resources with equivalent configurations within two (02) hours. 
  * This timeframe shall be calculated from the moment the customer confirms acceptance of the replacement solution and does not include any customer-side verification or testing time following the replacement. 
  * Data on the failed servers is not recoverable. 

## 5.4 Contact channels to receive and resolve incidents, service requests ​

Support and Operations teams work 24 hours a day, 7 days a week, ensuring that all incidents and requests from customers are answered on time. 

  * Hotline: 1800 6139 (For the call from Vietnam); +81-800-300-9739 (For the call from Japan) 
  * Email: support@fptcloud.com (Vietnam); support@fptcloud.jp (Japan) 
  * Helpdesk (Ticket support): support.fptcloud.com (Vietnam); support.fptcloud.jp (Japan) 

* * *

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:
    
    
    GET https://ai-docs.fptcloud.com/service-level-agreement/5.-incident-resolution.md?ask=<question>  
    

The question should be specific, self-contained, and written in natural language. The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
