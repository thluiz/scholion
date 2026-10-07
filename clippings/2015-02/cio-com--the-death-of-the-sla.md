---
url: "http://www.cio.com/article/2883770/cloud-computing/the-death-of-the-sla.html"
captured_at: "2015-02-19T06:21:10-03:00"
title: "The Death of the SLA"
domain: "cio-com"
---

# The Death of the SLA

I’ve attended countless cloud presentations discussing vendor relationships and contract agreements. A common feature of these presentations is a discussion of the Service Level Agreement (SLA) and how to define, negotiate and enforce it. I’ve always found this curious, but felt it was a relatively harmless, if not terribly, useful topic.

No longer. If you invest significant effort on a contractual SLA you’re not only wasting time, you’re focusing on the wrong thing. The SLA, if it ever made sense as a key contract topic, does so no longer. The traditional SLA is dead. Here’s why:

**SLAs Are Pointless**

People spend time on SLAs because they think they’ll make the cloud provider pay attention to availability. Guess what? They *already* spend time on availability and work really hard at it. Believing that your negotiation smarts are going to generate something above and beyond that from the provider is wrong. Outages happen and cloud providers respond as quickly as possible.

In any case, cloud providers recognize outages will occur, no matter how hard they try. So their standard contracts abjure responsibility for outages and never, ever promise anything beyond best efforts to restore availability as soon as possible. And your negotiation won’t change that. I remember seeing one presentation, where, after spending over an hour on negotiating SLAs, the speaker took a question: “How flexible are cloud providers on SLAs?” His response: “It depends. The larger providers refuse to make any changes and the smaller providers will sign anything to get the business.” In other words, all your negotiating prowess will be fruitless, in the end.

In any event, the penalties associated with SLAs won’t make you whole. They offer a refund of fees due the provider for the outage period. Not what you lost because your website wasn’t available. If you want to be compensated for that, they’ll steer you to an insurance company for continuity insurance. And guess what? That’s expensive and not easy to obtain. So thinking that there’s an easy legal solution for availability is just plain wrong.

**SLAs Are Distracting**

The biggest problem with a focus on SLA is that it frames the issue incorrectly. It addresses a problem -- infrastructure failure -- with the wrong solution -- legal. Now, don’t expect your legal or finance people to tell you this. As the Sage of Omaha, Warren Buffet says, “Never ask a barber if you need a haircut.” If you ask your lawyer if you should spend time on the SLA, he or she will -- of course -- tell you yes. That’s their haircut.

It also has the inevitable effect of directing you toward providers willing to be responsive to SLA discussions, instead of directing you toward providers with more important characteristics: large capacity, a broad ecosystem and a rich set of services with which to build innovative applications.

Your world is changing -- dramatically. This is an IT-forward economy, and failing to arm yourself with the right tools puts you at an enormous handicap. Spending time seeking a legal solution means time not spent on creating innovation, and every day you lose is a day you’ll never recover.

**The Right Way to Address Infrastructure Failure**

So if the SLA is the wrong solution, what’s the right one? In a word, technical. You have to engineer your applications to provide availability and recognize what characteristics your solutions need:

- **Redundancy**. It used to be the application paradigm was “reliable hardware, unreliable software.” Because applications weren’t reliable, everything was focused on making them simple and putting them onto rock-solid infrastructure. The only problem with that is that it severely limited application functionality, which is no longer tenable in an IT-infused world -- and those new applications are inevitably going to be more complex. The new mantra is “reliable applications, unreliable infrastructure.” This has two implications. First, your infrastructure is liable to fail, so you can’t design assuming a stable environment. Second, some part of your application very likely will fail. Both of these mean you have to avoid SPOF -- single point of failure -- which, in turn, means you have to implement a redundant application topology. So plan on redundancy from the very start of designing your application.
- **Partitioning**. The old model of simple application architectures means that they’re deployed in huge monolithic stacks. It’s difficult to put out a fix or improvement in the app because any change requires enormous integration and testing, so updates are infrequent. The solution to that is partitioning -- or, as the new buzzword puts it, microservices. Breaking the application down into self-contained, separately operating components communicating via RESTful interfaces allows easier updates and more rapid improvement. It’s not as easy as it sounds, however. Netflix, the pioneer and exemplar of microservices had an outage last week, so even the best are challenged with this model. Make no mistake, though, this is the path of the future, and the sooner you begin pursuing it, the better.
- **Elasticity and automation**. Another characteristic of the new model of applications is how much their traffic varies, requiring changes to the application topology to add or remove computing components. All of this topology modification means that the application has to be able to gracefully integrate and shed components -- in a word, be elastic. The only way to achieve this is to implement operational management via automation. This carries a set of requirements, including use of standardized components, automated configuration, application monitoring, and using metrics and analytics to understand application behavior.

The entire concept of an SLA is offloading risk, transferring responsibility to another party. In the new world of applications, unfortunately, that’s not feasible. I believe the next few years will be extremely challenging as practitioners come to grips with designing and operating applications to fit the new paradigm of redundant, partitioned components. Trying to avoid this, or worse, resist it via an insistence upon ever-more stringent vendor SLAs is, at best, misguided, and, at worst, irresponsible.

[Bernard Golden](http://www.cio.com/author/Bernard-Golden/)

Named by Wired.com as one of the 10 most influential people in cloud computing, Bernard Golden serves as vice president of strategy for ActiveState Software, an independent provider of CloudFoundry. He is the author of four books on virtualization and cloud computing, his most recent book being Amazon Web Services for Dummies. Learn more about him at www.bernardgolden.com.

[*Insider Resume Makeover:* Emphasize Your 'X Factor'](http://www.cio.com/article/2881909/resumes/it-resume-makeover-emphasize-your-x-factor.html#tk.cio_nsdr_intrcpt)
