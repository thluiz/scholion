---
title: "CAP Theorem for Databases: Consistency, Availability & Partition Tolerance"
date: '2022-04-10T15:33:15-03:00'
category: webclip
summary: 'The page explains CAP as a tradeoff in distributed databases: under network failure, a system can prioritize consistency or availability, while partition tolerance is required. It also links the choice to database types and use cases.'
tags: ["cap-theorem", "distributed-databases", "consistency", "availability"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "CAP Theorem for Databases: Consistency, Availability & Partition Tolerance – BMC Software | Blogs"
    url: "https://www.bmc.com/blogs/cap-theorem/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-04/bmc-com--cap-theorem-for-databases-consistency-availability-partition.md"
    kind: repo
---

The page explains that the CAP theorem applies to distributed data stores and says that, when a network failure happens, a system can provide either consistency or availability, but not both. It defines the three parts of CAP and says partition tolerance is required because distributed systems operate with network partitions.

## Reading notes

- Consistency means reads return the most recent write or an error.
- Availability means reads return data, even if it is not the latest.
- Partition tolerance means the system keeps operating despite network failures.
- In a network failure, higher consistency reduces availability, and higher availability reduces consistency.
- CAP consistency is about up-to-date information, which is different from ACID consistency.
- For a user query, the system can return the current server value for availability or wait for the new write, or return an error, for consistency.
- Brewer is quoted saying the goal should be to maximize the mix of consistency and availability that fits the application.
- NoSQL databases are described as schema-free, without table relations, and associated with ease of use, scalable performance, strong resilience, and wide availability.
- Consistent databases are presented as a fit for accurate information, such as bank account balances and text messages.
- Available databases are presented as a fit for services where keeping the system up matters more than returning the latest information, such as e-commerce shopping carts.
- Some databases, including Cosmos DB and Cassandra, let users choose between consistency and availability.
