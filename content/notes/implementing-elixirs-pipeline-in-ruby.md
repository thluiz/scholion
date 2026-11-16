---
title: "Implementing Elixir's Pipeline in Ruby"
date: '2026-11-16T20:10:11+00:00'
category: webclip
summary: 'Author experiments with a Ruby `pipeline` method inspired by Elixir’s `|>` operator, using Procs and Method objects while warning against monkey‑patching Object.'
tags: ["ruby", "elixir", "functional-programming"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Implementing Elixir's Pipeline in Ruby"
    url: "https://devonestes.com/implementing-elixirs-pipeline-in-ruby"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/devonestes-com--implementing-elixirs-pipeline-in-ruby.md"
    kind: repo
---

The author describes their appreciation for Elixir’s pipeline operator `|>` and attempts to recreate similar behavior in Ruby as a thought experiment. Since Ruby does not allow defining a `|>` method and monkey‑patching `Object` is considered dangerous, they introduce a `pipeline` method that accepts `Proc`, `Method`, or `UnboundMethod` objects, enabling function chaining and data transformation without being tied to collections.

## Reading notes

- Elixir’s pipeline operator `|>` passes the result of an expression as the first argument to the next function, enabling chained transformations.
- The author has been adopting functional paradigms in Ruby to improve testability and reduce complexity, which motivated trying to implement a pipeline operator.
- An attempt to define a Ruby method named `|>` fails because the Ruby interpreter treats `>` as a syntax error in that context.
- Since `|>` is unavailable, the author chooses a `pipeline` method name; `pipe` already exists on `IO`, and `pipeline` is not an instance method in the standard library or core.
- The initial implementation monkey‑patches `Object#pipeline`, warning that this is a bad idea for larger or more complex apps.
- `pipeline` takes a splat of arguments, shifts the first into `func`, and determines how to call it based on whether it is a `Proc`, `Method`, or `UnboundMethod`.
- For `Proc` or `Method`, `pipeline` calls the function with `self` as the first argument followed by any remaining arguments.
- For an `UnboundMethod`, `pipeline` binds it to `self` before calling it with the remaining arguments.
- If the first argument to `pipeline` is none of these types, it raises a `NotImplementedError` indicating the function type is not yet supported.
- As a safer alternative to monkey‑patching `Object`, the same `pipeline` implementation can be placed in a `Pipeable` module and included selectively in specific classes such as `String`.
- Using this approach, the author demonstrates chaining a string through an `UnboundMethod` for `String#upcase`, a `Proc` that formats a message, and a `Method` object created via `method(:puts)`.
- The example shows `pipeline` successively transforming `'nine thousand'` into an uppercased string and then interpolating it into a message printed with `puts`.
- The author expresses a desire to use Elixir‑style syntax (`|> func1 |> func2 |> func3`) but avoids modifying the Ruby interpreter itself.
- They chose `Proc`, `Method`, and `UnboundMethod` because Ruby commonly uses `to_proc` and `&method` for passing functions around, and these objects fit that convention.
- `UnboundMethod` is included partly because the author finds it appealing and useful to bind methods to specific receivers later.
- The author notes that Ruby already has many chainable methods, often through `Enumerable`, which primarily targets collections such as arrays and hashes.
- In contrast, the `pipeline` method is presented as a more generic mechanism for chaining behavior without assuming iteration over a collection.
