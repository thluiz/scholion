---
title: "Many to Many Relations in Ecto"
date: '2020-07-05T14:11:24+00:00'
category: webclip
summary: 'The post shows how to model a many-to-many relation in Phoenix/Ecto with a join table, schema associations, a like action, and a query that marks whether each comment is liked by the current user.'
tags: ["ecto", "phoenix", "many-to-many", "elixir"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Many to Many Relations in Ecto"
    url: "https://dev.to/ceyhunkerti/many-to-many-relations-in-ecto-33n4"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--many-to-many-relations-in-ecto.md"
    kind: repo
---

The post walks through a many-to-many setup for comment likes in a Phoenix/Ecto blog app. It uses a `comment_likes` join table, adds `many_to_many` associations on `User` and `Comment`, and defines a schema for the join relation itself.

It also shows two practical pieces: a controller action that likes a comment through the current user’s `liked_comments` association, and a query that returns comments with an `is_liked` field for the current user. The author also recommends using `iex -S mix` for testing and debugging Ecto models.

## Reading notes

- The example starts from a blog app with users, posts, comments, and comment likes.
- The migrations create `users`, `posts`, `comments`, and `comment_likes` tables.
- `comment_likes` uses `comment_id` and `user_id` as primary keys and also has a unique index on that pair.
- `User` defines `many_to_many :liked_comments, Comment, join_through: CommentLike, on_replace: :delete`.
- `Comment` defines `many_to_many :liked_by, User, join_through: CommentLike, on_replace: :delete`.
- `Post` belongs to a user and has many comments.
- The join schema `CommentLike` is defined with `@primary_key false` and `belongs_to` fields for `user` and `comment`.
- The like action preloads `liked_comments`, changes the user struct, and uses `put_assoc` with the target comment.
- The comment list query joins posts, comments, comment likes, and users to produce `comment` plus `is_liked`.
- The post suggests `iex -S mix` for learning and debugging Ecto models.
