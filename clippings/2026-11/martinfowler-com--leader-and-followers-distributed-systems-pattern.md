---
url: "https://martinfowler.com/articles/patterns-of-distributed-systems/leader-follower.html"
captured_at: "2026-11-25T16:15:08+00:00"
title: "Leader and Followers"
domain: "martinfowler-com"
---

Have a single server to coordinate replication across a set of servers.

## Problem

To achieve fault tolerance in systems that manage data, the data needs to be replicated on multiple servers.

It's also important to give some guarantee about consistency to clients. When data is updated on multiple servers, you need to decide when to make it visible to clients. Write and read [Majority Quorum](https://martinfowler.com/articles/patterns-of-distributed-systems/majority-quorum.html) is not sufficient, as some failure scenarios can cause clients to see data inconsistently. Each individual server does not know about the state of data on the other servers in the quorum. It's only when data is read from multiple servers, the inconsistencies can be resolved. In some cases, this is not enough. Stronger guarantees are needed about the data sent to clients.

## Solution

Select one server in the cluster as a leader. The leader is responsible for taking decisions on behalf of the entire cluster and propagating the decisions to all the other servers.

for more details go to [Chapter 06](https://learning.oreilly.com/library/view/patterns-of-distributed/9780138222246/ch06.xhtml) of the online ebook at oreilly.com
