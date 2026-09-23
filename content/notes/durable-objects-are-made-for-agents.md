---
title: "Durable Objects are Made for Agents"
date: "2026-09-23T18:36:05+01:00"
category: webclip
has_commentary: false
summary: "Argues Cloudflare Durable Objects are a near-perfect primitive for building agents, combining a per-ID V8 isolate, paired SQLite storage and native websockets at roughly a tenth of AWS's cost."
tags:
  - cloudflare
  - durable-objects
  - ai-agents
sources:
  - title: "Durable Objects are Made for Agents"
    url: "https://calv.info/durable-objects-are-made-for-agents?utm_source=tldrnewsletter"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-08/calv-info--durable-objects-are-made-for-agents.md"
    kind: repo
---

A Durable Object combines three things: a serverless V8 isolate keyed by ID, a paired SQLite instance for durable storage, and Cloudflare's own request routing to the right isolate. That combination reframes an app as a set of event-driven objects rather than services talking to a shared database. Each object runs single-threaded, so only one invocation touches its storage at a time, and it comes with native websocket support, which the author calls a godsend for fan-out on large notification feeds.

The author's own multi-agent workload runs at roughly $10/month on this setup, where the same footprint on AWS would cost 10 to 50 times more. Local dev through `wrangler` mirrors production closely since everything runs SQLite, and bindings to other DOs, services or R2 buckets skip the VPC and security-group configuration AWS or GCP would require.

## Fichamento

- The concurrency model has a sharp edge: some functions carry readable/writable gates, and an LLM call left inside one before a storage write can hang every subscriber for tens of seconds.
- First-class support is Typescript only; Rust, Golang and Python have fewer examples and options, and the author gave up on Wrangler's typegen in favor of hand-written types.
- Migrations require adding code that runs when a DO wakes, and tracking current schema state gets hard if some DOs never wake to pick up a migration.
- BYO-Cloud isn't really on the table, which the author flags as a blocker for customers handling sensitive data.
- Restate (Virtual Objects, self-hostable, Rust/Golang bindings) and Rivet (V8-isolate-based actors, from YC) are named as the closest comparisons; Vercel's Workflows/Sandboxes/AI Gateway stack is called the most promising alternative primitive set overall.
