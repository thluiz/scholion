---
url: "https://www.infoq.com/articles/technical-debt-your-friend/?ref=dailydev"
captured_at: "2026-09-25T22:29:59+01:00"
title: "How to Make Technical Debt Your Friend"
domain: "infoq-com"
---

### Key Takeaways

*   Incurring Technical Debt (TD) is a way to learn things, and to avoid over-investing in solutions to problems you may not yet fully understand. 
*   The idea that releases have to be perfect gets in the way of running experiments. TD reduces the cost of learning and the time it takes to get feedback. 
*   TD represents a deviation of your implemented solution from your ideal solution, but that ideal may not turn out to be correct. In other words, what you think is TD may not actually be TD.
*   Using a Minimum Viable Architecture (MVA) approach helps teams decide when and if they need to address specific TD items by considering whether failing to address them will impair the success of the MVP/MVA.
*   TD is, ultimately, a good thing because it reduces the likelihood that a team will over-invest in architecture.   
     

[Technical debt](https://www.infoq.com/articles/technical-debt-tells-you/) (TD) is a popular metaphor for communicating the long-term implications of architectural decisions and trade-offs to stakeholders. It is usually regarded as a bad thing, a liability that must be repaid. That’s the way that we used to look at it: that rising technical debt represents, at some level, a failure of a team to effectively manage their architectural trade-offs.

But in the course of further discussions, we started to ask ourselves questions about whether our view of TD was correct. What if it, like its real-world counterpart, debt, is an important and essential part of building something? And what if, at least sometimes, it really isn’t like debt at all, in that it may never need to be repaid? And if it is repaid, how and when should a team trade-off TD reduction against new development work?

By exploring these questions, we have come to look at TD in a different way by exploiting the feedback mechanism of the [Minimum Viable Architecture (MVA)](https://www.infoq.com/articles/minimum-viable-architecture/) approach. Upon further exploration, we have concluded that the TD metaphor is misleading because much of the so-called debt never needs to be, and in fact isn’t, repaid. Working on TD that doesn’t ever need to be repaid is detrimental to the success of the product; the critical difficulty is deciding what _really_ needs to be fixed and what perceived shortcomings can be lived with.  

#### Related Sponsors

*   ##### [Understanding Postgres Performance Limits for Analytics on Live Data](https://www.infoq.com/vendorcontent/show.action?vcr=a7d3e79b-c1f0-48c9-a1ef-84a625436518&primaryTopicId=2498&vcrPlace=EMBEDDED&pageType=ARTICLE_PAGE&vcrReferrer=https%3A%2F%2Fwww.infoq.com%2Farticles%2Ftechnical-debt-your-friend%2F%3Fref%3Ddailydev&ha=bW91c2Vtb3Zl)
    
*   ##### [AI-Native Software Delivery - Download the eBook (By O'Reilly)](https://www.infoq.com/vendorcontent/show.action?vcr=9831f722-2945-4987-98d0-c1c46b32e5ef&primaryTopicId=2498&vcrPlace=EMBEDDED&pageType=ARTICLE_PAGE&vcrReferrer=https%3A%2F%2Fwww.infoq.com%2Farticles%2Ftechnical-debt-your-friend%2F%3Fref%3Ddailydev&ha=bW91c2Vtb3Zl)
    
*   ##### [AI Agents in Production: What It Takes to Move Beyond the Demo](https://www.infoq.com/vendorcontent/show.action?vcr=35eee43a-8d40-4e5d-940d-4da636ae3b65&primaryTopicId=2498&vcrPlace=EMBEDDED&pageType=ARTICLE_PAGE&vcrReferrer=https%3A%2F%2Fwww.infoq.com%2Farticles%2Ftechnical-debt-your-friend%2F%3Fref%3Ddailydev&ha=bW91c2Vtb3Zl)
    
*   ##### [AI Agent Swarm Patterns (InfoQ Webinar) - Watch Now On-Demand](https://www.infoq.com/vendorcontent/show.action?vcr=b04e8a98-3462-46e7-bb9d-c621b641e63c&primaryTopicId=2498&vcrPlace=EMBEDDED&pageType=ARTICLE_PAGE&vcrReferrer=https%3A%2F%2Fwww.infoq.com%2Farticles%2Ftechnical-debt-your-friend%2F%3Fref%3Ddailydev&ha=bW91c2Vtb3Zl)
    
*   ##### [\[Webinar\] Creating Certainty in the Age of Agentic AI. Watch On-Demand.](https://www.infoq.com/vendorcontent/show.action?vcr=531d8edd-4f74-486b-aaca-10058c609c1c&primaryTopicId=2498&vcrPlace=EMBEDDED&pageType=ARTICLE_PAGE&vcrReferrer=https%3A%2F%2Fwww.infoq.com%2Farticles%2Ftechnical-debt-your-friend%2F%3Fref%3Ddailydev&ha=bW91c2Vtb3Zl)
    

In the MVA approach, each release is a Minimum Viable Product (MVP) that tests the theories and assumptions that a team (or an organization) has about what customers find valuable. Each MVP has an associated MVA, which is the minimum set of architectural decisions that the team must make to release the MVP. These decisions reflect the _current_ needs of the MVP, but do not invest in possible future MVP scenarios that may never occur if the MVP is not valuable.

In this context, TD represents a _hypothetical_ shortcoming of the architecture if the MVP is wildly successful - but only if the MVP is successful. As a result, the TD that the team thinks it has incurred may or may not be real. If the MVP is not successful, it’s a good thing that the team did not resolve their perceived TD, because their real solution may go in a significantly different direction or, in some cases, the product itself may be canceled. From this perspective, TD is a way to hedge against the possibility that the MVP may not be valuable, and this can be usefully exploited if the team knows how to use it. 

## Without technical debt, nothing would get built

TD has analogues in the world of physical architecture. [Fallingwater](https://fallingwater.org/), Frank Lloyd Wright’s masterwork in western Pennsylvania, illustrates this point. 

![](https://imgopt.infoq.com/fit-in/3000x4000/filters:quality\(85\)/filters:no_upscale\(\)/articles/technical-debt-your-friend/en/resources/5picture1-1725017131650.jpg)

**Source: [Fallingwater - Wikipedia](https://en.wikipedia.org/wiki/Fallingwater)**

Fallingwater, even nearly 90 years after it was built, is still a bold and breathtaking design that cantilevers above the Bear Run creek. These cantilevers were controversial at the time of their construction because they used no reinforcing steel beams. Wright specifically ignored the advice of structural engineers at the time, insisting that concrete reinforced with steel reinforcing rods would be sufficient. 

But even from the beginning, the terraces that define the lines of Fallingwater began to sag, and eventually, circa 2000, had to be supported with steel cables. In software terms, we would say that the original construction of Fallingwater was deficient and incurred technical debt that eventually had to be repaid.  But was this a bad thing?

Fallingwater, like most Wright projects, was horribly over budget from the start. Edgar Kaufmann Sr., a Pittsburgh retail magnate and the client, originally wanted a simple weekend retreat on land he owned in southwestern Pennsylvania. Wright sold him on a grander design by saying that it could be built "relatively" inexpensively. The original estimate for the house was $35,000, but the final cost was $155,000, which is about $3.4 million in 2023 when adjusted for inflation. Considering its renown, that looks like a bargain today, but it was a constant source of friction between Wright and Kaufmann Sr.

Had Wright put more steel into the design, and reduced the size of the dramatic cantilevers with more conventional supports, the cost would have gone up and the dramatic effect would have been diminished, so much so that the design might not have been built. And, perhaps, to the surprise of structural engineers at the time, the original design survived until the early 2000s before it required remediation.

Wright and Kaufmann Sr. were convinced that Fallingwater would receive universal acclaim when it was being built. Software products are different - each release is a "minimum viable product" (MVP) that tests the value of the ideas behind the release. In the course of building each MVP, the development team creates a "[minimum viable architecture" (MVA)](https://www.protecto.ai/blog/what-is-minimum-viable-architecture-why-is-it-important) that provides just enough architecture to support the MVP if it is successful. 

Like Fallingwater, over-investing in an MVA can kill an MVP, making it too late to be useful, or too expensive to be affordable, before the development team even knows whether the MVP is valuable. Yes, for example, the product may not scale, but that’s only a problem if the MVP is successful. The MVA just needs to be "good enough" to achieve the goals of the MVP; should the MVP unexpectedly be more successful than anticipated, the development team may have more time and money to deal with this "opportunity".

## Incurring Technical Debt is a risk-management trade-off 

Technical debt results from decisions that trade-off meeting short-term delivery goals against long-term viability and resiliency goals. It results from a necessary expediency of software development that recognizes "sure, this isn’t perfect and it may fail in the future, but if we don’t deliver something now we’re going to fail right now".

An effective MVA _always_ incurs technical debt because the MVP and its associated MVA are not yet proven. The biggest risk teams face is not building an unsustainable solution, but building a robust solution that no one wants. Using an MVP to test the viability of the solution helps to mitigate this risk, and incurring technical debt in the MVA helps to reduce overinvestment in a solution to a problem that people don’t have.

Viewed in this way, incurring TD is a way to learn at minimal cost. It is also not so much debt as it is a contingent liability: something that you may have to repay. But just as the success of the MVP is not guaranteed, the MVA supporting the MVP might be sufficient, or it may not. Either way, releasing the MVP/MVA and measuring the result provides information that better informs future decisions. 

## Technical debt can be an illusion

When a team identifies that they are incurring technical debt, they are basing that assessment on their theoretical ideal for the architecture of the system, but that ideal is just their belief based on assumptions that the system will be successful. The MVP _may_ be successful, but in most cases its success is only partial - that is the whole point of releasing MVPs: to learn things that can be understood in no other way. 

As a result, assumptions about the MVA that the team needs to build also tend to be at least partially wrong. The team may think that they need to scale to a large number of users or support large volumes of data, but if the MVP is not overwhelmingly appealing to customers, these needs may be a long way off, if they are needed at all. For example, the team may decide to use synchronous communications between components to rapidly deliver an MVP, knowing that an asynchronous model would offer better scalability. However, the switch between synchronous and asynchronous models may never be necessary since scalability may not turn out to be an issue. 

In a previous [article](https://www.infoq.com/articles/trade-offs-minimizing-unhappiness/), we discussed how teams deal with trade-offs in an MVA approach. Often trade-offs frustrate architects because they introduce solutions that are less than ideal, but in fact the "ideal" may be wrong. The only way to know if the "ideal" is correct is to experiment. 

Is TD just a decision you feel bad about? Maybe. Calling it "debt" makes you feel better because you convince yourself that someone will fix it in the future. But maybe it doesn’t need to be fixed. In fact, as noted above, not all TD needs to be dealt with; some of the trade-off decisions will turn out to be more than adequate to solve the problem at hand. The idea that TD has to be repaid, as if it were a real debt, leads teams to overinvest in solutions they don’t really need, or at the very least, to feel bad about not achieving their "ideal".

## Whether TD needs to be tackled depends upon the MVP & MVA

To reduce the risk of overinvesting in architecture, teams should ask themselves what is the minimum set of architectural decisions they need to resolve in order to support the MVP if it is successful; this is what we call the _minimum viable architecture (MVA)_. "Supporting" the MVP means delivering the desired customer outcomes of the release, including the desired quality attributes of the user’s experience.

Whether, and which, TD items need to be resolved is part of these MVA decisions. Reducing TD is not a separate activity that teams undertake, and this is where many teams struggle: they don’t have time to work on reducing TD and so TD just accumulates. Even, on rare occasions, when they can work on TD, they struggle to decide what to work on. Making TD reduction decisions just part of the normal MVA decision process makes the choices more clear.

Releasing MVPs (and their associated MVAs) helps teams to learn things that better inform their understanding of both the solution that they need to build and the QARs that they need to satisfy. As a result, some of their TD items become irrelevant as they learn more about what their customers really need and what they need to do to deliver it to them. As part of their backlog refinement efforts, teams should look at the TD items they have identified to clear-out items that are no longer relevant. 

In addition, TD work often needs to be justified, or at least explained, to stakeholders who are interested in what the team is working on, and why. Discussions with stakeholders are essential to:

*   Come to an agreement that there are questions that the organization must answer about value that only releasing a part of the product can answer. This is the heart of the MVP approach. If stakeholders think they have all the answers they will never embrace the incremental release strategy at the heart of the MVP approach.
*   Come to a common understanding of the value being tested in the MVP, so that everyone agrees on the goals of the MVP. Everyone needs to know why certain capabilities are important so the team knows what they _don’t_ need to work on.
*   Come to a common understanding of the QARs that must be satisfied for the MVP to meet the targeted needs of the customer. This helps the team decide which, if any, TD items need to be resolved to meet the goals of the MVP.
*   And finally, agree with stakeholders that some TD is essential to releasing the MVP/MVA; that the MVP/MVA only needs to be "good enough" to get feedback and satisfy the immediate needs of a small target set of potential customers. This means that some TD items will be ignored, for now, to achieve the goals of the MVP.

## Conclusion

Almost every architectural decision involves making trade-offs. When teams believe that a trade-off is unsatisfactory and needs to be revisited later, they assume that they are increasing TD, but the trade-off and related TD are necessary to releasing an MVP.  By releasing the MVP, they may learn that the trade-off is good enough and the associated TD never needs to be repaid. In that case the TD was not "real" and was, in fact, necessary to move the product ahead.

Each MVP/MVA only needs to be good enough to validate the solution and meet the immediate needs of users. It doesn’t need to be infinitely flexible or scalable; those are good problems to have, and teams can address them when needed. A greater problem is for them to spend lots of time and effort building a perfect solution that no one wants. TD helps teams avoid that by letting them run valuable experiments sooner than they would do otherwise.

As a result, not all TD that the team thinks they have is really "debt"; it is more like a contingent liability that may need to be repaid, or it may not. Some TD that teams identify will turn out to be unnecessary to resolve because MVPs reveal changing customer needs that don’t require the TD to be "repaid"–Premature "repayment" would have been a waste. The MVPs may reveal other issues, however, but these are just "defects" that need to be considered along with other work when planning the next MVP.

As we stated in a recent article, "to architect is to be a frustrated perfectionist" and not being able to repay known technical debt in the foreseeable future adds to the frustration. However, to architect is also to recognize that technical debt may be a helpful ally in delivering a quality product that meets or exceeds expectations.  
 

## About the Authors

[![Pierre Pureur](https://cdn.infoq.com/statics_s2_20260925154625/images/profiles/22c27753414b3827cb473ede92e13489.jpeg)](https://www.infoq.com/profile/Pierre-Pureur/)

#### **Pierre Pureur**

Pierre Pureur is an experienced software architect, with extensive innovation and application development background, vast exposure to the financial services industry, broad consulting experience and comprehensive technology infrastructure knowledge. His past roles include serving as Chief Enterprise Architect for a major financial services company, leading large architecture teams, managing large-scale concurrent application development projects and directing innovation initiatives, as well as developing strategies and business plans. He is coauthor of the books "Continuous Architecture in Practice: Scalable Software Architecture in the Age of Agility and DevOps"(2021) and "Continuous Architecture: Sustainable Architecture in an Agile and Cloud-Centric World" (2015) and has published many articles and presented at multiple software architecture conferences on this topic. 

Show moreShow less

[![Kurt Bittner](https://cdn.infoq.com/statics_s2_20260925154625/images/profiles/3789fc0e548a79744225f15083ab938c.jpg)](https://www.infoq.com/profile/Kurt-Bittner/)

#### **Kurt Bittner**

Kurt Bittner has more than 30 years of experience delivering working software in short, feedback-driven cycles. He has helped a wide variety of organizations adopt agile software delivery practices, including large banking, insurance, manufacturing, and retail organizations, as well as large government agencies. He has worked for or with large software delivery organizations including Oracle, HP, IBM, and Microsoft. He is also former technology industry analyst with Forrester Research, and has written widely on topics related to agile teaming and leadership.

Show moreShow less
