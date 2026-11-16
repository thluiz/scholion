---
title: "How to achieve a 50% reduction in Redis memory usage"
date: '2020-07-05T14:11:19+00:00'
category: webclip
summary: 'The post shows a Spring Boot Redis setup that stores User data as JSON, then cuts memory further by switching to MessagePack and Snappy, reducing dataset usage from 2GB to under 500MB.'
tags: ["redis", "spring-boot", "messagepack", "snappy"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to achieve a 50% reduction in Redis memory usage"
    url: "https://dev.to/darshitpp/how-to-achieve-a-50-reduction-in-redis-memory-usage-482b"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--how-to-achieve-50-reduction-in-redis-memory-usage.md"
    kind: repo
---

The article explains a Redis storage setup in Spring Boot and tracks how the author reduced memory use by more than 50%. It starts with a basic RedisTemplate-based service that stores User data as hashes, then measures the space used in Redis before and after serialization changes.

## Reading notes

- The app uses Spring Boot Web and Spring Data Reactive Redis with a LettuceConnectionFactory pointed at Redis on localhost:6379.
- The stored domain model is User with firstName, lastName, and birthday.
- The data is stored in a Redis hash with firstName as the key and lastName as the hash key.
- A NormalController and NormalService expose CRUD-style endpoints for insert, get, and delete.
- A custom RedisSerializer with Jackson stores User objects as JSON in Redis.
- After inserting 100 users, memory stats show keys.bytes-per-key at 1044 and dataset.bytes at 32840.
- Switching to MessagePack through a MsgPackRedisSerializer lowers dataset.bytes to 15976.
- Adding Snappy compression reduces dataset.bytes further to 15720.
- The author says the full cleanup and restructuring brought Redis memory use from 2GB to under 500MB.
