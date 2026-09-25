---
url: "https://www.akashbajwa.co/p/the-future-of-software-engineering"
captured_at: "2026-09-25T21:50:01+01:00"
title: "The Future Of Software Engineering with Anthropic"
domain: "akashbajwa-co"
---

_Software Synthesis analyses the evolution of **software companies in the age of AI** - from how they're built and scaled, to how they go to market and create enduring value. You can reach me on [LinkedIn](https://www.linkedin.com/in/akashbajwa/) and [X](https://x.com/AkashBajwa96)._

[Sivesh](https://www.linkedin.com/in/sivesh/?originalSubdomain=uk) and I recently hosted a roundtable on the future of software engineering with Anthropic’s [Ash Prabaker](https://www.linkedin.com/in/ash-prabaker/?originalSubdomain=uk) and we were joined by engineering leaders from Stripe, NVIDIA, Microsoft, Google DeepMind, xAI, Apple, Scale AI, as well as the legend Peter Steinberger of OpenClaw/OpenAI.

[

![](https://substackcdn.com/image/fetch/$s_!zY25!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6ff4479f-fb33-4993-91af-59edddaacf80_1536x2048.jpeg)

](https://substackcdn.com/image/fetch/$s_!zY25!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6ff4479f-fb33-4993-91af-59edddaacf80_1536x2048.jpeg)

The session opened with a retelling of the Claude Code origin story, much of which has been covered in public interviews. It began as a simple terminal UI in late 2024, was rough at first, and was built against a guiding principle of designing for where models would be in six to twelve months rather than where they were that day. Adoption was organic — an IC-driven project that scaled through demonstrated value rather than mandate.

A major thread throughout the discussion was “closed-loop” development. One participant described a setup at their company where bug reports are automatically triaged by an agent, bucketed by severity, checked against an eval set, and then a fix PR is opened — much of it running with minimal human touch. The room broadly agreed that this kind of loop is where compounding gains actually come from: better coding tools improve the models, better models improve the coding tools. Several people noted their companies are prioritizing coding specifically because of this dynamic.

Participants compared notes on what’s shifting in their engineering practice:

1.  Test-first has become the default. Multiple people said they now define test cases first and let the agent build against them — described as the only sane way to handle the volume of PRs being generated.
    
2.  Two tiers of evals. One participant outlined their team’s approach: regression evals that must stay at 100% and run on every PR, plus frontier evals for new capabilities. Others in the room recognized the pattern.
    
3.  Don’t mandate adoption. There was strong consensus here. One attendee described using competitions, hackathons, and casual incentives instead of top-down requirements — arguing that forced usage breeds resentment, whereas letting people see early adopters’ results drives proliferation naturally.
    
4.  Code review is in flux. One participant admitted that human reviewers at their company often just click approve within minutes because the AI review layer has gotten good enough. When pushed on where this ends up, they acknowledged the mandatory-human-review model will eventually become inefficient — and suggested they may already be past that point for some repos. This landed with a mix of recognition and discomfort around the table.
    
5.  Comments are back. A cultural reversal several people found amusing: engineers initially hated the verbose comments agents generated, but the consensus is now swinging toward leaving them in, because the next agent session finds them useful. One person put it as “we’re writing code for AI readability as much as human readability now.”
    
6.  Life in the terminal. One participant described their personal workflow as: plan, verify the plan, implement via the agent, move on — without reading generated code line by line. This prompted some debate about when that’s safe and when it isn’t.
    

Not all code is treated the same. Participants generally agreed that anything involving destructive actions (data loss, permission escalation) or core infrastructure deserves higher human review, while internal prototypes don’t need the same bar as public-facing code. Where exactly to draw the line varied by company.

The room converged on long-horizon tasks as the real frontier problem. One participant noted that product engineering has started to go exponential for them, but closing the loop on more complex research workflows isn’t there yet. The open questions everyone shared: what do you actually assign an agent for a four- or five-hour run? How do you observe it? How do you keep a human in the loop without babysitting? Nobody had a clean answer.

Discussion of how the industry has swung on sandboxing — first toward it for safety, then away from it for convenience, now back toward it with more nuance (remote coding agents, sandbox-per-session). The practical pain points people raised were compute for long-running sessions, permissioning, and enterprise deployment.

One participant described early-stage internal prototypes where agents with access to logs, source control, and chat systems handle incident triage and debugging — reducing the on-call burden even though the systems aren’t production-grade yet. A side effect several people found interesting: engineers without infra backgrounds can now contribute to infra work because agents fill the knowledge gaps.

Someone asked how you manage context at scale when thousands of people are changing things every minute. The honest answer from the room was that nobody has this figured out. One participant admitted their approach is basically unstructured — ad hoc chat threads that agents get MCP access to read, plus a strong writing culture but no formal documentation process.

A study was mentioned suggesting that pre-loaded markdown context files can sometimes underperform versus letting agents traverse the codebase from first principles. The counter offered was that this probably reflects stale or agent-generated context. The takeaway people seemed to agree on: human-authored context files help, agent-authored or stale ones can actively hurt. Humans have to supply the insight.

When hiring came up, the most striking claim was that the trait one participant now screens hardest for isn’t raw engineering skill — it’s willingness to experiment constantly at the bleeding edge. Their best performers are the ones who understand model limits deeply enough to know when to trust the output and when to intervene. Another attendee noted their core infrastructure teams have stayed lean because AI-assisted cross-pollination lets product engineers contribute outside their usual domain.

This got lively.

Participants traded stories about which tool categories they’ve replaced internally:

*   Incident management — one person said their team ripped out their vendor because it was too complicated for how people actually worked.
    
*   Auth layers — one participant claimed to have migrated auth systems several times in six months, each migration taking hours not weeks.
    
*   Project tracking — someone is building custom UIs on top of their coding agent for managing engineering work, and floated that this whole category might be next.
    
*   Internal micro-tools — link shorteners and similar utilities were the easy wins several people mentioned.
    

The pattern everyone noticed: it’s all developer tooling so far, because that’s where engineers have agency and speed. Business-facing software (CRMs, etc.) is stickier. One view was that incumbent business tools survive not because they’re good but because nobody has shipped a compelling AI-native replacement — just incremental add-ins.

A counterpoint from the room: the opportunity-cost argument (”we should focus on what we’re best at”) may always hold, which means labs might never prioritise building SaaS replacements over improving models.

A startup founder in the room raised the flip side: because AI makes everything feasible, prioritisation is harder, not easier. Six months ago, rebuilding a tool internally was obviously not worth it. Now it takes a night. Teams get overloaded by the sheer volume of things they could do. Nobody had a great answer beyond defining clear swim lanes and giving individuals ownership of mini-companies inside the org.

When someone asked about code quality standards, the response was that the definition is shifting. “Good code” used to mean human-centric things — simple, easy to maintain, easy to contribute to. Now it has to account for AI readability too. The practical view from the room: strong regression evals and test-first discipline matter more than clean-code aesthetics.

“The purple gradient vibe” got a laugh — everyone recognized the AI-generated-UI aesthetic. The catch-22 someone identified: if you update a model’s taste profile, everyone uses it, and the new aesthetic just becomes the next generation of slop. Someone also noted that some models actively steer users toward particular frameworks, which functions as a form of lock-in.

One attendee raised a concern that everyone coding with the same models making the same suggestions will collapse the industry onto the same tools and patterns. The pushback was that this was a bigger risk with earlier model generations, which were much stronger at popular web stacks than at legacy or niche languages — and that gap is closing. Code modernisation of legacy systems came up as an area improving fast.

General agreement that the direction of travel is toward asynchronous background agents — remote sandboxes, monitorable from a phone, persisting across hours or days. One person noted that multi-hour autonomous runs are only recently becoming routine for them, having been experimental until not long ago.

Asked how much recent improvement is model weights versus harness, one participant’s view was that both matter but on different cadences — big leaps come from model steps, and the harness philosophy should be “get out of the way of the model.” They described a stripped-down prototype — basically a current-gen model with a system prompt and bash access — that performs surprisingly well, which wouldn’t have worked a few generations ago.

Someone from a fintech background asked about regulated deployment. The room’s read: the most successful AI startups in regulated industries (legal tech was the example) are still fundamentally human-in-the-loop chat-with-document products. Nobody has made the jump to autonomous agents in regulated workflows. The bar is asymmetric — analogous to self-driving cars, where AI has to be dramatically better than a human to be accepted. Better explainability and structured audit trails were floated as the unlock.

Refreshingly low-tech answer: git worktrees and ten terminal tabs. More sophisticated orchestration is being built by third parties, but nobody in the room claimed to have it solved.

Someone observed that getting engineers to adopt AI tools — finding champions, overcoming resistance, managing change — is exactly the digital transformation problem other industries have faced for years. The irony of applying it to the engineers who built those transformation tools was not lost on the room.

Closing question: will agents start writing closer to the metal, bypassing the abstraction layers that exist for human convenience? The view was yes, eventually, but only when the model decides it serves performance — not because lower-level code is easier for models. Current models still benefit from well-structured, well-commented, human-readable code. Someone noted a trend toward Rust in startups, driven partly by AI flattening the learning curve.

*   The recursive loop is real. Better coding tools produce better models, which produce better coding tools. Multiple participants said this is why their companies are prioritising coding.
    
*   The bottleneck has moved from writing code to managing long-horizon tasks and deploying agents in regulated settings.
    
*   Developer tooling is being displaced first. Business-facing software with network effects is holding.
    
*   The human role is shifting from writing and reviewing to planning, evaluating, and steering — and the best performers are the ones who stay at the bleeding edge.
    
*   Enterprise adoption is gated by permissioning, sandboxing, and regulatory caution more than by model capability.
    
*   Slop and convergence are real concerns when millions of people use the same models to make the same choices.
    
*   Context remains unsolved. Human-authored context helps; stale or agent-generated context can hurt.
    

_Have any feedback? Reach out on [LinkedIn](https://www.linkedin.com/in/akashbajwa/) or [X](https://x.com/AkashBajwa96)._
