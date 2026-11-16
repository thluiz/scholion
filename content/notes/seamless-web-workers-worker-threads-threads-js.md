---
title: "Seamless web workers & worker threads - threads.js"
date: '2026-11-16T19:23:00+00:00'
category: webclip
summary: 'threads.js v1.0 offers a transparent API for web workers and worker threads, with promise-based calls, error handling, Node.js support, webpack integration, and TypeScript support.'
tags: ["web-workers", "worker-threads", "typescript", "webpack"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Seamless web workers & worker threads - threads.js"
    url: "https://dev.to/andywer/seamless-web-workers-worker-threads-threads-js-2g36"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--seamless-web-workers-worker-threads-threads-js.md"
    kind: repo
---

threads.js v1.0 is presented as a small library for using web workers and worker threads through a transparent API. The post says it works in browsers and in Node.js, offers thread pools, and keeps worker communication simple by exposing functions from the worker and calling them from the main thread.

It also shows that worker calls always return promises, which makes error handling straightforward. The article adds that the library can run in Node.js with worker threads or a tiny-worker polyfill, can be bundled with webpack through threads-plugin, and has TypeScript support that can fall back to ts-node when needed.

## Reading notes

- The post introduces threads.js v1.0 after beta and describes it as a small cross-platform library for workers.
- It highlights workers for CPU-bound tasks, keeping non-rendering code off the main thread, and isolating modules through message passing.
- The API exposes worker functions and lets the main thread call them as if they were regular methods.
- Calls like `auth.hashPassword()` always return a promise, even when the original worker function is not async.
- Error handling uses standard promise `try` / `catch` blocks around spawning and method calls.
- `Thread.terminate()` is used to stop a worker when it is no longer needed.
- In Node.js, the same code can run with worker threads support, or with `tiny-worker` as a polyfill on older versions.
- For webpack, the `threads-plugin` recognizes `new Worker()` and bundles worker files separately from the main entrypoint.
- TypeScript workers can be loaded as transpiled JavaScript, or via `ts-node` if that is available and the JavaScript build is missing.
- The post also mentions thread pools, observables, transferable objects, and more planned features.
