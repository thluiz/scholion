---
title: "3D modeling for UI Designers"
date: '2016-05-02T10:03:01-03:00'
category: webclip
summary: 'The article introduces a simple Maya workflow for UI designers, covering polygon mode, primitives, transform tools, camera navigation, and basic modeling steps to build a factory icon and its door details.'
tags: ["3d-modeling", "maya", "ui-design", "polygons"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "3D modeling for UI Designers — The HE:journal"
    url: "https://journal.helabs.com/3d-modeling-for-ui-designers-3c59a75caad0#.d6zeevyvv"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-05/journal-helabs-com--3d-modeling-for-ui-designers-the-he-journal.md"
    kind: repo
---

The article says it is based on an interactive isometric map built at HE:labs, where each building stood for a project and showed a short looping animation on mouse over. It presents a simple approach to creating 3D images and animations for apps in Maya, and says the tutorial is split into three parts: 3D models, rendering, and simple 3D animations.

## Reading notes

- The tutorial uses Maya 2015 and notes that the interface changes between versions, so using the same version helps follow along.
- For modeling objects, the dropdown in the top left should be set to polygons.
- The Create > Polygon primitives menu includes basic objects such as cubes, spheres, and cylinders.
- Creating a primitive adds an input in the Channel box/Layer editor, where attributes like width, height, and depth can be changed.
- The left-side tools are used to translate, rotate, and scale objects.
- Those same tools can be applied to vertices, edges, and faces after changing the selection mode with a right click.
- The default four-camera viewport can be changed to a single perspective panel through Panels > Layouts > Single Pane.
- Camera movement uses Alt plus middle mouse drag, and Alt plus left drag rotates the camera.
- Pressing F frames the selected object in the camera.
- To model the factory icon, the tutorial starts from a cube and adds edge ring splits to create divisions for the roof.
- The top faces are extruded to form the roof, Keep Faces Together is turned off, and Offset is increased.
- Deleting one edge from each roof section creates a triangle shape.
- The door starts from a cube as well, then the front face is extruded and offset to make the trim.
- Mesh > Separate > Extract is used to detach the front face from the trim so the door can be modeled separately.
- Metal bars for a rolling door are made with edge ring and split, followed by extrusion.
- Once one door is finished, it can be duplicated with Ctrl + D.
