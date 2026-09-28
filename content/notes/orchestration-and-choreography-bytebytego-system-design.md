---
title: "Orchestration and choreography - ByteByteGo System Design"
date: '2022-05-24T21:57:23-03:00'
category: webclip
summary: 'The page contrasts choreography and orchestration in microservices, showing orchestration as centralized control with transaction management and easier rule changes, but also higher latency and a single point of failure.'
tags: ["microservices", "orchestration", "choreography", "system-design"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Orchestration and choreography - ByteByteGo System Design"
    url: "https://blog.bytebytego.com/p/orchestration-and-choreography?s=r"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-05/blog-bytebytego-com--orchestration-and-choreography-bytebytego-system-design.md"
    kind: repo
---

The page compares two ways microservices collaborate: choreography and orchestration. In choreography, services follow rules for exchanging messages. In orchestration, a central orchestrator invokes and combines services, describes their interactions, and handles transaction management.

## Reading notes

- Choreography is described as rule-based interaction among microservices, with services exchanging messages according to set rules.
- Orchestration places a central authority in charge of invoking and combining services.
- The orchestration pattern includes transaction management among different services.
- Orchestration is presented as more reliable because it has built-in transaction management and error handling.
- Orchestration is presented as more scalable for adding a new service, since only the orchestrator needs updated interaction rules.
- A limitation of orchestration is lower performance, because all services communicate through a centralized orchestrator.
- Another limitation is the single point of failure risk if the orchestrator goes down.
- The page mentions Netflix Conductor as a real-world microservice orchestrator.
