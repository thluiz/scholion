---
url: "https://dev.to/steliosvoskos/the-obligation-of-a-software-developer"
captured_at: "2026-09-25T01:05:25+01:00"
title: "The obligation of a software developer"
domain: "dev-to"
---

[![SteliosVoskos](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3185%2FPhoto_on_05-03-2017_at_20.58.jpg)](https://dev.to/steliosvoskos)

We live in a world that changes everyday and software is one of the biggest part of that change. People interact with software in many ways, such as their laptops, their smart phones, their cars and they expect to get the most out of the devices they use.

Behind the software applications are the teams who build the products and the factors that determine the success or failure of the software are strongly connected with the cohesiveness of the team, the amount of effort the team has put during the delivery and the behaviour of each individual. In this article we will explore some of the ethics that a developer and a team should have during and after the delivery of a software product.

1.  **Find the best solution and not a solution**  
    As mentioned in the introduction, a significant factor that will determine the long-term success of a product, is the quality of the solution we are offering to the client. There is no reason to deliver a solution that is going to slow-down the product, make its state unpredictable or make the UI looking different from the one that your UX designers proposed. And this is simply because the quality of the solution and amount of effort, show the respective respect to the client and/or the future user. The high code quality in the codebase will also make the experience of the current and the future developers significantly better.
    
2.  **Do not write code you do not trust**  
    A codebase without unit tests or any kind of tests, contains code that cannot be trusted. And why should you deliver a website, a SPA or an app to a user with code you don't trust? The answer is that you should not. The tests are the first line of defense in a codebase, they are the part of the code that will give you the heads-up when something goes wrong and they are going to catch the bug faster than your `console.log('Hello')`, they are the part of the codebase that will explain to the software developer or the QA tester the purpose that your code serves. Also remember that the tests are the units that prevent you from writing unnecessary code. So always aim for the highest possible amount of code coverage for your benefit and the benefit of the future user. A codebase should include 15% UI tests, 30% integration tests and 55% unit tests. The unit tests should always be close to 100% code coverage and they should cover as many cases as possible.
    
3.  **Learn how to say No. But also learn to negotiate.**  
    I am glad that at the early stages of my career some Scrum Masters and Solution Architects taught me the value of saying No, but also how to negotiate to make the “No” a compromisation that works as a solution for the benefit of both sides. They taught me that if I don't raise my voice and say that “this, this and this can't be done now or in that way”, then I will end-up with unnecessary amount of pressure on me. And it's true. Unrealistic deadlines, unrealistic requirements and unrealistic delivery will be part of the discussions during development, but you have to find the correct arguments to defend the fact that some things cannot be done by a certain deadline or in the way they are proposed. It is the worst form of unprofessionalism to make a commitment that you can't keep, or make false delivery just to think that you keep your line manager happy in that way. The opposite may happen.
    
4.  **Respect your team members**  
    Your team members are the people you meet every day for at least 8 hours per day, the people that you have long meetings to find the appropriate technical and non-technical solutions, the people you speak with every day. There is no reason to create tension, and change arguments that may harm the cohesiveness and harmony of your team. And if that happens, it is your obligation to discuss the issue with your team member/s and resolve it as soon as possible. Also in a team there should not be a person who should think that is doing better job than the others, or that the depth of knowledge gives them an advantage to behave in an inappropriate way. If someone encounters an issue, then there should be the appropriate support and mentoring and help that team members or team members get back on track again. If there is success, then your team celebrates as a collective. If the product fails, then the team fails as a collective. At the end of the day, what's the meaning of a team that is just a disarrayed set of individuals?
    
5.  **Enhance an implementation. Do not criticise it.**  
    I am at the second year of my career and code review is the part of the development that I always consider an enjoyable task, because it's a good chance to sit down with your colleague and think as a collective how to enhance the implementation that has just been committed in the codebase. It's an exercise that should be happening in all development teams, as the developers are the people who should spot a mistake in codebase in the first place and improve an implementation to make it faster, better and more generic. The criticism and the advice should always be constructive, it should include the “why” your suggested implementation is better than the existing one and your advice should include examples from previous implementations. However, any kind of advice or suggestion should never be said in a judgemental and tough way, as the code review is a team exercise and not a chance to judge your colleagues just because they have done a coding mistake.
    

Mentoring is also part of our job and it is always required to help others improve and bring them to the level of the rest of the team. As Eric Elliott says in his article “The Essential Guide to Building Balanced Development Teams”:

_In a mentorship culture with lots of pairing and code reviews, even novice developers quickly become great contributors._

There is nothing better and greater than mentoring Juniors and see them becoming great developers just because your advice had an invaluable impact on them.

Great software is built by great teams, where the culture within the team is such that allows them to outwork the most difficult challenges. It is also the obligation of each individual to have the right mindset when developing a feature in order to deliver the code in the appropriate quality level.
