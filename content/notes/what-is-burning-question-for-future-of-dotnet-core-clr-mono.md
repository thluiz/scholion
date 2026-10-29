---
title: "What is the burning question for the future of .NET / Core CLR / Mono today?"
date: '2016-03-29T16:07:07-03:00'
category: webclip
summary: 'The thread asks what matters most for .NET’s future: CoreCLR readiness, Mono’s role, Xamarin, F#, distributed systems, microservices, desktop tooling, and whether an OSS cross-platform shift can win broad adoption.'
tags: ["dotnet", "coreclr", "mono", "oss"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "What is the burning question for the future of .NET / Core CLR / Mono today? · Issue #73 · dotnetfringe/dotnetfringe.github.io"
    url: "https://github.com/dotnetfringe/dotnetfringe.github.io/issues/73"
    kind: repo
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-03/github-com--what-is-burning-question-for-future-of-dotnet-core-clr-mono.md"
    kind: repo
---

The issue collects questions about where the .NET stack is heading and what would make the new platform usable in practice. The discussion centers on CoreCLR production readiness, Mono’s future, Xamarin’s place in Microsoft, F# adoption, distributed systems, microservices, desktop development, and the business impact of an OSS cross-platform .NET.

## Reading notes

- The thread opens by asking which issues are most urgent for the .NET community, including CoreCLR, Mono, Xamarin, distributed systems, F#, libraries, and microservices.
- Several comments focus on whether CoreCLR will be ready for production and on the need for clearer branding and migration guidance.
- One view is that Mono still matters as the only viable cross-platform .NET solution, while another expects Mono and CoreCLR to converge over time.
- Xamarin is treated as part of the cross-platform tooling story, with attention to mobile development and the shift toward iOS and Android.
- F# is described as strong in the community but held back by weak adoption pressure, even though some commenters think the community could carry it forward.
- Distributed systems come up through Orleans, Akka.NET, MBrace, and broker-based approaches, with concern about the lack of practitioners and the trade-offs involved.
- Microservices are discussed as part of a broader move toward HTTP, brokers, lighter runtimes, and smaller deployments rather than heavy vendor-driven SOA.
- The thread also raises desktop development, XAML fragmentation, Electron, Chrome Apps, and the possibility of WebAssembly-based tooling.
- Some comments say the OSS shift helps .NET stay relevant, while others stress enterprise resistance, licensing concerns, and the difficulty of getting organizations to adopt or contribute back.
- The discussion repeatedly returns to the same practical question: whether CoreCLR and the broader .NET redesign will create a real path for new apps on non-Windows platforms.
