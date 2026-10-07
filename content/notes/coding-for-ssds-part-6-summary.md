---
title: "Coding for SSDs – Part 6: A Summary"
date: '2015-03-02T19:14:46-03:00'
category: webclip
summary: 'The article summarizes SSD fundamentals, controller behavior, access patterns, and system optimizations programmers should consider to reduce write amplification, improve throughput, and avoid common performance pitfalls.'
tags: ["coding", "performance", "solid-state-drives", "programming"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Coding for SSDs – Part 6: A Summary – What every programmer should know about solid-state drives | Code Capsule"
    url: "http://codecapsule.com/2014/02/12/coding-for-ssds-part-6-a-summary-what-every-programmer-should-know-about-solid-state-drives/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-03/codecapsule-com--coding-for-ssds-part-6-summary.md"
    kind: repo
---

The article condenses the whole “Coding for SSDs” series into short points on how SSDs work and what that means for software. It covers flash cell types, limited lifespan, page and block behavior, the Flash Translation Layer, wear leveling, garbage collection, and the effects of background activity on host I/O.

It also lists practical guidance for access patterns and system setup, including aligning and batching writes, buffering small writes, keeping related data together, separating reads from writes, splitting hot and cold data, enabling TRIM, using over-provisioning, and aligning partitions.

## Reading notes

- SSDs store bits in flash-memory cells, using SLC, MLC, or TLC.
- NAND-flash cells have a limited number of P/E cycles and wear out over time.
- Benchmarks can be unreliable, so multiple sources and in-house testing are recommended.
- Reads and writes are aligned to page size, and pages cannot be overwritten in place.
- Pages are erased only by erasing whole blocks.
- The Flash Translation Layer maps logical addresses to physical addresses and helps handle random writes like sequential writes.
- Internal parallelism lets the drive write to several blocks across different chips at once.
- Wear leveling distributes work so cells reach their limits more evenly.
- Garbage collection reclaims stale pages for future writes.
- Background operations such as garbage collection can hurt foreground performance, especially with sustained small random writes.
- Writing less than a page should be avoided to reduce write amplification.
- Small writes should be buffered in RAM and flushed as larger batches.
- Related data should be written together so later reads can benefit from internal parallelism.
- Mixed small reads and writes can reduce throughput, so separating them into larger batches is preferable.
- Obsolete data should be invalidated in batches to help garbage collection and reduce fragmentation.
- Large aligned random writes can perform as well as sequential writes when they match the clustered block size.
- Large single-threaded reads and writes are preferred when the workload allows it.
- When small writes cannot be grouped, multiple threads can improve throughput.
- Hot data and cold data should be separated to reduce copying during updates and garbage collection.
- Very hot data and metadata should be buffered and written less often.
- PCI Express and SAS are faster than SATA, but also more expensive.
- Over-provisioning helps wear leveling and can improve performance under sustained random writes.
- TRIM helps the controller prepare deleted blocks during idle time.
- Partitions should be aligned to the NAND-flash page size.
