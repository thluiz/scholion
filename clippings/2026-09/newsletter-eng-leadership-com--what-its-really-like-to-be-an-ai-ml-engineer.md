---
url: "https://newsletter.eng-leadership.com/p/whats-really-like-to-be-an-aiml-engineer?ref=dailydev"
captured_at: "2026-09-25T18:06:47+01:00"
title: "What’s Really Like to Be an AI/ML Engineer"
domain: "newsletter-eng-leadership-com"
---

[

![](https://substackcdn.com/image/fetch/$s_!NvQ7!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F41759ab1-ebc8-4b2c-93f9-07b929448052_1600x626.jpeg)

](https://substackcdn.com/image/fetch/$s_!NvQ7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F41759ab1-ebc8-4b2c-93f9-07b929448052_1600x626.jpeg)

This week’s newsletter is sponsored by **[Atono.](https://na2.hubs.ly/H028QxH0)**

**How we built an MCP server from scratch**

MCP Servers has quietly become _the_ thing every engineering team is adding to their roadmap. Not because it is trendy, but because it finally gives AI a safe and predictable way to work with the systems you have already built.

In Atono’s latest webinar, senior engineer Lex walks through how their team built an MCP server from scratch. He shares what the process looked like, where things got strange, and how LLMs behave once they are connected to real workflows instead of clean examples.

[

![](https://substackcdn.com/image/fetch/$s_!-geR!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbfd84a6a-85c6-4acc-a2a5-27ffb3b86f1d_1600x900.webp)

](https://na2.hubs.ly/H028PT60)

In this walkthrough, you’ll learn:

*   **How MCP gives AI a predictable way to interact with your systems** — even when your product has years of features, fixes, and tech debt baked in.
    
*   **Why we built and shipped our MCP server as a Dockerized service** — and how that choice simplified security, setup, and compatibility across tools like Zed, VS Code, and Copilot.
    
*   **What happens when different LLMs start invoking your tools** — including the unexpected behaviors, model quirks, and debugging patterns that only show up once everything is wired into real workflows.
    

Whether you manage a team or write the code, this walkthrough shows how MCP works in practice.

[Get access to the webinar](https://na2.hubs.ly/H028PT60)

Thanks to Atono for sponsoring this newsletter, let’s get back to this week’s thought!

With the increase in popularity of AI, roles such as AI Engineer and ML Engineer are becoming more and more popular.

In order to understand the roles much better, I’ve asked 3 AI/ML Engineers to share their real-world experience:

*   How does their day-to-day look like
    
*   What technologies do they work with
    
*   Specific challenges they are facing
    
*   How does the work differ from Software Engineering
    

These are the 3 engineers I had the pleasure of talking to:

*   [Shivam Anand, Staff ML Engineer at Meta](https://www.linkedin.com/in/shivamanand/)
    
*   [Alex Razvant, Senior AI Engineer at Everseen](https://www.linkedin.com/in/arazvant/)
    
*   [Bhuvaneshwaran Ponnusamy Ilanthirayan, AI Engineer & Head of AI at contexxt.ai](https://www.linkedin.com/in/buvnswrn/)
    

If you like these kinds of articles, where I talk to various engineers & engineering leaders and share their insights, you’ll love these 2 articles as well:

[

![How to Use AI to Increase Software Development Productivity](https://substackcdn.com/image/fetch/$s_!hy8U!,w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffd0a9aae-3a0f-457e-a9d0-943360d54006_800x421.jpeg)

](https://newsletter.eng-leadership.com/p/how-to-use-ai-to-increase-software)

[

![How to Use AI to Be a Great Engineering Leader](https://substackcdn.com/image/fetch/$s_!YpoR!,w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7e64e783-a55d-4b03-afe3-27ba616e8e1d_800x348.jpeg)

](https://newsletter.eng-leadership.com/p/how-to-use-ai-to-be-a-great-engineering)

Let’s start!

Shared by [Shivam Anand, Staff ML Engineer at Meta](https://www.linkedin.com/in/shivamanand/).

His work focuses on large-scale machine learning systems, with a particular emphasis on adversarial ML → building resilient systems to defend against bad actors.

Before Meta, he spent over seven years at Google, leading ML efforts in ads spam and fraud, video ranking, and search quality.

What attracted him to AI/ML was how fast the field evolves. He always loved learning, and ML is one of the few areas in engineering where the landscape can shift dramatically year to year. That constant state of reinvention is what kept him engaged.

At Meta, his day-to-day varies depending on the time of year. During planning phases, the focus is on alignment and defining technical strategy.

In execution phases, it shifts to mentoring other engineers and hands-on work → building infra, training models, iterating quickly.

[

![](https://substackcdn.com/image/fetch/$s_!E69-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9d4a503d-0edf-4d37-970c-3faf59c91ba6_1600x616.jpeg)

](https://substackcdn.com/image/fetch/$s_!E69-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9d4a503d-0edf-4d37-970c-3faf59c91ba6_1600x616.jpeg)

He uses PyTorch extensively, tightly integrated with Meta’s internal stack. A major focus area has been deploying LLAMA models to handle problems where labels are scarce and adversarial behavior is dynamic.

One of the hardest problems he tackled recently involved scaling LLMs to handle billions of unknown examples with only a handful of positive labels.

It’s an extreme version of the class imbalance problem, where success depends not just on modeling, but on optimizing data pipelines, evaluation strategies, and inference performance across infrastructure.

Compared to earlier roles in software engineering, ML introduces more uncertainty. In traditional engineering, outcomes for a given effort are often easier to estimate, even if timelines slip.

In ML, the outcome itself is often unclear until you try, especially in adversarial settings. This makes iteration velocity, measurement discipline, and expectation management all critical parts of the job.

A common misconception about AI is that it’s full of magical breakthroughs. In practice, it’s empirical, iterative, and full of hard trade-offs. Most progress comes from structured experimentation and relentless tuning, not cleverness alone.

For those looking to break into ML roles at Big Tech companies:

> Understand that interviews are highly structured. Prepare deliberately, but also develop real depth in the problem domains you’re interested in. That combination is what makes people stand out.
