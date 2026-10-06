---
url: "http://blog.rokkincat.com/postgres-full-text-search-in-ecto/"
captured_at: "2015-06-07T11:50:26-03:00"
title: "Postgres Full Text Search in Ecto"
domain: "blog-rokkincat-com"
---

# Postgres Full Text Search in Ecto

Text search is often a core feature of web APIs, and Postgres and Ecto can fill the need without having to add additional technology (such as ElasticSearch or Solr) to the stack. We can lean on Postgres' [pg\_trgm](http://www.postgresql.org/docs/9.4/static/pgtrgm.html) to provide "good enough" search in early stages of API development.

My example will be on a User model, where we will be searching by username, so we'll set up a simple Ecto Model first:

|  |  |
| --- | --- |
|  | ```  defmodule  .Model  schema users  field :username, :string ``` |

To make sure the search remains fast as the table grows, we're going to index the field using Postgres' pg\_trgm:

|  |  |
| --- | --- |
|  | ```  defmodule Repo.Migrations.UserSearch  .Migration  execute CREATE extension if not exists pg_trgm;  execute CREATE INDEX users_username_trgm_index ON users USING gin (username gin_trgm_ops);  execute DROP INDEX users_username_trgm_index; ``` |

Inspired by Drew Olson's [post](http://blog.drewolson.org/composable-queries-ecto/), we'll give the Ecto Model a function so we can easily compose search queries. Ecto doesn't have any shorthand for a trigram query over a text column, but using Ecto fragments is straightforward enough:

|  |  |
| --- | --- |
|  | ```  defmodule  .Model  schema users  field :username, :string  search(query, search_term)  from(u  query,  where: fragment(, u.username, ^search_term),  order_by: fragment(similarity(?, ?) DESC, u.username, ^search_term)) ``` |

This query will compare the search term, and order by similarity. Let's see it in action:

|  |  |
| --- | --- |
|  | ```  .search(mitch)  .all  # [debug] SELECT u0."id", u0."username" FROM "users" AS u0 WHERE (u0."name" % $1) ORDER BY similarity(u0."name", $2) DESC ["mitch", "mitch"] (1.9ms)  [%{__meta__: %.Schema.Metadata{source: users, state: :loaded},  username: mitch},  %{__meta__: %.Schema.Metadata{source: users, state: :loaded},  username: mitch3}] ``` |

We've been building more APIs in Elixir and [Phoenix](http://www.phoenixframework.org/), and there have been questions on the Ecto mailing list about doing full text search in Ecto, so I thought I'd write up how we've done it. Hopefully it was helpful :)

Feel free to contact me on Twitter at [@mitchellhenke](https://twitter.com/mitchellhenke) or IRC in #elixir-lang with the same name.

##### ADDENDUM:

Someone on [Reddit](https://www.reddit.com/r/elixir/comments/35u5h5/postgres_full_text_search_in_ecto/cr8t7l1) asked how to change the limit of the `%` operator in Postgres, which I've usually done via the `set_limit()` function on each connection, since it resets to the default on new connections.

Ecto doesn't have an after connect hook (created an issue [here](https://github.com/elixir-lang/ecto/issues/599)), and the user needed to be able to set the limit per query. A solution to this is to use the `similarity` function for both the filter and the order:

|  |  |
| --- | --- |
|  | ```  defmodule  .Model  schema users  field :username, :string  search(query, search_term, limit  )  from(u  query,  where: fragment(similarity(?, ?) > ?, u.username, ^search_term, ^limit),  order_by: fragment(similarity(?, ?) DESC, u.username, ^search_term)) ``` |
