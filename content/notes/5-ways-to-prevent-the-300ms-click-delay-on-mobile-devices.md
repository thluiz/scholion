---
title: "5 Ways to Prevent the 300ms Click Delay on Mobile Devices"
date: '2015-04-02T19:33:11-03:00'
category: webclip
summary: 'The article explains why mobile browsers wait 300ms after taps and compares fixes: viewport settings, PointerEvents, touchend handlers, and libraries like FastClick and Tappy, while noting accessibility and browser limits.'
tags: ["mobile-web", "touch-events", "pointerevents", "fastclick"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "5 Ways to Prevent the 300ms Click Delay on Mobile Devices"
    url: "http://www.sitepoint.com/5-ways-prevent-300ms-click-delay-mobile-devices/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-04/sitepoint-com--5-ways-to-prevent-the-300ms-click-delay-on-mobile-devices.md"
    kind: repo
---

The article says many touch-based mobile browsers wait 300ms before firing the click handler because of double-tap zoom behavior. It treats that delay as one reason web apps can feel slower than native ones, then compares several ways to remove or reduce it.

The options depend on the browser and the kind of interface. Disabling zooming can remove the delay in Chrome and Firefox on Android, but it breaks on Safari and raises accessibility concerns. Setting the viewport to device-width helps in Chrome 32+ and is often already part of responsive sites. PointerEvents and `touch-action: manipulation` reduce the delay on supported browsers, while `touchend` handlers can work for touch-only interfaces. The article also mentions FastClick and Tappy as helper libraries, and warns that too many event handlers can hurt performance.

## Reading notes

- Most touch-based mobile browsers wait 300ms between a tap and the click handler because of double-tap zoom behavior.
- The delay was sensible before responsive web design and multi-touch pinch zooming became common.
- Content-only sites with standard navigation may not be affected much because users spend more time reading than tapping controls.
- Chrome and Firefox on Android can skip the wait when zooming is disabled with viewport settings in the HTML head.
- Disabling zooming fails on Safari and creates accessibility concerns for users with visual or motor impairments.
- In Chrome 32+, setting the viewport width to device-width disables double-tap zooming.
- Microsoft’s PointerEvents specification addresses touch issues, and `pointerup` is not fired when the user is scrolling.
- The `touch-action: manipulation` property can remove the delay on specific elements or the whole document without disabling pinch zooming.
- `touchend` fires instantly, but standard pages still need click handling for non-touch devices and for cases where touch gestures become scrolling.
- FastClick and Tappy are presented as small libraries that normalize tap handling when browser support is not enough.
- Adding event handlers to multiple elements can hurt performance and may be worse than the delay itself.
