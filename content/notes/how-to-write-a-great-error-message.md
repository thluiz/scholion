---
title: "How to write a great error message"
date: '2025-09-01T16:13:03+00:00'
category: webclip
summary: 'The article argues that good error messages are clear, specific, actionable, and written in plain language. It criticizes vague alerts, unnecessary interruptions, and defaults that could be handled without modal dialogs.'
tags: ["error-messages", "user-interface", "ux-writing", "alerts"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to write a great error message"
    url: "https://medium.com/@thomasfuchs/how-to-write-an-error-message-883718173322"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-09/medium-com--how-to-write-a-great-error-message.md"
    kind: repo
---

The article argues that error messages should explain what happened, why it happened, and what the user can do next. It says copy in an app is not secondary work and should be treated as part of product quality and interface design.

It criticizes vague or intrusive alerts from Windows Phone, Google Chrome, Photoshop, Twitter, and Postmates. It recommends avoiding alerts for minor issues, including enough context, using a friendly non-technical tone, and preventing errors when possible instead of showing a dialog.

## Reading notes

- Apple’s Human Interface Guidelines say alerts should describe the situation clearly and succinctly, add informative text with consequences and a solution or alternative, and use the user’s vocabulary.
- Writing copy in an app is not something to do on the side; it matters as much as correct app behavior and an efficient interface.
- “We are currently unable to check for updates” is too vague because it does not explain why the check failed or what the user should do.
- The Windows Phone update issue was caused by an incorrect phone clock, which broke SSL certificate validation.
- A better message for that case would mention security, the incorrect time and date, and the need to check settings and try again.
- Asking for location permission can make sense for search, but it should not use operating-system level alerts meant for serious problems.
- An obscure Photoshop setting should default to cancel instead of requiring a modal alert.
- One alternative is a non-modal bar that explains the setting and lets the user change the default.
- The best error message is the one that never shows up.
- Twitter could explain the attachment problem before upload or resize the image on the client before sending.
- The Postmates alert is not useful if it does not even say what it is about.
- The Windows Phone update problem could be avoided if the operating system set time and date automatically.
- Chrome could use a banner instead of interrupting users with an alert for location permission.
- Photoshop should ship with sane defaults and use undoable banners or tutorials for customization.
- The three most important points are to avoid abusing alerts, include enough context, and use a friendly, non-technical, non-threatening tone.
- The article recommends testing error messages with a non-technical person and asking them to explain the message back.
