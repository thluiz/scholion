---
title: "Sharing an SQLite database across containers is surprisingly brilliant"
date: '2020-02-22T12:11:44+00:00'
category: webclip
summary: 'The post argues that Segment reduced latency by moving customer control data to a local SQLite file shared across containers, shifting complexity from read paths to write paths and avoiding a networked database on the critical path.'
tags: ["sqlite", "containers", "distributed-systems", "reliability"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Sharing an SQLite database across containers is surprisingly brilliant | by Rick Branson | Medium"
    url: "https://medium.com/@rbranson/sharing-sqlite-databases-across-containers-is-surprisingly-brilliant-bacb8d753054"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/medium-com--sharing-sqlite-database-across-containers.md"
    kind: repo
---

Rick Branson describes how Segment changed its control-data architecture to improve reliability and reduce latency in a high-throughput streaming pipeline. Instead of keeping customer-specific configuration in a networked database, the team stored it locally in a file shared across containers and used SQLite to make concurrent access work.

## Reading notes

- Segment’s streaming pipeline handles more than 500,000 messages per second, and the post opens with a latency graph showing a large drop after the change.
- Major incidents had made the team wary of production changes, so engineering work focused on step-by-step improvements backed by data.
- The author says one key architectural decision was how to store customer configuration, called control data.
- The goal was to loosen the coupling between the control plane and the data plane.
- The proposed idea was to keep control data local to the host, store it in a file, and share that file across dozens of containers.
- The author says SQLite was the practical choice because multi-process concurrency is one of its distinguishing features.
- Containers are described as processes with filesystem isolation, which makes SQLite suitable for sharing a database across them.
- The setup was tested on a Docker shared volume across multiple containers, and it worked.
- WAL mode was needed for the system to work under load.
- The resulting system, called ctlstore, was open sourced.
- The main trade-off was moving complexity from the data plane read path to the control plane write path.
- The post argues that control data errors and unavailability are a major source of large outages and that reliability work should focus there.
