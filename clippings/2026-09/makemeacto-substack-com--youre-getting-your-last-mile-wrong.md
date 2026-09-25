---
url: "https://makemeacto.substack.com/p/youre-getting-your-last-mile-wrong?r=lcru6&ref=dailydev&triedRedirect=true"
captured_at: "2026-09-25T17:28:47+01:00"
title: "You're getting your last mile wrong"
domain: "makemeacto-substack-com"
---

I recently started building a SaaS tool for Engineering Leaders (more on that soon), which offered me a great opportunity to reflect on the _last mile_ of building a new software product.

Teams and individuals tend to focus 95% of their time and energy up front, building in an isolated environment, and focus on figuring out how to ship their new invention to production way too late.

That's when they face the pain of going through the proverbial _last mile_: setting up delivery pipelines, creating production environments, and often realizing that many of the assumptions they've followed through the development process don't work as well when facing the production test.

Concepts such as Agile development and DevOps have been around for decades. Yet, teams and individuals repeatedly follow superficial rituals without a deep understanding of the principles they're standing on. They all follow a glorified waterfall approach and consider developing and running systems as independent stages.

In today's article, I want to share my philosophy for building new products—whether API services, web applications, or mobile apps—focusing on the _last-mile_ issues that cause frustrations and delays even in 2024.

## The problem with the _last mile_ in software development

Software Engineers, Designers, and Product Managers frequently dream about the opportunity to build something from scratch. We spend the majority of our professional existence dealing with legacy products, maintaining systems built by someone else, often more than a decade ago. We are constrained by the needs of our current users and assumptions built into a codebase that can only evolve very slowly and carefully.

We keep noticing nimble startups moving faster than we do, which adds to our frustration. We know the comparison is unfair, yet we can't resist the temptation of indulging in it ourselves. Even worse, comments from our leaders and stakeholders comparing our ability to move with our up-and-coming competitors can contribute to feeling stuck and underappreciated.

That's why when the opportunity finally presents itself to build something from scratch, we get all excited and jump in it head first. This is finally our opportunity to work without legacy, _move fast and break things_, and show the world our true potential.

We are keen on starting with a clean slate and are happy to leave behind cumbersome constraints and perceived inefficiencies we used to deal with when working on the previous system.

The thrill of building inebriates us without constraints: a clean backlog, no tech debt, and a situation where 100% of our energy can go into _building._

The early stage of excitement can cause us to overlook something crucial, which will typically come back to bite us later.

With all its quirks and inefficiencies, the old systems we used to work on had been running in production for a long time. The ability to run smoothly and predictably results from investments and capabilities built up over time by ourselves or others who came before us.

Most of these capabilities concern non-functional requirements, so we downplay their importance. Their main contribution is hidden in the absence of observable issues or the familiarity of routine operations we've learned to take for granted.

Infrastructure redundancy, security, test automation, observability, and instrumentation are some examples of standard capabilities baked into established products that are often completely ignored in the early stages of building a new product.

Now, there are some valid reasons why you'll want to skip many such requirements: You are running against the clock trying to validate a new product idea. There is no point in prematurely investing in scalability, safety, and robustness until you know your product will have some chance to survive the reality test of putting it in front of the user.

But there is one part you cannot skip no matter how early your product is: **shipping your software to production**.

You can accept taking risks on security or scalability early on. Still, a product doesn't really exist unless it's accessible to your users and offers certain guarantees about data safety and availability.

You can't expect your users to use the current version on your laptop, can you?

Yet, this step is often left to the end, exactly when it is the most disruptive.

When you finally reach the _last mile_ after spending weeks or months building in an artificially simplified environment, two main categories of problems arise.

1.  **Delays.** The more you push the task of setting up your different environments properly and sensibly connecting them, the higher the cost of this activity. What you think might take a few hours at most, in reality, will take many days or weeks. As you’ve been deferring and thinking about how to run and connect all the pieces in production, this process is full of surprises. You keep delaying the release for work that is mainly invisible to nontechnical members of your organization.
2.  **Malfunctioning and bugs.** As you develop, you accumulate complexity, and what can be a minor detail at the beginning can turn into a major issue as you build on top of it. You discover that what worked smoothly on _http://localhost:3000_ doesn't work as well when you deploy the code to an environment with a different topology.

Compound that with the fact that you'll probably be under a lot of pressure — both externally driven and self-imposed — to cram in some additional features before launch, and you're in for a challenging ride.

You likely planned to spend the last few days before the launch adding additional features or tweaking some functional behaviors. Instead, you're trying to rush through delivery-related tasks, with the added risk of making costly mistakes caused by high pressure and expectations.

This is where the misconceptions around Agile and DevOps principles become apparent.

It doesn't matter that you have diligently followed your fair share of sprints, planning, standups, and retrospectives; you forgot the key principle underlying any Agile methodology: at every increment, your software should be _potentially shippable._

Not only are you not shipping it regularly, but you also don't know how exactly you'll ship it; you often don't even have an environment to ship it to.

While DevOps is predicated on the principle that Developing and Delivering software should not be considered in isolation but as two equally important components of the discipline of Software Engineering, you have interpreted them as Dev → Ops.

You do one first and then the other, hoping they'll magically fit together because you're running a Jenkins build on every commit.

The solution might not be appealing, but it's the most effective. Turn the approach around and **make your last mile your first mile**.

## Make it your first mile

