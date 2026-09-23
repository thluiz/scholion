---
url: "https://x.com/paularambles/status/2032124088890900669?s=12&utm_source=tldrnewsletter"
captured_at: "2026-03-17T09:43:44+00:00"
title: "\"paula\" on X: \"The Death of \"Good Enough\"\""
domain: "x-com"
---

paula (@paularambles)

The Death of "Good Enough"

This animation took three minutes to build.

Three minutes, from a single prompt to a working animation with tokens rotating in 3D space, natural physics, and clean integration with our app's state management.

A few months ago, this wouldn't have existed. It obviously was possible, but it most likely was never going to get prioritized. When you're an iOS engineer at a small startup that ships on a daily basis, you don't get a sprint to build a playful celebration animation. You get a concept, a deadline, and the animation gets cut, or worse, it ships as a fade-in and everyone agrees that's fine. And over time you end up with the version of your app where everything works but nothing delights.

That era is ending. Shipping no longer requires sacrificing craft for speed.

The three-minute animation

I'm an iOS engineer at Tolan. We recently added in-app currency, in the form of tokens, and we wanted a little celebratory moment, something that felt fun and alive.

In a previous life, here's how that would have gone: I'd look at the timeline, realize I didn't have half a day to hand-craft a SpriteKit animation, and I'd ship a simple counter increment. Maybe a scale bounce if I was feeling generous. Good enough.

But this time was different.

I started with a few token assets and a general sense of the vibe we wanted.

Here's the prompt I gave Claude Code:

"If users' tokens have incremented, we want to show an animation leading into their token counter. Use the AnimationToken1, AnimationToken2, AnimationToken3, AnimationToken4, and AnimationToken5 assets to create a SpriteKit animation that animates the tokens flying into the counter."

That was it. The whole brief. Each token follows a randomized Bezier curve with staggered timing, rotation, and scale, so it feels organic. Claude built the full thing: fade in, curved flight paths, 3D rotation, fade out, cleanup. It even integrated it into the right feature. First try.

It's cute! And it would have never existed if building it still cost what it used to cost.

The one-hour animation I never would have attempted

The token animation is a good example of speed. But here's a better example of ambition.

Recently we built a feature that lets users pick daily intentions, small activities they want to achieve on that day. We wanted the whole daily loop to feel as good as possible, and part of that meant that when you selected an intention, we wanted to fold it up like a piece of paper and fly it away, like a note you're saving for later.

An origami-like fold animation. With 3D perspective. On a card with live content.

A year ago we probably wouldn't have even attempted this. It's not a matter of ability, I could learn CATransform3D and figure out perspective projection and back-face compositing. But it would have taken a day or more, and at a startup where you want something in your users' hands by tomorrow, that math doesn't work. So the card would have faded out. Dissolved. Slid off screen. Good enough.

Instead, I spent about an hour playing around with Claude Code: prompting, tweaking, iterating on the feel. If the fold animation felt wrong, I'd try something else. If the easing was off, I'd describe what I wanted differently and see what came back. It felt more like play rather than painstaking engineering toward a spec. Here's what we shipped:

The animation is a four-step sequence: the card splits in half and folds right-to-left with a 3D perspective transform, then folds bottom-to-top, then the folded card flies up to a target icon, then fades out. There's a back-face swap timed to the visual midpoint of the fold, progressive shadow overlays that create the illusion of depth, and careful easing so the whole thing feels physical.

This is the kind of animation you see in polished consumer apps from teams with dedicated motion designers. I built it at a startup, by myself, in an hour, by describing what I wanted and iterating on the result.

What this changes

Every app you use is full of moments where someone decided "good enough" was good enough, not necessarily because they lacked taste, but because they lacked time. So we've ended up with fade-outs where there could have been origami.

We've always been told "don't let perfect be the enemy of good." That made sense when "perfect" cost a sprint, and "good" cost an afternoon, but when "perfect" costs an hour, and "good" costs five minutes, maybe it's time to retire that saying. We don't have to agonize over whether something is worth attempting, instead we can just try it, and if it doesn't work, we can try something else. We always wanted to build the delightful version, and now we can, while having the most fun we've had building software.
