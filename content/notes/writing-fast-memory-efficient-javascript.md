---
title: "Writing Fast, Memory-Efficient JavaScript"
date: '2012-11-06T11:22:28-03:00'
category: webclip
summary: 'The article explains how V8 and garbage collection affect JavaScript performance, then gives practical rules for objects, arrays, closures, timers, DOM work, benchmarking, profiling, and leak detection.'
tags: ["javascript", "optimization", "performance"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Writing Fast, Memory-Efficient JavaScript | Smashing Coding"
    url: "http://coding.smashingmagazine.com/2012/11/05/writing-fast-memory-efficient-javascript/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-11/coding-smashingmagazine-com--writing-fast-memory-efficient-javascript.md"
    kind: repo
---

The article explains that JavaScript performance depends on how engines such as V8 optimize code and manage memory. It focuses on practical habits that help hot code stay fast, reduce garbage collection pressure, and avoid patterns that slow objects and arrays down.

## Reading notes

- V8 uses a base compiler, hidden classes, a runtime profiler, an optimizing compiler, deoptimization, and garbage collection.
- Garbage collection reclaims objects that are no longer reachable, and local scope helps objects become collectible sooner.
- `delete` can change an object’s hidden class and make it slower.
- Setting a reference to `null` only clears that reference; it does not clear the object itself.
- Global variables stay alive for the life of the page.
- Event listeners should be unbound when they are no longer needed.
- Cached data should be cleaned up or aged out when it is no longer useful.
- Returning an object from a function keeps it reachable after the function returns.
- Closures keep access to outer scope, so captured values remain alive as long as the inner function is reachable.
- Closures used in `setTimeout` and `setInterval` can keep references alive until they run.
- Micro-benchmarks can be misleading, so optimizations should be tested in real code.
- The article compares a naive table-building module with versions that use `DocumentFragment`, native DOM methods, delegation, prototypes, and templates.
- In the example, `DocumentFragment` and event delegation give measurable gains, while prototypes and templating do not add much performance.
- V8 prefers monomorphic functions, short prototype chains for hot objects, and avoiding large functions.
- Arrays should not mix many types, should avoid holes, and should usually grow instead of being pre-allocated in large sizes.
- Objects are better for named properties; arrays are better for ordered numeric data.
- Copying big objects is slow, and explicit copy constructors are suggested when copying is unavoidable.
- Caching functions in the module pattern can improve iteration performance.
- Benchmarking should use careful timing and account for garbage collection.
- Profiling with Chrome Developer Tools helps identify CPU and memory hot spots.
- Heap snapshots and the three-snapshot technique help find memory leaks.
- Single-page applications need explicit cleanup of old views, listeners, and references.
- Reflows should be minimized by batching DOM writes and using `DocumentFragment`.
- Leak Finder, V8 flags, High Resolution Time, Navigation Timing, `about:memory`, and `about:tracing` are presented as tools for debugging and measurement.
- The conclusion says there is no single fix; real gains come from combining measurements, understanding, and targeted fixes.
