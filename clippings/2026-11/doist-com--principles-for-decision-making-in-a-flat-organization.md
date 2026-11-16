---
url: "https://doist.com/blog/decision-making-flat-organization"
captured_at: "2026-11-16T02:25:11+00:00"
title: "Principles for decision-making in a flat organization"
domain: "doist-com"
---

This article started out as an internal Twist thread around how our team could learn to ask and give feedback more mindfully. It explores how we can balance making decisions quickly while maintaining our openness to feedback to ensure our decisions are good ones.

At Doist, we believe that open and sincere communication improves our decision-making process. That’s why we’ve built a culture that encourages feedback at all levels of decision-making: from purely technical solutions to team and product management.

We built our team communication app, [Twist](https://twist.com/?utm_source=doist_blog&utm_medium=referral&utm_campaign=decisionmaking_flat_organizations), around public threads to make that level of transparency and engagement possible for both ourselves and other remote workplaces.

Initially, we thought that the more input you get, the better your decisions will be. (This idea aligns quite naturally with the engineering ethos that more data means better decisions).

However, as our team has grown, we’ve learned that too much of a good thing is not a good thing. I once witnessed one of our designers ask the team for feedback on a draft of the Twist logo. All of a sudden everybody turned into font and logo experts (I was guilty as well) and overwhelmed him with feedback.

> Initially, we thought that the more input you get, the better your decisions will be.

As the leader of Doist’s back-end team, I saw this kind of feedback overload as a big challenge to our team’s ability to operate efficiently. There were too many inputs. And more and more time was spent responding to feedback rather than executing on decisions. That’s when I came across a document detailing the principles of “rough consensus”.

![A comic showing a person writing some notes on a seamingly endless sheet of paper that unrolls behind them. Other people try to keep up with the notes but seem puzzled and some are outright overwhelmed. The person writing the notes seems oblivious and satisfied while announcing “Just adding my two cents here…”.](https://storage.ghost.io/c/3d/0b/3d0b3605-e62c-48fe-982e-7efe1e14e187/content/images/2022/06/-COMIC-_principles-of-decision-making-1.jpg)

Artwork by [Anaïs Pirlot-Mares](https://www.instagram.com/maresisanais/?ref=async.twist.com)

## Rough consensus

The [Internet Engineering Task Force](https://www.ietf.org/about/?ref=async.twist.com) (IETF) is a membership-based organization of designers, operators, vendors, and researchers that develop the standards that have shaped the internet into the tool we use today. Their main decision-making principle was coined by Dave Clark in 1992:

> We reject: kings, presidents, and voting.

> We believe in: rough consensus and running code.

I’ve always been curious about what “rough consensus” means. How do you actually know when you reach one?

> How does a group of people make the best decision without “kings” in situations where there’s no obvious right answer?

As it turns out, there is a document that explains in detail the process and the ideology behind the IETF’s approach to decision-making called “[RFC 7282. On Consensus and Humming in the IETF](https://tools.ietf.org/html/rfc7282?ref=async.twist.com).” It provides very practical guidelines on how to advance technical discussions to converge around a solution without unnecessary delay. This document can be helpful to all of us, especially product leadership and squad leaders.

IETF faces the same challenges all technology teams do as they shape the product and specify the behavior of its components. As the document puts it:

> “Engineering always involves a set of tradeoffs. It is almost certain that any time engineering choices need to be made, there will be options that appeal to some people, but are not appealing to some others.”

The question becomes: how does a group of people make the best decision without “kings” in situations where there’s no obvious right answer? A shared understanding around how decisions are made is necessary.

## Voting by humming

In IETF, they sometimes hum instead of raising their hands when they need to vote. The idea is to make voting more anonymous and also fight the temptation to make decisions based solely on the number of votes. As emphasized in the document, humming gives the person deciding the opportunity to “take the temperature of the room”. It’s just one tool they use to move the discussion forward, rather than end it.

While this approach can’t be replicated exactly on a remote team for obvious reasons, it does illustrate some of the main principles behind rough consensus and what distinguishes it from top-down decision-making on the one hand and majority-rule decision-making on the other.

## “Not the best choice” versus "fundamental flaws" feedback

Rough consensus relies on the distinction between two types of objections:

1.  “Not the best choice” feedback: “I don’t believe Solution A is the best choice, because XYZ. I believe Solution B would be better, but I accept that Solution A can work too.”
2.  Fundamental flaws: “I believe Solution A is unacceptable because XYZ.”

Rough consensus isn’t majority rule. It’s okay to go ahead with a solution that may not look like the best choice for everyone or even the majority. “Not the best choice” means that you believe there is a better way to solve the problem, but you accept that this one will work too. That type of feedback should be welcomed, but it shouldn’t be allowed to slow down a decision.

> Once everyone can live with a given solution, you’ve reached rough consensus, even if there are outstanding objections.

On the other hand, it’s crucial to address and discuss all fundamental flaws before the discussion is done. Fundamental flaws are critical issues that should disqualify a proposed solution. It’s hard to define what qualifies as a fundamental flaw, but a few starting points are:

*   It will substantially increase the technical debt.
*   It doesn’t scale well (unless the specific circumstance does not require scalability).
*   It requires too much work to implement, and it doesn’t justify the value which the solution adds.

This list is not complete, and other teams will of course define a fundamental flaw differently. For example, based on our values of respecting users’ time, attention, and intentions, the product design team may consider any solution that unnecessarily distracts the user to be fundamentally flawed. Based on our company’s priority to remain an independent and sustainable company, the marketing team may consider any solution that costs more than the revenue it will bring in to be fundamentally flawed.

It is important for an organization to have a shared understanding of what “fundamentally flawed” means going into a discussion of proposed solutions, even if the definition evolves over time.

## The art of asking for input

How do you ensure that fundamental flaws are fully addressed while neither stifling nor getting slowed down by non-critical feedback? Here’s how the IETF recommends moving toward rough consensus when a discussion has stalled:

> A chair who asks, “Is everyone OK with choice A?” is going to get objections. But a chair who asks, “Can anyone not live with choice A?” is more likely to only hear from folks who think that choice A is impossible to engineer given some constraints. The objector might convince the rest of the group that the objections are valid and the working group might choose a different path.

As you can see, an objector can’t simply say “I don’t like solution A” or even object by providing an alternative that they believe is better — they have to first prove why solution A has fundamental flaws.

Once everyone can live with a given solution, you’ve reached rough consensus, even if there are outstanding objections.

## On compromises

A substantial part of the IETF document is dedicated to the question of compromises, distinguishing between two types:

> Unfortunately, the word “compromise” gets used in two different ways \[…\] Engineering always involves balancing tradeoffs \[…\]: We might have to compromise processor speed for lower power consumption, or compromise throughput for congestion resistance. Those sorts of compromises are among engineering choices, and they are expected and essential. \[…\].

> However, there is another sense of “compromise” that involves compromising between people, not engineering principles. For example, a minority of a group might object to a particular proposal, and even after discussion still think the proposal is deeply problematic, but decide that they don’t have the energy to argue against it and say, “Forget it, do what you want”. That surely can be called a compromise \[…\] but really all that they’ve done is capitulated. That’s not coming to consensus; there still exists an outstanding unaddressed objection.

> Again, if the objection is only that the choice is not ideal but is otherwise acceptable, such a compromise is fine. But conceding when there is a real outstanding technical objection is not coming to consensus.

Sometimes there’s a temptation to jump into a Twist thread and add a quick “two cents” to an ongoing discussion. Chances are, those two cents will be either truisms that probably aren’t worth sharing in the first place or opinions which require further explanation to fully justify.

> If it’s not worth spending the time to over-communicate your point, the feedback is probably not worth slowing down the discussion for.

In the latter case, the decision-maker will likely either ignore your feedback since they don’t fully understand it or have to follow up with you to get to the root of your objections. Do what you can to provide them with the information they need to evaluate your argument up front. If you believe your feedback to be critical, say so and spend the extra time explaining and defending your position from the start.

This is especially important in the context of remote, [async-first](https://async.twist.com/asynchronous-communication/) teams. Here we lack the luxury of quick back-and-forth communications to clarify the point, and a person’s "two cents" can seriously slow down the decision-making process.

If it’s not worth spending the time to over-communicate your point, the feedback is probably not worth slowing down the discussion for.

## Doesn’t rough consensus contradict the "hell yeah" approach we preach?

The rough consensus approach contrasts with the “if it’s not a ‘hell yeah’, it’s a no” criterium we’ve adopted for hiring (i.e., reject a candidate unless everyone is in enthusiastic agreement). However, I believe a lower decision-making standard is acceptable, and even necessary, for most of the technical and product-related challenges we face.

We may use the “hell yeah” principle for hiring and some other decisions, but we use the quick iteration principle when we ship things. We don’t aim for perfection the first time — we build fast, we ship, we learn, we iterate, and we ship again. Step by step, we get to where we want to be. If we applied a standard of perfection and complete consensus to the things we shipped, we’d quickly become sluggish.

> We risk more when we delay decisions in an attempt to reach total consensus.

Thanks to our “hell yeah” approach to hiring, we can trust the competence and diligence of the person making the decision. Yes, with rough consensus we risk not making the best choice, but if the decider believes it’s the best solution, we can trust it to be adequate.

Even if it turns out to not be the best decision, in the end, the increased speed at which we’re able to operate will, on average, compensate for the setbacks. We risk more when we delay decisions in an attempt to reach total consensus.

Rough consensus doesn’t mean that we don’t aim for perfection in the actual implementation of the solution. When implementing, we should always aim for technical excellence. Commitment to the implementation is often what makes a solution the right one. (This is similar to Amazon’s “disagree and commitment” philosophy.)

The IETF case is a good example of how organizations with different structures and cultures solve the universal problem of decision-making.

I’m not proposing we apply rough consensus to all of our decisions. We are not the IETF — our goals and structure are quite different. However, I believe there are valuable lessons we can draw from their experience.

> If there is a good enough solution X, don’t ask people what they think about it. Instead, ask everyone if they can live with it and if not, why.

We aim to maintain a relatively flat, transparent, and inclusive organization. As a result, consensus-based decision-making comes more naturally to us than top-down decision-making. How do we harness the benefits of collective input while making decisions quickly?

Rough consensus is a good standard for ensuring that minor remarks or non-critical issues don’t impede our performance, and it’s an effective tool in our belt as more and more voices are added to the team.

Here are some concrete takeaways we can all apply for more efficient and effective decision-making:

**If you’re the one raising objections to a solution:**

*   Before you object, weigh whether or not your objection reveals a serious issue. It’s okay to make a remark like “I believe there is a better decision and it’s this, but I’m also okay with the current choice.” It’s also okay to suggest improvements to the idea (or the implementation, if you’re discussing a pull request for example) without vetoing the current choice. Make clear what type of objection you’re raising.
*   If you believe the choice has a blocking flaw, try to make your feedback as clear as possible so that the decision-maker can address it properly.
*   If you believe the choice has a blocking flaw, try to find enough time and energy to convince opponents. When you differentiate between non-critical feedback and a fundamental flaw and prioritize the latter, you’re able to conserve the time and mental energy for the most important discussions.

**If you’re the one deciding:**

*   Be vigilant and make sure the discussion doesn’t stall on non-critical, “not the best solution” feedback.
*   If there is a discussion which cannot converge, ask participants to clarify if objections to a proposal address fundamental flaws or remarks which should be taken in consideration.
*   If there is a good enough solution X, don’t ask people what they think about it. Instead, ask everyone if they can live with it and if not, why.
*   Don’t feel like you have to default to majority rule.

## Consensus is the path, not the destination

A final quote from the IETF document:

> We don’t try to reach consensus in the IETF as an end in itself. We use consensus-building as a tool to get to the best technical (and sometimes procedural) outcome when we make decisions.

At Doist we strive to create a culture where everyone’s feedback is heard. We believe we’re a stronger company for it. But as we’ve learned, this requires effort and self-awareness from all parties to the discussion. We’re not there yet, but the principles of rough consensus can be useful in balancing feedback and efficiency in all of our decision-making.

* * *

**What’s Twist?** Twist is an async messaging app for teams burned out by real-time chat, meetings, and email.

You don’t need to use Twist to get a ton of value out of this newsletter and community. But if the topics we talk about resonate with you, there’s a good chance the app will too. [See what makes Twist different →](http://twist.com/?ref=async.twist.com)

🌎 Built asynchronously by the fully remote team at [Doist](https://doist.com/?ref=async.twist.com)
