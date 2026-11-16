---
url: "https://dev.to/tooevangelist/the-ultimate-checklist-for-a-company-github-1b2h"
captured_at: "2026-11-16T00:58:13+00:00"
title: "The ultimate checklist for a company GitHub"
domain: "dev-to"
---

[Here’s some context to it](https://dev.to/tooevangelist/how-to-open-source-the-company-s-internal-tech-bg0), but in a nutshell, this long read is focused on what it takes to publish a company internal tool to GitHub. I will use the project I spend my time on as an example.

It takes time and effort to write, but also to read the long reads. So today I will focus on a small subset of the checklist below and will continue in a new blog post if you express your interest with a <3.

This is also a good reason to subscribe so you get a notification once the next part is ready.

## [](#tldr-checklist)TL;DR Checklist:

*   Internal dependencies
*   Security audit
*   License
*   Ownership model
*   Contribution guidelines
*   Code of conduct
*   Documentation
*   Launch plan
*   GitHub as a landing page

The checklist is based on my personal experience, and I am open to feedback and dialogue. I was employed or contracted by 3 companies who were eager to embrace open source to add value to their existing business models. This means that the business wasn’t built around the open-source like it is common to have an open-source product and sell services around it.

I am happy to state that more and more tech startups have this approach in mind.

## [](#github-as-a-landing-page)GitHub as a landing page

In many cases, it makes sense to have the company’s GitHub as the landing page for open-source initiatives. The internet has collected lots of wisdom on a perfect `readme.md` for a small private repo. But we’re talking about a product that was used internally for a while and now is being open-sourced. It is a task of higher complexity.

### [](#developer-community)Developer community

We start from a point when the community maintaining the project is just your team, they use internal processes and tools to communicate and to manage the issues. Transitioning to being open may be too cumbersome and expensive, then there’s a language barrier sometimes.

A good start is to put some feature requests and bugs to GitHub issues on your repo, so it is not empty.

Then you can focus on removing the barriers for the early adopters to dig through your code and try to use your thing. You can start a dedicated `Getting Started` thread in `Issues` so people don’t hesitate to post questions that may not deserve a dedicated issue in the comments. It may sound overwhelming, but we’re just starting to build the community and we have to be friendly and accommodating to people of different cultures and backgrounds.

Here’s an example of the [Issues page](https://github.com/ProtocolONE/ptah-editor/issues) of a young freshly open-sourced product:

## ![GitHub logo](https://res.cloudinary.com/practicaldev/image/fetch/s--vJ70wriM--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://practicaldev-herokuapp-com.freetls.fastly.net/assets/github-logo-ba8488d21cd8ee1fee097b8410db9deaa41d0ca30b004c0c63de0a479114156f.svg) [ProtocolONE](https://github.com/ProtocolONE) / [ptah-editor](https://github.com/ProtocolONE/ptah-editor)

### Powerful, fast and Open source Web Builder Framework for modern cross browser landing pages for the games.

## Ptah - Vue.js-based landing page builder

[Ptah Builder](https://ptah.pro/) is an easy-to-use open-source tool to build landing pages for video games without any coding.

[![License](https://camo.githubusercontent.com/dc5c93f4ddfa92aaed4ace74e89dbc075f7810c8/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d417061636865253230322e302d627269676874677265656e2e737667)](https://opensource.org/licenses/Apache-2.0) [![Build Status](https://camo.githubusercontent.com/1a83e47c9a7515efe5ded5c634de4b78dc66c742/68747470733a2f2f7472617669732d63692e636f6d2f50726f746f636f6c4f6e652f707461682d656469746f722e7376673f6272616e63683d6d6173746572)](https://travis-ci.com/ProtocolOne/ptah-editor) [![Codacy Badge](https://camo.githubusercontent.com/ca630bd0000cf50588f5375122bfc2c31dd2bf6e/68747470733a2f2f6170692e636f646163792e636f6d2f70726f6a6563742f62616467652f47726164652f6461353033626236313131363434663638613132363665656133373330396337)](https://www.codacy.com/app/ProtocolOne/storefront)

### [Features](https://raw.githubusercontent.com/ProtocolONE/ptah-editor/develop/#features) · [Getting Started](https://raw.githubusercontent.com/ProtocolONE/ptah-editor/develop/#getting-started) · [Documentation](https://raw.githubusercontent.com/ProtocolONE/ptah-editor/develop/#documentation) · [Contribute and Support](https://raw.githubusercontent.com/ProtocolONE/ptah-editor/develop/contribute-and-support)

## Features

[![](https://res.cloudinary.com/practicaldev/image/fetch/s--v1I2Tk6h--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://raw.githubusercontent.com/ProtocolONE/ptah-editor/develop/docs/edit-element.gif)](https://ptah.pro/)

[Ptah](https://ptah.pro/) is a Vue.js-based framework that combines various ready-to-use templates for a landing page.

[Ptah Builder](https://ptah.pro/) provides you with all the features you need to promote your game:

*   Free and open source under [Apache-2.0 license](https://raw.githubusercontent.com/ProtocolONE/ptah-editor/develop/LICENSE)
*   Produces ready to deploy [PWA projects](https://developers.google.com/web/progressive-web-apps/)
*   Ships with 2 production quality templates
    *   All our templates feature responsive design out of the box and are mobile-friendly
    *   You can modify our templates or add your own
*   Contains multiple ready to use [building blocks](https://raw.githubusercontent.com/ProtocolONE/ptah-editor/develop//src/components/sections)
    *   Each building section can be additionally tweaked to your needs and taste
    *   Sections support drag-n-drop and live edits

[![](https://res.cloudinary.com/practicaldev/image/fetch/s--pa_la-6R--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://raw.githubusercontent.com/ProtocolONE/ptah-editor/develop/docs/element-library.png)](https://ptah.pro/)

[![](https://res.cloudinary.com/practicaldev/image/fetch/s--KGJDwidf--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://raw.githubusercontent.com/ProtocolONE/ptah-editor/develop/docs/section-library.png)](https://ptah.pro/)

## Documentation

[Here's a blog post at dev.to](https://dev.to/tooevangelist/how-to-open-source-the-company-s-internal-tech-bg0) just about what we're doing and why.

The full documentation for Ptah Builder can be…

Make sure your dev team gets emails or slack messages for new issues on GitHub and that these issues get attention.

You can create custom issue templates to guide users through what you’d like them to submit. We didn’t overthink it [for the start](https://github.com/ProtocolONE/ptah-editor/tree/develop/.github/ISSUE_TEMPLATE). But as our community grows, we’ll put a link to the docs or FAQ to the templates and perhaps we’ll have separate templates for client and server issues.

### [](#readmemd)Readme.md

In many ways `readme.md` has to be optimised for the kind of user you’d like to start looking into your product. It should be easy to navigate, short enough so people can read it and find the relevant info and long enough so people who have no idea what they’re looking for and why on your GitHub page can scroll through to understand if it is something relevant for them.

We optimised the first 30 seconds experience by focusing on bullet points and one-liners that answer the critical questions and explain how the code in this repository may be relevant to the user.

We went the extra mile to have a demo of the product and a demo of whatever the product produces - a progressive web app in our case. We’re still at about 50 starts and don’t have too many people visiting our repository, so cannot tell if that extra mile was worth the effort.

Beyond obvious points like a nice gif, a popular license and some familiar badges, there’s a Getting Started part that draws attention. My very humble opinion is to not overcomplicate things -

*   Clear one-liner what is the expected result
*   The simplest case for how to build the minimal version of the product
*   Loud and sound promise for user support and further development

[In our case](https://github.com/ProtocolONE/ptah-editor/blob/develop/README.md#getting-started) we’re showing only how to build a client while the complex server part with dependencies is hidden in the docs. Which makes sense if you think about it. Ptah is a WYSIWYG editor, so it is the front end that potential users care about most. If devs like the editor, like the code, then they can dig deeper to understand how to launch it all in an own CMS, cloud or whatever setup is necessary.

The tricky part is that the readme features bits and pieces from the documentation along with the pitch. And there’s no easy way to automate it using standard GitHub tools, so you have to remember to update the readme each time you update the corresponding docs. And vice versa.

## [](#license-coc-cg-docs)License, CoC, CG, Docs

These topics require own long reads, but I cannot talk about GitHub as a landing page without mentioning the license, code of conduct, contribution guidelines and documentation.

Many devs cannot use your code if it lacks a popular license, either because they don’t want to pay a lawyer to read through your small print or because this is the policy in their company. This is crucial since the [Open Source Survey](https://opensourcesurvey.org/) states that at least 70% of respondents use open source professionally rather than for hobby projects. The data is years old, although I cannot see it being out of date.

Code of conduct and contribution guidelines are important for the user, but even more important for you as a company. You need a set of clear rules to base your future decisions and conflict resolutions on or else you may find yourself in a toxic situation.

We based [our CoC](https://github.com/ProtocolONE/ptah-editor/blob/develop/CODE_OF_CONDUCT.md) on Contributor Covenant for the same reasons we picked a popular license.

The contribution guidelines require extra work. Currently we just don’t accept pull requests, but further on we’ll explore solutions like [CLA Assistant](https://github.com/cla-assistant/cla-assistant) to automate the legal part.

Good docs take time to build or to move from whatever internal system you have. For now, we just have [a stub to build upon](https://github.com/ProtocolONE/ptah-editor/tree/develop/docs). These are regular non-fancy markdown files that we’ll convert to a nice documentation website using [Hugo](https://gohugo.io/) or similar tech.

## [](#summary)Summary

The checklist above is huge, while this article discusses just a single point that unrolls into 3 more bullet points, each owning a paragraph of text. Indeed, open-sourcing as a company is a different experience than as an individual.

### [](#like-share-ask-questions-i-need-dopamine-and-motivation-to-continue-typing)Like. Share. Ask questions. I need dopamine and motivation to continue typing.
