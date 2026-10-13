---
title: "13 Factors to Consider While Choosing a JavaScript Charting Library"
date: '2015-03-29T20:36:13-03:00'
category: webclip
summary: 'The article lists practical criteria for choosing a charting library, from browser and device support to customization, performance, export options, pricing, support, and the risks of small open source projects.'
tags: ["javascript", "charting-library", "dataviz", "open-source"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "13 Factors to Consider While Choosing a JavaScript Charting Library"
    url: "http://davidwalsh.name/13-factors-choosing-javascript-charting-library"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-03/davidwalsh-name--13-factors-to-consider-while-choosing-a-javascript-charting-.md"
    kind: repo
---

The article says choosing a charting library starts with the needs of the application: target devices, time available, and what the dataviz must achieve. It then walks through factors such as browser and device compatibility, input formats, customization, chart variety, learning curve, integration with other code, performance, export features, design, licensing, support, and open source maturity.

## Reading notes

- The choice should match the target audience, especially when older browsers like older IE versions still matter.
- Responsive behavior matters when the application must work well on mobile and desktop.
- JSON is becoming standard, but XML support can still be necessary.
- The author treats customizability as a major decision factor, including custom shapes, legends, events, drill-down, and themes.
- The library should include the chart types the project needs, or offer the right bundle for the use case.
- A steep learning curve can be a problem on a tight deadline or for first-time users.
- Some libraries or wrappers can generate the JavaScript and HTML needed for charts, which helps when the developer is not strong in JavaScript.
- Performance depends on library size, memory use, garbage collection, and repaint cycles, but speed alone should not decide the choice.
- Export support matters for dashboards and reports, especially for PDF, image, and SVG output.
- Good design includes built-in interactivity, such as pie slices pulling out on click and legend toggles in multi-series charts.
- Licensing depends on user count, application type, and server count, so permissions should be checked before buying.
- Support may need to come from personal help, forums, or community sites, and tighter schedules may justify a commercial component.
- Small open source charting libraries can be abandoned, so project longevity matters before adopting one.
