---
title: "Simple and Clean Code vs. Performance"
date: '2015-04-01T11:08:12-03:00'
category: webclip
summary: 'The article argues that simple, clean code should be the default. It separates efficiency from performance, says most code is not a bottleneck, and recommends profiling before sacrificing readability.'
tags: ["code-readability", "performance", "profiling", "data-structures"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Simple and Clean Code vs. Performance"
    url: "http://arne-mertz.de/2015/03/simple-and-clean-code-vs-performance/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-04/arne-mertz-de--simple-and-clean-code-vs-performance.md"
    kind: repo
---

Write readable and simple code by default. The article argues that efficiency and performance are different, that most code is not where runtime is spent, and that maintainability should come first unless profiling shows a real problem.

## Reading notes

- Efficiency is about doing less work, while performance is about doing work faster.
- Before trying to squeeze more speed from code, first check whether the algorithm is efficient.
- Most code does not matter much for total runtime, so optimizing it often has little effect.
- If code is not a proven bottleneck, it should not be optimized for speed.
- Programmers usually cannot predict well which code will perform best, because compilers and optimizers change a lot.
- If performance really matters, use a profiler instead of relying on guesswork.
- When two versions are equally readable, choose the one that probably performs better.
- Data layout and data structures can matter more than small instruction-level changes.
- Using well-written libraries can improve both simplicity and performance.
- Simple code should be sacrificed for performance only as a last resort.
