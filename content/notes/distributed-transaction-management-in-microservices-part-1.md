---
title: "Distributed Transaction Management in Microservices — Part 1"
date: '2022-06-23T14:40:56-03:00'
category: webclip
summary: 'The article explains why distributed transactions are hard in microservices, compares them with monoliths, and outlines 2PC and 3PC before motivating asynchronous Saga patterns.'
tags: ["microservices", "distributed-transactions", "two-phase-commit", "three-phase-commit"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Distributed Transaction Management in Microservices — Part 1 | by Dineshchandgr | Jun, 2022 | Dev Genius"
    url: "https://blog.devgenius.io/distributed-transaction-management-in-microservices-part-1-bb7dc1fbee9f"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-06/blog-devgenius-io--distributed-transaction-management-in-microservices-part-1.md"
    kind: repo
---

The article defines a transaction as a set of actions that must all succeed, with rollback needed if one step fails. It contrasts monoliths, where one service and one database can commit or roll back the whole unit, with microservices, where each service owns its database and distributed ACID behavior becomes difficult.

## Reading notes

- A transaction is a series of actions that must succeed together, and failures require rolling back to the previous stable state.
- In a monolith, the transaction boundary stays inside one application and one database, so all steps can be committed or rolled back together.
- In microservices, each service handles part of the business flow and keeps its own database, so the overall transaction is distributed.
- The example flow includes cart, order creation, stock reduction, invoice generation, payment, and email notification.
- The article says distributed transaction management should be avoided if possible.
- If it is needed, the article lists synchronous patterns and asynchronous Saga patterns.
- Two-Phase Commit uses a coordinator and two stages, prepare and commit.
- In the success case, services prepare, send prepared responses, and then commit after the coordinator receives all responses.
- In the rollback case, one failed response leads the coordinator to send abort and roll back changes.
- The drawbacks of 2PC are slowness and locking in every database until commit or abort.
- Three-Phase Commit extends 2PC by splitting commit into more stages and adding prepare-to-commit for fault tolerance.
- The article says 3PC helps recovery when the coordinator or a service fails during the commit phase.
- It also says 3PC still needs careful implementation to avoid problems with network partitioning and adds overhead.
- The article motivates asynchronous patterns because 2PC and 3PC are blocking and synchronous, which creates long locks and possible deadlocks.
- It ends by saying Saga-based patterns rely on eventual consistency and will be covered next.
