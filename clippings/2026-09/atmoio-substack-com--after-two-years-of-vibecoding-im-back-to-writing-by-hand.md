---
url: "https://atmoio.substack.com/p/after-two-years-of-vibecoding-im?utm_source=weeklyfoo&utm_medium=email&utm_campaign=weeklyfoo"
captured_at: "2026-09-23T14:33:50+01:00"
title: "After two years of vibecoding, I'm back to writing by hand"
domain: "atmoio.substack.com"
---
Discover more from Mo Bitar
Exploring what AI actually is
Over 2,000 subscribers
Subscribe
By subscribing, you agree Substack's Terms of Use, and acknowledge its Information Collection Notice and Privacy Policy.
Already have an account? Sign in
After two years of vibecoding, I'm back to writing by hand
MO BITAR
JAN 26, 2026
151
70
11
Share

Most people’s journey with AI coding starts the same: you give it a simple task. You’re impressed. So you give it a large task. You’re even more impressed.

You open X and draft up a rant on job displacement.

If you’ve persisted past this point: congratulations, you understand AI coding better than 99% of people.

Serious engineers using AI to do real work and not just weekend projects largely also follow a predictable development arc.

Still amazed at the big task you gave it, you wonder if you can keep giving it bigger and bigger tasks. Maybe even that haunting refactor no one wants to take on?

But here’s where the curtain starts to crinkle.

On the one hand, you’re amazed at how well it seems to understand you. On the other hand, it makes frustrating errors and decisions that clearly go against the shared understanding you’ve developed.

You quickly learn that being angry at the model serves no purpose, so you begin to internalize any unsatisfactory output.

“It’s me. My prompt sucked. It was under-specified.”

“If I can specify it, it can build it. The sky’s the limit,” you think.

So you open Obsidian and begin drafting beefy spec docs that describe the feature in your head with impressive detail. Maybe you’ve put together a full page of a prompt, and spent half an hour doing so.

But you find that spec-driven development doesn’t work either. In real life, design docs and specs are living documents that evolve in a volatile manner through discovery and implementation. Imagine if in a real company you wrote a design doc in 1 hour for a complex architecture, handed it off to a mid-level engineer (and told him not to discuss the doc with anyone), and took off on vacation.

Not only does an agent not have the ability to evolve a specification over a multi-week period as it builds out its lower components, it also makes decisions upfront that it later doesn’t deviate from. And most agents simply surrender once they feel the problem and solution has gotten away from them (though this rarely happens anymore, since agents will just force themselves through the walls of the maze.)

What’s worse is code that agents write looks plausible and impressive while it’s being written and presented to you. It even looks good in pull requests (as both you and the agent are well trained in what a “good” pull request looks like).

It’s not until I opened up the full codebase and read its latest state cover to cover that I began to see what we theorized and hoped was only a diminishing artifact of earlier models: slop.

It was pure, unadulterated slop. I was bewildered. Had I not reviewed every line of code before admitting it? Where did all this...gunk..come from?

In retrospect, it made sense. Agents write units of changes that look good in isolation. They are consistent with themselves and your prompt. But respect for the whole, there is not. Respect for structural integrity there is not. Respect even for neighboring patterns there was not.

The AI had simply told me a good story. Like vibewriting a novel, the agent showed me a good couple paragraphs that sure enough made sense and were structurally and syntactically correct. Hell, it even picked up on the idiosyncrasies of the various characters. But for whatever reason, when you read the whole chapter, it’s a mess. It makes no sense in the overall context of the book and the preceding and proceeding chapters.

After reading months of cumulative highly-specified agentic code, I said to myself: I’m not shipping this shit. I’m not gonna charge users for this. And I’m not going to promise users to protect their data with this.

I’m not going to lie to my users with this.

So I’m back to writing by hand for most things. Amazingly, I’m faster, more accurate, more creative, more productive, and more efficient than AI, when you price everything in, and not just code tokens per hour.

You can follow me on X @atmoio, where I post a few times a week about agentic coding.

You can watch the video counterpart to this essay on YouTube:

Thanks for reading! Subscribe for free to receive new posts and support my work.

Subscribe
151 Likes
∙
11 Restacks
151
70
11
Share
