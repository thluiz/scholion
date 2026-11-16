---
title: "Catalog of Patterns of Distributed Systems"
date: '2026-11-16T02:55:28+00:00'
category: webclip
summary: 'The page collects distributed-systems patterns developed since 2020 and published in 2023, with short summaries and links to chapters in the book. It frames common coordination, consistency, replication, and messaging problems these systems share.'
tags: ["distributed-systems", "patterns", "consistency", "replication"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Catalog of Patterns of Distributed Systems"
    url: "https://martinfowler.com/articles/patterns-of-distributed-systems/index.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/martinfowler-com--catalog-of-patterns-of-distributed-systems.md"
    kind: repo
---

The page gathers patterns for distributed systems around recurring problems in storage, messaging, system management, and compute. It says these systems face shared issues such as keeping multiple data copies synchronized, handling unreliable nodes, and dealing with network delays.

It presents a catalog of patterns first collected on the site in 2020 and later published in 2023 in the book *Patterns of Distributed Systems*. The page now offers short summaries of each pattern and deep links to the relevant book chapters.

## Reading notes

- Distributed systems often need multiple copies of data kept in sync, while nodes may fail and network delays can create inconsistencies.
- Organizations rely on distributed software for storage, messaging, system management, and compute capability.
- The site collects these shared solutions as patterns and links them to the book *Patterns of Distributed Systems*.
- The page provides short summaries of each pattern and deep links to the matching O'Reilly chapters.
- The catalog includes patterns for time ordering, replication, leader selection, leases, quorums, logs, retries, batching, and client notification.
