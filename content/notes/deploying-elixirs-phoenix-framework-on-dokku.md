---
title: "Deploying Elixir's Phoenix Framework on Dokku"
date: '2026-11-16T03:04:16+00:00'
category: webclip
summary: 'This gist lays out the Dokku setup for a Phoenix app: create the app, enable multiple buildpacks, set locale, secret key, host, and database config, then commit and push.'
tags: ["phoenix", "dokku", "elixir", "deployment"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Deploying Elixir's Phoenix Framework on Dokku."
    url: "https://gist.github.com/henrik/c70e32544e09c1a79841"
    kind: repo
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/gist-github-com--deploying-elixirs-phoenix-framework-on-dokku.md"
    kind: repo
---

The gist shows how to prepare a Phoenix app for Dokku by configuring buildpacks, environment variables, and deploy settings on the app's repo. It also notes that the instructions worked for Phoenix 1.0.1 on Dokku 0.3.25.

## Reading notes

- Create a Dokku app from the local repo with `ssh dokku apps:create my_app_name`.
- Set Dokku to use multiple buildpacks with `BUILDPACK_URL=https://github.com/ddollar/heroku-buildpack-multi.git`.
- Add the Elixir buildpack and the Phoenix static buildpack to `.buildpacks`.
- For Phoenix 1.1, the static buildpack may need `node_version=5.3.0` in `phoenix_static_buildpack.config`.
- The Elixir buildpack can be configured to lock Erlang and Elixir versions.
- Set `LC_ALL=en_US.utf8` in Dokku to avoid a locale warning.
- Store `SECRET_KEY_BASE` in Dokku config and read it in `config/prod.secret.exs` with `System.get_env("SECRET_KEY_BASE")`.
- Store `HOSTNAME` in Dokku config and read it in `prod.exs` with `System.get_env("HOSTNAME")`.
- If the app uses a database, read `DATABASE_URL` from config in the Repo settings.
- Comment out `#/config/prod.secret.exs` in `.gitignore` so the secret-less file can be committed.
- Commit the changes, add the Dokku remote, and push to deploy.
