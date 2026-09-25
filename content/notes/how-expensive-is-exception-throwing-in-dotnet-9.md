---
title: "How expensive is exception throwing in .NET 9?"
date: '2026-09-25T18:39:42+01:00'
category: webclip
summary: 'BenchmarkDotNet measurements on .NET 9 show that try-catch without thrown exceptions has almost no overhead, while throwing and catching an exception adds measurable time and allocation.'
tags: ["dotnet-9", "exceptions", "benchmarkdotnet"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How expensive is exception throwing in .NET 9?"
    url: "https://papers.cloudcat.dev/blogs/net-9-exception-overhead?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/papers-cloudcat-dev--how-expensive-is-exception-throwing-in-dotnet-9.md"
    kind: repo
---

The post compares try-catch usage in .NET 9 with and without thrown exceptions. It says the try-catch block itself has nearly identical execution time to code without it, but throwing and catching an exception still adds cost in time and memory.

## Reading notes

- The benchmark used a Qualcomm Snapdragon X Elite X1E-78-100, BenchmarkDotNet v0.14.0, Windows 11, and .NET SDK 9.0.101.
- TryCatch_NoError and NoTryCatch_NoError had nearly the same mean time and allocation.
- TryCatch_WithErrorOption was also close to the no-error cases.
- TryCatch_WithThrow was slower and allocated more memory than the other methods.
- The post reports about 0.002 milliseconds of overhead and 320 additional bytes when throwing and catching an exception.
- The conclusion says the overhead is minimal in most cases.
- It also says the cost can be greater in a large code base or on limited hardware.
- The post says it is still beneficial to reserve exceptions for truly exceptional situations.
- It also says the choice should be weighed against the developer time needed for graceful error handling.
