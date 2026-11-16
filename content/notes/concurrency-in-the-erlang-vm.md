---
title: "Concurrency In The Erlang VM"
date: '2026-11-16T01:26:09+00:00'
category: webclip
summary: 'The page explains why Erlang is built for concurrency, using lightweight actor-like processes, message passing, and the BEAM scheduler to support fault-tolerant, distributed systems.'
tags: ["erlang", "concurrency", "beam", "actor-model"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Concurrency In The Erlang VM"
    url: "https://dev.to/imswaathik/concurrency-in-the-erlang-vm-272k"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--concurrency-in-the-erlang-vm.md"
    kind: repo
---

The page links Erlang’s relevance to its concurrency-first design. It contrasts sequential execution, parallelism, and concurrency, then argues that Erlang’s process model and BEAM VM make it useful for fast, reliable web systems, especially through Elixir and Phoenix.

## Reading notes

- Erlang was built at Ericsson in 1986 for telephony systems and later became useful for distributed, fault-tolerant, highly available applications.
- The text says concurrency is different from parallelism because it switches quickly between small units of work and gives the impression of simultaneous execution.
- Context switching is described as costly, while modern CPUs moved toward multi-core processing instead of pushing single-core speed much further.
- The shared memory model is presented as common in Java and C#, but prone to deadlocks and in need of mutexes, locks, and synchronization.
- The actor model is presented as Erlang’s model, with isolated processes that communicate by non-blocking message passing.
- Each actor has an identity, a mailbox, and explicit reading of messages, and can create actors, send messages, or decide what to do with the next message.
- Erlang processes are described as lightweight, with PID-based communication and internal state that persists across messages.
- The BEAM VM compiles Erlang and Elixir into bytecode and schedules Erlang processes on the CPU.
- BEAM starts schedulers, one for each available core, and this is tied to concurrency, memory efficiency, fault tolerance, and context switching.
- Supervisors are described as special Erlang processes that decide what to do when a process fails and can reset it.
- The page also mentions fault tolerance, distribution across nodes, and the lack of a GIL as contributing factors to Erlang’s concurrency story.
