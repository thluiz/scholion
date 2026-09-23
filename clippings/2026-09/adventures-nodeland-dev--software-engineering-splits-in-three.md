---
url: "https://adventures.nodeland.dev/archive/software-engineering-splits-in-three/?utm_source=weeklyfoo&utm_medium=email&utm_campaign=weeklyfoo"
captured_at: "2026-09-23T17:31:23+01:00"
title: "Software Engineering Splits in Three"
domain: "adventures.nodeland.dev"
---

March 15, 2026
Software Engineering Splits in Three
"AI-assisted coding changes the game for enterprises by shifting the bottleneck from coding to judgment, impacting software builds and roles."

A few weeks ago, I wrote about the human in the loop and why review is now the bottleneck in software development. Then I wrote about what this means for careers and students entering the field.

But one question kept coming up in conversations: what does this mean for organizations? Not startups. Not tech companies. Enterprises. The banks, insurers, manufacturers, and retailers that run on software but don't think of themselves as software companies.

The Old Model Is Breaking

A major regional bank spent months weighing whether to build or buy a new payment reconciliation system. Stakeholders wavered, unable to make a clear decision. In the meantime, a processing error went undetected, delaying thousands of business transactions and triggering a $2 million regulatory fine and weeks of negative headlines. The cost of getting this decision wrong isn't just about overspending on a vendor; it's about risk, reputation, and real operational pain.

For decades, enterprises had two choices for building software:

Build it yourself. Hire a team, manage them, hope they don't leave. Expensive, slow, risky. Reserved for core systems.

Buy it or outsource it. SaaS for commodity needs. Consulting firms like Accenture or Deloitte for custom work. You'd sign a big contract, they'd provide bodies, and eighteen months later you'd get something that sort of worked.

Neither option was great. Building was too expensive for most needs. Buying meant working around software that didn't quite fit. Outsourcing meant paying senior rates for junior developers, then watching all the knowledge walk out the door when the engagement ended.

AI is breaking this model. But not in the way you might think.

What AI Actually Changes

The discourse focuses on "AI can code now." That's true but incomplete.

Gergely Orosz recently wrote about what happens when AI writes almost all the code. His conclusion: software engineers become more valuable, not less. But the nature of the work changes. Tech lead traits are in more demand. Being "product-minded" becomes a baseline at startups. Being a solid software engineer, not just a "coder," will be more sought after than before.

What AI actually changes is the economics of implementation. The cost of turning a well-defined requirement into working code has collapsed. As Malte Ubl, CTO at Vercel, put it: "the cost of software production is trending towards zero." What used to take a team of developers weeks now takes hours.

But here's what hasn't changed: someone still needs to know if the implementation is correct. Someone still needs to understand the business problem well enough to define the requirement. Someone still ought to maintain the system when the business evolves.

The bottleneck has shifted from coding to judgment.

The New Landscape

I see the market stratifying into three tiers, each with different needs.

This echoes Gergely Orosz's research on the trimodal nature of tech compensation. He showed that software engineering compensation isn't a single bell curve but three distinct markets: Big Tech and top scaleups at the top, companies competing for global talent in the middle, and everyone else competing locally at the bottom. Each tier has different compensation, different expectations, and different ways of working.

But here's what's changing: the three tiers existed before, but the work was fundamentally similar across all of them. You could start as a Software Engineer (SWE) at a regional bank, apply for a job at a tech giant, and get the job. In both places, you would write code, review pull requests, and debug production issues. The skills were transferred. You could move between tiers. A few years at a local company, then jump to a tech company, then maybe back to enterprise for work-life balance. The ladder was climbable.

AI breaks this. When implementation becomes cheap, and judgment becomes the bottleneck, the tiers start to diverge not just in compensation but in what the work actually is. The skills required at each tier are becoming genuinely different. And that has ramifications for career mobility, talent pipelines, and how organizations think about building software.

The tiers won't just differ in compensation. They'll differ in how software gets built, who builds it, and what skills matter.

Tier 1: Technology Companies and Digital-Native Giants

