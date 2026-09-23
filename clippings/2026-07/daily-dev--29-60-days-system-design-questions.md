---
url: "https://daily.dev/posts/FC21nqchq?utm_source=notification&utm_medium=email&utm_campaign=digest"
captured_at: "2026-07-06T12:26:09+01:00"
title: "29/60 Days System Design Questions! | daily.dev"
domain: "daily.dev"
---

You have an AI product with 4 specialized agents: a Planner, a Researcher, a Coder, and a Reviewer.

The Planner breaks down the task. The Researcher pulls context. The Coder implements. The Reviewer catches bugs.

Simple on paper. In production, it's falling apart.

Here's what's happening:

• The Researcher sometimes returns before the Planner finishes → Coder gets incomplete context

• The Reviewer flags issues → but there's no retry loop, so bugs ship anyway

• One agent timeout hangs the entire pipeline for 40 seconds

• You have no visibility into which agent failed or why

You need to redesign the orchestration layer. What do you do?

**A)** Centralized orchestrator — one controller calls each agent in sequence, owns retry logic, tracks state in a DB, times out per step individually.

**B)** Choreography via event bus — agents publish/subscribe to events, no central controller, each agent triggers the next autonomously.

**C)** DAG-based execution — model the pipeline as a directed acyclic graph, parallelize independent steps, block only on real dependencies.

**D)** Supervisor pattern — a meta-agent monitors all others, detects failures, decides whether to retry, reroute, or escalate to a human.

All four exist in production AI systems. Only one handles your specific failure modes without introducing new ones.

Pick one — A, B, C, or D — and tell me why. Full breakdown in the comments.

If you're building agentic systems, share this. Most teams hit these exact problems at month 2.

Drop your answer 👇

#30DaysOfSystemDesign #SystemDesign #AgenticAI #AIEngineering

•5w

48.6K

Creator

**Correct Answer: C — DAG-based execution**

Your pipeline has hard dependencies (Coder must wait for BOTH Planner AND Researcher) AND needs retry loops (Reviewer → Coder on failure).

A DAG models this explicitly:

```
Planner ──┐
          ├──► Coder ──► Reviewer
Researcher┘              │
              ◄───────── (retry on failure)
```

What this solves directly:

• **Race condition** → DAG blocks Coder until both upstream nodes complete. No manual checks.

• **Timeout hanging pipeline** → each node has its own deadline. One agent timeout doesn't freeze everything.

• **No retry loop** → retry is a first-class edge in the graph, not bolted-on logic.

• **No visibility** → DAG engines give you a full execution trace per run.

Real implementations: LangGraph, Temporal, AWS Step Functions, Prefect, Dagster. They all converge on this model because it makes dependencies visible, failures local, and execution testable.

**A — Centralized orchestrator (senior engineer trap)**

This is the closest wrong answer. A central controller with per-step timeouts and DB state _feels_ right — it's structured, it has retry logic, it has visibility.

The problem: it's **sequential by default**. Planner and Researcher still run one after the other unless you explicitly add parallel execution logic. You're basically hand-building a DAG imperatively, and you'll do it badly. Every new dependency becomes a code change.

Why it traps senior engineers: it looks like "proper architecture" but it's just imperative orchestration with extra ceremony.
