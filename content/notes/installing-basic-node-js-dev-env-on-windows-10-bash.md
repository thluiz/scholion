---
title: "Installing basic Node.js dev env on Windows 10 bash"
date: '2017-02-28T09:31:26-03:00'
category: webclip
summary: 'The post gives a short bash script for Windows 10 bash that installs git, Node.js, and npm, then explains each command and notes how to switch Node versions and upgrade later.'
tags: ["node-js", "git", "windows-10-bash", "npm"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Installing basic Node.js dev env on Windows 10 bash"
    url: "https://aigeec.com/installing-node-js-on-windows-10-bash/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2017-02/aigeec-com--installing-basic-node-js-dev-env-on-windows-10-bash.md"
    kind: repo
---

The page gives a quick way to set up a basic Node.js development environment in Windows 10 bash. It shows a script that updates apt, installs git, pulls the NodeSource setup for Node 6.x, and installs nodejs, with an optional symlink so the command can be called as node.

## Reading notes

- The script starts with sudo su, then runs apt-get -y update, apt-get install git, curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -, and apt-get install -y nodejs.
- The explanation says Windows 10 bash works much like Ubuntu for these steps.
- Some commands may need sudo, such as sudo apt-get -y update.
- git is installed with apt-get install git, and the post says git-all used to be listed but git should work in most cases.
- Without the NodeSource setup step, apt-get install would give Node 0.10.x.
- After installing nodejs, the post suggests creating a symlink from which nodejs to /usr/bin/node if needed.
- The page says that after this you should have node, npm, and git installed.
- It points to NodeSource version lists, the Node.js site, and a separate post about upgrading Node.js on Windows 10 bash.
