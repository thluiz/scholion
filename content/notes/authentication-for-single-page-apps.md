---
title: "Authentication for Single Page Apps"
date: '2014-06-30T10:06:04-03:00'
category: webclip
summary: 'The post argues that single-page app authentication works better when authorization and session creation are modeled as separate API concerns. It presents Torii as an Ember.js abstraction for composable providers, sessions, and adapters.'
tags: ["authentication", "single-page-apps", "api-design", "emberjs"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Authentication for Single Page Apps :: madhatted.com"
    url: "http://madhatted.com/2014/6/17/authentication-for-single-page-apps?utm_source=Ember+Weekly&utm_campaign=d5470c3387-Ember_Weekly_Issue_63&utm_medium=email&utm_term=0_e96229d21d-d5470c3387-99490097"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-06/madhatted-com--authentication-for-single-page-apps.md"
    kind: repo
---

The post argues that authentication in single-page apps should live inside the JavaScript application and the API, not as a separate server-side flow. It shows how mixing username/password login, OAuth2 handling, redirects, and session creation turns a session endpoint into an RPC-like endpoint with inconsistent inputs and many error states.

It proposes splitting authorization from session management so the API stays composable. Torii is presented as the Ember.js abstraction for this approach: providers create authorization, sessions track authentication state, and adapters bridge authorization objects to the app’s API.

## Reading notes

- Traditional server-side authentication patterns fit poorly in single-page apps.
- Putting authentication and authorization into the API and JavaScript app simplifies state, errors, refactoring, and UX.
- A single `/api/session` endpoint becomes messy when it handles username/password login and OAuth2 redirect handling together.
- Separating `socialAuthorization` from `session` keeps the API closer to RESTful domain objects.
- A social authorization object can be reused for session creation and for linking connected accounts.
- OAuth2 popup flows avoid server-side redirect handlers and keep the JavaScript app from reloading.
- Torii is built around providers, sessions, and adapters.
- Providers open authorization, sessions open/fetch/close authentication state, and adapters map authorization objects onto an app-specific API.
