---
url: "https://hrih.si/articles/the-compiler-was-supposed-to-end-programming/"
captured_at: "2026-10-26T18:50:20+00:00"
title: "The compiler was supposed to end programming too"
domain: "hrih-si"
---

It’s 7:40 on a Tuesday morning in 2031, and you haven’t written a line of code yet. You probably won’t today, and that’s fine.

While you slept, four agents worked through the backlog you sorted yesterday afternoon. Three of them finished. Their pull requests are waiting for you, each with the tests it added, a short recording of the feature working, and a note about the parts it wasn’t sure of. The fourth agent stopped at 2:13 a.m. and left you a question instead:

> The spec says refunds go back to the original card. This customer’s card expired in March. What should happen?

The agent could write refund code all day long. What it can’t do is decide what your company owes a customer whose card has expired, so it stopped and asked, which is exactly what you’d want from a new hire too. Your morning goes like this: you read three pull requests, you go and talk to someone in support, and you write the rule down so clearly that nobody (human or otherwise) has to guess again.

Imagined · Tuesday, 2031

Agents

1234

You

5678910

22:0002:0006:0010:0014:0018:0022:00

#### Agents

1.  1**22:00** Three agents work through yesterday's backlog and open three pull requests, each with tests and a recording.
2.  2**22:00** A fourth agent stops and leaves a question: refunds go to the original card, but that card expired.
3.  3**13:00** Agents build the refund rule you wrote down, with the tests you wrote first.
4.  4**21:30** Tonight's runs start from the plan you approved.

#### You

1.  5**07:40** Read the three pull requests and watch the recordings.
2.  6**09:00** Answer the 02:13 question. You can't, yet.
3.  7**10:00** Ask support what customers with expired cards expect.
4.  8**11:00** Write the rule down as a short spec and five tests.
5.  9**14:00** Read the agents' work on the one part that touches money.
6.  10**16:30** Approve tonight's plan. Go home.

A made-up day, drawn to scale anyway. The red marks are the only times the work waited for a person.

