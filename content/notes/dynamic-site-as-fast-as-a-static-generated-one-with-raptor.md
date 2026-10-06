---
title: "Dynamic Site as fast as a Static Generated One with Raptor"
date: '2015-05-20T13:06:52-03:00'
category: webclip
summary: 'The page shows how a Rails app can serve public pages with static-like speed by combining ETags, caching, Memcached, and Passenger 5, with load tests showing stable response times.'
tags: ["rails", "http-caching", "passenger", "memcached"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Dynamic Site as fast as a Static Generated One with Raptor"
    url: "http://www.akitaonrails.com/2015/05/20/dynamic-site-as-fast-as-a-static-generated-one-with-raptor#.VVywmZdViko"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-05/akitaonrails-com--dynamic-site-as-fast-as-a-static-generated-one-with-raptor.md"
    kind: repo
---

The page argues that a Rails app can serve public content with performance close to a static site when ETags, cache headers, Memcached, and Passenger 5 are used together. In the load test described, responses stay stable as concurrent users increase, and the setup avoids repeated rendering for unchanged pages.

It also explains that the controller caches recent page data, builds ETags from updated content plus a deploy identifier, and relies on Passenger’s internal cache when content is marked public. For authenticated areas, the page says other techniques such as fragment caching are still needed.

## Reading notes

- Blitz.io tests on a small Heroku setup show about 12 ms for a static 404 page and about 20 ms for Rails-generated content served through Passenger 5, with no timeouts or errors.
- The main mechanism is proper ETag generation with `stale?` and `fresh_when`, so unchanged content returns HTTP 304 instead of rebuilding the page.
- The index action caches the 10 most recent items and builds the ETag from the most recently updated item.
- The show action caches a single resource for a limited time, with the expiration chosen according to how often the content changes.
- Memcached is used so the app does not hit the database on every request, even though the external cache adds network overhead.
- A `deploy_id` is added to the ETag so a new deployment can invalidate cached pages when stylesheets, layout, or HTML structure change.
- Passenger needs `Cache-Control: public` to cache pages internally, and the page warns that this approach should be used only for publicly visible content.
- For logged-in areas, the page points to fragment caching and related techniques instead of full-page caching.
- The page recommends ActiveAdmin, Bourbon with Neat and Bitters, FriendlyId, Redcarpet, and Rouge for the rest of the stack.
