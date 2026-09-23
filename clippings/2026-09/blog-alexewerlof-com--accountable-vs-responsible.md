---
url: "https://blog.alexewerlof.com/p/accountable-vs-responsible"
captured_at: "2026-09-23T18:26:10+01:00"
title: "Accountable vs Responsible - Alex Ewerlöf Notes"
domain: "blog.alexewerlof.com"
---
Discover more from Alex Ewerlöf Notes
Technical Leadership, Reliability Engineering, Growth
Over 19,000 subscribers
Subscribe
By subscribing, you agree Substack's Terms of Use, and acknowledge its Information Collection Notice and Privacy Policy.
Already have an account? Sign in
TECHNICAL LEADERSHIP
Accountable vs Responsible
When to separate accountability from responsibility and why it usually doesn't matter?
ALEX EWERLÖF
NOV 29, 2024
14
2
Share

English isn't my native tongue. I didn't know the difference between these accountability and responsibility until my ownership trio was pretty popular. TLDR; here's the summary:

You cannot be responsible for something you don't control. You need the mandate.

You cannot use that mandate effectively over something you don't understand. You need knowledge.

You gain knowledge only if you are fully responsible for the consequences of your mandate.

Anything else, is a broken ownership.

6 Archetypes of Broken Ownership
ALEX EWERLÖF
·
AUGUST 1, 2023
Read full story

Then I got this question from multiple readers:

What about accountability?

To me responsibility and accountability were synonyms until I did the research.

There is a nuanced but profound difference between the two.

The difference isn't too important in the context of the ownership trio, but it is important implications in:

Roles Definitions: e.g., what is an Engineering Manager or Staff Engineer accountable for?

Legal Consequences: e.g., when a company goes bankrupt who is ultimately accountable?

Army and military: e.g., if the commander's mistakes perishes soldiers' lives, who is accountable?

🤖🚫 Note: No AI was used to generate this content (except one image from another article). This essay is only intended for human consumption and is NOT allowed to be used for machine training including but not limited to LLMs.

Subscribe
Dictionary

Cambridge English Dictionary:

Responsible: to have control and authority over something or someone and the duty of taking care of it, him, or her.

Accountable: Someone who is accountable is completely responsible for what they do and must be able to give a satisfactory reason for it

There's a bit of recursion there and the meaning isn't that distinguishable. 😄

Side note: the two words enjoyed different popularity through modern history:

The usage trend of two words over time. Source: Oxford dictionary entries for Responsible and Accountable
RACI

Responsibility assignment matrix (RAM) describes 4 roles:

Responsible: those who do the actual work to complete the task

Accountable: signs off the work that the responsible provides and can only be 1 person. Accountable is also responsible but in practice that doesn't mean the same level of engagement.

Consulted: Those whose opinions are sought, typically subject-matter experts (2-way communication)

Informed: Those who are kept in the loop on progress (1-way communication)

Putting it all together you get this picture:

Army

Lieutenant Colonel Joe Doty (US Army) and Captain Chuck Doty (US Navy) put it like this:

Accountability means consequences, both positive (awards, promotions, superb ratings, etc.) and negative (letters of reprimand, Article 15s, relief for cause, poor ratings, etc.). For example, the Army's officer evaluation reporting system holds commanders accountable for what happens in their units. —Command Responsibility and Accountability, Doty & Doty

I can't claim I'm smarter after reading that essay. The "positive consequences" reminds me of idea theft or credit theft:

Legal

Now we're getting somewhere:

Responsibility has a factual cause/effect aspect. For example, a storm can be responsible for causing damage to a home.

Legal responsibility (AKA liability) has a punishment and penalty aspect attached to it. For example if a child steals something, the parents are liable to pay the damage.

In other domains

In ethics and governance, accountability is answerability, blameworthiness, liability, and the expectation of account-giving. If you are accountable for something, you are in a position that requires you to report to or answer to someone for your actions and decisions.

Accountable gives an account, reason or explanation for the action. For example, a healthcare professional is obliged to offer a rationale for their decisions during the course of treatment (ref).

In corporate world, that is reporting lines!

Why we should not separate Responsibility from Accountability?

The primary reason is culture: a command and control structure may work for the army or when there are legal consequences (jail or punishment) but is that really the kind of team environment we need in our companies?

Most organizations don't need to separate accountability from responsibility. If they do need the separation, most probably there are larger cultural problems to solve than which word to use!

Formally, there's only 1 accountable party (usually the Engineering Manager or any variation of it: Director, VP, etc.). But does this mean individuals aren't supposed to give an account or explanation for their actions?

More often than not, the separation is pushed by:

Managers who want to call all the shots (monkey with a gun archetype of broken ownership)

Upper management who are desperate to find a neck to choke without bothering to understand the details (babysitter archetype of broken ownership)

