---
title: "Split route namespaces into different files"
date: '2012-05-15T21:55:06-03:00'
category: webclip
summary: 'The page recommends separating Rails routes by namespace into different files. This makes complex route sets easier to maintain and lets Rails reload only the file that changed.'
tags: ["rails-routes", "namespaces", "maintainability"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Rails Best Practices | split route namespaces into different files"
    url: "http://rails-bestpractices.com/posts/73-split-route-namespaces-into-different-files"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-05/rails-bestpractices-com--split-route-namespaces-into-different-files.md"
    kind: repo
---

The page argues that when a Rails app has a default route set plus several namespaces, keeping everything in one routes file makes the configuration harder to manage and easier to edit in the wrong namespace. It proposes moving each namespace into its own file.

## Reading notes

- The example starts with one `config/routes.rb` containing the default routes and the `developer`, `admin`, and `api` namespaces together.
- The text says this becomes difficult to maintain because the routes are similar across namespaces and easy to change in the wrong place.
- The suggested approach is to split the namespace routes into separate files such as `config/routes/developer.rb`, `config/routes/admin.rb`, and `config/routes/api.rb`.
- For Rails 2, the page shows an initializer that adds those route files with `ActionController::Routing::Routes.add_configuration_file`.
- For Rails 3, it shows adding all files from `config/routes/*.rb` in `config/application.rb`.
- The page says this setup makes it easier to change only the routes for one namespace and can reduce reloading work when only one route file changes.
