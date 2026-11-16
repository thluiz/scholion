---
title: "Aborting a signal: How to cancel an asynchronous task in JavaScript"
date: '2026-11-16T04:29:06+00:00'
category: webclip
summary: 'The article explains how AbortController and AbortSignal let you cancel async work in JavaScript, then shows how to build a cancelable function that handles both live and pre-aborted signals.'
tags: ["javascript", "abortcontroller", "abortsignal"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Aborting a signal: How to cancel an asynchronous task in JavaScript"
    url: "https://ckeditor.com/blog/Aborting-a-signal-how-to-cancel-an-asynchronous-task-in-JavaScript"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/ckeditor-com--aborting-a-signal-how-to-cancel-an-asynchronous-task-in-java.md"
    kind: repo
---

The article explains that JavaScript can cancel asynchronous activity with AbortController and AbortSignal. AbortController is described as a general DOM interface that can be passed to async APIs, and the Fetch API is the official example.

It then shows how to make a custom async function abortable. The function receives a signal, starts a timeout, listens for the abort event, clears the timer, and rejects with a DOMException named AbortError. It also checks signal.aborted at the start so it can fail immediately if the signal was already aborted.

## Reading notes

- AbortController and AbortSignal provide a way to cancel asynchronous activity in JavaScript.
- The solution came from WHATWG after earlier standardization efforts stalled.
- AbortController is part of the DOM, so it is not available in Node.js as an official built-in cancellation API.
- The signal property is an AbortSignal instance with an aborted flag and an abort event.
- Fetch accepts signal in its options and rejects the promise when abortController.abort() is called.
- A custom async function can accept an AbortSignal and use it to cancel its own work.
- In the example, the function starts a timeout, then removes it and rejects the promise when the abort event fires.
- The rejection should use a DOMException with name AbortError.
- If the signal was already aborted before the function receives it, the function should reject immediately after checking signal.aborted.