Dodgy team members who don't want to accept the consequences of their actions (teenager archetype of broken ownership)

If there's a need for a single neck to choke when things go wrong (or hang the medallion when things work out), we're fundamentally building the wrong organizational dynamics.

Great leadership is a network, not a hierarchy, Gitte Fredriksen (12 min)

I really enjoyed this TED talk by Gitte Frederiksen who leads Boston Consulting Group's work in over 15 countries, with an emphasis on the US, the Middle East, and Sweden:

What if leadership could be for the many? That's scary. And for all you leaders out there thinking it won't work, maybe in some cases it won't. But when it does, we have better outcomes and happier people, with everyone leaning in, even if just a bit more.

A typical view of leadership is a hierarchical organization chart. Either you're a leader or you're not. Most people are being led, not taking lead. Communication often flows from top to bottom along just one line, which means it doesn't match the complexity of problems which move in several directions at once. Decisions are left to one person, the leader, who, being only human, can become a bottleneck of speed and scale. They can miss new ideas, diverse capabilities and potential that exist all over the chart.

So in a network instead, everyone's in charge and we replace power of the few with influence of the many. Sure it looks more messy, but I'd argue more beautiful, more multi-dimensional, more dynamic, more like nature. I believe this model can help us do more and be less dependent on each individual. Which means it's resilient, and progress is sustainable.

Subscribe
When should Accountability and Responsibility be separated?

I reached out to one of the hard core proponents of this separation. The main question is: "where does the buck stop?"

"The buck stops here" is a phrase that was popularized by U.S. President Harry S. Truman, who kept a sign with that phrase on his desk in the Oval Office.

Image source: Wikipedia

"Buck passing" is said to have originated from poker but it evolved to have a nasty meaning in politics (and by extension corporate politics):

Buck passing, or sometimes (playing) the blame game, is the act of attributing to another person or group one's own responsibility. It is often used to refer to a strategy in power politics whereby a state tries to get another state to deter or fight an aggressor state while it remains on the sidelines —John, Mearsheimer (2001). The Tragedy of Great Power Politics

Basically the army version that we discussed above. Any of the following scenarios can benefit from separating accountable and responsible:

A finger pointing culture in need of finding someone to blame when things go wrong

A culture of heroism where a single person takes the credit for the team doing the actual work (credit theft)

Non-technical leadership who needs to rely on technical translators to make sense of things. We've talked about why it's an anti-pattern for Staff Engineers but Engineering managers aren't immune to this either:

A hierarchical culture where the information is trapped behind closed doors and the responsible parties aren't deemed worthy of knowing WHY they are doing WHAT they are doing (information asymmetry).

A parent/child situation where the child is not legally accountable or deemed mentally mature to be in charge of their actions.

A product where quality of execution does not matter and the responsible party is not obliged to do their best because they are not ultimately held accountable

A group of monkeys led by an astronaut! 🐒🐒🐒🐒🐒👨‍🚀

Organization where there's a "head" role. This title signals that the rest of the org is merely the execution "body". The head is accountable for all the thinking while the body is responsible for executing orders (a mini-dictatorship). The trick is to actually hold the head accountable when things don't work out! In my experience that's when the "head" blames the "body" for poor execution.

Jokes aside, the only valid scenario is when there are legal consequences for the wrong actions.

In tall organization trees where the distance between tech and leadership is too large, accountability can be implemented as answerability: someone to ask questions about how things work. In that context, the team should ideally know the answers but the EM should definitely know.

Most tasks and decisions aren't of that nature, even if the "head" thinks otherwise! We're all in this together.

What about ownership trio?

Back to where we started: where's the accountability in the full ownership?

Accountability is embedded in responsibility and mandate:

The team has the mandate to make decisions to improve their service

The team is also responsible to measure the service level from the consumer's perspective and if their commitment is under threat, the team is collectively responsible to prevent or mitigate that. Alerting is the absolute minimum mechanism to do that.

The reason I didn't separate accountability from responsibility is because in a healthy culture, most teams don't face legal consequences. Instead their on-call hurts. In my experience, incidents are enough motivation to nudge the team to up their knowledge and use their mandate effectively.

The knowledge growth element is important, because without that, you'll end up with the gambler archetype of broken ownership.

Image from the 6 archetypes of broken ownership

My monetization strategy is to give away most content for free. However, these posts take anywhere from a few hours to a few days to draft, edit, research, illustrate, and publish. I pull these hours from my private time, vacation days and weekends.

You can support this free content by sparing a few bucks on a paid subscription. As a token of appreciation, you get access to the Pro-Tips sections as well as my online book Reliability Engineering Mindset. Right now, you can get 20% off via this link. You can also invite your friends to gain free access.

If you find this post insightful, please share it in your circles to inspire others. 🙌

Share

14 Likes
∙
2 Restacks
14
2
Share
