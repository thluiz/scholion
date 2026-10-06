---
title: "Simple Sliding Windows in Elixir"
date: '2015-05-21T19:40:41-03:00'
category: webclip
summary: 'The post builds sized and timed sliding windows in Elixir, then refactors them behind a Windowable protocol and Enumerable implementations so both types share a common API.'
tags: ["elixir", "erlang", "data-structure", "protocols"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Simple Sliding Windows in Elixir"
    url: "http://blog.jonharrington.org/simple-sliding-windows-in-elixir/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-05/blog-jonharrington-org--simple-sliding-windows-in-elixir.md"
    kind: repo
---

The post first sketches two sliding-window structures in Elixir: a sized window that drops the oldest item after a fixed capacity, and a timed window that drops items based on a time threshold chosen by the user. Both start with a queue-based internal implementation and simple tests that define the interface.

## Reading notes

- The author wanted a sliding window data structure for research and used the exercise to learn custom data structures in Elixir.
- The first version is a sized sliding window that keeps a fixed number of items and pushes out the oldest item when the limit is reached.
- The implementation is based on Erlang's queue data structure because the window behaves like a FIFO queue.
- The early API is awkward because users need to know that the window stores data in a queue internally.
- The timed sliding window works like the sized one, but items are removed according to a time value rather than a size limit.
- The meaning of time and the resolution used are left to the end user.
- The author notes that the timed version also exposes the internal queue too directly.
- The refactor uses a protocol named Windowable with two functions: add and items.
- The Window module exposes constructors for sized and timed windows and delegates add to the protocol.
- Window.Sized and Window.Timed each get a Windowable implementation so they can hide their internal queue and still return their contents.
- The two window types also implement Enumerable so standard Elixir functions can work on them.
- The conclusion says structures and protocols provide reusable abstractions without classes, interfaces, or inheritance.
