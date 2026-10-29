---
title: "Functional Patterns in Domain-Driven Design"
date: '2016-04-11T12:10:45-03:00'
category: webclip
summary: 'The page says DDD benefits from a ubiquitous language, but class-based state-and-behavior models can become muddled and fragile. It presents standalone functions as a better fit for modular domain behavior.'
tags: ["domain-driven-design", "functional-programming", "domain-modeling"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Functional Patterns in Domain-Driven Design"
    url: "http://www.infoq.com/news/2014/05/functional-patterns-ddd?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-04/infoq-com--functional-patterns-in-domain-driven-design.md"
    kind: repo
---

The page argues that Domain-Driven Design benefits from a domain model and a ubiquitous language, but that implementing DDD with stateful objects can produce a muddled mutable model. It presents functional patterns as a way to make domain behavior more modular and aligned with the domain.

## Reading notes

- DDD supports building a domain model and a ubiquitous language, but object-oriented implementations can become muddled and mutable.
- A class that holds many concepts from one domain abstraction can become fragile and locally focused, with extra code needed to bridge class boundaries.
- Dean Wampler is cited as arguing that models should be anaemic, with state in domain objects and behavior moved into standalone functions.
- Debasish Ghosh rejects the idea that bundling state and behavior in a class increases encapsulation.
- He says standalone functions can improve modularization and represent domain behaviors more clearly inside a module for the aggregate.
- The examples connect to earlier work on implementing Specification and Aggregate patterns with functional programming principles.
- He says DDD should lift domain vocabulary into the implementation so the system’s functionality stays obvious throughout its lifecycle.
- Dean Wampler is also mentioned as having given a related talk at React conference in April.
