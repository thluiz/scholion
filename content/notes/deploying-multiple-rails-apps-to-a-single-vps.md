---
title: "Deploying Multiple Rails apps to a Single VPS"
date: '2013-12-02T16:49:50-03:00'
category: webclip
summary: 'Tutorial showing how to deploy multiple Rails apps on one VPS with Capistrano 2, using multistage setup, Unicorn, and nginx to keep each app’s configuration separate.'
tags: ["rails", "capistrano", "unicorn", "nginx"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Deploying Multiple Rails apps to a Single VPS by TalkingQuickly"
    url: "http://www.talkingquickly.co.uk/2013/11/deploying-multiple-rails-apps-to-a-single-vps/?utm_source=rubyweekly&utm_medium=email"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-12/talkingquickly-co-uk--deploying-multiple-rails-apps-to-a-single-vps.md"
    kind: repo
---

The tutorial explains the basics of deploying several Rails applications on a single VPS. It assumes a server already set up with nginx, a database server, SSH access, and a copied public key. It uses Capistrano 2, but says the setup is still relevant if you prefer Capistrano 3.

It then walks through a multistage Capistrano setup with a production stage, a helper for ERB templates, and stage-specific configuration. Each application gets its own database configuration, Unicorn config, init script, and nginx virtual host file. The deployment flow creates the config files on the server, lets you fill in the production database details, and then deploys the app. The approach scales until server resources become the limit.

## Reading notes

- The post answers a common question about whether the author’s Rails deployment book covers multiple apps on one VPS.
- The setup assumes nginx, a database server, SSH access, and an existing public key on the server.
- The tutorial uses Capistrano 2 and says the configuration focus still applies if you prefer Capistrano 3.
- The example starts by adding Capistrano to the development group and Unicorn to production in the Gemfile.
- Running `capify .` creates `Capfile` and `config/deploy.rb`.
- The deployment setup uses Capistrano multistage and starts with a production stage.
- A helper method reads an ERB template and writes the rendered result to a file.
- A production stage file is placed in `config/deploy` and matched by `cap production deploy`.
- The stage file sets the server address, Rails environment, application name, application domain, SCM, repository, and branch.
- `setup_config` creates application-specific configuration on the remote server.
- `database.yml` is kept out of source control and copied to the shared folder on the server.
- `symlink_config` links `app_root/config/database.yml` to the shared database file.
- `unicorn.rb.erb` configures Unicorn and creates pidfiles for worker processes.
- `worker_processes 1` is the key setting highlighted for Unicorn.
- The number of Unicorn workers depends on available RAM, the number of apps on the server, and the number of cores.
- `unicorn_init.sh.erb` becomes `/etc/init.d/unicorn_application` and supports restart, start, and stop commands.
- `nginx.conf` proxies requests for the configured domain to the Unicorn workers.
- Deploying follows the sequence `cap production deploy:setup`, editing `database.yml`, and then `cap production deploy`.
- The server can host as many Rails apps as its resources allow, because each app keeps its own config and nginx routes by domain.
