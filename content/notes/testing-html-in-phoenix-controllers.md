---
title: "Testing HTML in Phoenix Controllers"
date: '2026-11-16T03:39:52+00:00'
category: webclip
summary: 'The post shows how to test Phoenix HTML responses with ConnTest helpers, then adds ExMachina factories, a Post model, routes, a controller, and a view to make the tests pass.'
tags: ["phoenix", "testing", "ex-machina"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Testing HTML in Phoenix Controllers"
    url: "https://thoughtbot.com/blog/testing-phoenix-controllers-with-ex-machina"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/thoughtbot-com--testing-html-in-phoenix-controllers.md"
    kind: repo
---

The post explains how to test HTML responses in Phoenix controllers with ConnTest helpers, then extends the example by adding ExMachina for test data. It walks through the errors that appear along the way and the code needed to make the tests pass.

## Reading notes

- Phoenix ConnTest helpers can be used to test controller responses, and `html_response/2` both checks for a 200 status and returns the HTML body.
- `create_pair/3` inserts two posts for the list test, while `build_pair/3` would be used if database persistence were not needed.
- Adding ExMachina requires adding the dependency, listing it in the application, and creating a factory module with `use ExMachina.Ecto, repo: MyBlog.Repo`.
- The `:post` factory builds a `MyBlog.Post` struct, uses `sequence/2` for unique titles, and keeps body and author fixed.
- Importing `MyBlog.Factory` in `MyBlog.ConnCase` makes the factory functions available to controller tests.
- The missing `MyBlog.Post` struct is fixed by generating a Post model and migration with `mix phoenix.gen.model` and `mix ecto.migrate`.
- The missing `posts_path/2` helper is fixed by adding a `resources "/posts", PostController, only: [:index]` route and a `PostController` with an `index/2` action.
- The controller fetches posts with `Repo.all(Post)` and renders them with `render(conn, "index.html", posts: posts)`.
- The missing view and template are fixed by adding `PostView` and an `index.html.eex` template that iterates over `@posts` and outputs `post.title`.
- For tagged posts, the factory adds `:tag` and `:post_tag` factories, with `:post_tag` building a post and a tag by default.
- A `tagged_with(post, tag_name)` helper creates a tag, creates a post_tag join record, and returns the post.
- Using a regular function with ExMachina makes the tagged-post setup easier to reuse and easier to change later.
