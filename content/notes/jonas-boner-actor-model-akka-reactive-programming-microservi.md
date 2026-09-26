---
title: "Jonas Bonér on the Actor Model, Akka, Reactive Programming, Microservices and Distributed Systems"
date: '2026-09-27T00:37:09+01:00'
category: webclip
summary: 'Jonas Bonér presents Akka as a JVM toolkit for distributed systems, links the Actor Model to message passing and fault handling, and frames microservices as full systems built for resilience.'
tags: ["akka", "actor-model", "distributed-systems", "microservices"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Jonas Bonér on the Actor Model, Akka, Reactive Programming, Microservices and Distributed Systems"
    url: "https://www.infoq.com/podcasts/jonas-boner-akka?utm_source=email&utm_campaign=summerpodcast"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/infoq-com--jonas-boner-actor-model-akka-reactive-programming-microservi.md"
    kind: repo
---

Jonas Bonér describes Akka as a JVM toolkit for distributed systems built on the Actor Model. The podcast ties the model to message passing, private actor state, streaming, and handling failures such as dropped messages and partial failures. It also connects reactive systems, reactive programming, and the Saga pattern to the needs of resilient distributed communication.

## Reading notes

- Akka is a JVM-based toolkit for distributed systems built around the Actor Model.
- The Actor Model uses actors as universal primitives, with private state and message passing instead of locks.
- Akka makes distribution a first-class concern and combines concurrency with work across machines and nodes.
- Streams are presented as the most successful abstraction added on top of the actor model.
- Circuit breakers are described as a backup and retry policy that captures failure data and supports rollback.
- The talk links distributed systems to multi-core hardware, virtualized environments, and the cloud.
- The Reactive Manifesto is presented as a framework for building reliable systems that are elastic, resilient, and responsive.
- Reactive systems depend on asynchronous message passing.
- Event-driven and message-driven styles are distinguished, with message-driven communication described as the basis for reactive systems.
- Reactive programming is defined as using non-blocking and asynchronous communication to make components efficient and use hardware well.
- Every microservice should be viewed as a system with multiple parts running on different machines to be fully functional and resilient.
- Before deploying distributed systems, people, process, team structure, continuous delivery, rollback, and system visibility need to be addressed.
- The Saga pattern is described as a way to manage long-running transactions through compensating actions instead of global locks.
