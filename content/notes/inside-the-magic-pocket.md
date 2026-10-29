---
title: "Inside the Magic Pocket"
date: '2016-05-07T05:25:39-03:00'
category: webclip
summary: 'Dropbox explains the architecture of Magic Pocket, its immutable block storage system, and the requirements behind it: durability, low-latency reads, scale, and operational simplicity.'
tags: ["magic-pocket", "distributed-storage", "infrastructure"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Inside the Magic Pocket | | Dropbox Tech Blog"
    url: "https://blogs.dropbox.com/tech/2016/05/inside-the-magic-pocket/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-05/blogs-dropbox-com--inside-the-magic-pocket.md"
    kind: repo
---

Dropbox outlines Magic Pocket as its in-house system for storing file content, split into encrypted blocks and distributed across multiple geographic regions. The post frames the system around four requirements: immutable storage, low-latency access for a cold workload, durability across failures, and a simple design that avoids unnecessary distributed complexity.

## Reading notes

- Magic Pocket stores file content, while metadata is handled elsewhere.
- Files are split into encrypted blocks of up to 4 MB, and once written a block never changes.
- File changes are recorded in FileJournal, which keeps mutability higher in the stack.
- The workload is cold overall, but blocks still need fast reads after upload and later when revisited.
- The system uses hard drives for storage, with SSDs reserved for databases and caches.
- Recent uploads get high replication and caching, while older data uses more efficient storage encoding.
- Durability is designed to survive disk failures, calamities, and natural disasters through erasure coding and multi-region replication.
- Magic Pocket scaled from double-digit petabytes to multi-exabytes in about six months.
- The design favors simplicity and avoids quorum-style consensus and distributed coordination where possible.
- Blocks are identified by SHA-256 hashes and grouped into 1 GB buckets.
- A bucket is stored in a volume across multiple machines, in replicated or erasure-coded form.
- The system is multi-zone, with blocks stored in at least two separate zones.
- Frontends accept storage requests and decide where blocks should be stored or read from.
- The Block Index maps each block to its bucket and is implemented as a sharded MySQL cluster.
- Cross-zone replication copies block puts to another zone within one second.
- Cells are logical storage clusters of about 50 PB each, with racks arranged for physical diversity.
- OSDs are the storage machines that hold the disks and store the blocks.
- The Replication Table maps buckets to volumes and volumes to OSDs, and tracks open, type, and generation.
- Open volumes accept writes; closed volumes are immutable and can be moved safely.
- The Master coordinates repairs, bucket creation, garbage collection, and bucket merging, but is not on the data plane.
- Volume Managers move or erasure-code volumes by reading from and writing to OSDs.
- A Put first checks whether the block exists, chooses a volume, writes to the OSDs, and then updates the Block Index.
- A Get looks up the block through the Block Index and Replication Table, then fetches it from an OSD.
- Replicated volumes are read directly from any OSD holding the blocks.
- Erasure-coded volumes can often be read from a single OSD, with reconstruction handled when needed.
- Repair starts when an OSD has been offline for 15 minutes, after which the Master closes affected volumes and builds a reconstruction plan.
- The repair commit updates generation numbers and the Replication Table so old and new placements cannot be confused.
- The open/closed volume model keeps live traffic separate from background operations and simplifies consistency.
