---
title: "How to Design Twitter (X) in a System Design Interview?"
date: '2025-06-23T04:09:52+00:00'
category: webclip
summary: 'The article outlines a structured way to answer a Twitter-like system design interview by covering requirements, capacity estimates, APIs, database tables, caching, load balancing, and failure scenarios.'
tags: ["system-design", "twitter", "interview-prep"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to Design Twitter (X) in a System Design Interview?"
    url: "https://medium.com/javarevisited/how-to-design-twitter-in-a-system-design-interview-98983c649cc0"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-06/medium-com--how-to-design-twitter-x-in-a-system-design-interview.md"
    kind: repo
---

The article presents a step-by-step interview template for designing a Twitter-like messaging app. It emphasizes that the main difficulty in the interview is time, so the answer should be structured around requirements, estimates, APIs, storage, high-level architecture, request flow, trade-offs, and bottlenecks.

## Reading notes

- The problem is framed as a common system design interview question about Twitter or X.com.
- The author says the key challenge in the interview is convincing the interviewer in about 40 minutes.
- A structured system design template is recommended to organize the answer.
- Functional requirements include composing tweets, following users, and favoriting tweets.
- Non-functional requirements include scalability, high availability, and stability.
- The example capacity estimate assumes 500 million users.
- The traffic estimate includes 500 million tweets per day, 10 home feed page views per user per day, 100 followed users on average, and 5 favorites per user per day.
- The article estimates about 15k QPS for writes, 75k QPS for reads, and 30k QPS for favorites.
- Data size estimates include 140GB of tweet data per day and about 10TB per day for media.
- The proposed APIs cover posting tweets, following and unfollowing users, favoriting and unfavoriting tweets, and fetching feeds.
- The database design includes UserInfo, Tweets, and Follower tables.
- MySQL is suggested for structured data and Amazon S3 for media storage.
- The high-level design includes clients, load balancers, rate limiting, CDNs, server clusters, Redis, MySQL, and S3.
- The request flow goes from client to load balancer, then server, then MySQL and Redis, with media served through the CDN.
- Detailed component choices include clustered load balancers, Redis cluster with Sentinel, and MySQL master-slave replication with horizontal partitioning.
- MySQL is chosen over NoSQL for complex queries and transactions.
- Redis is chosen over Memcached for richer data types and horizontal scaling.
- For users who follow many accounts, the article suggests a hybrid pull-and-push feed model.
- For read hotspots, it suggests caching hot data in Redis and using local caches.
- A future improvement mentioned is a multi-region active-active strategy for disaster recovery and high availability.
