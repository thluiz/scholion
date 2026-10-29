---
title: "Secrets to Speedy Ruby Apps On Heroku"
date: '2015-07-24T08:45:10-03:00'
category: webclip
summary: 'The article explains how to speed up Ruby and Rails apps on Heroku by managing memory, tuning worker count, reducing N+1 queries, caching more, and using CDN and frontend performance checks.'
tags: ["ruby", "heroku", "rails-performance", "caching"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Secrets to Speedy Ruby Apps On Heroku"
    url: "http://nateberkopec.com/2015/07/22/secrets-to-speedy-ruby-apps-on-heroku.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-07/nateberkopec-com--secrets-to-speedy-ruby-apps-on-heroku.md"
    kind: repo
---

The article argues that Ruby apps on Heroku can still reach fast server response times if memory use, worker count, caching, and query behavior are tuned carefully. It focuses on the limits of small dynos, the cost of swap, and the need to measure real production behavior instead of relying on optimistic defaults.

## Reading notes

- Memory is presented as the main constraint on Heroku, since swap is much slower than RAM and can drag an app down if dynos run out of memory.
- Worker count should be chosen from actual per-process memory use, not from automatic tuning tools that may overestimate capacity.
- The master process and each worker consume RAM, so `WEB_CONCURRENCY` must fit the application’s warmed-up memory footprint.
- Extra gems and required Ruby code increase memory usage, so dependencies should be justified by their cost.
- Worker-killer gems are only for real memory leaks, not for ordinary memory bloat.
- Memory bloat should level off over time, while a leak keeps growing without bound.
- New Relic and Heroku metrics can look too good if asset requests are included in averages.
- Slow frontend JavaScript can make a site feel sluggish even when server metrics look fine.
- N+1 queries are identified by repeated SQL in traces, and ActiveRecord tools like `includes`, `joins`, `eager_load`, and `preload` are part of the fix.
- Caching is presented as necessary once memory and query problems are under control, and the cache should not live on the filesystem on Heroku.
- Development should use production-like data so slow SQL and query explosions are easier to see.
- A CDN reduces the impact of asset requests on the app server.
- Large uploads and other slow clients can lock up some web servers, while Puma and Phusion Passenger 5 are described as better protected options.
