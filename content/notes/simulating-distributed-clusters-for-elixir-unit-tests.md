---
title: "Simulating Distributed Clusters for Elixir Unit Tests"
date: '2026-11-16T08:12:11+00:00'
category: webclip
summary: 'The post explains why distributed testing in Elixir is awkward and shows Local Cluster, a small library that starts local BEAM nodes, links them to tests, and makes RPC calls easy.'
tags: ["elixir", "distributed-testing", "unit-tests", "local-cluster"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Simulating Distributed Clusters for Elixir Unit Tests"
    url: "https://web.archive.org/web/20200629141958id_/http://whitfin.io:80/setting-up-distributed-nodes-in-elixir-unit-tests/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--simulating-distributed-clusters-for-elixir-unit-tests.md"
    kind: repo
---

The post says distributed testing in Elixir is awkward because the OTP tools are useful but not obvious, and because many projects rely on them directly without common utilities. For Cachex, the author wanted only a way to start a set of nodes in a local cluster and call them through `:rpc`, so he split that into a separate library called Local Cluster.

## Reading notes

- distributed behavior in Elixir is described as annoying to test, even though OTP has useful tools
- many projects, including Phoenix, build distributed tests directly on standard OTP tools
- Local Cluster was created as a small separate library for starting local distributed nodes
- the API is intentionally tiny and avoids extra DSLs or unnecessary utilities
- `LocalCluster.start/0` starts the manager instance and can be called more than once
- `LocalCluster.start_nodes/2` starts named nodes in a local cluster, using a prefix and a count
- `start_nodes/2` links the nodes to the current process, which makes cleanup easy in ExUnit
- clusters can be kept across tests by starting them in `setup/0` and cleaning them in `teardown/0`
- `start_nodes/2` returns node names that can be used with `:rpc`
- the current VM is not included in the returned list of nodes
- `stop_nodes/1` stops selected nodes, and `stop/0` stops the manager
- under the hood, the manager is started with `:net_kernel.start/1` on 127.0.0.1
- the Erlang Boot Server is started on first startup so nodes can fetch code and startup scripts
- new nodes are created with the `:slave` module and named from the user prefix plus a number
- Local Cluster loads code paths on the new nodes, copies application environment and Mix environment, and starts required applications
- the result is that the new nodes match the current working node
- the example test starts a cluster, pings three nodes, stops one node, and then stops the manager
- the nodes are linked to the test process, so most tests only need the first two setup lines
