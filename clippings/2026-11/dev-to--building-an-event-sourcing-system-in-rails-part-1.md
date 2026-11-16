---
url: "https://dev.to/isalevine/building-an-event-sourcing-system-in-rails-part-1-what-is-event-sourcing-46db"
captured_at: "2026-11-16T19:50:08+00:00"
title: "Building an Event Sourcing System in Rails, Part 1: What is Event Sourcing?"
domain: "dev-to"
---

## [](#what-is-event-sourcing)What is Event Sourcing?

Event Sourcing is a system design pattern that emphasizes recording changes to data via immutable events.

In other words: _every time your data changes_, you save an event to your database with the details.

**Those events never change or go away.** That way, you have a permanent, unchanging history of how your data reached its current state!

[Martin Fowler’s important 2005 essay](https://martinfowler.com/eaaDev/EventSourcing.html) describes Event Sourcing this way (emphasis mine):

> Event Sourcing ensures that **all changes to application state are stored as a sequence of events.** Not just can we query these events, we can also use the event log to reconstruct past states, and as a foundation to automatically adjust the state to cope with retroactive changes.  
> …  
> The fundamental idea of Event Sourcing is that of **ensuring every change to the state of an application is captured in an event object**, and that these event objects are themselves stored in the sequence they were applied for the same lifetime as the application state itself.

Cool! From this, we get a few key points about Event Sourcing systems that we’ll explore:

*   Changes to data are stored as Event objects
*   The Events have a fixed chronological order that can be “replayed”
*   The Events cannot be changed or deleted (for as long as they might be needed)

## [](#examples-of-event-sourcing)Examples of Event Sourcing

The example app we will be building in these articles will focus on events related to creating and destroying a User model. Consider this situation:

*   Client sends a request to create a User
*   Server receives the request
*   Server creates and saves a User
*   Server creates and saves an Event, which records the details of the request and the created User

Obviously, the implementation (and order of operations) will be more complex--but at its core, that's the basic Event Sourcing system we'll be creating!

[In a 2017 essay, Martin Fowler points out](https://martinfowler.com/articles/201701-event-driven.html) that version-control systems (like Git) are probably the most common example of Event Sourcing that programmers encounter (emphasis mine):

> The core idea of [event sourcing](https://martinfowler.com/eaaDev/EventSourcing.html) is that whenever we make a change to the state of a system, we record that state change as an event, and we can confidently rebuild the system state by reprocessing the events at any time in the future. The event store becomes the principal source of truth, and the system state is purely derived from it. For programmers, **the best example of this is a version-control system. The log of all the commits is the event store and the working copy of the source tree is the system state.**

For Rails-specific Event Sourcing, two resources/examples are often cited:

*   [Kickstarter’s minimal Event Sourcing system, described in this blog post](https://kickstarter.engineering/event-sourcing-made-simple-4a2625113224)
*   [Arkency’s RailsEventStore library, which has a number of versatile uses detailed in the GitHub repo](https://github.com/RailsEventStore/rails_event_store)

The focus of these articles will be on following Kickstarter’s example as I create a personal project with event sourcing architecture. **Thanks Kickstarter, you folks are amazing!**

## [](#some-implications-of-using-an-event-sourcing-system)Some implications of using an Event Sourcing system

Since working on an event sourcing system at my previous job, I’ve been building a personal project using one too. The key difference is that, at work, I was expanding on an already-existing system (and one that _wasn’t_ initially designed for event sourcing).

Now that I’m building one from scratch, I’ve encountered some important considerations:

*   Data is **truly immutable**—forget about using `ActiveRecord.destroy`! Instead, it’s important to design data for permanence, such as including a `deleted` field on User models.
*   Recording payload dumps of event data can include **potentially storing sensitive data in an unsafe format** if the event is saved outside of auth features like `has_secure_password`—you must be extra cautious about when sensitive data might be exposed, and be ready to manually implement encryption where needed!
*   Since events become “the principal source of truth” ([in Martin Fowler’s words](https://martinfowler.com/articles/201701-event-driven.html)), tons of logic ends up being wrapped in Event objects—naming and organizing code (and making sure it’s **future-proof**) is more essential than ever! [As Philippe Creux at Kickstarter described](https://kickstarter.engineering/event-sourcing-made-simple-4a2625113224) (emphasis _not_ mine):

> **Naming is hard.** And there are so many **immutable** events and attributes to name. The names you choose now will be the ones stored forever. So take a good dictionary and make sure that you nail down names that are explicit and future-proof.

I hope to explore and share these implications (and future ones that will surely arise!) in these articles, as we walk through how to implement an Event Sourcing system from scratch.

## [](#next-up)Next Up

The next article will go through the basics of creating a Rails app, centered around creating and destroying a User model, that uses basic Event Sourcing architecture. We will cover:

*   Setting up the Rails app with a `User` model and controller
*   Building the BaseEvent class architecture ([per Kickstarter’s example](https://github.com/pcreux/event-sourcing-rails-todo-app-demo))
*   Implementing `Events::User::Created` and `Events::User::Destroyed` event classes

## [](#references)References

Special thanks to [Philippe Creux](https://kickstarter.engineering/@pcreux) and [Kickstarter](https://kickstarter.engineering/event-sourcing-made-simple-4a2625113224) for sharing [their Event Sourcing example](https://github.com/pcreux/event-sourcing-rails-todo-app-demo).

Thanks to [Martin Fowler](https://martinfowler.com/) for his [important writings](https://martinfowler.com/articles/201701-event-driven.html) on [Event Sourcing](https://martinfowler.com/eaaDev/EventSourcing.html).

Thanks to [Arkency](https://arkency.com/) for their great work with [the RailsEventStore library](https://github.com/RailsEventStore/rails_event_store).

And finally, thanks to fellow Dev.to user [Alfredo Motta](https://dev.to/mottalrd) for [sharing about this years ago](https://dev.to/mottalrd/an-introduction-to-event-sourcing-for-rubyists-41e5) (and keeping it up for me to catch up on!).
