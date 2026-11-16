---
url: "https://dev.to/scriptify/cantara-a-cli-tool-to-create-serverless-fullstack-react-apps-in-minutes-23g"
captured_at: "2026-11-16T19:41:50+00:00"
title: "Cantara 💙 - A CLI tool to create Serverless Fullstack React apps in minutes"
domain: "dev-to"
---

Today, I am happy to announce the release of a project I was working on lately:  
**💥 [Cantara](https://cantara.js.org/)** 💥

**A CLI tool to create (Serverless) Fullstack React apps using TypeScript**

[![Cantara CLI Wizard](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcantara.js.org%2Fimg%2Fctra_dev.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcantara.js.org%2Fimg%2Fctra_dev.gif)

[Website](https://cantara.js.org/) • [GitHub](https://github.com/CantaraJS/cantara) • [Chat on Spectrum](https://spectrum.chat/cantara)

## [](#question-the-what)❓ The WHAT

**[Cantara](https://cantara.js.org/) stands for:**  
**C**reate **A** **N**ode, **T**ypeScript **A**nd **R**eact **A**pplication.

It is a **zero-config** tool for:

*   developing (one or more) React Applications
*   ...with one or more Serverless endpoints **and/or** Node.js APIs
*   ...organized in a Monorepository
*   ...using TypeScript on all layers of the stack

It also makes it easy to share code between layers or to external consumers as packages, which can be used internally or from the outside using NPM.

Cantara aims to cover all aspects of the application development lifecycle for monorepository codebases:

*   Development
*   Testing
*   Building/deploying/publishing
*   Continous Integration
*   ...and so on

It could also be described as **the create-react-app for Fullstack applications**.

**So essentially a tool to make Fullstack TypeScript app development a breeze.**  
**✨Less configuring, more coding.✨**

### [](#zap-features)⚡ Features

*   Develop client side rendered React Apps (like you can do with create-react-app)
*   Develop and deploy serverless APIs
*   Develop Node.js applications (e.g. an express based REST API)
*   Develop React Components/JS packages, use them in your application and publish them to NPM
*   Write unit/integration/e2e tests

## [](#greyquestion-the-why)❔ The WHY

Most of the projects I am and was working on professionally, be it as a solo-dev or in teams, are structured as large monorepositories, where multiple APIs and React Apps are living in the same codebase. This workflow has a lot of advantages, but also includes a tremendous amount of configuration to get everything right: bundling, transpiling, environment variables, testing, CI/CD, just to name a few. This can get out of hand pretty quick. Now combine that complexity with the fact that there's not only one such repository, but multiple per company: Then you have dozens of different configuration files lying around, all trying to achieve basically the same task. Changing a webpack plugin in one configuration should also be reflected in all the other projects. Cantara aims to act as an easy to use abstraction layer over all those tools, taking away the boring parts which just hold you back and cost a lot of precious time. No one likes to spend the whole day configuring webpack (ok, except me probably 🙈).

## [](#fire-getting-started)🔥 Getting started

Enough talk, now let's do something useful with it.  
Getting up and running with a fullstack web application using Cantara is as easy as executing two commands. Let's do this!

First, install Cantara globally:  

```
npm i -g cantara
```

Enter fullscreen mode Exit fullscreen mode

This can take some time, as all development dependencies needed for frontend and backend development need to be installed.

After that, just type:  

```
ctra init my-fullstack-app
cd my-fullstack-app
```

Enter fullscreen mode Exit fullscreen mode

This will create a new folder with a sample application in it.

Now, start Cantara's CLI wizard, which prompts you with all the options you have in the current repository:  

```
ctra
```

Enter fullscreen mode Exit fullscreen mode

[![Cantara CLI Wizard](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcantara.js.org%2Fimg%2Fctra_dev.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcantara.js.org%2Fimg%2Fctra_dev.gif)

Choose the `dev` command and then pick the application `random-image-app`, which is a sweet little React app displaying a random image from Unsplash.  
This React app expects an API server to be running on port `3000`, so let's start that one too! To do so, repeat what you just have done (`ctra` -> `dev`) in a new terminal, but this time select `express-api`.  
As soon as the server started, you can navigate to [localhost:8080](http://localhost:8080/) and should see the following:  
[![Cantara simple starter](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcantara.js.org%2Fimg%2Fstarter_app.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcantara.js.org%2Fimg%2Fstarter_app.png)

Now, you can edit the files under `react-apps/random-image-app/src` or `node-apps/express-api/src` and start developing your app! Adding a new React app or API is as easy as executing the `new` command. For more information, [go to the docs.](https://cantara.js.org/)

This quick start guide merely scratches the surface, but hopefully gives you an idea of what Cantara is and how it can help **you** with your next (or existing) project!

If Cantara sparked your interest, here are some links to get you started:

## [](#clipboard-further-reading)📋 Further Reading

[Quick Start](https://cantara.js.org/docs/quick_start)  
[Website](https://cantara.js.org/)  
[Docs](https://cantara.js.org/docs/docs_intro)  
[Github](https://github.com/CantaraJS/cantara)

## [](#speechballoon-community)💬 Community

If you have questions, ideas or just want to have a chat, join Cantara's Spectrum Community! I'd be happy to meet you there 👋  
[![Join the community on Spectrum](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fwithspectrum.github.io%2Fbadge%2Fbadge.svg)](https://spectrum.chat/cantara)  
Find me on Twitter: [@scriptifyjs](https://twitter.com/scriptifyjs)
