---
url: "https://newsletter.techleadmentor.com/p/how-to-unlock-critical-thinking?ref=dailydev"
captured_at: "2026-09-25T18:17:14+01:00"
title: "How to Unlock Critical Thinking?"
domain: "newsletter-techleadmentor-com"
---

Ever nodded along to a proposal, only to realize later it didn't make sense? Or have you agreed to a solution that only attacked the symptoms but not the underlying problem?

Sometimes, in the moment, we fail to think critically and just agree to things that seem right superficially. I feel bad when that happens to me and worse when others find faults that I missed 😛. Jokes aside, critical thinking is a disciplined approach to reasoning that anyone can learn. It simply requires diligence and practice.

Today, I am sharing steps that help me think critically most of the time.

[

![](https://substackcdn.com/image/fetch/$s_!oCP1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2f9a071f-75af-498d-85a4-6b650aded4f4_2560x1472.png)

](https://workos.com/?utm_source=techleadmentor&utm_medium=newsletter&utm_campaign=q32024)

[WorkOS](https://workos.com/?utm_source=techleadmentor&utm_medium=newsletter&utm_campaign=q32024) is a modern identity platform for B2B SaaS. It provides flexible and easy-to-use APIs to ship user management, SSO, SCIM provisioning, and fine-grained authorization in minutes instead of months.

WorkOS powers some of the world's hottest startups, including Perplexity, Vercel, and Webflow.

[Get started today](https://workos.com/?utm_source=techleadmentor&utm_medium=newsletter&utm_campaign=q32024)

_To keep the article focused, I am sharing tips on thinking critically when a coworker shares a proposal (to add rate limiting to your service). However, the tips can also be used in other contexts._

First things first: get crystal clear on what the problem and the suggestion are.

Here's how:

*   **Grasp the elevator pitch:** What's the TL;DR version?
    
*   **Uplevel, but get specific:** Prefer using an example to validate your understanding.
    

Example:

❌ "We're adding rate limiting to protect the service."

This is too vague and doesn’t help you think critically. Let’s look at a better version:

✅ "The service gets overloaded (CPU/memory/other metrics) by a few clients, affecting others. We propose adding rate limiting to address this."

In this refined version, you know

1.  **who** is causing the issue (specific clients),
    
2.  **what** is being affected (service performance), and
    
3.  **how** the proposal aims to solve the problem (rate limiting).
    

This clarity helps you focus your critical thinking on the right aspects.

Don’t take the problem at face value, even if it comes from someone you trust. **Validate the issue** by digging deeper into the data and the backing evidence.

For example, if the proposal suggests that the service is overloaded, you should understand:

*   Is the overload system-wide or isolated?
    
*   What do the metrics say? Is there a direct relationship between the rise in traffic and the overload?
    
*   Is the overload proportional to the increase in load, or do we see a very high overload with a marginal increase in traffic?
    

Example:

The overload issue only appears with a subset of customers using a particular feature. This may suggest that the problem isn’t a general overload but a bottleneck specific to that feature. So, **optimizing the feature** might be a better solution than rate limiting.

Asking these questions helps you **distinguish between the symptoms** (overload) and the **underlying causes**.

Once you validate the problem, it’s time to quantify the **impact** by asking, "So what?" This helps you prioritize the issue and understand its business implications.

Example:

If the proposal says, “When client A overloads the service, it affects other customers,” keep digging deeper by asking, “So what?”

*   Many customers saw their requests fail. _So what_
    
*   Some key customers suffered huge revenue losses. _So what_
    
*   They will take their business elsewhere if this keeps happening. (Of course, this one was obvious 🙂)
    

By asking, "So what," you might discover subtle nuances: Some customers are affected more than others.

This helps you decide if: The problem is big enough to need the suggested solution.

Now that you understand the depth of the problem statement, it’s time to evaluate whether the proposal solves all of those problems.

Ask yourself:

*   Does this address the root cause or just the symptoms?
    
    *   For example, rate limiting isn't enough if you find inefficiencies in the service. The proposal also needs to make the service efficient.
        
*   Are there any unintended consequences?
    
    *   For example, if the proposal builds a simple global throttling, it could result in starving high-priority requests from customers that send less traffic.
        
*   Is this a long-term solution or a quick fix?
    
    *   For example, maybe the proposal intends to add rate limiting as a short-term fix, and in the long term, it also makes sense to partition the service for better isolation.
        

This step is about **vetting the proposal’s effectiveness.** You ensure it’s not just a band-aid but a comprehensive solution that addresses the immediate problem and potential long-term implications.

Even if the proposal looks solid, it’s crucial to **challenge your thinking and assumptions**. Playing devil’s advocate pushes you to identify risks, weaknesses, and potential failures, ensuring that no blind spots remain.

Challenge your thinking even when the proposal looks sane. Think about:

*   **What could go wrong?** Consider scenarios where this proposal might fail. Are there edge cases that could break the solution?
    
*   **What if this solution backfires?** Think about worst-case scenarios. Could the fix introduce new problems, like performance bottlenecks or customer dissatisfaction?
    
*   **Are there hidden costs?** Could this proposal introduce technical debt, maintenance overhead, or unforeseen negative impacts on users?
    
*   **Am I being swayed by biases?** Are you too trusting of this proposal because of the presenter’s credibility, or does it align too easily with your existing beliefs?
    

For example, if you’ve advocated rate limiting for a while, you might overlook other solutions, such as optimizing the service or partitioning traffic.

The goal is to **test your reasoning** and uncover any blind spots or biases. By challenging the proposal from multiple angles, you can ensure you’ve considered all potential risks and haven’t overlooked any critical details.

[

![](https://substackcdn.com/image/fetch/$s_!t7ex!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffebf63b5-b800-40ff-a9cb-115d1c799e81_3000x3000.jpeg)

](https://substackcdn.com/image/fetch/$s_!t7ex!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffebf63b5-b800-40ff-a9cb-115d1c799e81_3000x3000.jpeg)

Think of critical thinking as strength training. Just as you don’t build muscle overnight, sharpening your critical thinking takes time and consistent effort. The more you use this framework, the stronger your decision-making skills become. So keep practicing.

You will miss things along the way, and that’s okay. The key is to identify what you missed using the steps above and improve next time.

_If you enjoyed this article, then hit the ❤️ button. It helps!_

_If you think someone else will benefit from this, then make sure to 🔁 share this post._

[Share](https://newsletter.techleadmentor.com/p/how-to-unlock-critical-thinking?utm_source=substack&utm_medium=email&utm_content=share&action=share)
