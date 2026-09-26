---
url: "https://medium.com/javarevisited/how-to-design-twitter-in-a-system-design-interview-98983c649cc0"
captured_at: "2025-06-23T04:09:52+00:00"
title: "How to Design Twitter (X) in a System Design Interview?"
domain: "medium-com"
---

## Step by step solution of Twitter System design problem

[

![javinpaul](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*u9Ha3uTCjEmW_3gn.gif)

](https://medium.com/@javinpaul?source=post_page---byline--98983c649cc0---------------------------------------)

13 min read

Aug 16, 2024

\--

[](https://bit.ly/3D2qsRS)

credit — CodeCarle

Hello guys, if you are preparing for system design interview and looking for common System deign problems and resources then you have come to the right place.

In the past, I have shared [best System Design courses](https://levelup.gitconnected.com/7-best-software-design-course-for-programmers-and-developers-da3e18e9135), [books](https://medium.com/javarevisited/top-10-system-design-interview-books-in-2024-3e69e182e092), [websites,](https://medium.com/javarevisited/7-best-places-to-learn-system-design-79e2d261f343) [newsletters](https://medium.com/javarevisited/5-best-system-design-publications-and-newsletters-for-software-engineers-in-2024-54b8c8c5f65c), [cheat sheets](https://medium.com/javarevisited/top-3-system-design-cheat-sheets-templates-and-roadmap-for-software-engineering-interviews-53012952db28), [mock interviews](https://medium.com/javarevisited/3-best-mock-interview-platforms-for-system-design-and-coding-interviews-in-2024-7283f1579b17), [blogs](https://medium.com/javarevisited/40-must-read-engineering-blogs-to-learn-system-design-and-software-architecture-in-2024-aaa7c4f71ee6), [tips](https://medium.com/javarevisited/10-tips-for-system-design-interviews-fb3c2b6e4020), [GitHub repo](https://medium.com/javarevisited/10-best-github-repositories-to-prepare-for-system-design-interviews-6cc9d37d50f6), and [100+ System Design Interview Questions and Problems](https://javarevisited.blogspot.com/2024/05/100-system-design-interview-questions.html) and today I am going to discuss one popular System deign problem — designing Twitter or X.com.

Designing a complex system like Twitter can be challenging, especially in a system design interview.

**The biggest challenge is not the complexity but the time as you need to convince your interviewer in 40 minutes** **that you know your stuff** and this can only be possible if you prepare well and follow a structured approach while answering such questions.

In this System design tutorial I will also give you a simple guide to help you structure and system design template (see below) to collect your thoughts and present a clear design.

By the way, if you are preparing for System design interviews and want to learn System Design in a limited time then you can also checkout sites like [**ByteByteGo**](https://bit.ly/3P3eqMN), [**Design Guru**](https://bit.ly/3pMiO8g), [**Exponent**](https://bit.ly/3cNF0vw), [**Educative**](https://bit.ly/3Mnh6UR) and [**Udemy**](https://bit.ly/3vFNPid) which have many great System design courses

Similar, while answering System design questions you can also follow a System design template like this from [**_DesignGurus.io_**](https://bit.ly/3pMiO8g) to articulate your answer better in a limited time.

Following this template is actually one of the best thing you can do to start your preparation for any system design interview.

[](https://bit.ly/3pMiO8g)

Now, let’s jump into the problem and solution.

## How to design a Messaging App like Twitter or X.com?

Designing a system like Twitter is a common scenario in system design interviews but if you want to practice this question from scratch you can start it on [**_Codemia.io_**](https://codemia.io/?via=javarevisited) which is a Leetcode style platform for system design interviews.

It has more than 120+ system design problems and growing. It also provide editorial solution created by senior engineers from reputed company. It also got [**_free questions and designing Twitter i_**](https://codemia.io/system-design/design-twitter/editorial?via=javarevisited)s one of them. You can access it here.

Now coming back to question itself, it’s a great way to showcase your understanding of large-scale distributed systems, as it involves various aspects such as handling massive user bases, ensuring high availability, and maintaining stability under heavy loads.

This solution guide will walk you through the process of designing Twitter, covering system requirements, capacity estimation, API design, database design, high-level design, request flow, detailed component design, trade-offs, and potential failure scenarios.

By the end of this guide, you’ll have a solid understanding of how to approach and present this design in an interview setting.

## Table of Content

[**How to design a Messaging App like Twitter or X.com?**](#b17b)  
[**Twitter System Requirements**](#a30c)  
[**Capacity Estimation**](#516f)  
[**QPS (Queries Per Second)**](#f198)  
[**API Design**](#2449)  
[**Database Design**](#6085)  
[**Tables**](#90b7)  
[**Storage**](#b400)  
[**High-Level Design**](#002f)  
[**Detailed Component Design**](#0b15)  
[**Trade-offs and Tech Choices**](#2671)  
[**Failure Scenarios and Bottlenecks**](#0c34)  
[**Best System Design Interviews Resources (2025)**](#4ede)

## Twitter System Requirements

First thing you should get the requirements right and it starts with functional requirement.

Choose the one you are most familiar with if you are cloning a real app like buying stuff on Amazon or sending message on Facebook or Twitter.

## Functional Requirements

To design a robust and user-friendly Twitter-like system, we need to outline the core functionalities.

Users should be able to compose and share tweets, which is the primary function of the platform.

This involves creating a new tweet, attaching optional media, and sharing it with their followers. Additionally, users should be able to follow other users to see their updates in their feed.

This means managing a list of followed users and ensuring their tweets appear in the user’s timeline.

Another essential feature is allowing users to favorite tweets, indicating their appreciation and potentially bookmarking these tweets for future reference.

Here are the key functional requirements for your reference:

1.  **Compose and Share Tweets**: Users should be able to create and share tweets.
2.  **Follow Users**: Users should be able to follow other users and see their updates.
3.  **Favorite Tweets**: Users should be able to favorite tweets to show appreciation.

## Non-Functional Requirements

For a platform with the scale of Twitter, non-functional requirements are crucial. Scalability is paramount as the system must handle a vast number of users, tweets, and interactions without degradation in performance.

High availability ensures that the platform remains accessible and functional even during peak traffic times or in the event of hardware failures.

Stability is another critical aspect, as the service must be reliable, with minimal downtime and consistent performance, even under high concurrency.

Here are the key non-functional requirements which you should mention during interview:

1.  **Scalability**: The system should handle a large number of users, tweets, and interactions.
2.  **High Availability**: The system should be available even under high traffic.
3.  **Stability**: The system should be stable and accessible without frequent issues or downtime.

## Capacity Estimation

Estimating the user base is the first step in understanding the scale of the system. For this design, let’s assume a user base of 500 million. This helps us gauge the expected load and the necessary infrastructure to support such a large number of users.

## User Base

*   Assume a user base of 500 million.

## Traffic

To get a sense of the daily operations, we need to estimate the traffic. Assuming each user tweets once a day, we can expect 500 million tweets daily.

Additionally, if each user views 10 pages of their home feed per day, this results in substantial read operations.

Following relationships also add to the complexity, with each user following 100 others on average, leading to 50 billion follow relationships.

Lastly, if each user favorites 5 tweets daily, we have 2.5 billion favorite operations per day.

Here are the key traffic requirements you should consider or mention:

*   **Tweets**: 500 million tweets per day (one tweet per user per day).
*   **Home Feed**: Each user views 10 pages per day.
*   **Following**: Each user follows 100 other users on average, leading to 50 billion follow relationships.
*   **Favorites**: Each user favorites 5 tweets per day, leading to 2.5 billion favorites per day.

## QPS (Queries Per Second)

Breaking down these operations into queries per second (QPS) helps us understand the real-time load.

For write operations, we calculate approximately 15k QPS, for read operations about 75k QPS, and for favorite operations around 30k QPS.

These numbers help in planning the necessary infrastructure and load balancing strategies.

*   **Write**: 500M×23600×24≈15k\\frac{500M \\times 2}{3600 \\times 24} \\approx 15k3600×24500M×2​≈15k QPS
*   **Read**: 500M×103600×24≈75k\\frac{500M \\times 10}{3600 \\times 24} \\approx 75k3600×24500M×10​≈75k QPS
*   **Favorites**: 500M×53600×24≈30k\\frac{500M \\times 5}{3600 \\times 24} \\approx 30k3600×24500M×5​≈30k QPS

## Data Size

Understanding the data size is crucial for storage planning. With 500 million tweets daily, and each tweet averaging 300 bytes after considering encoding, this totals to 140GB of new data daily, or 50TB annually.

For media content, if we assume it to be 100 times the size of tweets, it results in 10TB daily, or 4PB annually.

This estimation underscores the need for a distributed storage architecture.

*   **Tweets**: 500 million tweets daily, each with 140 characters (300 bytes each). This totals 140GB per day, and 50TB per year.
*   **Media (Images/Videos)**: Assume 100 times the size of tweets, 10TB per day, and 4PB per year.

## API Design

Now, let’s talk about the API Design which is is another important area in System design interviews:

## Tweeting

APIs for tweeting need to handle the creation and posting of tweets efficiently. This involves capturing user information, tweet content, location data, and timestamp. Proper error handling and validation are essential to ensure a smooth user experience.

public Result postTweet(Long userId, String tweetText, String location, DateTime date);

## Following

The following functionality requires APIs to manage relationships between users. This includes following and unfollowing users, ensuring data integrity, and updating the user’s following list promptly.

public Result followUser(Long userId, Long followedUserId);  
public Result unfollowUser(Long userId, Long followedUserId);

## Favorites

APIs for favorites allow users to like or unlike tweets. These operations should be efficient, with proper indexing and error handling to ensure quick updates and accurate count of favorites on each tweet.

public Result favoriteTweet(Long userId, Long tweetId);  
public Result unfavoriteTweet(Long userId, Long tweetId);

The feed rendering API is crucial for fetching and displaying tweets from followed users. This requires efficient querying and pagination to ensure quick load times and a seamless user experience.

public Result getFeeds(Long userId, String location, int pageNo);

## Database Design

After API Design, let’s talk about Database design

## Tables

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

## Storage

Choosing the right storage solutions is critical. For structured data like user profiles and tweets, MySQL is a good choice due to its support for complex queries and transactions.

For media storage, Amazon S3 offers scalable and cost-effective storage for images and videos.

*   Use MySQL for structured data (users, tweets, follow relationships).
*   Use Amazon S3 for media storage (images and videos).

## High-Level Design

Let’s see the high level design first:

## Client Layer

The client layer involves websites and apps sending requests to the server. These requests are distributed via load balancers to ensure even load distribution and high availability. Using a CDN for static files helps reduce latency and improve load times.

*   Clients (websites/apps) send requests to the server.
*   Requests are distributed via load balancers.
*   Use a rate limiter to protect backend servers.
*   Use a CDN for static files (images, videos).

## Server Layer

The client layer involves websites and apps sending requests to the server. These requests are distributed via load balancers to ensure even load distribution and high availability.

Using a CDN for static files helps reduce latency and improve load times.

*   Server clusters handle requests and different services:
*   **Tweet Service**: Posting tweets.
*   **User Service**: User registration and profile management.
*   **Follow Service**: Following/unfollowing users.
*   **Home Feed Service**: Rendering user feeds.

## Data Layer

The data layer involves caching data with Redis to increase response speed and using MySQL for persistent storage with master-slave architecture to ensure consistency and availability. Amazon S3 is used for storing media files, ensuring scalability and durability.

*   Use Redis for caching to increase response speed.
*   Use MySQL with master-slave architecture for data consistency and availability.
*   Use Amazon S3 for storing media files.

## Request Flow

Explaining the request flow helps in understanding how different components interact. When a client sends a request, it first hits the load balancer, which distributes it to an appropriate server.

The server processes the request, updates the database, and caches the necessary data. For read requests, data is retrieved from the cache or database, and media files are fetched from the CDN, ensuring quick response times.

1.  Client sends a request to the load balancer.
2.  Load balancer distributes the request to a server.
3.  Rate limiter checks the traffic.
4.  Server processes the request and stores data in MySQL and Redis.
5.  Media files are stored in CDN.
6.  For read requests, the server retrieves files from CDN and data from Redis or MySQL.

## Detailed Component Design

Now, let’s see the detailed component design and various software architecture components we can use to design twitter.

## Load Balancer

Deploying multiple load balancers in a cluster ensures high availability and even load distribution.

Placing load balancers in different locations reduces latency for users, and using various algorithms like round-robin or least connections helps manage the load efficiently.

*   Deploy multiple load balancers in a cluster.
*   Place load balancers in different locations to reduce latency.
*   Use algorithms like round-robin, least connections, or IP hash.

## CDN

Using a CDN for static content reduces the load on the origin server and improves load times for users. Optimizing caching rules and adjusting TTL helps achieve higher cache hit ratios, ensuring content is served quickly.

*   Use both pull and push caching approaches.
*   Optimize caching rules and TTL to achieve higher cache hit ratios.
*   Scale the system by adding more server nodes.

## Redis

Using Redis for caching involves setting up a Redis cluster for scalability and employing master-slave replication for high availability. Sentinel monitors the cluster and handles failovers, ensuring the cache remains available even during node failures.

*   Use Redis cluster for large-scale data.
*   Employ master-slave replication for high availability.
*   Use Sentinel to monitor the cluster and handle failovers.

## MySQL

MySQL’s master-slave architecture supports high volume traffic and ensures data consistency through replication. Horizontal partitioning helps distribute the load across multiple servers, handling large datasets efficiently.

*   Use master-slave architecture for high volume traffic.
*   Use horizontal partitioning to handle more data.

## Trade-offs and Tech Choices

This is probably the most important part for interviews, let’s see:

## Database

Choosing MySQL over NoSQL is due to the need for complex queries and transaction support. While NoSQL offers schema flexibility, it lacks support for structured data and complex transactions, which are essential for Twitter’s business model.

*   Chose MySQL over NoSQL due to the need for complex queries and transaction support.

## Cache

Redis is preferred over Memcached due to its support for various data types and horizontal scaling. While Memcached is efficient for basic key-value storage, Redis offers advanced features and better scalability, making it suitable for large-scale systems.

*   Chose Redis over Memcached for its advanced features and horizontal scaling.

## Failure Scenarios and Bottlenecks

## Hybrid Model

To handle users who follow many accounts, a hybrid model combining pull and push approaches can reduce latency. For users following many people, pushing new tweets reduces the load during feed aggregation, improving user experience.

*   If a user follows many people, combine pull and push models to reduce latency.

## Read Hotspot

Handling read hotspots, such as popular users with many followers, involves caching their tweets in Redis and using a cache-aside strategy for consistency. Adding hot zones in Redis servers and using local caches can distribute the load, avoiding excessive calls to the same server.

*   Cache hot data in Redis with a cache-aside strategy.
*   Use local cache to handle high traffic.

## Future Improvements

Future improvements include implementing a multi-region active-active strategy for disaster recovery and high availability.

Deploying service clusters and database clusters in multiple locations with automatic failover and load balancing ensures no single point of failure, maintaining service continuity and reliability.

*   Implement a multi-region active-active strategy for disaster recovery and high availability.
*   Continue optimizing caching, load balancing, and data storage strategies to handle future growth.

## Best System Design Interviews Resources (2025)

And, here are curated list of _best system design books, online courses, and practice websites_ which you can check to better prepare for System design interviews. Most of these courses also answer questions I have shared here.

1.  [**DesignGuru’s Grokking System Design Course**](https://bit.ly/3pMiO8g): An interactive learning platform with hands-on exercises and real-world scenarios to strengthen your system design skills.
2.  [**Codemia.io**](https://codemia.io/?via=javarevisited) : This is another great platform to practice System design problems for interviews. It got more than 120+ System design problems, many of them are free and also a proper structure to solve them.
3.  [**ByteByteGo**](https://bit.ly/3P3eqMN): A live book and course by Alex Xu for System design interview preparation. It contains all the content of System Design Interview book volume 1 and 2 and will be updated with volume 3 which is coming soon.
4.  [**Exponent**](https://bit.ly/3cNF0vw): A specialized site for interview prep especially for FAANG companies like Amazon and Google, They also have a great system design course and many other material which can help you crack FAAN interviews.
5.  [**“System Design Interview” by Alex Xu**](https://amzn.to/3nU2Mbp): This book provides an in-depth exploration of system design concepts, strategies, and interview preparation tips.
6.  [**“Designing Data-Intensive Applications”**](https://amzn.to/3nXKaas) by Martin Kleppmann: A comprehensive guide that covers the principles and practices for designing scalable and reliable systems.
7.  [LeetCode System Design Tag](https://leetcode.com/explore/learn/card/system-design): LeetCode is a popular platform for technical interview preparation. The System Design tag on LeetCode includes a variety of questions to practice.
8.  [**“System Design Primer”**](https://bit.ly/3bSaBfC) on GitHub: A curated list of resources, including articles, books, and videos, to help you prepare for system design interviews.
9.  [**Educative’s System Design Cours**](https://bit.ly/3Mnh6UR)e: An interactive learning platform with hands-on exercises and real-world scenarios to strengthen your system design skills.
10.  **High Scalability Blog**: A blog that features articles and case studies on the architecture of high-traffic websites and scalable systems.
11.  [**YouTube Channels**](https://medium.com/javarevisited/top-8-youtube-channels-for-system-design-interview-preparation-970d103ea18d): Check out channels like “Gaurav Sen” and “Tech Dummies” for insightful videos on system design concepts and interview preparation.

[](https://bit.ly/3P3eqMN)

_image\_credit —_ [_ByteByteGo_](https://bit.ly/3P3eqMN)

Remember to combine theoretical knowledge with practical application by working on real-world projects and participating in mock interviews. Continuous practice and learning will give you confidence for system design interviews.

That’s all abou**t how to design a messaging app like Twitter or X.com** on system design interview. By following this structure, you can design a robust and scalable system similar to Twitter.

This guide will help you present your design effectively in a system design interview.

All the best for your System design interview

Other **System Design Articles and Resources** you may like

*   [Is DesignGuru’s System Design Course worth it](https://medium.com/javarevisited/is-designgurus-ios-grokking-system-design-and-coding-interview-courses-worth-it-review-1ed486913fa7)
*   [16 best Resources to Prepare for System Design Interview](https://medium.com/javarevisited/11-best-resources-to-crack-the-system-design-interview-2cbc77f6fc76)
*   [100+ System Design Interview Questions and Problems](https://javarevisited.blogspot.com/2024/05/100-system-design-interview-questions.html)
*   [Is Exponent’s System Design Course worth it?](https://medium.com/javarevisited/is-exponents-system-design-interview-course-worth-it-review-aad2034d3dd7)
*   [16 Best System Design Interview Resources for Developers](https://medium.com/javarevisited/11-best-resources-to-crack-the-system-design-interview-2cbc77f6fc76)
*   [Is System Design Interview RoadMap by DesignGuru worth it?](https://medium.com/javarevisited/is-system-design-interview-roadmap-on-designguru-io-worth-it-review-55dc74f0d270)
*   [Top 5 Places to learn System design and Software design](https://javarevisited.blogspot.com/2022/08/top-7-websites-to-learn-system-design.html)
*   [10 Reasons to Learn System Design in 2025](https://medium.com/javarevisited/10-reasons-to-learn-system-design-in-2024-fa795d301f62)
*   [6 Best System Design and API Design Interactive Courses](https://medium.com/javarevisited/top-6-system-design-and-api-design-interview-courses-from-educative-io-e9c149039410)
*   [Top 5 System Design YouTube Channels for Engineers](https://medium.com/javarevisited/top-8-youtube-channels-for-system-design-interview-preparation-970d103ea18d)
*   [10 Best Places to Learn System Design in 2025](https://medium.com/javarevisited/7-best-places-to-learn-system-design-79e2d261f343)
*   [How to Prepare for System Design Interview in 2025](https://javarevisited.blogspot.com/2022/03/how-to-prepare-for-system-design.html)
*   [Is ByteByteGo really worth the hype?](https://javarevisited.blogspot.com/2022/12/is-bytebytego-by-alex-xu-worth-it-for.html)
*   [10 Software Design Courses for Developers](https://medium.com/javarevisited/10-best-system-design-courses-for-coding-interviews-949fd029ce65)
*   [5 Best System Design Newsletters for Interviews](https://medium.com/javarevisited/5-best-system-design-publications-and-newsletters-for-software-engineers-in-2024-54b8c8c5f65c)
*   [My Favorite Software Design Courses for 2025](https://javinpaul.medium.com/7-best-software-design-course-for-programmers-and-developers-da3e18e9135)
*   [3 Places to Practice System Design Mock interviews](https://medium.com/javarevisited/3-best-mock-interview-platforms-for-system-design-and-coding-interviews-in-2024-7283f1579b17)
*   [Is Designing Data intensive application book worth reading?](https://medium.com/javarevisited/review-is-designing-data-intensive-applications-by-martin-kleppman-worth-it-b3b7dfa17a5c)

Thanks for reading this article so far. If you like this Twitter system design interview solution then please share with your friends and colleagues. If you have any questions feel free to ask in comments.

**P. S. —** By the way, [DesignGuru.io](https://designgurus.org/link/84Y9hP) also have many other Grokking courses to prepare for essential coding interview topics like OOP Design, System Design, Dynamic Programming etc and you can get access to all of their courses for a big discount by joining their [**All course bundle**](https://designgurus.org/link/84Y9hP?url=https%3A%2F%2Fdesigngurus.org%2Fbundles%3Fbundle_id%3Dall-courses). You can also **use code GURU to get 30% discount**.
