---
title: "Domain-Driven Design meets Functional Programming"
date: "2026-09-23T18:41:21+01:00"
category: webclip
has_commentary: false
summary: "Interview with Scott Wlaschin on why DDD's demand for composable, autonomous subsystems fits functional programming better than OO does in practice."
tags:
  - domain-driven-design
  - functional-programming
  - fsharp
  - software-design
sources:
  - title: "Domain-Driven Design meets Functional Programming"
    url: "https://blog.avanscoperta.it/2021/09/14/domain-driven-design-meets-functional-programming-scott-wlaschin/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/blog-avanscoperta-it--domain-driven-design-meets-functional-programming-scott-wlaschin.md"
    kind: repo
---

Matteo Baglini interviews Scott Wlaschin, author of fsharpforfunandprofit.com and the book Domain Modeling Made Functional, about why Domain-Driven Design and functional programming pair well. Wlaschin places FP as older than object-oriented programming and already leaking into OO languages through features like Java's lambdas and C#'s immutable records, while scoping it to pipelines of data transformation rather than distributed actor systems or behavior-heavy GUI code.

The DDD connection rests on composability. DDD asks subsystems to stay composable and autonomous, and FP's absence of mutable state makes that easier to sustain in practice than OO's theoretical support for the same properties. He also credits FP's algebraic type system, where AND/OR map directly onto domain choices, with modeling a domain more concisely than OO subclassing does.

## Reading notes

- FP predates object-oriented programming and keeps surfacing inside OO languages, through features like Java's lambdas and C#'s immutable records.
- FP suits data-transformation pipelines; a distributed system of independent components fits an actor model instead, the way Erlang works, and behavior-heavy code such as a GUI widget library fits OO.
- DDD calls for composable, autonomous subsystems. FP's lack of mutable state and side effects sustains that in practice more reliably than OO's theoretical support for the same properties.
- FP's algebraic type system maps AND/OR directly onto domain choices, modeling them more concisely than OO subclassing.
- In a microservices architecture, each autonomous subsystem gets modeled as its own domain in FP, communicating with the others through buffered asynchronous message queues.
- DDD is conceptually simple but hard to put into practice because it needs collaboration from other people. FP is a genuinely new paradigm for most developers and takes time to grow comfortable with.
- Non-developers respond well to domain models written in F#. The resistance to FP comes mostly from programmers unfamiliar with the paradigm, not from the business side.
- Names "The Design of Everyday Things" (Don Norman) and "How Buildings Learn" (Stewart Brand) as non-programming books that shaped his user-centered approach to design.
