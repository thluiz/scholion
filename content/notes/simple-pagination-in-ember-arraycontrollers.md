---
title: "Simple Pagination in Ember ArrayControllers"
date: '2014-01-12T14:08:23-03:00'
category: webclip
summary: 'The post builds pagination for an Ember ArrayController by adding page and perPage properties, deriving paginatedContent and pages, then moving the logic into a reusable mixin and a pagination-links component.'
tags: ["ember", "pagination", "arraycontroller", "components"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Simple pagination in Ember ArrayControllers - Resistor"
    url: "http://resistor.io/blog/2013/10/01/simple-pagination-in-ember-arraycontrollers/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-01/resistor-io--simple-pagination-in-ember-arraycontrollers.md"
    kind: repo
---

The post shows how to paginate a sorted Ember ArrayController by adding page and perPage, then computing paginatedContent from arrangedContent so the sort order is preserved. It also computes the total number of pages without depending on arrangedContent, since the count does not change when sorting changes.

The pagination logic is then extracted into a reusable mixin and displayed with a pagination-links component plus a pagination-page component. The component handles previous and next links, a centered window of visible pages, ellipses when needed, and actions that update controller.page.

## Reading notes

- Add page and perPage to control which slice of the collection is shown.
- Use arrangedContent for paginatedContent so sorting still applies.
- Compute pages from content.length and perPage, since sort order does not change the item count.
- Extract paginatedContent and pages into a reusable PaginatableMixin.
- Use a pagination-links component to render the navigation controls.
- Use a separate pagination-page component to keep the template simple and avoid extra divs inside Bootstrap markup.
- Give pagination-page a li tagName and disable the current page with class bindings.
- Handle page clicks by sending actions through parentView, since component actions do not bubble.
- Build visiblePages so it shows up to five page numbers, centered on the current page when possible.
- Show ellipses before or after the visible range when the full page list is larger than the window.
- Wire next, previous, and page selection actions to controller.page.
- The computed slice is noted as less performant for very large collections because it recreates arrays and does not use arrayComputed.
- The post also notes that large datasets should be paginated on the server side as well.
