---
title: "Elixir: How to distribute Mnesia between multiple nodes"
date: '2021-06-17T20:36:46-03:00'
category: webclip
summary: 'The article shows how WTTJ uses Mnesiac and Libcluster to sync Mnesia stores across nodes, avoid duplicate background work during blue-green deploys, and keep data available across instances.'
tags: ["elixir", "mnesia", "libcluster", "distributed-systems"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Elixir: How to distribute Mnesia between multiple nodes | by WTTJ Tech | Jun, 2021 | Medium"
    url: "https://medium.com/@wttj_tech/elixir-how-to-distribute-mnesia-between-multiple-nodes-cb7c851b1ed1"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2021-06/medium-com--elixir-how-to-distribute-mnesia-between-multiple-nodes.md"
    kind: repo
---

The article explains how WTTJ kept background state inside Mnesia and then distributed that state across multiple nodes so deployments would not lose processed data. The setup is used to keep GenServers from repeating work during blue-green deploys and to let a new instance continue from the previous one.

## Reading notes

- WTTJ uses Elixir on the BEAM and relies on Mnesia as an embedded distributed database instead of an external service.
- The service discussed builds and sends emails from saved job searches, with GenServers processing data in the background.
- The team chose Mnesia for state storage because Redis was not already set up for this instance and Mnesia was available out of the box.
- Blue-green deployments created a need to keep two running instances in sync so the same emails would not be sent twice and the new instance could continue processing.
- Mnesiac is used to define and manage Mnesia clusters, while Libcluster supervises the cluster setup.
- A store is defined for notifications, including record shape, field types, and conflict handling during synchronization.
- The store configuration uses `disc_copies` and a Mnesia directory based on the node name.
- The store can then be accessed through normal Mnesia transactions inside the application.
- Libcluster is configured with a simple EPMD topology for local nodes before moving to a cluster managed by application processes.
- The cluster module starts Mnesia with the current node list and adds both a Cluster.Supervisor and a Mnesiac.Supervisor.
- The cluster is added to the application supervision tree so it starts with the rest of the processes.
- The setup allows writing to Mnesia on one node and reading the same data from another node.
- The article also shows how to use ClusterEC2.Strategy.Tags with Libcluster_EC2 on AWS EC2 instances.
- An `ip_to_nodename/2` helper maps IP addresses to Erlang node names.
- The system is reported to run in production, processing about 150,000 notifications and sending roughly 30,000 mails per day.
