---
title: "Introducing the jQuery Mobile Metro Theme"
date: '2014-06-18T14:07:53-03:00'
category: webclip
summary: 'The post presents jQuery Mobile Metro as a stylesheet-based way to reuse the same markup for iOS and Metro UIs, then shows device detection and page tweaks for WP7.'
tags: ["jquery-mobile", "metro-theme", "html5-mobile", "windows-phone-7"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Introducing the jQuery Mobile Metro Theme"
    url: "http://www.scottlogic.com/blog/2012/04/30/introducing-the-jquery-mobile-metro-theme.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-06/scottlogic-com--introducing-the-jquery-mobile-metro-theme.md"
    kind: repo
---

The post introduces the jQuery Mobile Metro theme and shows how the same jQM markup can produce an iOS-style UI or a Metro UI by changing stylesheets. It also describes detecting Windows Phone 7 with the user agent string and switching themes for that device.

## Reading notes

- Microsoft Open Technologies backed jQuery Mobile Metro as part of its work on open source, standards, and interoperability.
- jQuery Mobile uses HTML annotated with data-role attributes, while its JavaScript adds the extra structure needed for styling and transitions.
- The framework can render an iOS-like interface and supports built-in mobile controls and AJAX page loading.
- Switching to the Metro look only requires referencing the Metro CSS theme and setting the page theme to dark.
- The SandwichFlow example uses the same structure to present sandwich recipes and list dividers that resemble a jump list in the Metro theme.
- The page can choose between themes by checking whether the browser string contains Windows Phone OS 7.5.
- Both themes can be included at once, with Metro loaded as an alternate stylesheet and activated by JavaScript when needed.
- A T4 template is used to generate individual recipe HTML files from XML data and add the files to the Visual Studio project.
- On WP7, a jQuery handler removes back buttons because the hardware back button is expected on that platform.
- The conclusion says jQM is simple and useful for quickly building mobile sites, but its dynamic behavior and some Metro controls still fall short of the native experience.
