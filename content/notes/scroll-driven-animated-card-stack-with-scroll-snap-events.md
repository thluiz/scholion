---
title: "Scroll-driven animated card stack with scroll snap events"
date: '2026-09-25T21:50:01+01:00'
category: webclip
summary: 'Paul Noble’s card stack demo uses an invisible scroller, a ScrollTimeline, scroll snapping, and snap events to animate the active card differently from the others.'
tags: ["scroll-driven-animations", "scroll-snap", "css-animations"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Scroll-driven animated card stack with scroll snap events"
    url: "https://www.bram.us/2024/10/13/scroll-driven-animated-card-stack-with-scroll-snap-events/?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/bram-us--scroll-driven-animated-card-stack-with-scroll-snap-events.md"
    kind: repo
---

The post breaks down Paul Noble’s card stack demo and then revisits it with a different implementation. The original uses an invisible scroller on top of the cards, hoists its ScrollTimeline to the body with timeline-scope, and uses scroll snapping so a card stays centered.

It also uses the new scrollsnapchange event to update data-active-index on the main element. That state controls separate animations for the snapped card and the non-snapped cards. The remix tries to share keyframes through ViewTimeline and animation-range, and adds a fallback for browsers without Snap Events.

## Reading notes

- An invisible scroller sits over the card stack and drives a ScrollTimeline named --scroll-timeline.
- timeline-scope on body lets .card-stack use that timeline.
- CSS scroll snapping keeps the cards centered.
- scrollsnapchange updates the markup with the snapped card through data-active-index.
- The snapped card gets an active 3D rotation animation.
- The other cards get an inactive animation that rotates each card around its base.
- The remix uses shared keyframes with ViewTimeline on the linked .scroll-item.
- animation-range limits when each animation runs.
- The rewritten scrollSnapChange logic uses event.snapTargetInline.
- IntersectionObserver is used as a fallback where Snap Events are not supported.
