---
url: "https://dev.to/integerman/communicating-technical-debt-3gbd"
captured_at: "2026-11-16T01:59:30+00:00"
title: "Communicating Technical Debt"
domain: "dev-to"
---

Many developers feel that product management and executive leadership don't "get it" when we talk about technical debt. At the same time, if you ask developers about factors vital to the long-term success of a project, paying down technical debt is high on the list. So, how can we communicate technical debt in a way that bridges that gap?

As a development manager, a core part of my job is to act as a bridge between product management and development teams. Let me share with you what's worked well for me so far.

This post is inspired, in part, by bob.js' wonderful article on [Accounting for Technical Debt](https://dev.to/rfornal/accounting-for-technical-debt-2pf0) and is intended as a bit of a companion for that article.

## [](#defining-technical-debt)Defining Technical Debt

Let's start from Webster's definition of debt:

> Debt: a state of being under obligation to pay or repay someone or something in return for something received : a state of owing

In this context, we incur technical debt by taking temporary advantage of something while incurring an obligation to pay it back.

## [](#principle-and-interest-in-technical-debt)Principle and Interest in Technical Debt

Extending further, we pay additional **interest** for our debt over time, meaning that a small piece of technical debt becomes larger over time.

As an example, if we cut some corners in implementing a feature by duplicating a method and making slight modifications, we pay interest on that decision every time we need to make a change that _should_ modify both methods.

Even if only one method is actually modified, the failure to modify the duplicated method likely constitutes a bug, introducing a form of quality debt into the application in the form of a hidden bug waiting to be encountered.

In this example, the **principle** of the technical debt is the time saved during initial implementation while the **interest** is the additional time, quality, and risk costs incurred for that decision until the point that it is resolved.

I particularly like the financial analogy when talking about technical debt because it takes something hidden and unknown to business-oriented professionals and puts it in terms that they work with on a day to day.

This also highlights that while technical debt can be advantageous in the short term (when interest paid is less than the principle borrowed), it can be ruinous in the long-term.

## [](#penalties-for-technical-debt)Penalties for Technical Debt

Above I mentioned the **increased amount of development time** penalty paid on future items when technical debt is in effect. This is likely the largest form of technical debt that we talk about as developers.

Additionally, we touched on the **quality debt** that can be incurred by brittle and unmaintainable code, lack of unit tests, and duplication that results in inconsistent behavior when modifying code. This is a form of risk that we pay off as interest when working with tech-debt heavy areas of code.

Another form of interest we pay on technical debt is **poor application performance**. This is typically paid when technical debt is at the design level as most performance issues ultimately turn out to be poorly designed flows through a system. Yes, you can make tactical improvements to code performance for days and weeks on end, but at a certain point it's hard to get additional improvements until you redesign with performance in mind.

**Security vulnerabilities** are another form of risk that we can incur as interest on technical debt. Uniquely, though, this does not just manifest itself as code is changed, but the risk starts from the day a vulnerability is present and continues on until it is resolved.

Finally, we do pay a **morale penalty** to developers when working on substandard code. This is frequently not isolated to just developers, however, as many developers are vocal about the more _interesting_ bits of code they discover and this affects anyone within earshot.

I would further argue that poor code inside of the codebase encourages substandard work on the project because it is shown to be an acceptable level of workmanship, so this form of debt encourages future debt.

## [](#talking-to-business-about-technical-debt)Talking to Business about Technical Debt

Okay, so now we've talked about what debt is and the interest we pay until it is resolved, let's talk about communicating these things to business stakeholders.

First of all, product management and business stakeholders are **not** your adversary. These are your key partners. Any discussion with business on code needs to have trust and respect at its core - from both sides - or friction is guaranteed to occur and success is far less likely.

I would take it a step further and say that establishing a relationship of trust, collaboration, and respect with business partners is **even more important** to the long term success of a project than technical debt.

In order to have a healthy and productive conversation with business stakeholders, you need to do at least the following things:

