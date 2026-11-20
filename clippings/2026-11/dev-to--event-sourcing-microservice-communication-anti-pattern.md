---
url: "https://dev.to/olibutzki/why-event-sourcing-is-a-microservice-anti-pattern-3mcj"
captured_at: "2026-11-19T22:49:48+00:00"
title: "Why Event Sourcing is a microservice communication anti-pattern"
domain: "dev-to"
---

Why Event Sourcing is a microservice communication anti-pattern

By Oliver Libutzki (DEV Community). Posted on Jun 28, 2019.

Event-driven architectures in general and Event Sourcing in particular gain traction in the last couple of years. This trend is caused by the fact that we strive after building modular systems which are resilient und scalable. Microservices is the term which is used in this context quite often. In my opinion microservices are just one way to implement a Bounded Context. The heart of a modular system are the boundaries of a module and the most promising idea how to identify these boundaries is the Strategic Design introduced by Eric Evans' Domain Driven Design. It helps you to identify/discover your modules with their boundaries (Bounded Context) and describes the way how these Bounded Contexts are related to each other (Context Map).

Note: I will presuppose some foreknowledge about certain terms as I do not want to explain them for the thousandth time. I decided to link to the explanations of microservices.io, Wikipedia or Martin Fowler's Bliki, so it's up to you do dive deeper into a certain topic, if you feel uncomfortable with your knowledge.

Domain Events as the heart of the Ubiquitous Language

Although not explicitly mentioned in Eric's book Domain Events facilitate the idea of the DDD concepts quite well. Techniques like Alberto Brandolini's Event Storming shift the focus on events from a technical to a organizational / business level. We do not talk about some UI layer events like a ButtonClickedEvent, but about Domain Events which are part of the business domain and which are spoken and understood by the business experts. These Domain Events are first-class concepts and provide a great way to form the Ubiquitous Language which all participants (domain experts, developers,...) agree on.

Domain Events used for cross-boundary communication

Domain Events can be used for facilitating the communication between Bounded Contexts. Let's assume we have an online shop with three Bounded Contexts: Order, Delivery, Invoice.

A Domain Event of the Order context is Order accepted. The Invoice as well as the Delivery context is interested in the occurence of this event as it causes some internal processes to be started.

The decoupling myth

The usage of Domain Events helps you to develop decoupled modules. Modules might be offline temporarily. Domain Events do not care about unavailable modules, they describe something that happened in the past. It's up to the other modules how fast they process the events. What you get is a resilient system by design.

Beside temporal decoupling Domain Events promise another advantage, at least at the first glance:
The Order context does not have to know that the Invoice and Delivery context listen to its events. Actually it even doesn't need to know that those contexts exist.

That's cool, but the challenging part is the event payload. Which data do put into the event?

The simple answer: Event Sourcing!

Events are useful, so why not giving them as much power (and responsibility) as possible. That's the basic idea of Event Sourcing. You do not store the state of an aggregate by updating its data (CRUD) but by applying an event stream.

Beside that fact that you can replay events to rebuild the application state, one great feature of Event Sourcing is that you get a complete and reliable audit log for free. So when such an audit log is required, Event Sourcing should definitely taken in account while evaluating the persistence strategy.

Is Event Sourcing just a persistence strategy?

You might wonder why I came from Domain Events straight to persistence strategy as these concepts obviously work at different layers / abstraction levels.

... and that's my point: Event Sourcing is a local decision made by a single Bounded Context! The events should not be exposed to the outside world! Other Bounded Contexts do not know about each other's persistence strategy and therefore they don't know and don't care, if another Bounded Context uses Event Sourcing.

If you use Event Sourcing at global scale, you expose your persistence layer.

Your persistence becomes your public API. Every time a Bounded Context adjusts its persistent data, we have to deal with a public API change.

I'm pretty sure everyone agrees that it's a bad idea that different Bounded Contexts share data in a (relational) database because of development und runtime coupling. But where is the difference?

There is none. It doesn't matter if we share events or database tables. In both cases we share our persistence details.

There is a way out

I still argue that Domain Events are a perfect fit for the communication between Bounded Contexts, but these events shall not correspond to the events used for Event Sourcing.

My proposed solution is the logical consequence: Regardless whether you use a CRUD or an Event Sourcing approach for persistence you publish Domain Events to a global event store. These Domain Events are your Bounded Context's public API. If you prefer the usage of Event Sourcing in your Bounded Context you store these events in a local event store which only accessible from this Bounded Context

The freedom of choice

Having dedicated Domain Events in your public API opens up the possibility to decide how to model these events. You are not restricted to the layout which is predefined by the Event Sourcing events.

You have two options for each occurrence of a "real world event":

Open Host Service with Published Language

Publish exactly one domain event which contains all the data which might be needed by other Bounded Contexts. In DDD terminology one would call this an Open Host Service with a Published Language.

The occurrence of the real world event Order accepted leads to one published Domain Event OrderAccepted. The payload of this event contains all the data which Order expects other Bounded Context's to be interested in... so hopefully the Invoice and the Delivery contexts find all the information they need.

Customer/Supplier

Publish multiple dedicated Domain Events, one for each event consumer. You have to discuss each particular Domain Event with exactly one other party (the consumer) and don't have to define a shared model. DDD calls this relationship Customer/Supplier.

The occurrence of the real world event Order accepted leads to one published Domain Event per consuming Bounded Context: InvoiceOrderAccepted and DeliveryOrderAccepted. Each Domain Event contains exactly the data which is requested by the consuming context.

I do not want to discuss the pros and cons of the two options. I just want to highlight that you are free to choose the number of Domain Events and their payload.

This is a great advantage you should not underestimate, because you can decide how to evolve your Bounded Context's API and are not committed to the events you need for Event Sourcing.

Conclusion

Exposing persistence details to the outside world is a well-known anti-pattern. When talking about persistence we think about database tables in the first place, but I explained why the events used for Event Sourcing are just another way how to persist data. Therefore exposing these events is a anti-pattern as well.

Event Sourcing is powerful, if it's used in an appropriate (local) way. At first glance it seems to be the silver bullet for event-driven architectures, but if you look in deeper, you realize that it might lead you to a tightly coupled (distributed) system... and that's not your aim, for sure.

References

Beside my personal experience I got a lot of inspiration from different abstracts and conference talks. I would like to highlight the talk Event-based Architecture and Implementations with Kafka and Atom by Eberhard Wolff. Especially the chapters Event Sourcing and Whats's in the event? are highly relevant in the context of this blog post. The online shop example I chose is inspired by this talk.

There are some other resources you can consult if you would like to get some additional information:

Domain Events vs. Event Sourcing by Christian Stettler, Blog post
What they don't tell you about event sourcing by Hugo Rocha, Blog post
A Decade of DDD, CQRS, Event Sourcing (CQRS/ES is NOT a top level architecture) by Greg Young, Conference talk
