---
title: "Elixir Processes: Observability"
date: '2026-11-16T03:50:57+00:00'
category: webclip
summary: 'The article shows how Elixir exposes process internals through built-in tools in IEx. It covers finding PIDs, inspecting process data, and using `:sys` helpers to read or replace GenServer state and gather statistics.'
tags: ["elixir", "processes", "observability", "iex"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Elixir Processes: Observability"
    url: "https://samuelmullen.com/articles/elixir-processes-observability"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/samuelmullen-com--elixir-processes-observability.md"
    kind: repo
---

The article argues that Elixir makes process observability much easier than in most programming languages because key process details are built in and available from IEx. It focuses on practical ways to inspect live systems by finding processes, reading their internal data, and using `:sys` tools with GenServers.

## Reading notes

- Elixir lets you answer questions about a process’s memory use, child processes, and internal state with a few keystrokes.
- In practice, these tools are often used from the REPL, either during development or by connecting a console to a running app.
- A process can be identified by name, PID, or reference, and IEx helpers like `pid/1,3`, `ref/1,4`, and `v/1` help recover values during exploration.
- `Process.whereis/1` returns the PID of a registered process name when the name is known.
- `Process.list/0` returns all running PIDs and can be combined with `Process.info(pid, :registered_name)` to find named processes.
- When a process is not obvious, linked or monitored processes can help narrow the search.
- `Process.info/1,2` returns detailed process information, including links, memory, mailbox size, messages, observed processes, registered name, status, and reductions.
- The article recommends requesting only the fields you need when using `Process.info/2`.
- `:sys.get_state/1` returns the current state of a GenServer.
- `:sys.replace_state/2` replaces a GenServer state through a function and is presented as a debugging-only tool.
- `:sys.statistics/2,3` can track reductions and message counts for a GenServer after statistics are enabled.
- The example with `Logger` shows reductions rising and `messages_in` increasing after a log call.
- A sample `Beholder` module wraps `Process.info` and `Process.whereis` to inspect processes, list named PIDs, and sort processes by memory use.
- The article suggests extending such tooling with filters, thresholds, rate checks, color coding, mailbox checks, and limited process graphs.
- The conclusion presents Elixir’s observability as a built-in advantage inherited from Erlang, especially through `Process`, `:sys`, and live console access.
