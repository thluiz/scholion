---
title: "AI Is Forcing Us To Write Good Code"
date: "2026-09-23T18:23:09+01:00"
category: webclip
has_commentary: false
summary: "A six-person team enforces 100% code coverage, thoughtful file naming, and fast disposable dev environments because coding agents need the guardrails humans used to skip under deadline pressure."
tags:
  - ai-agents
  - software-engineering
  - code-quality
  - developer-tools
sources:
  - title: "AI Is Forcing Us To Write Good Code - by Steve Krenzel"
    url: "https://bits.logic.inc/p/ai-is-forcing-us-to-write-good-code?utm_source=weeklyfoo&utm_medium=email&utm_campaign=weeklyfoo"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/bits-logic-inc--ai-is-forcing-us-to-write-good-code.md"
    kind: repo
---

Steve Krenzel argues that practices teams have called "best practice" for decades (thorough tests, small modules, static typing) were always the first casualty of deadline pressure because they were optional. Coding agents change the incentive. An agent left without those guardrails behaves like a Roomba that rolls over dog waste and spreads it through the house: it makes a mess and doesn't reliably clean it up on its own.

His six-person team's response is a set of specific, sometimes controversial investments built around that idea, treating the agent's working environment as the actual lever on code quality, not the model itself.

## Fichamento

- The team requires 100% code coverage, not as a bug-prevention metric but as a guarantee that the agent has demonstrated, with an executable example, how every line it wrote behaves.
- Krenzel argues 100% is a qualitatively different target from 95% or 99.99%: at 100%, any uncovered line is unambiguously something just introduced, removing the judgment calls about what's "important enough" to test.
- Directory structure and file naming are treated as an interface for the agent, since agentic tools navigate the codebase mostly through the filesystem; a path like `./billing/invoices/compute.ts` communicates more than `./utils/helpers.ts` even with identical code inside.
- Many small, well-scoped files are preferred because agents summarize or truncate large files pulled into context, while a short file can stay loaded in full.
- Dev environments need to be fast, ephemeral, and concurrent: guardrails have to run cheaply enough to execute constantly, spinning up a new environment has to take seconds through a single command, and multiple environments need to run in parallel without conflicts over ports, databases, or caches.
- The team leans on TypeScript with semantically meaningful type names (UserId, WorkspaceSlug, SignedWebhookPayload) so a model can immediately identify what kind of data it's handling, plus OpenAPI-generated clients and Postgres constraints to push correctness checks into the type system and database rather than relying on the agent to get it right unaided.
