---
title: "A Simple Example of Calling an Elixir Library from Gleam"
date: "2026-09-23T15:45:11+01:00"
category: webclip
summary: "Michael Lynch works through a minimal example of calling an Elixir CSV library from Gleam, wrapping @external attributes and converting Elixir's Enumerable into a Gleam List."
tags:
  - gleam
  - elixir
  - beam-vm
  - functional-programming
has_commentary: false
sources:
  - title: "A Simple Example of Calling an Elixir Library from Gleam · mtlynch.io"
    url: "https://mtlynch.io/notes/gleam-call-elixir/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-07/mtlynch-io--a-simple-example-of-calling-an-elixir-library-from-gleam.md"
    kind: repo
---

Michael Lynch wanted to see Gleam's flagship interop feature in action, calling an Elixir library, but couldn't find a worked example anywhere. So he built one himself: a Gleam wrapper around the Elixir `CSV` package's `encode` function, documented step by step as a beginner learning both languages at once.

The core difficulty is the type mismatch between a statically typed language and a dynamically typed one running on the same virtual machine. [Elixir](/notes/elixir/) and Gleam both compile to BEAM bytecode, so Gleam can call Elixir functions directly, but Gleam has no native concept of Elixir's `Enumerable` protocol, and the wrapper has to bridge that gap by hand.

## Reading notes

- Gleam calls Elixir code through the `@external(erlang, "Elixir.CSV", "encode")` attribute, using the `Elixir.` prefix because that's the namespace Elixir functions get compiled to on BEAM.
- `CSV.encode` takes a list of lists of strings and returns something typed as Elixir's `Enumerable`, which has no Gleam equivalent, so Lynch defines an opaque `ElixirEnumerable` placeholder type just to receive it.
- Converting that placeholder into something Gleam can actually use requires a second external call, to Elixir's `Enum.to_list`, which turns the `Enumerable` into a plain Elixir list that matches Gleam's `List` type.
- The final public wrapper is three lines: pipe the input through `csv_encode`, then through `enum_to_list`, exposing only that combined function and keeping the two low-level externals private.
- He hit a version bug immediately: `gleam new` scaffolded a `gleeunit` dependency requiring Gleam 1.11.0 while he had 1.10.0 installed, fixed by pinning `gleeunit` back to 1.3.1.
- Before writing any Gleam code, he explored `CSV.encode`'s behavior directly in `iex`, Elixir's interactive shell, since he didn't yet know Elixir's sigil syntax or the exact shape of the function's output.
