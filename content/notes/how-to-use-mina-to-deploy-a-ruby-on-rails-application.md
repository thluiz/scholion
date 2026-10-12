---
title: "How To Use Mina to Deploy a Ruby on Rails Application"
date: '2014-03-17T09:35:17-03:00'
category: webclip
summary: 'The page explains how to install Mina, configure deploy.rb, set SSH and repository options, and run setup and deploy tasks for a Rails app using Mina.'
tags: ["mina", "ruby-on-rails", "deployment", "ssh"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How To Use Mina to Deploy a Ruby on Rails Application | DigitalOcean"
    url: "https://www.digitalocean.com/community/articles/how-to-use-mina-to-deploy-a-ruby-on-rails-application"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-03/digitalocean-com--how-to-use-mina-to-deploy-a-ruby-on-rails-application.md"
    kind: repo
---

Mina is presented as a deployment tool that runs scripts over SSH and uses Rake instead of YAML configuration. The tutorial shows how to install the gem, generate deploy.rb, set server and repository details, and choose the right environment loader for rbenv or rvm.

It also shows the standard deploy flow: run mina setup to create the folder structure, then mina deploy to clone the repository, link shared paths, install gems, and optionally migrate the database and precompile assets. An example deploy.rb and a sample Rails app setup are included.

## Reading notes

- Mina manages deployments by running scripts over SSH and creates one SSH session per deploy.
- Configuration lives in Ruby files because Mina is built on Rake and does not use YAML files.
- The tool can be used with any project that can be deployed via SSH.
- Mina can be installed with gem install mina or added to a Rails Gemfile.
- deploy.rb is a Rakefile where server settings and tasks are defined.
- queue sends bash commands to the remote server.
- invoke calls subtasks from another task.
- A sample deploy.rb shows tasks for restart, logs, and a parent task that invokes both.
- mina init generates the deploy.rb file.
- The sample configuration sets domain, deploy_to, repository, branch, user, and ssh_options.
- If using SSH clone URLs, the tutorial says to enable agent forwarding in ~/.ssh/config.
- The environment task should load rbenv or rvm depending on the Ruby setup.
- The setup task creates folders and files under the deploy path and sets permissions.
- The deploy task clones the repository, links shared paths, installs gems, and can run database migrations and asset precompilation.
- For MySQL, the tutorial says to uncomment the database migration task.
- mina setup --verbose shows detailed output while creating the server structure.
- mina deploy --trace shows backtraces when errors happen.
- The example section creates a Rails app, pushes it to GitHub, and uses a simpler deploy.rb.
- The example deploy path points to a production folder under /home/username/app.
- The page says WEBrick is not recommended for production.
