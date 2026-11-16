---
title: "How to use Postgres NOTIFY PubSub with Elixir/Phoenix"
date: '2020-07-05T14:11:26+00:00'
category: webclip
summary: 'The post shows how to use Postgres NOTIFY in a Phoenix app to react to table changes, wiring a custom module and a GenServer worker through the phoenix_postgres_pub_sub package.'
tags: ["postgres", "elixir", "phoenix", "pubsub"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to use Postgres NOTIFY PubSub with Elixir/Phoenix | by Lorenzo Sinisi | elixir-bytes | Medium"
    url: "https://medium.com/elixir-bytes/in-this-post-i-would-like-to-illustrate-how-to-take-advantage-of-the-notify-feature-of-postgres-in-f5a919316f0b"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/medium-com--how-to-use-postgres-notify-pubsub-with-elixir-phoenix.md"
    kind: repo
---

The post explains how to use Postgres NOTIFY in a Phoenix application so the app can react when a database row changes. It gives examples like sending a welcome email for new members or keeping two systems in sync.

## Reading notes

- NOTIFY sends a notification event with an optional payload to clients that previously used LISTEN on the same channel.
- The feature is presented as a simple interprocess communication mechanism for processes using the same PostgreSQL database.
- A payload string can travel with the notification, and more structured data can be built with tables that pass extra data from notifier to listeners.
- The author says the application can call a function every time a row changes on a specific table.
- The example uses the phoenix_postgres_pub_sub package and an example Phoenix application.
- The setup starts with creating a new Phoenix app and generating a User schema under the Accounts context.
- The instructions include running the database setup and adding the dependency to mix.exs.
- The config file is updated with adapter and repo settings for phoenix_postgres_pub_sub.
- A module is created to receive notifications and print each one with IO.inspect.
- A migration generates the Postgres function and trigger used to dispatch notifications for the users table.
- The worker is added to the application supervision tree with a string that combines the table name and changes.
- The post says the same pattern can monitor other tables by passing other table_changes strings.
- The author links to a demo project on GitHub and invites comments with questions.
