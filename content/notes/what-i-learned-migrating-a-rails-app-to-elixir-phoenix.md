---
title: "What I learned migrating a Rails app to Elixir/Phoenix"
date: '2016-02-07T20:33:02-03:00'
category: webclip
summary: 'The migration favors small functions, explicit composition, and Phoenix idioms over Rails patterns. It also shows where the ecosystem is thinner and where custom integrations or rewrites are needed.'
tags: ["elixir", "phoenix", "rails-migration", "ecto"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "What I learned migrating a Rails app to Elixir/Phoenix — Medium"
    url: "https://medium.com/@stueccles/what-i-learned-migrating-a-rails-app-to-elixir-phoenix-f707436749aa"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-02/medium-com--what-i-learned-migrating-a-rails-app-to-elixir-phoenix.md"
    kind: repo
---

The migration emphasizes a shift away from Rails habits and toward Elixir and Phoenix patterns. The author says the process felt easier to understand because there is less magic, even though some integrations and code had to be written by hand.

## Reading notes

- The main mental change is to drop the object-oriented mindset around models and work with small functions composed together.
- The Elixir ecosystem does not yet cover every integration, so some libraries may need to be built manually.
- Some patterns from Rails should be changed completely, such as using `Task.async` or OTP instead of background job queues for concurrency.
- The front-end pipeline was moved from the Rails setup to Brunch, with `sass-brunch`, `bourbon`, `normalize.css`, and `css-patterns` added through `package.json` and `brunch.config`.
- Asset paths had to be rewritten because Phoenix does not provide Rails-style `asset_path` or `asset_url` helpers.
- The schema migration from ActiveRecord to Ecto was mostly straightforward, but `has_and_belongs_to_many` and HSTORE required changes.
- HSTORE data was moved to `jsonb`, and JSON extension support had to be configured for the environment.
- In Ecto, queries are composed in modules instead of using scopes.
- Associations are not lazy-loaded, so `Repo.preload` is needed when data must be available.
- Changesets replace model callbacks for setting derived values during updates and creates.
- Controllers can be organized as pipelines of functions, and plugs can be used for pre-action checks.
- Phoenix templates differ from Rails views, and helper-like logic moves into View modules.
- Business logic was moved into Elixir modules, where each step returns the updated order state before the next step runs.
- The author ends by saying the migration felt smooth and that the app became much faster, with response times under 100ms.
