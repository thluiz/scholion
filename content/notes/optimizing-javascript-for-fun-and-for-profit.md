---
title: "Optimizing Javascript for fun and for profit"
date: '2026-09-25T20:35:23+01:00'
category: webclip
summary: 'The page collects practical JavaScript optimization habits: avoid unnecessary work, string comparisons, shape changes, indirection, cache misses, large objects, and weak data structures, while insisting that benchmarking and profiling come first.'
tags: ["javascript-optimization", "benchmarking", "profiling", "data-structures"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Optimizing Javascript for fun and for profit"
    url: "https://romgrk.com/posts/optimizing-javascript"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/romgrk-com--optimizing-javascript-for-fun-and-for-profit.md"
    kind: repo
---

The page lists common ways to make JavaScript faster, but keeps returning to the same condition: measure first. It says performance often trades off with readability, so optimization should start with benchmarking and with the hottest part of the runtime, not with isolated micro-benchmarks.

## Reading notes

- Avoid doing work at all when memoization, laziness, or incremental computation can remove it.
- Prefer integers over string-based enums, since string comparisons can be costly.
- Keep object shapes consistent so engines can stay monomorphic instead of becoming polymorphic or megamorphic.
- Avoid array and object methods that allocate extra copies when an imperative loop can do the job.
- Reduce indirection from proxies, deep property chains, and function calls that may not be inlined.
- Keep memory access sequential and keep the working set small so caches are used better.
- Avoid large objects that push engines toward hashmap-like behavior and worsen access patterns.
- Use `eval()` or generated code only when it removes a pattern that engines struggle to optimize, while keeping the usual security warnings in mind.
- Use strings carefully, because concatenation and slicing can be cheap until mutation forces copies.
- Specialize code for the conditions that are actually common in the workload.
- Choose data structures that match the task, since that can matter more than smaller optimizations.
- Benchmark in production-like conditions, distrust dramatic speedups, and pick the engine that matters for the target environment.
- Profiling tools can be distorted by browser extensions, sampling limits, and engine-specific behavior, so the setup matters.
