---
title: "How to Build a Rails 5 API Only and Backbone Application"
date: '2015-07-20T11:01:54-03:00'
category: webclip
summary: 'The article walks through creating a Rails API-only backend, generating a Todo scaffold and serializer, then wiring a Backbone TODO app to the API with CORS enabled.'
tags: ["rails-api", "backbone", "cors"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to Build a Rails 5 API Only and Backbone Application - WyeWorks’ Blog"
    url: "http://wyeworks.com/blog/2015/6/11/how-to-build-a-rails-5-api-only-and-backbone-application"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-07/wyeworks-com--how-to-build-a-rails-5-api-only-and-backbone-application.md"
    kind: repo
---

The article shows how Rails API was merged into Rails core for Rails 5 and how it supports API-only applications with lightweight controllers, a reduced middleware stack, and customized generators. It then uses a simple Backbone TODO app to demonstrate the backend setup, JSON responses, and frontend integration.

## Reading notes

- Rails API was moved into Rails core, and Rails 5 will include its capabilities.
- API-only Rails apps use lightweight controllers, a reduced middleware stack, and customized generators.
- The example builds a Rails API backend for a simple Backbone TODO app.
- To generate an API-only app on the edge branch, the article uses `bundle exec railties/exe/rails new <parent-folder-path>/my_api_app --api --edge`.
- The generated Gemfile removes asset and template-related dependencies and includes `active_model_serializers`.
- `config/application.rb` uses `api_only` to exclude middleware and controller modules not needed for API-only apps.
- `ApplicationController` inherits from `ActionController::API`.
- A Todo resource is generated with `bin/rails g scaffold todo title completed:boolean order:integer`.
- The scaffolded controller omits `new` and `edit`, and it responds in JSON only.
- The scaffold does not generate template files or an `app/view` folder.
- `resources :todos` creates only the routes needed for the API, excluding `new` and `edit` routes.
- The database should be migrated with `bin/rake db:migrate`.
- A serializer is generated with `bin/rails g serializer todo title completed order`.
- The API can be tested with `curl`, creating a todo and listing todos from `http://localhost:3000/todos`.
- The Backbone app is changed to point its todos collection to `http://localhost:3000/todos` instead of local storage.
- Cross-origin requests are enabled by uncommenting `rack-cors` in the Gemfile and configuring `config/initializers/cors.rb`.
- The example allows requests from `localhost:9000` and accepts the listed HTTP methods.
- The frontend can then be served locally with `ruby -run -e httpd . -p 9000`.
- The article says the TODO items are then stored by the Rails API backend instead of browser local storage.
- It notes that serializer generation could be improved and mentions JBuilder as another serialization option.
