---
url: "https://peterszasz.com/how-to-lead-your-team-when-the-house-is-on-fire/?_bhlid=f9fcc630fe7bbbba4b34644dff9732cf1f401ae0"
captured_at: "2026-09-25T18:46:25+01:00"
title: "How to Lead Your Team when the House Is on Fire"
domain: "peterszasz-com"
---

The tech industry is going through challenging times: from one side, funding dried up [due to the end of the Zero Interest-Rate Period](https://newsletter.pragmaticengineer.com/p/zirp?ref=peterszasz.com); on the other one, [the rapid rise of AI disrupts previously safe domains and business models](https://unchartedterritories.tomaspueyo.com/p/how-ai-disrupts-tech-investing?ref=peterszasz.com). These forces are **pushing companies to "wartime" mode**, a concept I first read about in the works of [David B. Black](https://www.amazon.com/stores/David-B.-Black/author/B001KJ1JI2?ref=peterszasz.com), some of which were published in "[Wartime Software: Building Software when Speed Matters](https://www.goodreads.com/book/show/19497794-wartime-software?ref=peterszasz.com)"; or the [Peacetime CEO / Wartime CEO](https://a16z.com/peacetime-ceo-wartime-ceo?ref=peterszasz.com) article from Ben Horowitz, similarly from more than a decade ago.

These works describe "wartime" as an existential fight for survival that requires a different type of leadership compared to the relative prosperity of "peacetime". Many of the principles outlined by both Horowitz and Black are as relevant as ever for Engineering Managers leading in today's climate. For EMs, wartime means leading low-morale teams through **ambiguity, hard constraints, frequently changing goals, and intense pressure to perform**. It can feel like working in a house on fire. What can an EM do in this situation?

Let's get back to the basics, and look at the role of an Engineering Manager first.

## The three focus areas of an Engineering Manager

1.  Ensuring **delivery** that's aligned with company goals;
2.  Building and sustaining a **high-performing engineering team**;
3.  Supporting the success and **personal growth** of the individuals on the team.

Wartime doesn't change these fundamentals, but it does require some shifts in approach and priorities. Let's go through them by focus areas.

## Focus Area 1: Ensuring Goal-Aligned Delivery

In wartime, you need your team **laser-focused on shipping what matters most, now**. Your organization might not have the luxury of years of runway, and the environment you're operating in is rapidly changing. A few key things to get right:

**Ruthless prioritization is essential.** Narrow the team's attention to the top few goals that are critical for the company's survival and success. Communicate these repeatedly and reinforce them through your own behavior. Be ready to say no and drop anything that doesn't directly contribute. It's hard because you'll also need to say "no" to genuinely valuable, profitable things, projects you were planning to work on, just to be able to deliver the ones that are the most impactful now. Mentally you might find it easier to categorize these projects as "not now".

Next, you need to **empower the team to move fast**. Decentralize decision-making authority as much as possible. Remove barriers in their way, slash approval layers, attack dependencies. "Perfection is the enemy of done" and "Better to ask for forgiveness than permission" are good guidance.

To enable quick decisions, ensure you are frequently and clearly giving high-level context to the team, so they are aligned on company objectives. Set up a clear process for them to rapidly get input on critical choices and transparently communicate the decision to keep everyone aligned. **Bias heavily toward action** - it's better to decide and be wrong sometimes than to paralyze the team with analysis.

**Protect the team's focus time**. The chaos and uncertainties of wartime can be incredibly distracting. Set up processes to shield the team from constant interruptions so they can have deep, creative work sessions. Remove them from low-value meetings and relieve them from monotonous administrative duties. One effective technique is to establish a rotating "firefighter" role to singlehandedly deal with any incoming requests, represent the team in meetings, and handle the necessary amount of bureaucracy, allowing the rest to stay heads-down on the critical priorities.

Another option is to **get in the trenches with your team**. If you're a hands-on manager, wartime is when you can put some effort into technical tasks. Stay closely involved to understand the technical context, and help out where it makes sense. This can mean doing some code reviews, participating in pair programming, handling an incident, and even pushing small commits if that's what's needed. Make sure you're not taking the spotlight from your team members, and know that your impact in management areas can be magnitudes bigger than a small code cleanup.

It's important to note that these wartime actions will probably increase **tech debt** in your code. With the emphasis on velocity over quality, architectural compromises and maintenance shortcuts are often taken. To mitigate this, consider techniques like:

*   Keeping a visible, prioritized backlog of tech debt items to revisit later
*   Allocating a small percentage of each sprint to debt paydown
*   Pairing tech debt work with feature development
*   Conducting regular architecture reviews to spot and address emerging issues
*   Encouraging engineers to flag risky shortcuts during code reviews

You have more chance to succeed if your tech debt strategy is backward-looking, refactoring parts of the code that are causing concrete pain for developers today – as opposed to forward-looking, dreaming up grandiose plans for new frameworks that will be ready for any unknown challenge of the future. (Recognise that these challenges are unknown by definition, so your solution for them will be a hit-and-miss.) The risk of overengineering is real and can cripple developer performance significantly in a wartime era.

## Focus Area 2: Building and Leading the Team

### Retaining

To keep your team engaged and performing at their peak, **don't neglect morale and energy**. Celebrate quick wins, show frequent appreciation, praise the behavior you want to see. Acknowledge that the situation is tough, but project confidence that you'll get through it together.

One major pitfall to avoid is letting an **"us vs. them" mentality** take hold on the team. Naturally, the stress of painful decisions can erode trust in leadership and other departments, but reinforcing a negative mindset will hurt you more than the temporary warm camaraderie you'll enjoy by joining the chorus of cynics.

Don't dismiss or avoid the negative reactions, in fact, you should actively solicit concerns and input rather than waiting for issues to erupt. You cannot choose if people will discuss stressful events, but you can **choose to be a part of these discussions** or not. So never skip your one-on-one meetings, hold ad-hoc Q&As, and maintain these as a safe, open forum for any topics. Share the "why" behind difficult decisions, even if you can't always explain all the details – and acknowledge what you don't know transparently. Assume good intent and extend empathy, even when tension is running high. _(I write more about this and related topics in_ [_How To Represent Decisions You Disagree With_](https://peterszasz.com/how-to-represent-decisions-you-disagree-with/)_.)_

**Focus on the positive aspects of the job that can be taken for granted**, like the opportunity to work on cutting-edge challenges, the company's still existing perks and benefits, the amazing team you have, the chance to work with a modern tech stack, or how your product is helping its users. Showing your team how you appreciate what's still good can help with morale.

At the same time, **accept that you won't be able to retain everyone** through a stressful wartime period. If someone does decide to leave, support their decision and work to make the transition as smooth as possible for them and the remainder of the team.

### Hiring

Yes, there is still hiring in wartime, though more limited than during the growth-heavy periods of peace. If for no other reason, you might need to backfill folks due to the increased attrition. When you receive a new headcount, you need to **prioritize hiring experienced, self-sufficient, autonomous engineers** who can tolerate (even better, strive) in high-stress environments and are experienced enough to contribute immediately. Tighten onboarding to the bare essentials and focus on deploying code fast. You don't have months to train, the company might not exist long enough to get back the investment in juniors if you focus on the long term now.

Fortunately for you, the current job market is full of experienced developers due to mass layoffs. However, expectations are still high (especially around compensation and remote work), and AI companies are paying above market rate to the best talent. These, and the massive work necessary to go through sometimes hundreds of applications make your work harder, so you need to get creative and proactive to attract great candidates. Some ideas:

*   Leverage your network for referrals and backdoor references;
*   Emphasize anything that makes your company unique: its mission, product, tech stack, learning opportunities, compensation policies, hybrid friendliness, etc. Maybe someone out there is looking for the same exact criteria.
*   Partner closely with recruiters or the talent acquisition team to increase the quality of the first-level filtering, and to refine and expedite the hiring process;
*   Move quickly and decisively when you find a strong fit, to minimize the distraction of hiring on you and the team – but due to the current job market you have more luxury now than a few years ago. Consider allowing 2-3 candidates to pass through all rounds, and choose the best fit from them. Still, don't let this grow into indecisiveness, and don't drag the team into a long period of interviewing.

### Performance Management

Wartime pressure can breed **negativity** that you'll need to manage carefully. Understand the context that may be contributing, like uncertainty around job security or maybe some additional personal issues. However, infectious negativity and lack of engagement are performance issues, so handle them accordingly: **give clear feedback on actions and their impact**, separate from any judgment of the individual. Avoid public confrontation, but set firm expectations. Try to redirect negative energy productively by reframing complaints into problems to solve. _(I write more about this topic in_ [_How to Deal with Negative Behavior_](https://peterszasz.com/how-to-deal-with-negative-behaviour/)_.)_

Crucially, **hold everyone to the same standards**, regardless of circumstances. You can't afford to make exceptions for someone just because they have key knowledge or skills you don't want to lose. Consistent accountability is essential for team cohesion and morale – and if you forget this, you might end up with a disengaged, demoralized team, and the underperforming key developer that you wanted to save might already be interviewing anyway.

## Focus Area 3: Supporting Individuals to Succeed

When the house is on fire, it's tempting to put personal development on the back burner _(no pun intended)_. But now is the time when your team members need to feel more than ever that you're still invested in their success, to help them stay engaged and motivated. The trick is to **reframe growth to fit the wartime context**.

Instead of formal skills training or career pathing, focus on maximizing each person's impact by leaning into their strengths. Help them see how this challenging period is **an opportunity to stretch and step up** in ways that will serve them well in the future.

**Call out the valuable, transferrable experience they're gaining** by operating in this high-stakes environment. Emphasize that they're building "career security" - capabilities and experiences that will be valued anywhere - even if short-term "job security" may feel shaky and uncertain.

**Identify on-the-job learning opportunities**, like giving someone the chance to lead an incident response or a high-visibility project. Critical mistakes can still be catastrophic, but because of the fast-changing nature of wartime work, it's easier to process smaller errors with a healthy learning mindset. _(Read more about_ [_Celebrating Failure_](https://peterszasz.com/celebrating-failure/)_.)_

Finally, don't forget to look for **opportunities to display small gestures to show you care** about your team members' personal well-being despite everything that's going on. Make the few team-building occasions count, or simply send a note acknowledging a tough week. A little goes a long way.

## Finally: Take Care of Yourself First

Leading in wartime is incredibly demanding. You won't be able to show up for your team if you're running on empty. Remember to put on your own oxygen mask first, before you try to help others.

*   **Prioritize the basics** of healthy eating, sleeping, and exercising. Treat your body as a machine that needs regular maintenance.
*   **Find peers** within or outside of your organization who get the challenges you're facing, to vent with and get support.
*   **Carve out little breaks of relief**, whether it's a walk, a short meditation, or just a quick game of chess (or backgammon!) in the communal area. A small recharge can help a lot.
*   **Keep a healthy context**: while it might seem overpowering during the day, after all, this is just a job, and you should find other sources of satisfaction in your life besides your work.

## Conclusion

Wartime stretches and strains Engineering Managers especially hard because they receive pressure from above and below. By ruthlessly focusing on well-aligned delivery, building a resilient team, investing in individuals, and maintaining your own health, you can lead your team to not just survive but thrive under pressure. Keep calm, "lean into the suck", and trust that you've got what it takes. Your people count on you.

I write about Engineering Leadership topics similar to this one. [Sign up here to receive my future articles by email.](#/portal/signup)

## _Update_

_Since publishing the above article, I received a bunch of feedback that helped me shape a more nuanced view of the subject. I didn't change the article, but check the_ [_Follow-Up on My Management Under Pressure Article_](https://peterszasz.com/follow-up-on-my-management-under-pressure-article/) _for a few aspects that I missed or clarified._
