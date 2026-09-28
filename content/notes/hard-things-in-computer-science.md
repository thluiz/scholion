---
title: "Hard Things in Computer Science"
date: '2022-07-04T10:50:25-03:00'
category: webclip
summary: 'The post argues that computer science has many hard problems beyond cache invalidation and naming things, including timezones, estimates, distributed systems, and proving code is bug-free.'
tags: ["computer-science", "distributed-systems", "software-development", "estimation"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Hard Things in Computer Science - DZone Open Source"
    url: "https://dzone.com/articles/hard-things-in-computer-science"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-07/dzone-com--hard-things-in-computer-science.md"
    kind: repo
---

The post pushes back on the claim that only cache invalidation and naming things are hard in computer science. It says many other areas are difficult, including time-related edge cases, project estimates, distributed coordination, and proving correctness.

## Reading notes

- Cache invalidation depends on choosing a TTL that balances stale reads against unnecessary reloads.
- Naming is hard because code must be precise, and different terms can hide different meanings between business and developers.
- Dates, times, and timezones are complicated by calendar changes, DST, timezone shifts, and uneven offsets.
- Estimates are difficult because software work differs from house building, unexpected problems appear, and estimates are often treated as deadlines.
- Distributed systems are easy to get wrong because network assumptions fail, and coordination problems like dual writes and leader election are hard to solve.
- Dual writes may require 2PC, compensating transactions, or CDC, but consistency across stores is still only eventual in practice.
- Leader election depends on consensus, and algorithms like Paxos and Raft are meant to handle partitions and re-election.
- Bug-free code cannot be guaranteed by testing alone; the reliable route is formal proof, which still remains mostly in academia.
