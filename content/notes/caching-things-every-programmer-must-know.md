---
title: "Caching things every Programmer must know"
date: '2022-07-05T11:05:13-03:00'
category: webclip
summary: 'The article explains what caching is, when it matters, its benefits, cache memory levels, common cache types, distributed caching, hit and miss, cache strategies, and eviction policies.'
tags: ["caching", "distributed-caching", "cache-eviction", "performance"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Caching things every Programmer must know | by Dineshchandgr | Jun, 2022 | Dev Genius"
    url: "https://blog.devgenius.io/caching-things-every-programmer-must-know-28d4a7e8b9b1"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-07/blog-devgenius-io--caching-things-every-programmer-must-know.md"
    kind: repo
---

The article defines caching as an intermediary data store that serves data faster than the original source and helps improve application speed by reducing costly database calls and backend load. It gives examples with social media profile pages and CDN-delivered movie data, then lists cases where caching matters, such as external APIs, static content, repeated reads, frequent repeated output, computation-heavy aggregation, and long-running database queries.

## Reading notes

- Caching is presented as a way to store data in temporary memory so applications avoid repeated database access.
- The article says the first profile-page request is slower because it reads from the database, while later requests can be faster from cache.
- A CDN is described as caching content in proxy servers closer to end users than origin servers.
- The text lists benefits such as improved performance, lower database cost, reduced backend load, predictable performance, fewer hotspots, higher read throughput, and scalability.
- The cache memory section describes four levels: L1 inside the CPU, L2 as cache memory, L3 as main memory or RAM, and L4 as secondary memory on disk.
- The article says cached data is checked first in L1, then L2, then L3, while disk-based storage is slower but permanent.
- It lists application caching, database caching, DNS caching, client-side caching, CDN cache, and API gateway cache as caching types.
- Distributed caching is described as combining the RAM of multiple servers into a cluster that acts as one cache component and can scale by adding or removing nodes.
- Cache hit means the requested data is found in cache, and cache miss means it is not found there.
- The article describes cache aside, read through, write through, write back or write behind, and write around as caching strategies.
- Cache eviction is defined as freeing old unused data to make room for new data, and the article mentions FIFO, LIFO, LRU, and MRU as eviction policies.
