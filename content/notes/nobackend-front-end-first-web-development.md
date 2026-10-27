---
title: "NoBackend: Front-End First Web Development"
date: '2013-09-27T10:17:01-03:00'
category: webclip
summary: 'Gregor Martynus argues that app design should start from the front end, not server constraints, with JavaScript filling browser gaps and backend services handling security, syncing, and other server-side work.'
tags: ["front-end-development", "backend-as-a-service", "javascript", "offline-sync"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "NoBackend: Front-End First Web Development"
    url: "http://www.infoq.com/news/2013/05/nobackend"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-09/infoq-com--nobackend-front-end-first-web-development.md"
    kind: repo
---

Gregor Martynus argues for a front-end driven design process in which developers start from the user experience and work backward to whatever server-side pieces are still needed. The article presents noBackend as a way to remove backend constraints from the design stage, while still relying on servers for things like security and synchronization.

## Reading notes

- The front-end should shape the app first, instead of letting server technology and database choices dictate the design.
- noBackend means developers do not need to think about backend limits as the starting point, because JavaScript can fill gaps in browser support.
- The approach depends on CORS and asynchronous code such as callbacks, events, or promises.
- Dreamcode is presented as the simplest JavaScript needed to express a feature, and as a way to let frontend and backend teams work against the same interface.
- From the backend side, dreamcode is described as another name for BDD or TDD, and as a simpler successor to a REST API.
- Security still belongs on the server, including spam prevention and access checks for email sending and payments.
- Backend-as-a-Service is treated as a special case of noBackend, with examples including Firebase, Parse, Kinvey, Backendless, hood.ie, remotestorage.io, and deployd.com.
- Offline support is linked to lower latency and better user experience, with data stored locally first and synced later.
- noBackend is described as most suitable for applications whose logic lives mostly in the front end and whose user experience is the main feature.
