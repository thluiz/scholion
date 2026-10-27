---
title: "Programming JavaScript Applications — Internationalization (chapter 6)"
date: '2013-07-13T11:11:02-03:00'
category: webclip
summary: 'The text defines internationalization as preparing strings, numbers, dates, and currency for localization. It argues that support should be planned from the start and often handled with libraries like Globalize, Moment.js, or i18next.'
tags: ["internationalization", "localization", "globalize", "javascript"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Programming JavaScript Applications — Internationalization (chapter 6)"
    url: "http://chimera.labs.oreilly.com/books/1234000000262/ch06.html#internationalization"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-07/chimera-labs-oreilly-com--programming-javascript-applications-internationalization.md"
    kind: repo
---

The text defines internationalization as converting strings, numbers, dates, and currency into localized forms. It says the best time to prepare for translation is at the start of development, when templates are being built, and recommends using libraries instead of writing a custom solution.

## Reading notes

- Internationalization and localization convert text strings, numbers, dates, and currency into localized languages and representations.
- The text says expansion to other cultures is often the easiest way to grow a user base once a product nears saturation in one country or culture.
- Translation support should be planned from the beginning, because adding it later means finding every user-facing string and supporting it after the fact.
- Any string shown to the user should be passed through a translation function first.
- The text recommends using a library rather than rolling a custom translation solution.
- Moment.js is suggested for dates and i18next for strings.
- Globalize is presented as a thorough solution for strings, numbers, currency, percentages, and dates.
- Globalize uses a comprehensive locale database and does not require jQuery.
- CLDR is described as the closest comparable source of locale data, and the text notes that it is used by companies such as Apple, Google, IBM, and Adobe.
- The text mentions twitter-cldr-js as another option if Twitter's supported locales are acceptable, though it depends on Ruby.
- The recommendation at the end is to use Globalize.
- In the section on process resilience, the text says servers crash, logs should be written, the server should shut down, and a new instance should be launched.
- Node's cluster module, forever, and other monitoring tools are mentioned as ways to detect crashes and restore service.
- Separation of concerns is defined as giving each module or layer one responsibility and keeping unrelated code out of it.
- The text links separation of concerns to modular design and to application-wide layering, including n-tier and MVC architectures.
- Functions, modules, controls, widgets, layers, tiers, and services are all presented as possible units of concern.
- Controls are reusable GUI inputs such as combo boxes, calendar inputs, sliders, buttons, switches, and knobs.
- Widgets are small applications intended to be embedded in other applications.
- Layers are logical groupings of functionality, such as a data layer or a presentation layer.
- Tiers are the runtime environments where layers are deployed, and they should remain independent enough to move to separate machines or data centers.
- For large applications, tiers should be able to scale horizontally by adding machines.
- The modularity section says modules should be specialized, independent, decomposable, recomposable, and substitutable.
- The design principles listed for methods are KISS, DOT, and DRY.
