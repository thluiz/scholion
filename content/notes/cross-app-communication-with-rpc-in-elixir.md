---
title: "Cross-App Communication with RPC in Elixir"
date: "2026-09-23T19:05:10+01:00"
category: webclip
has_commentary: false
summary: "How Gearflow connects two Phoenix apps over distributed Erlang RPC instead of HTTP, and the coupling trade-off they accepted to skip building an internal API."
tags:
  - elixir
  - distributed-systems
  - software-architecture
sources:
  - title: "Cross-App Communication with RPC in Elixir"
    url: "https://blog.gearflow.com/cross-app-communication?utm_medium=email&utm_source=elixir-radar"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/blog-gearflow-com--cross-app-communication-with-rpc-in-elixir.md"
    kind: repo
---

Gearflow runs two Phoenix applications maintained by the same team and needed them to share data. Instead of an HTTP API, a message queue, or a shared database, they used distributed Erlang: nodes that share a secret cookie call each other's functions directly through `:rpc.call`, reusing the same GraphQL schema and resolvers both apps already expose through Absinthe, just over a different transport.

The team names the cost up front. Calling into another app's modules as if they were local creates implicit coupling: no API contract, no versioning, no compile-time warning when a remote function signature changes. Their bet is that catching an occasional breaking change quickly costs less than maintaining internal API infrastructure every day, given that the two apps already share a deploy pipeline and a Slack channel for coordinating releases.

## Fichamento

- The standard alternative, an internal API, was rejected for now: authentication between services, HTTP connection pools, retries, circuit breakers, schema versioning, and documentation are real costs that Gearflow judges premature at their current team size.
- Node discovery, not the RPC call itself, was the harder problem. `libcluster`'s DNS-poll strategy failed because Fly.io appends an image hash to each node name, and the static basename it expects doesn't account for that.
- The fix was a custom `libcluster` strategy that resolves DNS to IPs, queries EPMD directly on each IP for the real node names, and filters by prefix to find the right ones.
- The approach is scoped explicitly: both apps on the BEAM, both codebases under the team's control, a trusted network (same Fly.io org, same VPC). Different languages, separate-team ownership, or an untrusted network boundary rule it out.
- Production setup is a shared `RELEASE_COOKIE` secret across both Fly apps plus a pointer telling one app the other's name; after that, nodes discover each other and a cross-app query is a single function call.
- The migration path out, if the coupling bet stops paying off, is swapping `:rpc.call` for HTTP while keeping the same GraphQL queries.
