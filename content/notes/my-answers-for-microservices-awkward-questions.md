---
title: "My Answers for Microservices Awkward Questions"
date: '2015-03-19T11:59:10-03:00'
category: webclip
summary: 'The author frames his microservices experience as a report about reducing accidental coupling, then answers questions about deployment, ownership, monitoring, tracing, and what counts as a production-ready service.'
tags: ["microservices", "software-architecture", "deployment", "service-ownership"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Jay Fields' Thoughts: My Answers for Microservices Awkward Questions"
    url: "http://blog.jayfields.com/2015/03/my-answers-for-microservices-awkward.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-03/blog-jayfields-com--my-answers-for-microservices-awkward-questions.md"
    kind: repo
---

The post presents the author’s experience with small codebases as a response to accidental coupling in monolithic systems. He says he did not set out to build “microservices,” but to reduce coupling and keep software maintainable, and he treats the piece as an experience report rather than an argument for or against the approach.

## Reading notes

- The author says microservices were fringe when he started working on the application he mainly owns.
- He says he aimed to build a few small codebases that together provide one solid user experience.
- He prefers small services because accidental coupling is a major productivity drain in monolithic codebases.
- He says independent codebases reduce what can be accidentally coupled.
- He says each service compiles to a jar that can run independently and also be used as a library.
- He says something that is strictly a library provides no business value on its own.
- He says deployment uses shell scripts that copy jars and a web UI for browser-based deployment.
- He says the deployable unit is a jar.
- He says services are deployed in isolation, and new features should not require deploying separate services at the same time.
- He says backward compatibility is used so one service can be deployed first, run in production, and then another service can follow.
- He says they can run different instances of the same microservice with different configurations.
- He says another team may spin up another instance of a service.
- He says supported instances can be requested by others, who then become customers and pay allocated costs.
- He says forking a service is free but comes with no guarantees.
- He says the consumer is responsible for keeping up with API changes.
- He says there are common conventions and common libraries, but each service can still differ as needed.
- He says each service has a primary who is responsible for consistency.
- He says conventions are documented in the code.
- He says new team members pair exclusively for about four weeks and drive the whole time.
- He says service ownership usually comes only after at least six months on the team.
- He says the team uses a few common libraries for logging, testing, and common functions.
- He says monitoring is handled by proprietary software managed by another team, with frontline support on call.
- He says they log as much as is reasonable, log every user-generated interaction, and avoid logging some high-volume or large-data interactions.
- He says they have a test environment that can mirror production to reproduce interactions that were not logged.
- He says some systems log both interaction shapes and samples per shape.
- He says logging what you can and reproducing what you cannot log covers most cases.
- He says a production-ready microservice is something that provides value and has been hardened enough to create zero production issues under normal working circumstances.
- He says the smallest deployable microservice can be a single read-only webpage that shows data collected from other services.
