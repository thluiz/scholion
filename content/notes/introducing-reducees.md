---
title: "Introducing reducees"
date: '2015-05-29T18:07:19-03:00'
category: webclip
summary: 'The post traces Elixir’s collection-processing design from recursion to iterators, reducers, and iteratees, then explains reducees as the abstraction that keeps reduce simple, fast, and resource-safe.'
tags: ["elixir", "reducers", "iteratees", "collections"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Introducing reducees"
    url: "http://blog.plataformatec.com.br/2015/05/introducing-reducees/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-05/blog-plataformatec-com-br--introducing-reducees.md"
    kind: repo
---

Elixir’s collection story moves from manual recursion to iterators, then reducers, iteratees, and finally reducees. The post argues that reducees keep the simplicity and speed of reduce while still supporting resources, eager operations, and lazy collection processing.

## Reading notes

- Elixir collections include in-memory data structures, events, I/O resources, and more, and the Enumerable protocol is based on reducees.
- Recursing over lists works for simple cases like `double` and `map`, but it does not compose well across many data structures.
- Iterators ask a collection for the next item, which enables shared operations like `map`, but they perform poorly and make resource handling messy.
- Iterators need extra handling such as `halt` so resources can be closed when iteration stops early or fails.
- Reducers shift the traversal logic into the collection itself, which makes `reduce` the base for operations like `sum` and `map`.
- Reducers are simpler and faster, and they fit resources well because the collection can guarantee cleanup after reducing.
- The reducer model still has limits in Elixir, including difficulties with `take` in a purely functional way and with operations like `zip`.
- Iteratees send instructions back and forth between the source and the consumer, which lets them express more control, including halting.
- The post says iteratees are harder to understand and much slower in Elixir because they create a new closure for each mapped element.
- Reducees keep the reduce model but wrap the accumulator in a tuple carrying instructions such as `{:cont, acc}` and `{:halt, acc}`.
- This lets `map` and `take` work with the same reduce-based traversal while avoiding closures during iteration.
- The final abstraction in Elixir supports both in-memory data and resources, and it can handle both eager and lazy operations through `Enum` and `Stream`.
- The post ends by pointing toward asynchronous collection processing as the next step for Elixir.
