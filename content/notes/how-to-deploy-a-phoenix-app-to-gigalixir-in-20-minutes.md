---
title: "How to Deploy a Phoenix App to Gigalixir in 20 Minutes"
date: '2020-11-12T15:34:10-03:00'
category: webclip
summary: 'Shows the basic steps to create a Phoenix app, adjust production config for Gigalixir, set buildpacks, create a database, and push the app to the host.'
tags: ["phoenix", "gigalixir", "elixir", "deployment"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to Deploy a Phoenix App to Gigalixir in 20 Minutes | Mitchell Hanberg"
    url: "https://www.mitchellhanberg.com/how-to-deploy-a-phoenix-app-to-gigalixir-in-20-minutes/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-11/mitchellhanberg-com--how-to-deploy-a-phoenix-app-to-gigalixir-in-20-minutes.md"
    kind: repo
---

The page gives a short deployment walkthrough for getting a Phoenix app onto Gigalixir. It covers app creation, production config changes for the endpoint and repository, and the commands needed to set up Gigalixir, create the app and database, and deploy.

## Reading notes

- Generate a new Phoenix project with `mix phx.new`, create the database, start the server, and initialize git.
- Adjust `config/prod.exs` so the endpoint uses the Gigalixir app host and port 443, enables `force_ssl`, and sets `ssl: true` for the repo.
- Install Gigalixir with Homebrew, sign up, log in, create the app, and configure the Elixir, Erlang, and Node buildpacks.
- Create a free production database, push to the Gigalixir remote on `main`, and open the deployed app.
