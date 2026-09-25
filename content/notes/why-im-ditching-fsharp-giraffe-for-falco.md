---
title: "Why I'm Ditching F# + Giraffe For Falco For Building WebApps"
date: '2026-09-25T19:18:25+01:00'
category: webclip
summary: 'The author says Giraffe is still solid, but Falco’s simpler API, similar performance, and recent updates made it the new default for CloudSeed and future F# web apps.'
tags: ["fsharp", "giraffe", "falco", "web-frameworks"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Why I'm Ditching F# + Giraffe For Falco For Building WebApps"
    url: "https://hamy.xyz/blog/2025-01_ditching-giraffe-for-falco"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/hamy-xyz--why-im-ditching-fsharp-giraffe-for-falco.md"
    kind: repo
---

The author says Giraffe is still a solid choice for F# web apps and remains in use on existing projects, including this blog. The change is about preference: some APIs feel cumbersome, best practices around endpoints feel split, and big updates are rare.

Falco won out because its APIs feel clearer, it performs similarly, and its active development made it worth adopting. CloudSeed was updated to use Falco as its core web framework, while the author notes that other production-ready F# frameworks also exist.

## Reading notes

- Giraffe is described as fast, straightforward, battle-tested, regularly updated, and still a good option for building web apps with F#.
- The author does not see a need to move existing projects off Giraffe, and the blog itself still runs on F# + Giraffe.
- The main drawbacks mentioned are cumbersome APIs, split community guidance on endpoint practices, and the lack of major updates.
- Falco is presented as having clear and straightforward APIs.
- The author tried Falco after following its development and being interested in the changes in v5.
- Falco is described as performing similarly well, which helped support the decision to adopt it.
- The author has already built several side projects with Falco and made it the default for future projects.
- CloudSeed was updated to reflect that choice and now uses Falco as its core web framework.
- The post also mentions Saturn, WebSharper, and Oxpecker as other production-ready F# web frameworks worth considering.
