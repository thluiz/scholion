---
url: "https://highimpactengineering.substack.com/p/we-handed-testing-to-ai-here-is-what"
captured_at: "2026-11-12T12:32:27+00:00"
title: "We handed testing to AI. Here is what stayed human."
domain: "highimpactengineering-substack-com"
---

A few weeks ago, I wrote about a new bottleneck my team ran into: [manual validation](https://highimpactengineering.substack.com/p/the-next-bottleneck-is-not-code-review). Writing code got much faster, and QA had to keep up with it.

I argued that the only way for QA to keep up with the growing number of changes was to bring in AI, and I proposed using risk assessment to decide what to fully delegate to AI and what to leave to people.

I promised to report back. Here is what happened.

> I’m Roman, CTO at Cambri. I write High-Impact Engineering — a weekly newsletter about how product & engineering orgs work, and break, in their first 30 people. I’ve lived that passage as an executive; now I also advise founders and engineering leaders going through it.

Three things happened at the same time, and all of them landed on QA.

**First, there was more work.**

[

![](https://substackcdn.com/image/fetch/$s_!hnL-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa237b5d1-6b9e-4837-98f4-b786917b7245_1600x900.png)

](https://substackcdn.com/image/fetch/$s_!hnL-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa237b5d1-6b9e-4837-98f4-b786917b7245_1600x900.png)

To build this chart, I used data from Jira and GitHub. Active developers are people who merged more than five PRs in a month.

The numbers are a bit noisy, because the way tickets are created has changed. Before, tickets were mostly written by the PO by hand, later refined with ChatGPT once that became an option. Now everyone creates tickets with Claude and the Jira MCP: Claude writes the first version, and people check and edit it.

Still, the picture is clear. For three years, the same team of six or seven developers delivered roughly the same amount. Then, in January, we switched from Cursor to Claude. In 2026, the same team finished about 44% more tickets a month than in 2025, not counting bugs, and the PRs merged per month roughly doubled. From May, each ticket carried about three times as much code: tickets got much bigger, and more functionality now goes into a single ticket.

**Second, there were fewer testers.**

At the same time, the QA team shrank from 2.5 people to 2 in August (one QA engineer had worked another role half the time).

**Third, there was less review before the work reached QA.**

[

![](https://substackcdn.com/image/fetch/$s_!GGLl!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5eb2faf5-be01-405a-b760-136a19f5d6e5_1600x900.png)

](https://substackcdn.com/image/fetch/$s_!GGLl!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5eb2faf5-be01-405a-b760-136a19f5d6e5_1600x900.png)

Again, the data is a bit noisy. For example, I don’t remember what happened in December 2024 — why the jump. But the trend is clear.

In 2025, about a quarter of PRs were merged without another developer reviewing them. In 2026, it was about half, reviewed only by their authors with help from AI. Code review had to adjust to the speed of development, and QA became the main human check.

More work, fewer testers, and less review before it reaches them. You can imagine what would have happened if we had kept testing everything mostly by hand.

[

![](https://substackcdn.com/image/fetch/$s_!-f4b!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe70057d0-b202-4cfc-bd13-96d74f491f86_1600x900.png)

](https://substackcdn.com/image/fetch/$s_!-f4b!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe70057d0-b202-4cfc-bd13-96d74f491f86_1600x900.png)

One of our QA engineers, Javier, built the setup on Claude Code. It started as a single skill in the spring and has grown into a whole QA toolkit. A few principles make it work:

**The day starts with a sorted queue.** The first thing each morning, the QA engineer starts a scan with a Claude skill. An agent goes through every ticket waiting for QA, maps what each change touches, runs the tests that already exist, and sorts the queue.

**The QA engineer decides what to test.** The agent proposes how to spend the session: a group of tickets touching the same part of the product, the riskiest ticket, or a few quick wins. The person picks.

**Cheapest evidence first.** The agent breaks the acceptance criteria into small claims and checks each one in the cheapest way that can settle it: an existing test, or the code itself. Only what is left goes to the browser.

**Plan against the claim, not for it.** An AI asked to verify work tends to confirm it, because the requirements and the code use the same words. So for every claim, the agent has to name what would prove it wrong.

**Look for what nobody was looking for.** Then an agent explores the edges: empty and maximum values, two settings on at once, a refresh in the middle of a flow.

**The verdict stays human.** The QA engineer reviews what was checked, answers the agent’s questions, and asks for more scenarios. The final call is theirs, even when every check passed. The agent can never move a ticket to Done, and never files a bug without approval.

[

![](https://substackcdn.com/image/fetch/$s_!4Zj2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe4c4d4cc-5f82-41e5-b212-3961fabec865_1333x927.png)

](https://substackcdn.com/image/fetch/$s_!4Zj2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe4c4d4cc-5f82-41e5-b212-3961fabec865_1333x927.png)

The QA board runs locally and is built from a Claude skill. It is the single place from which the QA engineer manages testing: the scenarios checked, the evidence (videos and screenshots), the agent’s questions, and requests to test more.

My favourite line on it: “The verdict is yours; it is never filled in for you.”

By the team’s own estimate, the agent now does about 75–85% of the hands-on test execution on a ticket. It runs 16 to 29 scenarios per ticket, and the QA engineer answers about five questions. That is an estimate from a week of sessions, not a measurement.

Fully automated testing of low-risk tickets hasn’t happened yet. I see two reasons for that.

The first is that the QA team is not comfortable going fully hands-off. They still want to see what has been checked, so they don’t completely outsource it to AI and lose touch with the product.

The second is that it hasn’t been a big priority. The current classifier rarely marks tickets as low risk, so there is not much to outsource.

The QA team keeps up with the wave of validation, but barely.

Shift-left requirement testing has been abandoned: there is no time for it. The team is busy, and more reactive than proactive. If tickets are not handled quickly, the queue starts getting out of control.

The number of bugs found and fixed also went up sharply in September and October. Part of it is the new setup finding more. Part of it may be the code that went out with less review over the summer. I don’t know yet how the two split.

I don’t see this as sustainable in the long run. The work engineering does will accelerate even more as AI gets better and engineering harnesses improve.

A few possible directions:

*   QA runs more tests in parallel: several agents at once, with people constantly switching and making decisions.
    
*   QA turns into a quality-harness engineering discipline: designing the context, tooling, and agent interactions that take people out of the loop wherever it is safe.
    
*   California VCs stop subsidizing small businesses’ AI subscriptions, and we go back to coding by hand.
    

My bet is on the second. The bottleneck keeps moving. This time, the way through it is not more testers, but better systems around the ones we have.

_My newsletter is free and will stay free: no paywalls, no paid subscriptions. If this issue was useful, the best way to support my work is to share it with one person who would benefit from it._

[Share](https://highimpactengineering.substack.com/p/we-handed-testing-to-ai-here-is-what?utm_source=substack&utm_medium=email&utm_content=share&action=share)

_P.S. If you are a startup founder or CTO under pressure to deliver fast to stay in the game, I can help. I have been doing exactly that as a CTO for the last five years, and I am happy to work with you in whatever form fits: from sparring on ideas, to a full audit, to hands-on work inside your organization. The first step is a 30-minute call: [let's talk](https://tally.so/r/lbKxR5)._
