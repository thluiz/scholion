---
title: "reF#actoring: rewriting an actor in F#"
date: '2017-06-11T09:47:02-03:00'
category: webclip
summary: 'The article describes rewriting an Akka.NET Quartz scheduling actor in F# to reduce client dependencies on Quartz.NET and make the code more compact and idiomatic.'
tags: ["fsharp", "akka-net", "quartz-net", "actor-model"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "reF#actoring: rewriting an actor in F#"
    url: "http://miles.no/blogg/refactoring-rewriting-an-actor-in-f"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2017-06/miles-no--refactoring-rewriting-an-actor-in-f.md"
    kind: repo
---

The article explains why the team rewrote an Akka.Quartz.Actor-based scheduling actor in F#. Their goal was to keep the scheduling behavior they needed while removing client dependence on Quartz.NET details and on a direct Quartz.NET reference.

It compares the original C# project with the F# version and shows that discriminated unions, a functional actor loop, and a single-file layout made the code smaller and simpler. The article also notes that the F# version was tested with Akkling-style validation helpers and that the rewrite cut the code size by about 60%.

## Reading notes

- The team used Akka.NET as the actor framework in a media distribution engine at NRK.
- They tried an open-source scheduling actor and then chose to port it to F# for their own needs.
- Akka.Quartz.Actor already existed, and it had a NuGet package by the time of writing.
- The main concern was that clients still had to reference Quartz.NET and its trigger types.
- The F# version introduces a `JobSchedule` discriminated union for the scheduling DSL.
- `createTriggerBuilder` adapts the union cases to Quartz.NET trigger builder calls.
- The original C# command and event definitions were split across many files and much longer.
- The F# command and event definitions were condensed into a single file.
- The actor was rewritten as an F# function with a recursive `loop` inside `actor { ... }`.
- The F# actor starts and shuts down the Quartz scheduler and handles `CreateJob` and `RemoveJob` messages.
- A private `QuartzJob` type passes the message and actor reference through Quartz `JobDataMap`.
- The resulting code lives in one file called `Scheduler.fs` and is 106 lines long.
- The article says the rewrite reduced code size by about 60%.
- For testing, the author used helpers from Akkling to write F#-style actor tests.
- The conclusion argues that F# improved compactness and readability for this actor-based code.
