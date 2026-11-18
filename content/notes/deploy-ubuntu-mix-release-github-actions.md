---
title: "Deploy on Ubuntu with mix release and Github Actions (without Docker)"
date: '2020-05-12T10:53:30+00:00'
category: webclip
summary: 'Author shows how to auto-deploy an Elixir/Phoenix app on an Ubuntu server using a deploy.sh script triggered by a GitHub Actions SSH workflow on pushes to master.'
tags: ["elixir", "deployment", "github-actions", "ubuntu"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Deploy on Ubuntu with mix release and Github Actions (without Docker)"
    url: "https://medium.com/elixir-bytes/deploy-on-ubuntu-with-mix-release-and-github-actions-c0fc31a7ef02"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-05/medium-com--deploy-ubuntu-mix-release-github-actions.md"
    kind: repo
---

The author describes a simple setup to deploy an Elixir/Phoenix application on a low-cost Ubuntu server using mix release and GitHub Actions without Docker. The process relies on a deploy.sh script on the server that pulls master, builds a production release, runs migrations, and restarts the app, triggered remotely via an SSH GitHub Action when code is pushed to the master branch.

## Reading notes

- mix release can assemble self-contained releases for an Elixir project, making deployment on a small Ubuntu server straightforward.
- Once Elixir and mix are installed on the server, a manual deploy can be done with `cd`, `git pull`, and `MIX_ENV=prod mix release`.
- GitHub Actions can run tests or SSH scripts after pushing code to a repository.
- The author wants to automate the link between pushing to master and deploying to the server.
- A `deploy.sh` script is placed in the project root on the server, starting by sourcing `~/.profile` to load environment variables.
- The script uses `set -e` so it stops if any command fails.
- It changes to the project folder, stashes local changes so master takes precedence, then pulls from `origin master`.
- The script runs `mix deps.get` and `mix phx.digest` using the asdf-managed mix binary under `/root/.asdf/shims/mix`.
- It builds a production release with `MIX_ENV=prod /root/.asdf/shims/mix release --overwrite`.
- After building, the script runs database migrations via a release command that calls `ProjectNameRuntime.Release.migrate` through the release binary.
- The script restarts the application using the release’s `restart` command and prints "Deployment done!".
- A GitHub Actions workflow named "Deployment on master" is configured to trigger on pushes to the `master` branch.
- The workflow defines a `deploy` job that runs on `ubuntu-latest` and uses `garygrossgarten/github-action-ssh@release` to connect to the server over SSH.
- Environment variables in the workflow include SSH username and host, the private deployment key, and secrets such as signing salt, secret key base, project port, and `MIX_ENV` set to `prod`.
- The SSH action is configured with `script_stop: true`, the server hostname, username `root`, the private key secret, and a command that executes `./your-project/deploy.sh` on the server.
- With this setup, every merge to master automatically deploys the Elixir/Phoenix application to the server.
- The author contrasts this approach with heavier setups like CI pipelines, Kubernetes, or complex configurations and mentions fast deploy times as a benefit.
- The post closes by inviting feedback and suggestions for improving the deployment approach.
