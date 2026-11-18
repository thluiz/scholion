---
title: "10x developers"
date: '2025-07-11T18:59:31+00:00'
category: webclip
summary: 'Argues that 10x developers exist mainly by contrast to 0x and −nx developers and that perceived productivity varies heavily with context and environment.'
tags: ["software-development", "productivity", "teams", "context"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "10x developers"
    url: "https://blog.ploeh.dk/2019/09/30/10x-developers/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/blog-ploeh-dk--10x-developers-context-and-negative-productivity.md"
    kind: repo
---

The text questions the usual idea of a 10x developer and reframes it through examples of colleagues perceived as highly productive who actually create technical debt. Perceived 10x productivity often comes from non-technical stakeholders judging only visible output, while the clean-up work stays hidden.

The author argues that productivity in software is hard or impossible to measure, so the 10x label is subjective and context-dependent. Developers can be highly effective in familiar stacks and environments and ineffective in others. Team composition, work style, technology stack, and working conditions strongly influence how productive someone appears.

He introduces the notions of 0x and −nx developers: people who get nothing done or whose output has negative net value because others must spend time fixing or discarding their work. Against such baselines, anyone who consistently ships useful code is effectively an ∞x developer. The piece closes by noting that while true standouts might exist, variability in productivity seems mostly tied to environment rather than a fixed 10x trait.

## Reading notes

- The author believes 10x developers exist but not in the simplistic sense of someone being ten times more productive than a fixed baseline.
- A story about "Yohan" illustrates a developer praised by business stakeholders for always saying yes and delivering features quickly.
- Non-technical stakeholders label Yohan a 10x developer because they see visible outcomes and friendly behaviour.
- Technically, Yohan introduces risky practices such as blanket try-catch blocks, direct production changes, copy-paste code, business logic in triggers, log rewriting, and misusing technologies like email and HTML parsing on back-end servers.
- The rest of the team spends much of their time cleaning up after Yohan, which destroys their apparent productivity.
- The example shows how most programming work is invisible and why perceptions of 10x productivity depend heavily on perspective.
- The 10x notion assumes a "baseline" programmer, but modern software work is specialised, so a universal baseline is doubtful.
- The author is highly effective with test-driven, ASP.NET-based C# enterprise development, but would stall if asked to write a PlayStation game.
- This leads to the tongue-in-cheek claim that one is a 10x developer simply by being much better at familiar tasks than unfamiliar ones.
- Expertise in one language or domain, such as R, does not transfer automatically to another, like COBOL.
- Context extends beyond tech stack to preferences for co-location vs. solo work, detail focus vs. big-picture thinking, and time-of-day productivity.
- Teams of so-called mediocre programmers can outperform teams of all-stars, mirroring cases seen in professional soccer.
- The author states that software development productivity cannot be reliably measured, making the 10x idea inherently subjective.
- A referenced book, "The Leprechauns of Software Engineering," is cited as showing that the original evidence for 10x developers is weak.
- Despite weak evidence, belief in 10x developers persists because it feels intuitively obvious that some people contribute much less than others.
- The author recalls his first job, where dislike for the work led him to delay even simple tasks, making him effectively unproductive.
- He later interprets that episode as a mismatch of context and environment rather than pure incompetence.
- Another anecdote describes a colleague who talked extensively with many people, generated ideas, but produced almost no helpful code or changes.
- Git history and collaboration patterns suggested that this colleague contributed little independently.
- The author has met several programmers who get nothing done, some loud, some very quiet, often possibly misplaced rather than inherently incapable.
- From these experiences, he infers the existence of 0x developers who achieve zero output relative to an average developer.
- By comparison, any developer who regularly deploys code to production is vastly more productive than a 0x developer, effectively infinitely more.
- He then introduces −nx developers, whose net effect is negative because they create messes that cost more effort to fix than they contribute.
- Yohan is given as an archetype of a −nx developer whose well-meant work multiplies technical debt.
- In one case, a team isolated a particularly harmful colleague to a part of the system they planned to throw away after that person left.
- The team padded other estimates and rewrote the isolated code once the colleague was reassigned, which helped them still meet deadlines.
- Accepting that −nx developers exist leads to the conclusion that anyone who gets anything useful done at all is an ∞x developer.
- The article sums up that 10x developers exist because perceived productivity varies greatly and is strongly tied to context.
- There may be individuals who are simply better programmers, with the mention of Linus Torvalds as an example.
- However, the author thinks environment and fit with the stack, tasks, colleagues, hours, and workspace explain much of the variance.
- Even if environment factors were controlled, some people would still deliver and others would not, reinforcing the ∞x framing.
- Employers and non-technical founders often chase mythical 10x or "rock star" developers in hiring.
- A joke tweet about a Rockstar programming language led Dylan Beattie to create one, illustrating how labels can become novelty credentials.
- The author whimsically suggests inventing a "10x" language so developers could claim to be certified Rockstar, 10x programmers on their resumes.
