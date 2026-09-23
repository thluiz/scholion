---
title: "Four Layer Architecture"
date: "2026-09-23T17:20:05+01:00"
category: webclip
has_commentary: false
summary: "A pattern from the c2 wiki splits client-server apps into View, ApplicationModel, DomainModel and Infrastructure, extending MVC to cover persistence and the outside world."
tags:
  - software-architecture
  - mvc
  - design-patterns
sources:
  - title: "Four Layer Architecture"
    url: "http://wiki.c2.com/?FourLayerArchitecture"
    kind: wiki
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/wiki-c2-com--four-layer-architecture.md"
    kind: repo
---

The pattern starts from a gap in MVC: it separates UI widgetry from domain objects, but says nothing about how the domain talks to the outside world (persistence, network protocols, whatever sits past the object model). Four Layer Architecture answers by splitting the application into View, ApplicationModel, DomainModel and Infrastructure, each with a distinct job and a boundary the next layer doesn't cross.

## Fichamento

- View holds the physical windows and widgets, plus any Controller classes; a window-builder tool generates most of it.
- ApplicationModel mediates between UI components and the domain, translating UI events into domain messages and driving navigation between screens.
- DomainModel is where the actual business objects live (orders, employees, sensors, whatever the problem calls for).
- Infrastructure wraps connections to entities outside the object world: SQL tables, serial ports, terminals, network brokers.
- Strict boundaries between layers increase reuse and let different teams own different layers, since the interfaces are fixed well before coding starts.
- The domain and application layers end up independent of both the windowing toolkit and the persistence mechanism chosen.
- The pattern's authors trace layering further back than MVC, citing Dijkstra's paper on the T.H.E. operating system as an early precedent.
