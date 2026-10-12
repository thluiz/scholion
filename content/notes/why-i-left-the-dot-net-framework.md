---
title: "Why I Left the .NET Framework"
date: '2014-07-06T13:21:28-03:00'
category: webclip
summary: 'The author says .NET was strong, but its defaults narrowed choice, pushed developers inward, and kept implementation details ahead of the model and business behavior.'
tags: [".net", "software-development", "architecture", "vendor-lock-in"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Why I Left the .NET Framework"
    url: "http://blog.jonathanoliver.com/why-i-left-dot-net/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-07/blog-jonathanoliver-com--why-i-left-the-dot-net-framework.md"
    kind: repo
---

The post argues that .NET had real strengths, especially C#, ReSharper, BDD tools like MSpec, the CLR’s multi-language idea, NuGet, Mono, and the role of CQRS and event sourcing. It also says those gains came partly from the wider community rather than .NET itself.

The reasons for leaving are tied to Windows, Visual Studio, source control habits, Mono’s limits, IIS, close-mindedness, lock-heavy performance patterns, and SQL Server defaulting. The core claim is that .NET kept pulling projects toward its own assumptions instead of leaving technology as an implementation detail and keeping the model centered.

## Reading notes

- .NET had strong pieces, especially C#, ReSharper, MSpec, NuGet, Mono, and CQRS/event sourcing.
- The author values the CLR as a multi-language runtime that influenced JVM languages and competition.
- Windows is presented as limiting for server work, cross-platform skills, filesystem choices, and cloud scaling speed.
- Visual Studio is described as heavy, slow, and tied to project files that create friction and merge conflicts.
- Source control improved with git, while TFS is portrayed as invasive and clumsy.
- Mono is praised as impressive but described as slower and less reliable for serious workloads.
- IIS is criticized for performance and for trying to act like an application host rather than a web server.
- ALT.NET is cited as a reaction against close-mindedness inside traditional .NET circles.
- The post criticizes locks, blocking I/O, and thread-heavy designs as performance killers.
- SQL Server is treated as the default that encourages early technology choices and vendor lock-in.
- The conclusion says software should start from the model and business behavior, with technology kept as an implementation detail.
