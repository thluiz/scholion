---
title: "Tutorial: Build your own Google TV Using RaspberryPi, NodeJS and Socket.io"
date: '2014-10-16T08:34:35-03:00'
category: webclip
summary: 'The tutorial shows how to build a proof-of-concept Google TV with Raspberry Pi, Raspbian, Node.js, Socket.io, Chromium, YouTube-dl, and OMXPlayer, then connect a remote and screen through WebSockets.'
tags: ["raspberry-pi", "nodejs", "socket-io", "websockets"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Tutorial: Build your own Google TV Using RaspberryPi, NodeJS and Socket.io - Codementor"
    url: "https://www.codementor.io/nodejs-tutorial/build-google-tv-raspberrypi-nodejs-socket-io?utm_term=google-tv-nodejs-raspberrypi&"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-10/codementor-io--build-google-tv-raspberrypi-nodejs-socket-io.md"
    kind: repo
---

The article outlines a proof-of-concept Google TV built with open source tools on a Raspberry Pi. It uses Raspbian, Node.js, Socket.io, Chromium, YouTube-dl, OMXPlayer, QuoJS, HTML5, CSS3, JavaScript, Moustache, and the YouTube API, and it separates the project into setup, shell commands, back-end, and front-end work.

## Reading notes

- The project is described as a proof of concept, not as an actual Google TV replica.
- The hardware base is Raspberry Pi.
- The software stack includes Raspbian, Node.js, Socket.io, Express, Omxcontrol, Chromium, OMXPlayer, YouTube-dl, QuoJS, HTML5, CSS3, JavaScript, Moustache, and the YouTube API.
- The setup section covers installing Raspbian and Node.js, Chromium, fonts, and YouTube-dl.
- The tutorial notes that streaming YouTube in Chromium on the Raspberry Pi is very slow because the videos are not rendered on the GPU.
- YouTube-dl is used as an alternative because it downloads the video first and OMXPlayer renders it on the GPU.
- The shell section shows commands for setting DISPLAY, testing Chromium in kiosk mode, testing YouTube-dl, and playing downloaded videos with OMXPlayer.
- The back-end is a simple Express server with routes for index.html and remote.html.
- npm install is used after defining dependencies in package.json.
- The article mentions running the Node app in the background with node app.js &.
- Socket.io is added to provide realtime connectivity across browsers by choosing the most capable transport at runtime.
- The server keeps one socket for the screen and another for the remote.
- The remote and screen clients both connect through socket.io, and the remote sends control events.
- The server can receive control actions such as tap, swipeLeft, and swipeRight and forward them to the screen socket.
- The video flow listens for a play action, downloads the YouTube video with youtube-dl, then starts it with omx.start().
- The front-end section points to Google’s design guidance for TV interfaces.
- QuoJS is used for swipe gestures on the mobile remote.
- The article also shows mobile web app meta tags and icons for an iPhone-style native feel.
- The project is marked as a work in progress and links to the source code on GitHub.
