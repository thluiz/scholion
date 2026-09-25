---
url: "https://www.reactivesystems.eu/2024/10/31/the-dual-nature-of-events-in-eda.html?ref=dailydev"
captured_at: "2026-09-25T22:46:04+01:00"
title: "The Dual Nature of Events in Event-Driven Architecture"
domain: "reactivesystems-eu"
---

_Given that events play such a central role in event-driven architecture, there’s an astonishing lack of agreement on what should be contained in an event. This may be rooted in the fact that, depending on your perspective, events fulfill different purposes._

In a system that follows event-driven architecture in its contemporary style, microservices collaborate by emitting and subscribing to events.  
_(Please note this article only talks about events that are “published” from one domain for others to subscribe to. Not about internal events that are used for example if your approach to persistence is event sourcing.)_

In these event-driven systems, events that travel between services have a dual role: They **_trigger actions_** and **_carry data_**.

In principle events emitted from a service can be anywhere on the spectrum shown in the picture below.

![Events are usually both trigger and data carrier - varying in the amount of data included.](https://www.reactivesystems.eu/images/post0080/spectrum.svg)

_Events are usually both trigger and carrier of data - varying in the amount of data included._

The left end would be “pure trigger”, where all the information is contained in the event type alone. On the right end of the spectrum, all properties of the changed entity/aggregate would be included in the event.

_By the way, not only is there no consensus on how much data should usually be included in an event - it’s not even clear what to call the data-heavy events on the right end of the spectrum. Having been taught this term by a colleague of mine, I call them **wide events**._  
_But elsewhere on the internet, you’ll also find them referred to as [fat events](https://verraes.net/2019/05/patterns-for-decoupling-distsys-fat-event/), [god events](https://youtu.be/wM-dTroS0FA?si=mIbqmEyxBvbKybCO&t=1350), [RESTful events](https://blog.frankdejonge.nl/the-different-types-of-events-in-event-driven-systems/#the-restful-or-fat-event), or [state events](https://dzone.com/articles/how-to-design-event-streams-part-1)._

### The “software engineer/architect with DDD background” view

As a developer working on event-driven microservices, the primary concern is implementing a business process as an event flow.

You think of events as triggers, and you want to have different types of events for different triggers. This allows you to look at a sequence of events and understand what’s going on.

Having different types of events also matches design processes such as event storming. The stickies contain what happened (the type of event), you don’t write the data on them.

Using different, properly named types for events means applying the ubiquitous language. Looking at the technical events, even a business person understands what’s going on.

The processes you implement are stories, and events are the smallest unit of a story.

If you had only one type of event, e.g. `BookingUpdated`, you’d have to figure out what’s going on by looking at what data has changed. Guesswork.

Let’s say your process is buying a cinema ticket. If you look at the sequence of events, what do you want to see?

1.  `SeatSelected → PaymentReceived → TicketIssued` or
2.  `BookingUpdated → BookingUpdated → BookingUpdated`

After all, it’s about collaboration between services - event-driven is not data replication.

Taking this perspective, for any entity you emit different types of events, with the event type clearly indicating what has happened. In terms of data contained in the event, it would be only the properties related to the event (the ones that have changed in the context of the event).

If you use [Kafka](https://kafka.apache.org/), you publish all the different events relating to the same class of entity to one topic. _(To read the events relating to the same entity in order, they must be on the same partition. Being on the same topic is a prerequisite for being on the same partition.)_ If you use a schema registry, you use the [RecordNameStrategy](https://developer.confluent.io/courses/schema-registry/schema-subjects/#recordnamestrategy) or the [TopicRecordNameStrategy](https://developer.confluent.io/courses/schema-registry/schema-subjects/#topicrecordnamestrategy).

This is totally legitimate and will work. But there’s a different perspective you should also consider.

### The “data engineer” view

As a data engineer, it’s just data. Instead of in a table, it’s in a stream, but in the end, it represents the state of things.

Having data in too small units just creates more work for the data team to eventually create usable tables to represent the state of the represented entities.

That works best if you have just one type of event in the stream, so all events on a topic share the same schema. This gives you the “table-stream duality”. Also, it makes it easy to ingest the stream into a database, or into some headless data format (such as [Iceberg](https://iceberg.apache.org/)).

From a data point of view, if you could query the stream like a DB, you’d be happy with a stream that just retains the latest state forever. In fact, instead of having both a streaming infrastructure and a database, you’d actually prefer to just have one.  
_(I think [streaming databases](https://www.oreilly.com/library/view/streaming-databases/9781098154820/) address this, but haven’t really looked into this yet. And there are new streaming products such as [Tektite](https://tektitedb.com/), which lets you, I quote: “Query the data in any stream or table as if it were a database table”.)_

If you use Kafka, you publish only one type of event per topic. If you use a schema registry, you use the [TopicNameStrategy](https://developer.confluent.io/courses/schema-registry/schema-subjects/#topicnamestrategy).

### So what to do?

If you focus on only one of these purposes in the design of your events and neglect the other, you might make your life harder down the line.

If you only follow the data perspective, you’ll lose vital information about the reason for the event. Don’t reduce event collaboration to data replication.

Having said that, you’ll probably come across cases where it really _is_ just data replication, and where you want wide events. This includes

*   Using events to populate your data warehouse or data lake.
*   Bootstrapping new services that are added to your system later, that need the full event history to start off with the up-to-date data.
*   Cases where other services hold a local projection of the data that needs to be updated (but the update itself doesn’t trigger an action).

If you focus only on the triggering nature of events, and these use cases come up later in your product’s lifecycle, you might have to introduce wide events as additional events. That adds effort you can avoid if you have the data aspect in mind early on.

### So, based on all this, what should be in an event?

My take is:

*   It’s an absolute must that the event contains its reason, i.e. the business event that it represents.
*   It must contain at least the data that was changed in this event.
*   A fair amount of additional data doesn’t hurt. If your entity can be serialized into an event that’s still small enough, include a complete snapshot of its state and make your (and your data’s consumers) life easier.

“Include a _complete_ snapshot” requires further qualification. Still be mindful of the data you include of your events. Not only because, from a technical perspective, events should be small, so they can be replicated quickly e.g. between the multiple nodes of your distributed message broker. But even more importantly: Your event stream is an API. You need to design the events just as carefully as you would design JSON objects for a RESTful HTTP API. What goes in there is hard to remove, and you want to be able to change your domain model internally to some extent without affecting the event payload.

So my standard approach is to **use carefully designed, wide events and include the reason in the event** (or alternatively as a header). While I want to see the reasons, and get the story from looking at the sequence of events, it doesn’t necessarily have to be encoded as the event type.

A sequence would then be something like

`BookingUpdated(Reason: SeatSelected) → BookingUpdated(Reason: PaymentReceived) → BookingUpdated(Reason: TicketIssued)`

To me this embraces the dual nature, it’s a “best of both worlds” practice for me. What’s your approach? Let me know what you think in the comments.

* * *

_P.S. I help companies adopt event-driven architecture, from designing event schemas that balance the needs of software engineers and data teams to defining strategies for event granularity, versioning, and schema evolution. Whether you’re designing a new event-driven system or improving an existing one, I offer [architecture consulting and training](https://www.huehnken.de/) on exactly these topics. Feel free to [get in touch](mailto:info@huehnken.de)._
