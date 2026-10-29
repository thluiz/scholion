---
title: "Why I hate your Single Page App"
date: '2016-02-07T23:08:27-03:00'
category: webclip
summary: 'The author argues that most SPAs break core web features, centralize too much behavior in the client, and trade away linking, performance, accessibility, and maintainability for little user benefit.'
tags: ["single-page-apps", "web-architecture", "rest", "accessibility"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Why I hate your Single Page App — Medium"
    url: "https://medium.com/@stilkov/why-i-hate-your-single-page-app-f08bb4ff9134#.uzzji7uts"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-02/medium-com--why-i-hate-your-single-page-app.md"
    kind: repo
---

The author says most single page apps are annoying because they break browser features like back and forward navigation, refresh, bookmarking, and shareable links, while also loading slowly for simple interactions. He argues that this is a sign of the wrong architectural choice, since web applications should work with the web rather than against it.

## Reading notes

- Most SPAs break core browser behavior, including history navigation, refresh, bookmarking, and opening links in new tabs.
- They often have only one URI for the whole application instead of stable links for the things inside it.
- The author sees this as evidence that many SPAs are not really “on the web” in the way the web is meant to work.
- He says the web’s key feature is linking to individual things, so every important concept in an application should have its own entry point.
- He argues that back and forward navigation is an essential feature, not a bug.
- He says each target should respond quickly because any overhead is paid many times.
- If someone does not care about the web, he suggests building a native app, applet, Flash, or Silverlight instead.
- He warns that browser-based apps still sacrifice web properties even if they run in the browser.
- He says people often treat SPA development as synonymous with modern web development, while ignoring the downsides.
- He lists downsides such as framework maintenance problems, client-side complexity, performance issues, and accessibility problems.
- He presents the alternative as a classic web application with server-side HTML rendering and limited JavaScript for enhancement.
- In that approach, business logic stays on the server, including the state machine that handles page transitions.
- He says this makes server changes take effect immediately across clients and avoids duplicating logic in every client.
- He recommends REST principles, including stateless communication and resource identification.
- He says the architecture of a non-SPA follows the web itself rather than a framework’s model.
- He values server-side HTML rendering as an asset and says he does not trust the long-term maintainability of current client-side JavaScript frameworks.
- He notes that SPAs create coordination problems when multiple people or teams work on the same application.
- He says separate web applications can connect to one another through the web instead.
- He says server-side semantic HTML provides built-in accessibility support.
- He adds that JavaScript and Ajax still have a place as optional enhancements.
- He says JavaScript should extend browser capabilities, not drive the architecture.
- He concludes that SPAs usually bring no user benefit and that their supposed developer benefits are mostly illusory in the long run.
