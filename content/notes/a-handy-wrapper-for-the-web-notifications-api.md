---
title: "A handy wrapper for the Web Notifications API"
date: '2026-11-16T08:06:42+00:00'
category: webclip
summary: 'Alex Gibson presents Notify.js, a JavaScript wrapper that simplifies permission requests and Web Notification API events, with extra callbacks, convenience methods, and browser support notes.'
tags: ["web-notifications-api", "javascript", "notifyjs"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "A handy wrapper for the Web Notifications API – Alex Gibson"
    url: "https://web.archive.org/web/20200501014020id_/https://alxgbsn.co.uk/2013/02/20/notify-js-a-handy-wrapper-for-the-web-notifications-api/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--a-handy-wrapper-for-the-web-notifications-api.md"
    kind: repo
---

Notify.js is a JavaScript plugin that wraps the Web Notifications API so it is easier to reuse across projects. The page says it simplifies permission requests and notification events, and adds a few callbacks and convenience methods.

## Reading notes

- The author says the Web Notifications API is supported in Chrome, Safari 6, and recently in Firefox.
- It creates growl-style notifications for web applications and integrates with Notification Centre on OSX.
- Notify.js is described as a simplified wrapper for the API.
- It aims to simplify permission requests and related Web Notification API events.
- It also provides extra callbacks and convenience methods.
- A notification is created with a new `Notify` instance, using a required `title` and optional settings.
- The example passes `body` and `notifyShow`, then calls `show()` to display the notification.
- Required parameters include `title` as the notification title.
- Optional parameters include `body`, `icon`, `tag`, `timeout`, and callbacks for show, close, click, error, permission granted, and permission denied.
- Static methods include `Notify.needsPermission()`, `Notify.requestPermission()`, and `Notify.isSupported()`.
- Chrome does not allow permission requests on page load; it needs a user interaction such as a click.
- Testing uses Node and the Karma test runner, with `npm install -g karma` and `npm test` for a single pass in Firefox.
- The page points to the GitHub readme for current browser support details.
