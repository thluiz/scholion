---
title: "Elixir: How to distribute Mnesia between multiple nodes"
date: '2021-06-17T16:54:08-03:00'
category: webclip
summary: 'The article explains how WTTJ used Mnesiac and Libcluster to sync Mnesia stores across nodes, avoid duplicate background work during blue/green deploys, and keep state available in Elixir services.'
tags: ["elixir", "mnesia", "libcluster", "distributed-systems"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Elixir: How to distribute Mnesia between multiple nodes | by WTTJ Tech | Jun, 2021 | Medium"
    url: "https://medium.com/@wttj_tech/elixir-how-to-distribute-mnesia-between-multiple-nodes-cb7c851b1ed1"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2021-06/medium-com--elixir-distribute-mnesia-between-multiple-nodes.md"
    kind: repo
---

The article describes how WTTJ used Mnesia with Mnesiac and Libcluster to keep state synchronized across multiple nodes in Elixir services. The goal was to avoid data loss and duplicate processing during blue/green deployments while keeping the system self-contained on the BEAM.

## Reading notes

- The team needed a way to persist GenServer state for an email service based on saved job searches.
- They chose Mnesia over Redis because Mnesia was already available in the Elixir stack.
- Blue/green deployments could leave two app instances running at once, so both instances had to stay in sync.
- Mnesiac was used to define Mnesia stores, specify table content and types, and handle conflicts between nodes.
- A notification store was defined with `disc_copies` and a conflict resolution callback that logs and copies the store.
- Mnesiac was added to the application config with a Mnesia directory, a list of stores, and `:disc_copies` schema type.
- Libcluster was then used to build and supervise the cluster around the Mnesiac stores.
- The article shows a simple EPMD-based topology with local hosts and a cluster module that initializes Mnesia from `Node.list()`.
- The cluster children include both `Cluster.Supervisor` and `Mnesiac.Supervisor`.
- After adding the cluster to `application.ex`, Mnesia tables can be read and written through transactions.
- Two IEx sessions with matching node names can confirm that the nodes are connected and share data.
- For AWS, the article uses `libcluster_ec2` with EC2 tags and an `ip_to_nodename/2` helper to map IP addresses to Erlang node names.
- The system is described as running in production, processing about 150,000 notifications and sending roughly 30,000 mails per day.
