---
title: "Let's try to scale an API"
date: '2020-07-05T14:11:24+00:00'
category: webclip
summary: 'The article shows how a Node.js API that finds the highest prime in a range gets faster with cluster mode, a sieve-based algorithm, and caching, using load test results to compare each step.'
tags: ["nodejs", "api-scaling", "concurrency", "caching"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Let's try to scale an API"
    url: "https://dev.to/ashokdey_/building-a-scalable-system-4l41"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--lets-try-to-scale-an-api.md"
    kind: repo
---

The article uses a single GET endpoint that returns the highest prime between 0 and N to show practical ways to speed up a server. It starts with a brute-force approach, then adds cluster mode for concurrency, then replaces the algorithm with a modified Sieve of Eratosthenes, and finally adds caching.

It compares load testing results for each version. The brute-force implementation is slow on large inputs, cluster mode helps concurrent requests, the sieve reduces the computation time, and cache makes repeated requests faster. The main takeaway is that performance improves when concurrency, algorithm choice, and memoization are combined.

## Reading notes

- The example server exposes one GET route that returns the highest prime number between 0 and N.
- A brute-force prime search works for small values but becomes slow on large inputs.
- When a large request is running, another request can wait behind it in the same process.
- Cluster mode is used to run the app concurrently across available CPU threads.
- The article reports that cluster mode makes smaller requests return while a heavier one is still computing.
- The prime calculation is improved with a modified Sieve of Eratosthenes.
- The load test numbers show the brute-force version taking 187.492294273 seconds for num=20234456.
- The sieve-based version reduces that time to 32.284605092999996 seconds for the same input.
- A plain JavaScript object is used as a cache to store results for a given N.
- The article notes that Redis would do a better job for caching.
- With cache, the brute-force version drops to 47.291413455000004 seconds in the load test.
- With the sieve and cache together, the load test drops to 31.047955697999996 seconds.
- The article frames multithreading, algorithms, and caching as the main performance improvements.
