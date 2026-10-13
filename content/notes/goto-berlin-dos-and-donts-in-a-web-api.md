---
title: "GOTO Berlin: DO’s and DON’Ts in a Web API"
date: '2013-11-03T15:15:53-03:00'
category: webclip
summary: 'Oliver Wolf argues for web APIs shaped by hypermedia, client intent, correct HTTP verbs and status codes, caching, and content negotiation through headers, while avoiding URL versioning and direct exposure of the domain model.'
tags: ["web-api", "rest", "http", "hypermedia"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "GOTO Berlin: DO’s and DON’Ts in a Web API"
    url: "http://www.infoq.com/news/2013/10/gotober-do-dont-webapi"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-11/infoq-com--goto-berlin-dos-and-donts-in-a-web-api.md"
    kind: repo
---

Oliver Wolf’s talk at GOTO Berlin collects a set of rules for web APIs. The main thread is to treat the web as hypermedia, design around what the client needs to do, and follow HTTP semantics instead of working against them.

## Reading notes

- Do not think of the API as a single endpoint; connect resource representations with meaningful hypermedia links.
- Do not expose the domain model directly, because CRUD-style resources force the client to know too much about behavior and ordering.
- Design the API around intent, balancing clarity and flexibility for what the client wants to do.
- Do not misuse GET and POST; use HTTP verbs to communicate intent and expected server behavior.
- Use the full range of error codes instead of limiting responses to 200 and 500.
- Treat caching as part of the web and use cache headers and ETags to control it.
- Avoid versioning URLs; if the representation changes, use a new media type version instead.
- Use Accept and Content-Type headers for content negotiation rather than URL extensions.
