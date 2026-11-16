---
title: "Deploy on Ubuntu with mix release and Github Actions (without Docker)"
date: '2026-11-16T05:52:34+00:00'
category: webclip
summary: 'The article shows a simple deployment flow for an Elixir/Phoenix app on Ubuntu: a shell script pulls master, runs mix tasks, releases the app, runs migrations, and restarts it, triggered by GitHub Actions.'
tags: ["elixir", "github-actions", "ubuntu", "deployment"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Deploy on Ubuntu with mix release and Github Actions (without Docker) | by Lorenzo Sinisi | elixir-bytes | Medium"
    url: "https://medium.com/elixir-bytes/deploy-on-ubuntu-with-mix-release-and-github-actions-c0fc31a7ef02"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/medium-com--deploy-on-ubuntu-with-mix-release-and-github-actions-without.md"
    kind: repo
---

The post describes a lightweight deployment setup for an Elixir/Phoenix application on an Ubuntu server. After installing Elixir and mix on the server, deployment becomes a sequence of pull, release, migrate, and restart steps.

## Reading notes

- mix release is presented as a way to build self-contained releases for an Elixir project.
- A DigitalOcean Ubuntu server is used as the target deployment environment.
- The server-side script loads environment variables from ~/.profile when available.
- The script uses set -e so deployment stops if any command fails.
- The project directory is entered, and git stash is used before git pull origin master.
- mix deps.get and mix phx.digest are run through an asdf mix binary path.
- mix release --overwrite is run with MIX_ENV=prod.
- After the release, the script runs database migrations through the release binary.
- The application is restarted through the release binary.
- A GitHub Actions workflow triggers on pushes to master.
- The workflow uses an SSH action to run the deploy script on the server.
- Secrets passed to the action include SSH key material, signing salt, secret key base, port, and MIX_ENV.
- The author says this setup avoids the need for CI, Kubernetes, or complex configuration.
