---
title: "Monolith Decomposition Strategies"
date: '2023-12-04T10:03:58+00:00'
category: webclip
summary: 'Explains three types of monoliths and shows two approaches to decompose them into smaller services: the Strangler Fig pattern and branch by abstraction, with DDD as a supporting technique.'
tags: ["software-architecture", "monolith", "microservices"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Thread by @milan_milanovic: 𝗠𝗼𝗻𝗼𝗹𝗶𝘁𝗵 𝗗𝗲𝗰𝗼𝗺𝗽𝗼𝘀𝗶𝘁𝗶𝗼𝗻 𝗦𝘁𝗿𝗮𝘁𝗲𝗴𝗶𝗲𝘀 We have three types of monoliths. In 𝘁𝗿𝗮𝗱𝗶𝘁𝗶𝗼𝗻𝗮𝗹 ones, w…"
    url: "https://x.com/milan_milanovic/status/1731263367854047301"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2023-12/x-com--monolith-decomposition-strategies-milan-milanovic.md"
    kind: repo
---

The thread describes three types of monoliths and how to break them down. Traditional monoliths bundle everything in layered form. Modular monoliths define functional boundaries and dependencies but still deploy as a single unit. Distributed monoliths are built like monoliths and deployed like microservices, combining tight coupling with microservice complexity, often as a result of designing microservice architecture incorrectly.

To address this, the author presents monolith decomposition strategies. The Strangler Fig pattern introduces a façade that intercepts requests and routes them either to the monolith or to new services, so functionality can be migrated gradually while consumers keep calling the façade. Domain-Driven Design can support this by establishing a ubiquitous language, identifying relevant modules and domain models, and then defining bounded contexts. Another option is branch by abstraction, where an abstraction layer is placed over an original component so it can be replaced stepwise. Client calls go through this layer while two implementations can coexist, aligning with the Liskov substitution principle. The author notes that branch by abstraction focuses more on components than systems and recommends Sam Newman’s book "Monolith to Microservices" for further reading.

## Reading notes

- Defines three monolith types: traditional (all bundled in layered form), modular (functional boundaries and dependencies defined but single deployment), and distributed (built as monoliths, deployed like microservices).
- States that distributed monoliths combine tightly coupled services with microservice complexity and often result from incorrectly developing microservice architectures.
- Argues that fixing such systems requires some form of monolith decomposition using specific approaches.
- Describes the Strangler Fig pattern, inspired by plants that grow by strangling hosts, allowing targeted functionality replacement with new services.
- Explains that the Strangler Fig approach uses a façade to intercept requests and route them either to the monolith or to new services while functionality is gradually migrated.
- Notes that consumers always interact with the façade while old functionality moves into new services.
- Suggests using Domain-Driven Design to incrementally refactor into smaller services by defining a ubiquitous language shared by stakeholders.
- Adds that DDD involves identifying modules that use this vocabulary and defining domain models of the monolithic application.
- States that the last DDD step is defining bounded contexts as boundaries within a domain for those models.
- Introduces branch by abstraction as another approach, creating an abstraction layer over an original component to enable step-by-step replacement.
- Explains that client requests are directed to this abstraction layer, allowing changes behind it without affecting the client.
- States that when the changes are complete, clients interact only with the new component.
- Highlights that branch by abstraction allows two implementations of the same functionality to coexist, illustrating the Liskov substitution principle.
- Notes that, compared to the Strangler Fig pattern, branch by abstraction works at a lower abstraction level and focuses more on components than on systems.
- Recommends the book "Monolith to Microservices" by Sam Newman for readers interested in the branch by abstraction approach.
- Mentions the author’s free weekly newsletter for further learning, with over 19,000 subscribers.
