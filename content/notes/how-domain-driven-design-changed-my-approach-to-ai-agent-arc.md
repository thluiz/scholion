---
title: "How Domain-Driven Design Changed My Approach to AI agent architecture"
date: '2026-06-04T17:25:30+01:00'
category: webclip
summary: 'The author says Domain-Driven Design changed how he sees software design, helping him isolate the core domain of an AI coding platform and model agents through events instead of direct calls.'
tags: ["domain-driven-design", "ai-agents", "software-architecture", "bounded-context"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How Domain-Driven Design Changed My Approach to AI agent architecture"
    url: "https://www.jigjoy.ai/blog/ddd-applied-to-agent-orchestration?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-06/jigjoy-ai--how-domain-driven-design-changed-my-approach-to-ai-agent-arc.md"
    kind: repo
---

The author says Eric Evans’ _Domain-Driven Design_ changed his view of programming after years of software work and startup building. He connects that shift to his own AI coding platform, where growing complexity pushed him to look for clearer domain boundaries and a richer model of the system.

## Reading notes

- The book made him care more about clean code, architecture, and thoughtful design while building a vibe coding platform.
- His earlier microservice experience taught him that splitting a monolith without domain understanding creates latency, DevOps overhead, and awkward services with little business meaning.
- He now sees business and development as connected, not separate.
- He says the book requires slow reading because details like entities, value objects, object lifecycle, class names, method names, relationships, and side effects matter.
- He links DDD to deeper insight into complex domains and says insight comes from domain knowledge and repeated refactoring.
- He uses domain distillation to separate a platform into subdomains and identify the core domain.
- For his own platform, he lists user account and billing, project planning, project deployment, observability, version control, and AI coding, and identifies AI coding as the core domain.
- He says the domain should be modeled, not technology, and the domain layer should stay isolated from infrastructure.
- He describes a four-layer structure: UI, application, domain, and infrastructure.
- He says the domain layer should not call the file system, send HTTP requests to an LLM, depend on a framework, or talk to external APIs directly.
- He says the domain layer should not be anemic and must contain real business logic.
- While building Mozaik, a TypeScript framework for orchestrating AI agents, he moved orchestration toward events.
- He separates inference into an Inference Runner and function call execution into a Function Call Runner.
- He models agents so they notify runners through an observer and then react to results without infrastructure leaking into the domain.
- He says this makes agents non-blocking and suggests asynchronous, event-driven agents open more possibilities than synchronous ones.