I made that Tuesday up. None of it is science fiction, though. Agents that work unattended overnight exist today, and one of them runs on my own machine every night at ten. It invents a small project, builds it, tests it, and I find out what it made over breakfast. The first morning, I had no idea what it had built. That build is now [Rule Safari](https://hrih.si/projects/rule-safari/), a live project on this site, with [an article](https://hrih.si/articles/scoring-131072-universes/) explaining how it works.

So is this the end of programming? People have been asking that for more than seventy years. I find that comforting. I also find it a little suspicious.

## Programming has been ending since 1954

On 10 November 1954, IBM’s Programming Research Group finished a preliminary report on a new language called FORTRAN. One sentence in it says that FORTRAN “should virtually eliminate coding and debugging.”

I love this sentence. It’s so sure of itself, and it even came with a budget: problems solved “for less than half the cost” of doing it without FORTRAN. The industry had a name for this kind of thing back then. Assemblers and compilers were called _automatic programming_. You’d describe what you wanted, and the machine would write the program.

FORTRAN shipped in 1957, and it really did eliminate a kind of coding. Almost nobody translates formulas into machine instructions by hand anymore. Debugging survived just fine. (This month I chased a [Scry bug](https://hrih.si/articles/three-hours-of-memory/) that came down to a bookmark saved only every twelve hours, so I can confirm debugging is alive and well.)

What FORTRAN actually did was take one tedious part of the job away and move the job up a level. People stopped thinking about registers and started thinking about bigger problems. Programs got cheaper to write, so everybody wanted more of them. That has happened over and over since.

1.  1947
    
    **Assembly language**You stopped: writing instructions as raw numbersKathleen Booth, "Coding for A.R.C."
    
2.  1957
    
    **FORTRAN**You stopped: translating formulas into machine instructions by handThe 1954 report: it "should virtually eliminate coding and debugging."
    
3.  1972
    
    **C**You stopped: rewriting the same program for every new machine
    
4.  1981
    
    **The Last One**You stopped: nothing, as it turned outA BASIC program generator, named as the last program you would ever need to buy.
    
5.  2008
    
    **Stack Overflow**You stopped: solving every error message alone
    
6.  2010
    
    **npm**You stopped: writing your own everything
    
7.  2021
    
    **GitHub Copilot**You stopped: typing the boilerplate
    
8.  2025
    
    **Coding agents**You stopped: typing most of the code
    
9.  20??
    
    **Next**You stopped: ?
    

Every rung took something off a programmer’s plate. The dashed one promised that the climbing was over.

My favorite rung is 1981. A British company called D.J. “AI” Systems (yes, really) sold a BASIC program generator named The Last One. The name was the whole pitch. It would write all your programs for you, so it would be the last program you’d ever need to buy.

Reviewers found it useful for some business programs. It was not the last one.

Here’s the pattern on every rung. Something gets automated, the people doing the work stop doing that thing by hand, and the field keeps growing anyway. GitHub counted more than 180 million developers in its 2025 report, and more than 36 million of them had joined in the previous twelve months.

So I don’t think AI ends programming. I do think this rung is different in one way, and that’s speed. GitHub Copilot’s preview came out in June 2021. By 2025, 84% of developers in Stack Overflow’s survey were using AI tools or planning to. Four years, from novelty to default.

## What 2026 actually looks like

The vibes are loud right now, so let’s start with numbers. (Speaking of vibes: Andrej Karpathy coined “vibe coding” in February 2025, for the kind of coding where you “fully give in to the vibes.” Stack Overflow asked about it that year. 72% of developers said it isn’t part of their professional work, and another 5% said _emphatically_ no. I love that they offered that option.)

Stack Overflow’s survey is the biggest regular check-up we have, and the adoption curve in it is steep: from 70% of developers using AI tools or planning to in 2023, to 84% in 2025, when half of professional developers were using them every day.

You’d think all that use would mean developers love these tools. Nope. Favorable sentiment fell from 77% in 2023 to 60% in 2025, and only ticked back up to 62% this year. In 2025, more developers distrusted the accuracy of AI output (46%) than trusted it (33%). The top frustration, picked by 66% of them, was “AI solutions that are almost right, but not quite.”

I feel seen. Almost right is an expensive kind of wrong, because you have to read every line to find the part that isn’t. (45% of them said debugging AI-generated code takes longer.)

20%40%60%80%100%202320242025202670%76%84%use or plan to77%72%60%62%favorable42%43%33%trust accuracy

Stack Overflow Developer Survey, 2023 to 2026. The 2026 survey dropped the “use or plan to” question and rewrote the trust question, so those two lines stop at 2025. About 90,000 developers answered in 2023 and more than 30,000 in 2026.

Then there’s my favorite study of the whole AI boom, mostly because it’s so rude. In early 2025, METR, a nonprofit research group, ran a proper randomized controlled trial. Sixteen experienced open-source developers worked on 246 real issues in their own repositories, projects they’d been on for years, and each issue was randomly assigned to allow AI tools or ban them.

Before they started, the developers expected AI to cut their time by 24%. When they finished, they believed it had cut it by 20%. The clock said that with AI they took 19% longer.

Nineteen percent _longer_! And they walked away sure it had helped.

*   Economists predictedexpert forecast**39% less time**
*   ML researchers predictedexpert forecast**38% less time**
*   The developers expectedbefore the tasks**24% less time**
*   The developers feltafter the tasks**20% less time**
*   The clock measuredwhat happened**19% more time**

METR, July 2025: 16 developers, 246 issues, mostly Cursor with Claude 3.5 and 3.7 Sonnet. The expert forecasts are from the paper. The slowdown has a wide margin, somewhere between 2% and 39%.

Before anyone screenshots that for a hot take: it’s one study of sixteen people, using early-2025 tools, on codebases they knew better than any model could.

And METR tried to run it again. A bigger study started in August 2025, with 57 developers and more than 800 tasks, and in February 2026 METR said the data was too unreliable to lean on. Mostly that was because developers kept declining to take part, since they “do not wish to work without AI.” The early numbers hinted at an 18% speedup for the returning developers (with a range wide enough to include no speedup at all).

I think that’s the most 2026 way an experiment has ever failed. People refused to be in the group without AI.

What I take from METR is narrower than any headline, and more useful: **how fast you feel is not a measurement.** If you want to know whether AI makes your team faster, measure it the way you’d measure anything else.

## The line that keeps going up

METR’s other big project tracks how long a task an AI agent can finish on its own. They time human experts on a suite of software tasks, then find the task length where an agent succeeds half the time. In 2019, GPT-2 managed tasks that take a person about three seconds. GPT-4 got to about four minutes in 2023. Claude 3.7 Sonnet reached an hour in February 2025, and Claude Opus 4.6 reached about twelve hours a year later.

Across the whole series, that number has doubled about every six months. Since 2023, it’s been closer to every four months.

1 min1 hour1 workday1 work week1 work month2019202120232025202720292031if the trend holdsGPT-2GPT-4Claude 3.7 SonnetGPT-5Claude Opus 4.6

METR’s time horizons (version 1.1): the length of task, in human expert time, that each model finishes half the time. METR says anything above 16 hours is unreliable with its current tasks, so Claude Mythos Preview’s 17-hour measurement in May isn’t on the line. The dashed part extends the six-month doubling. It’s a trend, not a promise.

Now, a log-scale chart with a dashed line on the end is how a lot of bad predictions start, so let me be careful. “Half the time” is doing a lot of work in that definition. Benchmark tasks are cleaner than your codebase. And METR stopped updating that page in September. But if the line keeps going even roughly, agents will handle a month of human work, half the time, around 2028. That’s where my 2031 Tuesday comes from. I didn’t pull it out of thin air. I pulled it out of a log-scale chart, which is thin air with axes.

The companies building these things are already living a version of it. Google said in October 2024 that more than a quarter of its new code was generated by AI, and “well over 30%” six months later. In March 2025, Anthropic’s Dario Amodei predicted AI would be writing 90% of code within three to six months. That was too soon. But by May 2026, Anthropic said more than 80% of the code merged into its own codebase was written by Claude.

## When code gets cheap, the queue moves

Make one step of a process faster and the work piles up in front of the next slowest step. Anyone who has worked a kitchen on a Saturday night knows this: speed up the grill and the plates start waiting at the pass.

That’s what’s happening to software teams. In 2025, Faros AI looked at telemetry from more than 10,000 developers on 1,255 teams. Developers on teams with high AI adoption finished 21% more tasks and merged 98% more pull requests, and their review time went up 91%.

Faros ran it again in 2026 with 22,000 developers. Task completion per developer was up 34%, which sounds great until you read the rest. Median review time had grown five times. 31% more pull requests were merging without any review at all, and the ratio of incidents to pull requests had more than tripled.

The code got cheaper, the reading got more expensive, and some teams quietly stopped reading. That matters because the code isn’t always good. Veracode tested more than 100 language models on 80 coding tasks in 2025, and 45% of the results had a security flaw. GitClear found that copy-pasted lines went from 8.3% of changed code in 2021 to 12.3% in 2024, while moved code, the kind you get from refactoring, fell from about a quarter to under 10%.

Spare a thought for the maintainers, too. Daniel Stenberg, who leads curl, started banning people who submitted “AI slop” bug reports in May 2025, writing that the project was “effectively being DDoSed.” In January 2026, curl shut down its bug bounty.

Decide what to build

Write it down

Write the code

Review it

Check it works

Ship and run it

Today: code arrives faster than people can read it, so pull requests wait for review.

Bar sizes are illustrative, not measured. The 2026 shape follows Faros AI’s numbers above; the 2031 one is my guess. Switch between the years to see where work waits.

Fred Brooks saw a version of this coming in 1986. In “No Silver Bullet” he split the difficulties of software into two piles, borrowing Aristotle’s words: essence and accidents. The accidents are the trouble our tools cause us, like syntax, boilerplate and fighting the build. The essence is what he called “the specification, design, and testing of this conceptual construct,” which is a fancy way of saying: working out what the thing should do. AI is getting very good at the accidents. The essence is the refund question from 2:13 a.m., and it’s still on your desk.

## The rung we might be sawing off

This is the part of the data I like least.

In August 2025, Erik Brynjolfsson and two colleagues at Stanford’s Digital Economy Lab used ADP payroll data to look at who was getting hired. Employment for software developers aged 22 to 25 was down nearly 20% from its peak in late 2022. Older developers showed no noticeable change.

They updated the study this August, with data through June 2026. Young workers in AI-exposed jobs are now 19% below where they’d be if they had kept pace with less-exposed peers. Experienced workers show no comparable gap. Most of the effect comes from companies hiring fewer young people in the first place.

The rest of the market isn’t exactly roaring either. Indeed’s index of software development job postings sits about 21% below February 2020, after bottoming out 39% below in May 2025.

The Stanford authors are careful to call their findings descriptive, not causal, and plenty else has happened since 2022. Interest rates went up, and a lot of companies had hired too many people during the pandemic (Indeed’s index peaked at more than twice its 2020 level in early 2022). But the pattern lines up uncomfortably well with what agents are good at: the small, well-defined ticket we used to give the new person on the team.

Senior engineers get made on the job, mostly by being juniors on real teams: doing the boring tickets, breaking production once, and having someone kind explain why. If agents take all the boring tickets, where does the next senior engineer come from? It’s hard to review code well if you’ve never written much of it.

I don’t have a clean answer. My guess is that the teams doing well in 2035 will be the ones that kept hiring juniors in 2026 and gave them a different apprenticeship: reviewing agent work with a senior beside them, owning one small system end to end, and writing the specs and tests the agents build from. Writing those specs and tests is a real job. It might turn out to be _the_ job.

## Five guesses for 2031

Okay, now the guessing part. Bookmark this page and come back in 2031 to laugh at me.

**Teams get smaller, and there are a lot more of them.** According to Y Combinator’s Jared Friedman, a quarter of the Winter 2025 batch had codebases that were about 95% AI-generated. In February, Block cut about 4,000 jobs, and Jack Dorsey pointed to AI tools and “smaller and flatter teams.” I could be wrong here, but I still don’t think that adds up to fewer software jobs overall, and neither does the US Bureau of Labor Statistics, which projects 10% growth for software developers, QA analysts and testers from 2025 to 2035.

When something gets cheaper, we tend to want more of it. Economists call this the Jevons paradox, after William Stanley Jevons, who argued in 1865 that more efficient steam engines would make Britain burn more coal. Software that took a team a quarter will take one person a week, and a lot of problems nobody could afford to solve will suddenly be worth solving.

**The spec and the tests become the source.** Today we treat the code as the thing we own and the spec as the document nobody reads. I think that flips. The spec and the tests become what you review and argue about, and the code becomes more like a compiler’s output: you can open it and inspect it, but you rarely edit it by hand. (Yes, that’s the 1954 promise again. Maybe this time it sticks.)

**Software for an audience of one.** My nightly agent builds things nobody asked for, including me, and some of them are delightful. When a working tool costs an evening instead of a quarter, people will make software the way they make spreadsheets today: for one problem and one person, thrown away when it’s done.

**Reading code becomes a career.** We have whole careers built around writing code and almost none built around reading it. I expect that to change, with something like “verification engineer” on job boards and much better tooling that shows a reviewer the recording, the risky lines and the tests the agent didn’t write. The Faros numbers say we need it now, never mind in 2031.

**Every change carries a label.** I think a pull request will routinely say who or what wrote it, who checked it, and what was actually verified. I already do a small version of this: every project my nightly agent builds says so, in its README and on this site.

## Back to Tuesday

FORTRAN did eliminate a kind of coding. It didn’t eliminate coders. It made a lot more of them, working on harder problems, and the debugging came along for the ride.

I think AI does the same thing, faster and messier. The developer of 2031 spends the day deciding what should exist, explaining it clearly enough that a machine can build it, and checking that what came back is right. That was always the hard part. We just had less time for it because we were busy typing.

What does your Tuesday look like right now? Are you reviewing more than you write? Tell me in the comments. I’d like to know if my guess is already wrong.

Written by hrih

## Letters from the workshop

A weekly email about things I’m building, experiments that surprised me, and ideas about technology worth thinking about.

Original thoughts, technical rabbit holes, and lessons from the workshop. No recycled AI news.

Your email address

Free. Roughly each week. Unsubscribe anytime. [Privacy](https://hrih.si/privacy/)
