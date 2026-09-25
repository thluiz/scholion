---
title: "Don't use MediatR by default on all .NET projects"
date: '2026-09-25T09:00:42+01:00'
category: webclip
summary: 'The text argues that MediatR should not be added by default to every .NET project: the choice depends on the use case, and using internal messaging in dependent contexts can create unnecessary complexity.'
tags: ["net","mediatr","clean-architecture","cqrs"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Don't use MediatR by default on all .NET projects"
    url: "https://goatreview.com/dont-use-mediatr-by-default-net-projects/?utm_source=newsletter.csharpdigest.net&utm_medium=newsletter&utm_campaign=lesser-known-clr-gc-handles&_bhlid=46b30461a47be60a285fd3e1c55ba62047e3509b"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/goatreview-com--dont-use-mediatr-by-default-on-all-net-projects.md"
    kind: repo
---

The article argues that MediatR became common in .NET templates and tutorials, but that it should be added only when the use case justifies it. It shows a simpler use-case-based approach with commands and handlers, while keeping the option to switch to MediatR later if needed.

It also warns against using internal messaging between dependent contexts, especially when the operations must stay atomic. In that case, the text prefers direct service adapters over commands sent through MediatR, and says the same caution applies to other libraries such as EF Core and FluentValidation.

## Reading notes

- MediatR became almost synonymous with Clean Architecture in .NET projects, but that does not make it a mandatory dependency.
- The library facilitates the mediator pattern and decoupling between layers, but its adoption should be considered case by case.
- The text proposes maintaining a use-case-centered architecture without depending on MediatR's internal messaging system.
- The structure without MediatR uses its own interfaces for commands and handlers, with declarations similar to the library's.
- The API routes stay practically the same in both approaches, changing only the injection of the handler or the sender.
- Configuration without MediatR can be done with explicit registration of the handler in the container, and the author says this could also be automated with an extension similar to RegisterServicesFromAssemblies.
- The text avoids using CQRS as a label for this example, because it associates CQRS with separating reads and writes in the database.
- The main advantage of the approach without MediatR is allowing a return to the library later, with small changes to the interfaces and endpoint declarations.
- Using MediatR to trigger other operations inside a handler becomes a problem when the operations depend on each other.
- If creating a goat and recording an audit trail are independent, the text argues for publishing an event at the end of processing.
- If the operations are atomic, sending commands after the handler finishes can delay validations such as credit checking.
- In this scenario, calling another context inside the handler through internal messaging increases complexity and mixes dependent services.
- The suggested alternative is to use service adapters for communication between contexts, keeping the atomic relationship when it is necessary.
- The conclusion broadens the criticism to other libraries used out of habit, such as EF Core and FluentValidation, and asks whether the technical choice is a real need or developer preference.
