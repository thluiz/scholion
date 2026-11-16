---
title: "Phoenix CSRF protection in HTML forms, React forms, and APIs"
date: '2026-11-16T03:43:47+00:00'
category: webclip
summary: 'Explains how Phoenix handles CSRF protection for HTML forms, how to send the token in React AJAX requests, and how to expose it as a cookie for SPA or API-style clients.'
tags: ["phoenix", "csrf-protection", "react", "api"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Phoenix CSRF protection in HTML forms, React forms, and APIs"
    url: "https://nts.strzibny.name/phoenix-csrf-protection-in-html-forms-react-forms-and-apis"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/nts-strzibny-name--phoenix-csrf-protection-in-html-forms-react-forms-and-apis.md"
    kind: repo
---

The page explains how Phoenix protects non-GET requests with CSRF tokens. It shows that standard HTML forms get a hidden `_csrf_token` field automatically, while the router’s `:protect_from_forgery` plug validates that token and returns `403 Forbidden` when validation fails.

It also shows how to reuse the token outside classic Phoenix forms. A React form can read the token from `csrf_meta_tag()` and send it in the `X-CSRF-Token` header, and a separate SPA can fetch the token from a controller action that writes it into a cookie. The text notes that the plug can also use `:clear_session` instead of raising an exception.

## Reading notes

- Phoenix injects a hidden CSRF token into standard HTML forms.
- The router should include `:protect_from_forgery` in the browser pipeline.
- The CSRF token can arrive either in `_csrf_token` params or in the `x-csrf-token` header.
- The plug can use `:exception` or `:clear_session`.
- A React page can read the token from a meta tag and send it in `X-CSRF-Token`.
- A separate SPA can obtain the token through a controller action that stores it in a cookie.
