---
title: "PWA on iOS - Current Status & Limitations for Users [2025]"
date: '2020-02-22T12:11:42+00:00'
category: webclip
summary: 'The page says iOS PWAs have improved since iOS 13, with better install flow, dark mode, motion sensors, push notifications, background support, and inspection tools, but still depend on Safari and keep user-facing limits.'
tags: ["pwa", "ios", "safari", "progressive-web-apps"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "PWA on iOS - Current Status & Limitations for Users [2025]"
    url: "https://brainhub.eu/blog/pwa-on-ios-13"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/brainhub-eu--pwa-on-ios-current-status-limitations-2025.md"
    kind: repo
---

The page presents iOS PWAs as slowly improving, not fully equivalent to native apps. It highlights newer support for home screen installation, dark mode, motion sensor permissions, iPadOS behavior, push notifications, background running, and debugging tools, while keeping Safari as the main constraint.

## Reading notes

- iOS PWAs can be added to the home screen, but Safari does not show an automatic install prompt.
- The Share Sheet redesign and the apple-touch-icon meta tag help the home screen installation flow.
- Dark Mode is supported through prefers-color-scheme, though the app icon cannot change dynamically with the theme.
- On iOS 13 and later, motion sensors require explicit user permission.
- iPadOS gives Safari a desktop-class browsing experience, but PWAs do not automatically adapt when moving in or out of Split View.
- Apple improved installability, standalone and full-screen modes, storage quotas, security, privacy, and accessibility support.
- Pointer Events help PWAs detect finger, Apple Pencil, or mouse input, especially on iPadOS.
- PWAs on iOS are inspectable, and Safari Web Inspector supports remote debugging.
- Background running is more capable than before, but still limited by iOS restrictions.
- iOS 16.4 added push notification support for PWAs, and it requires home screen installation and permission.
- The page says Apple briefly planned to reduce PWA capabilities in the EU under DMA pressure, then restored full support.
- User limitations include manual installation, uneven device support, limited access to some hardware features, limited offline functionality, Safari dependence, and weaker App Store discoverability.
