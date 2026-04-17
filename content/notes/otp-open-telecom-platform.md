---
title: OTP (Open Telecom Platform)
date: '2026-04-04T09:14:51+01:00'
summary: OTP is a collection of middleware, libraries, and design principles for building applications in Erlang. The name stands for Open Telecom Platform — a branding attempt from Ericsson — but neither…
tags: ["software-engineering", "erlang", "concurrency"]
has_commentary: true
sources:
- title: Open Telecom Platform — Wikipedia
  url: https://en.wikipedia.org/wiki/Open_Telecom_Platform
  kind: wiki
---

OTP is a collection of middleware, libraries, and design principles for building applications in Erlang. The name stands for Open Telecom Platform — a branding attempt from Ericsson — but neither Erlang nor OTP is specific to telecom.

In practice, "Erlang" and "Erlang/OTP" are used interchangeably. OTP provides battle-tested abstractions: GenServer (generic server processes), Supervisors (fault-tolerance hierarchies), Applications (packaging and lifecycle), and ETS/Mnesia (in-memory and distributed databases).

The design principles are as important as the code: OTP codifies the "let it crash" philosophy into supervision trees, where each level knows how to restart its children. This is what makes Erlang systems fault-tolerant in practice, not just in theory.

OTP is maintained by the OTP product unit at Ericsson and released as open-source.
