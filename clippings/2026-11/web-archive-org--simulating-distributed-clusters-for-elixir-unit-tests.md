---
url: "https://web.archive.org/web/20200629141958id_/http://whitfin.io:80/setting-up-distributed-nodes-in-elixir-unit-tests/"
captured_at: "2026-11-16T08:12:11+00:00"
title: "Simulating Distributed Clusters for Elixir Unit Tests"
domain: "web-archive-org"
---

During the recent addition of [distribution to Cachex](https://whitfin.io/cachex-v3-1-and-the-return-of-distributed-caches/), I realised that testing distributed behaviour is quite annoying. Although there's a _tonne_ of useful inside the OTP standard library, it's not particularly obvious if you don't know what you're looking for. Most projects (such as Phoenix) roll their distributed tests around these standard tools directly, which means that there's little out there in terms of utilities for the general masses.

For my use case in Cachex, I needed nothing more than simply being able to start a batch of nodes in a cluster and call over to them via the `:rpc` module. I didn't want to work with anything beyond that, but I also didn't want to roll it all directly in the Cachex test helpers (because I have several other projects which could also benefit here). I figured I might as well separate it out into a small library named [Local Cluster](https://github.com/whitfin/local-cluster). Local Cluster makes it incredibly easy to start a distributed cluster that lives entirely on your local machine, which is perfect for unit testing applications which may have distributed behaviour.

### A Simple API

As mentioned above, the intent was not to create any DSLs, large dependencies, or any unnecessary utilities. As a result, the API is _tiny_. To start a cluster, you have to do no more than the following:

```
# It's required to call this at least once to start
# the manager instance in order to enable clustering.
# Note that calling it multiple times won't cause issue.
:ok = LocalCluster.start()

# Then it's as simple as starting a number of nodes with a prefix
# to designate the cluster. In this case, there will be three nodes
# started together in a cluster of nodes named "my-cluster-1", etc.
[node1, node2, node3] = LocalCluster.start_nodes("my-cluster-", 3)
```

Calling `start_nodes/2` will link the created nodes to the current process, which makes it great for unit testing with ExUnit as it means that clusters are automatically cleaned up at the end of your tests. If you want a cluster to live across a number of tests, you can start it in your `setup/0` block (inside an Agent or something), and clean it up in your `teardown/0`.

The `start_nodes/2` function will return a list of node names in the cluster, which can then be used with the `:rpc` module to call out to in order to run code on the started nodes. Note that the current node (i.e. the current VM) will not be returned in this list - all instances are started at call time. You can call `stop_nodes/1` with the nodes listing to terminate manually at any point. If you wish to fully disable local clusters on your current VM, you can call `stop/0` to stop it acting as a manager.

### How It Works

Local Cluster uses the tool provided by the standard library to provide a very basic interface to the user. Under the hood, Local Cluster starts a single process in the current BEAM instance which acts as the manager for a cluster (although without directly existing in the cluster). When you then start a cluster, BEAM simply spawns a number of new VM instances to act as workers in the cluster, and assigns names to them based on a prefix provided by the user (for namespacing).

Starting the manager is done via `:net_kernel.start/1` from the OTP standard library, using 127.0.0.1 as the host to begin the manager on. On the initial startup the Erlang Boot Server is also started - this server is required to start nodes on the same machine as it enables retrieval of code and the VM startup scripts.

To create a local cluster, the user provides a binary to identify the cluster as well as a number of nodes to start in the cluster (which can be any number greater than 0). This will then start a number of nodes on the same machine using the `:slave` module, and link them to the current process. These nodes will be named `${prefix}${number}` for consistency in naming; a prefix of `"my-worker-"` will result in nodes names `:my-worker-1` and so on.

Just starting the nodes themselves is insufficient; the runtime must also be available. To ensure this is the case, Local Cluster will then RPC on the started nodes to load all currently available code paths. Once the code paths are loaded, it will then copy all environment configuration (i.e. the stuff in `Application.get_env/2`) and the Mix environment, before starting all required applications. At this point, all nodes in the new cluster should match the state of the current working node.

### Example ExUnit Testing

Because this was designed to be only a small convenience API, it's trivial to use Local Cluster inside an ExUnit test. Here's an example, which demonstrates simply pinging nodes:

```
defmodule MyTest do
  use ExUnit.Case

  test "something with a required cluster" do
    :ok = LocalCluster.start()

    nodes = LocalCluster.start_nodes("my-cluster", 3)

    [node1, node2, node3] = nodes

    assert Node.ping(node1) == :pong
    assert Node.ping(node2) == :pong
    assert Node.ping(node3) == :pong

    :ok = LocalCluster.stop_nodes([node1])

    assert Node.ping(node1) == :pang
    assert Node.ping(node2) == :pong
    assert Node.ping(node3) == :pong

    :ok = LocalCluster.stop()

    assert Node.ping(node1) == :pang
    assert Node.ping(node2) == :pang
    assert Node.ping(node3) == :pang
  end
end
```

This is wonderfully easy; first of all we ensure that Local Cluster has been correctly initialized via `LocalCluster.start()`. Regardless of whether we've called this before, we call it now due to the potential re-ordering of tests. Then we start worker nodes via `LocalCluster.start_nodes("my-cluster-", 3)`, which will create 3 nodes (you can see that in the match on the line afterwards). Although you can't see it above, these nodes will be named `my-cluster-1`, `my-cluster-2` and `my-cluster-3`.

This returns us our list of started nodes, and we ping each node using `Node.ping/1` to ensure that we can see them all. Once this is confirmed we stop the first node and re-run the check. At this point pinging the first node does indeed tell us that it's unavailable, but the other two nodes are good to go. Finally we stop the entire manager instance, which stops all nodes.

You should note though, that stopping the nodes in the test above is simply to show off the API. Because the nodes are linked to the current process, the cluster will be automatically stopped when the current test process dies. This means that for most cases, you simply need the first two lines of the above test to work with a local cluster. Try it out and let me know what you think!
