---
url: "https://calv.info/durable-objects-are-made-for-agents?utm_source=tldrnewsletter"
captured_at: "2026-08-03T10:17:16+01:00"
title: "Durable Objects are Made for Agents"
domain: "calv.info"
---

For the last few months, I've been building almost exclusively with Cloudflare Durable Objects (DOs). They are a wonderful primitive for building products (particularly agents), and I wish more providers out there had a similar offering. There really isn't anything like them in the market.

As I was comparing notes with various friends, I realized that most people haven't really even heard of DOs, and don't understand why they are such a big deal. It's a shame because they really are a near-perfect fit for building agents on top of them.

## What are Durable Objects?

Durable Objects combine a few simple concepts:

1. A serverless V8 isolate for running your code. It spins up and down on demand. You write some form of code that is JS/WASM compatible and it runs within v8. You have access to a subset of Node APIs. Each instance is keyed by ID, so you write code, which then is invoked many times (a la Lambda) but with unique context. This is essentially the same thing a Cloudflare Worker is doing.
2. A paired SQLite instance per DO. You get the ability to read and write to durable storage, and not really have to worry that much about reading and writing from the database.
3. Request routing to a particular isolate. The system that Cloudflare orchestrates in the background is the request routing and spinning up and down of each isolate.

Rather than thinking about your code as a bunch of services which talk to a database, you start thinking about your service as a set of many 'objects' which are event driven by new requests or by timers you can set (called alarms). Each one gets an ID, and requests are routed accordingly to a single isolate by ID.

Once you start thinking this way... you start wanting to make everything a DO. Sticking with the chat metaphor... suppose you are spinning up a Slack clone. You might lay out your data model like WorkspaceDO (name, slug, channels, members) and ChannelDO (name, topic, is_private, messages). When a user loads Slack, they typically want some sort of notification feed on the workspace, and a realtime feed of a channel. You typically don't query across channels (except for a search use case, which can hit a vector store).

## The great parts about DOs

An extremely underrated part of working with DOs is their local dev setup — locally, you run your services using `wrangler`, a CLI that functions as a local env + all-in-one toolkit for working with Cloudflare. It becomes really quick to test changes when your coding agent doesn't rely on Docker or Postgres. Because it's all running SQLite in prod, the production drift for connecting to a DB is fairly minimal.

DOs also run explicitly in a single-threaded manner, so you have to worry less about locking and concurrency — only one invocation of a DO runs against its storage at a time.

Durable Objects also come with native support for websockets, a godsend for fan-out on large-scale notification feeds: you just keep connections warm per-DO and broadcast to any connected listeners.

Binding to other DOs, services, or R2 buckets feels much more intuitive vs AWS or GCP — you specify bindings in `wrangler.jsonc` and get the ability to talk to the service, with no need to think about complex network rules, VPCs, Security Groups, or NAT ingress.

By far the biggest benefit of DOs is that they are super cheap. They only cost you for storage when paused, and all of the author's infra for running a decently sized multi-agent workload was something like $10/mo, where on AWS it's easily 10-50x the cost. Preview environments are close to free, since DOs are cheap and don't cost anything while idle.

As a last bonus, working with Cloudflare infra is extremely token efficient — a chat room implementation requires only a few lines of code, and coding agents that have to explore sprawl across a large codebase tend to slow way down.

## What's harder

DOs had an amazing concurrency model because they're single-threaded, but some functions get marked as having readable/writable gates — if you're not careful, some part of your function may end up sampling from an LLM before writing to storage, and that hangs all your subscribers. The author hit a few cases where agent-generated code would end up blocking read requests for tens of seconds at a time.

He also hit reliability issues (misconfigured gateways to cloud LLM APIs, inability to deploy via the Cloudflare APIs) with less observability or control than AWS/GCP/Azure would offer.

First-class support is Typescript only — Rust, Golang, or Python have fewer options and fewer examples. He ended up using his own types rather than the Wrangler typegen after struggling to get it working properly.

Missing parts of the Node APIs can bite you — HTTP/2 isn't supported for things like gRPC to the Modal APIs, since a worker can't hang for a long time, but it means being careful about library usage, especially around native deps.

Migrations and versioning also get trickier: the way you change data shape within the DO is by adding migration code when the DO wakes, and it's easy to lose track of the current schema state, especially if you didn't wake every single DO. You can effectively never remove old migration paths unless you wake all DOs.

Lastly, many potential customers want the ability to BYO-Cloud, which is understandable for products dealing with sensitive data, and Cloudflare makes it a bit of a non-starter.

## What else is there?

Restate provides a cheap durable execution runtime, similar to a faster/cheaper Temporal, built by the ex-Flink team, leaning heavily into a log structure for handling events and replaying. It has a concept of 'Virtual Objects' with many of the same semantics as a Durable Object (single writer, attached storage), can be self-hosted, and has bindings in Rust and Golang.

Rivet is a new YC company providing infrastructure it calls 'actors', spiritually similar to Cloudflare, leaning heavily into V8 isolates.

Vercel leads the pack of other promising primitives — Workflows, Sandboxes, AI Gateway, Vercel Connect, and Functions create usable primitives you can string together to build long-lived agents, with EVE feeling like the culmination of all of these tools composed in a straightforward manner.
