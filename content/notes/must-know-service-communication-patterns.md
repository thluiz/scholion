---
title: "Must-Know Service Communication Patterns"
date: '2026-09-25T18:13:30+01:00'
category: webclip
summary: 'The post outlines four service communication patterns: synchronous request-response, file-based exchange, asynchronous request-response, and event-driven communication, with their main uses and tradeoffs.'
tags: ["service-communication", "request-response", "message-queues", "event-driven"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Must-Know Service Communication Patterns"
    url: "https://newsletter.systemdesigncodex.com/p/service-communication-patterns?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/newsletter-systemdesigncodex-com--must-know-service-communication-patterns.md"
    kind: repo
---

The post says communication is central to distributed systems and warns against using one pattern for every problem. It surveys the main service communication patterns and the situations where each one fits or breaks down.

## Reading notes

- Synchronous request-response keeps the caller blocked until a response or error arrives
- REST is presented as the most common style for synchronous communication, using HTTP methods like GET, POST, PUT, and DELETE
- Synchronous chains can fail end to end, waste resources, and create cascading failures
- File-based communication has one component write data to a location and another read and process it
- File-based exchange can connect legacy systems with modern systems, but it is not suited to low-latency needs
- Asynchronous request-response avoids blocking, and the receiving service must know where to send the response
- Message queues fit asynchronous request-response and can buffer multiple requests
- Correlating request and response is the hard part when the sending instance and receiving instance differ
- Event-driven communication has a service emit an event that other services consume
- Message brokers such as RabbitMQ handle event storage, subscriptions, and consumer notification
- Event-driven systems support loosely coupled interactions, but brokers must provide reliable delivery, ordering, and consistency
