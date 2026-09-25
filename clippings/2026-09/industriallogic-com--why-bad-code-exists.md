---
url: "https://www.industriallogic.com/blog/why-bad-code-exists/?ref=dailydev"
captured_at: "2026-09-25T22:28:15+01:00"
title: "Why Bad Code Exists"
domain: "industriallogic-com"
---

_“How dare you call my code **bad**! <gnarl> <gnash>”_

We’ve all had the experience of opening up a source file where everything just makes sense. Nothing is surprising or confusing, and we can easily make changes. Perhaps there is some passage that we don’t immediately grok, but when we reason it out, we’ve happily learned a valuable skill or technique. We’ll call this [good code](https://www.industriallogic.com/blog/code-virtues-explained/). It is profitable.

We’ve all also encountered code that’s just the opposite–it’s hard to read, hard to follow, and difficult to change. On puzzling through a confusing passage, all we get out of the deal is an understanding of what that difficult chunk of code does; there is nothing to raise our skill level. This is **_bad_** code. It is not only unprofitable, it increases costs for those who must later work on it.

![An aged boat aground on the beach, that has a deteriorated structure.](https://www.industriallogic.com/img/blog/2022-02-11-why_bad_code_exists/derelict-ship.png)

We don’t believe programmers intentionally seek to cause pain. Pretty much [everyone is just trying to do a good job](https://retrospectivewiki.org/index.php?title=The_Prime_Directive) and be helpful. Still, we all write good code and bad code. We learn. We fix things. Let’s move on and not sweat the labels so much.

### No continuous (active) review process

Back in our solo programming days, we’d whip up code all afternoon, then head into a test/fix cycle near day end. We’d look at our working code with pride–”gosh, that looks good”–then integrate it. Pull reviews weren’t really a thing back then, though sometimes our code would endure a semi-formal review process. We were often surprised and offended when others didn’t agree that our code was wonderfully made.

Code written by a solo developer makes a lot of sense to its author… at least while it’s fresh in their head. But others usually find it harder to follow–and that later includes the developer themself. This can even be true when the original developer tried hard to keep code clear via refactoring.

Post facto (_not_ active) review processes come with a host of challenges:

*   With only a sole reviewer and a closed process, the whole codebase can become subject to the whims of one person.
*   The review process can devolve into a gate slowing the flow to production, particularly when the team insists on a large number of reviewers (which is one potential reaction to the previous concern).
*   Most developers find post facto reviews a distracting nuisance, and thus minimize their efforts on them. The resulting rubber-stamp process creates false confidence and pointless delay.
*   Even with the right number of folks each trying hard, post facto reviews typically miss deeper problems. Reviewers weren’t privy to the deep conversations and decisions that were distilled into the code, and often offer only surface-level complaints as a result.
*   Even when significant problems are found, it’s often too late and too expensive to fix them. A cycle of code/review/rewrite/re-review isn’t effective. Nor is code/review/release-bad-code.

We want to instead examine the code, learn from it, propose alternatives, improve it, and grow the skills of the whole team _all at the same time_. A review process is an opportunity for rich communal learning.

An active review process like mob or pair programming dramatically reduces the potential for inscrutable or otherwise bad code to escape our development session. Errors are spotted and corrected before we move on. “[Given enough eyeballs, …](https://en.wikipedia.org/wiki/Linus%27s_law)”

_This bad code exists because it was the product of one person’s cleverness, rather than a solution the entire team has blessed._

### No editing process

When writing, your first job is to get your ideas onto the page. But those first thoughts of yours are almost never expressed in a way that is crystal clear to others. Your second job, then, is to edit the first draft so that it makes sense to readers. All writers, even the great ones, review and edit their prose.

Programming should work no differently: Once you get a brilliant bit of code working, you must edit, or _refactor,_ the resulting code. Why? Because it’s easy to introduce numerous design flaws, both small and large, in every few lines of code. You refactor to fix these inevitable deficiencies, to make the code less costly for others to understand and maintain.

Too many developers don’t have an ingrained editing process, however. They get the code working, then move on: “We need to start the next assignment.”

There’s also little impetus to change code once you get it working. “If it ain’t broke, don’t fix it”… because fixing it increases your likelihood of breaking other things without even knowing it.

In contrast, test-driven development (TDD) is one possible disciplined approach that insists on code editing every few minutes. The built-in refactoring step of TDD allows developers to maintain a high level of quality, rather than yield to the typical slow-but-sure degradation of a codebase.

_This bad code exists because it represents only an initial draft, and not an edited final product._

### Insufficient technical knowledge

When we work with “hyperproductive” folks, we find they have three key characteristics. Developers lacking any one of these characteristics lack what’s needed to efficiently produce code that works without unintended consequences:

*   **Knowledge and understanding of the technical stack**. When we don’t understand the stack well enough, our work can take the form of overly-complex and/or fragile work-arounds (hacks). Not only does this foster errors, it also results in convoluted, rigid, bad code.
*   **Disciplined, habitual use of quality practices.** Habits and practices like TDD, small steps, refactoring, or ensemble programming move us toward a disciplined, engineering approach to software development. These good habits don’t slow us down; they power us up and allow us to produce good code quickly and sustainably.
*   **Key understandings of software design principles**. Not adhering to long-established software design principles is a sure way to dramatically increase the costs of maintaining systems. Unfortunately, we’ve moved into what seems to be a post-design era. Modern development processes have been misinterpreted to the point where we’ve heard things like “agile says we must not do design.”
    
    To us, the accumulated wisdom of most developers seems like a random collection of acquired experience rather than a consistent and holistic design perspective. Many once learned about such a perspective, but over time replaced its legitimate principles with stories based on contextual biases–i.e. what they managed to get working at one time. Success can encourage the logical fallacy of hasty generalization.
    
    Undisciplined code resulting from a defective or incomplete understanding of software design creates immediate costs. It takes longer to navigate, understand, and maintain code as the result of things like poor naming, overly-complex logic, redundant logic, poor organization with misplaced responsibilities, and complex dependency chains.
    
    For many, that significant accomplishment of “making it work” is good enough. As a result, it’s usually tough to convince them that their code is only going to make it harder on others.
    

The importance of maintaining the quality of a codebase is well-documented, as are the techniques to do so, but far too few developers engage with the literature.

_This bad code exists because it was created by people who didn’t know enough to build it well._

### Time pressure

When we ask why people have defects, or have neglected their codebase in any way, the near-universal answer is “we were in a hurry.” Often they provide a legitimate reason for their hurry. Some deadlines can’t be moved.

Managers pressure people to turn around their tasks more quickly, to complete things that are started, to move on to the next thing, and to address completed-but-defective work: all at the same time; all Right Now. Why? Because the managers themselves are under pressure to deliver, as are _their_ managers, as are _theirs_.

Some aspects of time pressure are positive:

*   It helps us learn to be more efficient.
*   It reminds us that our users need solutions to problems sooner.
*   It keeps our sponsors and stakeholders happy.

But far more are negative:

*   It instills fear of being fired or reprimanded for missing a date.
*   It motivates us to cut corners.
*   It creates resentment when deadlines are bogus–for something other than the delivery of true business value (“we’ve got to finish this document by Monday”).
*   It fosters assessments of people (for promotion, raises, or even continued employment) based on how busy they look rather than how productive they are.
*   It results in naive managers trying to make up time by pushing people harder, particularly when delays are built into the company’s software process.
*   It creates more work for others down the line, particularly in the code.
*   It prevents us from learning what we should. While we know that learning a tool, technique, or framework can make us more efficient _and_ effective, we know that it will take away precious time **now**. We want to be experts, but we aren’t sure we can afford the time to get there. As a result, we and our teams muddle through.

There is always pressure to begin, perform, and complete work. But a strategy of rushing and cutting corners can only work for a while before it collapses. Eventually, there is so much half-done and hastily-dispatched work piled up that it becomes difficult to get anything done at all.

_This bad code exists because it was the quickest thing that a person under pressure could accomplish without learning anything new._

### Inadequate technical controls/fear

Nobody wants to be the scapegoat for a production disaster, particularly when it involves changing code that was working before. You try to add functionality by minimizing the impact to existing code out of fear–even if you know that your changes violate every principle of software design ever written. You pass around another boolean flag; you deepen a nest of _if_ statements, you duplicate a complex function in order to add a tiny new behavior–because that’s safer than doing _the right thing_. The right thing involves re-shaping to well-designed code, a highly risky activity without test controls.

Bad code got you into this mess. More bad code won’t get you out of it.

What to do? You can initiate a rewrite, which is tricky: Without requirements captured in tests, it’d take forever to determine [every last thing the rebuilt system needs](https://www.hyrumslaw.com/) to do. As you rewrite, new requirements will keep coming. Good luck keeping up with implementing them in the old (live) system as well as the new.

Alternatively, you can start adding [characterization tests](https://en.wikipedia.org/wiki/Characterization_test) to support refactoring the code, which can foster more tests and more good code. You can eventually get the whole system under the safety of a significant umbrella of automated tests. It sounds like a lot of work, but not getting things under control also sounds like a lot of work… and a lot of fearful risk. No one should have to live in fear.

A good suite of tests provides you with high confidence to change code, by revealing most errors before they end up in production and usually before they can escape your desk. These protections prevent financial loss and catastrophic runtime failures.

_This bad code exists because it’s the product of someone afraid to do the right thing._

### Lack of care

Yes, there are people who literally _do not care_ if their code is bad. It’s hard to imagine for most of us, we know.

Why would someone take a job where they have no interest in being skillful? Ah. Imagine the jobs you might have taken as a teenager–slinging fast food, counting change at a register, or hefting packages at a warehouse. You knew you weren’t in it for the long haul, so you learned enough to draw a paycheck, but you didn’t make it a specialty or become an expert at the work. You learned enough to not get canned, hoping to move on to better jobs.

Many things in software demand attention, but people have to choose where to focus–to each, what they consider the _real work_. The other things are the _silliness_ that they have to endure so that they can get on with the real work. Time cards, status reporting, writing unit tests after-the-fact, and pull requests are a few things that people drop into the silliness category.

Fairly common are those who only know enough, say, HTML + CSS + Javascript to be able to survive making changes in their team’s front-end environment, partly because they only occasionally find themselves working in it. Because these folks aren’t deeply invested in the environment, they muddle through the work rather than learn enough to do it properly. Certainly many of these folks care, or want to care; we might graciously chalk up their bad code to time pressure. They need the room and the permission to care.

_This bad code exists because someone didn’t care about you or your teammates._

You care, because you’re taking the time to read this article. Help others find the knowledge, room, and permission to care.

Keep an eye on our [public courses](https://www.industriallogic.com/training/public-events/) or enroll in one of our [technical workshops](https://www.industriallogic.com/training/technical/) for help in curing the causes of bad code.

**Related Discussion:**

We had an open discussion through our Industrial Logic TwitterSpace. Here is the recording of that conversation.
