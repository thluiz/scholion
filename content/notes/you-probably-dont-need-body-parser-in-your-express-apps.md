---
title: "You probably don't need body-parser in your Express apps"
date: '2026-11-16T01:32:34+00:00'
category: webclip
summary: 'The article says Express has included body parsing since version 4.16.0, so most apps can replace body-parser with express.json() or json() from Express directly.'
tags: ["express", "body-parser", "javascript"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "You probably don't need body-parser in your Express apps"
    url: "https://dev.to/taylorbeeston/you-probably-don-t-need-body-parser-in-your-express-apps-3nio"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--you-probably-dont-need-body-parser-in-your-express-apps.md"
    kind: repo
---

Express has included body parsing since version 4.16.0, so the extra body-parser dependency is usually unnecessary in new examples and apps. The article points to the Express docs and shows how the common setup can be simplified.

## Reading notes

- The common Express setup often installs both express and body-parser and then uses bodyParser.json().
- Express version 4.16.0 already includes body parsing support out of the box.
- The bodyParser reference can be replaced with express, which shortens the code to app.use(express.json()).
- With Babel, the code can be made even shorter by importing json from express and calling app.use(json()).