Software is the product. These organizations have platform engineering teams, SRE teams, and in-house deep expertise. They're building at massive scale and leading industry practices. They collaborate directly with upstream vendors and open-source projects, sometimes employing core maintainers or funding the development of the tools they depend on. For key infrastructure that they don't want to build or maintain themselves, they have support contracts and licenses with specialized vendors who know the technology better than anyone.

These organizations need senior engineers who can review AI-generated code and catch the subtle bugs that pass tests but fail at scale. AI is a force multiplier here, not a replacement. The same team ships more. But the team is still human, still senior, still accountable.

Example: Maria is a senior SWE at a major e-commerce platform. Her team operates the checkout system that processes millions of transactions daily. When she needs to optimize the payment flow, she prompts Claude Code to generate the implementation, but she spends most of her time reviewing whether the changes will hold up under Black Friday traffic. She understands distributed systems, latency requirements, and failure modes. When she hits a performance bottleneck in a core library, she opens an issue upstream or contributes a fix directly. For the parts of the stack her team doesn't want to own, they have enterprise support contracts with the vendors who built it. AI writes the code. Maria decides if it's the right code.

Tier 2: Large Enterprise

Banks, insurers, large retailers, telcos. Software is critical to their business, but it's not their core product. They have substantial engineering organizations, but they're competing with Tier 1 companies for talent and often losing.

These organizations can't build their own internal platforms to the same standard as tech companies. They can't hire enough senior engineers to cover all their needs. But they still need to ship software safely, and they still need judgment.

This is where the model changes most dramatically. These organizations will rely on platforms that provide sane defaults and built-in guardrails. And they'll bring in fractional senior expertise when they need judgment they don't have internally.

Example: James works at a large insurance company. He's part of an IT organization of 200 engineers, but they're not Stripe. They're building a new claims processing system using AI-assisted development, and the code is flowing fast. The platform they chose handles deployment, observability, and performance monitoring, giving them guardrails they couldn't build themselves. When they reach an architectural decision on event sourcing for audit trails, they bring in a fractional consultant for a few days to review the approach and point out pitfalls they hadn't considered.

Tier 3: Mid-Market and Small Business

The local manufacturing company needs production tracking. The restaurant needs a reservation system. The accountant's office needs a client portal.

These businesses couldn't afford custom software before. Now they can. But they're not buying enterprise platforms or hiring consultants. They're calling the local software developer, the same way they call the plumber.

This tier is a different market entirely, and I'll come back to it.

Example: Sofia runs a small software consultancy. Her clients are local businesses: a manufacturing company that needs production-quality tracking, a group of dental practices that want shared patient scheduling, and a wine distributor who needs inventory management that works the way they actually operate. None of these businesses could have afforded custom software five years ago. Now Sofia can build exactly what they need in a few days using AI-assisted development. She's not an expert on distributed systems. She's an expert in understanding what her clients actually need and delivering working software that solves their problems.

What Enterprises Should Do

If you're running engineering at a Tier 1 or Tier 2 organization, here's what I think you need to consider:

Platform Engineering Is More Critical Than Ever

When AI generates code faster than humans can reason about it, the platform becomes your safety net.

Guardrails over gates: that's the rule for modern platforms. The platform should enforce standards automatically and provide observability so you can see what's happening in production. It should make the right thing easy and the wrong thing hard.

If you don't have a platform engineering function, you need one. If you're too small to build your own platform, you need to buy one.

SRE Is More Important, Not Less

More code shipping faster means more things that can break in production. Your SREs become the last line of defense against AI-generated code that passes review but fails in production.

The SRE role evolves from "keep the systems running" to "catch what the review missed." They need to understand not just operations, but also the business logic that the code implements.

The Talent Pipeline Problem Is Real

If the "Jira ticket to clock-off" developer role is gone, where do your future senior engineers come from? Let's look at the numbers: imagine a 200-person engineering team that loses five senior engineers per year and promotes only three. If junior hiring stops altogether, that leaves a net deficit of two senior engineers annually, with no fresh pipeline to fill those future roles. Multiply that gap over a few years, and your organization's expertise erodes much faster than it can be replenished.

You can't just stop hiring juniors. The math doesn't work long-term. But you also can't hire juniors and expect them to learn judgment from doing tickets that AI now handles.

