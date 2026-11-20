---
title: "David Fowler on Blazor and full stack in .NET 8"
date: '2023-10-24T14:26:40+00:00'
category: webclip
summary: 'David Fowler argues that .NET 8, with Blazor’s server rendering and SignalR-based interactivity, finally delivers a convincing full-stack story alongside major JavaScript frameworks.'
tags: ["dotnet", "blazor", "full-stack", "web-development"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "David Fowler on Blazor and full stack in .NET 8"
    url: "https://threads.net/t/Cuw-t8MAOrY"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/threads-net--david-fowler-blazor-full-stack-dotnet-8.md"
    kind: repo
---

David Fowler comments that in .NET 8 Blazor finally delivers on a convincing "full stack" experience. He connects this to the broader shift of major JavaScript client-side frameworks toward server rendering, which he sees as giving Blazor a realistic chance to sit alongside those established options.

He highlights the current attention around React Server Components and Next.js server rendering, while noting that server rendering has long been central to ASP.NET Core. Extending that model to Blazor is described as the missing piece for the full-stack story. Fowler also emphasizes Blazor’s server rendering mode that uses SignalR per component to support client interactivity while keeping all code on the server. He says he has migrated some of his apps to .NET 8 and hopes more people will try Blazor in this release, adding that there is still much work to do but that .NET 8 preview 6 is the first major milestone where many features are functioning.

## Reading notes

- Fowler says that with .NET 8 it finally feels like the "full stack" challenge has been solved for Blazor.
- He links this to a recent trend where many JavaScript client frameworks are adopting server rendering.
- This shift is described as giving Blazor a serious opportunity to coexist with large, established JavaScript frameworks.
- He mentions significant excitement about React Server Components and Next.js server rendering and considers that excitement justified.
- Fowler states that server rendering has long been a core strength of ASP.NET Core.
- He views bringing ASP.NET Core-style server rendering into Blazor as the step that completes Blazor’s overall picture.
- He describes a Blazor server rendering mode that uses SignalR at the component level to provide client interactivity.
- In this mode, he notes that all application code remains on the server.
- Fowler says he has already upgraded some of his own applications to run on .NET 8.
- He expresses hope that more developers will try Blazor in this .NET 8 release.
- He remarks that there is still a lot of work ahead for the platform.
- He identifies .NET 8 preview 6 as the first major release where many of the planned features are available and working.
