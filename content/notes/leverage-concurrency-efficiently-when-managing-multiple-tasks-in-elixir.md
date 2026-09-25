---
title: "Leverage Concurrency Efficiently When Managing Multiple Tasks in Elixir"
date: "2026-09-23T18:37:23+01:00"
category: webclip
has_commentary: false
summary: "Builds from Task.start and Task.async to Task.async_stream, showing why one process per item breaks at scale and how max_concurrency, ordering, and timeouts trade off against each other."
tags:
  - elixir
  - concurrency
  - task-module
  - backpressure
sources:
  - title: "Leverage Concurrency Efficiently When Managing Multiple Tasks in Elixir"
    url: "https://blog.appsignal.com/2024/06/25/leverage-concurrency-efficiently-when-managing-multiple-tasks-in-elixir.html?utm_source=elixir-alchemy&utm_medium=email&utm_campaign=2024-07-03"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/blog-appsignal-com--leverage-concurrency-efficiently-when-managing-multiple-tasks-in-elixir.md"
    kind: repo
---

Walks through Elixir's Task module for running work concurrently, building from Task.start/1 up to Task.async_stream/3. Spawning an unbounded process per item works at small scale but breaks down at scale: the piece pushes a demo to a million phone numbers and hits Erlang's default process limit around 262,144, then shows that raising the limit trades the crash for a memory spike instead of fixing the underlying problem.

Task.async_stream/3 is the fix. It processes an enumerable concurrently while bounding how many processes run at once, closing the gap between Task.start/1 (fire-and-forget, no result) and Task.async/1 combined with Enum.map/2 (gets the result, but spawns one process per item with no ceiling).

## Reading notes

- Task.start/1 fires a process and returns {:ok, pid} without the function's own result. It fits background jobs that track completion elsewhere, such as a status column in a database, not work that needs its return value read back.
- Task.async/1 returns a %Task{} struct. Task.await/2 retrieves the result and raises past the 5-second default timeout; Task.yield/2 returns nil instead of crashing the caller.
- Combining Enum.map/2 with Task.async/1 to fan out one process per item hits Erlang's default 262,144 process limit around a million tasks. Raising the limit with +P avoids the crash but produces a memory spike.
- Task.async_stream/3 bounds concurrency through :max_concurrency, which defaults to the number of logical cores on the machine.
- :ordered defaults to true and returns results in input order, which means the whole stream waits on the slowest task; setting it to false lets faster results land as they finish.
- :timeout defaults to 5000ms and crashes the stream when a task runs past it; :on_timeout set to :kill_task drops the slow task instead and lets the rest complete.
