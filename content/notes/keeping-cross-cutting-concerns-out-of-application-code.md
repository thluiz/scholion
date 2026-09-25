---
title: "Keeping cross-cutting concerns out of application code"
date: "2026-09-23T19:37:15+01:00"
category: webclip
has_commentary: false
summary: "Mark Seemann refactors a Polly-coupled API class into application code with zero third-party dependencies, moving fault tolerance into a Decorator at the Composition Root."
tags:
  - software-design
  - dependency-injection
  - decorator-pattern
  - dotnet
sources:
  - title: "Keeping cross-cutting concerns out of application code"
    url: "https://blog.ploeh.dk/2024/09/02/keeping-cross-cutting-concerns-out-of-application-code/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/blog-ploeh-dk--keeping-cross-cutting-concerns-out-of-application-code.md"
    kind: repo
---

Mark Seemann starts from a Stack Overflow question about testing a `MyApi` class that injects both a Polly `ResiliencePipeline` and an `IOrganizationService`, wraps every call in `pipeline.Execute(...)`, and asks how to unit test it. His answer sidesteps the testing question by removing the reason it's hard to test: cross-cutting concerns like fault tolerance, logging, or caching belong in a Decorator, not injected straight into application code.

He walks the refactor in three moves: wrap `IOrganizationService` in a `ResilientOrganizationService` Decorator that owns the Polly pipeline, strip `MyApi` down to just the interface it actually needs, then wire the Decorator into `MyApi` at the Composition Root. What's left of `MyApi` has no Polly reference at all, and the resulting unit test needs only a mock of `IOrganizationService`.

## Reading notes

- The `ResilientOrganizationService` Decorator implements `IOrganizationService` itself while wrapping another instance of it, executing every call through the injected `ResiliencePipeline`. `MyApi` never sees Polly again.
- Constructor design follows Nikola Malovic's 4th law of DI, cited directly: a resolved class's constructor should do nothing but accept its own dependencies. The Decorator takes a ready-made `ResiliencePipeline` rather than a `ResiliencePipelineProvider` it would have to call `GetPipeline` on.
- Composition happens at the Composition Root: `new MyApi(new ResilientOrganizationService(pipeline, inner))`. Polly, and any pipeline-building code (`CreatePipeline`, retry/timeout configuration), stays entirely at that boundary.
- Two reasons given for decoupling from a third-party dependency, even a well-regarded one like Polly: it will keep changing over a five-to-ten-year system lifetime, and the maintaining organization can stop operating. Json.NET's fate after Microsoft shipped its own JSON API is the example cited for the first point.
- The article frames this as a bet on risk management: pay the small up-front cost of decoupling now, or postpone it and hope it's never needed. Seemann says he usually pays it up front, partly because it also makes unit testing simpler as a side effect.
- Explicit disclaimer: the piece isn't a criticism of Polly specifically, it's a general pattern (Decorator for cross-cutting concerns) illustrated with whatever third-party dependency happened to come up in the source question.
