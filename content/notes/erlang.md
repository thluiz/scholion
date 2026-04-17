---
title: Erlang
date: '2026-04-04T09:13:51+01:00'
summary: Erlang is a concurrent, functional programming language created by Joe Armstrong, Robert Virding, and Mike Williams at Ericsson in 1986 to improve the development of telephony applications. It was…
tags: ["programming-languages", "functional", "concurrency"]
has_commentary: true
sources:
- title: Erlang — Wikipedia
  url: https://en.wikipedia.org/wiki/Erlang_(programming_language
  kind: wiki
---

Erlang is a concurrent, functional programming language created by Joe Armstrong, Robert Virding, and Mike Williams at Ericsson in 1986 to improve the development of telephony applications. It was released as open-source in 1998.

The language was designed for systems that need to be distributed, fault-tolerant, and available without downtime. Its concurrency model is based on lightweight processes that communicate via message passing (the actor model) — a single node can run millions of them.

Error handling follows the "let it crash" philosophy: when a process fails, it exits cleanly and notifies a supervisor, which can restart it. These supervision hierarchies can nest to arbitrary depths, providing highly resilient systems.

Erlang runs on the BEAM virtual machine, which also hosts Elixir and other languages.
