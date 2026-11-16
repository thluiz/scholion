---
url: "https://medium.com/nick-tune-tech-strategy-blog/remote-optimised-domain-modelling-the-present-and-future-7d5e7d68c790"
captured_at: "2026-11-16T05:57:11+00:00"
title: "Remote-optimised Domain Modelling: The Present and Future | by Nick Tune | Nick Tune's weird ideas | Medium"
domain: "medium-com"
---

Ddd
Domain Modeling
Domain Driven Design
Remote-optimised Domain Modelling: The Present and Future
Nick Tune
10 min read
·
Apr 26, 2020

The techniques we use for visual, collaborative domain modelling are designed for in-person events, where everybody is in the same physical space. Teams working remotely have long been excluded from the real power of collaborative domain modelling.

Suddenly, though, we are all working remotely, and we may be working remotely in some fashion for an extended period of time. And when not enforced, we may see a big shift in people wanting to work remotely, and the need to prevent climate change may prohibit travel.

Both in the short-term and the long-term, there is a need for effective collaborative domain modelling techniques for remote teams.

I’m personally quite excited by the possibilities and I’ve been working with Gien Verschatse to experiment with remote-optimised modelling techniques. In this article we’ll take a look at what’s possible now, in the near future and the distant future.

We will be running a remote-optimised domain-driven design workshop on 15–16th June where we will use some of the techniques discussed in this post and many others, like the bounded context canvas.

Framing the Opportunity for Remote Domain Modelling

Before I share with you a few tricks and ideas for remote-optimised domain modelling, I’m going to explain some ideas around innovation which are useful for understanding how to apply the right mindset to remote-optimised domain modelling (you can skip this boring bit if you want).

Identify the True Limitations

Many of the efforts at converting in-person techniques to remote-friendly versions are applying a lift-and-shift mentality. Taking what works in-person and trying to recreate it in a digital environment is a sensible first step, but it’s unlikely to result in the optimal remote modelling technique.

In Dan North’s exceptional talk How to Break the Rules, which has influenced my thinking enormously, he quotes Eli Goldratt:

Technology can bring benefits if, and only if, it diminishes a limitation.

— Eli Goldratt

When we switch from in-person to remote, we are suffering from many additional limitations such as the ability to communicate easily, or read people’s body language.

When we switch to remote domain modelling, we also remove many limitations. The limitations we remove are significant, and open up new opportunities for us to exploit which are not possible with in-person modelling.

This means we should think about remote modelling from a fresh perspective. Not as a pathetic, temporary alternative to in-person, but a totally different experience designed around it’s limitations and advantages.

Anticipating Future Innovations

The limitations that exist now for both in-person and remote modelling will not exist in the future. Remote communication will be profoundly enhanced in the future, accelerated by the current pressures. The only question is how long it will take to make the giant leaps.

In-person limitations will also be removed. Instead of having to purchase physical goods like pens and post-its, there will be digital equivalents. It’s just a case of when.

As Simon Wardley’s Wardley Mapping teaches us. Every concept is moving from left to right — from novel new idea to established, commoditised product.

When you realise every concept is evolving, and you look at how quickly things change, you realise how radically different the world could look in a few years. Less than a decade ago the smartest and most senior engineers I worked with told me “The cloud is nice but it’s not going to be for most companies, especially us.” That aged well.

