---
title: "Getting started with Kranium.js"
date: '2012-06-09T02:37:33-03:00'
category: webclip
summary: 'The post introduces Kranium.js as a Titanium Mobile framework that brings web development techniques into app work, simplifying UI creation, styling, querying, testing, and installation.'
tags: ["kranium-js", "titanium-mobile", "mobile-frameworks"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Getting started with Kranium.js – a brilliant framework for Titanium Mobile – Adam Renklint, application developer"
    url: "http://adamrenklint.com/guides/getting-started-with-kranium-js-a-brilliant-framework-for-titanium-mobile"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-06/adamrenklint-com--getting-started-with-kranium-js.md"
    kind: repo
---

Kranium.js is presented as a Titanium Mobile framework built from web development techniques. The post says it speeds up development and styling, helps with prototyping and production, and aims to make app code more modular and readable.

## Reading notes

- It simplifies UI component creation and promotes a clean modular pattern for mobile apps.
- It makes deep object structures easier to read and write with a compact syntax.
- Custom components live in a kui folder and can be lazily autoloaded when needed.
- The author recommends a strong namespace pattern and gives ARLoginStatusLabel as an example.
- It ships with a CSS port for Titanium Mobile.
- kranium init and kranium watch can start an auto-compiler service for Sass, LESS, and CoffeeScript, with optional live in-app updating through sockets.
- It uses a modified Sizzle engine and emulates the DOM in a natural way.
- Pseudo selector support is still missing, and not all Sizzle filter methods are implemented yet.
- It includes Jasmine BDD integration and a localhost console.
- Installation requires NodeJS, the kranium command line tool, and the demo application.
