---
title: "Two Stack CMS"
date: '2014-10-07T09:11:00-03:00'
category: webclip
summary: 'The deck describes a global marketing site built with two separate software stacks for content creation and delivery to handle rich content, tool coordination, localization, high traffic, and high availability.'
tags: ["cms", "content-delivery", "localization", "high-availability"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Two Stack CMS"
    url: "http://martinfowler.com/articles/two-stack-cms"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-10/martinfowler-com--two-stack-cms.md"
    kind: repo
---

The deck describes a global marketing website for a manufacturer that needs design-heavy pages, graphics, video, interactive pages, and links to internal product systems. It also has to support many authoring tools, coordinate workflows across groups, and handle translation across more than twenty countries and nearly a hundred locales.

The response is to apply the editing-publishing separation pattern and build two distinct stacks of software for content creation and delivery. The deck says this architecture addresses integration between the stacks, secure preview of the live site, and the system’s evolution and scaling.

## Reading notes

- The site needs fresh, engaging pages with design-heavy structure, graphics, video, interactive pages, and links to internal systems for product specifications.
- Writers use a wide range of tools, both purchased and built in-house, so the system must support those tools and coordinate workflow between tools and groups.
- The global site must support over twenty countries and nearly a hundred locales, with imagery, product availability, and pricing varying by country.
- The site serves heavy traffic, with daily visitors in six figures and over two million daily page views.
- The site needs high availability and no downtime for frequent updates.
- The solution is to separate editing and publishing into two distinct software stacks for content creation and delivery.
- The deck also focuses on integration between the stacks, secure preview of the live site, and the evolution and scaling of the system.
