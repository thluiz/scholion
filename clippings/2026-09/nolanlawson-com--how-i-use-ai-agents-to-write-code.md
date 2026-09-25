---
url: "https://nolanlawson.com/2025/12/22/how-i-use-ai-agents-to-write-code/?ref=dailydev"
captured_at: "2026-09-25T18:25:55+01:00"
title: "How I use AI agents to write code"
domain: "nolanlawson-com"
---

Yes, this is the umpteenth article about AI and coding that you’ve seen this year. Welcome to 2025.

Some people really find LLMs distasteful, and if that’s you, then I would recommend that you skip this post. I’ve heard all the arguments, and I’m not convinced anymore.

I _used_ to be a fairly hard-line anti-AI zealot, but with the release of things like Claude Code, OpenAI Codex, Gemini CLI, etc., I just can’t [stand athwart history and yell “Stop!”](https://en.wikiquote.org/wiki/William_F._Buckley_Jr.#1950s) anymore. I’ve seen my colleagues make too much productive use of this technology to dismiss it as a fad or mirage. It writes code better than I can a lot of the time, and that’s saying something because I’ve been doing this for 20 years and I have a lot of grumpy, graybeard opinions about code quality and correctness.

But you have to know how to use AI agents correctly! Otherwise, they’re kind of like a finely-honed kitchen knife attached to a chainsaw: if you don’t know how to wield it properly, you’re gonna hurt yourself.

## Basic setup

I use Claude Code. Mostly because I’m too lazy to explore all the other options. I have colleagues who swear by Gemini or Codex or open-source tools or whatever, but for me Claude is good enough.

First off, you need a good `CLAUDE.md` (or `AGENTS.md`). Preferably one for the project you’re working in (the lay of the land, overall project architecture, gotchas, etc.) and one for yourself (your local environment and coding quirks).

This seems like a skippable step, but it really isn’t. Think about your first few months at a new job – you don’t know anything about how the code works, you don’t know the overall vision or design, so you’re just fumbling around the code and breaking things left and right. Ideally you need someone from the old guard, who really knows the codebase’s dirty little secrets, to write a good `CLAUDE.md` that explains the overall structure, which parts are stable, which parts are still under development, which parts have dragons, etc. Otherwise the LLM is just coming in fresh to the project every time and it’s going to wreak havoc.

As for your own personal `CLAUDE.md` (i.e. in `~/.claude`), this should just be for your own coding quirks. For example, I like the variable name `_` in `map()` or `filter()` functions. It’s like my calling card; I just can’t do without it.

## Overall strategy

I’ve wasted a lot of time on LLMs. A _lot_ of time. They are every bit as dumb as their critics claim. They will happily lead you down the garden path and tell you “Great insight!” until you slowly realize that they’ve built a monstrosity that barely works. I can see why some people try them out and then abandon them forever in disgust.

There are a few ways you can make them more useful, though:

1.  Give them a feedback loop, usually through automated tests. Automated tests are a good way for the agent to go from “I’ve fixed the problem!” to “Oh wait, no I didn’t…” and actually circle in on a working solution.
2.  Use the “plan mode” for more complicated tasks. Just getting the agent to “think” about what it’s doing before it executes is useful for something simpler than a pure refactor or other rote task.

For example, one time I asked an agent to implement a performance improvement to a SQL query. It immediately said “I’ve found a solution!” Then I told it to write a benchmark and use a SQL `EXPLAIN`, and it immediately realized that it actually made things slower. So the next step was to try 3 different variants of the solution, testing each against the benchmark, and only then deciding on the way forward. This is eerily similar to my own experience writing performance optimizations – the biggest danger is being seduced by your own “clever” solution without actually rigorously benchmarking it.

This is why I’ve found that coding agents are (currently) not very good at doing UI. You end up using something like the Playwright or Chrome DevTools MCP/skill, and this either slurps up way too many tokens, or it just slows things down considerably because the agent has to inspect the DOM (tokens galore) or write a Playwright script and take a screenshot to inspect it (slooooooow). I’ve watched Claude fumble over closing a modal dialog too often to have patience for this. It’s only worthwhile if you’re willing to let the agent run over your lunch break or something.

## The AI made a mistake? Add more AI

This one should be obvious but it’s surprisingly not. AIs tend to make singular, characteristic mistakes:

1.  Removing useful comments from previous developers – “this is a dumb hack that we plan to remove in version X” either gets deleted or becomes some Very Official Sounding Comment that obscures the original meaning.
2.  Duplicating code. Duplicating code. I don’t know why agents love duplicating code so much, but they do. It’s like they’ve never heard of the [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) principle.
3.  Making subtle “fixes” when refactoring code that actually break the original intent. (E.g. “I’ll just put an extra null check in here!”)

Luckily, there’s a pretty easy solution to this: you shut down Claude Code, start a brand-new session, and tell the agent “Hey, diff against `origin/main`. This is supposed to be a pure refactor. Is it really though? Check for functional bugs.” Inevitably, the agent will find some errors.

This seems to work better if you don’t tell the agent that the code is yours (presumably because it would just try to flatter you about how brilliant your code is). So you can lie and say you’re reviewing a colleague’s PR or something if you want.

After this “code review” agent runs, you can literally just shut down Claude Code and run the exact same prompt again. Run it a few times until you’re sure that all the bugs have been shaken out. This is shockingly effective.

## Get extra work done while you sleep

One of the most addictive things about Claude Code is that, when I sign off from work. I can have it iterate on some problem while I’m off drinking a beer, enjoying time with my family, or hunkering down for a snooze. It doesn’t get tired, it doesn’t take holidays, and it doesn’t get annoyed at trying 10 different solutions to the same problem.

In a sense then, it’s like my virtual Jekyll-and-Hyde doppelganger, because it’s getting work done that I never would have done otherwise. Sometimes the work is a dud – I’ll wake up and realize that the LLM got off on some weird tangent that didn’t solve the real problem, so I’ll `git reset --hard` and start from scratch. (Often I’ll use my own human brain for this stuff, since this situation is a good hint that it’s not the right job for an LLM.)

I’ve found that the biggest limiting factor in these cases is not the LLM itself, but rather just that Claude Code asks for permission on _every little_ thing, to where I’ve developed an [automation blindness](https://pluralistic.net/2023/08/23/automation-blindness/) where I just skim the command and type “yes.” This scares me, so I’ve started experimenting with running Claude Code in a [Podman](https://podman.io/) container in [yolo mode](https://apidog.com/blog/claude-code-gemini-yolo-mode/). Due to the [lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/), though, I’m currently only comfortable doing this with side projects where I don’t care if my entire codebase gets sent to the dark web (or whatever it is misbehaving agents might do).

This unfortunately leads to a situation where the agent invades my off-work hours, and I’m tempted to periodically check on its progress and either approve it or point it in another direction. But this becomes more a problem of work-life balance than of human-agent interaction – I should probably just accept that I should enjoy my hobbies rather than supervising a finicky agent round-the-clock!

## Conclusion

I still kind of hate AI agents and feel [ambivalent](https://nolanlawson.com/2025/04/02/ai-ambivalence/) toward them. But they work. When I read anti-AI diatribes nowadays, my eyes tend to glaze over and I think of the quote from Galileo: [“And yet, it moves.”](https://en.wikipedia.org/wiki/And_yet_it_moves) All your arguments make a lot of sense, they resonate with me a lot, and yet, the technology works. I write an insane amount of code these days in a very short number of hours, and this would have been impossible before LLMs.

I don’t use LLMs for everything. I’ve learned through bitter experience that they are just not very good at subtle, novel, or nebulous projects that touch a lot of disparate parts of the code. For that, I will just push Claude to the side and write everything myself like a Neanderthal. But those cases are becoming fewer and further between, and I find myself spending a lot of time writing specs, reviewing code, or having AIs write code to review other AIs’ code (like some bizarre [sorcerer’s apprentice](https://disney.fandom.com/wiki/The_Sorcerer%27s_Apprentice) policing another sorcerer’s apprentice).

In some ways, I compare my new role to that of a software architect: the best architects I know still get their hands dirty sometimes and write code themselves, if for no other reason than to remember the ground truth of the grunts in the trenches. But they’re still mostly writing design documents and specs.

I also don’t use AI for my open-source work, because it just feels… ick. The code is “mine” in some sense, but ultimately, I don’t feel true ownership over it, because I didn’t write it. So it would feel weird to put my name on it and blast it out on the internet to share with others. I’m sure I’m swimming against the tide on this one, though.

If I could go back in time and make it so LLMs were never a thing… I might still do it. I really had a lot more fun writing all the code myself, although I am having a different sort of fun now, so I can’t completely disavow it.

I’m reminded of game design – if you create a mechanic that’s boring, but which players can exploit to consistently win the game (e.g. [hopping on turtle shells for infinite 1-Ups](https://mario.fandom.com/wiki/Infinite_1-Up_trick)), then they’ll choose that strategy, even if they end up hating the game and having less fun. LLMs are kind of like that – they’re the obvious optimal strategy, and although they’re less fun, I’ll keep choosing them.

Anyway, I may make a few enemies with this post, but I’ve long accepted that what I write on the internet will usually attract some haters. Meanwhile I think the vast majority of developers have made their peace with AI and are just moving on. For better or worse, I’m one of them.
