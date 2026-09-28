---
title: "Interview question: Design Twitter (Episode 5)"
date: '2022-05-05T09:33:52-03:00'
category: webclip
summary: 'The newsletter contrasts process and thread, outlines a 2013 Twitter system flow, sketches database categories by workload, and lists ID generator requirements for social platforms.'
tags: ["process", "thread", "twitter-architecture", "database-selection", "unique-id"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Interview question: Design Twitter (Episode 5)"
    url: "https://blog.bytebytego.com/p/interview-question-design-twitter?s=r"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-05/blog-bytebytego-com--interview-question-design-twitter-episode-5.md"
    kind: repo
---

The newsletter brings together four technical prompts. It defines program, process, and thread, then uses Twitter’s 2013 tech talk to sketch tweet handling, search and discovery, and push compute. It also gives a high-level guide to database categories and a short checklist for globally unique ID generation.

## Reading notes

- A program is an executable file stored on disk, a process is a program in execution, and a thread is the smallest unit of execution within a process.
- One program can have multiple processes, and a process can have one or more threads.
- Processes are independent and use their own memory space, while threads in the same process share memory.
- Process creation, termination, and context switching are heavier than the same operations for threads, and inter-thread communication is faster.
- In the Twitter flow shown here, a tweet enters through the Write API, goes to Fanout, is stored in Redis cache, and is later pulled through the Timeline service.
- Search and discovery are split across Ingester, which annotates and tokenizes tweets, Earlybird, which stores the search index, and Blender, which creates search and discovery timelines.
- Push compute covers HTTP push and mobile push.
- The database guide says the choice should match the workload and lists structured, semi-structured, and unstructured data as the starting point.
- The database categories named here are relational, columnar, key-value, in-memory, wide column, time series, immutable ledger, geospatial, graph, document, text search, and blob.
- The ID generator section lists the desired properties as globally unique, roughly time-sorted, numeric only, 64 bits, highly scalable, and low latency.
