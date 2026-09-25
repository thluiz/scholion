---
title: "Thinking in Actors - Part 1"
date: '2026-09-25T17:05:09+01:00'
category: webclip
summary: 'The post argues that web apps are better modeled around real business operations and stateful domain behavior than around CRUD, and presents the Actor Model and virtual actors as a way to handle concurrency, distribution, and fault tolerance.'
tags: ["actor-model", "domain-driven-design", "virtual-actors"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Thinking in Actors - Part 1"
    url: "https://jeremycarterau.substack.com/p/thinking-in-actors-part-1?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/jeremycarterau-substack-com--thinking-in-actors-part-1.md"
    kind: repo
---

The post argues that modern web applications are often over-shaped by layers, CRUD endpoints, and database-first thinking. That leads to an anemic domain model, scattered business logic, and difficulty reasoning about workflows, state, and real-world constraints.

It proposes modeling the domain around business operations, behavior, and transitions first, then using the Actor Model and virtual actors to encapsulate state, process messages sequentially, and support distribution, persistence, concurrency safety, and fault tolerance.

## Reading notes

- The series is about “Thinking in Actors” and presents the techniques as a combination of Domain Driven Design and Object-Oriented Programming with finite-state machines.
- Layered web applications with controllers, services, repositories, cache, and SQL can work for a while, but distribution introduces latency, concurrency, consistency, contention, performance, fault tolerance, and observability problems.
- REST endpoints such as `POST /orders` and `PUT /orders/{id}` push developers toward thinking in entities and CRUD instead of business operations and workflows.
- An anemic data model spreads business logic across controllers and services while domain objects stay as data containers.
- Modeling a domain means capturing business processes, behaviors, interactions, people, parties, context, boundaries, rules, constraints, and exceptions.
- The post quotes Amy Fu saying code that matches the fundamental ideas of the product is more likely to survive future product changes.
- State is presented as central to software and especially hard to manage in distributed systems because of concurrency, consistency, scalability, fault tolerance, and observability.
- The desired system would keep business rules, processes, and workflows inside domain objects, enforce valid transitions, support scaling, persistence, debugging, events, retries, and testing without extra complexity.
- The Actor Model is described as a way to reason about state through encapsulation, sequential message processing, isolation, distribution by design, and fault tolerance.
- Virtual actors are presented as uniquely identified, activated on demand, stateful by design, concurrently safe, and fault tolerant.
- The post closes by saying the first step is learning to think in actors, and Part 2 will cover five modeling techniques.
