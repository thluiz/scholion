---
title: "GitHub - danhper/pushex: Push notifications for Elixir"
date: '2026-11-16T03:21:22+00:00'
category: webclip
summary: 'Pushex is an Elixir library for sending push notifications with a common API for iOS and Android, async sending, multiple apps, response handling, and a sandbox for testing.'
tags: ["elixir", "push-notifications", "gcm", "apns"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "GitHub - danhper/pushex: Push notifications for Elixir"
    url: "https://github.com/danhper/pushex"
    kind: repo
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/github-com--pushex-push-notifications-for-elixir.md"
    kind: repo
---

Pushex is a library for sending push notifications with Elixir. The page says it aims for an easy async API, one common API for iOS and Android, support for multiple applications, proper error and response handling, and a sandbox mode for testing.

## Reading notes

- The library currently works with GCM and APNS.
- APNS delegates to apns4ex for now, with a possible switch to the HTTP2 API in a later version.
- The API is still subject to change, with a minor version bump for each change.
- Installation uses mix.exs dependencies and adding :pushex to applications.
- Basic usage creates a Pushex.GCM.App and calls Pushex.push with a title, body, destination, and app.
- Configuration can define multiple apps for gcm and apns, including default_app entries.
- The push function is async and returns only a reference.
- The same message can be sent to both platforms by mixing common fields with apns and gcm payloads.
- Extra options such as priority can be passed in the keyword list.
- When to is an array, it is converted to registration_ids for the request.
- App lookup can be overridden with a custom module that implements Pushex.AppManager.
- Response handling can be implemented with Pushex.EventHandler and :gen_event.
- In sandbox mode, messages are stored in Pushex.Sandbox and returned to the sending process instead of being sent to GCM or APNS.
- Because sending is asynchronous, the sandbox notes that notification order is not guaranteed.
