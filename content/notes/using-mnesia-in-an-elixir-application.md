---
title: "Using Mnesia in an Elixir Application"
date: '2020-09-07T17:02:53-03:00'
category: webclip
summary: 'The post explains what Mnesia is, how it fits soft real-time and fault-tolerant use cases, when to prefer it over PostgreSQL or Redis, and shows an Elixir banking app built with Amnesia.'
tags: ["mnesia", "elixir", "otp", "database"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Using Mnesia in an Elixir Application | AppSignal Blog"
    url: "https://blog.appsignal.com/2020/05/19/using-mnesia-in-an-elixir-application.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-09/blog-appsignal-com--using-mnesia-in-an-elixir-application.md"
    kind: repo
---

The post presents Mnesia as an OTP-built DBMS available to Elixir and Erlang without extra dependencies or separate services. It focuses on the design trade-offs that make Mnesia fit soft real-time key/value access, complex queries, and replicated tables with fault tolerance.

## Reading notes

- Mnesia is built into OTP and can be used directly from Elixir or Erlang without installing extra dependencies or running a separate database system.
- It was designed for telecommunications workloads that need fast key/value lookup, complex queries, and high fault tolerance.
- Because it runs in the same memory space as the application, it avoids network overhead and can deliver soft real-time access.
- Mnesia stores Erlang data types natively, so read and write operations do not require marshalling and unmarshalling.
- For complex queries, the post mentions Query List Comprehensions, Match Specifications, and table indexes.
- Mnesia replicates tables across cluster nodes, and transactions write to all configured replicas.
- If some nodes are unavailable during a write, the available replicas are updated and the missing ones are synchronized when they return.
- In CAP terms, the post describes Mnesia as closer to a CP database because it propagates commits across replicas and does not support eventual consistency.
- The recommendation for using Mnesia depends on the application’s requirements and trade-offs.
- The author says Mnesia worked well in production for soft real-time session data that lived only for the duration of a user session.
- For large datasets or cases that do not need soft real-time latency, the post suggests traditional databases such as MySQL or Postgres.
- For needs similar to Redis or Memcached, the post suggests considering Mnesia because it is built into OTP.
- The hands-on section builds a simple banking app with Amnesia as an Elixir wrapper around the Mnesia API.
- The sample app supports creating accounts, transferring money, fetching account details, depositing funds, withdrawing funds, and searching for accounts with low balances.
- The database schema defines a single `Account` table with an auto-incrementing id, first name, last name, balance, and an index on balance.
- The tutorial creates the database with `mix amnesia.create -d Database --disk`, which produces a `Mnesia.nonode@nohost` directory for persisted data.
- The `Accounts` module creates accounts inside transactions and reads accounts back by id.
- The transfer, deposit, and withdraw functions update balances inside transactions, and the transfer logic checks for sufficient funds and valid source and destination accounts.
- The low-balance query uses `Account.where(balance < min_balance)` and `Amnesia.Selection.values()`.
- The sample IEx session shows seeded accounts, a transfer from one account to another, a low-balance query, and persisted data across sessions.
