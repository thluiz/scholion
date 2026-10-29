---
title: "Creating a Todo Application using the Phoenix Framework and Ember.js"
date: '2015-10-16T09:10:31-03:00'
category: webclip
summary: 'The tutorial shows how to build a todo app with Phoenix and Elixir on the server, PostgreSQL for storage, and Ember on the client, then connect both apps through REST, CORS, and JSON key changes.'
tags: ["phoenix", "ember-js", "postgresql", "todo-app"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Creating a Todo Application using the Phoenix Framework and Ember.js - Resolve Digital"
    url: "http://resolve.digital/blog/posts/creating-a-todo-application-using-the-phoenix-framework-and-ember-js"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-10/resolve-digital--creating-a-todo-application-with-phoenix-and-ember-js.md"
    kind: repo
---

The page walks through building a simple client-server todo app with Phoenix and Elixir on the server, PostgreSQL as the data store, and Ember on the client. It also shows how to connect the two parts so changes made in Ember are saved through the Phoenix API.

## Reading notes

- Phoenix is presented as a web application framework built on Elixir.
- The example app uses Phoenix and Elixir on the server, PostgreSQL for storage, and Ember JavaScript on the client.
- The stack is identified as PEEP, meaning Postgres, Elixir, Ember, Phoenix.
- The Phoenix side starts with creating a new API-only app with `mix phoenix.new` and `--no-brunch`.
- The database is created with `mix ecto.create` after checking PostgreSQL credentials.
- The server is started with `mix phoenix.server` and the app is available on `http://localhost:4000`.
- A Todo JSON resource is generated with fields for `title` and `is_completed`.
- A route is added for `/todos` so requests reach `TodoController`.
- The database is migrated to create the todos table.
- Seed data is inserted so the API returns initial todo items.
- On the client side, the page uses an Ember CLI TodoMVC app.
- The Ember app is cloned, dependencies are installed, and `ember server` runs it on `http://localhost:4200`.
- Ember Data is configured to use `DS.RESTAdapter` with the Phoenix API as the backend.
- A custom serializer is added so Ember can work with snake_case keys from Phoenix.
- Development CSP settings are updated so Ember can connect to localhost ports.
- The Ember app port is set to 9000.
- Phoenix is updated with `cors_plug` and a CORS origin of `http://localhost:9000`.
- The JSON root keys are changed from `data` to `todos` and `todo` so Ember REST deserialization works.
- After both servers are running, the Ember app shows the seeded data and persists changes back to Phoenix.
