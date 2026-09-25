---
title: "About"
date: '2026-09-25T17:22:07+01:00'
category: webclip
summary: 'The page explains why Liquid Projections was created, emphasizing autonomous projectors, dependency control, async support, and small NuGet building blocks for synchronous and asynchronous projectors.'
tags: ["event-sourcing", "projectors", "nuget", "async"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "About"
    url: "https://liquidprojections.net/about/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/liquidprojections-net--about.md"
    kind: repo
---

Liquid Projections is presented as a response to two concerns: projectors in event sourcing should have enough autonomy to choose how they work and when, and libraries should avoid creating dependency traps. The page says each projector should decide its own storage and execution model, and that libraries should only require the dependencies they truly need.

It describes Liquid Projections as a set of efficient building blocks that work alone but are stronger together for synchronous and asynchronous projectors. The package is said to be battle-tested in production, built around `async`, distributed as NuGet packages, and designed for broad .NET platform support.

## Reading notes

- Projectors should have the autonomy to decide how they work and when they run.
- A projector may use memory, a document database, or an OR/M, and that choice belongs to that projector.
- Each projector should be able to run at its own pace and restart itself when needed.
- Libraries should avoid dependency hell.
- Inheritance is avoided unless there is a real functional relationship.
- Base classes can hide too much magic and force users into a certain direction.
- If a library does not fit a need, users may have to fork it and create their own version.
- Liquid Projections is introduced as a set of building blocks for synchronous and asynchronous projectors.
- The library is described as efficient and as useful on its own, but stronger when used together.
- It is distributed as a collection of NuGet packages so users only depend on what they need.
- It embraces `async` and is designed for many .NET platforms.
- It uses Semantic Versioning and Semantic Release Notes.
- The library has gone through breaking changes and bug fixes and is described as reaching calmer waters.
