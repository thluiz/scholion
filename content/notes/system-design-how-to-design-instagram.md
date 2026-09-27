---
title: "System Design: How to Design Instagram"
date: '2024-01-03T16:00:25+00:00'
category: webclip
summary: 'The post outlines Instagram-like requirements, storage tables, and a high-level architecture for uploading, reading, and generating photo feeds with caching, sharding, blobs, and two feed strategies.'
tags: ["system-design", "instagram", "data-storage", "feed-generation"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Dr Milan Milanović (@milan_milanovic) on X"
    url: "https://x.com/milan_milanovic/status/1742576659067191706?s=20"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2024-01/x-com--system-design-how-to-design-instagram.md"
    kind: repo
---

The post frames an Instagram-style system around three main needs: uploading images from mobile clients, following users, and generating an image feed. It also sets scale and reliability goals, including 10 million users, photo uploads of 5 MB each, and a system where uploaded photos are not lost.

## Reading notes

- The data model uses three tables: User, Photo, and UserFollow.
- Upload flow goes from the mobile device to an API gateway, then a load balancer, then a write app server.
- The load balancer distributes traffic across multiple servers to avoid a single point of failure.
- The write server stores photo metadata in a Metadata DB and stores the image in Azure Blob, AWS S3, or a similar service.
- To support millions of users, the metadata database is partitioned with sharding.
- Sharding the metadata DB by UserID keeps a user’s photos in the same shard.
- The text says one user may have almost 3 TB of data, so a 1 TB shard would require three data shards for that user.
- Reading images goes through a read app server that reuses cache such as Redis, reads metadata from the Metadata DB, and returns the client to the image in Blob/S3 or through a CDN.
- Feed generation uses a Feed Generation service that reads from cache or the Metadata DB.
- The pull-based approach has users poll the server at intervals to check whether friends have new updates.
- The push-based approach sends new data to users as soon as it is available, with users keeping a long polling request open.
