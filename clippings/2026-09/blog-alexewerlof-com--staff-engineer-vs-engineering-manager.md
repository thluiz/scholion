---
url: "https://blog.alexewerlof.com/p/staff-engineer-vs-engineering-manager?utm_source=leadershipintech&utm_medium=newsletter&utm_campaign=hey-wait-is-employee-performance-really-gaussian-distributed&_bhlid=c103c83a930b356b8c37a32c718eff788824a66b"
captured_at: "2026-09-23T18:33:31+01:00"
title: "Staff Engineer vs Engineering Manager - Alex Ewerlöf Notes"
domain: "blog.alexewerlof.com"
---

Discover more from Alex Ewerlöf Notes
Technical Leadership, Reliability Engineering, Growth
Over 19,000 subscribers
Subscribe
By subscribing, you agree Substack's Terms of Use, and acknowledge its Information Collection Notice and Privacy Policy.
Already have an account? Sign in
TECHNICAL LEADERSHIP
Staff Engineer vs Engineering Manager
When do you need a Staff Engineers? What's the accountability model with or without?
ALEX EWERLÖF
NOV 24, 2024
276
10
15
Share

These are actual questions I've got in the past few years:

An EM: I don't want to deal with people anymore. I want to focus on the tech. Is Staff Engineering for me?

A Senior EM responsible for multiple teams: I have too much admin work. Should I hire a Staff Engineer to take over the technical part of my job?

A Staff Engineer at a team without an EM: I'm practically acting as the team manager and like it. Should I just switch lanes to become an EM?

A Senior Engineer frustrated with Ivory Tower Staff Engineers: what is the accountability of the Staff Engineers? They act like retired devs.

A new Staff Engineer: What are dotted reporting lines? I have my line manager, why should I care about other managers?

So I thought it's time to settle all these questions once and for all.

🤖🚫 Note: No AI is used to generate this content. This essay is only intended for human consumption and is NOT allowed to be used for machine training including but not limited to LLMs.

Introduction to the role of Staff Engineer
ALEX EWERLÖF
·
FEBRUARY 26, 2024
Read full story
When do you need a Staff Engineer?

Staff an EM have some similarities:

Let's step back and build a model.

Engineers create and maintain the tech. But the tech doesn't exist in vacuum. It's a solution to a problem. The problem is defined by the product.

The product offers a service to the consumers, whether they are end users or internal consumers. It solves a problem for someone. It can be:

An app that's used to measure running distance and sharing it with other runners

A website for booking hotels

An infrastructure platform that's used by other teams

A time-report system

etc.

The engineers usually work in a team led by an EM.

The Engineering Manager is accountable for the engineers as well as the technical artifacts they produce:

When the team is large or the tech is too complex (or both), the EM may not have enough bandwidth to do justice for both their people and technical accountability:

To increase their bandwidth, EM's are faced with a choice:

Delegate admin work: To optimize the HR processes and tooling or hire an admin assistant to lift some of the people management load from their shoulder

Delegate technical load: To hire a Staff Engineer to lift some of the technical load from their shoulder.

You may argue if having a dedicated admin assistant is justified at a team level, but I have seen one admin assistant shared by multiple teams. AI can cover some of the mechanical activities like scheduling events, answering admin questions, and gathering continuous feedback. Good HR tooling and processes can reduce the admin load as well.

Subscribe

Nonetheless, the admin assistant or AI is not supposed to take over the EM's people accountability like building a good team, mentorship, performance review, hiring, etc.

Previously we've argued that hiring a Staff Engineer to take over the technical aspects of Engineering Management is an anti-pattern.

Particularly, Staff is not supposed to act as a translation layer between the tech and engineers for the EM:

Engineering manager needs to be technical and we have covered some ways to keep the technical skills sharp here.

How can engineer leaders stay technical?
ALEX EWERLÖF
·
NOVEMBER 24, 2024
Read full story

Staff Engineer could be useful when:

The technical load is beyond the capacity of EM. For example:

Legacy tech that requires intense babysitting/migration

Overly complex solution that spans across teams or requires deep technical knowledge

Simply because the EM isn't technical (it's an anti-pattern but they do exist)

A clear accountability can be established for a subset of technical load

The tech expands the boundaries of individual EMs (more on that later)

Organizations that have Staff, should hold them accountable for the technology, not people:

Please don't read too much into this. 🙂 People are different. Products are different. And both change over time.

There's a small but important difference between responsibility and accountability that we've covered in a separate article:

Accountable vs Responsible
ALEX EWERLÖF
·
NOVEMBER 29, 2024
Read full story

The Staff Engineer should be deeper in the technology and have higher technical literacy tied to an accountability. The lack of people responsibility opens up their schedule to be more invested in tech. But the Engineering Manager is not supposed to be completely off-hand either.

So we went from this:

To this:

Now I have some bad news. Having Staff Engineer at the team level is an overkill. As we'll discuss in a minute, the real value of the Staff Engineer comes from operating across teams. Besides, having two roles accountable for tech can create confusion and breaking one role into multiple titles:

Breaking a role to multiple titles
ALEX EWERLÖF
·
NOVEMBER 3, 2024
Read full story

However, there are cases when a Staff Engineer may operate in the scope of one team. For example:

Legacy tech stack with a steep learning curve when the EM is new

When onboarding a new Staff Engineer (starting from a smaller scope)

Too much tech debt piled up and hurting the tech health metrics

Complexity getting in the way of maintaining the tech

