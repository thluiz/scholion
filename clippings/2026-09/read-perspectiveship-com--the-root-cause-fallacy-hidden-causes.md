---
url: "https://read.perspectiveship.com/p/the-root-cause-fallacy?ref=dailydev"
captured_at: "2026-09-25T20:31:55+01:00"
title: "The Root Cause Fallacy: Hidden Causes"
domain: "read-perspectiveship-com"
---

The system crashed at 3 AM. I ran Five Whys to find the root cause: it’s the database that ran out of memory. But that’s not a full story:

The database ran out of memory  
**AND** monitoring failed to alert developers  
**AND** the scaling policy didn’t work  
**AND** the culprit query wasn’t optimised.

Many contributing causes led to failure.

The complexity of the situation needs good answers, not just simple ones.

Too much simplification is like saying: water causes drowning or gravity causes planes to crash. It’s somewhat true, but useless.

Two weeks ago, I published the article: [Solve The Right Problem](https://read.perspectiveship.com/p/solve-the-right-problem), presenting the Five Whys method, where by asking five “why?” we can get to the root cause. The article got great comments on Reddit, [but one was perspective-shifting](https://www.reddit.com/r/programming/comments/1of9qf4/comment/nlauoyn/): Root cause is a fallacy. I’d presented Five Whys as a path to “the” root cause, but a complex failure rarely has just one cause. This is Part 2:

[

![](https://substackcdn.com/image/fetch/$s_!TW-V!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5bb09721-934d-4262-83f9-dd0d336e0b2d_2048x2048.png)

](https://substackcdn.com/image/fetch/$s_!TW-V!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5bb09721-934d-4262-83f9-dd0d336e0b2d_2048x2048.png)

_Why doesn’t it work? Why is the server down?_

The word “why” demands one answer, one reason, one thing to fix.

Simple explanations feel smart, elegant and right! But complex systems rarely fail for a single reason.

Brains are wired to look for causation, sometimes also where there is none [(correlation vs causation](https://read.perspectiveship.com/p/correlation-vs-causation)).

In “Solve the Right Problem”, I’ve pointed out, when describing Five Whys:

> The main critique of this method focuses on depth, as for most of cases, just five iterations might not be enough. (...) The closer to the real issue we get, the better, as it allows us to find better solutions.

When running Five Whys, each “why?” has a single answer. Choosing just one option when many factors contribute is satisfying our brain’s need for simplicity, but it’s not helping us get to the truth.

[Try inversion](https://read.perspectiveship.com/p/inversion), by defining the problem in reverse:

_Why is our product successful?  
Why is our application working without problems?_

There is no simple root cause of success. There are many contributing factors: luck, hard work, attention to detail, and a deep understanding of clients’ needs. It’s similar to failures: many things led to the undesired state.

_How did each cause contribute?_

3 AM database crash example breakdown:

*   Database ran out of memory → **high** (breaking point)
    
*   Missing monitoring → **medium** (would have caught it early)
    
*   Broken scaling policy → **high** (could have prevented overflow)
    
*   Suboptimal query → **medium** (accelerated memory consumption)
    

Running out of memory directly crashed the database, but other aspects shouldn’t be overlooked.

Five whys method can still help us uncover these root causes, but it’s worth looking at how each cause contributed to the failure. It’s a good starting point to think of improvements.

Next time you try to find “the root cause”. Pause and reflect on what combination of factors caused it, and don’t settle on just one. Rate their contribution, then fix based on impact.

**Trees have many roots, as with success and failure. So look for multiple root causes.**

Thanks for reading!  
— Michał

[Share](https://read.perspectiveship.com/p/the-root-cause-fallacy?utm_source=substack&utm_medium=email&utm_content=share&action=share)

[Share Perspectiveship](https://read.perspectiveship.com/?utm_source=substack&utm_medium=email&utm_content=share&action=share)

[

![Solve The Right Problem](https://substackcdn.com/image/fetch/$s_!ja5H!,w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F021a1c2a-2b25-4e06-80ad-e00e554b3f0b_2048x2048.png)

](https://read.perspectiveship.com/p/solve-the-right-problem)

[

![Correlation Does Not Imply Causation](https://substackcdn.com/image/fetch/$s_!1P90!,w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F169146a2-6e0b-417e-8474-be9262c5f9b4_2048x2048.png)

](https://read.perspectiveship.com/p/correlation-vs-causation)

Great articles which I’ve read recently:

*   [Give your engineers a kingdom](https://newsletter.manager.dev/p/give-your-engineers-a-kingdom?r=2c2vs2) by [Anton Zaides](https://open.substack.com/users/121956618-anton-zaides?utm_source=mentions)
    
*   [The uncomfortable truth about job security in tech](https://posts.managementdeltas.com/p/the-uncomfortable-truth-about-job?r=2c2vs2) by [Gilad Naor](https://open.substack.com/users/15576627-gilad-naor?utm_source=mentions)
    
*   [6 Leadership Tactics That Feel Like Cheating (But Work Like Magic)](https://www.thegoodboss.com/p/6-leadership-tactics-that-feel-like?r=2c2vs2) by [Gaurav Jain](https://open.substack.com/users/196112436-gaurav-jain?utm_source=mentions)
    

[LinkedI](https://www.linkedin.com/comm/mynetwork/discovery-see-all?usecase=PEOPLE_FOLLOWS&followMember=poczwardowski)n | [Substack DM](https://substack.com/@poczwardowski) | [Mentoring](https://adplist.org/mentors/micha-poczwardowski) | [X](https://x.com/m_poczwardowski) | [Bsky](https://bsky.app/profile/poczwardowski.bsky.social)
