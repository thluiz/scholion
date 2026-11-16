---
title: "Elixir and ETS Alchemy"
date: '2020-07-05T14:10:35+00:00'
category: webclip
summary: 'The post explains what ETS is, when it makes sense to use it, how table options and ownership affect behavior, and what to watch for when using ETS in production.'
tags: ["elixir", "ets", "beam", "production"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Elixir and ETS Alchemy - Sayan Chakraborty | Blog | Engineering | Software | Tech"
    url: "https://web.archive.org/web/20200610084520id_/https://sayan.xyz/posts/elixir-erlang-and-ets-alchemy/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--elixir-and-ets-alchemy.md"
    kind: repo
---

The post introduces ETS as an in-memory key-value store for Erlang terms and walks through its main table types and options. It also frames ETS as useful for large datasets and concurrent access, while warning that cache use should be justified by measured bottlenecks.

## Reading notes

- ETS is Erlang Term Storage, an in-memory key-value store for tuples of Erlang terms.
- `:set`, `:ordered_set`, `:bag`, and `:duplicate_bag` are the four ETS table types described in the post.
- `insert/2` is atomic, but it overwrites data destructively; `insert_new/2` returns a boolean when a key already exists.
- Table options include `:named_table`, access control with `:public`/`:protected`/`:private`, concurrency flags, `:compressed`, and `:decentralized_counters`.
- The post says not to use ETS as a cache too early; first log and analyze the application to find real bottlenecks.
- ETS tables live in off-heap memory, so frequent ETS operations do not create the same garbage collection pressure as process state.
- ETS supports efficient lookups and queries such as `lookup/2`, `lookup_element/3`, `match/2`, `match_object/2`, and `select/2`.
- `:private` tables restrict access to the owner process, `:protected` allows reads from other processes, and `:public` allows reads and writes from processes with the table reference.
- The post presents ETS as useful when concurrent processes need shared access to large data sets.
- ETS tables can store Elixir structs, so retrieved structs do not need to be deserialized.
- Table ownership can be transferred to an `heir` process if the owner crashes.
- The post recommends placing ETS ownership close to the processes that use the data, instead of keeping tables too high in the supervision tree.
- A dedicated GenServer or a Supervisor can own the table, depending on the lifecycle you want.
- ETS is not a database, so transactions are limited; the post says that for proper transaction support you should look into Mnesia.
- Iteration options mentioned include `tab2list/1`, `foldl/3`, and `foldr/3`, while `first/1`, `next/2`, `prev/2`, and `last/1` are not isolated unless used with `safe_fixtable/2`.
- For scalability, the post suggests sharding ETS tables and iterating over smaller groups of data.
- Large lookup results are copied into the receiving process heap, so `persistent_term` may be a better fit for very large read-heavy data.
- Observer can inspect ETS tables in production, but the post warns that it can also kill the owner process.
- Remote console access can let you change ETS data in production, which the post treats as risky and suitable only when you know what you are doing.
