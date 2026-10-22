---
title: "Replace axios with a simple custom fetch wrapper"
date: '2020-09-10T19:13:29-03:00'
category: webclip
summary: 'The page argues that, in the browser, a small custom wrapper around fetch can replace axios for most needs while keeping the API simpler, smaller, and easier to maintain.'
tags: ["fetch", "axios", "javascript", "browser"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Replace axios with a simple custom fetch wrapper"
    url: "https://kentcdodds.com/blog/replace-axios-with-a-simple-custom-fetch-wrapper"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-09/kentcdodds-com--replace-axios-with-a-simple-custom-fetch-wrapper.md"
    kind: repo
---

The page says axios does a lot, but for browser code a small wrapper around fetch often covers the common cases with less API surface and a smaller bundle. It presents a client helper that wraps a base API URL, parses JSON, rejects on non-OK responses, adds request bodies, and sends an Authorization header from localStorage when a token exists.

It also shows how the wrapper can handle a 401 by logging the user out and refreshing the page, and how other request helpers can build on top of the same client for create, read, update, and remove operations.

## Reading notes

- axios can be replaced in many browser cases by a simple custom wrapper around fetch
- fetch is described as a promise-based browser standard that is widely supported and polyfillable
- the wrapper reduces API to learn, bundle size, package update friction, and conceptual complexity
- the client function builds requests from a base API URL and JSON-parses responses
- non-OK responses are turned into rejected promises by checking response.ok
- request bodies are sent as JSON, with method chosen as POST when body is present and GET otherwise
- authenticated requests read a token from localStorage and add an Authorization Bearer header
- a 401 response triggers logout and a page refresh, with redirect to login mentioned as another option
- additional helpers can wrap the client for specific endpoints such as list-items create, read, update, and remove
- the conclusion says axios is still fine, especially in node projects, but custom fetch wrappers can be better suited to browser needs
