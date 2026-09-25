---
title: "New Method Is the Fastest Way To Find the Best Routes"
date: '2025-08-07T15:00:02+01:00'
category: webclip
summary: 'A new shortest-path algorithm breaks the long-standing sorting barrier by avoiding full sorting of the frontier. It runs faster than Dijkstra’s on directed and undirected graphs.'
tags: ["shortest-paths", "graph-algorithms", "sorting-barrier", "computer-science"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "New Method Is the Fastest Way To Find the Best Routes | Quanta Magazine"
    url: "https://www.quantamagazine.org/new-method-is-the-fastest-way-to-find-the-best-routes-20250806/?utm_source=tldrnewsletter"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-08/quantamagazine-org--new-method-is-the-fastest-way-to-find-the-best-routes.md"
    kind: repo
---

A team of researchers found a shortest-path algorithm that breaks the sorting barrier. Instead of sorting every frontier node, it clusters neighboring nodes, uses Bellman-Ford in limited steps, and reaches a faster runtime than Dijkstra’s on both directed and undirected graphs.

## Reading notes

- Shortest-paths asks for the shortest route from one source node to every other node in a weighted graph.
- Dijkstra’s algorithm works outward step by step, but its frontier scanning creates a sorting barrier.
- Tarjan and another researcher pushed Dijkstra’s original method to that speed limit in 1984.
- Earlier barrier-breaking algorithms worked only under special assumptions about weights.
- Ran Duan’s approach groups frontier nodes into clusters and considers one node from each cluster.
- The first version broke the barrier for arbitrary weights only on undirected graphs.
- Xiao Mao and Duan’s team then worked on directed graphs, which are harder because reachability can differ by direction.
- The team used short runs of Bellman-Ford to identify influential nodes without relying on its full slowness.
- Mao removed randomness from part of the approach, and Duan adapted a 2018 technique from another graph algorithm.
- The final algorithm slices the graph into layers, explores influential nodes first, and later returns to other frontier nodes.
- The method does not always visit nodes in order of increasing distance, so the sorting barrier no longer applies.
- The authors plan to see whether the algorithm can be streamlined further.
