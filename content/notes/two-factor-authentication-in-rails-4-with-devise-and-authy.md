---
title: "Two Factor Authentication in Rails 4 with Devise and Authy"
date: '2016-02-07T22:42:44-03:00'
category: webclip
summary: 'The post shows how to add Devise authentication to a Rails 4 app and then layer Authy on top to enable two-factor authentication with an API key, an initializer, and a database migration.'
tags: ["rails", "devise", "authy", "two-factor-authentication"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Two Factor Authentication in Rails 4 with Devise and Authy"
    url: "https://www.twilio.com/blog/2016/01/two-factor-authentication-in-rails-4-with-devise-authy-and-puppies.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-02/twilio-com--two-factor-authentication-in-rails-4-with-devise-and-authy.md"
    kind: repo
---

The post explains how to secure a Rails 4 app with user accounts and two-factor authentication. It starts from a small app called Super Secret Puppies, adds Devise for login and signup, then uses Authy and the devise-authy gem to require a second factor for account access.

## Reading notes

- passwords alone are treated as insufficient, especially when users choose weak ones like "123456"
- two-factor authentication combines something the user knows with something the user has, such as a phone
- Authy is presented as a Twilio service that exposes two-factor authentication through an API
- the example app already exists, so the work focuses on adding login protection to the puppy page
- Devise is added to the Gemfile, installed, and used to generate a User model
- the puppies controller is protected with authenticate_user so non-logged-in users are redirected to the login page
- sign-out is changed to use a GET request in the Devise initializer
- devise-authy is added after Devise to handle most of the Authy integration
- an Authy initializer sets the API key and API URI
- the API key comes from the Authy dashboard in the Twilio account portal
- the key is stored in config/env.yml through envyable
- the devise-authy install command updates the User model so two-factor authentication works when enabled
- enabling Authy for a user involves visiting /users/enable_authy, entering country and mobile number, and confirming a 7-digit token sent by SMS or the Authy app
- after enabling it, logging out and logging in again requires another token before access is granted
- the post points to custom views, custom redirects, and internationalized messages as optional changes
