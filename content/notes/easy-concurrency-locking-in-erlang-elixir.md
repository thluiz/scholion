---
title: "Easy Concurrency Locking in Erlang/Elixir"
date: '2020-07-05T14:10:32+00:00'
category: webclip
summary: 'Explains limits of GenServer as a single-owner lock and presents the sleeplocks library, which implements multi-slot, blocking locks on the BEAM using OTP message passing and GenServers.'
tags: ["erlang", "elixir", "concurrency", "otp"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Easy Concurrency Locking in Erlang/Elixir"
    url: "https://web.archive.org/web/20201108015122id_/https://whitfin.io/easy-concurrency-locking-in-erlang-elixir/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--easy-concurrency-locking-in-erlang-elixir.md"
    kind: repo
---

The text describes how GenServer in Erlang/Elixir can serialize access to a resource by processing messages synchronously in order, which works well for single-owner locks. It then motivates a need for locks that allow multiple concurrent holders to support throttling scenarios, and introduces the `sleeplocks` library as a BEAM-friendly implementation of spinlocks built on message passing and GenServers. The article walks through its simple API for creating, acquiring, attempting, and executing within locks, and then explains the internal data structures and message flow used to manage slots, waiting queues, and replies.

## Reading notes

- GenServer from OTP, exposed in Elixir’s standard library, can serialize access to a resource by handling messages synchronously and in order.
- Wrapping all database interactions inside a GenServer can effectively serialize writes, resembling a lock pattern from other languages.
- GenServer-based locking is limited because it effectively allows only a single process to hold the lock at any time.
- The author identified a gap for locks that can be held by multiple processes simultaneously, useful for throttling access where a single GenServer is insufficient.
- Use cases for multi-holder locks include throttling HTTP requests and controlling process spawn rates.
- To address this need, the author wrote the `sleeplocks` library to practice Erlang and implement this locking pattern.
- `sleeplocks` is described as a BEAM-friendly take on spinlocks, adapting the idea of repeatedly checking for an available lock to OTP’s message passing model.
- Traditional spinlocks repeatedly poll for a lock on a thread, while sleeplocks use GenServers and message passing instead of busy spinning.
- The design goal was to keep the library as a thin wrapper around existing OTP tools, reusing the VM’s message system and the GenServer abstraction.
- Reusing OTP primitives reduces the potential bug surface and leverages well-tested components written by experienced contributors.
- Each sleeplock has a configurable number of slots, representing the maximum concurrent processes allowed to hold the lock.
- A new lock is created with `sleeplocks:new/1` or `sleeplocks:new/2`, with an option to name the lock for global access.
- Passing `1` as the slot count creates a single-holder lock, equivalent to a mutex.
- Locks can be acquired and released via a simple API using the lock’s name, for example `sleeplocks:acquire(Name)` and `sleeplocks:release(Name)`.
- When acquiring a lock, the implementation infers necessary data (like channel reference and caller PID) from the message itself.
- If a slot is available when acquiring, the lock is granted immediately; if not, `acquire/1` blocks until a slot frees up.
- `attempt/1` provides a non-blocking option that returns `{error, unavailable}` when no slots are free instead of waiting.
- `execute/2` wraps `acquire/1` and `release/1`, running a provided function only after successfully acquiring the lock.
- Code run inside `execute/2` is wrapped in `catch` clauses so that locks are properly released even if the user code crashes.
- Ensuring release on crash avoids leaked slots that would otherwise remain held by defunct processes.
- Internally, creating a lock spawns a GenServer-backed process linked to the caller, which receives and manages lock-related messages.
- Each lock maintains three fields: total slot count, a map of processes currently holding the lock, and a queue of waiting processes.
- The processes map stores process identifiers associated with a simple `ok` atom as values.
- To check if a lock is full, the implementation compares the size of the processes map with the slot count stored in the lock state.
- When granting a lock, the process’s identifier is added to the processes map to record the holder.
- If a process that already holds the lock calls acquire again, the map update acts as a no-op and avoids deadlock because the duplicate entry is ignored.
- Releasing a lock removes the process’s entry from the processes map, freeing one slot.
- If all slots are filled when a process attempts to acquire, its identifier is appended to the lock’s waiting queue.
- In the full-lock case, the GenServer uses `noreply` to defer the response, causing the caller to block until a later reply.
- Once a lock is released and a slot opens, the implementation checks the waiting queue for the next process.
- If the queue is empty when a slot opens, no immediate action is taken and the free slot remains available for future acquire attempts.
- If there is a waiting process, it is removed from the queue and replied to manually via `gen_server:reply`, which unblocks that process.
- After replying to a waiting process, the lock inserts that process’s identifier into the processes map to record that it now holds a slot.
- The author invites feedback on the library, noting it is only their second written in Erlang and that style suggestions are welcome.
- `sleeplocks` is available on GitHub and published on Hex, making it easy to integrate into Erlang/Elixir projects.
- The library is already used in some utilities at the author’s workplace and plays a small role in `Cachex` to limit access to its main state table.
- The author mentions that, in their experience so far, `sleeplocks` has behaved reliably in real usage.
