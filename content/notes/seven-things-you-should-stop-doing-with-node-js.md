---
title: "Seven Things You Should Stop Doing with Node.js"
date: '2014-07-06T13:03:41-03:00'
category: webclip
summary: 'The post lists seven Node.js habits to avoid: nested callbacks, wildcard versions, console.log debugging, using GET and POST for everything, semicolons, comma-first style, and the default maxSockets limit.'
tags: ["node-js", "javascript", "debugging", "http"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Seven Things You Should Stop Doing with Node.js"
    url: "http://webapplog.com/seven-things-you-should-stop-doing-with-node-js/?utm_source=nodeweekly&utm_medium=email"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-07/webapplog-com--seven-things-you-should-stop-doing-with-node-js.md"
    kind: repo
---

The post argues that several common Node.js habits should be dropped in favor of clearer or safer alternatives. It recommends async control flow tools for nested work, exact package versions in package.json, real debuggers instead of console.log, REST verbs beyond GET and POST, optional semicolons, avoiding comma-first style, and raising or disabling the default socket limit.

## Reading notes

- Stop nesting multiple callbacks when async.series() or async.waterfall() can structure the flow more clearly.
- Use exact version numbers in package.json instead of * to avoid third-party updates breaking the app.
- Prefer a debugger such as Node Inspector over console.log when inspecting values and stepping through code.
- Use PUT and DELETE for updates and deletions instead of sending everything through GET and POST.
- Semicolons are optional in Node.js JavaScript because of automatic semicolon insertion, though the post notes two cases where they matter.
- The post rejects comma-first style and argues that it looks awkward compared with a more traditional line ending style.
- The default maxSockets value is 5, so it suggests increasing it, setting it to Infinity, or disabling pooling with agent: false.
