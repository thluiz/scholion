---
title: "Where to Host a Node.js App"
date: '2022-07-11T08:34:51-03:00'
category: webclip
summary: 'The post compares Node.js hosting options from local tunnels and playgrounds to cloud platforms, VPSs, and standard servers, then matches each option to different needs, budgets, and technical comfort.'
tags: ["nodejs-hosting", "deployment", "cloud-platforms", "vps"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Where to Host a Node.js App. Top 10 Node.js Hosting Platforms for… | by Thomas Sentre | Jun, 2022 | Level Up Coding"
    url: "https://levelup.gitconnected.com/where-to-host-a-node-js-app-our-top-10-picks-5d562e207f1a"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-07/levelup-gitconnected-com--where-to-host-a-node-js-app.md"
    kind: repo
---

The post lists several ways to host a Node.js app, starting with the simplest options and moving toward more capable setups. It says the right choice depends on the kind of app, how public it needs to be, and how much infrastructure the developer wants to manage.

## Reading notes

- A local tunnel can expose an app behind a dynamic IP or NAT, and it is useful for testing, demos, or access by a very small group.
- ngrok is presented as a practical service for local tunnels, with a free plan using an ngrok.com address and paid plans that allow custom domains and more security.
- Glitch is described as a playground for building apps quickly, with live projects on glitch.com subdomains, custom domains, Node.js features, CDN support, secure credential storage, and GitHub import/export.
- Codepen is described as a platform with an active community where projects can include multiple files and use a custom domain.
- Serverless is presented as a way to publish apps as functions without managing a server, using functions that respond on a network endpoint.
- The post says Google Cloud Platform is a good environment for Node.js deployment and points to its Node.js documentation.
- VPS hosting is described as giving the developer a virtual server, installing the operating system separately, and deploying applications independently.
- Vercel is presented as an option with free and paid plans where the platform handles the server side of the deployment.
- Heroku is listed as another platform for hosting Node.js applications, and later as a free option for limited use.
- Microsoft Azure is described as a major cloud platform with services for hosting and deploying Node.js applications, including App Service for fully managed hosting.
- A standard server can also be bought or rented, connected to the internet, and used to host Node.js apps.
- For technically savvy users, Azure, AWS, and Google Cloud Platform are recommended as good choices because they streamline infrastructure work.
- DigitalOcean and Heroku are presented as PaaS options for end-to-end development.
- For free hosting, Glitch is recommended for non-mission-critical projects, and Heroku is said to offer a limited free plan.
- The conclusion advises trying free credits or free trials and scanning the app for security weaknesses before it goes live.
