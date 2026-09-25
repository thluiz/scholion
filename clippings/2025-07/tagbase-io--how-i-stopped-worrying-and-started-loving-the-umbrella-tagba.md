---
url: "https://www.tagbase.io/how-i-stopped-worrying-and-started-loving-the-umbrella/"
captured_at: "2025-07-17T13:36:19+01:00"
title: "How I Stopped Worrying and Started Loving the Umbrella – TAGBASE"
domain: "tagbase-io"
---

---
When we first started tagbase.io, my co-founder Manuel had already built a working prototype in Node.js. It did the job—users could scan their NFC tags and get verified—but it was just that: a prototype. We shipped it, polished the UI a bit, and kept it alive for almost a year. But it was clear from the start that this app wouldn’t scale with us.

The biggest issue was architecture. Our system had two very different needs: a globally distributed verification app that had to respond as close to the user as possible, and a much more centralized portal where customers could configure their tags. Trying to mash both into one app was a non-starter.

I had experience with Elixir—over eight years of it—and I wanted to show off its strengths, especially around real-time communication. So I started the portal app with Elixir and Phoenix. One of the first things I demoed to Manuel was a globe visualization that would rotate to show the location of an NFC scan in real-time. That demo sealed it.

Pretty soon, we also realized we needed a back-office app for feature flags, internal tools, and operational insights. Naturally, we built that in Elixir too. And finally, we rewrote the original Node.js verification app in Elixir as well, with proper testing and shared logic.

Now we had three Phoenix apps. All written in Elixir. All needing to share code. And that’s when things got tricky.

## The Multi-App Headache

Sharing code across standalone Elixir apps is messy. You can mess with `mix` dependencies, symlink folders, or straight-up copy code, but none of those are elegant or sustainable. I’d worked with Elixir Nerves before, which uses a `MIX_TARGET` variable to manage hardware-specific builds. I figured I could repurpose that idea to manage a quasi-monorepo: one shared folder structure, different targets for each app.

It worked surprisingly well, especially with Docker and Fly.io. Each app got its own `mix release`, built into separate containers. But the local dev experience was painful.

Tailwind components wouldn’t update across apps. I’d make changes, wonder why nothing was working, and realize I was editing the wrong folder. It was chaos. I had three checkouts of the same repo just to keep the apps separated. That’s when I started seriously considering umbrella apps.

## Why Not Umbrella?

So why didn’t I start with an umbrella app in the first place?

First off, the setup felt like a pain. Converting everything took two full days—and while it was worth it, that initial cost felt daunting. If you’re starting fresh or only have one or two apps, the setup is faster, but when you’re knee-deep in a growing codebase, it’s a commitment.

Second, the documentation is lacking. Umbrella apps are rarely covered in tutorials or blog posts, and when they are, it’s often superficial. There’s very little guidance on how to do real-world things—like managing shared assets.

Which brings me to another friction point: assets. Where do you put shared Tailwind or JavaScript files? How do you keep app-specific styles separate? It’s not obvious, and I ended up figuring out by chance that you can link one app’s asset pipeline into another. That’s not in any guide I came across.

Lastly, I was thinking a lot about security. I didn’t want dangerous functionality from the back office—like user deletion—anywhere near the portal codebase. I knew `mix release` could give me that separation, but it’s buried deep in the docs. Nothing makes it clear how powerful that isolation can be.

## Embracing the Umbrella

Eventually, I made the switch. It was a lift, but absolutely worth it.

Suddenly, I could run everything with a single command. Code changes reflected immediately across all apps. Compilation got faster because shared files were compiled once, not three times. Local development stopped feeling like a game of whack-a-mole.

Each app has its own dependency tree. If the portal doesn’t need something, it doesn’t even see it. The boundaries are visible and enforced.

It’s made everything cleaner. Easier to test. Easier to deploy. Easier to think about.

So yeah, I stopped worrying. And I started loving the umbrella.
