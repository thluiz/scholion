---
title: "Elixir - The Love Child of Ruby and Erlang"
date: '2015-02-03T17:37:46-03:00'
category: webclip
summary: 'The article tours Elixir’s core features: the IEx shell, functional tools, immutability, recursion, streams, the pipe operator, processes, message passing, and Erlang interoperability.'
tags: ["elixir", "functional-programming", "erlang", "concurrency"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Elixir - The Love Child of Ruby and Erlang"
    url: "http://www.sitepoint.com/elixir-love-child-ruby-erlang/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-02/sitepoint-com--elixir-love-child-ruby-erlang.md"
    kind: repo
---

The article presents Elixir as a functional, meta-programmable language built on the Erlang VM and notes its Ruby influence through José Valim. It then walks through the language’s main features with short IEx examples.

## Reading notes

- IEx is the interactive shell, and it includes syntax highlighting and built-in documentation access with commands like `h(Enum)` and `h(Enum.reverse)`.
- Elixir supports higher-order functions, so functions can be passed as arguments and returned as values, as shown with `Enum.map` and an anonymous square function.
- List comprehensions are available, but the article says `List` and `Enum` functions are often more flexible.
- Pattern matching is inherited from Prolog through Erlang and is used to destructure lists, tuples, atoms, and strings.
- Elixir data structures are immutable, so calling `List.delete` returns a new list without changing the original variable.
- Recursion replaces loops in the example `MyList.length`, which uses arity and pattern matching on empty and non-empty lists.
- Streams are lazy, which makes them suitable for infinite data sources and remote feeds, and the example uses `Stream.repeatedly` with `Enum.take`.
- The pipe operator `|>` passes the left-side result as the first argument to the next function, improving readability in chained calls.
- Elixir processes communicate by message passing, and the `Greeter` example uses `receive` with pattern matching to handle different message types.
- `spawn` starts a process and returns a pid, while unrecognized messages fall through to the catch-all `_` pattern.
- Elixir can call Erlang functions and libraries directly because both share the same byte code, and it also has access to Erlang’s OTP framework.
- The article closes by pointing readers to official documentation, books on Elixir and Erlang, and learning resources for Erlang.
