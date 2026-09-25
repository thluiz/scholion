---
url: "https://dev.to/somadevtoo/twitter-system-design-example-for-tech-interviews-1ihb?context=digest"
captured_at: "2026-09-25T01:04:31+01:00"
title: "Twitter System Design Example for Tech Interviews"
domain: "dev-to"
---

_Disclosure: This post includes affiliate links; I may receive compensation if you purchase products or services from the different links provided in this article._

[![Twitter System Design Example](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fs6jlqztank2nscgj23hg.png)](https://bit.ly/3Mnh6UR)

credit - [**Sandeep/CodeKarle**](https://bit.ly/3D2qsRS)

Hello guys, if you are preparing for a system design interview and looking for common System design problems and resources, then you have come to the right place.

In the past, I have talked about essential system design concepts like [API Gateway vs Load Balancer](https://dev.to/somadevtoo/difference-between-api-gateway-and-load-balancer-in-system-design-54dd) and [Horizontal vs Vertical Scaling](https://dev.to/somadevtoo/horizontal-scaling-vs-vertical-scaling-in-system-design-3n09), [Forward proxy vs reverse proxy](https://dev.to/somadevtoo/difference-between-forward-proxy-and-reverse-proxy-in-system-design-54g5) as well common [System Design problems](https://dev.to/somadevtoo/top-50-system-design-interview-questions-for-2024-5dbk) and today I am going to discuss one popular System design problem --- designing Twitter or X.com.

Designing a complex system like Twitter can be challenging, especially in a system design interview.

**The biggest challenge is not the complexity but the time, as you need to convince your interviewer in 40 minutes** **that you know your stuff** and this can only be possible if you prepare well and follow a structured approach while answering such questions.

In this system design tutorial, I will also give you a simple guide to help you structure a system design template (see below) to collect your thoughts and present a clear design.

By the way, if you are preparing for System design interviews and want to learn System Design in a limited time then you can also check sites like [**ByteByteGo**](https://bit.ly/3P3eqMN), [**DesignGurus.io**](https://bit.ly/3pMiO8g), [**Exponent**](https://bit.ly/3cNF0vw), [**Educative.io**](https://bit.ly/3Mnh6UR), [**Codemia.io**](https://codemia.io/?via=javarevisited) and [**Udemy**](https://bit.ly/3vFNPid) which have many great System design courses

Similarly, while answering System design questions, you can also follow a System design template like this from [**DesignGurus.io**](https://bit.ly/3pMiO8g)to articulate your answer better in a limited time.

Following this template is one of the best things you can do to start your preparation for any system design interview.

[![System Design template for interviews](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F7lj6202p2n776w8bksum.jpg)](https://bit.ly/3pMiO8g)

Now, let's jump into the problem and solution.

* * *

## [](#how-to-design-twitter-or-xcom)How to design Twitter or X.com?

Designing a system like Twitter is a common scenario in system design interviews, but if you want to practice this question from scratch you can start it on [**_Codemia.io_**](https://codemia.io/?via=javarevisited) which is a Leetcode-style platform for system design interviews.

It has more than 120+ system design problems and is growing, including Designing Twitter. It also provides editorial solutions created by senior engineers from reputed companies.

It also has free System Design questions and [**_designing Twitter is_**](https://codemia.io/system-design/design-twitter/editorial?via=javarevisited) is one of them. You can access it here.

Now coming back to the question itself, it's a great way to showcase your understanding of large-scale distributed systems, as it involves various aspects such as handling massive user bases, ensuring high availability, and maintaining stability under heavy loads.

This solution guide will walk you through the process of designing Twitter, covering system requirements, capacity estimation, API design, database design, high-level design, request flow, detailed component design, trade-offs, and potential failure scenarios.

By the end of this guide, you'll have a solid understanding of how to approach and present this design in an interview setting.

Here is a Twitter architecture diagram to get an overall idea:

[![Twitter feed architecture](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F5pfjmn2so4b9d2e1ngvv.png)](https://bit.ly/3Mnh6UR)

As I said we will solve this problem step by step, and we will cover:

1.  Requirements
2.  Capacity Estimations
3.  QPS (Queries Per Second)
4.  API Design
5.  Database Design
6.  Tables
7.  Storage
8.  High-level design
9.  Detailed Component Design
10.  Failure Scenarios and Bottlenecks
11.  Tradeoffs

So, what are we waiting for, let's start.

## [](#twitter-system-requirements)Twitter System Requirements

First thing you should get the requirements right, and it starts with functional requirements.

Choose the one you are most familiar with if you are cloning a real app, like buying stuff on Amazon or sending messages on Facebook or Twitter.

### [](#functional-requirements)Functional Requirements

To design a robust and user-friendly Twitter-like system, we need to outline the core functionalities.

Users should be able to compose and share tweets, which is the primary function of the platform.

This involves creating a new tweet, attaching optional media, and sharing it with their followers. Additionally, users should be able to follow other users to see their updates in their feeds.

This means managing a list of followed users and ensuring their tweets appear in the user's timeline.

Another essential feature is allowing users to favorite tweets, indicating their appreciation and potentially bookmarking these tweets for future reference.

Here are the key functional requirements for your reference:

1.  **Compose and Share Tweets**: Users should be able to create and share tweets.
2.  **Follow Users**: Users should be able to follow other users and see their updates.
3.  **Favorite Tweets**: Users should be able to favorite tweets to show appreciation.

* * *

### [](#nonfunctional-requirements)Non-Functional Requirements

For a platform with the scale of Twitter, non-functional requirements are crucial. Scalability is paramount as the system must handle a vast number of users, tweets, and interactions without degradation in performance.

High availability ensures that the platform remains accessible and functional even during peak traffic times or in the event of hardware failures.

Stability is another critical aspect, as the service must be reliable, with minimal downtime and consistent performance, even under high concurrency.

Here are the key non-functional requirements that you should mention during the interview:

1.  **Scalability**: The system should handle a large number of users, tweets, and interactions.
2.  **High Availability**: The system should be available even under high traffic.
3.  **Stability**: The system should be stable and accessible without frequent issues or downtime.

* * *

## [](#capacity-estimation)Capacity Estimation

Estimating the user base is the first step in understanding the scale of the system. For this design, let's assume a user base of 500 million. This helps us gauge the expected load and the necessary infrastructure to support such a large number of users.

**User Base**

*   Assume a user base of 500 million.

**Traffic**  
To get a sense of the daily operations, we need to estimate the traffic. Assuming each user tweets once a day, we can expect 500 million tweets daily.

Additionally, if each user views 10 pages of their home feed per day, this results in substantial read operations.

The following relationships also add to the complexity, with each user following 100 others on average, leading to 50 billion follow relationships.

Lastly, if each user favors 5 tweets daily, we have 2.5 billion favorite operations per day.

Here are the key traffic requirements you should consider or mention:

*   **Tweets**: 500 million tweets per day (one tweet per user per day).
*   **Home Feed**: Each user views 10 pages per day.
*   **Following**: Each user follows 100 other users on average, leading to 50 billion follow relationships.
*   **Favorites**: Each user favors 5 tweets per day, leading to 2.5 billion favorites per day.

* * *

### [](#qps-queries-per-second)QPS (Queries Per Second)

Breaking down these operations into queries per second (QPS) helps us understand the real-time load.

For write operations, we calculate approximately 15k QPS, for read operations about 75k QPS, and for favorite operations around 30k QPS.

These numbers help in planning the necessary infrastructure and load-balancing strategies.

*   **Write**: 500M×23600×24≈15k\\frac{500M \\times 2}{3600 \\times 24} \\approx 15k3600×24500M×2​≈15k QPS
*   **Read**: 500M×103600×24≈75k\\frac{500M \\times 10}{3600 \\times 24} \\approx 75k3600×24500M×10​≈75k QPS
*   **Favorites**: 500M×53600×24≈30k\\frac{500M \\times 5}{3600 \\times 24} \\approx 30k3600×24500M×5​≈30k QPS

* * *

### [](#data-size)Data Size

Understanding the data size is crucial for storage planning. With 500 million tweets daily, and each tweet averaging 300 bytes after considering encoding, this totals 140GB of new data daily, or 50TB annually.

For media content, if we assume it to be 100 times the size of tweets, it results in 10TB daily, or 4PB annually.

This estimation underscores the need for a distributed storage architecture.

*   **Tweets**: 500 million tweets daily, each with 140 characters (300 bytes each). This totals 140GB per day and 50TB per year.
*   **Media (Images/Videos)**: Assume 100 times the size of tweets, 10TB per day, and 4PB per year.

* * *

## [](#api-design)API Design

Now, let's talk about API Design, which is another important area in System design interviews:

### [](#tweeting)Tweeting

APIs for tweeting need to handle the creation and posting of tweets efficiently. This involves capturing user information, tweet content, location data, and timestamps. Proper error handling and validation are essential to ensure a smooth user experience.  

```
public Result postTweet(Long userId, String tweetText, String location, DateTime date);
```

Enter fullscreen mode Exit fullscreen mode

### [](#following)Following

The following functionality requires APIs to manage relationships between users. This includes following and unfollowing users, ensuring data integrity, and updating the user's following list promptly.  

```
public Result followUser(Long userId, Long followedUserId);\
public Result unfollowUser(Long userId, Long followedUserId);
```

Enter fullscreen mode Exit fullscreen mode

### [](#favorites)Favorites

APIs for favorites allow users to like or unlike tweets. These operations should be efficient, with proper indexing and error handling to ensure quick updates and an accurate count of favorites on each tweet.  

```
public Result favoriteTweet(Long userId, Long tweetId);\
public Result unfavoriteTweet(Long userId, Long tweetId);
```

Enter fullscreen mode Exit fullscreen mode

The feed rendering API is crucial for fetching and displaying tweets from followed users. This requires efficient querying and pagination to ensure quick load times and a seamless user experience.  

```
public Result getFeeds(Long userId, String location, int pageNo);
```

Enter fullscreen mode Exit fullscreen mode

* * *

## [](#database-design)Database Design

After API Design, let's talk about Database design

### [](#tables)Tables

The database design involves defining tables for users, tweets, and follower relationships. The `UserInfo` table stores user details, the `Tweets` table handles tweet content and metadata, and the `Follower` table manages follow relationships. Proper indexing is essential for fast lookups and updates.

*   **UserInfo Table**
*   userId (Primary Key)
*   userName
*   status
*   otherProfile (avatar, age, etc.)
*   **Tweets Table**
*   tweetId (Primary Key)
*   userId (Index)
*   content
*   postTime (Index)
*   modifyTime
*   status
*   **Follower Table**
*   userId
*   followerId (Index)
*   followedTime

Here is a simple ERD diagram to understand Twitter Schema architecture better:

[![Twitter architecture](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F44u76copkh7c5ihp7e1h.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F44u76copkh7c5ihp7e1h.png)

* * *

## [](#storage)Storage

Choosing the right storage solutions is critical. For structured data like user profiles and tweets, MySQL is a good choice due to its support for complex queries and transactions.

For media storage, Amazon S3 offers scalable and cost-effective storage for images and videos.

*   Use MySQL for structured data (users, tweets, follow relationships).
*   Use Amazon S3 for media storage (images and videos).

* * *

## [](#highlevel-design)High-Level Design

Let's see the high-level design first:

### [](#client-layer)Client Layer

[![twitter architecture client layer](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fi6dxu0xasysd7vnt2txy.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fi6dxu0xasysd7vnt2txy.png)

The client layer involves websites and apps sending requests to the server. These requests are distributed via load balancers to ensure even load distribution and high availability. Using a CDN for static files helps reduce latency and improve load times.

*   Clients (websites/apps) send requests to the server.
*   Requests are distributed via load balancers.
*   Use a rate limiter to protect backend servers.
*   Use a CDN for static files (images, videos).

### [](#server-layer)Server Layer

The client layer involves websites and apps sending requests to the server. These requests are distributed via load balancers to ensure even load distribution and high availability.

Using a CDN for static files helps reduce latency and improve load times.

*   Server clusters handle requests and different services:
*   **Tweet Service**: Posting tweets.
*   **User Service**: User registration and profile management.
*   **Follow Service**: Following/unfollowing users.
*   **Home Feed Service**: Rendering user feeds.

### [](#data-layer)Data Layer

The data layer involves caching data with Redis to increase response speed and using MySQL for persistent storage with a master-slave architecture to ensure consistency and availability. Amazon S3 is used for storing media files, ensuring scalability and durability.

*   Use Redis for caching to increase response speed.
*   Use MySQL with master-slave architecture for data consistency and availability.
*   Use Amazon S3 for storing media files.

### [](#request-flow)Request Flow

Explaining the request flow helps in understanding how different components interact. When a client sends a request, it first hits the load balancer, which distributes it to an appropriate server.

The server processes the request, updates the database, and caches the necessary data. For read requests, data is retrieved from the cache or database, and media files are fetched from the CDN, ensuring quick response times.

1.  The client sends a request to the load balancer.
2.  The load balancer distributes the request to a server.
3.  The rate limiter checks the traffic.
4.  The server processes the request and stores data in MySQL and Redis.
5.  Media files are stored in CDN.
6.  For read requests, the server retrieves files from CDN and data from Redis or MySQL.

Here is a nice mermaid diagram to better understand the request flow in Twitter's architecture. When I practice system design problems on [Codemia.io](https://codemia.io/?via=javarevisited), I use their interface to create such a mermaid diagram also.

[![Twitter architecture request flow](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fk407xbxovaoi59tlelko.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fk407xbxovaoi59tlelko.png)

* * *

## [](#detailed-component-design)Detailed Component Design

Now, let's see the detailed component design and various software architecture components we can use to design Twitter.

### [](#load-balancer)Load Balancer

Deploying multiple load balancers in a cluster ensures high availability and even load distribution.

Placing load balancers in different locations reduces latency for users, and using various algorithms like round-robin or least connections helps manage the load efficiently.

*   Deploy multiple load balancers in a cluster.
*   Place load balancers in different locations to reduce latency.
*   Use algorithms like round-robin, least connections, or IP hash.

If you don't know what a load balancer is, here is a nice diagram from [**DesignGurus.io**](https://bit.ly/3pMiO8g), one of my favorite sites for learning System design:

[![ ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F3r2jp600la9j52kg71wa.png)](https://bit.ly/3pMiO8g)

* * *

### [](#cdn)CDN

Using a CDN for static content reduces the load on the origin server and improves load times for users. Optimizing caching rules and adjusting TTL helps achieve higher cache hit ratios, ensuring content is served quickly.

*   Use both pull and push caching approaches.
*   Optimize caching rules and TTL to achieve higher cache hit ratios.
*   Scale the system by adding more server nodes.

* * *

### [](#redis)Redis

Using Redis for caching involves setting up a Redis cluster for scalability and employing master-slave replication for high availability. Sentinel monitors the cluster and handles failovers, ensuring the cache remains available even during node failures.

*   Use Redis cluster for large-scale data.
*   Employ master-slave replication for high availability.
*   Use Sentinel to monitor the cluster and handle failovers.

* * *

### [](#mysql)MySQL

MySQL's master-slave architecture supports high-volume traffic and ensures data consistency through replication. Horizontal partitioning helps distribute the load across multiple servers, handling large datasets efficiently.

*   Use master-slave architecture for high-volume traffic.
*   Use horizontal partitioning to handle more data.

* * *

## [](#tradeoffs-and-tech-choices)Trade-offs and Tech Choices

This is probably the most important part of System Design interviews, as you will have to explain your choices and tradeoffs you made and how they help. let's see:

### [](#database)Database

Choosing MySQL over NoSQL is due to the need for complex queries and transaction support. While NoSQL offers schema flexibility, it lacks support for structured data and complex transactions, which are essential for Twitter's business model.

*   Chose MySQL over NoSQL due to the need for complex queries and transaction support.

### [](#cache)Cache

Redis is preferred over Memcached due to its support for various data types and horizontal scaling. While Memcached is efficient for basic key-value storage, Redis offers advanced features and better scalability, making it suitable for large-scale systems.

I chose Redis over Memcached for its advanced features and horizontal scaling.

* * *

## [](#failure-scenarios-and-bottlenecks)Failure Scenarios and Bottlenecks

Now, let's take a look at how robust and resilient our system is

### [](#hybrid-model)Hybrid Model

To handle users who follow many accounts, a hybrid model combining pull and push approaches can reduce latency. For users following many people, pushing new tweets reduces the load during feed aggregation, improving user experience.

*   If a user follows many people, combine pull and push models to reduce latency.

### [](#read-hotspot)Read Hotspot

Handling read hotspots, such as popular users with many followers, involves caching their tweets in Redis and using a cache-aside strategy for consistency. Adding hot zones in Redis servers and using local caches can distribute the load, avoiding excessive calls to the same server.

*   Cache hot data in Redis with a cache-aside strategy.
*   Use local cache to handle high traffic.

### [](#future-improvements)Future Improvements

Future improvements include implementing a multi-region active-active strategy for disaster recovery and high availability.

Deploying service clusters and database clusters in multiple locations with automatic failover and load balancing ensures no single point of failure, maintaining service continuity and reliability.

*   Implement a multi-region active-active strategy for disaster recovery and high availability.
*   Continue optimizing caching, load balancing, and data storage strategies to handle future growth.

* * *

## [](#best-system-design-interviews-resources-for-developers)Best System Design Interviews Resources for Developers

If you are preparing for a System design interview and looking for the best resources, here is a curated list of the best system design books, online courses, and practice websites to help you better prepare for System design interviews. Most of these courses also answer questions I have shared here.

### [](#best-system-design-interview-resources)Best System Design Interview Resources

And, here are curated list of the best system design books, online courses, and practice websites which you can check to better prepare for System design interviews. Most of these courses also answer questions I have shared here.

1.  [**ByteByteGo**](https://bit.ly/3P3eqMN): A live book and course by Alex Xu for System design interview preparation. It contains all the content of the System Design Interview book volumes 1 and 2, and will be updated with volume 3, which is coming soon.
    
2.  [**Codemia.io**](https://codemia.io/?via=javarevisited): This is another great platform to practice System design problems for interviews. It has more than 120+ System design problems, many of which are free, and also a proper structure to solve them.
    
3.  [**Bugfree.ai**](https://www.bugfree.ai/?via=javarevisited): Thisi is another popular platform for technical interview preparation. It contains AI-based mock interviews as well as Interview experience and more than 3200+ real questions on System Design, Machine Learning, and other topics for practice =.
    
4.  [**DesignGuru's Grokking System Design Course**](https://bit.ly/3pMiO8g): An interactive learning platform with hands-on exercises and real-world scenarios to strengthen your system design skills.
    
5.  [**"System Design Interview" by Alex Xu**](https://amzn.to/3nU2Mbp): This book provides an in-depth exploration of system design concepts, strategies, and interview preparation tips.
    
6.  [**"System Design Primer"**](https://bit.ly/3bSaBfC) on GitHub: A curated list of resources, including articles, books, and videos, to help you prepare for system design interviews.
    
7.  [**Educative's System Design Cours**](https://bit.ly/3Mnh6UR)e: An interactive learning platform with hands-on exercises and real-world scenarios to strengthen your system design skills.
    
8.  **High Scalability Blog**: A blog that features articles and case studies on the architecture of high-traffic websites and scalable systems.
    
9.  **[YouTube Channels](https://medium.com/javarevisited/top-8-youtube-channels-for-system-design-interview-preparation-970d103ea18d)**: Check out channels like "Gaurav Sen" (ex-Google engineer and founder of [InterviewReddy.io](https://interviewready.io/?aff=JavaRevisited) and "Tech Dummies" for insightful videos on system design concepts and interview preparation.
    
10.  [**"Designing Data-Intensive Applications"**](https://amzn.to/3nXKaas) by Martin Kleppmann: A comprehensive guide that covers the principles and practices for designing scalable and reliable systems.
     
11.  [**Exponent**](https://bit.ly/3cNF0vw): A specialized site for interview prep, especially for FAANG companies like Amazon and Google. They also offer a great system design course and many other materials to help you crack FAANG interviews.
     

[![how to prepare for system design](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fkqv3p46jmw5qc0newuiu.jpg)](https://bit.ly/3P3eqMN)

image\_credit - [ByteByteGo](https://bit.ly/3P3eqMN)  
Remember to combine theoretical knowledge with practical application by working on real-world projects and participating in mock interviews.

Continuous practice and learning will give you confidence for system design interviews.

That's all about **how to design Twitter or X.com** on system design interviews. By following this structure, you can design a robust and scalable system similar to Twitter. This guide will help you present your design effectively in a system design interview.

All the best for your System design interview