In all those examples, team-scoped Staff Engineer can be a temporary position.

Where Staff Engineers really shines is:

Acting as glue between the teams.

Working shoulder-to-shoulder with other engineers and being their voice in the upper management room. Turns out engineers are much more open with other engineers than when communicating with the person who has mandate over their salary, vacation, performance review, and raise.

Getting very deep into the technical aspects. Unlike EMs, Staff Engineers don't spend a lot of time in meetings, 1:1's, and various administrative activities. That extra time should be spent on honing their engineering skills and technical depth in order to lead the technical decisions effectively.

By far, the biggest pitfall ahead of Staff+ Engineers is to turn into Ivory Tower Architects.

Ivory Tower Architect
ALEX EWERLÖF
·
OCTOBER 31, 2024
Read full story
Staff Engineer for a system spread across multiple teams

In his seminal essay Will Larson, identified 4 archetypes for Staff Engineers:

Tech lead

Architect

Solver

Right hand

What's shown in the diagram above is a Tech Lead operating within one team. Calling that role a Staff Engineer is a bit of a stretch.

Introduction to the role of Staff Engineer
ALEX EWERLÖF
·
FEBRUARY 26, 2024
Read full story

That's because most of the value of the Staff Engineer comes from operating across multiple teams:

Often, the tech that is owned by one team is just a piece of the puzzle. The larger system or domain may be spread across multiple teams or at least has tight dependencies across the org.

In this scenario it makes sense to have a dedicated role (Staff Engineer) for the entire system regardless of which team owns which piece of it.

Subscribe

Here's the catch: the "tech" doesn't talk or listen:

The tech doesn't exist in vacuum!

For Staff engineers to deliver their true value, they have to go through both people (engineers) and product:

And that's why Staff Engineers have all those "dotted reporting lines" (the unofficial but critical collaborations and commitments across the org):

Those with the kin eyes may ask why the arrow is pointing from the Staff to "lower" positions (in the career ladder). The answer is two-fold:

Good leadership is about collaboration not authority. See it as Staff going to a team-level EM or PM and asking for favors in a way that fits the engineers and product roadmap, not demanding to lift the state of tech in isolation

Staff Engineer is an IC (individual contributor) and by definition does not have any direct reports. If you're lucky to have a sync channel with EM/PM, please don't waste it in regular report, but instead turn it to a 2-way dialogue about the state of tech (status quo) and where the tech needs to be to solve the emerging product problems (vision) as well as cohesive actions to take us there (organizational tech strategy).

All these reporting lines can be overwhelming. One tool to align product teams across the org is a strategy document:

Strategy basics
ALEX EWERLÖF
·
DECEMBER 5, 2022
Read full story

There are other ways to reduce the span of tech to one team through deliberate organizational architecture. We've discussed one powerful alternative in Kebab vs Cake model using consumer journeys:

Kebab vs Cake organization
ALEX EWERLÖF
·
AUGUST 7, 2024
Read full story

Staff Engineers should have clear accountability over a system. That means they expose 3 elements of ownership:

Knowledge: They know the tech stack, the product problem and can speak fluently about it as well as code when needed

Mandate: They have a say in how the tech evolves and is maintained.

Responsibility: They are held accountable for the health of the tech (e.g. incidents, tech debt, documentation, tech defragmentation, etc.)

As we discussed before, Staff Engineer is not a pure technical role and heavily relies on soft-skills to influence the technical organization.

Funny enough, focusing too much on soft-skills is one of the most dangerous pitfalls ahead of Staff Engineers. It turns them to Ivory Tower Architects:

Conclusion

Not all organizations need Staff Engineers, especially when:

EMs are technical enough to manage their team's tech

Tech stack is healthy enough that doesn't need a dedicated technical steward

The tech has high cohesion and does not span across multiple teams (one way to achieve that is the Cake organizational architecture)

The engineering organization is mature enough to find the best way forward for the system they collectively own without the need for a dedicated owner

For orgs that have Staff Engineers, they should clarify the technical ownership and hold the Staff Engineer accountable for it

Ivory Tower Architect is bad

Breaking a role to multiple titles is inefficient

Non-technical EM is inefficient

And just like any essay by some random person on the internet, please please please use your best judgement and don't get stuck in cargo culting.

Cargo culting
ALEX EWERLÖF
·
NOVEMBER 10, 2024
Read full story

I didn't write some universal laws of physics. You know what is best for your particular technology, product, operations, and people.

T-POP
ALEX EWERLÖF
·
MARCH 18, 2024
Read full story

If you have counter-arguments, feedback, corrections, or questions, let me know in the comments down below. 🙏

If you find this post insightful, please share it in your circles to inspire others. 🙌

Share

You can also share your thoughts and comments on HackerNews.

My monetization strategy is to give away most content for free. However, these posts take anywhere from a few hours to a few days to draft, edit, research, illustrate, and publish. I pull these hours from my private time, vacation days and weekends.

You can support my work by sparing a few bucks for a paid subscription. As a token of appreciation, you get access to the Pro-Tips sections as well as my online book Reliability Engineering Mindset. Right now, you can get 20% off via this link. You can also invite your friends to gain free access.

Subscribe to Alex Ewerlöf Notes
Launched 4 years ago
Technical Leadership, Reliability Engineering, Growth
Subscribe
By subscribing, you agree Substack's Terms of Use, and acknowledge its Information Collection Notice and Privacy Policy.
276 Likes
∙
15 Restacks
276
10
15
Share
