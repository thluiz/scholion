---
url: "https://text-incubation.com/AI+code+is+legacy+code+from+day+one"
captured_at: "2025-05-07T09:09:03-03:00"
title: "AI code is legacy code from day one - Text Incubation"
domain: "text-incubation-com"
---

Originally posted to Hacker News - I've included some of the more interesting comments in a section below.

It seems like there are a few stages in the life of a codebase (and/or parts of it), that dictate its likelihood of deep improvement.

1. When something is new, and you're the one who built it: "Oh yeah — we should just change to doing it that way instead"
2. When something is new, and someone else built it: "It was probably done this way because of {recent temporary-but-ambient context}. If necessary, I can consider prioritizing."
3. When something is older, and you're the one who built it: "Oh yeah — we probably should have done it that way. If it becomes necessary to, I can consider prioritizing."
4. When something is older, and someone else built it: "I wonder why it was done that way. Probably only worth revisiting if it becomes an issue."

Software evolves more rapidly under the maintenance of its original creator, and in proportion to how recently it was written.

This is efficient — it would be wasteful to "improve" software that already works, has worked for a while, especially when the risks of introducing major changes are not as comprehensively understood as they would be by the original creator.

Some second-order, AI-oriented, conclusions/formulations:

- AI is "stateless" in an important way, even with its context windows. It can infer why something may have been written in a particular way, but it (currently) does not have access to the actual/point-in-time reasoning the way an actual engineer/maintainer would.
- Every iteration is written by "someone else," and with no more working memory than that of someone rereading your code and building up context from scratch. It ultimately still doesn't remember-remember the circuits that turned the original prompts/inputs into particular outputs.
- AI-generated software starts its life aged, in the last bullet stage — without the benefit of "recency", nor with its original creator as its maintainer. Legacy code.

There's a good chance AI-savvy engineers already solve for this in their workflows; cleverly-constructed prompts and context windows, well-annotated code, etc. The above feel more like the inertial direction of this stuff.

My hunch is that the real reason this won't actually matter, is that "code" itself is a type of state, that prompts + large context windows will replace — increasingly "complex" software will simultaneously run on far fewer lines of code, and more of its functionality will rely on prompts with smarter models. Prompt-generated code seems like a short/medium-term bridge.

People deeper in the AI rabbit-hole likely have a ton of counterarguments + corrections to make — which I'd be interested in hearing!

#### Highlights from Hacker News responses to this post:

> The opening of the article derives from (or at least relates to) Peter Naur's classic 1985 essay "Programming as Theory Building". (That's Naur of Algol and BNF btw.)
>
> Naur argued that complex software is a shared mental construct that lives in the minds of the people who originally build it. Source code and documentation are lossy representations of the program—lossy because the real program (the 'theory' behind the code) can never be fully reconstructed from them.
>
> Legacy code here would mean code where you still have the artifacts (source code and documentation), but have lost the theory, because the original builders have left the team. That means you've lost access to the original program, and can only make patchwork changes to the software rather than "deep improvements" (to quote the OP). Naur gives some vivid examples of this in his essay.
>
> What this means in the context of LLMs seems to me an open question. In Naur's terms, do LLMs necessarily lack the theory of a program? It seems to me there are other possibilities:
>
> - LLMs may already have something like a 'theory' when generating code, even if it isn't obvious to us
> - perhaps LLMs can build such a theory from existing codebases, or will be able to in the future
> - perhaps LLMs don't need such a theory in the way that human teams do
> - if a program is AI-generated, then maybe the AI has the theory and we don't!
> - or maybe there is still a theory, in Naur's sense, shared by the people who write the prompts, not the code.
> - There was an interesting recent article and thread about this:
>
> Naur's "Programming as Theory Building" and LLMs replacing human programmers - https://news.ycombinator.com/item?id=43818169 - April 2025 (129 comments)

> My old boss and I used to defend ourselves to younger colleagues with the argument that "This is how you did it back in the day". Mostly it was a joke, to "cover up" our screw-ups and "back in the day" could be two weeks ago.
>
> Still, for some things we weren't wrong, our weird hacks where do to crazy edge cases or integrations into systems designed in a different era. But we where around to help assess if the code could be yanked or at least attempt to be yanked.
>
> LLM assisted coding could technically be better for technical debt, assuming that you store the prompts along side the code. Letting someone what prompt generated a piece of code could be really helpful. Imagine having "ensure to handle the edge case where the client is running AIX 6". That answers a lot of questions and while you still don't know who was running AIX, you can now start investigating if this is still needed.

> "AI is "stateless" in an important way, even with its context windows. It can infer why something may have been written in a particular way, but it (currently) does not have access to the actual/point-in-time reasoning the way an actual engineer/maintainer would."
>
> CoT fixes this. And in a way, non CoT can retrigger its context by reading the code.
>
> In a similar fashion, engineers remember their context when reading code, not necessarily by keeping it all in their head
