---
url: "https://dev.to/ben/what-types-of-features-typically-lead-to-lots-of-tech-debt-p46"
captured_at: "2026-11-16T01:30:08+00:00"
title: "What types of features typically lead to lots of tech debt?"
domain: "dev-to"
---

[![Ben Halpern](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F1%2Fbabb96d0-9cd2-49bc-a412-2dc4caf94c2a.png)](https://dev.to/ben)

What _types_ of features consistently lead to technical debt in your world? Like, a manager or client asks for this and you just _know_ it won't end well.

## Top comments (41)

Subscribe

Collapse Expand

[![cjbrooks12 profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F66227%2F6e81450b-870b-492c-b7ad-ae964c7c0006.jpeg)](https://dev.to/cjbrooks12)

[Casey Brooks](https://dev.to/cjbrooks12)

What's the best way to get something production-ready? Use it in production.

*   Email
    
*   Location
    
    Houston, TX
    
*   Education
    
    B.S. Computer Engineering from Texas A&M University
    
*   Work
    
    Senior Director of Engineering at Branch Ventures
    
*   Joined
    
    Apr 6, 2018
    

• [Oct 18 '18](https://dev.to/ben/what-types-of-features-typically-lead-to-lots-of-tech-debt-p46#comment-68cg)

*   [Copy link](https://dev.to/ben/what-types-of-features-typically-lead-to-lots-of-tech-debt-p46#comment-68cg)

*   [Report abuse](https://dev.to/report-abuse?url=https://dev.to/cjbrooks12/comment/68cg)

Features that are completely unlike anything you've implemented before, because a lot of infrastructure needs to get set up to support that one feature, and you may not have time to plan it all out properly.

Alternatively, features that are _nearly_ the same as an existing feature, but have a few significant differences. Either leads to lots of duplicated code, or else a bunch of hacks in the current code to make it also work for this edge case.

Collapse Expand

[![rrampage profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F35035%2Ff095885d-5235-4d65-8998-55c42b8764d4.jpg)](https://dev.to/rrampage)

One-off feature requests which are of the form **"We need this for today, nothing fancy, just a special check for X customer"**. The problems with these are:

*   **Poor planning** : These requests are a symptom of poor planning and often involve patchwork solutions to keep everything running fine (for now).
*   **Permanence** : Many requests which are a "hack" for today become accepted as part of daily flow. Even if they are stopped, **code is often added but rarely removed**. After a while, the programmer who implemented the feature would have left the team and even the people who requested the feature will not have a solid memory of the details.
*   **Prevalence** : Such special cases add up in codebase very quickly. Accepting even once sets a precedent and then the floodgates for these kinds of requests will burst open!
*   **Emergent complexity** : Such features are suggested in isolation and since it is an "easy" feature, no one pays attention to how these features interact with different parts of the system. It can lead to emergent complexity where combinations of small exceptions can lead to an unexpected behavior of the system.

IMHO, the best way to answer these kinds of requests (depending on how mature your company is) would be flat say no or ask for enough time to implement it in a sensible way.

A caveat for startups. Many startups are still experimenting with their core product when they launch. Such features are needed for fast iteration and feedback. Being ruthless in removing code for failed experiments is required to manage code base.

Collapse Expand

[![kpollich profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F32172%2Fb4320e9e-7d1b-46f8-9b7e-c6721d3854ce.jpg)](https://dev.to/kpollich)

[Kyle Pollich](https://dev.to/kpollich)

Lancaster, PA Full Stack Dev. Node, React, GraphQL.

*   Location
    
    Lancaster, PA
    
*   Education
    
    BS Computer Science - Millersville University
    
*   Work
    
    Software Engineer at Ridwell
    
*   Joined
    
    Sep 4, 2017
    

• [Oct 20 '18](https://dev.to/ben/what-types-of-features-typically-lead-to-lots-of-tech-debt-p46#comment-69fd)

*   [Copy link](https://dev.to/ben/what-types-of-features-typically-lead-to-lots-of-tech-debt-p46#comment-69fd)

*   [Report abuse](https://dev.to/report-abuse?url=https://dev.to/kpollich/comment/69fd)

+1 to "Poor Planning" here. Technical debt is, as other users have mentioned, meant to be a conscious decision. Engineers need to make constant trade offs when developing software and technical solutions. Without proper planning, it's likely that engineers don't have all the information they need to make educated decisions about trade offs, leading to poorly implemented or short sighted solutions. If you're unable to consciously understand the trade offs you're making, you'll likely wind up with unintended technical debt or an inadequate solution.

Collapse Expand

[![cjbrooks12 profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F66227%2F6e81450b-870b-492c-b7ad-ae964c7c0006.jpeg)](https://dev.to/cjbrooks12)

[Casey Brooks](https://dev.to/cjbrooks12)

What's the best way to get something production-ready? Use it in production.

*   Email
    
*   Location
    
    Houston, TX
    
*   Education
    
    B.S. Computer Engineering from Texas A&M University
    
*   Work
    
    Senior Director of Engineering at Branch Ventures
    
*   Joined
    
    Apr 6, 2018
    

• [Oct 18 '18](https://dev.to/ben/what-types-of-features-typically-lead-to-lots-of-tech-debt-p46#comment-68eb)

*   [Copy link](https://dev.to/ben/what-types-of-features-typically-lead-to-lots-of-tech-debt-p46#comment-68eb)

*   [Report abuse](https://dev.to/report-abuse?url=https://dev.to/cjbrooks12/comment/68eb)

I've never really considered it that way, but you're totally right in that tech debt is exactly that: debt. Having a credit card isn't a bad thing if you can pay it off in a timely manner, just like writing "bad code" or rushing a feature for a timeline isn't necessarily bad if you take time to pay down that debt after release. But if you have a pattern of consciously choosing to add features and never pay it back, then you start to get in trouble.

Collapse Expand

[![jfrankcarr profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F36993%2F53d1ff19-31b8-48cc-b6c4-62f4ff405fec.png)](https://dev.to/jfrankcarr)

Tightly coupling features to particular things, such as customers, vendors, products, events or even hardware.

A real world example: A manufacturing company has made 12 different product lines for about 15 years. All software gets written around this fact. Suddenly, one day, there's a urgent need to expand it to more product lines because of a big contract with a certain big retailer. That's when things start to break all over the place because everything from the database to the front end is written specifically for 12 product lines. What the company did in this situation is to setup separate databases and apps for the new product line by making copies of the existing software. But there were other things tightly coupled so that didn't work. It almost sunk the company.

Collapse Expand

[![bgadrian profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F32000%2Fa32696b2-dd6a-4c9e-a786-681a9ae6447d.jpg)](https://dev.to/bgadrian)

[Adrian B.G.](https://dev.to/bgadrian)

Striving to become a master Go/Cloud developer; Father 👨‍👧‍👦; 🤖/((Full Stack Web|Unity3D) + Developer)/g; Science supporter 👩‍🔬; https://coder.today

*   Email
    
*   Location
    
    E EU
    
*   Education
    
    Bachelor of Economic Informatics
    
*   Work
    
    Cloud Engineer at CrowdStrike
    
*   Joined
    
    Sep 1, 2017
    

• [Oct 19 '18](https://dev.to/ben/what-types-of-features-typically-lead-to-lots-of-tech-debt-p46#comment-68n2)

*   [Copy link](https://dev.to/ben/what-types-of-features-typically-lead-to-lots-of-tech-debt-p46#comment-68n2)

*   [Report abuse](https://dev.to/report-abuse?url=https://dev.to/bgadrian/comment/68n2)

Anything that contains

*   **urgency** "URGENT", "ASAP", "tomorrow"
*   **Diminutives** "just a quick small tiny bit exception", it usually means that he does not understand or explicitly hide the complexity
*   **excluding** conditions: "we do not need to worry about X" where X is stability, performance, security usually. "We will worry about it later"

Collapse Expand

[![elmuerte profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F14430%2F62d2dca3-0053-4127-9bae-03d29e4c73ab.jpeg)](https://dev.to/elmuerte)

Technical debt isn't just about bad code. It is about the price you have to pay for going back to that code to make changes.  
Bad code, and even bad architecture can have zero technical debt when it works, and does not require change.

Collapse Expand

[![kspeakman profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F15366%2Fc6550569-8654-4c9e-828b-c1dcb9c8a0df.png)](https://dev.to/kspeakman)

I can nearly guarantee a feature will be technical debt, when a user has asked for it to meet organizational requirements that have nothing to do with the application's normal usage. When I implement it, I always know it is going to be a thorn in my side. Executives and managers are always coming up with new initiatives and policies. So then the code has to be reworked for non-functional reasons. Or it might just become unused cruft which is supplanted by another new org-overhead feature. And with every core-feature change I make, I must consider the impact to the org-overhead features even though it has no importance to the core use cases.

Users tend to not be able to differentiate between what features they need to accomplish their work and what things are just organizational cruft. So they always ask for (or outright demand) features like this. Nowadays, I try to determine what use case is driving a feature request. If it is not the main purpose of the app, I look for alternative ways to help the user meet those organizational requirements without generating tech debt for me. For example "What if I give you a CSV of the data so you can play with it in Excel?" Or "How about using X product to accomplish that?" Or "Does this really need to integrate with BizTalk?"

Answers like these help the user solve their problem and also avoid writing code that will be a grief to me in the future.

Collapse Expand

[![rhymes profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F2693%2Fbfd9a4a5-92b3-4ac3-a276-3ccb68d78203.jpg)](https://dev.to/rhymes)

> I can nearly guarantee a feature will be technical debt, when a user has asked for it to meet organizational requirements that have nothing to do with the application's normal usage. When I implement it, I always know it is going to be a thorn in my side.

The magical words you hear too often in consulting are "the customer asked for this".

They make you wonder if PMs are doing their job or just saying yes to whatever the customer asks them for :D After a few "yeses" veering off the core product you tend to accumulate a lot of debt already.

Maybe PMs should be UX designers or UX designers should be the ones talking to the customers and let PMs run the day to day of the project.

Collapse Expand

[![ben profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F1%2Fbabb96d0-9cd2-49bc-a412-2dc4caf94c2a.png)](https://dev.to/ben)

A couple things that come to mind for me:

*   A/B testing. Whether additional scripts on the client, complexity on the backend or anything in between, it rarely seems to end well.
*   "Example" versions for potential customers.

Collapse Expand

[![rhymes profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F2693%2Fbfd9a4a5-92b3-4ac3-a276-3ccb68d78203.jpg)](https://dev.to/rhymes)

> "Example" versions for potential customers.

Also "prototypes" that become the final version :D

Collapse Expand

[![andrewmsboyd profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F42901%2Fdf11f089-bf1c-438a-a0c7-d9d8d1b720fb.jpeg)](https://dev.to/andrewmsboyd)

[andrewmsboyd](https://dev.to/andrewmsboyd)

Information Technology specialist, aspiring data dev, dog dad, professional mac & cheese seasoner

*   Location
    
    Austin, TX
    
*   Education
    
    Tarleton State University
    
*   Joined
    
    Nov 15, 2017
    

• [Oct 18 '18](https://dev.to/ben/what-types-of-features-typically-lead-to-lots-of-tech-debt-p46#comment-68fg)

*   [Copy link](https://dev.to/ben/what-types-of-features-typically-lead-to-lots-of-tech-debt-p46#comment-68fg)

*   [Report abuse](https://dev.to/report-abuse?url=https://dev.to/andrewmsboyd/comment/68fg)

As a super beginner dev, I'd like to know a little bit more about why A/B testing might qualify as a practice that leads to tech debt.

It seems like something that giants like Google and FB do all the time. Is A/B testing not a practice intended to _prevent_ tech debt?

Collapse Expand

[![ben profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F1%2Fbabb96d0-9cd2-49bc-a412-2dc4caf94c2a.png)](https://dev.to/ben)

A/B testing is, in my experience, usually an attempt to improve some business metric like landing page conversions and engagement etc. They're great if done right, but they inherently add a lot of complexity and coordination that can cause holes that are hard to dig out of.

Big orgs do a lot of A/B testing, but they devote the resources to making it work, and I'm sure they still have their issues. Smaller engineering orgs get in trouble trying to add split testing into an already rigorous workload.

[![picocreator profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F56734%2F7c96ac1b-1775-452b-8aa2-e49cac86d45b.jpeg)](https://dev.to/picocreator)

There is also a stats issue involved. And how many misunderstand stats.

Seen way too many startup spending way too much time trying to use A/B, as a means to try find a magical 10x conversion rate improvement through it. With sample size of under a thousand.

Over simplifying, my rule of thumb, until one reach over a million hits per month, or a team of 50, one should never consider A/B. Till then incremental improvement and feedback is good enough.

Collapse Expand

[![davepacifico profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F108678%2F43bcb8ee-bfe9-480d-bf9b-29d27775b3f9.jpeg)](https://dev.to/davepacifico)

I don't think you have to consciously decide to take on debt in code. First of all, you could just not realize you're making a bad decision. Maybe you are inexperienced. Second, and I think more importantly, you can do everything right based on the information you have at that moment and then it becomes debt later as you get more information, understand more about new use-cases, etc. This is an oldie but a goodie by Martin Fowler - [martinfowler.com/bliki/TechnicalDe...](https://martinfowler.com/bliki/TechnicalDebtQuadrant.html)

Collapse Expand

[![nestedsoftware profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F59384%2Faeea81a5-33f5-4ed8-89d9-6ec48ad4bd8e.png)](https://dev.to/nestedsoftware)

I don’t know if this helps, but I think there are three factors that can all contribute to technical debt:

*   Hastily adding features
*   Having a limited understanding of the kind of programming one is doing
*   Adding a source of complexity where it may be avoidable (e.g. A/B testing)
