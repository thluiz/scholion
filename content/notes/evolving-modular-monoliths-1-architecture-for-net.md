---
title: "Evolving modular monoliths: 1. An architecture for .NET"
date: '2021-06-14T13:48:19-03:00'
category: webclip
summary: 'The article introduces a modular monolith approach for .NET that keeps monolith simplicity while isolating features with bounded contexts, layered design, and rules that improve cohesion, testability, and changeability.'
tags: ["modular-monolith", "dotnet", "bounded-contexts", "clean-architecture"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Evolving modular monoliths: 1. An architecture for .NET – The Reformed Programmer"
    url: "https://www.thereformedprogrammer.net/evolving-modular-monoliths-1-an-architecture-for-net/?utm_source=csharpdigest&utm_medium=email&utm_campaign=363"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2021-06/thereformedprogrammer-net--evolving-modular-monoliths-1-architecture-for-net.md"
    kind: repo
---

The article presents a way to structure a .NET application so it stays simple like a monolith but avoids becoming a "big ball of mud." It combines clean architecture and DDD bounded contexts to separate business features, support testing, and make code easier to find and change.

## Reading notes

- The series focuses on building a .NET application with a modular monolith architecture.
- The goal is to keep monolith simplicity while preserving structure as the application grows.
- The design uses clean separation between major parts of the application through modular monolith structure and DDD bounded contexts.
- The article does not compare monoliths with microservices or serverless architectures.
- The intended audience is .NET developers and software architects who already know C#, projects, and NuGet packages.
- The author applies encapsulation, separation of concerns, organisation, collaboration, development effort versus reward, and testability as guiding principles.
- The first level of modularization is an n-layered application with front-end, service layer, infrastructure, business logic, persistence, and domain layers.
- The author uses a clean architecture style, but with some changes, including a Persistence layer deep inside the rings and interfaces placed with the service that defines them.
- Front-end code is kept thin, and services are used to handle input and output because they are easier to test than ASP.NET Core pages or APIs.
- The ServiceLayer acts as an adapter between business classes and user-facing code.
- A pure n-layered structure keeps separation at the layer level, but not within layers, so layers can become large and hard to navigate.
- The second level of modularization uses DDD bounded contexts to isolate feature groups such as Books and Orders into separate .NET projects.
- Each bounded context contains its own layers, namespaces, and projects, with a naming convention that makes the code easier to locate.
- Bounded contexts can share data without losing isolation, and the article says this is covered later in the series.
- The third level of modularization breaks code up inside a bounded context so large features can be split into smaller .NET projects.
- The author places code for specific queries or features into separate projects, especially in the ServiceLayer.
- The rules are that projects only reference others in the same bounded context, outer layers can reference inner layers, and same-layer sharing is allowed only for projects named "Common."
- Unit tests are used to enforce those modularization rules.
- The approach is presented as a way to reduce spaghetti code and make relationships between parts of the system harder to violate.
- For large applications, the article considers tooling limits, team collaboration, and whether the approach can be added to an existing monolith.
- The author suggests moving larger or more complex bounded contexts into separate solutions, packaging them as NuGet packages, and installing them in the main application.
- This keeps the benefits of quick method and data transfer while giving teams more separation.
- The article concludes that the author’s experience with this structure made code easier to find and later helped with refactoring for performance tuning and CQRS.
