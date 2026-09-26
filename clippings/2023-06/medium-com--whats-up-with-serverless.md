---
url: "https://medium.com/javascript-scene/whats-up-with-serverless-1b9bfa80f21f"
captured_at: "2023-06-26T18:08:20+00:00"
title: "What’s Up With Serverless? - JavaScript Scene - Medium"
domain: "medium-com"
---

[

![Eric Elliott](https://miro.medium.com/v2/resize:fill:88:88/1*VZfJFJj5oVmZ5WzlrgSmRg.jpeg)

](https://medium.com/@_ericelliott?source=post_page-----1b9bfa80f21f--------------------------------)[

![JavaScript Scene](https://miro.medium.com/v2/resize:fill:48:48/1*fegbK6HDD8crwrwARuMhaQ.png)

](https://medium.com/javascript-scene?source=post_page-----1b9bfa80f21f--------------------------------)

Published in

8 min read

Nov 14, 2022

\--

> “Every new app should start serverless.”

Adobe Creative Cloud’s early services were written in Ruby, but they didn’t perform well. So we decided to rebuild them with Node. That was part of my job.

Developing and maintaining always-on API routes is an expensive process. We had custom-built fleet management software. Each service had a `/version` route we'd ping automatically and frequently to detect downtime and cycle out offline services from the load balancer, replacing them with new instances. Each server instance ran a minimal Linux distribution designed for cloud ops. The ops team spent a few hours every week staying on top of updates and customizing our VM configuration.

We also had a custom-built auto-scaler that would monitor traffic and server loads and spin up more servers automatically during busy times. We had dedicated server operations support staff who helped us build and maintain a release train system that would push new changes to production about once an hour. Our build and deploy pipeline was automated using Jenkins — a configuration that took quite some time to evolve into something that worked well for us.

We had custom logging services that aggregated all our server logs so that we could easily query particular requests if something went wrong and we needed to investigate and debug. We also spent a lot of time talking to the folks at MongoDB to figure out how to scale our database operations horizontally to keep up with the rapid growth of the Creative Cloud offering. Every time we launched a new service, we had to do load testing and horizontal scaling tests to ensure it would scale well.

In the early days of Adobe Creative Cloud, Adobe was already a successful software business with a large operational budget and thousands of developers on the payroll. Running all those operations was expensive, and in the early days of Creative Cloud, we weren’t at all sure we would find product-market fit any time soon. We had the budget to take the risk and make it a success, and today, Adobe Creative Cloud is a $10b/year business.

If we were building Creative Cloud from scratch today, we could do it on a fraction of the budget — and we’d get scalability for free.

Serverless can save new development teams hundreds of thousands of dollars — sometimes millions — on the road to successful product launch and growth. With very few exceptions, almost all new software products should be serverless-first and only expand to add managed services on an as-needed basis.

## What is Serverless?

Serverless architecture is a way of building and running applications that do not require traditional server infrastructure, maintenance, or scaling operations. Serverless applications use a combination of 3rd party back-end services and APIs such as [Google Firebase](https://firebase.google.com/) or [FaunaDB](https://fauna.com/). Those services typically scale smoothly and transparently, from a trickle of traffic to tsunami spikes that would drown traditional server architecture faster than you can auto-scale to meet demand.

There are many benefits to using Serverless architecture, including:

1.  **Reduced operational costs:** During early growth, traffic peaks frequently bring in much more traffic than you usually have. To prevent service overload, many startups pay for far more capacity than they need. For example, in the early days of DevAnywhere, our hosting costs were more than $1,000/month to keep up with large, roughly weekly traffic spikes. After switching to serverless architecture, server costs fell to less than $100. When budgets are tight, and the focus is on finding product-market fit, those differences can make or break a company.
2.  **Increased developer productivity:** Serverless architecture can increase developer productivity by allowing developers to focus on building features and functionality rather than worrying about server infrastructure.
3.  **Increased reliability:** Serverless architecture can increase the reliability of applications by allowing them to scale dynamically in response to changes in demand. Serverless architecture responds to traffic spikes with relatively low latency. In contrast, traditional elastic scaling can take minutes to respond to a sudden surge in traffic, leaving the first wave of users looking at error messages instead of your product.

## When Do We Need Servers?

First, serverless doesn’t mean “no servers.” There are still servers under the hood, but you don’t need to manage or maintain them because your in-house APIs are more granular than servers: They’re on-demand functions and data queries instead of always-on, dedicated web servers. In other words, instead of launching Node, Apache, or HAProxy on Docker containers, you build functions and let the cloud service provider handle function invocation for you. Most applications work great without an always-on Node runtime listening for requests.

You may need servers for always-on or long-running processes like high-speed, low-latency PVP game servers or optimization with custom hardware (e.g., ASICs, neural clusters). Even if you need those things, much of your application could still benefit from serverless (e.g., your UX or business logic services).

## The Serverless Stack

This section is opinionated: No exhaustive list of options with pros and cons to help you make your own informed decision. Instead, we’ll list only my favorite options. If you know of some great alternatives, please share them in the comments. Let’s flex the wisdom of the crowd a little.

Let’s look at a few common requirements:

*   **Application framework and deployment**
*   **Authentication**
*   **Database**
*   **Content Management**
*   **Commerce**
*   **Media and Storage**

## Application Framework and Deployment

For a long time, I’ve been saying that using [Vercel](https://vercel.com/) is like employing the best DevOps team in the world, but instead of paying them salaries, they save you money. They did not invent it, but Vercel has made working with serverless a breeze.

[AWS Lambda](https://aws.amazon.com/lambda/) is probably better known, but it’s also quite challenging to integrate. You’ll spend hours just reading the docs. With Next.JS, all you have to do is drop a function in an API folder. To get started, `npm install -g vercel`, create a new React+NextJS app with `npx create-next-app`, and push your first serverless website with `vercel push`. Try it out - you can spin up your first deployment in minutes.

I strongly recommend building your app using Next.js. Next is a serverless-native framework with support for serverless functions, edge functions/API routes, Server Side Render (SSR), [static CDN/edge network deployment](https://vercel.com/docs/concepts/edge-network/overview), [incremental static regeneration](https://vercel.com/docs/concepts/incremental-static-regeneration/quickstart), automatic image optimization, bundle splitting, page load time optimization, cache management — the works.

I was once tech lead on a video social network used by NBC, BBC, CBS, and The Wall Street Journal. Among my other responsibilities, I needed to reduce The Wall Street Journal World Stream page load time from a whopping 20+ seconds.

During that process, we optimized everything: we compressed every file to web-appropriate sizes and formats. We cached all the assets and pushed them to CDN servers close to visiting users. We spent a week working on our cache optimization strategy alone. I spent days combing through our JavaScript bundle, manually splitting and optimizing (this was before bundlers had tree shaking). I wrote a custom framework that allowed us to selectively defer the loading of JavaScript. I lazy-loaded every asset I could.

When all was said and done, I reduced our slow mobile load times from 20+ seconds to about 4 seconds and our broadband load times to about 2 seconds. We were rewarded with a Webby nomination and became one of the first large-scale demonstrations of crowd-sourced social video. Imagine TikTok before TikTok. Before our app, TV networks did not have a good way to invite viewers to participate with crowd-sourced video. But it only gained the traction it did with a tremendous amount of challenging optimization work.

But every app I have ever built with Next.JS is optimized far better. There’s no contest. You have to do something really wrong to fail to get a good lighthouse score with Vercel. See for yourself: We built [EricElliottJS.com](https://ericelliottjs.com/) with Next.JS on Vercel, and we did nothing special to optimize it. Our lighthouse performance score is 96 as of this writing.

By abstracting away the servers, Vercel and Next.js made it possible for their incredibly effective ops team to optimize every part of the deployment stack. Instead of worrying about which servers have the lowest response latency, NodeJS, Apache, or HAProxy, we can focus on building our applications and achieving world-class performance by default.

## Authentication

There are two things you absolutely must understand about authentication:

1.  **Passwords are obsolete and unsafe to use.**
2.  **NEVER build your own authentication.** It requires full-time, dedicated security experts to get right.

For these reasons, I have used [Magic’s Web3 authentication](https://magic.link/) for every app I’ve built since they launched. They are currently the _only_ authentication provider I trust. That said, social auth from a big provider like Google is also acceptable. [Google Firebase](https://firebase.google.com/) also offers social auth that gets the job done. **Whatever you do, DON’T enable username/password flows.**

## Database

I prefer [Fauna](https://fauna.com/) for GraphQL support, event streaming, scalability, ultra-low-latency read and write performance, and reliability. Bonus: You can use the Fauna DB event streaming capability to leverage the database as a message bus and job queue for complex apps, and in-browser query subscriptions can keep your clients in the loop.

In the past, I have also used [Firebase](https://firebase.google.com/), but I prefer Fauna’s features and query flexibility.

## Content Management

This tip comes from one of the companies I advise and mentor ([reach out](https://devanywhere.io/help?subject=Advise+My+Team) if you want me to advise your company, too): [Notion](https://www.notion.so/pricing) has [an API](https://developers.notion.com/) and easy-to-use content management that many companies already use for internal team documentation. Unlike most headless CMS systems, it’s very budget-friendly. Combine their API with [Next.JS incremental static generation](https://nextjs.org/docs/basic-features/data-fetching/incremental-static-regeneration) with on-demand revalidation, and you can avoid making your users wait for round trips to the Notion API.

## Commerce

[Stripe](https://stripe.com/) is excellent for simple subscriptions and payment processing. For more complex commerce, check out [Shopify](https://www.shopify.com/) or [BigCommerce](https://www.bigcommerce.com/solutions/headless-commerce/). Both support headless APIs. For cryptocurrency transactions, [Magic Connect offers turnkey fiat onramps](https://magic.link/docs/connect/additional-features/fiat-on-ramp), including instant ACH, credit card, debit card, Apply Pay, Google Pay, and SEPA transfer.

## Media and Storage

If your content is all made by you, Next.JS has you covered with its auto-optimized Image tag system. If you need to host lots of user-generated content, my favorite programmable media API service is [Cloudinary](https://cloudinary.com/products/programmable_media). If you need permanent, immutable storage for NFTs, you want [NFT.storage](https://nft.storage/) — hosted on IPFS and supported by Filecoin.

## Next Steps

Want to learn more about serverless? At [DevAnywhere.io](https://devanywhere.io/), we can help you get up to speed with serverless using React/Next.js on Vercel. Reach out!

**_Eric Elliott_** _is a Webby-nominated tech product and platform advisor, author of_ [_“Composing Software”_](https://leanpub.com/composingsoftware)_, cofounder of_ [_EricElliottJS.com_](https://ericelliottjs.com/) _and_ [_DevAnywhere.io_](https://devanywhere.io/)_, and dev team mentor. He has contributed to software experiences for_ **_Adobe Systems, Zumba Fitness,_** **_The Wall Street Journal,_** **_ESPN,_** **_BBC,_** _and top recording artists including_ **_Usher, Frank Ocean, Metallica,_** _and many more._

_He enjoys a remote lifestyle with the most beautiful woman in the world._
