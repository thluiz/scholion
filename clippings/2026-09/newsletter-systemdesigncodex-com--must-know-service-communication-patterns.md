---
url: "https://newsletter.systemdesigncodex.com/p/service-communication-patterns?ref=dailydev"
captured_at: "2026-09-25T18:13:30+01:00"
title: "Must-Know Service Communication Patterns"
domain: "newsletter-systemdesigncodex-com"
---

Communication is the essence of building any system distributed across multiple nodes.

Very little can be achieved without two or more components of your system talking to each other over a network.

However, you may have also experienced that getting the communication right is always tricky. I’ve often seen developers trying to apply a single pattern to all problems when it should be the other way around.

In this post, I’ll cover the main communication patterns at your disposal and how you should think about using them.

This is a synchronous communication pattern. One service sends a request to another service and remains blocked until it receives a response or error.

REST is the most popular architectural style for this type of communication. It uses the HTTP protocol and its methods (such as GET, POST, PUT, DELETE).

This pattern is robust and widely used, but there’s one pitfall where it can do more harm than good.

Don’t rely on synchronous request-response if you have a chain of services talking to each other. Even if one service in the chain faces an issue, the entire operation can fail. Also, it can lead to resource wastage and cascading failures.

This pattern flies a bit under the radar not because it’s not heavily used but because developers don’t think of it as a communication pattern.

In this pattern, one component writes data to a specific location, and another component reads and processes the data. For example, one service may drop a file in an S3 bucket and another service picks up that file to take the next action.

The pattern is simple to implement. It can help old legacy systems talk to modern systems without compatibility issues. File handling is something all programming languages and frameworks support.

However, as a drawback, this pattern is not suitable for low-latency requirements.

The request-response approach need not always be synchronous. You can implement it in an asynchronous non-blocking manner.

In an asynchronous non-blocking request-response implementation, the receiving service has to explicitly know the destination for sending the response.

Message queues are ideal to implement this pattern. Apart from facilitating communication, the message queues allow multiple requests to be buffered.

The challenging aspect of this communication pattern is the correlation between request and response. The service instance that sent the request may not be the same as the instance receiving the response and therefore, needs a way to keep track of the requests.

Lastly, we have the event-driven communication pattern.

In this approach, a service doesn’t directly talk to another service. Instead, it emits an event that other services can consume.

This means that you need a place where services can send the event data and a mechanism by which receiving services can discover the events.

Message brokers like RabbitMQ can handle both aspects. Producers use an API to push events to the broker, while the broker manages subscriptions, notifying consumers when an event arrives.

This pattern is great for building loosely coupled interactions between services.

However, the message broker needs to ensure reliable event delivery, ordering, and consistency. Plus, there is an additional component in the mix.

👉 **So - which communication pattern have you used?**

[Leave a comment](https://newsletter.systemdesigncodex.com/p/service-communication-patterns/comments)

Here are some interesting articles I’ve read recently:

*   [Is Copilot Fooling You](https://open.substack.com/pub/akoskm/p/fooled-by-my-ai-coach-is-copilot?r=1m1f9z&utm_campaign=post&utm_medium=web) by [Akos](https://open.substack.com/users/50223467-akos?utm_source=mentions)
    
*   [How to get started learning AWS Cloud in 30 Days](https://www.thecloudplaybook.com/p/how-to-get-started-learning-aws-cloud?r=1m1f9z&utm_campaign=post&utm_medium=web) by [Amrut Patil](https://open.substack.com/users/17666670-amrut-patil?utm_source=mentions)
    
*   [Comparison Guide: Bootstrap vs. Tailwind CSS. When and What to choose?](https://thetshaped.dev/p/comparison-guide-bootstrap-vs-tailwindcss?r=1m1f9z&utm_campaign=post&utm_medium=web) by [Petar Ivanov](https://open.substack.com/users/10269058-petar-ivanov?utm_source=mentions)
    

**That’s it for today! ☀️**

Enjoyed this issue of the newsletter?

Share with your friends and colleagues.

[Share](https://newsletter.systemdesigncodex.com/p/database-caching-strategies?utm_source=substack&utm_medium=email&utm_content=share&action=share&token=eyJ1c2VyX2lkIjo5NzQ4NDE4MywicG9zdF9pZCI6MTM5MzgwNTM1LCJpYXQiOjE3MDYyMzg2NzEsImV4cCI6MTcwODgzMDY3MSwiaXNzIjoicHViLTIxNDgxMTEiLCJzdWIiOiJwb3N0LXJlYWN0aW9uIn0.g1BLNvN1bO0UbRH-bufX7vstlve_rQsqx7Iylcr-ENs)

_**See you later with another edition — Saurabh**_
