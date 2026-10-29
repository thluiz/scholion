---
title: "Remove N+1 queries in your Ruby on Rails app"
date: '2015-11-04T09:16:15-03:00'
category: webclip
summary: 'The post explains the N+1 query problem in Rails, shows how eager loading methods reduce repeated database calls, and gives a few other ways to merge queries and spot them in development.'
tags: ["ruby-on-rails", "n-plus-one", "database-queries", "eager-loading"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Remove N+1 queries in your Ruby on Rails app"
    url: "http://blog.diatomenterprises.com/remove-n1-queries-in-your-ruby-on-rails-app/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-11/blog-diatomenterprises-com--remove-n-plus-one-queries-in-your-ruby-on-rails-app.md"
    kind: repo
---

The post says N+1 queries slow pages because the app keeps asking the database for associated records inside a loop. It then shows the usual Rails tools for avoiding that pattern, plus a few ways to collapse repeated counts into fewer queries.

## Reading notes

- N+1 happens when an app makes extra database calls to fetch the same associated data over and over.
- In the example, iterating through items and calling each item’s category causes one query for the items and more queries for categories.
- preload loads the main records and the associated records in separate queries, and it does not work with a where clause on the associated table.
- includes can choose between separate queries and a join, depending on the query shape.
- references can force includes to use a LEFT OUTER JOIN.
- eager_load behaves like includes plus references and uses one query with a LEFT OUTER JOIN.
- Repeated count queries with a dynamic date condition can be replaced with one grouped query and a hash lookup.
- Some sets of counts can be combined into one SQL query with selected aliases.
- The bullet gem helps find N+1 queries during development by showing browser notifications.
