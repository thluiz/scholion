---
title: "Asynchronous Programming"
date: '2026-09-25T08:55:21+01:00'
category: webclip
summary: 'The page collects guidance for writing asynchronous code in .NET and ASP.NET Core. It emphasizes that async should propagate through the call stack, and it warns against blocking patterns, fire-and-forget mistakes, and misuse of task and cancellation APIs.'
tags: ["async-await","dotnet","aspnet-core","threading"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "AspNetCoreDiagnosticScenarios/AsyncGuidance.md at master · davidfowl/AspNetCoreDiagnosticScenarios"
    url: "https://github.com/davidfowl/AspNetCoreDiagnosticScenarios/blob/master/AsyncGuidance.md?utm_source=newsletter.csharpdigest.net&utm_medium=newsletter&utm_campaign=asynchronous-programming&_bhlid=98378ffc763df38b8ee3294e51ad1b1a24a08533"
    kind: repo
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/github-com--asynchronous-programming-aspnetcore-diagnostic-scenarios.md"
    kind: repo
---

The page collects guidance for writing asynchronous code in .NET and ASP.NET Core. It emphasizes that async should propagate through the call stack, and it warns against blocking patterns, fire-and-forget mistakes, and misuse of task and cancellation APIs.

It also covers lower-level scenarios such as timer callbacks, concurrent dictionary caching, constructors, impersonation, and AsyncLocal usage, including cases where execution context capture can cause leaks or unexpected behavior.

## Reading notes

- Once a code path becomes async, the callers should also be async, because partial asynchrony can be worse than staying synchronous.
- `async void` is always bad in ASP.NET Core because exceptions can crash the process and the method cannot be tracked.
- For precomputed or trivial results, `Task.FromResult` is preferred over `Task.Run`; `ValueTask<T>` can avoid the allocation entirely.
- `Task.Run` should not be used for long-running blocking work, because it steals a thread-pool thread; a dedicated thread or `TaskCreationOptions.LongRunning` is preferred.
- `Task.Result` and `Task.Wait` should generally be avoided because they cause sync over async, thread-pool starvation, and can deadlock in some application models.
- `await` is preferred over `ContinueWith`, which behaves differently because it does not capture `SynchronizationContext`.
- `TaskCompletionSource<T>` should be created with `TaskCreationOptions.RunContinuationsAsynchronously` so continuations do not run inline on the thread that completes the task.
- `CancellationTokenSource` instances used for timeouts should be disposed so their timers do not stay in the queue.
- `CancellationToken` values should be passed through to APIs that accept them so cancellation works across the whole call chain.
- For uncancellable operations, `Task.WaitAsync` is preferred on .NET 6 or newer; older patterns use `Task.WhenAny`, `CancellationTokenRegistration`, or timeout tasks.
- `StreamWriter` and `Stream` should be flushed asynchronously before disposal, or disposed with `DisposeAsync`, to avoid synchronous blocking on buffered output.
- Returning a `Task` directly is faster, but `async`/`await` normalizes exceptions, improves diagnostics, and avoids leaking async locals out of the method.
- `AsyncLocal<T>` is powerful but risky because it flows through execution context; values should be immutable, thread-safe, and preferably non-disposable.
- APIs such as `Timer`, `CancellationToken.Register`, `Task.Run`, and `ThreadPool.QueueUserWorkItem` can capture execution context and keep async-local data alive longer than intended.
- Using `CancellationToken.UnsafeRegister` avoids capturing execution context and can reduce memory leaks caused by async locals.
- Setting `AsyncLocal<T>` values outside async methods can let mutations propagate unexpectedly; async methods restore the original execution context on exit.
- `Timer` callbacks should not be implemented with `async void` or with blocking waits; the page shows discarded `Task` callbacks and `PeriodicTimer` as alternatives.
- `ConcurrentDictionary.GetOrAdd` can cause thread-pool starvation if the value factory blocks on async work; storing a `Task<T>` or an `AsyncLazy<T>` is preferred.
- Constructors are synchronous, so asynchronous initialization should be moved to a factory method such as `CreateAsync`.
- `WindowsIdentity.RunImpersonatedAsync` is the recommended way to combine impersonation with asynchronous work in .NET 5 or newer.
