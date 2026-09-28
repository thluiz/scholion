---
title: "S3 Is the Future, S3 Is the Past"
date: '2026-09-28T14:33:21+01:00'
category: webclip
summary: 'The text argues that S3-shaped cloud architecture is widespread because of durability, scale, and low cost, but its disk-era latency and write model are increasingly mismatched with SSDs and modern networks.'
tags: ["s3", "cloud-storage", "ssd", "distributed-systems"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "S3 Is the Future, S3 Is the Past"
    url: "https://btrblocks.com/blog/s3_is_the_future_and_the_past/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/btrblocks-com--s3-is-the-future-s3-is-the-past.md"
    kind: repo
---

The page argues that S3 has become the default foundation for data systems because it offers large capacity, durability, low storage cost, and a shared namespace for stateless compute. It says this model now shapes analytics stacks and other services, but much of that architecture exists to work around S3’s limits.

It contrasts S3’s disk-like behavior with SSD-based storage and modern datacenter networking, which can support much lower latency, cheap random access, and in-place updates. The text presents S3 Express One Zone as only a narrow improvement and concludes that a true SSD-based disaggregated storage service is technically possible, but cloud providers lack incentive to build it.

## Reading notes

- S3 is described as the basis for modern cloud software architecture, especially for data-intensive systems.
- Its appeal comes from capacity, durability, low per-gigabyte cost, and a shared durable namespace.
- Common patterns such as data lakes, Kafka on S3, and vector storage on S3 are presented as examples of this shift.
- The text says S3 behaves like a million hard disks behind an HTTP API, with latency in tens of milliseconds and limited bandwidth per request.
- Systems built on S3 need caching, batching, separate metadata stores, and object rewrites because S3 cannot handle small random access efficiently.
- SSD prices have fallen, the SSD-disk gap has narrowed, and SSDs offer microsecond latency, high IOPS, and 4 KB access granularity.
- Modern datacenter networks are fast enough to support disaggregated storage with much lower latency than S3.
- In that model, caching, batching, compaction, and separate metadata stores become less necessary.
- S3 Express One Zone is presented as restricted to one availability zone, still multi-millisecond, and too expensive to be a general replacement.
- The conclusion is that the main obstacle to SSD-based general-purpose storage is inertia and incentives, not technical feasibility.