*   Come at the conversation looking to improve _understanding_ in both you and them. You want to inform them of current and future obstacles and the prices paid by past decisions and you need to hear and understand their needs.
*   You need to have an extreme amount of professionalism. Developers love to have fun, but when we're alien to the business in our conduct, it's not too hard to see why the business might not think that we're not capable of thinking about the things they think about.
*   Have both data and anecdotal evidence to back up your claims.
*   Have a few key top priority technical debt items already identified.
*   Have flexible plans for resolving things that can be modified by business needs.
*   Have an idea of how long that it will take to resolve things.
*   Have ideas for ensuring that technical debt becomes less of a problem in the future.
*   Be prepared to give progressive status reports as technical debt is paid down.

When talking to business stakeholders about serious levels of technical debt, you are essentially a doctor giving a patient a warning about health complications and future consequences. You need to tell the truth while not being alarmist, and you need to offer a plan to remedy the situation and monitor it going forward.

We'll talk more about these things in a bit.

## [](#isnt-technical-debt-the-developers-fault)"Isn't Technical Debt the Developer's Fault?"

I hear this question sometimes from business. It's often not asked in a malicious way and it's even asked reluctantly at times. Most business people don't understand the nature of software development or software projects because they haven't developed code for them. As such, it's completely reasonable to assume that technical debt is the developer's fault.

The truth about this assumption, unfortunately, is that sometimes technical debt _is_ our fault. Sometimes we didn't warn on the consequences of a decision as it was being made, sometimes we didn't notice it until it was too late, and sometimes developers get lazy, make mistakes, or are still growing the full set of skills they need.

However, I choose to believe that the majority of technical debt is not our fault or is detected too late to change without jeopardizing key business goals.

An analogy I like to make when dealing with business stakeholders who blame development for technical debt is one from farming.

In farming, if you repeatedly farm the same land season after season after season, you systematically render that land less fertile and productive by draining the nutrients from the soil. This is why farmers have adopted techniques such as crop rotation (leaving a field fallow or empty in off seasons to recharge) or to substitute soil-enriching crops for soil-depleting crops every so often to help fields recharge.

In this analogy, it makes it clear that while developers are working on what the business wants, project after project, the lack of time available to weed out the fields and allow the metaphorical soil to recharge is ultimately reducing the crop yield. You ultimately don't have bad farmers (developers), but a farming strategy and schedule that optimizes yield for the first few seasons at the expense of long-term viability.

## [](#the-business-perspective)The Business Perspective

Sometimes sacrificing long-term health of a codebase is actually acceptable.

Sometimes you critically need to finish a project to stay in business. Sometimes you plan on completely rewriting an application or retiring it after a number of iterations in favor of a replacement. In this case, productivity in the short run _should_ be the primary concern.

Other times business simply doesn't understand. They live in the world of looking at the needs of stakeholders, sales goals, deals won and lost, contracts at risk, support incidents, bug counts, and other concrete and understandable things and when they hear technical debt, it can be easy to assume it just means "code I'm not particularly fond of" and not "a massive quality risk waiting to unleash a flood of defects on our users".

This is why they need us to translate our day-to-day into something they can understand.

That means we have to look at metrics. Armed with data from issue tracking systems, time tracking systems, source control, code analysis tools, test coverage results, CI/CD pipelines, performance monitoring tools, and other sources you can put together some interesting figures such as:

*   Defects by area of the application
*   Time needed to complete a single feature (particularly over time as this shows losses in productivity)
*   Time spent on development vs support activities
*   % of code that is covered by unit tests over time
*   "code smells" by source file
*   "code smells" over time
*   % of incoming requests that result in errors

