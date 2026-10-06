---
title: "Making a Single Page App Without a Framework"
date: '2015-04-20T09:11:40-03:00'
category: webclip
summary: 'Tutorial that shows how to build a simple SPA with jQuery and Handlebars, using JSON data, hash-based navigation, filters, a single-product view, and an error state.'
tags: ["single-page-app", "jquery", "handlebars", "hashchange"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Making a Single Page App Without a Framework | Tutorialzine"
    url: "http://tutorialzine.com/2015/02/single-page-app-without-a-framework/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-04/tutorialzine-com--making-single-page-app-without-framework.md"
    kind: repo
---

The tutorial explains how a single page app keeps one URL while changing content through JavaScript. It uses jQuery and Handlebars instead of a framework, loads product data from a JSON file, and uses the hash plus the hashchange event to move between states without reloading.

## Reading notes

- A SPA loads the needed code once and updates content dynamically through JavaScript, avoiding reloads unless the user refreshes the page manually.
- The example avoids a framework and relies on jQuery for DOM and events, plus Handlebars for templates.
- Product data comes from products.json, which can later be replaced by a server-side script connected to a real database.
- The app keeps one URL and uses the hash part to store state, so browser history still works and links can be shared.
- The HTML separates the interface into three states: all-products, single-product, and error.
- The all-products view renders a product grid from Handlebars templates and supports checkbox filters.
- The single-product view is filled only when the matching hash is reached.
- The render function reads the hash, hides the current page, and chooses which state to show.
- The homepage clears filters, unchecks the boxes, and shows all products.
- The product hash reads the selected product index and shows the single-product page.
- The filter hash parses the JSON query, applies the filters, and updates the visible products.
- generateAllProductsHTML compiles the template once on load and binds clicks on products to update the hash.
- renderProductsPage hides all list items, then reveals the ones whose ids match the filtered data.
- renderSingleProductPage searches the product list, fills the preview with the chosen product, and shows the page.
- renderFilterResults iterates through the allowed criteria, narrows the product set, and keeps the checkboxes in sync.
- createQueryHash writes the filters object into the hash when filters exist, or returns to the homepage hash when they do not.
