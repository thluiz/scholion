---
title: "Let’s Make a Drawing Game with Node.js"
date: '2012-08-24T12:09:42-03:00'
category: webclip
summary: 'The tutorial builds a real-time drawing app with node.js, socket.io, a canvas, and a small server that serves files and relays mouse movement so users can draw together.'
tags: ["node-js", "socket-io", "canvas", "real-time"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Let’s Make a Drawing Game with Node.js | Tutorialzine"
    url: "http://tutorialzine.com/2012/08/nodejs-drawing-game/?utm_source=javascriptweekly&utm_medium=email"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-08/tutorialzine-com--lets-make-a-drawing-game-with-nodejs.md"
    kind: repo
---

The article shows how to build a simple online drawing game with node.js and socket.io. Users draw on a canvas by moving the mouse, and each browser sees the others’ cursors and strokes in real time.

## Reading notes

- node.js is described as an asynchronous web server built on Google’s V8 engine and suited for scalable web services with many simultaneous connections.
- The app uses socket.io as the real-time data channel, with websockets and AJAX long polling, and the example is said to work in modern browsers.
- The client side creates a canvas for drawing and a separate container for mouse pointers.
- The HTML includes the canvas, an instructions block, jQuery, the app script, and /socket.io/socket.io.js served by node.js itself.
- The client script checks for canvas support, connects to the server, and assigns each user a unique id.
- When a moving event arrives, the script creates a cursor element for a new user, moves the cursor, and draws a line if that user is drawing.
- Mouse movement is rate-limited to one socket emit every 30 ms.
- The current user’s drawing is rendered locally with lineTo so the marks become continuous lines instead of separate dots.
- The script removes inactive clients after 10 seconds without updates.
- The server uses http, socket.io, and node-static.
- The server listens on port 8080 and serves the files in the current folder.
- On each mousemove message, the server broadcasts the moving event to every client except the sender.
- The article ends by suggesting possible additions such as different brushes, erasers, colors, shapes, and flags next to cursors.
