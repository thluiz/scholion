---
url: "https://fluxus.io/article/why-your-ai-never-works-on-the-first-try?utm_source=tldrai"
captured_at: "2025-08-12T17:36:30+01:00"
title: "Why Your AI Never Works on the First Try"
domain: "fluxus-io"
---

---
It's 3am. You're staring at ChatGPT, thinking "just one more try."

You've been iterating on the same email for an hour. Each attempt gets slightly closer to sounding human. The tone improves, the awkward phrases decrease, but something's still off. You know you're close - you can feel it - but you have no idea if you're one attempt away or ten.

This is the universal experience of AI power users. That peculiar exhaustion of grinding through iterations, knowing you're making progress but unable to see the destination. Like being stuck on the same level of a video game, except the level changes slightly each time you play it.

I came back to coding after 13 years away. Within weeks I was shipping real systems - the AI's power was obvious. But I noticed something strange. Everything took multiple attempts to get right. Sometimes two, sometimes twenty. Occasionally you'd get lucky on the first try, but that was rare enough to feel like winning the lottery.

At first I thought it was me. Rusty skills, bad prompting, not understanding the tools. But the pattern was everywhere. Emails, proposals, images. And here's the weird part: it only happened when I knew what good looked like. When I ventured into unfamiliar territory, the first output seemed brilliant. When I had expertise, the grinding began.

For months I just accepted this. Everyone does. Multiple revisions of a paragraph that should take two minutes to write. Endless attempts at a Midjourney prompt. By attempt five, you're using caps lock. By attempt ten, you're swearing at it like it's deliberately being obtuse. If there was a human on the other end, HR would be involved.

Then one night, deep into another session, something clicked. This is software. Deterministic, mathematical software. Imagine if Excel took multiple attempts to sum a column. If Gmail needed three tries to send an email. If Spotify required a couple of refreshes before a song would play. You'd think your computer was broken.

But we've normalised this exact behaviour in AI. We've accepted "let me try again" as standard operating procedure.

That night, I started asking a different question. Not "how do I reduce iterations" but "why do iterations exist at all?"

The answer changed everything I understood about what we're actually building.

I started documenting the pattern obsessively. Every AI interaction, I tracked the iterations. Code, emails, images - didn't matter. The variance was maddening. Sometimes two attempts, sometimes twenty. Never predictable.

At first I thought it was randomness - LLMs are probabilistic, temperatures, sampling, all that. The people quick to explain that LLMs are non-deterministic often don't realise that at temperature 0, they're effectively deterministic. Same prompt, same output. GitHub Copilot runs near zero. Claude and GPT in production often run low.

Yet they still require multiple attempts. The randomness wasn't the problem.

I watched what actually happens when you iterate. With code, you get an error, paste it back, the AI patches that specific issue. Another error, another patch. It's not debugging - it's something else. The AI can't see why its original wouldn't work. It needs the error message to navigate from.

Same with writing. You say "too formal" and it lurches into casual slang. "No, back it off" and it swings to corporate speak. You're playing pendulum, trying to dampen the swings until it accidentally lands in the middle.

The AI wasn't learning or understanding. It was doing something more primitive. Something almost... mechanical.

