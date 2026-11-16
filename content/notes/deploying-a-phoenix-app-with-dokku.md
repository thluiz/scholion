---
title: "Deploying a Phoenix app with Dokku"
date: '2020-08-26T19:31:15+00:00'
category: webclip
summary: 'This tutorial explains how to deploy an Elixir + Phoenix + Ecto blog app on Dokku, connect Postgres, run migrations on deploy, add a custom domain, and enable SSL with letsencrypt.'
tags: ["dokku", "phoenix", "postgres", "deployment"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Deploying a Phoenix app with Dokku"
    url: "https://nithinbekal.com/posts/dokku-phoenix-deploy"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/nithinbekal-com--deploying-a-phoenix-app-with-dokku.md"
    kind: repo
---

The page walks through deploying a Phoenix blog app on Dokku, starting with a VPS setup and a Dokku installation on Ubuntu. It then shows how to create the app, set environment variables, connect a Postgres database, and configure buildpacks so Elixir and frontend assets compile during deploy.

## Reading notes

- Dokku is presented as the preferred way to deploy a web app to a VPS, with a Heroku-style workflow based on pushing code with git.
- The example app is an Elixir + Phoenix + Ecto blog connected to Postgres.
- The server setup uses a $5/month DigitalOcean VPS with Ubuntu 18.04 and a 1GB swap file to help node compile frontend dependencies.
- Dokku is installed over SSH with the bootstrap script from the Dokku release.
- The web installer is used to set the hostname and enable user virtual naming for apps, which allows subdomain access.
- The blog subdomain is pointed to the Dokku server’s IP address.
- A Dokku app named `blog` is created, and `LC_ALL`, `MIX_ENV`, and `SECRET_KEY_BASE` are set as environment variables.
- The Postgres plugin is installed, then a `blog` database is created and linked to the app.
- Linking Postgres exports `DATABASE_URL`, which Phoenix already expects.
- A local git remote named `dokku` is added so the repository can be deployed with `git push dokku master`.
- The repo needs `.buildpacks` plus Elixir, Erlang, and Node version files so Dokku can build the app correctly.
- After the first push, the app should run on the server IP or on the configured subdomain.
- Ecto migrations are still required: the database is created with `dokku run mix ecto.create`, and an `app.json` file sets `mix ecto.migrate` as the postdeploy command.
- A custom domain can be added with `dokku domains:add blog <your-fancy-domain>`.
- SSL is enabled with the Dokku letsencrypt plugin, which also sets up auto-renewal.
