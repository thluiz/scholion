---
url: "https://jeremycarterau.substack.com/p/thinking-in-actors-part-1?ref=dailydev"
captured_at: "2026-09-25T17:05:09+01:00"
title: "Thinking in Actors - Part 1"
domain: "jeremycarterau-substack-com"
---

Recently some posts I’ve made on Reddit and Hacker News have garnered some interest. Usually, I’m posting something about the Actor Model or some form of state management. Several users have messaged me with, “I’m interested in what you wrote, did you write any blog about it?” and “I would like to understand more how it works”.

In this series of blog posts I’m going to talk about “Thinking in Actors”. The techniques are not anything novel, they’re just a mashup of old techniques found in Domain Driven Design and Object-Oriented Programming (utilizing Finite-state machines).

*   Part 1 - Challenging your software modelling techniques to be simpler
    
*   [Part 2 - Welcome to a world of ordered thinking](https://jeremycarterau.substack.com/p/thinking-in-actors-part-2)
    
*   [Part 3 - Learning to fly with digital wings](https://jeremycarterau.substack.com/p/thinking-in-actors-part-3)
    

Architectural patterns always evolve, reflecting the technological constraints and business demands of their time. Currently the File → New Web Application has become a distributed microservice architectural mashup of stateless applications that are independent, yet dependant - somewhat paradoxical. But when you simplify it a modern web application is made up of layers.

Now I’m no expert on the history of any of this, but every software developer has probably been exposed to some kind of layered architecture. We tend to categorize components into layers of best fit and then debate it with our peers when they disagree - but ultimately everything can be categorized.

So, you use the current “best practice” and create a simple web application. It might employ a controller, service and repository layer, and you’ll connect it to your SQL database and you’re set! You’ve got a table called `order` and `order_item`. You write a controller `OrderController` it will talk to the `OrderService` and then it will use the `OrderRepository`. You connect up the system to some kind of cache and pump out some more features.

For most applications something like this works well. That is until you need to distribute it (because it’s in the File → New Web Application mandate). So again, you look around and see what “best practice” is. You put in some form of load balancing, place an API gateway in front of it, add more caching. Standing 10ft back you look at your system, and you observe a whole new set of **challenges**: network latency, concurrency, data consistency, contention, database performance, fault tolerance, and observability.

So, are all of the prescribed layers necessary? Are each of these challenges independent or do they have an underlying root cause?

At first glance you could assume that our new challenges are all independent and can be solved in some kind of layered fashion.

Putting APIs directly in front of the database seems like a straightforward solution: expose endpoints that perform CRUD operations, and let the database do the heavy lifting. It seems perfect because the web is stateless, and each request is its own operation. Sadly, this approach oversimplifies the complexities of actual real-world applications.

The problem starts with our data model and how we interact with it. Here's why:

An [anemic data model](https://martinfowler.com/bliki/AnemicDomainModel.html) is easy to spot. There are domain objects everywhere, simply reduced to DTO’s without encapsulating any behaviour or business logic. Instead of rich, meaningful and well modelled objects, we see properties that are modified by business logic scattered in layers such as the controller or service.

When you have a lack of encapsulation you see a disjointed system, making it harder to understand the complete logic flow.

Here’s an example of an anemic data model:

[

![](https://substackcdn.com/image/fetch/$s_!4IUq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb0f11511-520f-4428-a82e-7b07ba81050d_3944x5228.png)

](https://substackcdn.com/image/fetch/$s_!4IUq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb0f11511-520f-4428-a82e-7b07ba81050d_3944x5228.png)

Business rules and domain logic rarely relate 1:1 with a database operation. Because most of us are taught to think in terms of relational databases we tend to think in rows and tables.

For example, it's tempting to think of operations like "place an order" or "add an item to an order" as simple `INSERT` or `UPDATE` statements on `order` or `order_item` tables. However, unless you’re writing a Hello World application for your university assignment these operations are **never** that simple. Typically, they involve multiple steps, such as validation, communication with other systems, state transitions, or complex business rules.

RESTful API patterns, whilst commonly used and beneficial in many scenarios, have inadvertently reinforced the notion of thinking in terms of **entities** instead of **business operations**. Endpoints like `POST /orders` or `PUT /orders/{id}` encourage developers to see APIs as direct mappings to database tables, where each request corresponds to a CRUD operation or some kind of database mutation.

When you expose an API chances are you are actually exposing a **process** or **workflow**. Somehow we've exposed the entities via API to our customers and not the actual operations they want to do. So why do we do that?

If all you have is a hammer, you treat everything as a nail.

As developers, it’s tempting to approach software challenges as purely technical problems. Often, we’re tasked to “fix the problem” and so we focus on patching symptoms. When we are in this mindset it’s easy to Google the problems individually: Concurrency? Put in some distributed locking mechanism. Database performance? Add more cache. Fault tolerance? Add retry mechanism and [idempotency](https://developer.mozilla.org/en-US/docs/Glossary/Idempotent). While these solutions may work in isolation, they fail to address the underlying cause: the misalignment between the software and the business domain it serves.

They say all problems are a communication problem. Coincidentally in this case the root cause of our problem lies with how we’ve modelled our [domain](https://en.wikipedia.org/wiki/Domain-driven_design) - we've miscommunicated our domain model to our code. Could it be that we didn’t quite understand the business domain at the start? Could it be that we skipped applying domain driven design techniques? Could it be that we modelled our software as if they were tightly coupled to the data models and paradigms of our database? Did we focus on database schemas and the code rather than the customers problem?

Modelling your domain is more than creating data structures, it’s about capturing business processes, behaviours and interactions. The end goal is a model that is rich enough that it truly reflects the real-world.

When you have an anemic data model we see objects in our system that are just data containers - without meaningful behaviour. A more domain driven approach would have us encapsulate business logic, state and behaviour inside the domain object itself.

When modelling we need to consider:

*   The critical problems, people and parties
    
*   The naive operation the user wants to do, and what they want to achieve
    
*   The state and behavior (operations, workflows, processes)
    
*   The context and boundaries
    
*   Real world rules, constraints and exceptions
    

Amy Fu recently [blogged](https://testing.googleblog.com/2024/09/write-change-resilient-code-with-domain.html) and I quote:

> **if we write code that matches the fundamental ideas of the product, it will be more likely to survive future product changes**.

It’s actually so simple - model the system based on the ideas first, behaviours and state second. Why does this matter?

State is a fundamental concept in software development - it represents the system’s knowledge of the world and drives behavior. It’s considered a double edge sword. On one hand almost every application will have some form of state, and on the other hand managing it is complex, especially when the system is distributed, concurrent or needs to be fault tolerant.

When replicating a bug, you are in essence attempting to get the system in the defective state and reason against its values. If every operation and interaction is considered a potential state change, then why don’t we design and model our state in such a way that it can be isolated and interrogated?

When we distribute a system, the management of state becomes a key challenge. Here's why:

1.  **Concurrency**: Multiple components or users may interact with the same piece of state simultaneously. Without proper handling, this leads to race conditions, stale data, or corruption.
    
2.  **Consistency**: In distributed systems, maintaining a consistent view of state across nodes is notoriously difficult.
    
3.  **Scalability**: State can become a bottleneck when multiple components need to access or modify it. Some systems partition/aggregate state but this can be complex.
    
4.  **Fault Tolerance**: Distributed systems must recover from failures. Ensuring state consistency during node crashes, network partitioning, retries and deployments requires additional design. When something retries will it be in the same state?
    
5.  **Observability**: Debugging issues across many components or services can be difficult. What state was available to the component at the time the request was made?
    

Given these challenges, many modern systems lean toward stateless architectures wherever possible. In a simple Controller-Service-Repository web application where exactly is our state?

If we’ve already modelled our domain in a rich real-world manner, how can we bring it to life? Can we make it stateful? If so, what would that look like?

What do we need to better manage our state? In an ideal world, this is kind of what we want:

1.  I don’t want to write everything in controllers, services and repositories. There are rich parts of my domain where state and behaviour need to be properly managed.
    
2.  Business rules, processes and workflows should live within the domain objects, ensuring that the logic is cohesive and centralized.
    
3.  I want to be able to express the domain logic clearly and succinctly so that everything the `Order` manages is encapsulated in the one place.
    
4.  I want to be able to define state machines and transitions so that the system is well guarded against incorrect states.
    
5.  Domain objects should scale naturally with the system, supporting partitioning and sharding without additional complexity.
    
6.  I don’t want to have to build locking mechanisms to handle concurrency.
    
7.  I don’t want to have to build queuing mechanisms for out of order messages.
    
8.  The system should natively support and enforce valid state transitions, reducing the risk of invalid or inconsistent states.
    
9.  State persistence should be seamless, in a way that is transparent to the developer.
    
10.  I want to be able to easily debug the state of things, I want to be able to easily inject the exact state so I can replicate the bug.
     
11.  The domain model should support emitting and reacting to domain events, enabling easy integration with other systems and workflows.
     
12.  I don’t want to bake in custom retry and fault tolerance mechanisms.
     
13.  The system should support both horizontal and vertical scaling without any additional complexity.
     
14.  I want to be able to test the integration of domain objects without any additional complexity.
     

The Actor Model offers a structured approach to reasoning about state. Actor systems act as runtimes for small, independent objects called actors, which encapsulate both state and behaviour. A system has:

*   **Encapsulation:** Each actor owns its state and exposes it through well-defined messages or methods. External components or other actors cannot access the internal state directly, which keeps things pure and prevents corruption.
    
*   **Behaviour:** Typically, actors react to incoming messages, whereby they can change state, producing a response, or creating further messages. Actors can talk to other actors.
    
*   **Isolation:** Since actors process messages they receive sequentially, there are no concurrency issues within an actor. This simplifies reasoning about state mutation and transitions.
    
*   **Distributed by Design:** Actors can be distributed across nodes, with state partitioned naturally. This enables horizontal scalability without shared locks, complex transactions or coordinators.
    
*   **Fault Tolerance:** State can be persisted (e.g., to storage, database or event log) between messages. If an actor crashes, it can recover its state on another node and resume processing.
    

Systems such as [Microsoft Orleans](https://learn.microsoft.com/en-us/dotnet/orleans/overview), [Service Fabric](https://learn.microsoft.com/en-us/azure/service-fabric/service-fabric-reliable-actors-introduction) and [Dapr](https://docs.dapr.io/developing-applications/building-blocks/actors/actors-overview) offer the virtual actor pattern. The [virtual actor](https://learn.microsoft.com/en-us/dotnet/orleans/grains/) pattern introduces some abstractions to simplify development. You can think of a virtual actor as a distributed OOP object in memory (kind of like an old [EJB](https://en.wikipedia.org/wiki/Jakarta_Enterprise_Beans)). The object has methods on it such as `AddToOrder` and its lifecycle is managed by the system. The object can be invoked externally (from your API or an event).

There are 5 core features of a virtual actor:

1.  **Unique identity:** Each virtual actor is uniquely identified by an ID and its type. For example `OrderActor/28afcc20-913b-4415-964b-2dcf465902e3`
    
2.  **Activated on demand:** Virtual actors are instantiated (activated) automatically when needed. They are deactivated when idle for a certain period of time.
    
3.  **Stateful by design:** Virtual actors encapsulate their own state. The state is persisted transparently to a backend store (e.g., databases, blob storage) and is restored upon reactivation.
    
4.  **Concurrently safe:** Each actor processes messages sequentially, one at a time, ensuring thread safety. Prevents race conditions and deadlocks without additional effort. Encourages modular design, where each actor operates independently and focuses solely on its own state and behavior.
    
5.  **Fault Tolerance and Reliable:** If an actor's host node fails, the runtime can restart or reallocate the actor on another node, preserving its state and availability.
    

Now that we know the features of a virtual actor, how do we make them? Sometimes its difficult to get started, because we have to learn to think in actors. In my [next post](https://jeremycarterau.substack.com/p/thinking-in-actors-part-2) I will be discussing 5 modelling techniques to help you unlock your inner actor modelling brain.

*   **Database modelling is for later** — It’s easy to design systems from the database first. Instead ignore the data modelling, be naive and focus only on the real-world model.
    
*   **Anemic data models hinder maintainability** — Encapsulation of state and behavior is crucial. Anemic models lead to scattered business logic, making systems harder to maintain and extend.
    
*   **Rethink state with Domain-Driven Design** — A rich real-world model that contains state, behaviors, and transitions, aligns better with business needs and simplifies reasoning about state in distributed systems.
    
*   **The Actor Model solves stateful challenges** — Actors encapsulate state and behavior, process messages sequentially, and scale naturally, addressing concurrency, persistence, and fault tolerance in distributed systems.
    
*   **Virtual Actors simplify distributed systems —** The Virtual Actor pattern popularized by Microsoft Orleans provide a way for us to model and run our real-world model at scale.
    

**If we model the fundamental ideas of the product first, the system is easier to reason against, making it resilient to future changes.**

**Up next:** [Thinking in Actors - Part 2 - Welcome to a world of ordered thinking](https://jeremycarterau.substack.com/p/thinking-in-actors-part-2)
