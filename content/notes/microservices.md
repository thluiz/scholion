---
title: "Microservices"
date: '2015-04-10T22:29:22-03:00'
category: webclip
summary: 'The article defines microservices as a way to build an application from small, independently deployable services and explains why this can reduce monolith pain through clearer boundaries, automation, and decentralized decisions.'
tags: ["application-architecture", "web-services", "microservices"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Microservices"
    url: "http://martinfowler.com/articles/microservices.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-04/martinfowler-com--microservices.md"
    kind: repo
---

Microservices are presented as a style for building a single application as a suite of small services, each running in its own process and communicating with lightweight mechanisms, often HTTP APIs. The article contrasts this with the monolithic style and says the appeal comes from independent deployment, clearer service boundaries, and the ability to let different services use different languages and storage technologies.

The article groups the main characteristics of the style around services organized by business capability, product ownership instead of project handoff, smart endpoints with dumb pipes, decentralized governance, decentralized data management, infrastructure automation, failure tolerance, and evolutionary design. It also warns that microservices add complexity in communication, coordination, and monitoring, so the case for them is cautious rather than absolute.

## Reading notes

- A microservice system is a single application split into small services that run in separate processes and communicate through lightweight mechanisms.
- The main contrast is with a monolith, where the whole server-side application must be rebuilt and redeployed for any change.
- Microservices are attractive because services are independently deployable, independently scalable, and can form firm module boundaries.
- The article describes a component as independently replaceable and upgradeable, and treats services as the primary way to componentize software.
- Services make interfaces more explicit than libraries, but remote calls are more expensive and harder to change.
- The preferred split is by business capability, not by technical layer such as UI, server logic, or database.
- Teams should be cross-functional and aligned with service boundaries.
- The term microservice does not imply a fixed size, but the article mentions team-sized services as a common range.
- The model favors product ownership over project handoff, with teams staying responsible for software in production.
- Communication should use smart endpoints and dumb pipes, usually HTTP resource APIs or lightweight messaging.
- The article prefers simple protocols over complex orchestration or ESB-centric integration.
- Governance should be decentralized, with teams choosing the right tools and sharing useful, battle-tested code.
- Service contracts matter, but the article favors tolerant readers and consumer-driven contracts over heavy central contract management.
- Data management should also be decentralized, with each service managing its own data store when appropriate.
- The article notes that distributed transactions are hard and that microservices often accept eventual consistency and compensating actions.
- Infrastructure automation and continuous delivery are treated as important enablers.
- Automated tests and automated deployment are presented as core practices.
- Services must be designed for failure, with monitoring, logging, and resilience built in.
- The article warns that synchronous service calls can multiply downtime across a system.
- Microservice practitioners are described as using evolutionary design, splitting components so they can be replaced or scrapped independently.
- The article concludes with cautious optimism, saying microservices may be worthwhile but their long-term consequences are not yet fully known.
