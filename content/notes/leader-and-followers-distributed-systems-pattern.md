---
title: "Leader and Followers"
date: '2026-11-25T16:15:08+00:00'
category: webclip
summary: 'Describes designating a single leader server in a replicated cluster to coordinate updates and provide stronger consistency guarantees than simple majority quorum.'
tags: ["distributed-systems", "replication", "consistency"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Leader and Followers"
    url: "https://martinfowler.com/articles/patterns-of-distributed-systems/leader-follower.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/martinfowler-com--leader-and-followers-distributed-systems-pattern.md"
    kind: repo
---

The text discusses how data replication across multiple servers, used for fault tolerance, must also provide clients with consistency guarantees. Majority quorum reads and writes are sometimes insufficient, since individual servers lack knowledge of other servers' states and inconsistencies are only detected when reading from multiple servers, which does not always provide strong enough guarantees. The proposed approach is to select a single leader server in the cluster that makes decisions for the whole cluster and propagates them to the other servers.

## Reading notes

- Data replication across multiple servers is used to achieve fault tolerance in systems that manage data.
- Clients require some level of consistency guarantee when data is updated on multiple servers.
- With majority quorum reads and writes, some failure scenarios can still expose inconsistent data to clients.
- Individual servers in a quorum do not know the data state on other servers, so inconsistencies are only resolved when reading from multiple servers.
- In certain cases, resolving inconsistencies through quorum reads does not provide strong enough guarantees for data returned to clients.
- The solution is to choose one server as the leader for the cluster.
- The leader takes decisions on behalf of the entire cluster regarding data updates.
- The leader is responsible for propagating its decisions to all the other servers in the cluster.
