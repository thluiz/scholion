---
url: "https://strategizeyourcareer.com/p/ai-steering-how-to-get-ai-to-do-what-you-want?ref=dailydev"
captured_at: "2026-09-25T20:55:52+01:00"
title: "How to turn AI from a random code generator into a reliable teammate"
domain: "strategizeyourcareer-com"
---

Get the free AI Agent Building Blocks ebook when you subscribe:

[

![](https://substackcdn.com/image/fetch/$s_!kwYe!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F969930d1-7a41-45f1-921a-57cf9e34cc44_1080x1350.png)

](https://substackcdn.com/image/fetch/$s_!kwYe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F969930d1-7a41-45f1-921a-57cf9e34cc44_1080x1350.png)

Most engineers I talk to treat AI like a slot machine. Some days it writes a good function, other days it hallucinates code and deletes all the tests so the build succeeds (yes, I’ve seen this multiple times). It feels random, so you end up using it because it seems to be the best practice, but not trusting it, so sometimes it feels like it slows you down.

The truth is simple. Productive engineers do not hope AI gets it right. They steer it. They decide the architecture, the data flow, and the definitions of done. AI only fills in the boring parts at high speed.

You do not need to become an AI researcher for this. You need a different way to think about AI in your daily work. A mental model, a small set of rules, and a workflow you can run on every ticket. That’s what you’ll find in this article (🎁 and a checklist for paid subs with tactical actions)

[

![](https://substackcdn.com/image/fetch/$s_!YCCA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc906647f-a05c-441c-9460-d9bc5492a2e6_500x673.png)

](https://substackcdn.com/image/fetch/$s_!YCCA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc906647f-a05c-441c-9460-d9bc5492a2e6_500x673.png)

*   How to think of AI
    
*   How to write a steering doc
    
*   How to design prompts
    
*   How to build an iterative loop
    

[

![](https://substackcdn.com/image/fetch/$s_!Wk_Z!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2cd056dd-a3ed-4cd0-8a5c-88321c90bbc6_800x60.png)

](https://substackcdn.com/image/fetch/$s_!Wk_Z!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2cd056dd-a3ed-4cd0-8a5c-88321c90bbc6_800x60.png)

Most engineers paste a vague task into an AI tool, accept the first wall of text, and call it a day. The code compiles, so they move on without review, which brings a lot of comments. Even worse if you accept the code and keep building on top of that. The next time, the AI output is worse because it takes bad examples from previous AI-generated code. They stop trusting AI for serious work, and it becomes a downwards spiral.

A teammate wrote a doc that was one hundred percent AI generated. Pasted some metrics and investigations into the prompt, and asked AI to write a document with proposals. There was no investigation behind it. No check if the numbers even made sense. The result looked polished and with good writing, but the solutions proposed weren’t taclking the problem. It was the same pattern as copy pasting a Stack Overflow answer for another problem that you don’t have.

Productive engineers behave differently. They use AI to accelerate steps they already do. They still read documentation, they still design data flows, and they still decide what a good solution looks like. AI speeds up the typing and some of the research, but it does not replace their judgment.

Your manager will not promote the person who pastes prompts and ships whatever comes back. That is like a developer who forwards every question to another teammate. They’ll promote the engineer who can design, orchestrate, and ship with AI as leverage. Steering AI is now part of the job, and sooner than later a performance evaluation criteria.

The first shift is simple. You are the orchestrator. AI is the fast pair of hands, you’re the thinking head. The model does not keep software design principles in mind unless I push for them. It will happily mix concerns in a single function and add logic in the wrong place. If I do not act as the architect, the code base gets messy.

[

![](https://substackcdn.com/image/fetch/$s_!pzAT!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fed489718-5619-4e67-8f70-47a7f1ed7e5d_1648x904.png)

](https://substackcdn.com/image/fetch/$s_!pzAT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fed489718-5619-4e67-8f70-47a7f1ed7e5d_1648x904.png)

For example, when I was working with some dependency injection in Java, I tried to hack my way through with AI. I kept asking for fixes and patches based on the terminal output without really understanding what was happening. The result was a lot of trial and error, with no success. Only when I slowed down and read the terminal output myself I could find what was happening. AI cannot fix a mental model you do not have.

Reviewing AI output is another place where the orchestrator mindset matters. I noticed a lazy habit in myself. Once the AI code worked, I did not want to go through it in detail. The tests passed, so my brain wanted to move on. That is a trap. AI is not yet at the level where you can skip review. You need to treat its output like a pull request from a new hire. First check the structure, then the happy path, then edge cases...

[

![](https://substackcdn.com/image/fetch/$s_!46d2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcac89e3c-c7c2-49d4-a042-8f540188b9ae_822x900.png)

](https://substackcdn.com/image/fetch/$s_!46d2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcac89e3c-c7c2-49d4-a042-8f540188b9ae_822x900.png)

Thinking of AI as a junior engineer is a helpful frame. You give them clear tasks with little ambiguity, you define patterns, and you review their work. Productive engineers do the same with AI. They do not outsource judgment. They design the system, then let AI do the repetitive parts inside that system.

Once you accept that you are the orchestrator, you need to communicate rules to the AI. That is where a steering doc comes in. I treat it as a small rule in the IDE and some snippets I can paste in my prompts. It defines the task at hand (e.g. write code or brainstorm), the code and file structure, and the quality bar I expect.

When I take time to prepare prompts ahead of time and have a clear idea of how I want the code to look, everything moves faster. Instead of asking for implmenetation fast, I check the flows, gather the right context, and craft the requirements. The hard part is defining what to do, and AI is much better when I give it that up front. When implementing, I tell the AI to write the code first, and only when I ask it later, to add metrics or logs. There’s no point in having AI write more code without validating it, it becomes more troublesome.

[

![](https://substackcdn.com/image/fetch/$s_!IqFK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5ef10d4f-33b7-4eca-9c75-5cb654976046_808x882.png)

](https://substackcdn.com/image/fetch/$s_!IqFK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5ef10d4f-33b7-4eca-9c75-5cb654976046_808x882.png)

Guardrails in the steering doc reduce AI “hallucinations”. I set hard limits like “no new dependencies”, “don’t add fake APIs”, “follow existing patterns”. I also add a line that says that if the model does not know something, it must ask clarifying questions first. Also, it’s important to define your domain entities (add lengthy comments in those classes).

This is a lot of work if you wrote from scratch every time. That’s why saving this steering doc as a snippet and tweaking it when AI does somehting unexpected is the way to go.
