---
title: "How to write a login form that doesn't suck, using Ember.js"
date: '2014-04-23T16:46:13-03:00'
category: webclip
summary: 'The post shows how a login form in Ember.js can give feedback for failed logins, disable submission while processing, and warn users when a request is slow.'
tags: ["ember-js", "ux", "login-form", "ajax"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to write a login form that doesn't suck, using Ember.js - sensible.io Blog"
    url: "http://blog.sensible.io/2013/05/23/how-to-write-a-login-form.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-04/blog-sensible-io--how-to-write-a-login-form-that-doesnt-suck-using-ember-js.md"
    kind: repo
---

The post argues that Ember.js should be used to improve user experience, not because it is trendy or fast for its own sake. It uses a login form to show how the interface can communicate failure, processing, and slow network requests.

## Reading notes

- Ember makes it easy to build a login form, but the point is to improve UX rather than chase the framework itself.
- A simple flash message can show invalid username or password when the login request fails.
- The controller should clear the error state and mark the form as processing when a new login request starts.
- The submit button is disabled while the request is being processed.
- If the request takes more than five seconds, the controller sets a slow-connection flag and the template shows an informational message.
- The code is refactored into separate success, failure, slowConnection, and reset methods.
- The article says these indicators matter because AJAX removes the normal page-submission progress feedback users would otherwise see.
- It argues against showing a loading indicator for every request, because that can distract from a single-page application.
