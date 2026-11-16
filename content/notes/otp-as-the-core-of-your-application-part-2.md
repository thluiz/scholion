---
title: "OTP as the Core of Your Application Part 2"
date: '2026-11-16T04:34:12+00:00'
category: webclip
summary: 'The post builds an actor-model book store in Elixir with a Registry, DynamicSupervisor, and per-book GenServers, then compares its request latency and resource use with a database-centered version under load.'
tags: ["elixir", "otp", "actor-model", "phoenix"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "OTP as the Core of Your Application Part 2"
    url: "https://akoutmos.com/post/actor-model-genserver-app-two"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/akoutmos-com--otp-as-the-core-of-your-application-part-2.md"
    kind: repo
---

The post implements the actor-model parts of a book store application in Elixir. It adds a Registry to map book UUIDs to process IDs, a DynamicSupervisor to start and track book processes, and a GenServer per book to keep state in memory while persisting changes after each update. It also wires Phoenix routes and context functions so the API can use either the database or the actor-based implementation.

It then hydrates application state on startup by loading all books from the database and starting one process per book. A stress test script sends mixed list, read, and order requests, and the post reports lower latency and flatter response times for the actor-based version, while noting that the approach fits independent resources better than tightly coupled or query-heavy workloads.

## Reading notes

- Uses a local Registry to look up a book process by book ID and drop stale entries when a process terminates
- Uses a DynamicSupervisor to start one `BookProcess` per book and to restart transient children when needed
- Stores each book as GenServer state so reads and writes can happen serially and atomically per book
- Uses `handle_continue/2` to persist state changes to the database after replying to the caller
- Adds Phoenix routes for listing books, showing one book, and ordering a copy
- Provides parallel `Books` context functions for actor-based calls and for database-only calls
- Hydrates the application at startup by loading all books and starting their processes before the endpoint comes up
- Uses a uniform stress test over book IDs to compare the two implementations under load
- Reports faster average response times and lower variance for the actor-model version than for the database-centered version
- Notes that the approach works best when actors are independent and the database is still better for complex queries and tightly coupled transactions
