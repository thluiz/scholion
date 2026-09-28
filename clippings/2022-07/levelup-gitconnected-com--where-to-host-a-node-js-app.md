---
url: "https://levelup.gitconnected.com/where-to-host-a-node-js-app-our-top-10-picks-5d562e207f1a"
captured_at: "2022-07-11T08:34:51-03:00"
title: "Where to Host a Node.js App. Top 10 Node.js Hosting Platforms for… | by Thomas Sentre | Jun, 2022 | Level Up Coding"
domain: "levelup-gitconnected-com"
---

# Where to Host a Node.js App

![1*OWMyT4KTTxP8_zM18VN8cA.jpeg](levelup-gitconnected-com--where-to-host-a-node-js-app/7f03c56e5f6f5fa519b9585869ee06fe.jpeg)

The choice of hosting for Node.js applications depends on your needs. Here is a small list of hosting options that you can explore once you decide to deploy your app and make it public.

First, we will consider simple options that have limited capabilities, and then — more complex, but also have more serious capabilities.

We will start by listing the options from simplest and constrained to more complex and powerful:

- Simplest option over local tunnel.
- Codepen
- Glitch
- Serverless environments
- Google Cloud Platform
- VPS Hosting
- Vercel
- Heroku
- Microsoft Azure
- Standard Server

## **The simplest hosting option: the local tunnel**

Even if your computer is assigned a dynamic IP address or you are behind a NAT (Network Address Translation), you can deploy your application on it and serve user requests to it using a local tunnel.

This option is suitable for quickly organizing testing, for organizing a product demonstration, or for giving access to the application to a very small group of people.

For organizing local tunnels, there is a very good service, [ngrok](https://ngrok.com/), available for many platforms. Using ngrok, it is enough to execute a command like *ngrok PORT* and the port you specified will be available from the Internet. At the same time, if you use the free version of the service, you will have an address in the domain *ngrok.com*. If you decide to sign up for a paid subscription, you can use your own domain names, and, in addition, you can improve the security of the solution (using ngrok, you open access to your computer to the entire Internet).

**Glitch**

[Glitch](https://glitch.com/) is a playground and a way to build your apps faster than ever, and see them live on their own *glitch.com* subdomain. You can also [add a custom domain to your Glitch project.](https://glitch.happyfox.com/kb/article/9-adding-a-custom-domain/) It looks fun (and this is a plus), and it’s not a dumbed-down environment — you get all the power of Node.js, a CDN, secure storage for credentials, GitHub import/export, and much more.

**Codepen**

[Codepen](https://codepen.io/) is a great platform around which an interesting community has formed. Here you can create projects that include multiple files and deploy them using your own domain.

**Serverless environments**

A way to publish your apps, and have no server at all to manage, is [Serverless](https://about.gitlab.com/topics/serverless/). Serverless is a paradigm where you publish your apps as functions, and they respond on a network endpoint (also called FAAS — Functions As A Service).

Very popular solutions are:

They both provide an abstraction layer to publishing on AWS Lambda and other FAAS solutions based on Azure or the Google Cloud offering.

**Google Cloud Platform**

Google Cloud is a great environment for Node deployment.js applications. Here is the relevant section of its [documentation.](https://cloud.google.com/nodejs)

**VPS Hosting**

There are many platforms that provide VPS (Virtual Private Server) hosting services. A common feature of such platforms is the fact that the developer gets a virtual server at his disposal, independently installs an operating system (Linux or Windows) on it, and independently deploys applications. Among the plat­forms that provide VPS services, of which there are a great many, you can note the following that I have used and that I could recommend to others:

**Vercel**

[Vercel](https://vercel.com/) is an interesting option for deploying applications.

There is a free version of Vercel, provided that there are some restric­tions when working with it. There is also a paid, more powerful version of this platform. Using Vercel, you can simply not think about the fact that your application needs a server to work. You simply deploy the applica­tion, and everything else is the responsibility of this platform.

**Heroku**

[Heroku](https://dashboard.heroku.com/) is another great platform for hosting Node.js applications.

**Microsoft Azure**

Another one of the big name cloud computing platforms, [Microsoft Azure](https://azure.microsoft.com/en-us/develop/nodejs/) also offers a number of services that make it easy to host and deploy Node.js applications.

Specifically, Azure’s App Service offers a fully managed solution for hosting Node.js applications.

**Standard Server**

Another hosting solution is to buy (or rent, for example, using the Vultr Bare Metal service) a standard server, install Linux and other software on it, connect it to the Internet, and host Node.js applications on it. Hosting is a huge topic, but we hope that the materials in this section will allow you to choose exactly what you need.

## **What’s the best Node.js hosting for your needs?**

To close out this post and help you pick the best Node.js hosting for your specific situation, let’s run through some scenarios:

First, if you’re technically savvy, the big cloud infrastructure services like [Microsoft Azure](https://azure.microsoft.com/en-us/develop/nodejs/), [AWS](https://aws.amazon.com/getting-started/hands-on/deploy-nodejs-web-app/), and [Google Cloud Platform](https://cloud.google.com/nodejs) make a good option, and they usually give you services that help streamline managing your app and eliminate a lot of the more tedious infrastructure requirements.

[DigitalOcean](https://www.digitalocean.com/) and [Heroku](https://www.heroku.com/) also offer good options, offering a PaaS ( platform as services ) to help you with end-to-end development.

If you’re specifically looking for free Node.js hosting, [Glitch](https://glitch.com/) is a good option for non-mission critical stuff, and [Heroku](https://www.heroku.com/) also offers a limited free plan.

**Conclusion**

I hope this post helps you to find the right NodeJS hosting platform for your needs. It’s highly recommended to make the most of free credit or free trial deals and to try multiple platforms without risk. Most importantly, always make sure you run a scan of your Node.js app to identify security weaknesses when your code goes live.

# Level Up Coding

Thanks for being a part of our community! More content in the [Level Up Coding publication](https://levelup.gitconnected.com/).  
Follow: [Twitter](https://twitter.com/gitconnected), [LinkedIn](https://www.linkedin.com/company/gitconnected), [Newsletter](https://newsletter.levelup.dev/)  
**Level Up is transforming tech recruiting ➡️** [**Join our talent collective**](https://jobs.levelup.dev/talent/welcome?referral=true)
