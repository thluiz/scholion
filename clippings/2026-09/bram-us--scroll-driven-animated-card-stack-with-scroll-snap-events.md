---
url: "https://www.bram.us/2024/10/13/scroll-driven-animated-card-stack-with-scroll-snap-events/?ref=dailydev"
captured_at: "2026-09-25T21:50:01+01:00"
title: "Scroll-driven animated card stack with scroll snap events"
domain: "bram-us"
---

Video Player

Recording of Paul’s demo

Dissecting and reworking a very nice demo by Paul Noble.

~

### Card Stack Demo

Paul Noble created [an AMAZING scroll-driven animations demo](https://codepen.io/paulnoble/full/gOVPedz) in which you can drag cards from a card stack. As he [describes it](https://twitter.com/paul_uiux/status/1841437472711938322):

> Card stack using scroll-driven animation w/ snapping. Just a few lines of JS, zero dependencies.

Try it out (in Chrome) right here:

The logic/math used for the stack is based on [this thread by Nate Smith](https://twitter.com/nasm423/status/1795133452016054401). You can also find instructions in this two parter: [Creating the iMessage Card Stack Animation: Part 1 — The Timeline Design](https://lorenzomigliorero.medium.com/creating-the-imessage-cardstack-animation-part-1-the-timeline-design-5a4375c3b0c5) and [Creating the iMessage Card Stack Animation: Part 2 — The Interactive Layer](https://lorenzomigliorero.medium.com/creating-the-imessage-cardstack-animation-part-2-the-interactive-layer-10392405e858).

~

~

### Dissecting the code

On social media I already shared ([Twitter](https://twitter.com/bramus/status/1845234440278245446), [Mastodon](https://front-end.social/@bramus/113270818264746037)) how Paul built it:

Invisible Scroller

The first clever thing Paul is doing there is using an invisible scroller laid on top of the stack of cards. This scroller gets a ScrollTimeline named `--scroll-timeline` attached to it.

Hoisting the Timeline

To make the `.card-stack` see the `--scroll-timeline`, it gets hoisted using `timeline-scope` on the `body`. Any child of the `body` – including `.card-stack` – can therefore use that `--scroll-timeline`.

Scroll-Snapping

To make the cards always show at the center, CSS scroll-snapping is used.

Snap Events

In his demo, Paul also uses [the new `scrollsnapchange` event](https://developer.chrome.com/blog/scroll-snap-events) to let the markup know which card has snapped. This is propagated through the `data-active-index` attribute on the `main` element.

Custom animations based on which card has snapped

Based on the `data-active-index` attribute, different animations are attached to the cards: the snapped card gets an active animation – which rotates in 3D around the stack – and the non-snapped cards get an inactive animation – which rotates the card around its base.

~

### Remixing the demo

Paul’s demo is amazing but also hard to read because the Sass code uses quite some some math to generate keyframes for each card. As hinted on social media I was quite sure that the effect can also be done using shared keyframes for each card. To attach the keyframes to a single `.card` a ViewTimeline on the linked `.scroll-item` can be used, and using `animation-range` it’s possible to limit when the animation should run.

Yesterday evening I put my money where my mouth is and took my idea for a spin. The result is not 100% perfect – there are some 3D stacking issue, most likely I need to tweak the `animation-range`s a bit more – but the result comes pretty close to the original:

While at it, I also reworked the `scrollSnapChange` logic to use `event.snapTargetInline` and by also providing a fallback using `IntersectionObserver` in browsers with no support for the Snap Events.

~

![](https://secure.gravatar.com/avatar/f2f3975d755fc2711e29e9795df804bcd686bbb770d0d947eba58f3478942b6d?s=128&d=mm&r=g)

Bramus is a frontend web developer from Belgium, working as a Chrome Developer Relations Engineer at Google. From the moment he discovered view-source at the age of 14 _(way back in 1997)_, he fell in love with the web and has been tinkering with it ever since _[(more …)](https://www.bram.us/about)_

## Post navigation
