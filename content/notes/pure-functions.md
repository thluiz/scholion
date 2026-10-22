---
title: "Pure functions"
date: '2021-07-20T16:53:31-03:00'
category: webclip
summary: 'A pure function is deterministic and has no side effects. The post explains how mutable state, input streams, argument mutation, and output streams break purity, and why isolation matters.'
tags: ["pure-functions", "determinism", "side-effects"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Pure functions | Compositional IT"
    url: "https://www.compositional-it.com/news-blog/pure-functions/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2021-07/compositional-it-com--pure-functions.md"
    kind: repo
---

A pure function is one that returns the same output for the same arguments and does not cause side effects. The post explains purity through determinism, side effects, and the idea that a pure function is isolated from the rest of the program.

## Reading notes

- A function is deterministic when repeated calls with the same arguments produce the same output.
- A function can be non-deterministic if it depends on a non-local mutable variable.
- A mutable parameter can also make a function non-deterministic, while an immutable input like a list keeps it deterministic.
- Reading from an input stream makes a function non-deterministic because the input can change between calls.
- A side effect is any change a function makes beyond returning a value.
- Mutating a non-local variable is a side effect.
- Mutating an argument is also a side effect.
- Writing to stdout is a side effect, and the post notes that saving to a database or sending an email are similar examples.
- A pure function has only direct input and output, with no indirect input or output.
- The post says isolation is stronger than simply avoiding indirect input and output, because the arguments must also be immutable.
