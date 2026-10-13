---
title: "An In-Depth Introduction To Ember.js"
date: '2013-11-10T22:11:27-03:00'
category: webclip
summary: 'The article introduces Ember.js concepts, then walks through building a CRUD app with routes, controllers, templates, Ember-Data, helpers, views, components, and template precompiling.'
tags: ["emberjs", "ember-data", "crud", "handlebars"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "An In-Depth Introduction To Ember.js | Smashing Coding"
    url: "http://coding.smashingmagazine.com/2013/11/07/an-in-depth-introduction-to-ember-js/?utm_source=javascriptweekly&utm_medium=email"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-11/coding-smashingmagazine-com--an-in-depth-introduction-to-ember-js.md"
    kind: repo
---

The article introduces Ember.js for newcomers and uses a simple users CRUD app to explain the framework’s main concepts. It covers how routes, controllers, views, templates, models, helpers, components, and Ember-Data fit together, then shows how to add editing, deletion, creation, formatting, and local storage persistence.

## Reading notes

- Ember.js 1.0 is presented as a good moment to start learning the framework.
- The article aims to make the learning curve smoother for beginners.
- It first explains the main concepts, then builds a simple web app with Ember.js and Ember-Data.
- The demo comes in two versions, one unstyled and one with extra CSS, animations, and responsive behavior.
- Models are described as the application’s data, such as a collection of users.
- Ember-Data is used to simplify retrieval, updating, and persistence over a REST API.
- The Router summarizes the routes of the application, and routes query the model in their `model` hook.
- Controllers bridge the model and the template, and can hold methods for UI state changes.
- Views are used for visual parts and for handling events that templates cannot manage well.
- Components are isolated views that do not access surrounding context and are meant for reusable UI.
- Templates print model data and update when the model changes.
- Handlebars helpers format data before rendering.
- The app example is a CRUD interface for managing users.
- Ember.js relies heavily on naming conventions for templates, routes, controllers, and views.
- The tutorial uses jQuery, Ember.js, Handlebars, and Ember-Data.
- Templates can be declared in `script` tags or precompiled from `.hbs` files.
- The article uses `FixtureAdapter` first and later switches to `LSAdapter` for local storage persistence.
- The user model includes `name`, `email`, `bio`, `avatarUrl`, and `creationDate`.
- The router defines nested resources for users, a single user, edit, and create routes.
- The application template contains `{{outlet}}` for rendering nested templates.
- `UsersRoute` loads the user collection from the store.
- `UsersController` can sort users and compute the number of users.
- Computed properties are shown as functions declared as properties that react to dependent keys.
- The index route can redirect to the users route.
- `{{#link-to}}` is used for navigation and for linking to a specific user.
- `{{bind-attr}}` is used for bound attributes such as the avatar image source.
- Nested routes require `{{outlet}}` in parent templates.
- `UserRoute` loads a single user by dynamic segment.
- The edit form reuses the nested user template and binds fields with `{{input}}` and `{{textarea}}`.
- `modelFor('user')` lets the edit route reuse the parent route’s model.
- `{{action}}` is used to trigger edit, save, delete, confirm delete, and cancel delete behavior.
- Saving edits calls `save()` on the record and transitions back to the user route.
- Deletion is first toggled into a confirmation state and then confirmed.
- The create route reuses the edit template and creates a new empty object as its model.
- A new user gets a `creationDate` before being saved to the store.
- `formatDate` is shown as a helper that formats dates with Moment.js.
- A bound helper is presented for data that can change later.
- Ember-Data is explained through the store and its adapters.
- `FixtureAdapter`, `RESTAdapter`, and custom adapters are described as ways to connect different back ends.
- The article also explains how Ember can be used without Ember-Data.
- Template precompiling stores compiled Handlebars templates in `Ember.TEMPLATES`.
- Grunt and Rails are both presented as ways to precompile templates.
- The article ends with tooling, debugging tips, the Ember Inspector extension, and a note to use the development build while developing.