A Wardley Map. Credit: Simon Wardley (https://twitter.com/swardley/status/1254345323780153344)
Products Co-evolve with Usage

The way we use tools influences how they evolve. I still remember when retweeting with a comment on twitter was performed by manually adding the prefix “RT:” followed by a copy of the original tweet. Twitter saw this popular behaviour and made it a feature of their product to improve the user experience.

The existing generation of tools might be cumbersome for remote domain modelling, but if we are patient and we can find techniques that work, even if they are slow and painful, they can become first class product features in the future.

It’s going to be a long journey, but it can be an enjoyable and rewarding one.

Remote Limitations and Opportunities

Having large groups of people working in parallel is a characteristic of existing modelling techniques. The limitations of remote communication tools, like Zoom, make it practically impossible to replicate such rich communication in a remote environment.

My feeling at the moment is that for remote modelling we should follow the sentiment of Gall’s Law and build something simple that works and later evolve it into something more complicated that works. And we should adopt the Lean Startup approach of running lots of small experiments to see what works and what doesn’t for given situations and groups of people (I do this for all of my workshops anyway).

Single-threaded Storytelling

Single-threaded storytelling means that there is one conversation happening at a time, and only person is allowed to update the model. The storytelling elements means that we focus on specific parts of the domain, or specific user journeys rather than trying to model the whole domain, as one model, all at the same time.

This style of modelling will be slow and will not generate the huge insights of a chaotic, parallel modelling process. But it will provide a solid foundation on which to run experiments that help us to scale the technique. And I must be clear, I already use this format in-person, because I enjoy the calm nature and low-tempo. It is an effective way to collaboratively model domains.

In practice, single-threaded storytelling begins by defining a specific story to model. The more concrete the better. Use real user personas, given them names. Here’s an example:

This description describes the story that will be modelled — a limited slice of the domain rather than the entire domain

Workshop attendees who cannot speak are always allowed to annotate the boards with questions which are subsequently reviewed.

Frequent Iterations and Feedback

It is easy for people to dis-engage when all they are doing is watching. Working in iterations can remedy this. Rotate the facilitator mob-programming style. Every 10–15 minutes is a useful starting point.

At the end of each iteration, review the questions that have been added to the board. Discuss them or dot vote on them. And then ask the group for their feedback, and decide as a group where to go next: continue modelling the same flow, zoom in on a specific aspect, zoom out to a higher level, or switch to another story. Or, just take a break.

Purpose-designed Notation

A limitation of the physical world is that we have to use post-it notes. Ignoring the hassles of having to buy large quantities of post-its in a variety of shapes and colours, post-it notes are an extremely generic tool applicable to a wide range of scenarios.

When modelling domains digitally, the physical limitations are gone (and the shopping bills, and all of the faff) and we can design notation that better suits domain modelling rather than generic ones.

Below is a sample of the rough first iteration of notations Gien and I threw together over the course of a few hours on a Sunday afternoon.

Visually, I find this easier to read and follow than post-it notes (many people will have strong and varying opinions about this, here I am merely expressing my own preferences). And this was just a first attempt. I’m sure it’s possible to create notations that properly improve the experience of remote modelling.

Lines and Arrows

In-person modelling sessions prohibit the use of lines and arrows. Despite this rule, people always try to use them in collaborative domain modelling sessions. Sometimes unnecessarily, but on many occasions lines and arrows would be beneficial.

We can’t use lines and arrows in a physical environment because we need the ability to move post-its around the wall and we can’t move the ink stained into the paper with them.

This limitation does not exist in the digital world. When we have loops, fan-ins, and fans-out in our domain processes, we can easily show them. There is, obviously a risk that they can over-complicate our visualisation, so we still need to apply them judiciously.

Enhanced Visualisation of Time

With in-person modelling, we know that time flows left to right. The model tells a story running from left-to-right. But it’s not clear exactly how much time passes between each event.

Using digital tools, there is no limitation preventing us from showing us the elapsed amount of time between each step in the process. By showing the duration of time that elapses between each domain event, we add a rich dimension to our model.

For example, when we realise that there is large gap of time between two events, it’s a sign that there could be a lot of detail here that we have missed. More edge cases and complexity we should ask our domain experts to describe to us.

The duration of time between events can uncover hidden edge cases or user behaviours

In the example above, a first time user has to wait for their driving licence to be approved before they can rent an electric scooter. By asking the domain expert “what is the minimum and maximum time between these two events” we realised that nobody would wait the full two hours. This uncovered a drop out in the flow and an opportunity to improve the UX.

Digital Catalogue of Questions and Outcomes

Digital tools like Miro treat comments as first class citizens with special powers. It’s possible to view all questions in a todo list format and be notified when there are updates. The comment stores metadata, such as the person who create the question and allows a conversation to be associated with the question.

Miro also has the concept of a card. We can use these to capture outcomes from the workshop aka follow-up actions. Cards also have a special todo-list style board meaning they can be left on the model next to the part of the domain they are related to, but they can also be viewed separately on the list view so they aren’t missed.

This is an example of the general benefit when storing things as digital data. We can project the same data into multiple different views for different purposes. In-person modelling does not allow this.

Comments and Cards (conventions shown are our and not enforced by Miro)
Higher Lifetime Value of Model with Asynchronous Communication

Storing our visual domain models electronically means they have a higher lifetime value.

In-person domain modelling sessions mean we can get lots of people in the same place at the same time and have lots of high-value, cross-discipline conversations occurring in parallel. Remote modelling cannot compete with these short-term benefits.

The competitive advantage for remote modelling is that a model can be built up at a slower pace over a longer period of time. Everybody in the company can have access to the model, not only to contribute, but to challenge and to ask their questions at any time — fitting beautifully into the workflow of distributed teams who who work asynchronously.

The potential is there for remote domain modelling to be more inclusive to a greater number of people (your whole organisation) who can both contribute to and learn from the model.

Copy and Paste

A digital model can be copy and pasted, but why would anybody want to do that?

One scenario where copy and paste is extremely valuable is when we want to re-model into a different format such as from a singe flow narrative to a swimlane based narrative which helps to identify the hand-offs between different actors in the domain.

Another scenario where copy and paste is valuable is where different individuals or different groups want to translate the domain model into a software architecture aligned to bounded contexts by grouping events on the model.

In my in-person workshops, I’ve faced this hard limitation. There is 1 model shared by the whole group. It’s not possible to give each small team their own copy of the model as a basis for designing their architecture. With remote modelling it is!

Extensibility and APIs

Some products become wildly successful due to their extensibility. They open up their product as a set of APIs, and become a platform for a whole ecosystem of tools. Slack is an example that immediately springs to mind.

Online collaboration tools are heading well in this direction. Miro already supports integrations and has a suite of APIs.

When our domain models are stored as digital information and exposed as APIs, who can predict the type of innovations that may arise? A whole world of possibilities awaits.

Big Potential, But Patience and Caution Needed

Remote domain modelling is at the far left of the Wardley Map. There is a whole bunch of innovation that is going to happen over the next decades. I’m optimistic and I’m quite excited to see what happens. It’s an area I’m certainly going to be working in.

We do have to be careful not to repeat the mistakes of previous waves of innovation, especially enterprise data models and code-generation. But equally we need to remember that each iteration of an innovation removes some limitations and opens new possibilities.

Current and future generations of tools may look similar to previous generations, and our instincts may warn us to avoid them. I’ll never forget the hostility toward the iPad when it was launched, even from the hardcore Apple fans. Who doesn’t own a tablet now?

I encourage you to be patient, to give remote domain modelling a try, and to take an experimental approach.

If you’re interested in collaborating, or you want to share ideas, then of course I would love to hear from you and we can experiment together.
