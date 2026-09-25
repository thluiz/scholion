---
title: "Message Queues & Message Brokers"
date: '2026-09-25T18:11:11+01:00'
category: webclip
summary: 'The page explains how message queues enable asynchronous producer-consumer communication, and how brokers manage queues while adding routing, transformation, protocol translation, and pub/sub support.'
tags: ["message-queues", "message-brokers", "pub-sub", "asynchronous-communication"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Message Queues & Message Brokers"
    url: "https://newsletter.systemdesigncodex.com/p/message-queues-and-message-brokers?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/newsletter-systemdesigncodex-com--message-queues-and-message-brokers.md"
    kind: repo
---

Message queues are presented as a FIFO structure that lets producers and consumers communicate asynchronously. The page uses file processing in a web application to show how a job can be queued, stored in object storage, and later processed by a worker. It also lists background tasks, competing consumers, email and notification services, buffering, and payment retries as common uses.

## Reading notes

- A message queue stores messages in FIFO order, with new messages added at the back and removed from the front.
- Queues enable asynchronous communication between producer and consumer.
- A web app can create a job for an uploaded file, add it to a task queue, store the file in object storage, and let a worker process it later.
- Common uses include scheduling background tasks, distributing work across multiple workers, email and notification services, data buffering, and retrying failed payment transactions.
- A message broker is middleware that manages one or more message queues.
- Brokers can route messages to different destinations using routing keys.
- Brokers can transform messages by changing their format or content.
- Brokers can translate messages from one protocol to another, such as HTTP to JMS.
- Brokers support publish-subscribe communication.
- In the example, an Order Service publishes an OrderCreated message, while Inventory, Shipping, and Notification services subscribe to react to it.
