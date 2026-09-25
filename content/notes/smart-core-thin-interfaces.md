---
title: "Smart core, thin interfaces"
date: '2026-09-25T21:16:15+01:00'
category: webclip
summary: 'The post argues for keeping business logic in a small, smart core and putting actor-specific handling at the edges, where inputs are sanitized and interfaces hide messy details.'
tags: ["software-engineering", "architecture", "modularity"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Smart core, thin interfaces"
    url: "https://swizec.com/blog/smart-core-thin-interfaces/?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/swizec-com--smart-core-thin-interfaces.md"
    kind: repo
---

The post recommends structuring software around a core that knows the domain, commands, and events, with thin interfaces for each actor that needs to interact with it. That separation keeps business rules in one place and keeps edge-specific concerns out of the core.

It says this pattern shows up in several forms, including hexagonal architecture, SOA, microservices, fat models with skinny controllers, state machines, custom hooks, global state managers, and functional core with imperative shell. The practical rule is to sanitize inputs at the edges, expose the public interface, and keep the deeper implementation private so the rest of the codebase does not need to handle every branch.

## Reading notes

- Build a smart core that understands the business domain, events, and commands.
- Surround that core with thin interfaces for different actors such as admins, consumers, APIs, and backend systems.
- Keep shared rules close to the core so they are not repeated across the codebase.
- Repeat code freely when needed, but avoid repeating semantics.
- The same idea appears under names like hexagonal architecture, service-oriented architecture, microservices, fat models and skinny controllers, state machines, custom hooks, global state managers, and functional core, imperative shell.
- Sanitize inputs at the edges so deep logic has fewer exceptions to handle.
- Make the public interface handle the messy cases and keep the internal functions private when possible.
- An interface is any code that translates public commands into internal function calls.
