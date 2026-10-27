---
title: "#292 Virtual Machines with Vagrant - RailsCasts"
date: '2012-09-08T19:50:12-03:00'
category: webclip
summary: 'Vagrant runs a Rails app and its dependencies in a portable, shareable environment, usable for development, a staging server, or a production setup experiment.'
tags: ["vagrant", "virtual-machines", "rails"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "#292 Virtual Machines with Vagrant - RailsCasts"
    url: "http://railscasts.com/episodes/292-virtual-machines-with-vagrant"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-09/railscasts-com--virtual-machines-with-vagrant.md"
    kind: repo
---

Vagrant is presented as a way to run a Rails application and all of its dependencies in a portable, shareable environment. The page frames it as useful for development, for setting up a staging server, and for trying out a production setup.

## Reading notes

- Vagrant runs a Rails app and its dependencies in a portable environment.
- The same setup can be used for development, staging, or experimenting with production.
- The page lists Vagrant, VirtualBox, Vagrant Boxes, Chef, rbenv, and ruby-build as resources.
- The example shows forwarding port 3000 in Vagrantfile.
- The example Gemfile adds therubyracer.
- The setup sequence includes installing Vagrant, adding a box, creating a Rails app, initializing Vagrant, starting the virtual machine, and connecting by SSH.
- Inside the virtual machine, it updates packages and installs build tools, zlib, curl, git, SQLite, rbenv, Ruby 1.9.2, bundler, and then runs the Rails server.
- The page also lists common Vagrant commands such as reload, status, suspend, resume, halt, up, package, and destroy.
