---
title: "Connection Speed Detection with Javascript"
date: '2012-01-16T13:51:17-03:00'
category: webclip
summary: 'The article shows how to estimate a user’s connection speed in JavaScript by timing an image load, first with one test and then with several trials to average the result.'
tags: ["javascript", "connection-speed", "image-loading", "closures"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Alex Le’s Blog » Blog Archive » Connection Speed Detection with Javascript"
    url: "http://alexle.net/archives/257"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-01/alexle-net--connection-speed-detection-with-javascript.md"
    kind: repo
---

The page explains a JavaScript way to estimate connection speed by loading an image and measuring how long the browser takes to finish it. It presents a simple version and a multi-trial version, both using a known image size and the onload event to calculate Kbps and KBps.

## Reading notes

- The technique uses an image, a small JavaScript snippet, and no third-party library.
- The browser starts a timer before loading the image and stops it when the image’s onload event fires.
- The simple version runs once and returns runTime, Kbps, and KBps.
- The code appends a random query value to the image URL to avoid caching.
- The article uses a closure variable named me so the onload handler can access the SpeedTest object’s properties.
- The sample usage defines onStart and onEnd callbacks, and onEnd can branch on the measured speed.
- The multi-trial version runs the test several times, stores each result, and averages the runtimes.
- The article says that multiple runs reduce errors caused by DNS lookup, network latency, and browser overhead.
- The multi-trial version stores the user’s onEnd callback on the SpeedTest object and calls it after the last trial.
- The page ends by offering a zip package with the code and test image.
