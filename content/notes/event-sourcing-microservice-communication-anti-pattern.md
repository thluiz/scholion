---
title: "Why Event Sourcing is a microservice communication anti-pattern"
date: '2019-07-09T09:00:17+00:00'
category: webclip
summary: 'Argues that using event-sourcing events as cross-boundary messages exposes persistence details, tightly couples bounded contexts, and should be avoided in favor of separate public domain events.'
tags: ["event-sourcing", "microservices", "domain-driven-design", "architecture"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Why Event Sourcing is a microservice communication anti-pattern"
    url: "https://dev.to/olibutzki/why-event-sourcing-is-a-microservice-anti-pattern-3mcj"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--event-sourcing-microservice-communication-anti-pattern.md"
    kind: repo
---

The text argues that Event Sourcing should be a local persistence decision inside a bounded context, not the basis for communication between microservices. Using event-sourcing events as global messages exposes persistence details as a public API, which couples bounded contexts in a way similar to sharing database tables. Instead, domain events should be modeled and published explicitly as a context’s external API, independent of whether persistence is CRUD-based or event-sourced.

Domain Events are presented as central to DDD’s idea of a Ubiquitous Language and to cross-boundary communication. Techniques like Event Storming emphasize business-level events understood by domain experts. In an online shop example with Order, Delivery, and Invoice bounded contexts, an "Order accepted" domain event is of interest to multiple contexts and triggers internal processes, illustrating how domain events connect contexts without direct knowledge of each other.

## Reading notes

- Event-driven architectures and Event Sourcing have become popular as ways to build modular, resilient, and scalable systems, often in connection with microservices.
- Microservices are described as one possible implementation of a DDD Bounded Context, with Strategic Design and context mapping used to define module boundaries and relationships.
- Domain Events, though not emphasized in Evans’ original book, are aligned with DDD and help form the Ubiquitous Language shared by domain experts and developers.
- Business-oriented Domain Events differ from technical UI events; they represent concepts from the problem domain rather than interface actions.
- Techniques like Alberto Brandolini’s Event Storming focus on events at an organizational or business level to model domains.
- Domain Events are suitable for communication between bounded contexts, as shown in the example of an online shop with Order, Delivery, and Invoice contexts.
- In the example, an "Order accepted" event from the Order context is relevant for both Delivery and Invoice, since it initiates processes in these contexts.
- Using Domain Events supports temporal decoupling: consumers can be temporarily offline and process events later, which increases resilience.
- The Order context does not need to know that Delivery and Invoice consume its events, or even that these contexts exist, reducing explicit dependencies.
- A practical challenge with events is deciding which data to include in the event payload when publishing to other contexts.
- Event Sourcing is introduced as an approach where aggregate state is stored as a stream of events instead of through CRUD-style updates.
- With Event Sourcing, the system can rebuild application state by replaying events, and gains a complete and reliable audit log as a byproduct.
- The author positions Event Sourcing primarily as a persistence strategy, despite initially discussing Domain Events and inter-context communication.
- A key claim is that Event Sourcing should be a local decision inside a single bounded context, and its events should not be exposed externally.
- Other bounded contexts neither know nor care whether a peer context uses Event Sourcing; exposing these events reveals the persistence strategy.
- If event-sourcing events are shared globally, the persistence layer effectively becomes the public API of the bounded context.
- Any change in persistent data then becomes a change to the public API, because external consumers depend on the event structure.
- The author compares sharing event-sourcing events across contexts to sharing relational database tables between services.
- In both cases, other bounded contexts depend on internal persistence details, leading to development and runtime coupling.
- The text argues that there is no essential difference between sharing database tables and sharing event-sourcing events, in terms of exposing persistence.
- The suggested alternative is to keep Event Sourcing events local and publish separate Domain Events to a global event store as the public API.
- This approach applies whether persistence is implemented with CRUD or with Event Sourcing; the public Domain Events are independent of storage details.
- When Event Sourcing is used, its events are stored in a local event store that is only accessible from within the owning bounded context.
- Having dedicated public Domain Events decouples API design from the layout of internal event-sourcing events.
- This separation lets the bounded context choose how to model external events without constraints from its internal persistence representation.
- For each real-world occurrence, there are two outlined options for publishing domain events to other contexts.
- The first option is an Open Host Service with a Published Language, where one domain event is published containing all data potentially needed by consumers.
- In this option, the real-world "Order accepted" leads to a single public "OrderAccepted" event whose payload aims to fit the needs of Invoice, Delivery, and other consumers.
- The second option is a Customer/Supplier relationship, with one dedicated domain event per consuming bounded context.
- In the Customer/Supplier case, "Order accepted" produces events like "InvoiceOrderAccepted" and "DeliveryOrderAccepted", each tailored to a single consumer.
- Each dedicated event in the Customer/Supplier model carries exactly the data requested by its specific consumer context.
- The author does not compare the advantages and disadvantages of Open Host Service vs. Customer/Supplier in detail, but stresses that both are valid and the choice is open.
- A highlighted benefit of this separation is the freedom to decide the number of public events and their payloads independently of Event Sourcing.
- This freedom allows the bounded context to evolve its public API without being constrained by internally used event-sourcing events.
- The conclusion states that exposing persistence details is a known anti-pattern, commonly discussed in relation to sharing database tables.
- Since Event Sourcing events are another way to persist data, exposing them to other bounded contexts is framed as an anti-pattern as well.
- Event Sourcing is described as powerful when applied locally, but using it as a global integration mechanism can create a tightly coupled distributed system.
- The author underlines that such tight coupling between services is the opposite of the modular, resilient architecture teams usually seek.
- The text credits Eberhard Wolff’s talk "Event-based Architecture and Implementations with Kafka and Atom", particularly sections on Event Sourcing and event contents, as a major influence.
- Additional suggested resources include Christian Stettler’s blog post on Domain Events vs. Event Sourcing, Hugo Rocha’s post on what is rarely mentioned about event sourcing, and Greg Young’s talk on DDD, CQRS, and Event Sourcing.
