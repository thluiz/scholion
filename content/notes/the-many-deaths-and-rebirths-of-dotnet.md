---
title: "The Many Deaths and Rebirths of .NET"
date: '2026-07-06T12:43:07+01:00'
category: webclip
summary: '.NET moved from a Windows-centered framework to a cross-platform runtime, with .NET Core, .NET Standard, and .NET 5+ marking a public reset, unification, and steady maturity.'
tags: ["dotnet", "dotnet-core", "dotnet-standard", "software-history"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The Many Deaths and Rebirths of .NET | Bipin Joshi .NET"
    url: "https://www.binaryintellect.net/articles/abee895e-480b-4aca-b174-d8ce1c6f012d.aspx?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-07/binaryintellect-net--the-many-deaths-and-rebirths-of-dotnet.md"
    kind: repo
---

The article reads .NET as a survival story shaped by changing platform assumptions. It says .NET Framework fit a Windows-first world, then became hard to move because of its deep ties to Windows APIs and IIS. Microsoft answered by open-sourcing .NET Core, accepting a restart in public rather than trying to patch the old foundation.

It also explains how .NET Standard served as a bridge between Framework and Core, then lost its central role once the platform unified under .NET 5 and later releases. The newer .NET line is presented as faster, cross-platform, and more stable, with .NET 6 through 10 showing a mature platform that keeps improving without another identity crisis.

## Reading notes

- .NET Framework shipped in 2002 with the assumption that Windows was the platform.
- It offered managed runtime support, garbage collection, and a unified way to build web, desktop, and service applications on Windows.
- Its deep dependence on Windows made it difficult to port to Linux without rebuilding it.
- Microsoft responded by creating .NET Core and open-sourcing it on GitHub.
- .NET Core 1.0 was cross-platform and fast, but it lacked many APIs and technologies that Framework developers had relied on.
- The article frames that restart as a loss for many developers who had to become beginners again.
- .NET Core’s strengths were performance, modular deployment, self-contained executables, and support for Linux, Mac, Docker, and ARM.
- .NET Standard is described as a specification meant to let libraries run across different runtimes.
- It existed to bridge the gap between Framework and Core, and it is now presented as finished.
- .NET 5 dropped the word Core and signaled unification under a single .NET name.
- The numbering moved from 3.1 to 5 to avoid confusion with .NET Framework 4.x.
- .NET 6 added MAUI, minimal APIs, hot reload, and Blazor.
- .NET 7 continued performance work in areas like JSON serialization, LINQ, regular expressions, and native AOT.
- .NET 8 is described as an LTS release and a mature production version.
- The article says .NET 11 will continue the same steady versioning rather than another reinvention.
- It ends by arguing that platforms grow by outgrowing themselves, and that .NET’s reinvention came from humility and public rebuilding.