Be creative. The exact metrics that are appropriate for your code are going to be unique to your organization and your current flavors of technical debt. If you need ideas on analyzing problems and coming up with ways of representing them, take a look at my post on [the 7 basic tools of software quality](https://dev.to/integerman/the-7-basic-tools-of-software-quality-16i1).

## [](#code-analysis)Code Analysis

Code Analysis tools are something I absolutely would lean on. These could be anything from compiler or linter warnings to a dedicated tool that analyzes a codebase and generates recommendations. The exact tools used will vary by the programming language you're using, but I'll share what works well for me.

I use [SonarQube](https://www.sonarqube.org/) / [SonarCloud](https://sonarcloud.io/) to scan a wide variety of code in many different languages.

[![Sonar Cloud Issues List](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fs91njyse3sowp3c4xql2.png)](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fs91njyse3sowp3c4xql2.png)

This can also help me prioritize which files need attention most in a very visual manner suitable for communication with business stakeholders:

[![Sonar Cloud Files by Code Smell](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fei9ttm0qptmlhhzvomoy.png)](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fei9ttm0qptmlhhzvomoy.png)

While SonarQube / SonarCloud is good for simple tracking that works well out of the box, more in-depth and customizable analysis may be necessary and should come from a specific tool suited to your programming language.

I use [NDepend](https://ndepend.com/) to analyze .NET assemblies and get detailed metrics and visualizations as to everything wrong with those projects in order to prioritize and track code smells over time.

[![NDepend Dashboard](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fuu7g21b5uo0vkmo6m2ee.png)](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fuu7g21b5uo0vkmo6m2ee.png)

NDepend, in particular, can pinpoint methods by size and complexity, code coverage, etc. and generate some very helpful graphs and charts for prioritizing and even potentially communicating technical debt.

[![NDepend Tree Map](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F0x4ebt1y13nqzskhvlh8.png)](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F0x4ebt1y13nqzskhvlh8.png)

_Disclaimer: While I have previously paid for NDepend, my current copy was provided by the developer_

## [](#tips-for-communicating-with-business-stakeholders)Tips for Communicating with Business Stakeholders

So, now that you have the metrics and data you need to prioritize and communicate technical debt, let's talk about that conversation.

First, you need to determine how big of a deal this is. This can range from a 30 second elevator pitch of "We'd really be more productive if we could fix X. Can I send you a short E-Mail with some details and get this included in a future sprint?" to "I've been looking at our code quality and I have some concerns I'd like to share with you. I'd like to set up a meeting for later this week to go over them and talk about some possible solutions. What day would work best for you?"

Second, you need to put together the appropriate level of communication. Typically this is going to be anywhere from a paragraph-long E-Mail to a one or two page report or a 5-10 slide deck. Your goal is to concisely communicate the problem to them in a way that they can understand and participate fairly in a discussion for prioritizing and planning a remedy for the issue.

Thirdly, you need to take their communication styles into account. Some people hate E-Mail or phone. Others hate formal meetings. Style matters too - some people want concise confident statements without any preliminaries while others want to really interact with you and shoot the breeze before getting to business. Some people are motivated by hard facts while others are swayed by stories of how individuals are impacted. Know your audience. When in doubt, try a mixture of approaches or have anecdotes ready to share if your data flops.

I would highly recommend keeping your presentation focused on the bare minimum needed to adequately communicate the problem. Do your homework going into the meeting, but don't bore them. If an executive wants details, they'll ask for it. You're not trying to sound smart or win points here - you're trying to bring a partner into a problem solving world that's not their forte.

Present your proposed plan for remedying things to them as part of the presentation. Expect to be asked questions around how many resources you'll need, how long it will take, what the risks are, and what things the business will be unable to do in the short term due to the loss of resources.

The other thing I would caution against going into these meetings - fair or otherwise - is that many at the executive level are focused on people's clock-in and clock-out times and if you're telling them you need to be able to dedicate time to technical debt and the dev team leaves immediately at closing time every day, shows up late, or takes long lunches, the executives may have trouble focusing on what you're saying - right or wrong, this just tends to be how many people think at that level.

## [](#closing)Closing

Now that we know how to communicate technical debt to business stakeholders and, hopefully, get buy in, let's look at [some strategies for paying down technical debt](https://dev.to/integerman/strategies-for-paying-off-technical-debt-2da9).

What's worked for you when talking with business stakeholders? What obstacles have you encountered other than what I've shared above?

* * *

Photo by Sabine Peters on Unsplash
