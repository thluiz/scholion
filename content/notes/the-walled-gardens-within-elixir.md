---
title: "The Walled Gardens within Elixir"
date: '2020-07-05T14:10:40+00:00'
category: webclip
summary: 'The article argues that Elixir lacks a built-in way to reflect all modules that implement a behaviour or use a macro, and surveys static lists, BEAM introspection, protocols, and ProtocolEx as ways to build registries around that gap.'
tags: ["elixir", "behaviour-reflection", "registry", "protocols"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The Walled Gardens within Elixir. Elixir is great, in this article… | by Marcel Otto | Medium"
    url: "https://medium.com/@MarcelOttoDE/the-walled-gardens-within-elixir-d0507a568015"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/medium-com--the-walled-gardens-within-elixir.md"
    kind: repo
---

The article describes a recurring limitation in Elixir: there is no built-in way to reflect all modules that implement a behaviour, or all modules that `use` a given module. To show the problem, it walks through examples from RDF.ex and SPARQL.ex, where registries are needed for serialization formats, SPARQL extension functions, and datatypes.

It then compares several ways to work around the limitation. Static module lists can work in some cases, BEAM introspection can discover loaded modules and compiled files, runtime stores like ETS or FastGlobal can hold registries, protocols expose implementations only at runtime, and ProtocolEx can provide a fast pattern-based registry with consolidation. The article closes by saying each approach feels like a workaround, and that Elixir or the BEAM still lack a native solution.

## Reading notes

- Elixir does not provide a built-in way to reflect all modules that implement a behaviour.
- The same gap also appears for modules that are brought in with `use`.
- In RDF.ex, this affects registries for serialization formats and datatypes.
- In SPARQL.ex, it affects registries for extension functions.
- Static listings can be acceptable when the set of implementations is manageable.
- Filtering static lists with `Code.ensure_loaded?/1` can remove modules that are not present in the application.
- `:code.all_loaded/0` can be used to inspect loaded modules, but its result depends on how the BEAM runtime was started.
- Reading compiled `.beam` metadata can find behaviour implementations from project files, but it does not cover `.exs` files and depends on Mix.
- A runtime registry can be stored in a process or ETS.
- For very performance-sensitive lookups, mochiglobal-style solutions such as FastGlobal are mentioned.
- Protocols expose implementations through `__protocol__(:impls)`, but only after consolidation and only at runtime.
- ProtocolEx can map identifiers to implementations through pattern matching and supports consolidation for fast lookup.
- The article ends by saying these solutions work around the problem, but do not remove it from the language or the runtime.
