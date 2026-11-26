---
url: "https://martinfowler.com/articles/patterns-of-distributed-systems/fixed-partitions.html"
captured_at: "2026-11-25T16:15:36+00:00"
title: "Fixed Partitions"
domain: "martinfowler-com"
---

Keep the number of partitions fixed to keep the mapping of data to partition unchanged when the size of a cluster changes.

## Problem

To split data across a set of cluster nodes, each data item needs to be mapped to them. There are two requirements for mapping data to the cluster nodes.

*   The distribution should be uniform.
*   It should be possible to know which cluster node stores a particular data item without making a request to all the nodes.

Consider a key-value store, which is a good proxy for many storage systems. Both requirements can be fulfilled by taking a hash of the key and using the modulo operation to map it to a cluster node. So if we have a three-node cluster, we can map keys Alice, Bob, Mary, and Philip like this.

Keys

Hash

Node Index †

Alice

133299819613694460644197938031451912208

0

Bob

63479738429015246738359000453022047291

1

Mary

37724856304035789372490171084843241126

2

Philip

83980963731216160506671196398339418866

2

† Node Index = Hash %3

However, this method creates a problem when the cluster size changes. If two more nodes are added to the cluster, we will have five nodes. The mapping will then look like this.

Keys

Hash

Node Index †

Alice

133299819613694460644197938031451912208

3

Bob

63479738429015246738359000453022047291

1

Mary

37724856304035789372490171084843241126

1

Philip

83980963731216160506671196398339418866

1

† Node Index = Hash % 5

This way, mapping for almost all the keys changes. Even after adding only a few new cluster nodes, all the data needs to be moved. When the data size is large, this is undesirable.

## Solution

One of the most commonly used solution is to map data to logical partitions. Logical partitions are mapped to the cluster nodes. Even if cluster nodes are added or removed, the mapping of data to partitions doesn't change. The cluster is launched with a preconfigured number of partitions—for the sake of this example, 1024. This number does not change when new nodes are added to the cluster. So the way data is mapped to partitions using a hash of the key remains the same.

It's important that partitions are evenly distributed across cluster nodes. When partitions are moved to new nodes, it should be relatively quick with only a smaller portion of the data being moved.

for more details go to [Chapter 19](https://learning.oreilly.com/library/view/patterns-of-distributed/9780138222246/ch19.xhtml) of the online ebook at oreilly.com
