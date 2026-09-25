---
title: "CQRS Pattern With MediatR"
date: '2026-09-25T21:19:34+01:00'
category: webclip
summary: 'CQRS separates writes from reads so each side can be optimized independently. The text also shows how MediatR can model commands and queries with handlers and a request pipeline.'
tags: ["cqrs", "mediatr", "dotnet", "software-architecture"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "CQRS Pattern With MediatR"
    url: "https://t.co/kQx1k2flfP"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/t-co--cqrs-pattern-with-mediatr.md"
    kind: repo
---

CQRS separates the write side and the read side of an application, either as a logical split in one database or as a physical split across two. The text ties this to MediatR by extending `IRequest` into `ICommand` and `IQuery`, then sending each request through `ISender` to its handler.

## Reading notes

- CQRS gives commands and queries their own models so writes and reads can be optimized independently.
- The split can be logical in one database or physical across two databases.
- The text lists complexity management, improved performance, scalability, flexibility, and security as benefits.
- CQS is described as a method-level principle, while CQRS is its architectural evolution.
- With multiple databases, CQRS introduces eventual consistency and the need to handle synchronization failures.
- MediatR is presented as a way to apply CQRS with `IRequest`, custom `ICommand` and `IQuery` abstractions, and `ISender`.
- On the write side, the text favors EF Core and a rich domain model.
- On the read side, it favors minimal indirection, such as Dapper with raw SQL, database views, or EF Core projections.
- The request pipeline can handle cross-cutting concerns, including validation through `IPipelineBehavior`.
