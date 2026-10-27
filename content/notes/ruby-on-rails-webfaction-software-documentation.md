---
title: "Ruby on Rails — WebFaction Software Documentation"
date: '2014-01-05T17:21:18-03:00'
category: webclip
summary: 'WebFaction explains how to install, configure, and deploy Rails apps, including PATH setup, gems, Bundler, ImageMagick, databases, Action Mailer, and troubleshooting production mode.'
tags: ["ruby-on-rails", "webfaction", "deployment", "configuration"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Ruby on Rails — WebFaction Software Documentation"
    url: "http://docs.webfaction.com/software/rails.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-01/docs-webfaction-com--ruby-on-rails-webfaction-software-documentation.md"
    kind: repo
---

The page describes Ruby on Rails on WebFaction as an open source Ruby web development framework used to quickly design, develop, and deploy web applications. It then walks through application setup and maintenance tasks for a Passenger-based Rails install, including environment variables, gem management, database configuration, deployment, and troubleshooting.

## Reading notes

- Rails is presented as an open source Ruby web development framework, also called Rails or RoR, for quickly designing, developing, and deploying web applications.
- The page suggests adding the application’s bin directory to PATH and setting GEM_HOME and RUBYLIB so gem and rake work for that application.
- WebFaction’s Rails installer creates an nginx instance running Passenger.
- To install a Rails application, the user creates a new application in the control panel, chooses the Rails category, and saves it.
- To make the application available on the web, it must be added to a website record.
- Passenger-based applications can be upgraded to a newer RubyGems version by downloading the archive and running ruby setup.rb install with the application prefix.
- Gems are installed inside the Rails application after setting GEM_HOME, RUBYLIB, and PATH.
- The page lists common gems for MySQL, PostgreSQL, RSpec, and Sinatra, and notes that gem install can skip RDoc and RI documentation.
- Bundler can install multiple dependency gems at once, after gem install bundler and bundle install in the project directory.
- ImageMagick is installed from source in the user’s home directory, PATH is updated to include $HOME/bin, and RMagick is installed afterward.
- Rails is configured by default for SQLite 3, and sqlite3-ruby must be installed to use a SQLite 3 database.
- To deploy a custom Rails app, the application is uploaded to the Rails application directory, nginx.conf is edited to point root to the app’s public directory, and the app is restarted.
- The Capistrano section applies to Capistrano 2.x, tells the user to set application, repository, scm, deploy_to, server roles, user settings, and a restart task, then run deploy setup, deploy check, and deploy.
- Database use requires creating a MySQL or PostgreSQL database, installing the corresponding adapter gem, and editing config/database.yml for production.
- Action Mailer configuration for Rails 3.0 or later uses config.action_mailer.delivery_method = :sendmail in production.rb.
- The troubleshooting section says the “We’re sorry, but something went wrong” error happens when the link is clicked in production mode, and switching to development requires sqlite3-ruby and rails_env development; in nginx.conf.
- Development mode uses more resources than production, so the page advises returning to production when it is no longer needed.
