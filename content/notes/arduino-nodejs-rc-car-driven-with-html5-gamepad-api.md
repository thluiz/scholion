---
title: "Arduino Node.js RC Car Driven with the HTML5 Gamepad API"
date: '2015-07-24T08:39:11-03:00'
category: webclip
summary: 'The post shows how a browser gamepad can feed steering and pedal data to a Node.js server, which relays it through WebSockets and serial output to an Arduino-driven RC car.'
tags: ["gamepad-api", "nodejs", "arduino", "websockets"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Arduino Node.js RC Car Driven with the HTML5 Gamepad API - Web on Devices"
    url: "http://www.webondevices.com/arduino-nodejs-rc-car-driven-with-html5-gamepad-api/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-07/webondevices-com--arduino-nodejs-rc-car-driven-with-html5-gamepad-api.md"
    kind: repo
---

The post describes a remote-controlled car project built from browser gamepad input, a Node.js server, WebSockets, and Arduino hardware. It starts with reading raw USB controller data in the browser through the HTML5 Gamepad API, then filters that data into JSON and sends it to the server in real time.

## Reading notes

- The browser reads steering wheel, pedals, and buttons through `navigator.getGamepads` or `navigator.webkitGetGamepads`, with extra code for feature detection, connection and disconnection events, and Chrome event handling.
- The gamepad data is compiled into a JSON object and sent to a Node.js server.
- The server uses Express to serve `index.html` and Socket.IO to create a real-time WebSocket connection.
- The browser emits the JSON data through the socket, and the server receives and logs it.
- Node.js then writes the received message to a USB serial port so it can reach the Arduino board.
- The browser cannot access the Arduino serial connection directly because of browser security limits.
- The RC car keeps two motors, one for steering and one for acceleration, after the original radio and motor drive modules were removed.
- The rebuilt system uses an L298n H-bridge, two nRF24l01 antennas, and the original 6V battery pack.
- An Arduino Nano on the car receives wireless messages from an Arduino UNO connected to the MacBook Pro.
- The author says an onboard wireless camera, a stronger battery pack, and more sensors or lights are planned for later.
