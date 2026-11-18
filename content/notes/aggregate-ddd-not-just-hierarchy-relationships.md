---
title: "Aggregate (DDD) isn’t hierarchy & relationships"
date: '2023-10-24T14:26:35+00:00'
category: webclip
summary: 'Argues that aggregates in DDD should be designed around behavior, invariants, and consistency boundaries, not around entity hierarchies and data relationships alone.'
tags: ["ddd", "aggregates", "cqrs", "software-architecture"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Aggregate (DDD) isn’t hierarchy & relationships"
    url: "https://codeopinion.com/aggregate-ddd-isnt-hierarchy-relationships/?utm_content=bufferd631e&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/codeopinion-com--aggregate-ddd-not-just-hierarchy-relationships.md"
    kind: repo
---

The post explains that many developers design aggregates by focusing on entity hierarchies and relationships instead of behaviors and invariants. Using a route–location–vending machine example, it shows how modeling only object relationships leads to an anemic design that lacks real business logic and could be handled with database constraints and transaction scripts. An aggregate is described as a consistency boundary used to enforce invariants, so only data involved in these invariants belongs in the aggregate. This perspective naturally leads to CQRS, where command models use aggregates for state changes and query models read data directly. Reframing the example around behavior, the vending machine becomes its own aggregate that raises alarms as events, while a separate route/location aggregate consumes those events when needed, especially for querying alarmed routes.

## Reading notes

- Many developers approach aggregate design by thinking primarily about data, hierarchies, and relationships between entities.
- The example domain involves a bus route with multiple locations (bus stops), each location having one vending machine that emits telemetry and alarm events.
- An initial model focuses on wiring up entities (Route, Location, VendingMachine) and their relationships, with minimal behavior beyond the vending machine triggering an alarm.
- This relationship-focused model builds an object hierarchy without capturing meaningful business logic, leaving most rules to database constraints or simple transaction scripts.
- The author questions whether such a relationship-only model really needs an aggregate, given that a database can enforce referential integrity.
- Aggregates are described as clusters of related objects where “related” means tied together by the invariants that must be enforced.
- The key reason to use an aggregate is to enforce invariants and act as a consistency boundary during state changes.
- Only state involved in enforcing invariants or consistency needs to live inside an aggregate; other data has no purpose there.
- This leads to the idea that exposing extra data (like alarm counts or last alarm dates) from the aggregate may be unnecessary for enforcing invariants.
- Differentiating between models for commands and queries naturally aligns with CQRS: commands use aggregates for state changes and invariants, while queries can read the data store directly.
- CQRS is explained as using separate paths for reads and writes, not necessarily separate data stores; both paths can share the same database.
- Rethinking the domain around behavior, the vending machine is modeled as its own aggregate that can trigger an alarm event independently.
- A separate aggregate that includes Route and Location can subscribe to or consume vending machine alarm events if it needs to be aware of alarms.
- This event consumption is especially useful for query needs, such as identifying routes that have locations with vending machines in an alarmed state.
- The post concludes that treating aggregates as mere hierarchies of related entities comes from a data-first mindset, while their real role is to define consistency boundaries and enforce invariants tied to behaviors.
- Without understanding the behaviors, you cannot know which invariants to enforce, and you end up with a pure object model hierarchy instead of a true aggregate, adding complexity that a simple data model and transaction scripts could handle.
