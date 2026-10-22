---
title: "How LiveView differs from a traditional SPA"
date: '2021-06-14T13:44:42-03:00'
category: webclip
summary: 'The text contrasts traditional SPAs, which split state and code between client and server, with Phoenix LiveView, which keeps state on the server and reduces custom browser-server code.'
tags: ["phoenix-liveview", "single-page-applications", "elixir", "web-development"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How LiveView differs from a traditional SPA."
    url: "https://rafaelantunes.com.br/how-liveview-differs-from-a-traditional-spa?utm_source=elixirdigest&utm_medium=email&utm_campaign=307"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2021-06/rafaelantunes-com-br--how-liveview-differs-from-a-traditional-spa.md"
    kind: repo
---

The text says traditional SPAs depend on coordinating state across browser and server, which splits development into separate parts and makes the code harder to build, test, and maintain. Phoenix LiveView is presented as an alternative that keeps the programming model centered on the server.

## Reading notes

- Traditional SPAs render pages in the browser after requesting markup and data separately, which avoids full page reloads and improves performance and user experience.
- Many SPA solutions rely on JavaScript frameworks such as React and Angular, but the split between front end and back end is described as messy.
- LiveView is described as an Elixir library for Phoenix that enables interactive, real-time single-page flows inside a Phoenix application.
- Current SPA approaches force developers to think in terms of many small requests and responses that change parts of a page independently.
- Splitting development across the client and server creates security risks, slower team workflow, slower bug fixes, and more complicated testing.
- LiveView handles state on the server side and removes the need to write custom code between the browser and the server.
- The result is presented as interactive and fast apps that are resistant to failure and easier to maintain.
