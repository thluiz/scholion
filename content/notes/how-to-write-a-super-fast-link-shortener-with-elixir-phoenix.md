---
title: "How to write a super fast link shortener with Elixir, Phoenix, and Mnesia"
date: '2020-07-05T14:11:26+00:00'
category: webclip
summary: 'Tutorial showing how to build a link shortener with Phoenix, custom hash ids, and Mnesia instead of Postgres, so links can be saved and redirected quickly.'
tags: ["elixir", "phoenix", "mnesia", "link-shortener"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to write a super fast link shortener with Elixir, Phoenix, and Mnesia"
    url: "https://freecodecamp.org/news/how-to-write-a-super-fast-link-shortener-with-elixir-phoenix-and-mnesia-70ffa1564b3c"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/freecodecamp-org--how-to-write-a-super-fast-link-shortener-with-elixir-phoenix.md"
    kind: repo
---

The tutorial walks through building a link shortener with Elixir, Phoenix, and the Erlang VM. It starts from a new Phoenix project without a frontend, then adds a links context, model, controller, and migration, and later switches storage from Postgres to Mnesia for faster lookups.

## Reading notes

- The project is set up with `mix phx.new shorten_api --no-html --no-brunch`.
- `mix phx.gen.json Links Link links hash:string:unique url:string:unique` creates the context, model, controller, and migration for links.
- A custom Ecto type is created so the link id can be a short, unique, auto-generated string.
- The link schema is updated to use `HashId` as the primary key instead of an integer.
- The database migration is adjusted to match the model changes.
- A controller function looks up a link by id and redirects to the stored URL.
- The router is updated to connect that controller action.
- The article says the main delay in link shorteners comes from database lookups.
- It switches configuration from Postgres to Mnesia, using Mnesia as an in-memory datastore.
- The Mnesia database is created with `mkdir priv/data/mnesia`, `mix ecto.create`, and `mix ecto.migrate`.
- After that, the app can create shortened links with `curl` and redirect from `localhost:4000/{hash}` to the original URL.
