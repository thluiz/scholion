---
title: ".NET Threading Gotchas"
date: '2020-02-22T12:11:49+00:00'
category: webclip
summary: 'The article lists five common .NET threading mistakes and shows fixes: avoid synchronous async code, use ConfigureAwait carefully, choose thread-safe collections when needed, limit static state, and use Interlocked for atomic updates.'
tags: ["dotnet", "threading", "async-await", "concurrency"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: ".NET Threading Gotchas - Kill All Defects"
    url: "https://web.archive.org/web/20200808064046id_/https://killalldefects.com/2020/01/16/dotnet-threading-gotchas/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--dotnet-threading-gotchas.md"
    kind: repo
---

The article reviews five common threading mistakes in .NET applications and explains how to avoid them. It focuses on cases where developers may accidentally make threading harder or slower while trying to handle asynchronous or multi-threaded code.

## Reading notes

- Using async methods synchronously can add threading overhead without gaining parallelism, so the article recommends Task.WhenAll when the operations can run independently.
- Await resumes on the original SynchronizationContext by default, which can create delays or deadlocks in busy environments; ConfigureAwait(false) avoids that when the thread context does not matter.
- When multiple threads access the same collection, the article advises using locks or concurrent collections such as ConcurrentDictionary instead of assuming ordinary collections are safe.
- Static classes and static state are presented as risky because they can be accessed by multiple threads and can also make parallel unit tests inconsistent.
- A simple increment is not a single operation at the CLR level, so race conditions can lose updates when many threads touch the same field.
- For shared numeric state, the article recommends Interlocked methods to perform atomic updates instead of managing the field with a lock.
- The article points readers to the Async Guidance page on GitHub for more detailed threading guidance.
