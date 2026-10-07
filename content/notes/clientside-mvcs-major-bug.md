---
title: "Client-side MVC's Major Bug"
date: '2015-02-10T10:55:05-03:00'
category: webclip
summary: 'Tim Kadlec argues that client-side MVC frameworks often become the main performance bottleneck, especially on first load, and that they need server-side rendering to avoid hurting reach and stability.'
tags: ["client-side-mvc", "server-side-rendering", "performance", "web-apps"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Client-side MVC's major bug - TimKadlec.com"
    url: "http://timkadlec.com/2015/02/client-side-templatings-major-bug/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-02/timkadlec-com--clientside-mvcs-major-bug.md"
    kind: repo
---

Tim Kadlec says his performance audits repeatedly found client-side MVC frameworks, often Angular, to be the main bottleneck. He argues that they slow initial rendering, especially on mobile, and make it harder to optimize the critical path.

He supports server-side rendering for the first page load and points to examples like Twitter, AirBnB, Wal-Mart, and Trulia. He sees the issue as one of performance, stability, reach, and responsible web development.

## Reading notes

- Client-side MVC frameworks were the main bottleneck in several site audits.
- They slowed initial rendering, especially on mobile.
- They limited optimization of the critical path.
- Filament Group's To-Do app tests showed better initial load times for Backbone than for Ember or Angular.
- PPK argues that filling an HTML page with default data belongs on the server, not the client.
- Kadlec says a client-side MVC framework without server-side rendering is buggy and hurts performance.
- He also says client-side templating creates a single point of failure.
- He does not reject these tools outright.
- He supports RESTful APIs, JavaScript templating, and better performance on later page loads.
- He argues that the first page load still needs a server-side data layer.
- He points to Twitter, AirBnB, Wal-Mart, and Trulia as examples that support server-side rendering.
- He mentions Node.js as a shared layer between server and client templates.
- He says Ember's FastBoot and React.js are pushing in this direction.
- He frames the issue as performance, stability, reach, and responsible web building.
