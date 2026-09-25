---
title: "Ports and Adapters (Hexagonal Architecture), Explained with Two Real Codebases"
date: '2026-06-04T17:12:19+01:00'
category: webclip
summary: 'Explains how ports, adapters, and a registry keep business logic independent from vendors, making payment, email, and frontend API changes cheaper and easier to migrate.'
tags: ["hexagonal-architecture", "dependency-inversion", "adapters", "software-architecture"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Ports and Adapters (Hexagonal Architecture), Explained with Two Real Codebases — Saad Hasan"
    url: "https://saadh393.github.io/blog/adapter-port-architecture-two-cases"
    kind: repo
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-06/saadh393-github-io--ports-and-adapters-hexagonal-architecture-explained-with-two.md"
    kind: repo
---

The post argues that the main problem is not integrating with a vendor, but letting vendor-specific code spread through the codebase. Its solution is to put a port between business logic and the outside world, use adapters for each provider, and let a registry choose the active implementation at runtime.

It illustrates the pattern with two backend refactors and one frontend migration. In the backend, moving from direct SDK calls to ports and adapters made it possible to add Stripe beside bKash, then switch email providers with only the wiring changed. In the frontend, static adapters let the team build against agreed response shapes before the backend was ready, so components did not need to change when real endpoints arrived.

## Reading notes

- The pain comes from integration code leaking into many files, not from writing one integration file.
- A port is an interface in the domain’s own language, with no SDK names or HTTP details.
- An adapter wraps one provider and translates between the provider and the port.
- A registry decides which adapter is active at runtime, while business logic depends only on the port.
- In the payment example, adding Stripe required one new adapter file and one change in the registry.
- When bKash changed its response shape, the fix stayed inside the bKash adapter.
- In the email example, many different sending patterns were replaced by one Mailer port.
- Migration happened gradually, one calling site at a time, until switching providers became a one-line registry change.
- Retry logic and audit logging became easier once they lived behind the port.
- On the frontend, components called repository functions while the registry switched between in-memory data and real fetch calls.
- Static adapters matched the future API shapes, letting frontend and backend work in parallel.
- Tests became simpler because they could use fake adapters instead of module mocking.
- The pattern costs more files and a small debugging hop, so it is not meant for every dependency.
- The rule of thumb is to build a port when there are two implementations or a real plan for a second one.
- The author would design the port before writing the first adapter, and keep the fake adapter after shipping.
