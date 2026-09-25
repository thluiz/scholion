---
title: "Performance Improvements in .NET 9"
date: '2026-09-25T07:57:45+01:00'
category: webclip
summary: 'A release tour of .NET 9 performance work across the JIT, GC, runtime, libraries, and tooling, with benchmarked gains in casts, loops, bounds checks, vectorization, LINQ, regex, JSON, networking, and more.'
tags: ["dotnet","performance","jit","runtime"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Performance Improvements in .NET 9"
    url: "https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-9/?_bhlid=19677f8720c25fb16cce66e0ac29aa1f1cb4c9af"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/devblogs-microsoft-com--performance-improvements-in-net-9.md"
    kind: repo
---

The post surveys performance work in .NET 9 across the stack. It highlights JIT changes such as dynamic PGO for casts and lengths, tier 0 boxing fixes, loop and bounds-check optimizations, stronger branch reasoning, and new AVX512, Arm64, and SVE code generation. It also covers GC, threading, reflection, Native AOT, and many library updates that reduce allocation, remove unnecessary work, and improve throughput.

## Reading notes

- The text says that .NET 9 brings together more than 350 pull requests focused on performance, with improvements in JIT, GC, VM, Mono, Native AOT, reflection, numerics, strings, LINQ, compression, cryptography, networking, JSON, and diagnostics.
- In the JIT, the post highlights dynamic PGO to optimize common casts and sizes, as well as changes that reduce boxing in tier 0 and improve loops, bounds checks, branches, inlining, and operations with `Nullable<T>`.
- In vector code and intrinsics, the text points to support for SVE and AVX10.1, improvements in AVX512, new instructions, and changes that speed up `SearchValues`, `TensorPrimitives`, `BigInteger`, `Base64`, `Hex`, `BitArray`, `Quaternion`, and other numerical routines.
- The post reports that server-mode GC now uses DATAS by default, that there is less cost in write barriers, and that there were changes to reduce allocations in several runtime and base library routines.
- In reflection and metaprogramming, the text shows gains in `Delegate.EnumerateInvocationList`, `ActivatorUtilities.CreateInstance`, `FieldInfo`, `UnsafeAccessor`, `Type.GetType`, `Enum.Parse`, and `JsonSerializer` with cheaper enumeration and caches.
- In LINQ, the text describes a major internal reorganization of iterators, with less interface dispatch, new shortcuts for arrays and lists, improvements in `ToArray`, `ToList`, `ToDictionary`, `OrderBy`, `GroupBy`, `Distinct`, `Union`, `Any`, `First`, `Single`, `SequenceEqual`, `Chunk`, and `DefaultIfEmpty`.
- In strings, spans, and regex, the post highlights `SearchValues<string>`, `IndexOfAny`, `ContainsAny`, `EndsWith`, `Split` over spans, `Regex.EnumerateSplits`, and broader use of vectorization for searches and comparisons.
- In networking, the text mentions gains in `SslStream`, TLS handshake, resumption, HTTP/1.1 connection pooling, `HttpClient`, `WebUtility`, `HttpUtility`, `WebSocket`, and `Uri`, as well as new APIs for `JsonSerializer` over `PipeWriter`.
- At the end, the author explains that they write these posts to learn, test, thank contributors, share free performance gains, and show techniques that readers can apply in their own code.
