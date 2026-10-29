---
title: "On problems with threads in node.js"
date: '2015-04-24T08:40:20-03:00'
category: webclip
summary: 'The article shows how Node.js relies on libuv’s thread pool for asynchronous work, why the default pool size can limit parallelism, and how that can block other tasks.'
tags: ["nodejs", "libuv", "thread-pool", "asynchronous-io"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "On problems with threads in node.js | Future Processing"
    url: "http://www.future-processing.pl/blog/on-problems-with-threads-in-node-js/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-04/future-processing-pl--on-problems-with-threads-in-node-js.md"
    kind: repo
---

The article argues that Node.js is single-threaded only at the JavaScript level, while asynchronous work is often handled by libuv’s thread pool. A small example with delayed directory reads shows that once the default pool of four threads is saturated, later requests wait in the queue and finish later.

## Reading notes

- JavaScript code runs on one thread, but Node.js uses threads for asynchronous work under the hood.
- The example delays scandir() with a shared library so the queueing effect becomes visible.
- libuv submits work requests with a function to run, data for that function, and a function that collects the result back on the main thread.
- The default libuv thread pool size is 4, which explains why six readdir() calls split into two waves.
- The thread pool is used mainly for file system operations and user code.
- In a database-heavy application, query execution can also consume the same pool, so slow queries can block unrelated asynchronous tasks.
- UV_THREADPOOL_SIZE can change the pool size, but only before the first work request creates the pool.
- The article ends with a bug where query termination requests failed because they were queued behind long-running queries.
