---
url: "https://makemeacto.substack.com/p/exploring-the-relationship-between?ref=dailydev"
captured_at: "2026-09-25T17:27:38+01:00"
title: "Exploring the relationship between Tech Lead and Engineering Manager"
domain: "makemeacto-substack-com"
---

[Theory](https://makemeacto.cc/tag/theory/)

A book I recentlu red left me thinking that we could do a better job at helping teams clarifying the relationship between these two roles. Discover my mental model and practical tips.

I've recently (re)read _The Manager's Path_ by Camille Fournier. As I wrote in my notes[1](#footnote-1), this otherwise great book missed a few opportunities to be excellent. One is that, in my opinion, it didn't explore nearly enough the often confusing relationship between a Tech Lead and an Engineering Manager within a team.

In today's article, I want to focus on exploring the blurry boundaries of responsibilities between these two roles.

But before we get into the core topic, let's look at another relationship whose boundaries often cause confusion and see if we can draw some parallels.

## The Relationship between an Engineering Manager and a Product Manager

Lots of (digital) ink has been spent exploring the ideal relationship between an Engineering Manager (EM) and its Product Manager (PM) counterpart. In practice, I have seen many interpretations of splitting work and collaborating between these two peers.

On one end of the spectrum, you have the setup where PMs are very hands-on and are almost entirely in charge of the entire roadmap for the team, while EMs are little more than glorified executors. In such a setup, it's common for the EM to bring up any arbitrage question with the PM, refraining from making any decision that could require changing plans.

I attribute this extreme case to a too-literal interpretation of the PO role from the agile literature. In there, it's often referred to as the person who “owns the team's time,” as such, it's the only one in charge of deciding how to spend it. As the PM is somewhat confusedly considered an evolution of the PO role, it naturally follows that they are responsible for all decisions relating to prioritization.

On the opposite end of the spectrum, you find entirely hands-off PMs. They focus on the strategy, designing experiments, processing data, and leaving it entirely to the EM to break things down into deliverables, prioritize work, and ensure it aligns with the directions set by the PM.

If we keep stretching the Agile analogy, in such a scenario, the EM is de facto the PO for the team, and the PM is the main stakeholder to serve and support.

As is often the case, most teams fall somewhere between these two extremes, where the boundaries between EM and PM are blurred and not wholly clear-cut. I believe that is perfectly fine: the specifics of the relationship will depend on a multitude of factors, including the company culture, team size, and skills and competencies of the two persons covering the roles.

What I found helpful, though, is to always stick to the following mental model:

> PM and EM **share accountability** for the team's outcome
> 
> PM and EM have **clear separate responsibilities** to achieve that.

I find this model powerful and effective for a few reasons:

1.  It clearly distinguishes between Accountability and Responsibility, two concepts that are often confused.
2.  It reminds us that the team's outcomes or impact matters, not its output, for both the EM and the PM role.
3.  It set the foundations for the two roles, agreeing on splitting responsibilities while working in the same direction.

This model is more articulated — and more accurate — than the overly simplistic one that splits the roles between _What to do_ — the PM — and _How to do it_ — the EM.

That's because _what_ and _how_ are not entirely orthogonal when building and shipping software.

I could devote the entire article to exploring this relationship further, but I'll leave that for another time. Please let me know in the comment section if you'd like a more thorough analysis and evaluation of the PM/EM relationship, and I'll gladly work on it.

With this mental model clarified, let's look back at what we came here for: the relationship between the Engineering Manager and the Tech Lead within a team.

## The Relationship between the Engineering Manager and the Tech Lead.

One might be tempted to apply the mental model of “Shared accountability, Split Responsibility” to the EM-TL duo, and some teams do.

There is just a problem with it: it's broken.

I think this approach is broken based on three fundamental premises.

**#1 Reporting lines imply accountability**

In the most common case, and the one we're looking at here, the Tech Lead is part of the team, often a Senior Engineer, and as such, they report to the Engineering Manager who is in charge of the entire team.

There are scenarios where there is no TL in the team, and the role is covered by Staff Engineers operating across multiple teams. Alex Ewerlöf has written an excellent article[2](#footnote-2) covering — among other things — why such an approach in that scenario would not make sense. I am not going to repeat what he's written so well already.

Simply put, EMs should take full accountability for technical decisions within the team, and as we've seen, they share accountability for the team's outcome with their product peer.

**Having a Tech Lead is not a hard requirement.**

Not all teams have Tech Leads. As such, the EM should be able to be in charge of the team's decisions without sharing that responsibility with any other leadership figure. Most teams start off this way, and they only add a Tech Lead later when either the EM workload or the complexity of the scope reaches a point where some extra help becomes highly beneficial.

An engineering manager must be capable of leading the technical direction and agenda of the team when no one is covering the tech lead role.

**These are both technical roles.**

Unlike the relationship between PM and EM, EM and TL are among equals. They both share a very similar set of competencies in the technical field. Even though a Tech Lead does not manage people, a good one will have a broad portfolio of people and leadership skills that allow them to effectively influence and guide the team through difficult decisions or projects.

In many companies, covering the Tech Lead role is considered a requirement for later promotion to Engineering Manager. Given that the skills of an EM and a TL should overlap by 80% or more, there is no natural line for splitting their responsibilities.

Despite these considerations, more often than not, we can observe suboptimal configurations where the relationship between the two roles will be oversimplified down to the following:

*   The Engineering Manager takes care of the team: career development, hiring and firing, staffing different projects, processes, tracking, metrics, etc
*   The Tech Lead is in charge of making technical decisions.

In such a scenario, the Tech Lead often assumes the traits of the “more equal among peers” to other engineers in the team. At the same time, the Engineering Manager becomes little more than a glorified team secretary. The Tech Lead will often cause frustration and resentment with their peers; the Engineering Manager will progressively lose relevance and career capital, which they'll usually only realize the next time they interview for a role.

Why do many teams follow this path if this approach is so detrimental in the long run? In my opinion, it has to do with two main factors at play:

1.  **Convenience**: this model is very convenient and easy to reason about. Roles are clear, fewer discussions are required, fewer open conflicts, and more opportunities to say “not my role.”
2.  **Efficiency**: Assigning specific responsibilities to a single person is a great driver for efficiency. The person in charge can make decisions quickly, fewer meetings are required, and seeking consensus is considered an accessory waste of time.

While optimizing for convenience tends to be driven by the individual's need to preserve energy and avoid headaches, the push toward efficiency often emanates from organizational guidelines. Too frequently, companies are eager to sacrifice effectiveness on the altar of efficiency, especially when the side effects materialize on relatively long time horizons.

## Aiming for a more effective setup

My current thinking is that a more appropriate mental model for the EM/TL relationship is almost the exact inverse of the one that rules the relationship between an Engineering Manager and a Product Manager.

> **Accountability is not shared**: the Engineering Manager is solely accountable for the team's technical direction and decisions
> 
> Engineering Manager and Tech Lead **share the responsibility** to take the right technical decisions

![](https://storage.ghost.io/c/d3/84/d3840377-8f34-47dc-83e5-6425ca34f9cb/content/images/2026/06/e10b182f-f015-490d-8a0a-a888588dedae_2422x1898.png)

Wait, what do you mean by saying that they share the responsibility?

The simplest way to put it is to **consider the Tech Lead an extension of the Engineering Manager's bandwidth rather than as a profile that has complementary skills and responsibilities**.

As such, the responsibilities that the Engineering Manager will share — or delegate — with the Tech Lead will vary depending on the team context: its composition, challenges, priorities, gaps, etc.

In turn, the Tech Lead will **extend the capacity of the Engineering Manager** by taking on some of the following duties:

*   **Propose improvements in the technical platform.** Collect data and feedback from the engineers in the team. Formulate a proposal for overcoming current challenges, covering different scenarios, their relative strengths, and the proposed solution. The engineering manager will be consulted throughout the process; they will challenge the TL's proposal where they see fit and ultimately decide whether to ratify it and proceed.
*   **Lead the delivery of a specific project.** The EM might decide to free up some of their capacity by delegating the tasks of planning, executing, and reporting on a particular project, allowing them to focus on a smaller scope. In this scenario, EM and TL break down the scope into more manageable parts and split the duty of driving the execution of each sub-part. The TL and EM will constantly consult with each other to overcome specific issues, and the ultimate decision maker will still be the EM when consensus is not reached.
*   **Operate as the primary technical interface on a project involving multiple teams.** The EM can ask the Tech Lead to become their team's primary point of contact in a project requiring coordination across various teams. The EM will be exempted from attending certain meetings but not all of them. They'll have regular syncs with the TL to ensure they're on top of what is going on, weigh in their views on how to approach specific problems and support the TL by influencing the general direction where needed.

These are just a few examples that cover the most common cases.

They all have in common that they don't identify the responsibility of a Tech Lead in absolute terms, attributing them full decision powers on a team's dimension (Technology, Processes, Staffing, etc).

Instead, they'll often assume responsibilities transversally on a slice of the team's scope while consulting and aligning with the EM on the general direction to follow, tradeoffs, and prioritization.

Though less efficient on the surface — as it requires more coordination and discussions between the two figures — I consider this approach more effective as it substitutes the efficiency goal with achieving more effective results, including the following:

*   The EM will remain the figure who owns the technical agenda for the team, something they'll need to be able to keep doing in the future, be it in different companies or as a consequence of a promotion.
*   The Tech Lead will be exposed to a broader set of skills beyond the purely technical ones, something required for them to access the next level successfully: becoming an EM themselves or staying on the IC track and being promoted to a Staff Engineer role.
*   The Engineering Manager will be able to make better prioritization decisions with their product peer as they can consider technical nuances and constraints.
*   By formalizing proposals to be approved by the EM, the Tech Lead — and, therefore, by extension, the whole team — will drive much better technical decisions. They will be more thoroughly thought through and cover aspects such as implementation or opportunity costs that are often ignored.
*   Last but not least, less disruption will be caused to the team if the Tech Lead or the Engineering Manager were to leave it, as the other figure will be able to stretch themselves and fill the gap. Bandwidth will be reduced, but the ability to cover all the aspects of a team performing effectively should be preserved.

Considering the broad definition of _technical_, the Tech Lead role will still have a technical focus. Not one limited to code and architecture but one that encompasses tradeoffs, communication, prioritization, and processes.

That is also true for the Engineering Manager, who needs to be both a robust technology leader and a great people leader.

I am convinced that a lot of the disfunctional relationship between Tech Leads and Engineering Managers is a consequence of overindexing the differences between the two roles rather than their similarities.

I'm curious to hear about other views, as this is one of those topics with as many opinions as individuals, and I'm always trying to come up with a more nuanced perspective.

## If you found this valuable

If you found this valuable, here are other ways I can help you and your company:

1.  Follow me on [LinkedIn](https://www.linkedin.com/in/piffio/?ref=makemeacto.cc) for regular posts on tech leadership throughout the week.
2.  [Contact me](https://sergiovisinoni.com/services-for-businesses/?ref=makemeacto.cc) if you're interested in a Fractional CTO, Technical Advisor, or Board Member for your company.
3.  [Work with me 1:1](https://sergiovisinoni.com/services-for-individuals/?ref=makemeacto.cc) as your mentor and coach. I love working with driven and competent people in their specific situations and providing personalized guidance, insights, perspectives, and support.
4.  Promote your product or brand to 1,200+ tech leaders from 80+ countries. Just reply to this email to get a conversation started.

* * *

1.  Here you can find the article with my full review: [↩](#footnote-anchor-1 "Jump back to footnote 1 in the text.")
    
    [
    
    📚 Books I read in July & August 2024
    
    Last month, I was traveling around Europe with the family, so I skipped July's edition of the books I read. I combine July and August books in a single post in today's issue.
    
    ![](https://storage.ghost.io/c/d3/84/d3840377-8f34-47dc-83e5-6425ca34f9cb/content/images/2026/06/35aaf2d1-461d-4765-a380-bd6b2daf4c23_800x800-110.png)Sudo Make Me a CTOSergio Visinoni
    
    ![](https://storage.ghost.io/c/d3/84/d3840377-8f34-47dc-83e5-6425ca34f9cb/content/images/2026/06/84367877-ca35-4522-8a45-32b2e9bf2ab1_1449x2048-jpeg-2.jpg)
    
    ](https://makemeacto.substack.com/p/books-i-read-in-july-and-august-2024)
    
2.  See Alex's Article here [↩](#footnote-anchor-2 "Jump back to footnote 2 in the text.")
    
    [
    
    When Staff Engineer is an anti-pattern
    
    Years ago, I & Gabbon were interviewing a candidate for an EM (engineering management) position. By that point I had carried out dozens of technical leadership interviews for Staff Engineer and EM positions but this one was noteworthy. It felt like we took a guy off the streets!
    
    ![](https://storage.ghost.io/c/d3/84/d3840377-8f34-47dc-83e5-6425ca34f9cb/content/images/2026/06/8c58cb07-9341-402b-bcdb-9fa767c2cdac_500x500.png)Alex Ewerlöf Notes
    
    
    
    ](https://blog.alexewerlof.com/p/when-staff-engineer-is-an-anti-pattern?ref=makemeacto.cc)