Internships become critical. Real exposure to real systems with real consequences. Pairing with senior engineers on review, not just implementation. Learning to ask "is this right" rather than "does this work."

Some organizations will solve this by poaching senior engineers from tech companies. Expensive and creates its own cultural challenges. Others will partner with external firms that provide senior expertise. The key is recognizing that judgment has to come from somewhere.

The Consulting Model Is Changing

The old consulting model was body shopping. You paid for hours of implementation, billed at rates that assumed senior expertise yet often delivered junior work.

That model is dying. AI does the implementation now.

The new model is fractional senior expertise. You don't need twenty developers for eighteen months. You need one senior architect for 2 days a week who provides judgment, reviews what your internal team and AI produce, and helps you avoid architectural mistakes.

The value proposition flips. You're not paying for implementation time. You're paying for judgment quality.

Consider What Should Be Custom vs. Commodity

Here's where AI changes the buy-vs-build calculation.

Before, custom software was so expensive that you built it only for true differentiators. Everything else, you bought SaaS and worked around the limitations.

Now, custom software is much cheaper to build. Some things that were "not worth building" before become feasible: integrations that would have required a consulting engagement, internal tools that never made the priority list, and workflow automations specific to how your organization actually works.

Still, not every idea needs a custom solution. Here's a quick checklist to help test if an initiative is truly "custom-worthy":

Does this process give your organization a competitive advantage, or is it central to how you deliver value?
Are off-the-shelf or SaaS solutions unable to support your unique requirements without unacceptable workarounds?
Will this tool need to evolve with your business or help you maintain flexibility over time?

If the answer is yes to two or more, you likely have a good candidate for custom software. If not, consider if a tailored off-the-shelf option gets you most of the way there without the extra investment.

But "cheaper" doesn't mean "free." You still need judgment to decide what to build, review to ensure it's built correctly, and maintenance when requirements change.

The question shifts from "can we afford to build this" to "do we have the judgment to build and maintain this well." But to actually elevate decision-making, it is not only about cost or capability—it is about identifying where bespoke software can create an unfair advantage for your business. The most strategic leaders will ask: Where does custom software allow us to do what competitors cannot?

The Tier 3 Opportunity

Small businesses are a different market, but it's important.

For decades, custom software was only for big companies. Small businesses used off-the-shelf products and worked around their limitations. Or they used nothing at all.

AI changes this. A skilled developer with AI assistance can now build custom software for a small business at a price point that makes sense.

Think of all the WordPress and Joomla customizations that small businesses relied on. Now extend that to actual custom applications. Actual solutions to problems that no SaaS product solves because the market is too small.

This creates a new role: the software plumber. Local developers who serve local businesses. Who understands the business setting, can translate needs into requirements, and can be there when something breaks.

The skills differ from those of enterprise engineering. Less about distributed systems and scale. More regarding understanding business problems and shipping working solutions quickly. But it's real software work, and it's a growing market.

What This Means for Your Organization

The future of software engineering is not "AI replaces developers." It's more subtle than that.

Enterprises must now focus on cultivating experienced engineering talent, prioritizing robust platforms and guardrails for AI-assisted development, and evolving consulting models toward fractional senior expertise rather than traditional body shopping. Success depends on building sound judgment within teams, ensuring SREs can address gaps in AI-generated code, and proactively developing the next generation of senior engineers.

If you're leading engineering at an enterprise, the questions you should be asking:

Are we still buying SaaS for things we could now build custom?
Do we have the platform and guardrails to safely ship AI-assisted code?
When we need external expertise, are we paying for implementation or judgment?
Do we have the senior expertise to review what AI produces?
Where will our future senior engineers come from?

The human in the loop isn't going away. The human becomes more important as the tools become more powerful.

But which humans, doing what work, with what support? That's what's changing. And that's what companies need to figure out.

Don't miss what's next. Subscribe to Adventures in Nodeland:
Email *
SUBSCRIBE
← Newer
The DCO Debate: Who Is Responsible for AI-Generated Code?
Older →
Your Coding Agent Keeps Making the Same Mistakes. I Built a Fix
Share this email:
Share on Twitter
Share on LinkedIn
