---
title: "Scaling Ruby Apps to 1000 Requests per Minute - A Beginner's Guide"
date: '2015-07-31T20:47:25-03:00'
category: webclip
summary: 'The post argues that scaling Ruby apps is mostly about throughput, request queues, and server choice. For sub-1000 rpm systems, it favors buffering and concurrency over adding dynos.'
tags: ["ruby", "scaling", "request-queue", "puma"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Scaling Ruby Apps to 1000 Requests per Minute - A Beginner's Guide"
    url: "http://nateberkopec.com/2015/07/29/scaling-ruby-apps-to-1000-rpm.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-07/nateberkopec-com--scaling-ruby-apps-to-1000-requests-per-minute.md"
    kind: repo
---

The post focuses on Ruby applications below 1000 requests per minute and says the main scaling problem is not raw speed but how requests are queued and accepted. It explains Heroku routing, compares server models, and argues that scaling hosts only helps when requests are waiting.

## Reading notes

- The article limits itself to Ruby apps at 1000 requests per minute or less and excludes database scaling, Redis, RabbitMQ, Kafka, and devops beyond the application server.
- It says many Rails apps are over-scaled and wasting money because developers add dynos or larger instances when the real issue is elsewhere.
- Scaling increases throughput, not speed, and only improves response times when requests are waiting in a queue.
- It explains that Heroku requests pass through a load balancer and then a router, where each router has its own request queue and may wait up to five seconds for a dyno connection.
- Webrick is described as single-thread, single-process, and bad with slow clients and slow uploads.
- Thin is described as event-driven and better with slow clients, but it still struggles with slow application responses and I/O without custom work.
- Unicorn uses a master process and worker processes on a Unix socket, so free workers can still handle requests while others process work, but it is vulnerable to slow client downloads.
- Phusion Passenger 5 combines worker processes with a buffering reverse proxy, which protects workers from slow clients and can route to unused workers.
- Puma in threaded mode can continue accepting requests while threads wait on I/O, and clustered Puma combines threads with multiple workers to handle both slow clients and slow responses.
- The article concludes that on Heroku with MRI/C Ruby, the serious scalable choices are clustered Puma and Passenger 5, while custom setups can also use Unicorn with nginx.
- It says queue time should be measured before scaling and that low queue times mean scaling is pointless.
- It presents Little’s Law as a way to estimate capacity from request rate and average response time, while noting that response-time variation and blocking make it only approximate.
- It uses Twitter, Shopify, and Envato numbers to compare theoretical capacity with real-world instance counts and to show when the math matches or diverges.
