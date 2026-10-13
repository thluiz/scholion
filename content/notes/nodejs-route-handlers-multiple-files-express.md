---
title: "How to include route handlers in multiple files in Express"
date: '2012-07-24T10:33:57-03:00'
category: webclip
summary: 'The page shows one way to load every route file in a routes directory by reading the folder, skipping index.js, requiring each module, and calling it with app from app.js.'
tags: ["nodejs", "express", "routes"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "node.js - How to include route handlers in multiple files in Express - Stack Overflow"
    url: "http://stackoverflow.com/questions/6059246/how-to-include-route-handlers-in-multiple-files-in-express"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-07/stackoverflow-com--nodejs-route-handlers-multiple-files-express.md"
    kind: repo
---

The page describes a pattern for splitting Express route handlers across several files and loading them from a directory. A routes/index.js file reads the directory, ignores index.js, requires each other file, and calls it with app. Then app.js only needs to require('./routes')(app).

## Reading notes

- routes/index.js uses fs.readdirSync(__dirname) to iterate through files in the routes folder.
- The code skips index.js and derives a module name from each file name before requiring it.
- Each route file exports a function that receives app.
- A route file like routes/test1.js can register routes with app.get('/test1/', ...).
- app.js loads the directory entry point with require('./routes')(app).
