---
title: "Writing Documentation – Elixir v1.3.0-dev"
date: '2016-02-07T22:30:58-03:00'
category: webclip
summary: 'Elixir treats documentation as a first-class citizen and explains how to write it with Markdown, module attributes, doctests, privacy rules, and the difference between docs and comments.'
tags: ["elixir", "documentation", "markdown", "doctests"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Writing Documentation – Elixir v1.3.0-dev"
    url: "http://elixir-lang.org/docs/master/elixir/writing-documentation.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-02/elixir-lang-org--writing-documentation-elixir-v1-3-0-dev.md"
    kind: repo
---

Elixir treats documentation as a first-class part of the language, meant to be easy to write and easy to read. The page covers the main conventions for writing docs, including Markdown, module attributes, doctests, privacy, and the distinction between documentation and code comments.

## Reading notes

- Elixir documentation is written in Markdown, and GitHub guides are suggested as a starting point.
- Documentation is usually attached to module attributes.
- `@moduledoc` documents a module, `@doc` documents a function, and `@typedoc` documents types in typespecs.
- Function argument names are inferred by the compiler, but a bodyless clause can be used when the inferred names are not good enough.
- The first paragraph should be short and simple, because tools like ExDoc use it as the summary.
- Code references in docs should use full module names, and functions should be referenced with name and arity.
- Headings should start at `##`, because the first heading is reserved for the module or function name.
- Examples are encouraged under `## Examples`, and doctests use `iex>` snippets from the documentation.
- When a function depends on state or side effects, the page recommends including examples without the `iex>` prompt.
- `@moduledoc false` hides whole modules from documentation.
- `@doc false` does not make a function private, so the page recommends caution with it.
- Undocumented functions can be hidden in a module with `@moduledoc false`, or given an underscore prefix such as `__add__/2`.
- Documentation and code comments are treated as different things: docs are for API users, while comments are for developers reading the code.
- Documentation is required for public API modules and functions, while code comments are optional.
- Documentation is stored in bytecode chunks and can be accessed with `Code.get_docs/2`.
- Modules defined in memory, such as in IEx, do not have accessible documentation because their bytecode is not written to disk.
