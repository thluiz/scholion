---
title: "Testing races with a synchronizing Decorator"
date: '2025-08-06T11:02:32+00:00'
category: webclip
summary: 'Article shows how to deterministically reproduce a race condition in reservation tests by synchronizing database reads with a Decorator, and discusses trade-offs.'
tags: ["concurrency", "testing", "decorator-pattern"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Testing races with a synchronizing Decorator"
    url: "https://blog.ploeh.dk/2025/08/04/testing-races-with-a-synchronizing-decorator"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/blog-ploeh-dk--testing-races-with-a-synchronizing-decorator.md"
    kind: repo
---

The article revisits testing race conditions in a restaurant reservation system. A previous approach used a slow Decorator to provoke races, but could still yield false negatives when tasks do not truly run in parallel. Here, the author introduces a synchronizing Decorator that coordinates database reads to deterministically provoke overbooking when transaction control is missing.

## Reading notes

- A test `NoOverbookingRace` creates two reservation POST requests with the same date and quantity, originally using a slow repository Decorator to expose race conditions.
- An added `Task.Delay` between starting `task1` and `task2` demonstrates that even with asynchronous starts, the tasks may effectively run sequentially instead of in parallel.
- Real systems can experience similar pauses due to garbage collection, thread starvation, OS scheduling, or other factors, which can change how concurrent code interleaves.
- Without transaction control, a long enough pause between tasks can make them behave sequentially so the system correctly rejects the second reservation, hiding an overbooking bug.
- With a configured 100 ms slow Decorator that causes about 300 ms delay for a reservation, experiments show that a 300 ms pause sometimes reveals the bug and sometimes not, while a one-second delay always makes the test pass even if transaction control is missing.
- Depending on the context, occasionally missing a real race might be acceptable, but some situations require more deterministic testing behaviour.
- To reliably reproduce the race, the article proposes synchronizing the repository reads so that both competing operations see the same data snapshot.
- A `SynchronizedReaderRepository` Decorator implements `IReservationsRepository` and wraps an inner repository, adding a `CountdownEvent` initialized with count 2.
- The `ReadReservations` method delegates to the inner repository, then signals the `CountdownEvent` and waits until the count reaches zero before returning the result.
- Under the assumption that only the two test calls invoke `ReadReservations`, both threads are forced to wait until both reads have completed, ensuring they see the same reservations.
- If transaction control is missing, both threads conclude that the reservation can be accepted and the system overbooks the time slot, making the bug surface reliably.
- A new version of the `NoOverbookingRace` test uses `service.Select(repo => new SynchronizedReaderRepository(repo))` to build a service with synchronized reads and then posts the two reservations in parallel.
- The test asserts that exactly one response is an internal server error and the other is successful, then verifies that the reservation with quantity 10 was actually created.
- With the synchronizing repository, if the system under test lacks transaction control the test fails, and it passes when proper transaction control is in place, eliminating the false negatives seen with the slow Decorator.
- The approach has drawbacks: the Decorator assumes exactly two parallel readers, which couples it tightly to a specific test scenario.
- Additional tests or different synchronization needs could require new Decorators or a more generalized synchronization mechanism, increasing complexity.
- The test becomes sensitive to changes in the system under test; if new calls to `ReadReservations` are added, the countdown may reach zero too early and unblock threads prematurely.
- An example of such a change is adding queries for surrounding time slots, which could change how many reads occur and when they happen.
- Making the Decorator robust to such changes might involve tracking separate synchronization objects per argument set, which complicates the implementation.
- The Decorator still cannot guard against identical duplicate reads with the same arguments, which could interfere with the intended synchronization.
- Caching introduces further problems: with a read-through cache wrapping the `SynchronizedReaderRepository`, only the first query may hit the synchronized repository and block, potentially leading to a deadlock.
- A possible mitigation could be using a `Wait` overload with a timeout when waiting on the countdown, though this adds extra configuration and logic.
- The article notes that if reads are cached, pessimistic locking via `TransactionScope` will not be effective, and optimistic concurrency would be needed instead, which brings its own difficulties.
- The author generalizes that synchronization primitives are not only for making production code thread-safe but can also help create deterministic tests for race conditions.
- The technique relies on understanding the underlying race well enough to design a targeted synchronization scheme, and the article acknowledges that diagnosing such problems remains the hardest part.
