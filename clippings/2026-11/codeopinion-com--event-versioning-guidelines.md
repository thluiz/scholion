---
url: "https://codeopinion.com/event-versioning-guidelines"
captured_at: "2026-11-16T02:27:17+00:00"
title: "Event Versioning Guidelines"
domain: "codeopinion-com"
---

_**Sponsor:** Do you build complex software systems? See how NServiceBus makes it easier to design, build, and manage software systems that use message queues to achieve loose coupling. [Get started for free](https://go.particular.net/codeopinion/4-2026/used-queue-before)._

![Event Versioning Guidelines](https://codeopinion.com/wp-content/uploads/2020/01/EventVersioningGuidelines-Twitter-1024x536.png)

This post serves as a guideline for how to handle versioning for messages, specifically in most cases, events. This Event Versioning Guidelines post is in a series related to messaging. You can find the overview in my [Message Properties](https://codeopinion.com/message-properties/) post.

## Backward Compatible

Generally, adding additional properties to an event will not cause a versioning conflict with the event consumer.

Meaning if we have a contract that defines the shape of our event, as long as we don’t break that contract, the existing event consumers will be able to process our new event and will ignore the additional properties.

Also, if you are persisting events to an event/data store, you must be able to upcast an old stored event to our new version.

This isn’t that crazy of a concept. If you think about a relational database, when you need to add a new column, you generally will create the new column as having a default NULL value. The difference is you **won’t** backfill the existing events by replacing NULL with an actual value. Rather you handle the NULL value in your application code.

If you must change the contract, then you must create a new version of that event and cause a breaking change.

## Version Number

One option for defining a new event is to include a version number within the event itself. Event consumers can then use this version number to determine how they should handle or process the event.

Regardless of backward compatibility, you can use a version number alongside your event name to indicate to consumers which contract to an event they are processing.

As an example using [Semantic Versioning](https://semver.org/) to define our events:

## New Event

Most of the time if an event is not backward compatible, you likely have an entirely new event. And because of this, the name of the new event is likely different from the old event.

What’s tricky is to determine if this new event **replaces** the old event. Is the new event a discovery of an actual business event or is it simply a new understanding that replaces an existing concept?

## Double Publish

If an event isn’t backward compatible, you might want to publish both v1 and v2 of the event that occurred.

Meaning the publisher writes both versions (v1 and v2) to the message queue or event stream.

One issue with this approach is consumers must understand this. They must understand they should only process one or the other. They either must process v1 and ignore v2, or process v2 and ignore v1.

This isn’t that big of a deal when the consumers aren’t replaying (re-processing) existing events from an event store. If you are using an event store and replaying events for a projection, you likely do not want to double publish. The reason being is processing both _could_ have a negative impact.

If you’re not replaying events, then you’re consumers have to implement the new version you’re publishing. At the same time, they can remove the handling of the old event.

It’s not that odd to double publish by creating a new event and deprecate an old event and remove it once all consumers have handled the new event.

If you have any additional event versioning guidelines that I have omitted, please let me know on Twitter or in the comments.

## Related Links

*   [Message Properties](https://codeopinion.com/message-properties/)
*   [Message Naming Guidelines](https://codeopinion.com/message-naming-guidelines/)
