---
url: "https://dev.to/bigi/dev-to-is-the-perfect-demonstration-of-how-content-based-web-apps-should-be-developed-5fa4"
captured_at: "2026-11-16T01:08:55+00:00"
title: "Dev.to is the perfect demonstration of how content-based web apps should be developed"
domain: "dev-to"
---

I have been intending to move my writing off of Medium for a while now, and while I haven't put in the work to move old posts away, I'm at least starting to explore other platforms. Dev.to is the one everyone is recommending now, so I signed up and started to try to write a post here.

I'd still like to write that post (and I'll publish it next time), but it'll have to wait -- I have to write about Dev.to right now first and its inspiration for myself.

## [](#devto-is-fast)Dev.to is Fast

It is insane. Dev.to is capital-F Fast. It's so fast that it feels like a local web app, not one on the internet. I was exposed to Dev.to a long time ago but it had always been one-off articles, so the speed is less noticeable; when I actually went through to sign up for an account, edit my profile, etc. I noticed how ridiculously fast it is.

My immediate thought was, what is Dev.to doing right that pretty much every other site on the internet right now is doing wrong? How can they be so fast? By comparison, it makes the sites of even internet giants (Reddit, Github, and even Hacker News!) feel like turtles. And it's not like Dev.to is small -- Alexa reports it at around the 8000~ range in global ranking (compared to HackerNoon at 4000~ or npmjs at 6000~ or so), and there's tons of content!

## [](#digging-into-it-its-a-traditional-rails-site-with-instantclick)Digging into it, it's a traditional Rails site with InstantClick

I first started by viewing source and opening Chrome Dev Tools; and noticed that every page had full HTML rendered so it didn't seem like a React (or any other frontend framework) site. Then I noticed that whenever I hover any links, it sends a request to preload pages. I knew of a JS library called [Turbolinks](https://github.com/turbolinks/turbolinks) that did that, so I thought that might be it.

Then I noticed the Dev.to site code is [open source](https://github.com/thepracticaldev/dev.to), so I checked it out and found its [tech stack page](https://github.com/thepracticaldev/dev.to/blob/master/docs/technical-overview/stack.md) and saw that [InstantClick](http://instantclick.io/) was the secret sauce. It works exactly as I observed -- it preloads the HTML output of hyperlinks as you hover them, and replaces the current page's HTML when you click on them, and adds some `history.pushState()` for good measure.

## [](#this-is-the-model-contentbased-web-apps-should-strive-for)This is the model content-based web apps should strive for

Let's face it, big orgs/startups that manage content-based web sites with a modest amount of functionality/business logic almost always default to React for a frontend framework. Organizationally this makes sense, you have a big dev team working on the product, and a component-based frontend architecture is the most sensible way to work together on a big frontend codebase.

But is it the best UX? One doesn't need to venture far from your typical popular media sites (Techcrunch, ESPN, etc.) to see them doing React or React-like behaviors -- your typical server-side-rendering of the first page, loading a JS bundle, hydrating the app on client JS framework, and then the next pages load in API calls, etc.

In contrast, Dev.to simply prints the output HTML of the page from the server at each server endpoint, and it's only boosted by InstantClick preloading the page when you hover the links (and subsequently the new HTML replacing the current HTML to prevent a full browser page navigation). I argue that this is the model content-based sites, content-based web apps, including blogs, e-commerce web sites, etc. should be using in their development.

## [](#why-does-this-make-sense)Why does this make sense?

We, as the whole tech industry, spent a decade (roughly from 2007 to 2017 or so) optimizing every part of the server side of web apps -- everything ranging from database performance (techniques like read replicas, sharding, and newer and newer generations of DB engines), caching (memcache, Redis, local web server caching), asynchronous work queues for writing data, loadbalancers and infinitely scaling web servers (with the advent of AWS), regions/availability zones and edge CDNs to be closer to users.

Once we have everything, we really proceeded to nullify all that investment in server side performance optimization by putting a heavyweight frontend framework like React on the client side to work with those servers. Now to load a web site you need to load a 1mb JS bundle, have a spinner on the first page load of your site or web app, and let React handle this whole virtual DOM and calculate how to render everything at every point in time when anything changes states. We're right back to where we were in the 2000s when web sites/web apps were slow, when it was because we didn't have all those server side technologies and consumer internet connections were slow. Web sites take a few seconds to load now, just as it did in 2007; but for entirely different reasons. Isn't it a little sad for the end user, with all the advancement of technologies, the user experience stayed roughly the same (or worse)?

## [](#but-componentbased-frontend-development)But, component-based frontend development!

Honestly, as someone who's not a fan of React, the only valid argument I agree with for doing a React frontend (and this is a huge one) is the organizational reason. In my 15 years of working in software teams, component-based frontend is really the most sensible way for a big team to work on a frontend codebase together and scale a frontend codebase; there's no way around it.

Traditional MVC frameworks with templated views make it entirely too difficult to have any reasonable re-use of frontend code without some frankenstein monstrosity; and scaling a jquery frontend inevitably leads to spaghetti code. I believe it's one of the primary reasons React has taken off in tech startups; it's the best way to grow a dev team to work on frontend seriously.

## [](#maybe-a-new-development-paradigm-is-in-order)Maybe a new development paradigm is in order?

How can we take advantage of server side generated HTML outputs in a web app, but also take advantage of component-based frontend development? Here's something I came up with literally just tonight, perhaps this could inspire you to try something similar?

*   Frontend team develops in component-based framework of choice (React, Vue, Svelte, etc.).
*   Frontend toolchain to build static HTML of each page based on components (This build happens both locally during development and on CI tool as well) -- this can continue to use Webpack, Rollup, or whatever folks prefer.
*   Each built page takes in set of variables (similar to how templated views work in traditional MVC web apps).
*   Frontend can mock this backend-provided data similar to how it mocks API responses for React frontends during development.
*   Backend uses a traditional MVC architecture, with any language (Ruby, PHP, Python, Nodejs) and framework (Rails, Laravel, Django, CodeIgniter) of choice.
*   Backend renders views by loading those prebuilt static HTML by page name, and passes in variables just as it does for templated views.
*   Feature development workflow: Backend and frontend team members work on same branch for a feature, each check in their changes independently, when frontend checks in the components source code, CI tool runs the build toolchain and the generated static HTML for each view is then committed into repo as well.
*   Frontend can continue to organize code in a similar React monorepo as they do right now, with reusable components and everything.
*   Don't get me wrong, your React components can still react to clicks, moves, etc. and change states locally, you are free to still make AJAX requests in many valid use cases of it. All of that doesn't change. But page navigation should be left to `<a href>` and InstantClick and the server to generate the next page, when it's an entire page change.

## [](#your-thoughts)Your thoughts?

I haven't given this work flow any more thoughts than it took to just write it all down, so curious to hear opinions of others.
