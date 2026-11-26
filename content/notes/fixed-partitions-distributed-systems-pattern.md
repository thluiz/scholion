---
title: "Fixed Partitions"
date: '2026-11-25T16:15:36+00:00'
category: webclip
summary: 'Explains mapping data to a fixed set of logical partitions so that cluster resizing only remaps partitions to nodes, avoiding widespread data movement.'
tags: ["distributed-systems", "data-partitioning", "cluster-management"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Fixed Partitions"
    url: "https://martinfowler.com/articles/patterns-of-distributed-systems/fixed-partitions.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/martinfowler-com--fixed-partitions-distributed-systems-pattern.md"
    kind: repo
---

The text describes how directly hashing keys to cluster nodes distributes data uniformly and allows locating items without querying all nodes, but causes extensive remapping when the cluster size changes. It then presents fixed logical partitions as a way to keep the key-to-partition mapping stable while letting partitions move between nodes as the cluster grows or shrinks.

## Reading notes

- Mapping data in a cluster should spread items uniformly and make it possible to locate an item without broadcasting to every node.
- A simple scheme is to hash each key and take the modulo of the cluster size to choose a node, which satisfies both requirements at a given size.
- When nodes are added and the modulo divisor changes, the hash-to-node mapping shifts, so most keys end up on different nodes.
- With large datasets, having to move almost all data after adding only a few nodes is undesirable.
- A common alternative is to map data to logical partitions first, and then map these partitions to cluster nodes.
- The cluster is started with a fixed, preconfigured number of logical partitions (e.g., 1024), and this number stays constant even as nodes are added or removed.
- Because the number of partitions is fixed, the way keys are hashed and assigned to partitions does not change when the cluster size changes.
- Only partitions are reassigned to nodes when the cluster membership changes, so data movement is limited to the partitions that move.
- Partitions should be evenly spread across nodes so that workload and storage are balanced in the cluster.
- Moving partitions to new nodes should be relatively fast and require transferring only a small subset of the total data.
