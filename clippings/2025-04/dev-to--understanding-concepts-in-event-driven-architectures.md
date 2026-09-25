---
url: "https://dev.to/jhonifaber/introduction-to-event-driven-architecture-eda-3ioj?context=digest"
captured_at: "2025-04-03T09:24:29-03:00"
title: "Understanding concepts in Event Driven Architectures (EDA) - DEV Community"
domain: "dev-to"
---

---
Event Driven Architecture has become a very popular choice in recent times for developing highly scalable distributed systems. Is a way of designing software where different parts of the system communicate by sending and reacting to events.

An **event** is something that happens, like:

-   A user signs up
-   A user uploads a photo
-   A payment is completed

Instead of making direct requests to each other, different parts of the system listen for these events and react when needed(asynchronously).

For example:

1.  _The Payment Service_ is completed and emits an event: "payment done".
2.  _The Inventory Service_ listens for that event and updates the stock for the new product that has been bought.
3.  _The Email Service_ listens and sends a confirmation email.

Let's see a very simple diagram of the components in Event Driven Architecture

## [](https://dev.to/jhonifaber/introduction-to-event-driven-architecture-eda-3ioj?context=digest#key-components)**Key Components**

[![Image description](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F7nvc22aj7zc04n5p8ql9.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F7nvc22aj7zc04n5p8ql9.png)

**1\. Event Producer/Publisher**  
The system or service that creates and emits events when something happens.  
Example: A User Service sends an event "User Registered" when a new user signs up.

**2\. Message Broker**  
A message broker is a middleware that acts as an intermediary between event producers and event consumers. Its primary role is to receive, store, and route events efficiently, ensuring that the events are delivered to the correct consumer services.

In this context, there is a crucial concept inside message brokers called **Channels**. These channels act as communication routes that orchestrate the flow of events from producers to the right consumers.

-   In **Kafka**, these channels are called **Topics**. It supports **multi subscriber models**, allowing multiple consumers to listen to the same publisher.
-   In **RabbitMQ**, these channels are called **Queues**. RabbitMQ is typically **point-to-point** for queues, meaning that only one consumer can process a message from a queue.

Example technologies: Kafka, RabbitMQ, AWS SNS/SQS, Google Pub/Sub.

**3\. Event Consumer/Subscriber**  
The service that listens to events and reacts to them.  
Example: A Notification Service listens for "User Registered" and sends a welcome email.

**4\. Event**  
The actual message that describes what happened. It usually contains structured data (JSON, XML).  
Example event message:  

```
<span>{</span><span>
  </span><span>"data"</span><span>:</span><span> </span><span>{</span><span>
    </span><span>"id"</span><span>:</span><span> </span><span>"event-123456"</span><span>,</span><span>
    </span><span>"type"</span><span>:</span><span> </span><span>"user.event.registered"</span><span>,</span><span>
    </span><span>"timestamp"</span><span>:</span><span> </span><span>"2025-04-01T12:00"</span><span>,</span><span> 
    </span><span>"attributes"</span><span>:</span><span> </span><span>{</span><span>
      </span><span>"id"</span><span>:</span><span> </span><span>"usr-98765"</span><span>,</span><span>
      </span><span>"email"</span><span>:</span><span> </span><span>"user@example.com"</span><span>,</span><span>
      </span><span>"surname"</span><span>:</span><span> </span><span>"example"</span><span>,</span><span>
    </span><span>}</span><span>
  </span><span>}</span><span>
</span><span>}</span><span>
</span>
```

## [](https://dev.to/jhonifaber/introduction-to-event-driven-architecture-eda-3ioj?context=digest#broker-exchanges)**Broker Exchanges**

In message brokers, an exchange is a routing mechanism that determines how messages are delivered to queues. Different types of exchanges provide different message distribution patterns.

**Direct Exchange (1:1 Routing)**  
Routes messages to queues based on an exact match between a routing key and a queue **binding key** (RabbitMQ).  
How it works?

-   The producer sends a message with a routing key.
-   The exchange forwards the message only to queues with a matching binding key.

Example:  
A message with routing key = `"order.created"` goes only to the queue bound with `"order.created"`.

[![Image description](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F1pra4kdkq5gi6t7nxa49.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F1pra4kdkq5gi6t7nxa49.png)

**Fanout Exchange (Broadcast)**  
Sends messages to all bound queues, **ignoring the routing key**  
(RabbitMQ-Fanout Exchange | Kafka-multiple consumers per topic).

How it works?

-   The producer sends a message.
-   The exchange copies the message to all queues bound to it.

Example:  
A notification event is broadcasted to multiple services (email, SMS, push notifications).

[![Image description](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fiuh8eqc9p7pmnv6h17qx.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fiuh8eqc9p7pmnv6h17qx.png)

**Topic Exchange (Pattern Matching)**  
Routes messages based on wildcard patterns in routing keys. Supports `*`, matches one word and `#`, matches multiple words. (RabbitMQ-Topic Exchange | Kafka-topics with partition keys).  
How it works?

-   Uses `.` to separate words in routing keys (`"order.payment.failed"`).

Example:  
A queue bound to `"order.*"` receives `"order.created"` and `"order.cancelled"`, but not `"user.created"`.

[![Image description](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fvm14p35ghlut5yv4ssza.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fvm14p35ghlut5yv4ssza.png)

## [](https://dev.to/jhonifaber/introduction-to-event-driven-architecture-eda-3ioj?context=digest#advantages-of-eda-reactive-manifesto)**Advantages of EDA** - [Reactive Manifesto](https://www.reactivemanifesto.org/)

-   **Scalability**: decoupled services can scale independently.
-   **Flexibility**: easy to add new event consumers without modifying existing services.
-   **Real-time Processing**: enables real-time data streaming and quick responses.
-   **Resilience**: failures in one service don’t impact the entire system as long as events and subscriptions are managed properly
-   **Loose Coupling**: components interact through events, reducing dependencies.

## [](https://dev.to/jhonifaber/introduction-to-event-driven-architecture-eda-3ioj?context=digest#disadvantages-of-eda)**Disadvantages of EDA**:

-   **Eventual consistency**: different parts of the system might temporarily have outdated information until all events are processed.
-   **Complex Debugging**: harder to trace issues across multiple async events.
-   **Increased Latency**: some events may take longer to be processed due to async nature.
-   **Event Duplications**: requires idempotency to avoid duplicate processing.
-   **Event Ordering Issues**: some brokers don’t guarantee message order (RabbitMQ).
-   **Learning Curve**: requires expertise in event-driven design patterns.

## [](https://dev.to/jhonifaber/introduction-to-event-driven-architecture-eda-3ioj?context=digest#conclusion)**Conclusion**

If you are thinking of implementing a distributed, real-time and highly scalable system, you should definitely consider implementing an event-driven architecture to take advantage of all the benefits it offers.
