---
url: "https://dev.to/shelob9/a-few-things-i-do-every-time-i-start-a-new-gatsby-site-5gd"
captured_at: "2026-11-16T00:47:00+00:00"
title: "A Few Things I Do Every Time I Start A New Gatsby Site"
domain: "dev-to"
---

[![Cover image for A Few Things I Do Every Time I Start A New Gatsby Site](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fthepracticaldev.s3.amazonaws.com%2Fi%2Fbbv0za6zszoo3jlaor2c.jpg)](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fthepracticaldev.s3.amazonaws.com%2Fi%2Fbbv0za6zszoo3jlaor2c.jpg)

[![Josh Pollock](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F63421%2F1ce6f212-f8bc-417a-b61e-92a6743899dd.jpg)](https://dev.to/shelob9)

I'm a big fan of Gatsby.js. It powers [my blog](https://joshpress.net/) and a my other random sites. I've been trying our some starters recently -- trying out [TinaCMS](https://tinacms.org/) and [to display my dev.to posts on my own domain](https://github.com/geocine/gatsby-starter-devto).

I started keeping a list of what I do every time I start a Gatsby site, so I'll remember next time, and thought I would share.

## [](#upgrade-all-of-the-dependencies)Upgrade All Of The Dependencies

There are so many cool Gatsby starters out there. It makes starting up a site fairly painless and saves a ton of time. Before I start working with a starter, I like to set all of the dependencies to the latest versions. I use [my favorite yarn command](https://yarnpkg.com/lang/en/docs/cli/upgrade-interactive/) for this:  

```
yarn upgrade-interactive --latest
```

Enter fullscreen mode Exit fullscreen mode

This might break everything. I'd like to know early on if using a starter is going to force me to stick with an out of date version of Gatsby, React, etc or take work to update.

## [](#use-yarn)Use Yarn

I prefer yarn to npm. I run a find and replace in package.json for "npm run" and replace it with "yarn". I also delete package.lock.

## [](#add-a-language-attribute)Add A Language Attribute

When I look at a demo of a Gatsby starter, I always use the [aXe accessibility tester Chrome extension](https://chrome.google.com/webstore/detail/axe-web-accessibility-tes/lhdoppojpmngadmnindnejefpokejbdd?hl=en-US) to make sure I'm not going to end up with a ton of bugs to fix in the generated HTML. **Almost** all the time, I see this violation:  

```
<html> element must have a lang attribute
```

Enter fullscreen mode Exit fullscreen mode

This issue is considered serious and is [explained in depth here](https://dequeuniversity.com/rules/axe/3.4/html-has-lang?application=AxeChrome). It has a simple fix in most Gatsby starters and themes.

Presuming that [Helmet](https://github.com/nfl/react-helmet/) is being used, you can use an `htmlAttributes` prop to set an attribute on the `<html>` element:  

```
<Helmet title={config.siteMetadata.title} htmlAttributes={{ lang: 'en' }} />
```

Enter fullscreen mode Exit fullscreen mode

## [](#add-some-plugins)Add Some Plugins

Gatsby plugins are super helpful. I always want to try and get the benefits of offline caching of a PWA and the security of implimenting CSP headers, so I add these two plugins:

*   [Content Security Policy](https://www.gatsbyjs.org/packages/gatsby-plugin-csp/)
*   [Offline](https://www.gatsbyjs.org/packages/gatsby-plugin-offline/?=offline)

Here is [a good article](https://alligator.io/gatsbyjs/gatsby-pwa/) on PWAs and Gatsby.

## [](#what-else-do-you-do)What Else Do You Do?

That's my list, for now.

> What did I miss? [Let me know on Twitter @Josh412](https://twitter.com/josh412) or leave a comment 👇
