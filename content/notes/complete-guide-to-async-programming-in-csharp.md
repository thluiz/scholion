---
title: "A complete guide to async programming in C#: understand threading, non-blocking I/O, await behavior, and best practices with ConfigureAwait"
date: 2026-09-23T15:13:28+01:00
category: webclip
summary: "Stalin walks through what async/await does under the hood in C#, from thread pooling and await's resume point to SynchronizationContext, ConfigureAwait(false), and CancellationToken."
tags: ["csharp", "async-programming", "dotnet", "threading"]
has_commentary: false
sources:
  - title: "A complete guide to async programming in C#: understand threading, non-blocking I/O, await behavior, and best practices with ConfigureAwait"
    url: "https://medium.com/@lstalin.paul/a-complete-guide-to-async-programming-in-c-understand-threading-non-blocking-i-o-await-f3f178dc6746"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-08/medium-com--complete-guide-to-async-programming-in-csharp.md"
    kind: repo
---

A thread is the smallest unit of execution, and a long-running operation on the main thread blocks everything else until it finishes. Async I/O sidesteps that by releasing the thread back to the pool once an operation like a file read is registered with the OS, then resuming the calling code once the runtime gets notified the result is ready.

## Fichamento

- A blocking `File.ReadAllText` call ties up the thread until the file finishes reading. The async `File.ReadAllTextAsync` version frees the thread immediately and resumes the rest of the method automatically once the I/O completes.
- Calling `Task.Delay(1000);` without `await` starts the operation but returns immediately without waiting for it, a pattern the guide calls fire-and-forget.
- `SynchronizationContext` decides which thread or environment a continuation resumes on after an `await`, which matters in UI applications that need code to come back on the original thread.
- `ConfigureAwait(false)` skips resuming on the captured context. The guide recommends it for ASP.NET Core apps, background services, and console utilities that don't care which thread they resume on.
- `CancellationToken` lets a long-running async method call `token.ThrowIfCancellationRequested()` periodically and abort early instead of running to completion. The guide's example cancels a loop of five one-second delays after two seconds.
- [C#](/notes/csharp/) covers the language's own history and multi-paradigm design. This post makes the practical case for one specific piece of it, the async model built around thread pooling and continuations.
