---
title: "Holier Than Thou"
date: '2015-06-07T11:37:00-03:00'
category: webclip
summary: 'The post argues that C++ free-store fragmentation is a deliberate consequence of not having a garbage collector or memory compactor, and that long-running or low-RAM programs must design around it.'
tags: ["c-plus-plus", "memory-fragmentation", "free-store", "dynamic-memory"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Holier Than Thou"
    url: "http://bulldozer00.com/2015/06/01/holier-than-thou/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-06/bulldozer00-com--holier-than-thou.md"
    kind: repo
---

The post says C++’s lack of a native garbage collector or memory compactor means repeated dynamic allocation and deallocation can leave small holes in the free store. It treats this fragmentation as a feature of the language rather than a memory leak.

It limits the practical impact to long-running programs and systems with small RAM footprints, and suggests avoiding post-initialization deletes, either by doing all allocations up front or by using fixed-size pools and stacks. If fragmented memory prevents a contiguous allocation, the runtime can throw std::bad_alloc and crash the program.

## Reading notes

- C++ deliberately does not include a native garbage collector or memory compactor.
- Dynamic allocation and deallocation can cause small holes to accumulate in the free store over time.
- This is not the same as a memory leak, which is described as a bug.
- Free-store fragmentation matters mainly for long-running programs and systems with small RAM footprints.
- One practical approach is to do all dynamic allocation during program initialization and use the CPU stack at runtime.
- Another approach is to use pre-allocated, fixed-size, unfragmentable pools and stacks for runtime buffers.
- If the free store becomes too fragmented, a new request can fail with std::bad_alloc.
- Refactoring a large system after coding and testing to reduce fragmentation is described as expensive, time consuming, and technically risky.
- The post includes a simulator that repeatedly allocates and deallocates random chunk sizes to test whether fragmentation can make a program fail.
- The author notes a long-running simulator and asks how to change the code to make it exit sooner.
