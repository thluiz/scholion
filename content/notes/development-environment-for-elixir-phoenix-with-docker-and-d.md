---
title: "Development environment for Elixir + Phoenix with Docker and Docker-compose"
date: '2026-11-16T15:43:31+00:00'
category: webclip
summary: 'The post shows how to set up a hot-reloaded local development environment for Elixir and Phoenix with Docker, Docker-compose, a Postgres service, and container-based database configuration.'
tags: ["elixir", "phoenix", "docker", "docker-compose"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Development environment for Elixir + Phoenix with Docker and Docker-compose"
    url: "https://web.archive.org/web/20200818140203id_/https://dev.to/hlappa/development-environment-for-elixir-phoenix-with-docker-and-docker-compose-2g17"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--development-environment-for-elixir-phoenix-with-docker-and-d.md"
    kind: repo
---

The article describes a local development setup for Elixir and Phoenix that runs inside Docker and Docker-compose. It uses a Dockerfile, a docker-compose.yml file, and an .env file, and it keeps the application connected to Postgres through a container environment variable.

## Reading notes

- Start from a newly generated Phoenix app and remove deps and node_modules from the host project structure because the app will run in containers.
- Build the image from bitwalker/alpine-elixir-phoenix, copy mix files and asset package files, and run deps.get, npm install, and mix phx.server in the container.
- Define two services in docker-compose.yml, one for postgres:11-alpine and one for the web app, with a pgdata volume and port 4000 exposed.
- Store DATABASE_URL in .env and read it in config/dev.exs with System.get_env("DATABASE_URL").
- Replace the direct database settings in dev.exs with a url-based Repo configuration and keep the development endpoint settings for code reloading and live reload.
- Remove the SSL section from the development config because the local setup does not use SSL.
- Run docker-compose build, then docker-compose up, and create the database with docker-compose run web mix ecto.create when the container reports that the database does not exist.
- Use mix commands inside the container for tasks such as migrations, seeds, database reset, and startup, with file changes reflected without manual container restarts.
- The setup is presented as a minimal development configuration, and the author says a follow-up post will cover production deployment to Azure.
