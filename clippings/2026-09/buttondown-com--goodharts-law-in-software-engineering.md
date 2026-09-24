---
url: "https://buttondown.com/hillelwayne/archive/goodharts-law-in-software-engineering/?ref=dailydev"
captured_at: "2026-09-24T23:07:08+01:00"
title: "Goodhart's Law in Software Engineering"
domain: "buttondown-com"
---

### Blog Hiatus

You might have noticed I haven't been updating my website. I haven't even _looked_ at any of my drafts for the past three months. All that time is instead going into _Logic for Programmers_. I'll get back to the site when that's done or in 2025, whichever comes first. Newsletter and [Patreon](https://www.patreon.com/hillelwayne) will still get regular updates.

(As a comparison, the book is now 22k words. That's like 11 blog posts!)

## Goodhart's Law in Software Engineering

I recently got into an argument with some people about whether small functions were _mostly_ a good idea or _always 100%_ a good idea, and it reminded me a lot about [Goodhart's Law](https://en.wikipedia.org/wiki/Goodhart%27s_law):

> When a measure becomes a target, it ceases to be a good measure.

The _weak_ version of this is that people have perverse incentives to game the metrics. If your metric is "number of bugs in the bug tracker", people will start spuriously closing bugs just to get the number down.

The _strong_ version of the law is that even 100% honest pursuit of a metric, taken far enough, is harmful to your goals, and this is an inescapable consequence of the difference between metrics and values. We have metrics in the first place because what we actually _care about_ is nonquantifiable. There's some _thing_ we want more of, but we have no way of directly measuring that thing. We _can_ measure something that looks like a rough approximation for our goal. But it's _not_ our goal, and if we replace the metric with the goal, we start taking actions that favor the metric over the goal.

Say we want more reliable software. How do you measure "reliability"? You can't. But you _can_ measure the number of bugs in the bug tracker, because fewer open bugs roughly means more reliability. **This is not the same thing**. I've seen bugs fixed in ways that made the system _less_ reliable, but not in ways that translated into tracked bugs.

I am a firm believer in the strong version of Goodhart's law. Mostly because of this:

![A peacock with its feathers out. The peacock is scremming](https://assets.buttondown.email/images/2573503d-bc57-49ce-aa26-9d399d801118.jpg?w=960&fit=max)

What does a peahen look for in a mate? A male with maximum fitness. What's a metric that approximates fitness? How nice the plumage is, because nicer plumage = more calories energy to waste on plumage.[1](#fn:peacock) But that only _approximates_ fitness, and over generations the plumage itself becomes the point at the cost of overall bird fitness. Sexual selection is Goodhart's law in action.

If the blind watchmaker can fall for Goodhart, people can too.

### Examples in Engineering

Goodhart's law is a warning for pointy-haired bosses who up with terrible metrics: lines added, feature points done, etc. I'm more interested in how it affects the metrics we set for ourselves that our bosses might never know about.

*   "Test coverage" is a proxy for how thoroughly we've tested our software. It diverges when we need to test lots of properties of the same lines of code, or when our worst bugs are emergent at the integration level.
*   "Cyclomatic complexity" and "function size" are proxies for code legibility. They diverges when we think about global module legibility, not local function legibility. Then too many functions can obscure the code and data flow.
*   Benchmarks are proxies for performant programs, and diverge when improving benchmarks slows down unbenchmarked operations.
*   Amount of time spent pairing/code reviewing/debugging/whatever proxies "being productive".
*   [The DORA report](https://dora.dev/) is an interesting case, because it claims four metrics[2](#fn:metrics) are proxies to ineffable goals like "elite performance" and _employee satisfaction_. It also argues that you should minimize commit size to improve the DORA metrics. A proxy of a proxy of a goal!

### What can we do about this?

No, I do not know how to avoid a law that can hijack the process of evolution.

The 2023 DORA report suggests readers should avoid Goodhart's law and "assess a team's strength across a wide range of people, processes, and technical capabilities" (pg 10), which is kind of like saying the fix to production bugs is "don't write bugs". It's a guiding principle but not actionable advice that gets to that principle.

They also say "to use a combination of metrics to drive deeper understanding" (ibid), which makes more sense at first. If you have metrics X and Y to approximate goal G, then overoptimizing X _might_ hurt Y, indicating you're getting further from G. In practice I've seen it turn into "we can't improve X because it'll hurt Y and we can't improve Y because it'll hurt X." This _could_ mean we're at the best possible spot for G, but more often it means we're trapped very far from our goal. You could come up with a weighted combination of X and Y, like 0.7X + 0.3Y, but _that too_ is a metric subject to Goodhart.

I guess the best I can do is say "use your best engineering judgement"? Evolution is mindless, people aren't. Again, not an actionable or scalable bit of advice, but as I grow older I keep finding "use your best judgement" is all we can do. Knowledge work is ineffable and irreducible.
