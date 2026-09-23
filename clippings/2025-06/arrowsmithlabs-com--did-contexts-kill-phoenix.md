---
url: "https://arrowsmithlabs.com/blog/did-contexts-kill-phoenix"
captured_at: "2025-06-27T00:57:54+01:00"
title: "Did contexts kill Phoenix? · Arrowsmith Labs"
domain: "arrowsmithlabs.com"
---

I love Elixir and Phoenix. They've been my main stack for years, and I use them on almost every project when I have a choice. But we Phoenicians must admit that the framework, now in its twelfth year, never really took off like, say, Rails before it. It remains a niche technology with a small but loyal following, and it will probably stay that way.

Those who learn Phoenix tend to really like it — just see the Stack Overflow developer survey, where Elixir and Phoenix were rated the 2nd and 1st "most admired" technologies in their respective categories. And you only need to look at the Elixir Slack or subreddit to find crowds of developers who'd happily take full-time Phoenix work if they could find it. So why isn't there more work?

In some respects the deck was always stacked against Phoenix. It was a late entry into a crowded field going up against big, popular established players, and Elixir never had the big institutional backing that, for example, Typescript had from Microsoft or Go had from Google.

But that might not be the only reason. I think about this thread a lot: "Code Merchant" argues that Phoenix's momentum was killed by certain architectural changes: in particular, the introduction of contexts in Phoenix 1.3. Previously, Phoenix was more similar to existing popular frameworks like Rails, and thus easier for newcomers to learn. Contexts, however, introduced a layer of confusion and complexity that raised the barrier to entry.

I wasn't using Phoenix back then, but Google Trends does show a steady decline in interest starting in mid-2017. I'm not sure what caused the later spike in 2022 — tell me your theories. But still, the line today in 2025 is well below its 2017 peak.

Is it contexts' fault? As I explained last week, contexts don't have to be difficult. They're actually quite a simple concept, and if beginners get confused it's usually because they overthink it, imagining contexts to be something more complicated than they actually are.

But still, beginners do get confused, and that's a problem. If we want more people to learn Phoenix, we need to provide as gentle as possible of an on-ramp. And contexts, I think, do more harm than good.

## The second-hardest problem in computer science

It's a nice idea in theory: follow the principles of domain-driven design and divide your app into cleanly-separated logical domains, exposing to the web layer only the precise set of functions that are required by your business logic.

But in practice, it's a lot of extra work. For starters, it slams you repeatedly into one of the two hard problems in computer science: naming things.

Let's say I want to add the concept of a "post" to my blogging app. In Rails I pick a name for the model, `Post`. But in Phoenix, I also need to pick a name for the context, such as `Blog`. It's not always obvious what the context should be called. The docs suggest to just use the plural name of the schema (i.e. `Posts` above) if you're not sure. But I'd rather not be forced to think of any name. It's extra mental overhead that slows me down, and I'm not convinced it's necessary.

## The root of all evil?

Of course, I'm not merely picking a name. I'm supposed to be thinking of a domain — a high-level concept that encapsulates a particular area of my business logic. I don't just have a `Blog`, I have `Accounts` whose users post `Comments` that need `Moderation`, and I can organize my code into these logical categories.

Again, it's nice in theory, but in my experience this type of high-level architectural wrangling only starts to make sense once your codebase reaches a certain size. When you're starting out, it can feel like the root of all evil — premature optimization.

It's rarely obvious, at least not to me, how exactly to extract my "domains". Should user profiles go in the same context as auth? Does banning a user go under `Accounts` or `Moderation`? Should admin-only functionality go in a new `Admin` context or in one of the existing ones? I'm not saying these conversations are useless, I'm just saying that it slows you down.

It's especially a problem on a greenfield project. When you're starting out — as beginners are by definition — you're often not sure of the full requirements. Building the app is part of the process of discovering what's needed. If everything needs to go in a context, you have to think of context names long before it's clear what the contexts should even be. The result is friction.

## Clutter and boilerplate

I can only speak to my own experience, but I've seen what happens to contexts on the apps I've worked on. They tend to fill up with repetitive, boilerplate functions that are thin wrappers around `Repo`: `get_user/1`, `get_course/1`, `get_post/1`, `get_widget/1`, `get_tps_report/1`, and so on.

More complicated functions are often hyper-specific to the controller or LiveView that uses them, and thus are only called from one other place in the codebase. It's an extra layer of indirection for dubious architectural benefit.

To be clear, I'm not saying that contexts are an awful idea. I just think they're overemphasized. Technically, nothing forces you to use contexts — Chris McCord isn't going to kill you in your sleep if you call a `Repo` function directly from a controller. But the docs imply that everything should be directed through a layer of contexts, and it's easy to see why beginners get hung up.

I know a lot about what Phoenix beginners think. I've taught thousands of them, I've heard from many, many Phoenix learners with all kinds of questions, and I confirm that contexts are a consistent source of confusion. I'm sure that this has hurt Phoenix's adoption.

Phoenix is still an incredible framework, and I'm not suggesting we abandon contexts entirely. But I think the Phoenix community needs to acknowledge that our love of good architecture has created barriers to adoption.

Maybe we need better tooling that makes contexts more automatic. Maybe we need stronger conventions that remove the bikeshedding. Maybe we need a "simple mode" for beginners that defers the complexity.

Or maybe we need to accept that architectural elegance and mass adoption are sometimes at odds. Rails won by being pragmatic, not pure. Phoenix could learn from that lesson.
