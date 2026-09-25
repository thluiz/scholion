---
title: "Set up HTTP Tunneling in minutes with Tunnelmole"
date: '2025-07-17T13:34:15+01:00'
category: webclip
summary: 'The article explains HTTP tunneling, how it forwards public requests to a local server, and why developers use it for webhooks, demos, device testing, API work, and bypassing network blocks.'
tags: ["http-tunneling", "tunnelmole", "webhooks", "nodejs"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Set up HTTP Tunneling in minutes with Tunnelmole - DEV Community"
    url: "https://dev.to/robbiecahill/set-up-http-tunneling-in-minutes-with-tunnelmole-56n4?context=digest"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-07/dev-to--set-up-http-tunneling-in-minutes-with-tunnelmole.md"
    kind: repo
---

The article explains HTTP tunneling as a way to expose a local web service through a public URL, with requests flowing through a secure tunnel to `localhost` and responses returning the same way. It also distinguishes HTTP from HTTPS tunneling and recommends HTTPS for modern development.

## Reading notes

- HTTP tunneling encapsulates HTTP traffic inside another protocol so a local machine can be reached from the public internet through a public URL.
- Tunnelmole provides that public URL and forwards traffic to a local server such as one running on `localhost:3000`.
- HTTPS tunneling is presented as the recommended option because it is secure and encrypted, and Tunnelmole gives free HTTPS URLs by default.
- The request flow goes from the public user or webhook provider to Tunnelmole, then through a secure connection to the client on the developer machine, then to the local app, and back again.
- The guide lists common uses: testing and debugging webhooks, sharing work in progress with stakeholders, testing on real devices, developing APIs for frontend apps, and bypassing restrictive networks or CGNAT.
- The setup steps are to install Tunnelmole, start a local web service, and run Tunnelmole on the port used by the server to get a public URL.
- The article also shows programmatic use in Node.js, both with ES module `import` and CommonJS `require`, so the tunnel can start automatically with the development server.
