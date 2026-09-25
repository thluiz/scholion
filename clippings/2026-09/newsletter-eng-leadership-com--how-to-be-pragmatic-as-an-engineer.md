---
url: "https://newsletter.eng-leadership.com/p/how-to-be-pragmatic-as-an-engineer?ref=dailydev"
captured_at: "2026-09-25T18:04:10+01:00"
title: "How to Be Pragmatic as an Engineer"
domain: "newsletter-eng-leadership-com"
---

[

![](https://substackcdn.com/image/fetch/$s_!5VXq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F95b8eac4-caf2-47d4-8f71-025ff7214d69_2000x788.jpeg)

](https://substackcdn.com/image/fetch/$s_!5VXq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F95b8eac4-caf2-47d4-8f71-025ff7214d69_2000x788.jpeg)

Pragmatism is one of the most important concepts in Software Engineering. There are endless variables and trade-offs we need to consider when building Software. And a lot of them are people-focused.

And pragmatism is just going to be more and more important as time goes on. The reason?

AI can just predict the next best token, but what is missing is the touch of real-world experience and the feel for what may be the best decision in a certain moment, based on many different signals.

In this article, we’re going to go through how to become pragmatic as an engineer. It’s a must-read article as pragmatism plays a big part in [future-proofing your career as an engineer](https://newsletter.eng-leadership.com/p/future-proof-your-career-as-an-engineer?utm_source=publication-search).

This is an article for paid subscribers, and here is the full index:

\- 1. What Does it Actually Mean to Be Pragmatic  
\- A Real-World Example From My Experience  
\- 2. Core Pragmatic Principles to Always Keep in Mind  
\- Build the Right Things First and Only Second Build Things Right  
\- Prioritize Simple Solutions Over Complex Ones  
\- Always Think in Trade-offs  
\- Design for Change but Don’t Optimize Too Early  
\- Use Proven Tech Over Shiny New Tech  
\- 3. My Top Tips for Becoming Pragmatic as an Engineer  
\- Ask Better Questions at the Start of Every Project  
🔒 🎁 Notion template: List of questions to ask before making a technical decision  
🔒 Get Used to Building Proof of Concepts and Prototypes  
🔒 Always Look to Reduce Scope Without Reducing Value  
🔒 Get Used to Building Proof of Concepts and Prototypes  
🔒 Learn to Deliver Iteratively  
🔒 Focus on Good Enough Solutions and Avoid Perfectionism  
🔒 Last words

For more highly relevant skills on how to be a great engineer, I highly recommend reading these articles as well:

[

![How to Develop a Senior Mindset](https://substackcdn.com/image/fetch/$s_!1Lyy!,w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5857788e-7697-4767-9342-71346afcc731_800x400.jpeg)

](https://newsletter.eng-leadership.com/p/how-to-develop-a-senior-mindset)

[

![How to Be a Proactive Engineer](https://substackcdn.com/image/fetch/$s_!84AY!,w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F17f5d7de-0448-4469-9b68-bb3b89c9ac55_800x465.jpeg)

](https://newsletter.eng-leadership.com/p/how-to-be-a-proactive-engineer)

[

![How to Be a Reliable Engineer](https://substackcdn.com/image/fetch/$s_!5qLe!,w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F07d45f46-cd5d-40b3-9942-8563e1fda1a5_800x389.jpeg)

](https://newsletter.eng-leadership.com/p/how-to-be-a-reliable-engineer)

[

![How to Become a Resourceful Engineer](https://substackcdn.com/image/fetch/$s_!_xLS!,w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F02bb3867-e88f-47d2-98b7-cf0784a55e4c_2000x857.jpeg)

](https://newsletter.eng-leadership.com/p/how-to-become-a-resourceful-engineer)

Let’s start!

There are many ways we can define what pragmatic means, and I’ll share what it means for me:

> Being pragmatic as an engineer means focusing on what actually works in the specific case, not just what is theoretically correct.
> 
> An engineer who is pragmatic finds the best solution possible within the constraints of the real world, not the ideal world.

There are often many different solutions to every engineering problem, which can be theoretically correct solutions. But in reality, they don’t work because of a set of specific constraints.

I like to look at pragmatism from this perspective → Engineering is not performed in a vacuum. Real production software needs to live under:

*   a specific budget,
    
*   change of requirements, focus, and vision,
    
*   specific knowledge and expertise from the team,
    
*   legacy code,
    
*   hardware constraints,
    
*   people-related factors,
    
*   regulatory frameworks,
    
*   time pressure, and many more.
    

Pragmatism ensures that we build useful, reliable, and achievable solutions, which are aligned with the constraints mentioned above.

Now, let me share an example from my experience, where I made a mistake of not being pragmatic, but blindly building a solution that was theoretically correct.

This was some time ago, back when I was a Senior Software Engineer.

Together with the rest of the engineering team, we were building an application using Angular on the frontend and ASP.NET CORE on the backend. We were building a new feature → it was an image upload functionality and then the image viewer UI.

I remember how excited I was to build that specific functionality, as it included a lot of interesting features like users are able to resize and crop the images, optimization of the size of the images, and also setting many metadata for the specific image.

We spent a lot of time and effort on it, and I was personally very proud of it.

But then, what happened in reality when the users actually started using it, they were already used to cropping the images themselves and uploading them, so they never really used the image cropper functionality, resizer, and so on.

It was a technically correct solution that worked amazingly well, but pragmatically → it was a bad call.

The best and most pragmatic decision would be to ask ourselves:

> What would the simplest solution that we can deliver be? And deliver exactly that, and only after, try to optimize it further if needed.

Too often, we try to optimize prematurely and are excited about building that “complex solution”, but in reality, it’s not even needed, and we are wasting both time and effort.

Now, let’s dive into the core pragmatic principles I like to follow.

[

![](https://substackcdn.com/image/fetch/$s_!NlLF!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6d348d3d-6320-4903-86c8-27593f1da6e3_800x420.png)

](https://substackcdn.com/image/fetch/$s_!NlLF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6d348d3d-6320-4903-86c8-27593f1da6e3_800x420.png)

This is crucial, and the example from my experience, which I mentioned above, is completely aligned with it.

> You can build the best technically possible solution, but if the users don’t need it, it won’t be perceived that way.

So, that’s why it’s crucial to ruthlessly prioritize what to focus on and only after look to optimize it.

Read more in this article:

[

![A good engineer thinks like a product manager](https://substackcdn.com/image/fetch/$s_!IJB_!,w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4bd5568e-11cd-409c-97ef-a0e016ca2f79_800x500.jpeg)

](https://newsletter.eng-leadership.com/p/a-good-engineer-thinks-like-a-product)

> The more complex a solution is, the more costly it is for the business.

This is really important to understand. With every line of code we create, someone needs to maintain it, and the more complex the code is, the harder it is going to be for people to understand it.

[

![](https://substackcdn.com/image/fetch/$s_!6dte!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0222e5fd-36fd-49ab-a1d2-c7f60ad4998b_800x400.png)

](https://substackcdn.com/image/fetch/$s_!6dte!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0222e5fd-36fd-49ab-a1d2-c7f60ad4998b_800x400.png)

Therefore, it will cost more to the business to ensure that it works correctly or to add additional functionalities.

I have made many mistakes in my career, thinking that complexity is a good thing.

I did it both as an engineer and a manager as well, but now simplifying is my personal philosophy. I strongly believe in it not only professionally, but also personally.

Anything I put my mind into, I ask myself:

> What would be the simplest solution for this?

Read more in this article:

[

![Simple code is the best code](https://substackcdn.com/image/fetch/$s_!BrHy!,w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc2608233-a5d3-4cd3-b325-4d6a51492e4c_800x450.jpeg)

](https://newsletter.eng-leadership.com/p/simple-code-is-the-best-code)

> There is no right or wrong decision in engineering → every decision is a trade-off. The same decision may work in one case, but it may not work in another case.

This is really important to realize. And that is a foundation for how you should approach everything in engineering.

Building a microservice architecture makes sense in some cases, especially as the load may be getting too big to handle and teams can’t really move because of too many cross-team dependencies.

But the majority of the time, a simple monolith would do the trick, especially if there are not a lot of daily active users (DAU) and we have a small team.

And the same goes for any requirements or requests to build something.

> Everything can be built, but that doesn’t mean that it actually should be built.

So, instead of saying, this is not possible, rather give a quick estimate and define the pros and cons that come with that specific request. That’s also how all business-oriented people think, and they will resonate much better with you if you do that.

You’ve probably heard about this saying:

> “Premature optimization is the root of all evil.”  
> — Donald Knuth

And it’s very true. You can see where I made this exact mistake in the example from my experience above.

I tried to optimize the functionality too soon, instead of waiting for when it’s actually needed.

There’s no coincidence that 2 of the favorite principles I like to always follow and what I suggest to engineering teams are:

*   KISS → Keep it simple, stupid.
    
*   YAGNI → You aren’t gonna need it.
    

Both principles have saved countless years of development time for my teams that I have managed or been a part of.

So, my main advice here is to have in mind different cases and scenarios that may happen in the future, and design your system in a way that you can easily add or adjust if needed.

But that doesn’t mean you should also support the future cases now. Keep it simple, and be prepared if optimization is needed.

One of the main principles I like to follow is to:

> Use boring tech to build great products.

Be focused on building the best product possible and delighting the users, and not be focused on using shiny new tech, just because you want to learn it or “that’s what everyone is using and experimenting with”.

There are definitely use cases where using a shiny new technology or a tool makes sense, but again, you want to think in terms of trade-offs.

Boring tech is proven and it works, so you don’t need to focus on unpredictable problems that in most new tools come up regularly.

You can put your full focus on building the best product for the users. And everyone who has tried building and selling their own product knows that the hardest part of a product is getting paying users. Building is the fun part.

So, you want to focus your attention on the RIGHT things. That’s what pragmatic-minded engineers focus on.

Now that you understand the core principles regarding pragmatism, let me share my top tips on becoming pragmatic as an engineer next.

Many things make you pragmatic as an engineer, and I’ll be sharing the ones I believe are the most important.

Let’s start with the first one.

The first one is crucial, and just asking good questions before even starting building things and writing your first line of code can save you so much time and also headaches.

How many times has it happened that you built something, but it actually turned out that you built something that wasn’t expected?

Well, I definitely did that a lot of times.

The thing is that you can quickly find out if you just ask a few questions beforehand. To help you with this, here are the list of questions.

**Notion template: List of questions to ask before making a technical decision**

Use this list of 35+ product + business-oriented and technical questions when making your next decision. This will help you to make an informed decision and build the RIGHT things.

[

![](https://substackcdn.com/image/fetch/$s_!e0y-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff0c15c9c-6086-4352-bb9e-c7b57c5505a0_1280x720.jpeg)

](https://newsletter.eng-leadership.com/p/100-discount-code-for-products)

You can get the template here: [🎁 Products for paid subscribers](https://newsletter.eng-leadership.com/p/100-discount-code-for-products).
