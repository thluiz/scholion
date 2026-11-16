---
title: "The Complete Guide to Status Codes for Meaningful ReST APIs - Let's start!"
date: '2020-04-20T21:22:44+00:00'
category: webclip
summary: 'The article explains what HTTP status codes are, why they matter for clients, monitoring, and SEO, and how to choose common 200, 300, 400, and 500 codes correctly in APIs.'
tags: ["http-status-codes", "rest-apis", "api-design", "monitoring"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The Complete Guide to Status Codes for Meaningful ReST APIs - Let's start!"
    url: "https://dev.to/khaosdoctor/the-complete-guide-to-status-codes-for-meaningful-rest-apis-1-5c5"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--the-complete-guide-to-status-codes-for-meaningful-rest-apis-.md"
    kind: repo
---

The article argues that HTTP status codes make API responses more meaningful than just choosing request verbs. It defines status codes as part of the HTTP protocol, grouped into classes, and shows why they matter for debugging, monitoring, and SEO.

## Reading notes

- Status codes are defined in HTTP RFCs and are meant to tell the client what happened after a request was processed.
- The code classes are informational 100s, success 200s, redirection 300s, client errors 400s, and server errors 500s.
- Correct status codes help developers validate responses, monitor application health, and let crawling bots understand pages.
- The article says this first part of the series covers the most used API codes only.
- 200 means a successful request, and the exact response can vary by HTTP method.
- 201 is used when a resource has been created, usually after a successful POST.
- 301 is for permanent redirects and should be used with GET or HEAD.
- 302 is for temporary redirects and should be used with GET or HEAD.
- 400 is for cases where the server cannot process the client request and should not be used as a default for every failure.
- 401 applies when the client is not authenticated.
- 403 applies when the client is authenticated but not allowed to perform the action.
- 404 is used when a resource cannot be found, including a missing item from a find-by-id request.
- 405 is used when the method is known but not allowed for that resource.
- 429 is used for too many requests and rate limiting.
- 500 is for server-side errors that are not caught or understood.
- 502 is for proxy or gateway failures.
- 503 indicates service unavailability due to overload or maintenance.
- 504 is for gateway timeout when the upstream server does not answer in time.
