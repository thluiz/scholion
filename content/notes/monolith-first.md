---
title: "MonolithFirst"
date: '2015-06-05T10:23:43-03:00'
category: webclip
summary: 'The page argues for starting new applications as a monolith, since microservices add overhead, depend on stable boundaries, and are easier to adopt later after the system’s shape becomes clearer.'
tags: ["microservices", "monolith", "software-architecture"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "bliki: MonolithFirst"
    url: "http://martinfowler.com/bliki/MonolithFirst.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-06/martinfowler-com--monolith-first.md"
    kind: repo
---

The page argues that many successful microservice systems began as monoliths that were later split apart, while projects built as microservices from the start often ran into trouble. It recommends a monolith-first strategy for new applications, especially because microservices bring extra management cost and slow teams down on simpler systems.

## Reading notes

- Successful microservice stories often begin with a monolith that became too big and was then broken up.
- Systems built as microservices from scratch have often ended up in serious trouble.
- Microservices carry a significant premium, which makes them a poorer fit for simpler applications.
- A new application should often start as a monolith, even if microservices may be useful later.
- The first reason is YAGNI: at the start, it is uncertain whether the application will be useful, so speed and feedback matter more than microservice overhead.
- Microservices require good, stable service boundaries, and those boundaries are hard to get right at the beginning.
- Refactoring across services is much harder than refactoring inside a monolith.
- A monolith-first approach can help reveal the right boundaries before moving to microservices.
- One way to execute this strategy is to design the monolith carefully, with modular APIs and storage.
- Another common way is to start with a monolith and gradually peel off microservices at the edges.
- Another route is to replace the monolith entirely after using it to get to market quickly.
- A different approach is to begin with a small number of coarse-grained services and split them further once boundaries stabilize.
- The counterargument is that starting with microservices helps teams learn the rhythm of service-based development and scale team effort earlier.
- This counterargument is presented as more viable for system replacements and for teams with reasonable experience building microservice systems.
- The page treats advice on this question as tentative because microservices are still early and there are relatively few anecdotes to rely on.
