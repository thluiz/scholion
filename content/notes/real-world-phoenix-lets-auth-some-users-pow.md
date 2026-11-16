---
title: "Real World Phoenix |> Let's auth some users |> Pow!"
date: '2020-07-05T14:11:26+00:00'
category: webclip
summary: 'The post shows how to add Pow to a Phoenix app for user registration and session-based authentication, from dependency setup and config to routes and a protected pipeline.'
tags: ["phoenix", "elixir", "authentication", "pow"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Real World Phoenix |> Let's auth some users |> Pow!"
    url: "https://web.archive.org/web/20190721084510id_/https://www.theguild.nl/real-world-phoenix-lets-auth-some-users/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--real-world-phoenix-lets-auth-some-users-pow.md"
    kind: repo
---

The post introduces Pow as a way to add user authentication to a Phoenix app while keeping the Elixir style explicit and modular. It uses a student manager app as the example and focuses on getting registration and session-based authentication running quickly.

## Reading notes

- Pow is presented as a new option for user authentication in Elixir and Phoenix.
- The author prefers it because it fits an explicit and modular Elixir mindset.
- The example app starts from a Live View Dashboard starter template with Ecto and Postgres added.
- The setup begins by adding the Pow dependency to `mix.exs` and running `mix deps.get`.
- `mix pow.install` creates a user file and a migration.
- The author changes the generated `users/user.ex` path to `accounts/user.ex` and configures Pow to use `Studentmanager.Accounts.User` and `StudentManager.Repo`.
- A session plug is added in the endpoint with `Pow.Plug.Session`.
- `pow_routes()` adds routes for registration and authentication.
- A protected pipeline uses `Pow.Plug.RequireAuthenticated` with `Pow.Phoenix.PlugErrorHandler`.
- After `mix ecto.setup`, the app can create a new user at `/registration/new`.
- The conclusion says Pow makes registration and session-based authentication straightforward, with customization options and template generation available for further adaptation.
