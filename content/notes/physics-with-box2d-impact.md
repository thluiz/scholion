---
title: "Physics with Box2D - Impact"
date: '2013-05-13T09:23:36-03:00'
category: webclip
summary: 'The page explains how to use Box2D with Impact, from creating a world and stepping the simulation to scaling pixels into meters and defining Box2D-backed game entities and levels.'
tags: ["box2d", "impact", "physics", "game-development"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Physics with Box2D - Impact"
    url: "http://impactjs.com/documentation/physics-with-box2d"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-05/impactjs-com--physics-with-box2d-impact.md"
    kind: repo
---

The page introduces Box2D as a way to get more accurate physics in Impact, beyond its basic collision detection and response. It notes the JavaScript port, the namespace changes, and the module wrapper used so Box2D can load in Impact, then points to the Box2D 2.0.2 manual and a demo.

## Reading notes

- Box2D is presented as a physics engine for cases where Impact’s built-in collision handling is not enough.
- The JavaScript version used here comes from Jonas Wagner’s port, with Box2D classes placed under the `b2.` namespace.
- The page links to the Box2D 2.0.2 manual.
- A Box2D world is created with a bounding box, gravity vector, and `b2.World` instance.
- A body is added by defining a `b2.BodyDef`, creating the body in the world, and attaching a `b2.PolygonDef` shape.
- Box2D body positions use the object’s center, unlike Impact entities, which use the upper-left corner.
- `SetAsBox` takes half-width and half-height values, so the example box becomes 10 by 10 units.
- The physics simulation advances in the game update method with `b2.World.Step`, using `ig.system.tick` as the timestep.
- Box2D units are tuned for meters, so the page uses `b2.SCALE` to convert from pixels to meters.
- `ig.Box2DGame` and `ig.Box2DEntity` are described as helper classes that handle the integration work.
- `ig.Box2DGame.loadLevel()` builds physics objects from a collision map and combines adjacent tile regions into larger rectangles.
- The page says Box2D performance seems more tied to the number of collisions than the number of objects.
- `debugCollisionRects` can draw collision boxes as green outlines.
- `ig.Box2DEntity` creates a physics body sized like the entity and updates the entity position from the physics simulation.
- A crate entity can subclass `ig.Box2DEntity`, disable normal Impact collision handling, and use an animation sheet.
- Movement should use Box2D forces and impulses, with the example showing `ApplyForce` for a jetpack jump input.
