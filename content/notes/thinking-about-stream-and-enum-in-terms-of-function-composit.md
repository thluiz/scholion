---
title: "Thinking about Stream and Enum in Terms of Function Composition"
date: '2015-10-02T07:51:23-03:00'
category: webclip
summary: 'The post explains Enum and Stream as ways of composing functions in Elixir. Enum builds shortcuts on top of reduce, while Stream delays work by creating a collection-like transformation.'
tags: ["elixir", "enum", "stream", "function-composition"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Curse the Darkness: Thinking about Stream and Enum in Terms of Function Composition"
    url: "http://www.cursingthedarkness.com/2015/08/thinking-about-stream-and-enum-in-terms.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-10/cursingthedarkness-com--thinking-about-stream-and-enum-in-terms-of-function-composit.md"
    kind: repo
---

The post reads Enum and Stream as tools for function composition rather than as generalized arrays. Enum is built from a collection’s basic functions, especially reduce, and its helpers are shortcuts over that mechanism.

## Reading notes

- Enum’s basic protocol methods are count, member?, and reduce, not an each method.
- Enum uses reduce to implement higher-level operations such as all?.
- These operations can stop early when the result is already determined.
- Stream is similar, but it does not execute reduce right away.
- Stream creates an anonymous function that transforms one collection into another.
- A Stream-based collection can be used where a regular collection is used.
- The example with 1..10 mapped by Stream shows lazy evaluation when Enum.take is called.
- A collection defined by Stream does not imply state and remains immutable.
- Each use of a Stream starts from the beginning again.
- The choice to use Stream depends on the tradeoff between storing a collection and creating it at runtime.
- Stream supports reduce, but count and member? from Enumerable fail directly.
- Enum.count can emulate count by using reduce.