Then I found out I wasn't alone in noticing this. Thoughtworks had just published extensive experiments on autonomous code generation. [**Martin Fowler**](https://www.linkedin.com/in/martin-fowler-com/)'s site featured the work by [**Birgitta Boeckeler**](https://www.linkedin.com/in/birgittaboeckeler/) and her team. These aren't hobbyists. They're distinguished engineers with unlimited resources. They built sophisticated multi-agent systems, reference applications, elaborate workflows. Months of systematic work.

Their conclusion? Human oversight remains essential. They called it "playing whac-a-mole" - every run produced different errors requiring different fixes. They [**documented the pattern exhaustively**](https://martinfowler.com/articles/pushing-ai-autonomy.html).

They just couldn't explain why.

The best engineering minds in the industry had mapped the same territory I was exploring. They saw the constraint but not the cause. Multiple agents didn't help. Better prompting didn't eliminate it. More sophisticated workflows just moved the problem around.

That's when I realised we were all missing something fundamental. Something about the architecture itself.

For weeks, the pattern haunted me. The AI could generate plausible solutions but couldn't see if they'd work. It needed errors to navigate from. It overcorrected, then overcorrected the overcorrection. Always walking, never seeing ahead.

Then, during another late-night session watching the AI fumble through iterations, it hit me. I'd seen this before. Not in AI, but in an old computer science problem.

The traveling salesman problem.

But not the classic version where you can see all the cities and plan the optimal route. This was different. The AI was like a traveling salesman without a map. It could only see the road signs at its current intersection. It couldn't look ahead to plan a route. It could only see which roads left from where it stood and pick the most promising one.

That's exactly what LLMs do. All of generative AI - every neural network generating text, images, or code - has this same constraint.

Every token an LLM generates is selected from adjacent possibilities in probability space. It can't see the complete solution - the working function, the polished email, the image that doesn't scream "AI." It sees only the next most probable token from where it stands. Then the next. Then the next.

The AI isn't "thinking" and then outputting a solution. It's walking through semantic space, one intersection at a time, unable to see beyond the immediate next step. When your code throws an error, that error becomes a new starting position. The AI takes another step from there.

This made everything click. The maddening variance? Sometimes your prompt randomly places the AI close to a working solution - two steps and you're done. Other times, you're in semantic Siberia, twenty iterations from anything usable. And you can't know which until you start walking.

Computer scientists have studied this for decades. They call it "online graph exploration" or "partially observable planning." They've proven that without a map, you're mathematically forced to take longer routes.

AI researchers know LLMs can't plan. The planning community has written papers about it. But here's what nobody had connected: LLMs are literally solving the mapless traveling salesman problem in token space.

Every ChatGPT session. Every coding attempt. Every email revision. It's all the same mathematical constraint manifesting everywhere. We just didn't see it because we were too busy arguing about consciousness to notice we'd built something that navigates blind.

Call it Beatty's Law - earned through too many sessions mapping this particular hell: You never know if you're one iteration away or twenty.

Once you see it, you can't unsee it. Every AI behaviour suddenly makes sense through this lens.

**Why expertise changes how you use AI:** When you know what good looks like, you can see exactly how far the AI is from where it needs to be. Expertise isn't just knowing tools - it's years of building a mental map of quality. A designer sees why the typography fails. A developer sees why the architecture won't scale. A writer sees why the voice is wrong.

This mental map lets experts navigate the AI toward excellence through targeted iteration. But AI is also powerful to people without these maps - not because they can't tell it's producing slop, but because it lets them create things they couldn't before. Different uses, different destinations, same tool.

**Why everything starts as slop:** The centre of the probability distribution - the most average, most generic, most likely starting point. That corporate jargon, that derivative image style, that boilerplate code. That's literally where the AI begins walking from.

Humans have already pattern-matched this slop as lazy. Nobody's impressed by obvious AI output anymore. It has a reputational cost.

With iteration, you can push past slop to mediocre. More iterations might get you to good. And with serious grinding - the kind that leaves you swearing at your screen - you can reach somewhere between very good and superhuman. Output that's better than what you could create alone. Code architectures you wouldn't have conceived. Insights that surprise you.

But you never know if superhuman is two iterations away or two hundred.

**Why scaffolding has limits**: People try to solve iteration with elaborate READMEs, detailed specs, comprehensive prompts. But you're giving directions to something that can still only see one intersection ahead. The AI still has to walk the path. Worse, creating that scaffolding requires its own iteration cycles. The truth is, the scaffolding is as much for us as for the AI - it keeps us from getting lost while we're both wandering through possibility space together.

**Why it feels like gambling:** The variance creates a perfect variable reward schedule. Sometimes you win quickly (close starting position), sometimes you're grinding for hours (distant starting position). Your brain responds exactly like it does to slot machines - that "just one more try" isn't weakness, it's engineered addiction.

But this leads somewhere unexpected: if LLMs are mapless navigators, then what we've built isn't artificial intelligence at all.

Think about what intelligence actually requires. A human expert can picture the destination. They can predict that an approach will fail three steps ahead. They can say "X conflicts with Y" without trying it. They have a map.

AI has none of this. It can't simulate outcomes. It can't see the destination. It can only walk and see what happens. That's not intelligence - that's something else entirely.

So what the fuck have we actually built?

The answer changes everything about how we should think about AI. We're not being replaced by digital minds. We're not on the path to artificial general intelligence. We've built something far stranger and perhaps more important.

We've built cognitive exoskeletons.

## The Cognitive Exoskeleton

Forget everything you've heard about AI replacing humans. That's not what's happening. We're witnessing something far more interesting: the emergence of cognitive exoskeletons.

An exoskeleton doesn't replace your body - it augments it. You wear it. You control it. It amplifies your strength but requires your constant guidance. That's exactly what AI has become.

But let me be clear about "cognitive" here - I mean human cognition. The AI isn't thinking. It has no cognition to speak of. It's amplifying YOUR thinking. You're piloting machinery that extends your mental capabilities while requiring your constant navigation. The tail isn't wagging the dog here - you're in control, exhaustingly so.

Every ChatGPT session, every Cursor interaction, every Midjourney prompt - you're not being automated away. You're strapping on computational machinery. The AI provides raw processing power, vast pattern matching, endless generation. But you provide the intention, the navigation, the quality control. You're the pilot of a system that can walk but cannot see.

This changes everything about knowledge work. You're not a programmer anymore - you're a programming pilot, guiding powerful tools through solution space. Not a writer but a navigator, steering through possibilities toward meaning. Not a designer but a design director, conducting generative systems toward your vision.

The exhaustion people feel isn't from being replaced. It's from the constant piloting required. Every iteration demands judgment. Every output needs evaluation. Every session becomes a dance of guidance and correction. You're not doing less work - you're doing different work. Higher leverage, but requiring constant attention.

This is why senior developers adapted fastest to traditional workflows while juniors invented entirely new ones. Seniors navigate with existing quality maps. Juniors are building different maps altogether - spec-driven development, vibe-coding communities, using AI as a tutor to accelerate learning. The exoskeleton amplifies what you have, but it also helps you build what you don't have yet. This isn't rigid machinery - it's software that shapeshifts to your needs.

For some tasks, this amplification is transformative. You can build systems you couldn't conceive alone. Write at scales you couldn't sustain. Create things that would have taken weeks in hours. The exoskeleton lets you punch far above your weight class.

But you never know if that transformation is two iterations away or two hundred. Sometimes you get lucky and start near excellence. Sometimes you're grinding for hours just to escape mediocrity. The exhaustion is real. The power is real. The constraint is permanent.

We're all exoskeleton pilots now. The question isn't whether AI will replace you. It's whether you're willing to do the work of navigation.

So understanding this means knowing when iteration is worth it.

For production code, for work that matters, for anything where the difference between mediocre and excellent counts - the grinding is worth it. You can build systems you couldn't conceive alone, solve problems that were previously intractable, create at scales you couldn't sustain. It might take an unknown number of iterations, but the outcome justifies the exhaustion.

For internal emails, meeting notes, first drafts? Maybe slop is fine. Maybe a couple of iterations to mediocre. Save your energy for where quality matters.

The mistake is treating all tasks the same - using AI for everything or nothing. The skill is recognising which tasks deserve the grinding and which can live with "good enough."

GPT-5 won't eliminate the constraint. GPT-N won't eliminate it. Scaling helps - bigger models start closer to good outputs more often - but they still can't see the destination. They're still mapless travellers. You can make the salesman faster, give him better shoes, but he still can't see the map.

Multiple agents won't fix it either. Multiple mapless navigators are still mapless. They're just bumping into each other in the dark.

So here's your decoder ring for the AI age:

**Will it require iteration?** Yes. How many? You can't know until you start walking.

**Is it worth the effort?** Depends on what you're building.

**When should you grind?** When excellence matters. When you need something you couldn't create alone.

**When should you accept slop?** When "good enough" is actually good enough.

The future isn't humans being replaced by AI. Every time you fire up ChatGPT, you're hiring a mapless traveling salesman. Whether you guide them to excellence or accept their first guess depends on what you're trying to build.

We're in the age of mandatory iteration. The age of cognitive exoskeletons. The age where humans aren't replaced but transformed into pilots of immensely powerful, fundamentally limited systems.

At least now you know why. And knowing why changes everything about how you navigate.

Welcome to the age where nothing works on the first try.
