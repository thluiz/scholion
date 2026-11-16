---
url: "https://dev.to/integerman/defining-technical-debt-2e08"
captured_at: "2026-11-16T19:16:22+00:00"
title: "Defining Technical Debt"
domain: "dev-to"
---

I was looking for a definition of technical debt for [a talk I’ll be giving next month](https://www.codemash.org/session-details/?id=143477) when I discovered something that shocked me: I couldn’t find a simple definition of technical debt out there on the internet.

This article is an attempt to clearly define technical debt, its impacts, and causes. Along the way I’ll also highlight some metaphors that are helpful when discussing technical debt with others.

## [](#my-definition-of-technical-debt)My Definition of Technical Debt

I tried to come up with a comprehensive definition of technical debt on my own. I came up with this:

> A state of unnecessary complexity, duplication, subpar code, or otherwise deficient code that introduces risks in the form of time, quality, security, team morale, or other forms.
> 
> Typically the result of past action or inaction.
> 
> Matt Eland (Me)

While this definition is fairly broad and comprehensive, it doesn’t read terribly well and it just feels _clinical_.

## [](#adam-tornhills-definition)Adam Tornhill’s Definition

A few weeks later, I was reading Adam Tornhill’s excellent book, [Software Design X-Rays](https://pragprog.com/book/atevol/software-design-x-rays) and I found this definition:

> Technical debt is code that’s more expensive to maintain than it should be.
> 
> Adam Tornhill, [Software Design X-Rays](https://pragprog.com/book/atevol/software-design-x-rays)

I love this definition.

Specifically, I love how simple, yet open it is. The phrase _more expensive to maintain_ in particular is broad enough to cover:

*   Productivity / time loss
*   Quality risk in the form of added defects
*   Morale loss from bad code

While I can’t say that Adam intended it to cover these things, I am happy that it does.

## [](#causes-of-technical-debt)Causes of Technical Debt

Adam’s definition is good, but it doesn’t speak to the causes of technical debt much. To be fair, my definition doesn’t speak much to that, so let’s discuss it now.

I write a lot on technical debt and I will occasionally get comments to the effect of _“If your engineers just did it right the first time, we wouldn’t have technical debt at all”_.

I think these types of comments are common thoughts, but illustrate a slight misunderstanding of the nature and origin of technical debt.

Sure tech debt can come about because I was lazy or feeling a little sick and made some stupid mistakes, left some unfinished TODO comments in my code, or otherwise cut corners.

Yes, tech debt can come about from developers not having the skills or knowledge to properly do what they’re attempting to do. This often happens when developers work on threading, database, or web service communication code for the first time.

## [](#strategic-debt-and-the-financial-metaphor)Strategic Debt and the Financial Metaphor

However, just as frequently, technical debt can be strategic in nature – when a team needs an urgent fix for a problem we didn’t anticipate having and need to cut corners, for example. Additionally, teams operating under urgent deadlines will cut corners at the encouragement or requirement of the deadlines the business has accepted.

This means that technical debt can be a strategic decision. This is where the _financial metaphor_ most comes into play.

Under the financial metaphor, we can look at taking on debt as a loan with all detrimental effects as interest in that loan as illustrated by the following waterfall chart:

[![](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F2nsnwn9o2wim6swj1153.png)](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F2nsnwn9o2wim6swj1153.png)

For more information on the contents of this chart and how technical debt impacts us over time, take a look at my article on [understanding the true cost of technical debt](https://killalldefects.com/2019/11/09/the-true-cost-of-technical-debt/).

## [](#farming-and-the-impact-of-technical-debt)Farming and the Impact of Technical Debt

To talk about the impact of technical debt, I’d like to turn to the field (no pun intended) of farming.

[![](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fl3n2foah2gxjqq16z8ow.png)](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fl3n2foah2gxjqq16z8ow.png)

_Photo by Douglas Williams on Unsplash_

Most people know that if you continually plant the same crops in a field year after year without letting the field rest, you’ll eventually get a diminishing return from the field.

This is because the crops have depleted the nutrients in the soil so the same amount of effort results in a diminishing amount of return over time.

By the same token, if you constantly run your development teams ragged implementing feature after feature, bugs will be more prevalent due to diminished code quality, and you’ll find it takes more time to get features to market overall.

The answer in farming is to leave the field fallow for a season or rotate in nutrient enriching crops that replenish the soil.

With technical debt, the answer is to allocate time to pay down technical debt. See my dedicated article on [strategies for paying down technical debt](https://killalldefects.com/2019/10/02/strategies-for-paying-off-technical-debt/) for more details.

## [](#atrophy-and-technical-debt)Atrophy and Technical Debt

Technical debt can also come about in the form of software atrophy and aging. Let’s say I wrote a beautiful application in SomeNewWebFramework 2.0. It’s perfect in every way. The users love it and the code is clean and maintainable.

Fast forward a few years and SomeNewWebFramework 4.2 was released to market. Our code is still on 2.0, meaning that it takes a bit of time and effort to move us up to the more modern version. On top of that, the release notes for version 4.2 mention that they fixed some security vulnerabilities that were unknown previously, but have existed since version 1.0.

This example illustrates how an application can go from cutting edge to legacy code in a short amount of time – without any changes to its code at all.

Software atrophy is real and it constitutes an infrequently recognized form of technical debt.

## [](#pipes-and-arteries)Pipes and Arteries

I don’t frequently like to give this metaphor because it is slightly morbid, but you _can_ compare technical debt to the build up of corrosion in pipes or plaque in arteries.

[![landscape photograph of brown hill under blue sky](https://res.cloudinary.com/practicaldev/image/fetch/s--rIZN78uH--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://images.unsplash.com/photo-1505797051774-a1839fcca67f%3Fixlib%3Drb-1.2.1%26ixid%3DeyJhcHBfaWQiOjEyMDd9%26auto%3Dformat%26fit%3Dcrop%26w%3D1000%26q%3D80)](https://res.cloudinary.com/practicaldev/image/fetch/s--rIZN78uH--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://images.unsplash.com/photo-1505797051774-a1839fcca67f%3Fixlib%3Drb-1.2.1%26ixid%3DeyJhcHBfaWQiOjEyMDd9%26auto%3Dformat%26fit%3Dcrop%26w%3D1000%26q%3D80)

Photo by [Drew Sal](https://unsplash.com/@drewsal?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/pipe?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

Over time, bad code will naturally build up in a system like corrosion or plaque in our metaphors. This build up reduces the ability of new work to flow through the system, effectively slowing down the velocity.

It also makes it more likely that the flow of work through the system will result in blockages or free up deposits and push them downstream, leading to major issues that are the equivalent of strokes and heart attacks in humans.

Like I said, this one is more morbid, but if you find someone isn’t understanding the farming metaphor, it can be helpful to compare the quality issues you’re doubtlessly experiencing with build up in pipes and arteries.

This comparison is necessary because the fix is to stop (or severely reduce) the work flowing through the system and invest in invasive procedures to pay down the technical debt before it kills your product.

## [](#closing-thoughts)Closing Thoughts

Since I don’t want to end talking about heart attacks and strokes as they apply to software, let’s close with something different.

Talking about technical debt in a way that your organization can understand and prioritize is important. More than that, it’s a key part of the workload of technical leadership, who must balance multiple things including:

*   Hiring, training, and retaining developers
*   Planning the architecture and code needed for where the business is going
*   Managing implementation of technical priorities for the business
*   Helping the business meet its strategic goals
*   Reducing costs of the IT infrastructure
*   Communicating critical risks to the organization in terms of technical debt and quality deficits

If you’d like to learn more about communicating technical debt, I strongly encourage you to read my article on [communicating technical debt](https://killalldefects.com/2019/10/01/communicating-technical-debt/) or [attend my talk at CodeMash on January 9th, 2020](https://www.codemash.org/session-details/?id=143477).

The post [Defining Technical Debt](https://killalldefects.com/2019/12/23/defining-technical-debt/) appeared first on [Kill All Defects](https://killalldefects.com/).
