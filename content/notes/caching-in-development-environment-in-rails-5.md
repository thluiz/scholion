---
title: "Caching in development environment in Rails 5"
date: '2016-02-07T22:38:28-03:00'
category: webclip
summary: 'Rails 5 adds `rails dev:cache` to toggle development caching by creating or removing `tmp/caching-dev.txt`, so you no longer need to edit `development.rb` and restart manually.'
tags: ["rails-5", "caching", "development-mode"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Caching in development environment in Rails 5 | BigBinary Blog"
    url: "http://blog.bigbinary.com/2016/01/25/caching-in-development-environment-in-rails5.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-02/blog-bigbinary-com--caching-in-development-environment-in-rails-5.md"
    kind: repo
---

Rails 5 adds a command for turning development caching on and off without editing `config/environments/development.rb` by hand. The command creates or removes `tmp/caching-dev.txt`, and the app uses that file to decide whether caching is enabled in development.

## Reading notes

- In Rails 4, enabling caching in development required changing `configaction_controllerperform_caching` in `config/environments/development.rb` and restarting the server.
- Rails 5 introduces `rails dev:cache` to help test caching behavior in development mode.
- Running `rails dev:cache` creates `tmp/caching-dev.txt` and prints that development mode is now being cached.
- In a new Rails 5 app, `development.rb` checks whether `tmp/caching-dev.txt` exists and then uses `:mem_cache_store` when it does.
- The dev cache code toggles the file in `tmp/caching-dev.txt` and touches `tmp/restart.txt`.
- The advantage is that caching can be turned on or off without restarting the server manually.
- The feature is not supported by unicorn, thin, and webrick.
- Running `rails dev:cache` again disables development caching if it was previously enabled.
