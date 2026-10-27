---
title: "jQuey fullCalendar plugin and repeatable events and tasks (Example)"
date: '2013-01-03T22:57:39-03:00'
category: webclip
summary: 'Explains how fullCalendar can load events with AJAX and custom feeds, then shows how to generate a repeating Monday meeting through an event source function.'
tags: ["fullcalendar", "jquery", "events", "repeatable-events"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "jQuey fullCalendar plugin and repeatable events and tasks (Example)"
    url: "https://coderwall.com/p/rti-rg"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-01/coderwall-com--jquery-fullcalendar-repeatable-events-example.md"
    kind: repo
---

The page presents fullCalendar as a jQuery plugin for displaying and managing events and tasks. It says the calendar can fetch event data with AJAX, be customized visually, and react to user actions such as clicking or dragging. It also notes that the plugin is open source and available under MIT or GPL v2.

The example shows how to add events with an events array, then explains that repeatable events can be created with an event source function. fullCalendar calls that function when it needs new data, passing start and end dates plus a callback. The sample generates a Monday morning meeting for each matching date in the requested range.

## Reading notes

- fullCalendar is a jQuery plugin for visually displaying and managing events and tasks.
- It can fetch events or tasks on the fly with AJAX and can use a custom feed format.
- The plugin is visually customizable and exposes hooks for user-triggered events like clicking or dragging.
- It is open source and dual licensed under MIT or GPL Version 2.
- Events can be passed as an events source object.
- Repeatable events can be generated with an event source function.
- fullCalendar calls that function when the user clicks prev or next or switches views.
- The function receives start and end Date objects and a callback.
- The example creates a Monday meeting at 10:00 am and returns the generated events through the callback.
