---
title: "Introducing Incident Context and Incident Notes"
date: '2019-06-30T12:44:12+00:00'
category: webclip
summary: 'AppSignal adds more context to incident pages by showing other errors, performance issues, and active anomaly alerts, and lets users leave notes for colleagues or future reference.'
tags: ["incident-context", "incident-notes", "errors", "performance"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Introducing Incident Context and Incident Notes"
    url: "https://blog.appsignal.com/2019/06/25/introducing-context-incident-notes.html?utm_source=boostedblogpost&utm_medium=twitter&utm_campaign=product-incident-context-notes-02-organic"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/blog-appsignal-com--introducing-incident-context-and-incident-notes.md"
    kind: repo
---

AppSignal is adding two improvements to its Incident page for errors and performance incidents. The page now includes more context around a faulty request, and it also lets users add notes to incidents.

## Reading notes

- The Incident page is one of the most used pages in the application, and it is where users land from a notification.
- Incident context now shows whether other errors occurred, what performance issues were happening, and whether any Anomaly Detection Alerts were active at the same time.
- This extra context helps users see whether the root cause may be elsewhere or whether multiple incidents are related.
- Users can now leave notes on Error or Performance incidents for colleagues or for their future selves.
- The notes are meant to store technical and historical knowledge at the point where someone is fixing the issue.
- The note field can be used to record how to solve the incident or the steps taken to help prevent it from happening again.
