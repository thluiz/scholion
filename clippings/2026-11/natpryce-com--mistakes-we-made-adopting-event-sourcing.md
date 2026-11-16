---
url: "http://natpryce.com/articles/000819.html"
captured_at: "2026-11-16T18:50:35+00:00"
title: "Mistakes we made adopting event sourcing (and how we recovered)"
domain: "natpryce-com"
---

Over the last year or so we have been building a new system that has an [event-sourced](https://martinfowler.com/eaaDev/EventSourcing.html) architecture. Event-sourcing is a good fit for our needs because the organisation wants to preserve an accurate history of information managed by the system and analyse it for (among other things) fraud detection. When we started, however, none of us had built a system with an event-sourced architecture before. Despite reading plenty of advice on what to do and what to avoid, and experience reports from other projects, we made some significant mistakes in our design. This article describes where we went wrong, in the hope that others can learn from our failures.

But it’s not all bad news. We were able to recover from our mistakes with an ease that surprised us. I’ll also describe the factors that allowed us to easily change our architecture, in the hope that others can learn from our successes too.

## Mistakes

### Not separating persisting the event history and persisting a view of the current state

The app maintained a relational model of the current state of its entities alongside the event history. That in itself wouldn’t be a bad thing, if it had been implemented as a “projection” of the events. However, we implemented the current state by making the command handlers both record events and update the relational model. This meant that (a) there was nothing to ensure that entity state could be rebuilt from the recorded events, and (b) managing the migrations of the relational model was a significant overhead while the app was in rapid flux.

Surely this was missing the entire point of adopting event-sourcing?

Well… yes. People came to the project with different backgrounds and technical preferences. There was a creative tension that led to an initial design the team was comfortable with, rather than one that was “by the book” for any specific book. Some of us did notice the architecture diverging from what the event-sourcing literature described, but didn’t react immediately. We wanted the team (ourselves included) to build an intuition for the advantages, disadvantages and trade-offs inherent in an event-sourced architecture, rather than apply patterns cookie-cutter style. And we didn’t know how this hybrid architecture would work out – it could have been very successful for all we knew – so we didn’t want to dismiss the idea based only on a theoretical understanding gleaned from technical articles & conference sessions. Therefore we continued down this road until the difficulties outlined above were clearly outweighing the benefits. Then we had a technical retrospective in which we examined the differences between canonical event-sourcing and our architecture. The outcome was that we all understood why canonical event-sourcing would work better than our application’s current design, and agreed to change its architecture to match.

### Confusion between event-driven and event-sourced architecture

In an event-driven architecture, components perform activity in response to receiving events and emit events to trigger activities in other components. In an event-sourced architecture, components record a history of events that occurred to the entities they manage, and calculate the state of an entity from the sequence of events that relate to it.

We got confused between the two, and had events recorded in the history by one component triggering activity in others.

We realised we’d made a mistake when we had to make entities distinguish between reading an event in order to react to it, and reading an event in order to know what happened in the past.

This also led to us…

### Using the event store as a message bus

We added notifications to our event store so services could subscribe to updates and keep their projection up to date. Bad idea! Our event store started being used as an event bus for transient communication between components, and our history included technical events that had no clear relationship to the business process. We noticed that we had to filter technical events out of the history displayed to users. For example, we had events in the history about technical things like “attempt to send email failed with an IOException”, which users didn’t care about. They wanted to see the history of the business process, not technical jibber-jabber.

The literature describes event-sourced and event-driven architectures as orthogonal, and that tripped us up. We came to realise that clearly distinguishing between commands that trigger activity and events that represent what happened in the past is even more important than Command/Query Responsibility Segregation, especially at the modest scale and strict consistency requirements of our system. The word “event” is such an overused term we had many discussions about how to name different kinds of event to distinguish between those that are part of the event-sourcing history, those that are emitted by our active application monitoring, those that are notifications that should trigger activity, and so on. In our new applications we use the term _Business Process Event_ for events recorded in our event-sourcing history.

### Seduced by eventual consistency

Initially we gave the event store an HTTP interface and application components used it to read and store events. However, that meant that clients couldn’t process events in ACID transactions and we found ourselves building mechanisms in the application to maintain consistency.

## Noticing our mistakes

Luckily we caught these mistakes early during a regular architecture “[wizengamot](https://www.hp-lexicon.org/thing/wizengamot/)” before our design decisions had affected the event history of our live system.

We decided to replace our use of HTTP between command processors and the event store with direct database connections and serialisable transactions. We kept the HTTP service for traversing the event history, but only for peripheral services that maintain read-optimised views that can be eventually consistent (daily reports, business metrics, that kind of thing).

We decided to stop using notifications from the event store to trigger activity and went back to REST (particularly [HATEOAS](https://en.m.wikipedia.org/wiki/HATEOAS)) for passing data and control between components.

We decided to not update the record of the current state of the entities in command handlers. Instead the application computes the current state from the event history when the entity is loaded from the database. The application still maintains a “projection” of the current entity states, but treats the projection as a read-through cache, used to optimise loading entities, so that it doesn’t have to load all of an entity’s events on every transaction, and to select subsets of the currently active entities, so that it doesn’t have to load all events of all entities. Entries are expired from the cache by events: each projection is a set of tables and function is passed each event and creates, updates and deletes rows in its tables in response.

Logic to execute commands now looks like:

1.  Load the recent state of the entity into an in-memory model
2.  In a write transaction
    1.  load events that occurred to the entity since the recent projection into the in-memory model
    2.  perform business logic
    3.  record events resulting from executing the command
3.  Save the in memory state as the most recent projection if it was created from more recent events than that the projection that is currently persisted (the persisted state may have been updated by a concurrent command)

Read transactions don’t record events and can therefore run in parallel with each other and write transactions.

We decided to replace the relational model, which required so much effort to migrate as the app evolved, with JSON blobs serialised from the domain model that can be automatically discarded and rebuilt when the persisted state becomes incompatible with the latest version of the application. Thanks to Postgres’ [JSONB](https://www.postgresql.org/docs/9.5/datatype-json.html) columns, we can still index properties of entity state and select entities in bulk without adding columns of denormalised data for filtering.

The application also maintains projections for other uses, which have less stringent consistency requirements. For example, we update projections for reporting in the background on a regular schedule.

## Re-engineering the system architecture

We were concerned that such significant changes to the systems architecture would deliver a blow to our delivery schedule. But it turned out to be very straightforward. The reasons why are orthogonal to event-sourcing.

As well as using event-sourcing, the application has a Ports-and-Adapters (aka “hexagonal”) architecture. Loading the current state of an entity was hidden from the application logic behind a Port interface that was implemented by an Adapter class. My colleague, [Ivan Sanchez](https://www.linkedin.com/in/s4nchez/), was able to switch the app over to calculating an entity’s current state from its event history and treating persistent entity state as a read through cache (as described above) in about _one hour_. The team then replaced the relational model, which required so much effort to migrate as the app evolved, with JSON blobs serialised from the domain model that could be automatically discarded and rebuilt when the persisted state became incompatible with the latest version of the application. The change was live by the end of the day.

We also have extensive functional tests that run in our continuous deployment pipelines. These were [written to take advantage of the Ports-and-Adapters architecture](https://www.youtube.com/watch?v=Fk4rCn4YLLU), a style we call “Domain-Driven Tests”. They capture the functional behaviour of the application in terms of users needs and concepts from the problem domain, without referring to details of the technical infrastructure of the application. They can be run against the domain model, in memory, against the HTTP interfaces of the application services, or through the browser, against an instance running on a developer workstation or one deployed into our cloud environment.

The functional tests serve two purposes that paid off handsomely when we had to make significant changes to the application’s architecture.

Firstly, they force us to follow the Ports-and-Adapters architecture. Our tests cannot refer to details of the application’s technical underpinnings (HTTP, database, user interface controls, HTML, JSON, etc). We get early warning if we violate the architectural constraints by, say, writing business logic in the HTTP adapter layer, because it becomes impossible to write a test that can run against the domain model alone.

As a result, changes to the technical architecture of the application were strictly segregated from the definition and implementation of its functional behaviour, neither of which needed to be changed when we changed the architecture. This allowed them to fulfil their second purpose: to rapidly verify that the application still performs the same user visible behaviour as we made large changes to its architecture.

## Conclusions

It’s inevitable that you’re going to make mistakes when implementing a system, especially when adopting a new architectural style with which the team are not familiar. A system’s architecture has to address how you recover from those mistakes.

In our case, using the Ports and Adapters style, with which the team had a lot of experience, and considering test and deployment infrastructure as an essential part of the system architecture allowed us to adopt Event Sourcing, with which we were entirely unfamiliar, and recover from our misunderstandings as the system evolved.

## Acknowledgements

Thanks to [Duncan McGregor](http://oneeyedmen.com/), [Dan North](https://dannorth.net/), [Owen Rogers](https://medium.com/exortech) & [Daniel Wellman](https://blog.danielwellman.com/) for their detailed and valuable feedback.
