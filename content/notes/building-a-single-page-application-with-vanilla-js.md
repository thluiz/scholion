---
title: "Building a single page application with vanilla js"
date: '2026-09-25T01:18:28+01:00'
category: webclip
summary: 'The post refactors a PHP blog into a framework-free SPA, outlining routing, controllers, templates, API requests, and a folder structure built with HTML, CSS, and JS.'
tags: ["single-page-application","vanilla-js","routing","templates"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Building a single page application with vanilla js"
    url: "https://dev.to/vinay20045/building-a-single-page-application-with-vanilla-js/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--building-a-single-page-application-with-vanilla-js.md"
    kind: repo
---

The post describes refactoring a PHP blog into a single-page application without a framework. It keeps the site in HTML, CSS, and JS, uses markdown posts, and aims for mobile-friendly hosting on GitHub Pages or AWS S3.

It then breaks the app into a page shell, assets, posts, and uploads, with routing based on hashchange, controllers for business logic, templates for reusable markup, views exposed through the URL, and an XHR request helper for loading content.

## Reading notes

- Criticizes dependency on frameworks and advocates knowing and using plain JavaScript with better project structure.
- Reorganizes a PHP blog as a framework-free SPA, with the code available in the repository and a live demo.
- Defines the goals of avoiding page loads per post, writing posts in markdown, using only HTML, CSS, and JS, hosting on GitHub Pages or AWS S3, and maintaining mobile compatibility.
- Organizes the project into assets, index.html, posts, and uploads, separating CSS, images, config, init, controllers, templates, utils, and views.
- Uses hash-based routing for deep linking, bookmarking, and SEO, registering routing in the hashchange event.
- Puts business logic in the controllers, which manipulate views and build the home page content from the most recent posts.
- Reserves templates for reusable markup and leaves hrefs as the main exception to the rules of linkage between layers.
- Exposes views to the user and has one of them call a controller after fetching the post index by AJAX request.
- Implements requests with XMLHttpRequest, handling success and error with callbacks and noting CORS considerations.
- Says the site became fast in repaints, without perceptible jank, and that he still intends to create a site packer in Python to reduce network calls on the first load.
