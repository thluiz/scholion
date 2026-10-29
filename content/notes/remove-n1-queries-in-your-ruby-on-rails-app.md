---
title: "Remove N+1 queries in your Ruby on Rails app"
date: '2015-11-03T12:04:18-03:00'
category: webclip
summary: 'Explains the N+1 query problem in Rails and shows how eager loading, grouping, SQL joins, and the Bullet gem reduce repeated database calls in common cases.'
tags: ["ruby-on-rails", "n1-queries", "activerecord", "bullet-gem"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Remove N+1 queries in your Ruby on Rails app"
    url: "http://blog.diatomenterprises.com/remove-n1-queries-in-your-ruby-on-rails-app/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-11/blog-diatomenterprises-com--remove-n1-queries-in-your-ruby-on-rails-app.md"
    kind: repo
---

The post explains the N+1 query problem as repeated database calls made while iterating over records and fetching the same associated data again and again. It shows how this slows pages down and uses a Rails example to illustrate the issue.

## Reading notes

- N+1 happens when a page loads a collection and then asks the database for the associated record for each item.
- `preload` loads the main records and the associated records in two separate queries, but it does not support conditions on the associated table.
- `includes` can choose between separate queries and a join, and it can be combined with `references` to force a `LEFT OUTER JOIN`.
- `eager_load` works like `includes` with `references` and loads the data with one `LEFT OUTER JOIN` query.
- Repeated aggregate calls with changing conditions can be replaced by grouping once and reading values from a hash.
- Some multiple counts or sums can be merged into one SQL query with `select` and aliased expressions.
- The Bullet gem helps detect N+1 queries during development by showing browser notifications when eager loading is needed or unnecessary.
