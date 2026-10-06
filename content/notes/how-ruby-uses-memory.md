---
title: "How Ruby Uses Memory"
date: '2015-05-11T16:02:40-03:00'
category: webclip
summary: 'The article explains how Ruby memory use grows through object retention, object creation hotspots, and heap growth, and shows when freezing or in-place changes can cut allocations and speed code up.'
tags: ["ruby", "memory", "garbage-collection", "performance"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How Ruby Uses Memory"
    url: "http://www.sitepoint.com/ruby-uses-memory/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-05/sitepoint-com--how-ruby-uses-memory.md"
    kind: repo
---

Ruby memory use rises when objects stay referenced and cannot be garbage collected. Constants, globals, modules, and classes can keep objects alive, while short-lived objects disappear after use. Because Ruby allocates memory in larger chunks, bursts of object creation can raise a process’s footprint even when many objects are later freed.

## Reading notes

- Objects held by globally accessible references stay alive and are not garbage collected.
- Retaining a frozen string lets Ruby reuse one object instead of creating many copies.
- Short-lived code paths still create many intermediate objects, which can add pressure on GC.
- Ruby grows its heap in larger chunks, so a spike in allocations can leave the process using more RAM.
- In-place modification can reduce allocations in hotspots, but it can also create hard-to-find bugs if state is shared.
- Memory use can be measured and investigated with tools such as get_process_mem, benchmark-ips, derailed_benchmarks, allocation_tracer, and memory_profiler.
- Ruby does release memory gradually, but the article recommends reducing object creation in hot paths instead of relying on that release.
