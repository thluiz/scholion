---
title: "Building A Simple AI Chatbot With Web Speech API And Node.js"
date: '2026-09-27T00:37:49+01:00'
category: webclip
summary: 'Tutorial for building a browser voice chat app with Web Speech API, Node.js, Socket.IO, and API.AI, using speech recognition for input and speech synthesis for the reply.'
tags: ["web-speech-api", "node-js", "socket-io", "api-ai"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Building A Simple AI Chatbot With Web Speech API And Node.js — Smashing Magazine"
    url: "https://www.smashingmagazine.com/2017/08/ai-chatbot-web-speech-api-node-js/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/smashingmagazine-com--building-a-simple-ai-chatbot-with-web-speech-api-node-js.md"
    kind: repo
---

The article explains how to build a simple browser chatbot that listens to spoken input, sends the transcript to API.AI, and speaks the reply back with the Web Speech API. It uses Node.js and Socket.IO to move messages between the browser and server, and notes that the app depends on browser support for speech recognition and synthesis.

## Reading notes

- The app uses the Web Speech API to create a voice chat interface with a minimal visual UI.
- The flow has three steps: capture speech with SpeechRecognition, send the text to a natural-language-processing API, and read the response with SpeechSynthesis.
- The tutorial assumes Node.js and basic JavaScript knowledge.
- The server setup uses Express to serve the app locally.
- Socket.IO is used for real-time, bidirectional communication between browser and server.
- The front end starts speech recognition when the user clicks a button.
- SpeechRecognition returns the user’s spoken text as a result event, along with a confidence value.
- API.AI is used as the conversational layer, with the Small Talk preset enabled.
- The Node.js SDK sends the text to API.AI and receives the reply text.
- The browser speaks the reply through SpeechSynthesisUtterance and speechSynthesis.speak().
- The browser asks for microphone permission the first time speech input is used.
- The article notes that Web Speech API support is still experimental and uneven across browsers.
