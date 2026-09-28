---
title: "Building Distributed Systems with Elixir — 02: Correlated Request–Reply"
date: '2026-09-28T15:10:20+01:00'
category: webclip
summary: 'The article shows how to pair each asynchronous request with a unique reference so a client can match the right reply, even when one process makes several requests.'
tags: ["elixir", "request-reply", "selective-receive", "distributed-systems"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Building Distributed Systems with Elixir — 02: Correlated Request–Reply"
    url: "https://dev.to/pckrishnadas88/building-distributed-systems-with-elixir-02-correlated-request-reply-4b2a"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--building-distributed-systems-with-elixir-02-correlated-reque.md"
    kind: repo
---

The article explains that a PID tells the server where to send a response, but it does not identify which request the response belongs to. To solve that, the client creates a unique reference with `make_ref/0` and sends it with the request, while the server returns the same reference in the reply.

The client then uses selective receive with `^ref` to match only the reply for that request, leaving other messages in the mailbox. The pattern works with one client or many, and the article closes by pointing to process monitoring as the next step.

## Reading notes

- A PID identifies the process, not an individual request.
- `make_ref/0` creates a unique request identifier.
- The server receives `{:request, from, ref, value}` and replies with `{:reply, ref, result}`.
- The client matches replies with `{:reply, ^ref, result}`.
- Unmatched messages stay in the mailbox, which is selective receive.
- One process can send several requests and keep the same PID while each request gets a different reference.
- The pattern also works when multiple client processes talk to the same server.
- Processes are for concurrency and isolation, while references are for identifying operations.
- The next topic in the series is process monitoring and `:DOWN` messages.

## Series

*Building Distributed Systems in Elixir*, by krishnadaspc. Research: [Distributed Systems Patterns](/research/distributed-systems-patterns).

- [Part 1 — Stateful Process Without GenServer](/notes/building-a-stateful-process-in-elixir-without-genserver)
- **Part 2 — Correlated Request–Reply**
- [Part 3 — Process Monitoring](/notes/building-distributed-systems-in-elixir-part-3-process-monito)
- [Part 4 — Process Linking](/notes/building-distributed-systems-in-elixir-part-4-process-linkin)
- [Part 5 — Supervisor From Scratch](/notes/building-distributed-systems-in-elixir-part-5-supervisor-fro)
- [Part 6 — Named Processes](/notes/building-distributed-systems-in-elixir-part-6-named-processe)
- [Part 7 — Worker Pool](/notes/building-distributed-systems-in-elixir-part-7-worker-pool)
- [Part 8 — Publish / Subscribe](/notes/building-distributed-systems-in-elixir-part-8-publish-subscr)
- [Part 9 — Backpressure](/notes/building-distributed-systems-in-elixir-part-9-backpressure)
