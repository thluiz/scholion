---
url: "https://newsletter.systemdesigncodex.com/p/message-queues-and-message-brokers?ref=dailydev"
captured_at: "2026-09-25T18:11:11+01:00"
title: "Message Queues & Message Brokers"
domain: "newsletter-systemdesigncodex-com"
---

Synchronous communication dominates the world of software development, but sometimes it can make the users wish they never crossed paths with your application.

It’s not a pretty sight when that happens. The application support is bombarded with complaints and threats, resulting in a general loss of reputation that takes years to mend.

Message queues and message brokers can come in quite handy at such times.

A message queue is a data structure that stores messages in FIFO order. Every new message enters the back of the queue while messages are removed from the front of that queue.

This capability of message queues unlocks asynchronous communication between the producer and consumer, which is game-changing.

Here’s a practical use of a message queue:

Consider that you want to process files uploaded through a web application. The message queue can act as a task queue that processes jobs asynchronously.

When the user uploads a large file for processing:

*   The web server receives the file and creates a job.
    
*   The job is added to a task queue and the file is uploaded to an object storage.
    
*   Later on, a worker process consumes the jobs from the queue one by one and processes them. It gets the file from the object storage.
    

This is just a small example. Message queues have several more uses such as:

Message queues have several uses such as:

*   Schedule and manage background tasks
    
*   Distributing tasks across multiple worker instances using the competing consumer pattern.
    
*   Email and notification services
    
*   Data buffering
    
*   Retries in payment processing where failed transactions are queued for retries
    

So far so good. Now, at some point, you must have also come across the term “message broker”.

A message broker is a middleware that manages one or more message queues. It also supports other features such as:

*   **Message Routing:** This is about directing messages to different destinations based on certain criteria. Brokers use routing keys to send the messages to the correct queue. This is like the flight number on a flight ticket.
    
*   **Message Transformation:** This involves changing the format or content of messages. For example, replacing all numbers with a special character before sending it to a queue.
    
*   **Protocol Translation:** Convert messages from one protocol to another. For example, translating an incoming HTTP message to a JMS message.
    

Most important, however, is that message brokers enable a crucial communication pattern known as publish-subscribe.

Pub/Sub makes message brokers ideal for communication between different applications or services. Here’s an example:

Consider an e-commerce platform that needs to integrate multiple services:

*   **Order Service:** When a new order is placed, it publishes an “OrderCreated” message to the broker.
    
*   **Inventory Service:** Subscribes to the “OrderCreated” message to update stock levels.
    
*   **Shipping Service:** Also, subscribes to the “OrderCreated” messages to initiate the shipping process.
    
*   **Notification Service:** Subscribes to various events to send emails or push notifications to customers.
    

The diagram below shows this flow with a message broker acting as the central hub.

**👉 So - have you used message queues and message brokers in your application?**

[Leave a comment](https://newsletter.systemdesigncodex.com/p/message-queues-and-message-brokers/comments)

Here are some interesting articles I’ve read recently:

*   [Startup to Mid-Market Tech: What I Learned in 3 Months](https://open.substack.com/pub/akoskm/p/startup-to-mid-market-tech-what-i?r=1m1f9z&utm_campaign=post&utm_medium=web) by [Akos](https://open.substack.com/users/50223467-akos?utm_source=mentions)
    
*   [TCP#23: Every byte of data has a story](https://www.thecloudplaybook.com/p/tcp23-every-byte-of-data-has-a-story?r=1m1f9z&utm_campaign=post&utm_medium=web) by [Amrut Patil](https://open.substack.com/users/17666670-amrut-patil?utm_source=mentions)
    
*   [The importance of taking breaks and recharging your batteries](https://thetshaped.dev/p/importance-taking-breaks-recharge-batteries?r=1m1f9z&utm_campaign=post&utm_medium=web) by [Petar Ivanov](https://open.substack.com/users/10269058-petar-ivanov?utm_source=mentions)
    

**That’s it for today! ☀️**

Enjoyed this issue of the newsletter?

Share with your friends and colleagues.

[Share](https://newsletter.systemdesigncodex.com/p/message-queues-and-message-brokers?utm_source=substack&utm_medium=email&utm_content=share&action=share)

_**See you later with another edition — Saurabh**_
