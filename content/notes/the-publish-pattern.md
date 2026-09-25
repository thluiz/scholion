---
title: "The Publish Pattern"
date: 2026-09-23T17:30:10+01:00
category: webclip
has_commentary: false
tags: ["concurrency", "cpp", "design-patterns", "software-architecture"]
summary: "A concurrency pattern for decoupling producers and consumers using a const shared_ptr, avoiding mutex bottlenecks while keeping the consumer always on the latest published version."
sources:
  - title: "The Publish Pattern"
    url: "https://accu.org/journals/overload/32/183/teodorescu/?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/accu-org--the-publish-pattern.md"
    kind: repo
---

Lucian Radu Teodorescu names a pattern he's used across multiple codebases but never seen documented: a way to pass data from a continuously-running producer thread to a continuously-running consumer thread without a mutex blocking either side. A naive mutex-protected shared document works, but a slow producer stalls the consumer, and vice-versa. The fix wraps the shared state in a `std::shared_ptr<const T>`: the producer builds a new version off to the side and swaps it in under a short-lived lock; consumers just grab a copy of the pointer and read a version that can never change under them, since the pointee is const.

The design gives every consumer a consistent snapshot without ever blocking on the producer's work, at the cost of memory: multiple versions of the document can be alive at once, and each publish still costs a copy and an allocation. Teodorescu frames it as a relative of double-buffering and of read-copy-update (RCU), then extends it to handle multiple producers (optimistic retry against the last-seen version) and to cheapen the copy for large documents (persistent data structures, or sharing unchanged subparts via nested shared pointers).

## Reading notes

- Requirements driving the pattern: producer constantly produces, consumer constantly consumes, consumer always uses the latest version, and consuming must never be delayed by a slow produce.
- The `published<T>` template holds a `std::shared_ptr<const T>` guarded by a small mutex, with just two operations: `publish()` (swap in a new version) and `get()` (return a copy of the current pointer).
- Because the pointee is `const`, a `shared_ptr<const T>` handed to a consumer stays valid and unchanged for as long as that consumer holds it, even as the producer publishes newer versions concurrently.
- The lock inside `published<T>` is held very briefly and infrequently (twice per produce, once per consume), so contention stays low even though the pattern trades that for extra allocations and copies.
- A consumer job is guaranteed a consistent version for its whole run, but not necessarily the newest one by the time it finishes. Newer versions may have been published mid-job.
- The pattern has no upper bound on how many document versions can be alive simultaneously if there are many long-running consumers, unlike a mutex-based approach that guarantees a single live version.
- It's a form of double-buffering / multiple-buffering, and a variant of read-copy-update (RCU) applied to whole documents rather than low-level structures.
- Multiple producers break the basic version (one can silently overwrite another's work); the fix is an optimistic `try_publish()` that compares against the last-seen version and retries with reapplied updates on conflict, with no bound on retry count unless one is added deliberately.
- When updates are monotonic (only additions, never removals, as in a type checker built by Dimi Racordon for the Hylo compiler), the producer can separate "compute the additions" from "commit the additions," shrinking the window where a competing publish can force a retry.
- For large documents, copying cost can be cut with persistent data structures (new versions share unchanged parts with old ones) or by wrapping expensive subparts in their own `shared_ptr<const T>` so only the container, not the subparts, gets copied.
