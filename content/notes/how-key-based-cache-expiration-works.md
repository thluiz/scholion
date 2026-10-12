---
title: "How key-based cache expiration works"
date: '2014-06-24T10:13:35-03:00'
category: webclip
summary: 'The post explains key-based cache expiration as a way to avoid manual cache invalidation by making the cache key change with the object’s updated_at timestamp, so old entries become disposable and stale data is avoided.'
tags: ["cache-invalidation", "rails", "memcached", "key-based-cache-expiration"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How key-based cache expiration works by David of Basecamp"
    url: "http://signalvnoise.com/posts/3113-how-key-based-cache-expiration-works"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-06/signalvnoise-com--how-key-based-cache-expiration-works.md"
    kind: repo
---

The post argues that manual cache invalidation is error-prone and that key-based cache expiration is a cleaner approach. In this scheme, the cache key changes together with the object it represents, usually through a timestamp in the key, while the cached content itself stays fixed.

It also says dependency chains should update their timestamps together so related keys change at the same time. Caching then happens in views through nested partials, and old cache entries are left behind because Memcached can evict them when needed.

## Reading notes

- manual cache invalidation is described as frustrating and easy to get wrong
- the cache key changes, while the cache content stays fixed
- the key is tied to the represented object, often with a timestamp such as class/id-timestamp
- when the object changes, new content is written to the new key
- old cache entries become garbage and are not manually cleaned up
- Memcached evicts old keys when space runs out
- dependency chains are handled by updating updated_at across related model objects
- Rails cache calls can nest through partials and use cache_key on array elements
