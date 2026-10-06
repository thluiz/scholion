---
title: "Caching Strategies for Rails"
date: '2012-05-22T20:26:24-03:00'
category: webclip
summary: 'The page lays out when to use page, action, fragment, and low-level caching in Rails on Heroku, and recommends memcached, Varnish, and Rails.cache for different kinds of slow content.'
tags: ["rails", "caching", "memcached", "http-caching"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Caching Strategies for Rails | Heroku Dev Center"
    url: "https://devcenter.heroku.com/articles/caching-strategies#low_level_caching"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-05/devcenter-heroku-com--caching-strategies-for-rails.md"
    kind: repo
---

Heroku says caching should start with the slowest pages and requests, identified with New Relic. It recommends low-level caching for slow database or API work, memcached for action and fragment caching, and Varnish HTTP caching for page-level responses that are the same for all users.

## Reading notes

- Use New Relic to find the longest running requests and database work before choosing a caching approach.
- Avoid automagic caching libraries like cache-money or cache_fu.
- After memcached is configured, Rails can use it for action and fragment caching.
- Built-in page caching does not work on Heroku because it needs file system write access.
- Varnish HTTP Cache can serve the same role for pages without before_filter logic and without customized content.
- Action caching works for pages that need authentication or other before or after filters, and it requires the Heroku Memcache add-on.
- The controller can use caches_action, :layout => false, and expire_action to cache actions while keeping dynamic layout parts.
- Fragment caching fits widgets, partials, and other page sections that do not need fresh datastore reads on every load.
- Rails can generate a cache key automatically when cache receives an ActiveRecord object.
- Low-level caching uses Rails.cache directly for data that is costly to fetch and can be slightly stale.
- Rails.cache.fetch is presented as the most efficient low-level caching method.
- Instance-level caching should use cache keys that reflect model changes, such as id and updated_at, so updates invalidate the cache.
