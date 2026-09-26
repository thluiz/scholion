---
title: "Message Queues in System Design"
date: '2024-09-07T03:05:20+00:00'
category: webclip
summary: 'The page explains message queues as an asynchronous buffer between producers and consumers, showing how they decouple work, improve durability, and let systems scale under load.'
tags: ["message-queues", "system-design", "asynchronous-communication"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Message Queues in System Design - Level Up Coding"
    url: "https://levelup.gitconnected.com/message-queues-in-system-design-0440a1221023"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2024-09/levelup-gitconnected-com--message-queues-in-system-design.md"
    kind: repo
---

The page describes message queues as a way to handle application events asynchronously instead of processing everything at once. In the example of an online store, order tasks are turned into messages, added to a queue, and later processed by workers. The queue acknowledges processed messages and removes them after successful handling.

It also says message queues help decouple producers and consumers, let one side keep working when the other is unavailable, and keep data durable if the queue or a worker crashes. The page also mentions that queues can support scalability, and it lists FIFO and priority queues, plus push-based and pull-based queues. It ends with examples such as RabbitMQ, Kafka, and Amazon SQS.

## Reading notes

- Message queues are a durable component stored in memory that supports asynchronous communication.
- Input services act as producers or publishers, while other services act as consumers or subscribers.
- In the store example, order details are turned into a message, sent to the queue, and processed by workers.
- The queue removes a message after the server acknowledges that it received and processed it.
- The main benefit is decoupling events so they can be processed asynchronously.
- A producer can post messages even when the consumer is unavailable, and a consumer can read messages even when the producer is unavailable.
- If the queue crashes, the data is not lost because it is stored on disk.
- If a worker crashes while processing a message, another worker can pick it up from the queue.
- Message queues support scalability by letting the queue grow and allowing more workers to be added.
- FIFO queues process messages in arrival order.
- Priority queues process more important messages sooner.
- Some queues are pull-based, while others are push-based.
- Examples mentioned are RabbitMQ, Kafka, and Amazon SQS.
