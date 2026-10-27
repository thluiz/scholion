---
title: "Everyone should be using low level caching in Rails"
date: '2012-05-16T20:55:25-03:00'
category: webclip
summary: 'The post argues that low level caching in Rails is easy to start using and helps reduce database queries and API calls. It shows Rails.cache.fetch, cache key invalidation, and layered caching in practice.'
tags: ["rails", "caching", "active-record", "api-calls"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Everyone should be using low level caching in Rails | robotmay"
    url: "http://robotmay.com/post/23161612605/everyone-should-be-using-low-level-caching"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-05/robotmay-com--everyone-should-be-using-low-level-caching-in-rails.md"
    kind: repo
---

The post argues that low level caching in Rails is easy to adopt and useful for reducing database queries and API calls. It gives examples from application-wide category data and Flickr lookups, and explains that cache keys should be designed so updates invalidate stale data.

## Reading notes

- Low level caching is easy to start with in Rails 3, although it is missing from the official guides.
- The author uses it to reduce the number of queries and API calls.
- A global list of categories is cached in ApplicationController with Rails.cache.fetch and expires_in: 10.minutes.
- When using this pattern, the query should be forced with .all so the results are stored in the cache, not only the ActiveRecord relation.
- Rails.cache.fetch is presented as the main method for low level caching in Rails.
- In development, caching is enabled by default, so config.cache_store = :null_store is suggested to avoid confusion.
- fetch takes a cache key, an options hash, and a block.
- If a valid cache entry exists, fetch returns it; otherwise it stores the block result under the key.
- The author says low level caching is used most for API calls.
- In the Flickr example, a place is looked up by latitude and longitude through FlickRaw.
- The result is cached for 7 days because the place is unlikely to change often.
- Using self.updated_at in the cache key makes the cache invalidate automatically when the record changes.
- Caching works best in layers, so different kinds of cache should be combined rather than used alone.
- The article assumes a cache store such as memcached or Redis and recommends the Dalli gem with memcached.
