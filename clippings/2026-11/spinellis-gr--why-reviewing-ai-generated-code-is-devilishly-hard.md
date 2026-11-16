---
url: "https://www.spinellis.gr/blog/20260523/"
captured_at: "2026-11-16T10:42:43+00:00"
title: "2026-05-23 — Why reviewing AI-generated code is devilishly hard"
domain: "spinellis-gr"
---

Here’s the thing: when working on code with GenAI assistance (from a chat-bot, through IDE auto-completion, or, increasingly, with an AI agent) you need a better understanding of the system than when working without. Cognitive psychology and the workings of large language models (LLMs) give us four clues on why this happens.

When working without AI assistance on a non-trivial task and on code you don’t know, you first need to comprehend it in order to perform your task. Otherwise you’re hacking (in the sense of performing undisciplined changes), not programming, and most likely you won’t go anywhere (fast). This is an objective built-in control gate of the human-only software development process: if you don’t understand the code, you can’t contribute to it and you you fail.

When working with AI assistance and you have to review an AI-generated change that passed continuous integration, the control gate is missing: there’s no objective mechanism to determine whether you _truly_ understand the code or not. This means that you may accept an AI-generated change in the mistaken belief that you understand it, when in fact you don’t.

The required type of thinking, _metacognition_, involves not only understanding the code but also assessing your understanding. In brief, it involves two abilities.

*   **Metacognitive monitoring**: assessing what you know (e.g. a specific data structure or design pattern used in the code), how well you understand the change, confidence in your review comments, and detecting confusion.
*   **Metacognitive judgment**: specific evaluative acts within monitoring, such as
    *   _judgment of learning_ (I’ll remember this change when we discuss our new architecture);
    *   _feeling of knowing_ (I’ll understand this code when I see it again);
    *   _confidence judgment_ (I’m 95% sure this code is correct); and
    *   _ease-of-processing judgments_ (this change feels easy, so I’ll probably understand it).

Unfortunately, a couple of influential psychological studies have shown that people are often poor at accurately evaluating their own knowledge or performance. Most famously, the [Dunning-Kruger effect](https://doi.org/10.1037//0022-3514.77.6.1121) states that people with low competence tend to overestimate their competence because the skills needed to perform a task are also needed to evaluate performance. The implication of this is that junior programmers are more at risk from accepting faulty AI-generated code.

In addition, through the [illusion of explanatory depth](https://doi.org/10.1207/s15516709cog2605_1) people think they understand mechanisms with far greater precision, coherence, and depth than they really do. Moreover, this gap is strongest for explanatory knowledge than many other kinds of knowledge, such as that for facts, procedures, or narratives. In the original study, its authors tested how well students could explain the working of devices such as a sewing machine, a can opener, a self-winding watch, a nuclear power plant, or a photocopier. This could well apply to explanatory knowledge of code: algorithms, data structures, designs, interactions, and architecture. Importantly, in programming, explanatory knowledge, which allows reasoning across the software development lifecycle, is a lot more important than facts (can be established with tools), procedures (should be automated), or narratives (are rarely embedded into code).

Finally, the fluency of LLMs makes faulty code appear more trustworthy than it deserves and also feeds another cognitive trait. Consider the diverse ways in which a programmer can err: slips, lapses, mistakes, knowledge-based reasoning failure, rule-based misapplication, cognitive overload, confirmation bias, availability bias, anchoring, overconfidence, abstraction mismatch, inattentional blindness, plan-composition failure, or specification ambiguity. For most, it is probable that a reviewer (especially a more experienced one) may be able to detect the resulting fault by thinking differently. In contrast, AI-generated code is written so as to look plausibly correct, even when it’s faulty. (This is how due to how LLMs work: they generate a series of the next most probable tokens.) This makes it more difficult for a human reviewer to detect a fault in the code.

The plausibility of LLM code gets compounded by a specific trait in the [complex relationship of humans and automation](https://doi.org/10.1518/001872097778543886), _automation bias_: the well-documented tendency of people to place unwarranted trust in automated systems, reducing their own independent verification effort. [A study of automation across diverse critical domains](https://doi.org/10.1006/ijhc.1999.0252) has shown that when automation provides recommendations, people are more likely to accept incorrect suggestions (_errors of commission_, say a duplicated routine) and less likely to detect problems that the automation failed to address (_errors of omission_, e.g. a missing handler or test).

In short, when reviewing AI-generated code, remember that we humans are at a severe disadvantage and try to be even more vigilant.

[Comments](https://www.spinellis.gr/cgi-bin/comment.pl?date=20260523#comments)   [Post](https://bsky.app/intent/compose?text=Why%20reviewing%20AI-generated%20code%20is%20devilishly%20hard%20https%3A%2F%2Fwww.spinellis.gr%2Fblog%2F20260523%20via%20%40CoolSWEng.bsky.social) [Toot!](https://toot.kytta.dev/?text=Why%20reviewing%20AI-generated%20code%20is%20devilishly%20hard%20https%3A%2F%2Fwww.spinellis.gr%2Fblog%2F20260523%20via%20%40CoolSWEng%40mastodon.acm.org)
