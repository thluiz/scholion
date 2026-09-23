---
title: "A Greyscale iPhone Setup that Works in Everyday Life"
date: "2026-09-23T15:34:18+01:00"
category: webclip
summary: "Fabian Hemmert keeps his iPhone in greyscale by default and uses per-app Shortcuts automations to re-enable colour only where it does real work, like Maps or Camera."
tags:
  - digital-minimalism
  - ios-shortcuts
  - attention
  - low-dopamine
has_commentary: false
sources:
  - title: "A Greyscale iPhone Setup that Works in Everyday Life ⋅ Prof. Dr.-Ing. Fabian Hemmert"
    url: "https://www.fabianhemmert.com/opinions/a-greyscale-iphone-setup-that-works-in-everyday-life?utm_source=tldrnewsletter"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-06/fabianhemmert-com--greyscale-iphone-setup-that-works-in-everyday-life.md"
    kind: repo
---

Fabian Hemmert likes what a greyscale phone does to his attention: it makes the device less attractive, so he spends less time on it. It was a practical problem, though: some apps genuinely need colour, so he kept switching back to colour mode and forgetting to switch back, which defeated the setup entirely.

His fix is a pair of iPhone Shortcuts, "Colour" and "Greyscale," wired to automations that fire when specific apps open or close. Colour comes back only for the handful of apps where it carries real information.

## Fichamento

- Greyscale mode has a real usability cost: reading a map's route, for instance, gets noticeably harder without colour.
- The automations trigger on app open and app close, and Hemmert stresses adding the "close" trigger too, or the phone stays in colour mode after you leave the app.
- His colour-enabled list: Camera, Photos, Maps, a to-do app, and Amazon. In these, colour serves clarity or a specific task.
- He runs 12 apps that re-enable greyscale against 11 that enable colour. The extra one is WhatsApp, set as a safety fallback: closing WhatsApp resets the phone to greyscale even if some other automation failed to fire, since locking the phone doesn't count as "closing" an app for Shortcuts' purposes.
- A Siri voice command tied to the "Colour" shortcut works as a manual override for one-off cases, like checking a photo inside WhatsApp.
- He flags a gotcha: the iPhone's built-in accessibility greyscale toggle (triple-click the lock button) is a separate setting from the Shortcuts-based one, and running both can leave the phone stuck in greyscale until you find which layer is active.
