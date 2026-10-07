---
title: "Why Microservices Matter"
date: '2015-01-24T08:16:32-03:00'
category: webclip
summary: 'Heroku argues that microservices help large teams scale by splitting applications into smaller services, but they also add operational overhead, testing complexity, and integration costs.'
tags: ["microservices", "paas", "distributed-systems"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Heroku | Why Microservices Matter"
    url: "https://blog.heroku.com/archives/2015/1/20/why_microservices_matter"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-01/blog-heroku-com--why-microservices-matter.md"
    kind: repo
---

Microservices are presented as a way to decompose a growing application into smaller pieces that are easier to manage, let teams work more independently, and make it simpler to adopt different technologies where they fit. The post also ties the approach to modern software use, where services must serve many devices and respond quickly under changing demand.

## Reading notes

- Successful applications tend to become more complex over time, so teams manage that complexity either by keeping one monolithic codebase or by splitting the project into smaller parts.
- A monolith can be easier to reason about and operate, but deploying a very large project can slow delivery and make collaboration harder as teams grow.
- A microservice is defined as application functionality factored into its own codebase and connected to other services through a standard protocol.
- Microservices map business functions into separate services, such as account management, advertising logic, or a web interface.
- The post says this structure fits a world of APIs and many devices, and it can support low-latency global deployment and multiple versions of the same service for redundancy.
- Microservices are not described as a solution to every problem, and the author says they do not make a slow IT organization fast.
- One driver of the microservices trend was a reaction against monolithic architecture, since smaller services let engineers work more independently and make individual changes less costly.
- Another driver was the availability of reliable Platform-as-a-Service providers, which supply supporting capabilities like load balancing, discovery, process monitoring, and scaling outside the application container.
- The post recommends considering microservices when scaling over time, but warns that each service adds overhead, monitoring, alerting, and system-integration work.
- It advises against splitting code too finely and says a sensible place to start is separating mobile and web clients from their APIs.
