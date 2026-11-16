---
title: "How Do I Think About Async Code?!"
date: '2020-07-05T14:10:35+00:00'
category: webclip
summary: 'The post explains async programming as a way to keep work moving without blocking a thread, shows it with a cake example, and points to Task, async, and await in C#.'
tags: ["async-programming", "csharp", "dotnet", "responsive-applications"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How Do I Think About Async Code?!"
    url: "https://devblogs.microsoft.com/visualstudio/how-do-i-think-about-async-code"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/devblogs-microsoft-com--how-do-i-think-about-async-code.md"
    kind: repo
---

Async programming lets code keep doing other work while one task is waiting, instead of blocking the whole thread. The post says its main benefit is higher throughput, not necessarily better performance, and notes that async can be used in single-threaded or multithreaded programs.

The article uses a cake example to compare synchronous and asynchronous flow. In the async version, a method can save a task’s state, do other work, and return to the awaited result when needed. It also says C# uses Task, async, and await to write async code, and gives HTTP requests and UI apps as common uses.

## Reading notes

- Async programming lets a method wait for a task without blocking the entire thread.
- The main benefit described is more concurrent throughput, not automatic performance gains.
- Async code can work in single-threaded programs or in multithreaded ones.
- The cake example shows that synchronous code waits on each step in sequence.
- The async version can do other work while it waits for baking or another task to finish.
- The method named PassTheTime saves task state, runs other code, and retrieves the value later.
- In C#, Task, async, and await are the basic tools for async code.
- An async method runs synchronously until it reaches an await keyword.
- HTTP requests are one common case where async code helps because responses may take time.
- UI programs such as WPF apps can stay responsive while an operation runs in the background.
