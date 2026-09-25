---
title: "Possibilities of abstractions"
date: '2026-09-25T20:21:53+01:00'
category: webclip
summary: 'The article compares ways to abstract multiple implementations in F#: function records, interfaces, supplied functions, and discriminated unions. It weighs brevity, naming, optional parameters, documentation, and state handling.'
tags: ["fsharp", "abstraction", "interfaces", "function-records"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Possibilities of abstractions"
    url: "https://raymens.github.io/posts/1-type-abstractions.html"
    kind: repo
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/raymens-github-io--possibilities-of-abstractions.md"
    kind: repo
---

The article compares several ways to build types with different implementations while hiding details from consumers. It focuses on F# and contrasts succinct function-record styles with interfaces, then notes other options such as passing functions directly or using discriminated unions.

## Reading notes

- Function records are a concise way to package behavior, but they do not support named parameters directly, and optional parameters need `option` values.
- Record fields can carry `///` documentation, and record-like parameter objects can make meanings more explicit.
- Interfaces feel more natural for C#-style contracts, support named and optional parameters, and make it easier to keep state inside the implementation.
- Interface-based code can use XML documentation, which is useful when the code is consumed by other .NET libraries.
- Another option is to pass the needed functions one by one, or to turn those functions into type aliases and mix them with records.
- Discriminated unions can represent real and fake implementations, but each function must know which implementation it is using.
- The article concludes that there are no winners or losers, and that the preferred path is to start with functions and data and move toward a more OO solution only when control or state becomes necessary.
