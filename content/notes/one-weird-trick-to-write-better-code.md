---
title: "One Weird Trick to Write Better Code"
date: '2016-01-02T14:03:36-03:00'
category: webclip
summary: 'The page shows the full interface of a large idEntity class, with many fields and methods grouped by responsibility, exposing how much gameplay, rendering, sound, physics, networking, and scripting it manages.'
tags: ["code-structure", "game-engine", "idtech"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "One Weird Trick to Write Better Code · Evan Todd"
    url: "http://etodd.io/2015/09/28/one-weird-trick-better-code/?utm_content=buffere19c0&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-01/etodd-io--one-weird-trick-to-write-better-code.md"
    kind: repo
---

The page presents the interface of `idEntity` and shows how much responsibility a single game object can carry. The class includes state, flags, targets, health, binding, physics, damage handling, scripting, GUI hooks, networking, and snapshot support, along with the methods that manage each part.

## Reading notes

- The class stores core identity data such as entity number, entity definition number, name, spawn arguments, and script object.
- It tracks behavior and state with fields like think flags, dormant state, cinematic state, health, and many entity flags.
- It supports rendering through render views, render entities, model and skin control, shader parameters, overlays, and visual updates.
- It supports animation and sound through animator access, sound playback, sound emitters, volume updates, and listener IDs.
- It handles binding and teams with methods for joining, binding to joints or bodies, converting coordinates, and getting master or team entities.
- It wraps physics operations such as setting the physics object, running physics, interpolating physics, setting origin and axis, and reacting to collision and impulses.
- It exposes damage and pain callbacks, including damage application, effects, feedback, pain, and killed notifications.
- It includes scripting, GUI, target activation, teleportation, trigger touch, and event methods for networked state and client interpolation.
