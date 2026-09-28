---
title: "Memoization in JavaScript"
date: '2022-05-03T09:45:35-03:00'
category: webclip
summary: 'The article introduces memoization as a speed optimization technique that caches results for repeated inputs, then shows a simple `myMemoize()` wrapper for reusing computed outputs and optionally binding context.'
tags: ["memoization", "javascript", "performance-optimization"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Memoization in JavaScript"
    url: "https://parthasarma.hashnode.dev/memoization-in-javascript"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-05/parthasarma-hashnode-dev--memoization-in-javascript.md"
    kind: repo
---

The article explains memoization as a way to avoid repeating expensive calculations when a function receives the same inputs again. It uses a slow multiplication example to show that the second call can reuse a cached result instead of running the function body again.

## Reading notes

- Memoization returns a cached output when the same inputs are used again.
- The example wraps `slowProduct()` in `myMemoize()` and stores the memoized function in `memoizedProduct`.
- `myMemoize()` keeps results in an object keyed by `JSON.stringify(args)`.
- When a key is missing, it calls the original function, stores the result, and returns it.
- The complete example shows the second call reusing the stored value instead of recalculating.
- A later change lets `myMemoize()` accept an optional context and uses `fn.call(context || this, ...args)`.
- The conclusion says memoization can improve performance and can be combined with other optimizations.
