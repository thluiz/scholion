---
title: "10 years of Apple text editor solo dev"
date: "2026-09-23T13:44:43+01:00"
category: webclip
has_commentary: false
summary: "A decade building Paper, a native Mac/iOS text editor, alone: why native beat Electron, why cosmetic-only paid features, why one release a month."
tags:
  - indie-software
  - product-design
  - pricing
sources:
  - title: "10 years of Apple text editor solo dev"
    url: "https://paper.pro/dev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-04/paper-pro--10-years-of-apple-text-editor-solo-dev.md"
    kind: repo
---

Mihhail Lapushkin, a web developer with no prior Apple experience, spent ten years building Paper, a native text editor for Mac and iOS, alone. He avoided Electron, stayed on Objective-C after 2015, and kept the app going for a decade on a fixed monthly release cadence.

## Fichamento

- Chose native development over Electron to get a lighter, faster app and finer control over text handling, even though it meant learning Xcode, AppKit, and Objective-C from zero.
- Picked Objective-C over Swift in 2015 after comparing compiled app sizes: an empty Swift project embedded a 5MB runtime, the Objective-C equivalent stayed under 100KB.
- Paper has no third-party dependencies. The Markdown parser, the `.docx` exporter, and every UI component are custom-built, which cost weeks of work but produced a codebase tailored exactly to the app's needs.
- The product philosophy separates a clean "default path" from feature-rich "fringes" hidden under the Option key, aiming to keep the core app as minimal as it was on launch day.
- Paid features are cosmetic (colors, visual flourishes); functional features stay free. Pro features remain usable during an unlimited trial, with a nag popup tied to characters typed while using a Pro feature.
- Pricing moved from one-time payments ($5, tested up to $200) to subscriptions, which the author expected to fail for such a simple app and didn't.
- In-app support chat, built after Microsoft discontinued HockeyApp, became the main source of the product roadmap, at one point driving 90% of new features.
- Releases follow a fixed monthly cadence: one flagship feature per release note, written as a short letter to the user, with bug fixes folded in unannounced.
