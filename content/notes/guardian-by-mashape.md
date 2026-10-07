---
title: "Guardian by Mashape"
date: '2014-11-23T08:10:14-03:00'
category: webclip
summary: 'Guardian reduces OAuth handling to a single request, uses plugins for different flows, supports production and testing, and exposes HTTP routes for storing and starting authentication.'
tags: ["oauth", "authentication", "nodejs"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Guardian by Mashape"
    url: "http://guardianjs.com/?utm_source=javascriptweekly&utm_medium=email"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-11/guardianjs-com--guardian-by-mashape.md"
    kind: repo
---

Guardian says it reduces the OAuth footprint in code to a single request. It is built around plugins, with five pre-made ones that cover most OAuth services, and it is meant to work in both production and testing by supporting multiple environments.

## Reading notes

- OAuth handling is reduced to one request in client code.
- The system uses plugins to handle OAuth flows, and custom flow plugins can be added when needed.
- Five pre-made plugins are included and are said to cover 99% of OAuth services.
- It is designed for production and testing, with centralized configuration for multiple environments.
- It requires Node.js and Redis.
- Installation uses `npm install -g guardian` after Redis is installed.
- Configuration is loaded from the current working directory, and `./config/default.js` is used when no configuration argument is passed.
- The configuration options include host, protocol, port, workers, pid directory, Redis settings, and cookie and session secrets.
- The HTTP API includes `POST /store` to store OAuth information and return a session hash.
- The stored information expires after 60 seconds by default, controlled by `redis.expire`.
- `/store` accepts OAuth 2, OAuth 1, plugin, and general parameters.
- `GET /hash-check` lets you preview or verify stored information.
- `GET /start?hash=<guardian store hash>` begins the authentication steps through 302 redirects.
- Tests and examples are based on real APIs and show how to use Guardian in practice.
- The project is licensed under MIT.
