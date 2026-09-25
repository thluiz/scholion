---
title: "A crash course in memory management"
date: '2026-09-25T09:05:28+01:00'
category: webclip
summary: 'Explains memory as fixed-size boxes with addresses, contrasts JavaScript’s automatic garbage collection with manual allocation and freeing in C, and links that tradeoff to performance and bugs.'
tags: ["memory-management","javascript","garbage-collection","webassembly"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "A crash course in memory management – Mozilla Hacks - the Web developer blog"
    url: "https://hacks.mozilla.org/2017/06/a-crash-course-in-memory-management/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/hacks-mozilla-org--a-crash-course-in-memory-management.md"
    kind: repo
---

The article explains memory as fixed-size boxes with addresses and uses that model to show how JavaScript engines allocate values, track reachability, and reclaim memory through garbage collection. It contrasts that automatic management with C-style manual memory management, where developers use malloc and free and must decide when memory can be released.

It says automatic memory management reduces developer burden but adds overhead and can make performance unpredictable. Manual memory management gives more direct control, but mistakes can cause bugs, security holes, or running out of memory. The article frames this tradeoff as part of the background for ArrayBuffer and SharedArrayBuffer in JavaScript.

## Reading notes

- Presents memory as same-sized boxes, each with an address, to explain where data is stored.
- Shows that numbers go directly into memory in binary, while letters and other characters need encoding and decoding.
- Explains that, in JavaScript, the engine handles memory allocation and tracks whether a value can still be reached in the program.
- Defines garbage collection as the process of freeing memory for values that can no longer be reached.
- Says languages with this model are memory-managed languages and that this makes the developer's work easier, although it adds overhead.
- Compares with C and WebAssembly, where memory is handled directly and the execution environment includes auxiliary code for encoding and decoding bytes.
- States that, in manual management, the runtime can keep a free list, and that malloc and free are used to request and return memory.
- Points out that deciding when to free memory is difficult and that mistakes in this decision can generate bugs, security failures, or lack of memory.
- Connects this cost and difficulty to the reason many modern languages prefer automatic management.
