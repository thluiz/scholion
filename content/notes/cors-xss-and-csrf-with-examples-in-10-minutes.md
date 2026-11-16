---
title: "CORS, XSS and CSRF with examples in 10 minutes"
date: '2026-11-16T19:18:08+00:00'
category: webclip
summary: 'The article introduces CORS, XSS, and CSRF, shows how each attack works, and explains practical defenses such as server headers, input handling, CSRF tokens, and SameSite cookies.'
tags: ["cors", "xss", "csrf", "web-security"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "CORS, XSS and CSRF with examples in 10 minutes"
    url: "https://dev.to/maleta/cors-xss-and-csrf-with-examples-in-10-minutes-35k3"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--cors-xss-and-csrf-with-examples-in-10-minutes.md"
    kind: repo
---

The article frames CORS, XSS, and CSRF as core web security topics and explains how they affect browser requests, user input, and authenticated actions. It also points readers to common prevention methods, including server-side configuration, validation, escaping, sanitization, CSRF tokens, and SameSite cookies.

## Reading notes

- CORS is described as a browser security feature that controls which origins can access resources through AJAX, and it is disabled by default unless the server enables it for specific domains.
- In development, a VueJS app on one localhost port talking to a NodeJS server on another port can trigger a CORS error because the origins differ.
- The article suggests using a devServer proxy in VueJS development mode and handling OPTIONS requests in production with the right Access-Control-Allow-Origin and Access-Control-Allow-Methods headers.
- XSS is presented as an injection attack in which malicious script is inserted into a trusted website.
- The article separates XSS into stored, reflected, and DOM-based variants.
- Stored XSS is tied to unprotected and unsanitized user input that is saved in a database and later shown to other users.
- Reflected XSS uses unprotected and unsanitized values from URLs that are inserted directly into web pages.
- DOM-based XSS is similar to reflected XSS, but the malicious part of the URL never reaches the server and is handled by client-side code.
- The article says every user-entered value should be treated as untrusted data and processed before use on both server and client.
- It lists string validation, string escaping, and string sanitization as the main ways to handle untrusted data.
- Escaping replaces special characters such as <, >, &, and " with HTML entity equivalents.
- Sanitization is described as allowing some HTML tags while removing others, and the article warns that this approach is resource expensive and considered harmful.
- CSRF is described as a way to make a browser perform an unwanted action on a trusted site where the user is authenticated.
- The example uses an authenticated stock exchange app where a forged request can trigger a withdrawal because the browser sends authentication data automatically.
- The main defense presented is a CSRF token that is generated, stored, returned to the client, sent with state-changing requests, and checked by the server.
- The article also mentions that SameSite session cookies can be used with modern browsers.
- It notes that XSS breaks CSRF protection because XHR responses can be processed by malicious script.
- The bonus section points to Samy’s MySpace worm as an example of XSS bypassing CSRF defense.
