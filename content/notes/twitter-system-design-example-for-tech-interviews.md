---
title: "Twitter System Design Example for Tech Interviews"
date: '2026-09-25T01:04:31+01:00'
category: webclip
summary: 'A system design guide for interviews that structures the creation of a Twitter/X.com into requirements, capacity estimates, APIs, database, architecture, and trade-offs.'
tags: ["system-design","twitter","interview-prep"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Twitter System Design Example for Tech Interviews"
    url: "https://dev.to/somadevtoo/twitter-system-design-example-for-tech-interviews-1ihb?context=digest"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--twitter-system-design-example-for-tech-interviews.md"
    kind: repo
---

The post frames Twitter or X.com as a common system design interview problem and says the main challenge is explaining a structured design within 40 minutes. It walks through requirements, capacity estimation, QPS, API design, database design, storage, high-level architecture, detailed components, trade-offs, failure scenarios, and bottlenecks.

## Reading notes

- The text presents Twitter or X.com as a typical system design interview case and insists on the need for a structured answer to fit within the time of the conversation.
- It proposes a template to organize the answer and says that following this structure helps articulate the reasoning better in the interview.
- In the functional requirements, it lists posting tweets, following users, and favoriting tweets.
- In the non-functional requirements, it highlights scalability, high availability, and stability.
- In the capacity estimate, it assumes 500 million users.
- From this base, it estimates 500 million tweets per day, 10 feed pages per user per day, 100 followers on average per user, and 5 favorites per day.
- It converts these assumptions into an approximate load of 15k QPS for writes, 75k QPS for reads, and 30k QPS for favorites.
- It estimates 140 GB of new data per day for tweets and 10 TB per day for media, reaching 50 TB per year for tweets and 4 PB per year for media.
- In the tweeting API, it proposes a method to post a tweet with userId, text, location, and date.
- In the follow API, it proposes methods to follow and unfollow users.
- In the favorites API, it proposes methods to favorite and unfavorite tweets.
- For the feed, it proposes an API for obtaining timelines with pagination.
- In the database, it defines tables for user information, tweets, and follower relationships.
- The users table stores userId, userName, status, and other profile data.
- The tweets table stores tweetId, userId, content, postTime, modifyTime, and status.
- The followers table stores userId, followerId, and followedTime.
- In the storage layer, it suggests MySQL for structured data and Amazon S3 for images and videos.
- In the high-level architecture, it describes clients, load balancers, rate limiter, CDN, tweet, user, follow, and feed services, plus Redis, MySQL, and S3 in the data layer.
- In the request flow, the call passes through the load balancer, goes to a server, passes through the rate limiter, writes to MySQL and Redis, and uses CDN for media on reads.
- In the detailed design, it recommends multiple load balancers in a cluster and algorithms such as round-robin, least connections, or IP hash.
- For CDN, it suggests pull and push caching and TTL tuning to improve hit rate.
- For Redis, it suggests a cluster, master-slave replication, and Sentinel for failover.
- For MySQL, it suggests a master-slave architecture and horizontal partitioning.
- In the trade-offs, it chooses MySQL over NoSQL because of complex queries and transaction support.
- It also chooses Redis over Memcached because of data types, advanced features, and horizontal scalability.
- Among failure scenarios, it proposes a hybrid pull and push model for users who follow many people.
- For read hotspots, it recommends Redis cache with cache-aside and use of local cache.
- As a future improvement, it suggests an active-active multi-region strategy for disaster recovery and high availability.
