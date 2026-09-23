---
title: "From Microservices to Modular Monoliths"
date: "2026-09-23T18:08:37+01:00"
category: webclip
has_commentary: false
summary: "Argues that teams stuck in microservice hell should migrate back to modular monoliths, keeping modularity without distributed-system overhead."
tags:
  - microservices
  - modular-monolith
  - software-architecture
sources:
  - title: "From Microservices to Modular Monoliths - Ardalis (Steve Smith)"
    url: "https://ardalis.com/from-microservices-to-modular-monoliths/?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/ardalis-com--from-microservices-to-modular-monoliths.md"
    kind: repo
---

Steve Smith argues that teams who broke a legacy monolith into microservices and landed in "microservice hell" don't need to live there. A modular monolith keeps the same modularity, with modules talking to each other through well-defined interfaces, but drops the distributed-system tax: no network latency, no partial failures, no bandwidth games between services.

He's blunt about who benefits from microservices beyond what a given system needs: cloud vendors selling hosting and management tooling, consultants billing for the migration and the scaling work that follows, and developers padding a resume with distributed-systems experience.

## Fichamento

- Microservices break a monolith into smaller, independently scalable pieces, but bring their own management, latency, and complexity costs as the number of services grows.
- Cloud vendors, consultants, and developers chasing resume-driven development all have incentives to push microservices past what the problem requires.
- A modular monolith keeps functional separation through well-defined module interfaces, while staying a single deployable, avoiding the fallacies of distributed computing.
- Modularity still carries its own complexity: keeping modules independent while letting them communicate efficiently.
- Migrating from microservices back to a modular monolith takes deliberate planning, not just a reversal of the original split.
