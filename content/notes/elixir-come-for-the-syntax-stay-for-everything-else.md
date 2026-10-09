---
title: "Elixir: Come for the syntax, stay for everything else"
date: '2015-04-10T11:35:01-03:00'
category: webclip
summary: 'The author says Elixir first appeals through Ruby-like syntax, then keeps developers with functional programming, scalability, memory handling, immutability, fault tolerance, and a community he trusts.'
tags: ["elixir", "functional-programming", "backend-development", "programming-languages"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Elixir: Come for the syntax, stay for everything else"
    url: "http://reefpoints.dockyard.com/2015/04/08/elixir-come-for-the-syntax-stay-for-everything-else.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-04/reefpoints-dockyard-com--elixir-come-for-the-syntax-stay-for-everything-else.md"
    kind: repo
---

The author says Elixir first hooked him through syntax, especially its resemblance to Ruby. He presents that syntax as only the entry point, and says the real reason to stay is what the language offers beyond it.

## Reading notes

- Elixir appeals to Ruby developers because it keeps a Ruby-like syntax while offering more than syntax alone.
- The author places Elixir alongside Go and Rust as a language that may shape backend development in the next decade.
- Functional programming is the main reason he stays with Elixir.
- Elixir can use CPU cores well through the BEAM VM, without extra work from the programmer.
- Elixir programs are split into many processes, which reduces the impact of garbage collection.
- Each process manages its own memory, and short-lived processes may finish before garbage collection runs.
- Immutability matters because it helps keep state stable when processes run in parallel.
- The author values Elixir’s fault tolerance, including hot code swapping and the possibility of zero-downtime deploys.
- He prefers technologies that are not controlled by a single company, and sees Elixir’s community as more open than the communities around Go and Rust.
- He says Elixir’s community feels similar to the early Ruby community.
- He recommends Elixir to Ruby developers looking for a change of pace and points to Dave Thomas’s book as a starting place.
