---
title: "Elixir Stream Patterns"
date: '2015-05-07T13:16:40-03:00'
category: webclip
summary: 'The post surveys how Streams are used in Elixir code, comparing them with Enum and other constructs, and argues for choosing the clearest form while using lazy evaluation only where it saves work.'
tags: ["elixir", "streams", "enum", "lazy-evaluation"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Elixir Stream Patterns"
    url: "http://learningelixir.joekain.com/stream-patterns-in-elixir/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-05/learningelixir-joekain-com--elixir-stream-patterns.md"
    kind: repo
---

The post looks at several Elixir examples and notes that Streams are not widely used. It compares Stream-based code with ranges, comprehensions, and Enum-based alternatives, and favors the clearest expression for the task.

## Reading notes

- Bmark uses `Stream.repeatedly/1` with `Stream.take/1` to run a function multiple times without a mutable counter.
- That pattern suggests the function can produce different results on repeated calls.
- Using a range with `map` requires wrapping a zero-arity function, which reduces readability.
- A comprehension is presented as a cleaner alternative to `Stream.repeatedly(f) |> Stream.take(count)`.
- ExUnit’s `ExUnit.DocTest` uses `Stream.filter` and `Stream.with_index` in a pipeline that ends with `Enum.map`.
- The post questions why `Stream` is used there instead of `Enum`, since `Enum.map` eagerly consumes the result.
- In `Mix.Utils`, `stale_stream` feeds both `stale?` and `extract_stale`.
- `stale?` can stop early with `Enum.any`, while `extract_stale` needs the full list of stale files.
- That example shows how lazy evaluation can save work when only the first matching element matters.
- The closing advice is to experiment with Elixir’s syntax and choose the most expressive form for the code at hand.
