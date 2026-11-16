---
url: "https://medium.com/elixir-bytes/deploy-on-ubuntu-with-mix-release-and-github-actions-c0fc31a7ef02"
captured_at: "2026-11-16T05:52:34+00:00"
title: "Deploy on Ubuntu with mix release and Github Actions (without Docker) | by Lorenzo Sinisi | elixir-bytes | Medium"
domain: "medium-com"
---

Elixir
Deployment
Servers
Architecture
Deploy on Ubuntu with mix release and Github Actions (without Docker)
Lorenzo Sinisi
2 min read
·
May 8, 2020

Right now we are all aware of the great job done with mix release to assemble self-contained releases for your current Elixir project.

Deploying a new version of your Elixir app on your Digital Ocean 5$/month Ubuntu server has never been easier.

After setting up Elixir, mix, etc on your server it is as easy as:

cd YOUR_PROJECT_FOLDER
git pull
MIX_ENV=prod mix release

And we are all aware of how cool Github Actions are, you can run tests, ssh script, etc after pushing your code to your repositories.

But how to automate the push to master with the deployment on your server?

I came up with the following setup for my project:

I have created a file called `deploy.sh` on the root of my project:

#!/bin/bash
[ -f ~/.profile ] && source ~/.profile # load all env vars
# fail if any command fails (recommended)
set -e
cd project_folder
git stash # master wins
git pull origin master
# if your mix binary is somewhere else, change it below because I use asdf:
/root/.asdf/shims/mix deps.get
/root/.asdf/shims/mix phx.digest
MIX_ENV=prod /root/.asdf/shims/mix release --overwrite
# run the migrations
_build/prod/rel/project_name/bin/project_name rpc "ProjectNameRuntime.Release.migrate"
_build/prod/rel/project_name/bin/project_name restart
echo "Deployment done!"

And a Github Action like the following:

name: Deployment on master
on:
push:
branches: [ master ]

jobs:
deploy:
runs-on: ubuntu-latest
steps:
- name: Deploy master to your-project.com
uses: garygrossgarten/github-action-ssh@release
env:
USERNAME: root
HOST: your-project.com
KEY: ${{ secrets.SSH_DEPLOYMENT_KEY }}
PROJECT_SIGNING_SALT: ${{ secrets.PROJECT_SIGNING_SALT }}
SECRET_KEY_BASE: ${{ secrets.SECRET_KEY_BASE }}
PROJECT_PORT: ${{ secrets.PROJECT_PORT }}
MIX_ENV: prod
with:
script_stop: true
host: your-project.com
username: root
privateKey: ${{ secrets.SSH_DEPLOYMENT_KEY}}
command: . ./your-project/deploy.sh

And so now every time I merge something on master my Elixir/Phoenix application gets deployed automagically :) No need for CI, K8s, Crazy configuration etc.

Does your Google Cloud deploy in 35 seconds? :D

Feel free to share what you think of that and if you can suggest any improvement is very welcome of course
