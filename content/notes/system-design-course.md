---
title: "GitHub - karanpratapsingh/system-design: Learn how to design systems at scale and prepare for system design interviews"
date: '2026-09-25T08:56:35+01:00'
category: webclip
summary: 'Course outline on system design covering networking, storage, databases, distributed systems, APIs, messaging, security, and interview patterns, plus worked designs for URL shortener, WhatsApp, Twitter, Netflix, and Uber.'
tags: ["system-design","distributed-systems","databases","system-design-interviews"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "GitHub - karanpratapsingh/system-design: Learn how to design systems at scale and prepare for system design interviews"
    url: "https://github.com/karanpratapsingh/system-design?utm_source=weeklyfoo&utm_medium=email&utm_campaign=weeklyfoo"
    kind: repo
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/github-com--system-design-course.md"
    kind: repo
---

The page presents a course on system design and organizes it from fundamentals to interview-oriented case studies. It covers networking basics, storage, caching, load balancing, databases, distributed systems, APIs, messaging, security, and scaling concepts, then applies them to URL shortener, WhatsApp, Twitter, Netflix, and Uber designs.

## Reading notes

- The course begins by defining system design as the process of defining architecture, interfaces, and data for a system that meets specific requirements.
- The structure of the content includes chapters on networking, storage, databases, distributed architecture, service communication, security, and system design interviews.
- The material explains IP, the OSI model, TCP and UDP, DNS, load balancing, clustering, cache, CDN, and proxy.
- It also covers availability, scalability, storage, and concepts such as RAID, volumes, file storage, block storage, object storage, NAS, and HDFS.
- In the database section, it distinguishes SQL and NoSQL, discusses replication, indexes, normalization, denormalization, ACID, BASE, CAP, PACELC, transactions, distributed transactions, sharding, consistent hashing, and federation.
- The architecture section covers N-tier, message brokers, message queues, publish-subscribe, ESB, monoliths and microservices, event-driven architecture, event sourcing, CQRS, API gateway, REST, GraphQL, gRPC, and real-time communication methods such as long polling, WebSockets, and SSE.
- The text also covers geohashing, quadtrees, circuit breaker, rate limiting, service discovery, SLA, SLO, SLI, disaster recovery, VMs, containers, OAuth 2.0, OIDC, SSO, SAML, SSL, TLS, and mTLS.
- The interview part recommends clarifying functional, non-functional, and extended requirements, estimating scale, drawing the data model, defining APIs, assembling high-level components, and identifying bottlenecks.
- The URL shortener example defines requirements for short alias generation, redirection, expiration, abuse prevention, and analytics, as well as discussing Base62, MD5, counter, Key Generation Service, and cache.
- The WhatsApp example describes one-to-one chat, groups, file sharing, receipts, last seen, push notifications, WebSockets, presence, media service, object storage, CDN, and API gateway.
- The Twitter example includes posts, follow, newsfeed, search, retweets, favorites, ranking, fan-out, Elasticsearch, Kafka, Spark, cache, media storage, and CDN.
- The Netflix example covers streaming, upload, search, comments, video processing, transcoding, quality, HLS, CDN, geo-blocking, recommendations, and analytics.
- The Uber example addresses nearby cab search, booking, live location, geohashing, quadtrees, surge pricing, payments, notifications, sharding, and cache.
