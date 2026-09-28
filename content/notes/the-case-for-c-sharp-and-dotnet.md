---
title: "The Case for C# and .NET"
date: '2022-07-26T14:26:25-03:00'
category: webclip
summary: 'The page argues that server-side JavaScript brings dependency sprawl, security risk, weaker performance, and productivity costs, while modern .NET and C# offer a more secure, faster, and lower-maintenance backend path.'
tags: ["c-sharp", "dotnet", "javascript", "backend"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The Case for C# and .NET. It has been interesting as I’ve shifted… | by Charles Chen | ITNEXT"
    url: "https://itnext.io/the-case-for-c-and-net-72ee933da304"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-07/itnext-io--the-case-for-c-sharp-and-dotnet.md"
    kind: repo
---

The page argues for C# and .NET as a better backend stack than server-side JavaScript. It contrasts Microsoft’s curated .NET libraries and cross-platform runtime with JavaScript’s dependency sprawl, security exposure, and weaker performance in benchmarks.

It also says TypeScript does not fully solve JavaScript’s productivity problems for backend work, because type tooling can encourage poor code organization and readability. The closing case is that modern .NET, especially with .NET Core, C# 10, and minimal APIs, is now a practical and familiar path for teams coming from TypeScript.

## Reading notes

- JavaScript used to be the author’s preferred language, especially for server-side work before ASP.NET.
- The .NET ecosystem is described as having richer first-party libraries and stronger governance than JavaScript’s package ecosystem.
- NPM dependency chains are presented as large, hard to manage, and sometimes exploited for low-quality package publishing.
- Security issues are tied to deep dependency stacks and vulnerabilities that can stay undiscovered for long periods.
- Benchmarks are used to argue that .NET often performs better than Node.js, sometimes by large margins, in serverless and web workloads.
- The author says TypeScript helps manage JavaScript, but can also lead inexperienced developers to rely too much on tooling and write worse code.
- Server-side JavaScript is portrayed as popular because it is easy to learn, easy to reuse across front end and back end, and supported by hot reload.
- The author now prefers a backend runtime with less maintenance burden, stronger contracts, and better security.
- Modern .NET is described as truly cross-platform and a more natural transition for developers already using TypeScript.
- The post ends by arguing that .NET and C# deserve broader adoption again as the platform matures.
