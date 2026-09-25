---
title: "Understanding concepts in Event Driven Architectures (EDA)"
date: '2025-04-03T09:24:29-03:00'
category: webclip
summary: 'The page explains event-driven architecture as an asynchronous way for system parts to communicate through events, then outlines producers, brokers, consumers, exchanges, and trade-offs.'
tags: ["event-driven-architecture", "message-broker", "rabbitmq", "kafka"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Understanding concepts in Event Driven Architectures (EDA) - DEV Community"
    url: "https://dev.to/jhonifaber/introduction-to-event-driven-architecture-eda-3ioj?context=digest"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-04/dev-to--understanding-concepts-in-event-driven-architectures.md"
    kind: repo
---

Event-driven architecture is presented as a way to build highly scalable distributed systems. The page says different parts of a system communicate by sending and reacting to events, and shows a flow where one service emits an event and other services listen and act on it asynchronously.

## Reading notes

- An event is something that happens, such as a user signing up, uploading a photo, or completing a payment.
- A producer or publisher creates and emits events when something happens.
- A message broker sits between producers and consumers, receives events, stores them, and routes them to the right services.
- Channels in message brokers organize how events move from producers to consumers; in Kafka they are called topics, and in RabbitMQ they are called queues.
- Kafka supports a multi-subscriber model, while RabbitMQ queues are described as point-to-point, with one consumer processing a message from a queue.
- An event consumer or subscriber listens for events and reacts to them, such as sending a welcome email after a user registers.
- The event itself is the message describing what happened and usually contains structured data like JSON or XML.
- A direct exchange routes messages only when the routing key exactly matches the queue binding key.
- A fanout exchange sends the same message to all bound queues and ignores the routing key.
- A topic exchange routes messages by wildcard patterns in routing keys, using `*` for one word and `#` for multiple words.
- The page lists scalability, flexibility, real-time processing, resilience, and loose coupling as advantages of EDA.
- It also lists eventual consistency, complex debugging, increased latency, event duplications, event ordering issues, and a learning curve as disadvantages.
- The conclusion says EDA should be considered for distributed, real-time, and highly scalable systems.
