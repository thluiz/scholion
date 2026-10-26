---
url: "https://daily.dev/posts/LgFVrktej"
captured_at: "2026-10-26T12:30:42+00:00"
title: "Developers should be aware of these two AI engineering approaches"
domain: "daily-dev"
---

As a developer, there are two engineering practices you should be aware of - Harness Engineering & Graph Engineering, to build reliable agentic systems.

**Graph Engineering** is becoming one of the most useful ways to build reliable AI-native engineering systems. Instead of putting everything into one massive prompt and hoping an AI model handles every detail correctly, I design the work as a connected system of smaller, explicit tasks. Each task has a purpose, a defined input, an output, and a route to the next step. That is the core idea behind Graph Engineering. It gives AI agents structure, makes their decisions easier to inspect, and lets independent work happen in parallel.

Similarly, Harness Engineering is becoming essential because AI coding agents are getting very good at generating code, but code generation is only one small part of real software engineering. A useful agent must also understand the service it is working on, the team that owns it, its dependencies, the engineering rules it must follow, what it is allowed to change, and how to verify that its work is correct.

That complete environment is what makes an AI agent reliable. In this guide, I will explain Harness Engineering in a simple way, then walk through two practical implementations: a controlled payment bug fix and a scorecard-based deployment gate.

Well, I would like to share the guides around these two engineering approaches.

Here is my video guide on harness engineering: [https://youtu.be/vAHnGUWPPNY](https://youtu.be/vAHnGUWPPNY?si=kMliPXcr6L3Jp6N5)

Here is my video guide on graph engineering: [https://youtu.be/g3C7mudBURA](https://youtu.be/g3C7mudBURA?si=xrF8qOMFNjovsV7j)

20 Comments

Sort:

Share this post

[![andrewduncan's profile](https://lh3.googleusercontent.com/a/ACg8ocIOpyCFieHnXPAc199x8b2A7uhSGmRANbdNykfN9iOaYPIG6vU=s64-c)](https://daily.dev/andrewduncan)

interesting article! Small edit [@johhnypav](https://daily.dev/johhnypav) your thumbnail has the descriptions backwards. the description for graph engineering appears under harness engineering, and the description for harness engineering appears under graph engineering.

Graph engineering has fascinating potential

[![johhnypav's profile](https://media.daily.dev/image/upload/s--r9dshbly--/f_auto/v1776930121/avatars/avatar_DFA0U7-fS?_a=BAMAMiWQ0)](https://daily.dev/johhnypav)

[@andrewduncan](https://daily.dev/andrewduncan) Thanks for noticing that, just edited the post properly. Yes, Graph engineering has a great potential and looks like many companies are already seeing it.

[![harshitmanepally's profile](https://media.daily.dev/image/upload/s--O0TOmw4y--/f_auto/v1715772965/public/noProfile)](https://daily.dev/harshitmanepally)

A great article. Helpful for beginners.

[![swarnasharmin's profile](https://media.daily.dev/image/upload/s--joHEq_jD--/f_auto/v1791022797/avatars/avatar_ZL6bebyCVkszL2cr0g8ab?_a=BAMAMicg0)](https://daily.dev/swarnasharmin)

Graph architecture paired with strict harness rules is exactly how we move from flaky LLM demos to production-grade agents.

[![johhnypav's profile](https://media.daily.dev/image/upload/s--r9dshbly--/f_auto/v1776930121/avatars/avatar_DFA0U7-fS?_a=BAMAMiWQ0)](https://daily.dev/johhnypav)

[@swarnasharmin](https://daily.dev/swarnasharmin) That ls exactly right. That’s why both are important while building agentic systems.

[![jeremiahcharles69's profile](https://lh3.googleusercontent.com/a/ACg8ocJTFqBp-LCXy1SjhWhMIt18sz1Fwq9ON0v5KqVsaYRcZVfg-pPW=s64-c)](https://daily.dev/jeremiahcharles69)

Hey

Thanks for bringing this here, it was really helpful.

[![itskiranrao's profile](https://media.daily.dev/image/upload/s--hQa8XkPK--/f_auto/v1789152231/avatars/avatar_AmGE2HhTmmKGwLMuVkqQz?_a=BAMAMicg0)](https://daily.dev/itskiranrao)

Smaller tasks also make debugging easier. You can see which step went wrong instead of digging through one huge agent run.

[![johhnypav's profile](https://media.daily.dev/image/upload/s--r9dshbly--/f_auto/v1776930121/avatars/avatar_DFA0U7-fS?_a=BAMAMiWQ0)](https://daily.dev/johhnypav)

[@itskiranrao](https://daily.dev/itskiranrao) That’s true and that’s where graph engineering helps.

![](https://media.daily.dev/image/upload/s--lf8LUJjq--/f_auto/v1732012913/login-popover-dailydev_mxb7lw)

## daily.dev is the fastest growing developer platform in Portugal!

### We know how hard it is to be a developer. It doesn't have to be. Personalized news feed, dev community and search, much better than what's out there. Maybe ;)

Already have an account?
