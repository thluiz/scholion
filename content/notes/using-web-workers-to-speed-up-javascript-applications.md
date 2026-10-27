---
title: "Using Web Workers to Speed-Up Your JavaScript Applications"
date: '2013-01-18T22:08:21-03:00'
category: webclip
summary: 'The post explains that Web Workers let browser apps move heavy tasks off the main thread, keeping the UI responsive. It also shows how to create, message, and terminate workers, plus their main limits.'
tags: ["web-workers", "javascript", "browser-performance"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Using Web Workers to Speed-Up Your JavaScript Applications"
    url: "http://blog.teamtreehouse.com/using-web-workers-to-speed-up-your-javascript-applications?utm_source=javascriptweekly&utm_medium=email"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-01/blog-teamtreehouse-com--using-web-workers-to-speed-up-javascript-applications.md"
    kind: repo
---

The post argues that Web Workers help browser-based JavaScript applications stay responsive by moving expensive work to background threads. It contrasts single-threaded blocking with multi-threaded execution, then shows the basic worker lifecycle: create a worker file, send messages to it, receive replies, and terminate it when the task is done.

## Reading notes

- JavaScript in the browser usually runs on a single thread, so a long task can block everything else until it finishes.
- Web Workers let the browser run JavaScript in separate threads, which helps prevent frozen user interfaces during resource-intensive work.
- A worker is created by loading a separate JavaScript file with `new Worker('work.js')`.
- The main application starts communication with `postMessage()`.
- A worker listens for incoming data with a `message` event listener.
- A worker sends data back with `self.postMessage()`.
- The main application can listen for replies from the worker with its own `message` event listener.
- A worker can be stopped from the main application with `worker.terminate()`.
- A worker can stop itself with `self.close()`.
- Worker scripts must come from the same domain and protocol as the page that creates them.
- Workers do not have access to the DOM, `document`, `window`, or `parent`.
- If a worker needs to affect the UI, the main application must receive the data and update the interface itself.
- Web Workers do not work when a page is opened directly from `file://`; the post says a local development server is needed instead.
