---
title: "Postgres Full Text Search in Ecto"
date: '2015-06-07T11:50:26-03:00'
category: webclip
summary: 'The post shows how to add username search in an Ecto model with Postgres pg_trgm, including a GIN index, a composable query function, and a note on using similarity when the % operator limit must be set per query.'
tags: ["postgres", "ecto", "pg-trgm", "full-text-search"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Postgres Full Text Search in Ecto"
    url: "http://blog.rokkincat.com/postgres-full-text-search-in-ecto/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-06/blog-rokkincat-com--postgres-full-text-search-in-ecto.md"
    kind: repo
---

The post explains that Postgres and Ecto can cover search needs in early API development without adding ElasticSearch or Solr. It uses a User model with username search, adds a pg_trgm index for speed, and builds an Ecto function with fragments to filter and order by similarity.

It also notes that the % operator threshold can be hard to change per connection in Ecto, so the addendum switches to similarity in both the where clause and the ordering.

## Reading notes

- Use Postgres and Ecto for search when you want to avoid adding ElasticSearch or Solr to the stack.
- The example searches users by username in a simple Ecto model.
- Add the pg_trgm extension and a GIN index on username with gin_trgm_ops so the search stays fast as the table grows.
- Compose the search as an Ecto function using fragments, with a trigram match in the filter and similarity in the order_by.
- If the % operator limit needs to vary per query, use similarity in both the filter and the ordering instead of relying on set_limit().
