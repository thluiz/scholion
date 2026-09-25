---
url: "https://strategizeyourcareer.com/p/how-the-best-software-engineers-write?ref=dailydev"
captured_at: "2026-09-25T21:03:03+01:00"
title: "How the best software engineers write technical designs (the blueprint for consistent results)"
domain: "strategizeyourcareer-com"
---

Get the free AI Agent Building Blocks ebook when you subscribe:

[

![](https://substackcdn.com/image/fetch/$s_!kwYe!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F969930d1-7a41-45f1-921a-57cf9e34cc44_1080x1350.png)

](https://substackcdn.com/image/fetch/$s_!kwYe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F969930d1-7a41-45f1-921a-57cf9e34cc44_1080x1350.png)

How do you consistently operate at your highest level as a software engineer?

We all have good and bad days, and it’s important to remember that there's more to life than work. Yet, as engineers, we strive to perform with the precision and consistency of professional athletes.

The key to achieving this?

Developing systems and processes that drive efficiency and excellence. At the core of these systems is one fundamental process: **designing good software**.

Why? Because every decision you make after a solid design will be more impactful than those made following a poor one.

In today’s article, we’ll break down the technical design process. By the end, you’ll not only understand the value of a robust software design but also have a downloadable template for your own designs.

> “Winners and losers have the same goals. You do not rise to the level of your goals. You fall to the level of your systems - James Clear in [Atomic Habits](https://amzn.to/4eRIc3X)”

[

![](https://substackcdn.com/image/fetch/$s_!QPPC!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd9548e1d-58a0-4e7d-9265-85e0f4957630_3876x2444.jpeg)

](https://substackcdn.com/image/fetch/$s_!QPPC!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd9548e1d-58a0-4e7d-9265-85e0f4957630_3876x2444.jpeg)

1.  Why and when to write a technical design
    
2.  Sections to include in your design:
    
    [
    
    ![](https://substackcdn.com/image/fetch/$s_!6myj!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9ff3e1f9-0794-49c5-b034-0b96c1e1833f_387x590.jpeg)
    
    ](https://substackcdn.com/image/fetch/$s_!6myj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9ff3e1f9-0794-49c5-b034-0b96c1e1833f_387x590.jpeg)
    
3.  What to include in each section
    

From a project perspective, writing a technical design is inefficient. You are dedicating a single person to the project – a bottleneck.

But it’s worth down the line.

It reduces ambiguity, aligns the team, and identifies workstreams to parallelize.

This process is not only valuable at the beginning of the project. Once completed, you’ll still find value in having documented your decisions.

Even for small functionalities, create a one-pager outlining the proposal and workstreams

History of revisions, review panel for each revision, approvals from different interested parties.

Get the status of the document first thing.

Here summarize the existing system. What it does, what needs covers.

Expose the problem driving this change and explain why it’s important and why now is the right moment to do it

List teams interested in this project and why they care about it. include both clients and dependencies

> Example:
> 
> *   **Infra Team:** Will this design affect the main Ring AWS account?
>     
> *   **Foo Team:** Foo will need to call Service in order to <>.
>     
> *   **Bar Team:** Bar showed interested in <>, they want to consume the data in Service.
>     

*   **Functional requirements:** What the system must do. Include here UI mocks if applicable
    
*   **Nonfunctional requirements:** How the system must behave
    

> Example:
> 
> 1.  The service must expose information about the state of <>, accessible by X ID.
>     
> 2.  Updates to <> must be visible within 10ms
>
