---
title: "Ember pagination full example"
date: '2014-01-12T14:07:03-03:00'
category: webclip
summary: 'The post shows a full Ember.js RC1 pagination setup using a custom mixin, an ArrayController, a pagination view, routes for page selection, and Handlebars templates to render prev, next, and page links.'
tags: ["emberjs", "pagination", "arraycontroller", "routes"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "ember.js - Ember pagination full example - Stack Overflow"
    url: "http://stackoverflow.com/questions/13008838/ember-pagination-full-example"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-01/stackoverflow-com--ember-pagination-full-example.md"
    kind: repo
---

The post shows how to build pagination in Ember.js RC1 by adding a custom mixin, because the core did not include one. The mixin computes page lists, current, next, and previous pages, the total number of available pages, and the slice of content for the selected page.

It then applies that mixin to an ArrayController with itemsPerPage set to 2, adds a small view to render page numbers as list items, and wires routes so page selection updates selectedPage. The Handlebars templates render the table, Prev and Next links, and the page-number links.

## Reading notes

- The example works with Ember.js RC1.
- A pagination-like mixin is created because Ember core does not provide one yet.
- pages builds an array of page_id values from availablePages.
- currentPage reads selectedPage and falls back to 1.
- nextPage returns the next page when it is within availablePages, otherwise it returns the current page.
- prevPage returns the previous page when it is above 0, otherwise it returns the current page.
- availablePages is calculated from content.length divided by itemsPerPage and rounded up.
- paginatedContent slices content using the selected page and itemsPerPage.
- PersonController extends Ember.ArrayController with Ember.PaginationMixin and sets itemsPerPage to 2.
- PaginationView uses templateName pagination and tagName li.
- The router nests person.page under person.
- PersonPageRoute sets the person controller selectedPage from params.page_id.
- PersonRoute sets selectedPage to 1 and returns PersonApp.Person.find().
- The template loops through controller.paginatedContent to render rows.
- Prev and Next use linkTo with person.page and target controller.
- The pagination template links each page number to person.page.
- A GitHub repository is linked as a full working project.
