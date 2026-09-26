---
url: "https://machine-learning-made-simple.medium.com/understanding-managed-services-in-software-engineering-606804469fa3"
captured_at: "2025-07-17T03:10:51+00:00"
title: "Understanding Managed Services in Software Engineering"
domain: "machine-learning-made-simple-medium-com"
---

## Exploring the business of convenience, Cloud, and More.

[

![Devansh](https://miro.medium.com/v2/resize:fill:64:64/1*xiFRgHfgfMR7S111UB2hMw.jpeg)

](https://machine-learning-made-simple.medium.com/?source=post_page---byline--606804469fa3---------------------------------------)

11 min read

Sep 23, 2024

\--

Earlier this week, we talked about [The Business of Open Source and how people often misunderstand the relationship between Open and Closed Software](https://artificialintelligencemadesimple.substack.com/p/why-companies-invest-in-open-source). To reiterate-

> **Because it leverages crowd-sourced expertise, OSS is really good at the Macro- solving big, important problems that affect tons of people. Consequently, OS Projects often form foundational components- frameworks, platforms, core technologies etc.** However, you can’t build a successful product by solving the average problem because the average person does not exist. People have specific challenges, quirks, and advantages, and that is what they will pay for. A strong foundation is important for a house, but no one will buy a house with only a foundation. **Closed Software is great for this, and thus many successful AI/Tech companies build massive companies around OS Tech to solve specific challenges for specific enterprises.**

This post aims to be a practical example to highlight the ideas discussed there by exploring a particular kind of business strategy built around OSS software- Providing Managed Services. In today’s rapidly evolving cloud computing environment, software engineers face a pivotal choice that can significantly shape their projects: opting for managed or unmanaged infrastructure. **_This decision extends beyond technical preferences; it’s a strategic move that affects development velocity, scalability, operational expenses, and security strategies._**

FYI, the Open Source article has this masterpiece, so make sure you catch it if you haven’t already.

This article will play with the complexities of infrastructure models to examine the subtleties of each approach. I’ll share my opinions on the benefits and challenges of managed and unmanaged infrastructures and offer my rough framework when evaluating what to recommend. **_Remember that while I am a competent Software Engineer (at least when it comes to AI), my core skillset is closer to applied research. My thoughts on this subject (or any other) should never be treated as the end-all. They are simply starting points for a discussion around this topic, and I’d encourage you to pitch in your thoughts as well._**

With that covered, let’s get into the thoughts in more detail.

## Understanding Managed vs. Unmanaged Infrastructure

**Managed Infrastructure** and **Unmanaged Infrastructure** represent two ends of a spectrum concerning who is responsible for managing different layers of the technology stack:

*   **Unmanaged Infrastructure**: You, as the user, are responsible for managing most or all aspects of the infrastructure. This includes the hardware, network, operating system, middleware, runtime, data, and applications. You have maximum control but also bear full responsibility for maintenance, updates, security, and scalability. You are condemned to be free and completely responsible for all that you do.
*   **Managed Infrastructure**: The service provider takes on the responsibility for managing various layers of the infrastructure. This reduces your operational burden but also limits the level of control you have over the environment. It’s like getting Ronaldo on your team- you’re guaranteed certain results, but you’ll have to adjust your process to accommodate him.

That is the crux of the article, and you can honestly click off here. The rest of this piece will be my thoughts on this topic in more detail than

When evaluating the tradeoffs on this topic, I think it can be good to map this discussion to a discussion that’s more common in tech, since it also reflects the dynamic of convenience vs control-

[Source](https://kinsta.com/blog/function-as-a-service/)

So let’s dig into this and see how it can inform our thoughts on managed vs unmanaged services.

_I provide various consulting and advisory services. If you‘d like to explore how we can work together,_ [_reach out to me through any of my socials over here_](https://linktr.ee/iseethings404) _or reply to this email._

## Exploring the Infrastructure-Service Spectrum

Understanding the array of infrastructure models available is essential for effectively comparing managed and unmanaged options. This will form the context for our analysis. The different models are differentiated on how much control (and responsibility) you experience-

[Source](https://medium.com/@tanmayct/serverless-architecture-function-as-a-service-19e127b8c990)

As you shift from left to right- you give up more control in favor for convenience. This also theoretically coincides with a shift from CapEx (Capital Expenditures or big one-time payments for buying) towards OpEx (Operating Expenditures or smaller, recurring payments). However, in most cases, maintenance can add a lot of OpEx when you’re responsible for everything, and that’s why many non-tech companies (companies where developers are a cost center, not money-makers) tend to favor SaaS. **Some tech teams look down on this, but IMO you should buy when you can to allocate your time to more specialized needs (although this might just be my inherent desire to work as little as possible).**

## Infrastructure as a Service (IaaS)

At the foundation of cloud computing lies IaaS, providing virtualized computing resources over the internet. IaaS offers high levels of control, granting engineers full access to operating systems, network settings, and storage configurations.

**Key Features:**

*   Provisioning of virtual machines, storage volumes, virtual private clouds (VPCs), and load balancers
*   Flexibility to create custom application stacks and migrate legacy systems
*   Requires expertise in operating system hardening, network security, and infrastructure scaling

**Technical Considerations:**

*   Enables granular control over resource allocation and performance tuning
*   Supports custom kernel modules and low-level optimizations
*   Kind of a pain to deal with and I like to avoid working on this when I can. I kept using a laptop for 4+ years (without a GPU!!) just because I didn’t want to go through the effort of redownloading Python and AI tools.

Examples include AWS EC2, Google Compute Engine, and Azure Virtual Machines.

[Source](https://www.mongodb.com/resources/basics/cloud-explained/virtual-machines)

## Platform as a Service (PaaS)

Stepping up the abstraction ladder, PaaS provides pre-configured environments optimized for application deployment. **This model allows developers to focus on writing code rather than managing infrastructure.** This is where I operate the most for my work.

**Key Features:**

*   Offers application runtimes, middleware, and development tools
*   Ideal for deploying web applications, APIs, and microservices
*   Abstracts away operating system management, patching, and some scaling concerns

**Technical Considerations:**

*   May impose restrictions on language versions, libraries, and deployment processes
*   Often includes integrated continuous integration/continuous deployment (CI/CD) pipelines and monitoring tools

Popular PaaS offerings are AWS Elastic Beanstalk, Google App Engine, and Heroku.

I find PaaS very interesting because of how lucrative the Platform play has been for various organizations. Becoming a platform allows a company to leverage economies of scale, since it allows other people to build on top of it (instead of building everything itself). Operating Systems, Mobile App Stores, and Foundation Models can be seen as three iterations of the same principle- make a lot of money by incentivising other people to build on top of something you provide.

[Image Source](https://www.fostec.com/en/platform-economy-strategy/?open=). I think it’s interesting how many software products end up as Platforms as the final iteration. Platforms are like the Crabs of Software Products. Although I might just be biased because I’m working on building a legal platform right now (FYI we’re looking for investors, so reach out if interested. [Some deets on the AI here](https://open.substack.com/pub/artificialintelligencemadesimple/p/how-we-built-an-efficient-knowledge?r=4tnbw&utm_campaign=post&utm_medium=web)).

In most conversations, we would now talk about SaaS, but not here. That’s b/c this post is in the context of managed and unmanaged services and what to build on- and developers don’t build on a SaaS product (you use it as is). So, instead, let’s move to the maximum possible level of abstraction for a developer.

## Function as a Service (FaaS) / Serverless Computing

At the highest abstraction level, FaaS or serverless computing (these aren’t the same, but close enough for our discussion) enables developers to deploy individual functions that execute on demand, automatically scaling with traffic.

**_Organizations will continue to invest in serverless._** _95 percent of users surveyed plan to maintain or increase their serverless investments during the next year._[Source- IBMs writeup on Serverless](https://www.ibm.com/cloud/learn/serverless)

[Anatomy of a Functions as a Service (FaaS) Solution](https://blogs.vmware.com/professional-services/2020/04/anatomy-of-a-functions-as-a-service-faas-solution.html)

**Key Features:**

*   Event-driven, stateless computing platforms

[So… what is Stateless Architecture in Software Engineering](https://codinginterviewsmadesimple.substack.com/p/so-what-is-stateless-architecture?utm_source=publication-search)

*   Suited for event processing, scheduled tasks, and real-time data processing
*   Provides automatic scaling with pay-per-execution pricing models

**Technical Considerations:**

*   Requires stateless design patterns and awareness of cold start latencies
*   Can complicate local testing and debugging processes.
*   Can be easy to fall asleep at the wheel when building on this, so be careful to have lots of checks to ensure you don’t end up donating money to your cloud providers.

Prominent examples include AWS Lambda, Google Cloud Functions, and Azure Functions.

Evaluating the results from this tradeoff can help us make better judgments on our unmanaged vs. managed services conundrum.

## Unmanaged Infrastructure: Control with Complexity

## The Power of Customization

Unmanaged infrastructure places you firmly in control, allowing for extensive customization beneficial in specific scenarios:

1\. **Performance Optimization:** Access to low-level configurations enables fine-tuning of system performance. You can implement custom TCP algorithms, optimize CPU scheduling, and tailor storage I/O to your workload.

2\. **Compliance Requirements**: Industries with strict regulatory standards can implement custom security protocols, data handling procedures, and auditing mechanisms to meet compliance needs precisely. This has been the biggest selling point of the Legal AI startup I’m working on since we allow our users the maximum possible security on a digital system.

3\. **Legacy System Suppor**t: Unmanaged infrastructure allows replication of outdated environments necessary for legacy applications, ensuring compatibility while leveraging cloud benefits.

Unfortunately, freedom is expensive-

## The Costs of Autonomy

1\. **Operational Complexity**: Managing every infrastructure aspect — from OS security to disaster recovery — demands a team with broad expertise in system administration, network engineering, and cybersecurity.

2\. **Performance Tuning Overhead**: Realizing performance gains requires significant effort. Engineers must be skilled in low-level optimizations, such as CPU pinning and Non-Uniform Memory Access (NUMA) configurations.

CPU pinning ties a CPU to a specific VM, ensuring that VM gets the complete resources of it. This is good for mission critical apps, where you don’t want to skimp on latency. [Image Source](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux_openstack_platform/7/html/instances_and_images_guide/ch-cpu_pinning)

3\. **Security and Compliance Burden**: You are responsible for implementing comprehensive security measures, including intrusion detection, firewall management, and timely patching against vulnerabilities.

## Managed Services: Convenience with Constraints

Managed services offer a contrasting approach, trading some control for ease of use and accelerated development.

## Accelerating Development and Deployment

Managed services reduce the operational load, offering several advantages:

**Rapid Deployment**: With pre-configured environments and built-in CI/CD tools, you can move from code to production swiftly, reducing time-to-market. This has been one of the biggest reasons behind the Vector DB hype- they don’t do much that you couldn’t do yourself ([and tbh, you’re better off not using them in more cases than you’d think- as we discussed in our deep-dive on best practices for RAG](https://artificialintelligencemadesimple.substack.com/p/understanding-the-best-practices)). But they do make using Vectors a bit easier, which is why a lot of people default to them-

2\. **Automatic Scaling and High Availability**: Out-of-the-box solutions for load balancing and auto-scaling simplify the creation of resilient, multi-region architectures.

3\. **Built-in Security Features**: Managed services often include security best practices by default, such as managed encryption and automated patching, reducing the risk of misconfigurations.

## The Trade-offs

Despite the benefits, managed services come with considerations:

**Vendor Lock-in**: Deep integration with a provider’s ecosystem can make future migrations challenging if your needs evolve. Migration Costs are a massive problem that are often overlooked when making these decisions.

**Performance Overhead**: Abstraction layers may introduce slight performance penalties compared to finely-tuned, unmanaged solutions.

**Limited Visibility**: Reduced access to underlying infrastructure can complicate troubleshooting and performance optimization, sometimes necessitating support from the provider.

Putting all that together, we here are some factors that help me think about this topic-

## Decision-Making Framework:

Choosing between managed and unmanaged infrastructure requires careful analysis. Consider the following factors:

**Application Architecture**: Microservices and modern architectures often benefit from managed services, while monolithic or specialized applications may require the control of unmanaged infrastructure.

**Scalability Needs**: Applications with variable traffic patterns might favor the automatic scaling of managed services, whereas predictable workloads could be more cost-effective on unmanaged platforms.

**Performance Requirements**: If your application demands ultra-low latency or specific resource configurations, unmanaged infrastructure may be necessary. If instead, you need to do a lot of testing/restructuring, using MSPs can reduce the effort required to manage every variable.

**Security and Compliance**: Assess your industry’s regulatory requirements. Managed services provide strong security features, but certain compliance standards might necessitate the control only unmanaged infrastructure offers. In cases with sensitive data, your customers might not want that data being pinged around a bunch of different providers, and this might force you toward Unmanaged services.

**Team Expertise**: Evaluate your team’s skills. Unmanaged infrastructure demands a wide range of expertise, whereas managed services allow teams to focus more on application development. Keep in mind that you’ll only get the maximum benefits from unmanaged if your team has the skills to make it worthwhile, and it’s worth considering if this is a battle you want to fight.

Fortunately, it is possible to successfully combine both approaches, which we will talk about another time. For now, there’s a very special follow up that I have to write, so I’ll end this here and catch you later.

[If you liked this article and wish to share it, please refer to the following guidelines.](https://artificialintelligencemadesimple.substack.com/p/read-this-if-you-want-to-share-ai)

I put a lot of work into writing this newsletter. To do so, I rely on you for support. If a few more people choose to become paid subscribers, the Chocolate Milk Cult can continue to provide high-quality and accessible education and opportunities to anyone who needs it. If you think this mission is worth contributing to, please consider a premium subscription. You can do so for less than the cost of a Netflix Subscription.

[**Upgrade to paid**](https://artificialintelligencemadesimple.substack.com/subscribe?)

**Many companies have a learning budget, and you can expense your subscription through that budget.** [**You can use the following for an email template**](https://docs.google.com/document/d/1xy6CNE8S7ZIM1LPKc5qdjwLJcqj6lwxzv3HFz3gEU14/edit?usp=sharing)**.**

That is it for this piece. I appreciate your time. As always, if you’re interested in working with me or checking out my other work, my links will be at the end of this email/post. And if you found value in this write-up, I would appreciate you sharing it with more people. **It is word-of-mouth referrals like yours that help me grow.** [You can share your testimonials over here](https://shoutout.io/submit/aimadesimple/).

I regularly share mini-updates on what I read on the Microblogging sites [X(https://twitter.com/Machine01776819](https://substack.com/redirect/ff622832-9505-453b-ae09-978237ceceb0?j=eyJ1IjoiNHRuYncifQ.nS0IHgRyrTV_q5g5rpAjxOmBlt9SxaItll-b0wAdi-o)), [Threads(https://www.threads.net/@iseethings404](https://www.threads.net/@iseethings404)), and [TikTok(https://www.tiktok.com/@devansh\_ai\_made\_simple](https://www.tiktok.com/@chocolatemilkcultleader?_t=8lBL3GzTyXK&_r=1))- so follow me there if you’re interested in keeping up with my learnings.

## Reach out to me

Use the links below to check out my other content, learn more about tutoring, reach out to me about projects, or just to say hi.

[Small Snippets about Tech, AI and Machine Learning over here](https://www.instagram.com/yourgodandsavior/)

[AI Newsletter- https://artificialintelligencemadesimple.substack.com/](https://artificialintelligencemadesimple.substack.com/)

[My grandma’s favorite Tech Newsletter- https://codinginterviewsmadesimple.substack.com/](https://codinginterviewsmadesimple.substack.com/)

Check out my other articles on Medium. : [https://rb.gy/zn1aiu](https://machine-learning-made-simple.medium.com/)

My YouTube: [https://rb.gy/88iwdd](https://rb.gy/88iwdd)

Reach out to me on LinkedIn. Let’s connect: [https://rb.gy/m5ok2y](https://www.linkedin.com/in/devansh-devansh-516004168/)

My Instagram: [https://rb.gy/gmvuy9](https://rb.gy/gmvuy9)

My Twitter: [https://twitter.com/Machine01776819](https://twitter.com/Machine01776819)
