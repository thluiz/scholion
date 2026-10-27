---
title: "François Dion: iPhone app with Python"
date: '2013-01-29T09:12:19-03:00'
category: webclip
summary: 'The post shows an iPhone GPS app built as a web application with Brython: HTML and CSS for the interface, Python for the code, and a remote Python script linked from the page.'
tags: ["brython", "python", "iphone", "web-app"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "François Dion: iPhone app with Python"
    url: "http://raspberry-python.blogspot.com/2013/01/iphone-app-with-python.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-01/raspberry-python-blogspot-com--francois-dion-iphone-app-with-python.md"
    kind: repo
---

The post presents an iPhone GPS app written as a web application. It uses HTML and CSS for the interface, while the application logic is written in Python through Brython. The page also notes that the app can be launched from the home screen and that Brython lets the Python code live in a separate remote script.

## Reading notes

- The app launches with a splash screen and works as a web application rather than a native app.
- It can be opened by visiting the Brython gallery URL and adding it to the home screen.
- The code is split between HTML, CSS, and Python, with Brython linking to a remote Python script.
- The HTML sets up the page layout, includes Brython, loads the Python script, and enables the app to behave like a mobile web app.
- The Python code uses geolocation, defines callbacks for successful and failed position tracking, and handles the auto-refresh switch.
- The refresh switch uses `watchPosition` and `clearWatch` to toggle continuous location updates.
- The CSS is not shown in full, but the post says it can be checked in the source and that the iOS-style switch CSS was borrowed from another article.
- The post says the same basic structure can apply to different mobile devices, even if this example is iPhone-specific in style.