![](https://storage.ghost.io/c/d3/84/d3840377-8f34-47dc-83e5-6425ca34f9cb/content/images/2026/06/a634ebb1-266e-4f0e-9fcb-df84eb158805_3046x1860.png)

My recommended approach when building a new product from scratch is almost completely to reverse the order of operations: **Before you write your first line of code, think about how you will operate it in production**.

It isn't very pleasant, and it might sound counterintuitive. You might think it smells of premature optimization, or that's not how nimble startups should operate.

I've heard all sorts of arguments against this approach, yet they tend to fade when the perspective of the _last mile_ pains becomes a reality.

Our brains effectively push us to avoid short-term pain in favor of pleasurable and exciting activities. Most people are more excited about starting to toy with code immediately rather than engaging in the complex activity of figuring out the complexity of shipping it to our users.

Using Khaneman's terminology[1](#footnote-1), _System 1_ just wants to get its hands dirty churning out fresh code, while _System 2_ would rather evaluate the plan for how this new product is supposed to operate.

While there are activities where I'm happy to let my System 1 be in the driving seat, Product Development and Software Engineering are not among them.

So, here is my recommended approach when starting a new project from scratch. Assuming enough clarity about what you're supposed to build is there, you should follow some variation of this sequence:

1.  **Step 1**: Create the required repository/ies with a Hello World implemented using whatever stack you plan to use, with unit tests.
2.  **Step 2**: Set up CI to ensure it's triggered with every PR and push to the main branch.
3.  **Step 3**: Set up at least two environments, one for Test/Staging and one for Production. Some teams like to use three environments; it's up to you. What matters is that you also have a production environment from the beginning.
4.  **Step 4**: Set up CD across the environments following the approach you consider reasonable. Focus on automating deployments from day 0 and making the deployment to Production part of your definition of done.

Once that's available, you can start implementing the actual code for your project. Make sure you treat your production environment as you'd treat a production environment with users relying on it.

You'll want to add some basic level of observability and alerting early on to evolve as you learn more about your system's behaviors.

Bonus points if you add dogfooding to the mix: Can you and your team use the production environment as a tool in your daily work and rely on its availability and data integrity to function correctly?

As you've built these capabilities early on in your product, they will increase rather than slow down your ability to do quick experimentation or even major pivots to your product. The more you progress in the development process, the more time you'll be able to dedicate to shipping value.

Your product will be potentially shippable virtually at any point in its development journey, giving you and your team the extra flexibility to decide to pull the trigger whenever needed without additional delays or complications.

Being able to go live virtually anytime is the ultimate sign of you operating as a nimble startup. There is no reason not to invest in being able to do so early on.

## A word on personal projects

The approach I detailed applies, with a few nuances, to company—or team-based projects as well as personal projects.

With personal projects, I refer to initiatives where a single person is building a software product. This applies both to the traditional Indie Hacker and to many new actors in the space leveraging the possibilities offered by GenAI tools to lower the barrier to entry into coding.

There is an essential factor to consider in such cases, and that's **the lifespan of your idea**.

As you don't rely on a team to do thorough market analysis and product discovery, such projects are often the result of a person having an _idea_ that sounds interesting at the moment. I don’t have an exact number here, but it's well-known that many such ideas do not live more than a few days or weeks. What looked like a great idea turns out to be way too complex, or our interest dies down.

You should adjust the _first-mile_ approach to consider that.

Your first step should be to do early validation of the idea on various dimensions:

*   How familiar are you with the problem space?
*   How tractable is the problem you're trying to solve?
*   Do you have enough motivation and conviction to keep working on it for a long time?

These questions do not replace a thorough product discovery process but should help you filter out ideas that sound nice on paper from those that you should reasonably invest more time in.

As part of this initial process, you will build early prototypes to gain more insights into the problem and solution spaces and demonstrate your willingness to spend hours dealing with them.

There is no need to spend time setting up your delivery mechanisms at this stage, as you do not know yet if there will be a final product. You're focused on exploring and learning.

But once the first phase is over and you have decided to commit to building something for real, I recommend you take the time to think about and set up your delivery capabilities before you move on with the actual implementation.

Software Delivery is one of the key aspects that differentiates the practice of Software Engineering from the practice of Programming. Though the approach I'm suggesting might seem radical, you can decide to adopt it incrementally.

You could spread the work over the first few weeks while doing some product development work in parallel or proactively plan to complete this work a few weeks down the road.

The key recommendation is to follow the principle of building potentially shippable software as closely as possible and consider software delivery a first-class citizen in the work your team is doing to bring an idea from concept to usable solution.

I've only seen positive results whenever I've been able to follow these principles closely, and I'm curious to know more about other people's experiences.

Let's start a conversation in the comments section.

## If you found this valuable

If you found this valuable, here are other ways I can help you and your company:

1.  Follow me on [LinkedIn](https://www.linkedin.com/in/piffio/?ref=makemeacto.cc) for regular posts on tech leadership throughout the week.
2.  [Contact me](https://sergiovisinoni.com/services-for-businesses/?ref=makemeacto.cc) if you're interested in a Fractional CTO, Technical Advisor, or Board Member for your company.
3.  [Work with me 1:1](https://sergiovisinoni.com/services-for-individuals/?ref=makemeacto.cc) as your mentor and coach. I love working with driven and competent people in their specific situations and providing personalized guidance, insights, perspectives, and support.
4.  Promote your product or brand to 1,300+ tech leaders from 80+ countries. Just reply to this email to get a conversation started.

* * *

1.  Daniel Kahneman explains these concepts in his seminal book [Thinking Fast and Slow](https://amzn.to/47BSGSC?ref=makemeacto.cc) [↩](#footnote-anchor-1 "Jump back to footnote 1 in the text.")
