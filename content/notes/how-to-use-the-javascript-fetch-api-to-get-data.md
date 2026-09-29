---
title: "How to Use the JavaScript Fetch API to Get Data"
date: '2020-05-28T18:45:59-03:00'
category: webclip
summary: 'The article shows how fetch() makes GET requests simpler than XMLHttpRequest, then demonstrates turning JSON into a list of Random User results and using Request objects for POST-style calls.'
tags: ["javascript", "fetch-api", "http-requests"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to Use the JavaScript Fetch API to Get Data ― Scotch.io"
    url: "https://scotch.io/tutorials/how-to-use-the-javascript-fetch-api-to-get-data"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-05/scotch-io--how-to-use-the-javascript-fetch-api-to-get-data.md"
    kind: repo
---

The article introduces the Fetch API as the built-in JavaScript way to make server requests with promises. It shows a basic fetch call with a URL, then uses it to load 10 users from the Random User API and render them in a list.

## Reading notes

- `fetch(url)` is presented as the default GET request pattern, with `.then()` for handling the response and `.catch()` for errors.
- The response is described as an object with methods such as `clone()`, `redirect()`, `arrayBuffer()`, `formData()`, `blob()`, `text()`, and `json()`.
- The example converts the response with `resp.json()` because the data is meant to be handled as JSON.
- Two helper functions are defined, one to create elements and one to append them.
- The code takes `data.results`, maps over the users, creates `li`, `img`, and `span` elements, sets the image source and the name text, and appends everything to the `ul`.
- The article also shows how to send other request types such as POST by passing an options object as the second argument to `fetch`.
- It gives a second POST example using the `Request` constructor before calling `fetch(request)`.
- The closing note says Fetch API support was not yet complete in all browsers at the time, mentions Safari as unsupported, and refers to polyfills.
