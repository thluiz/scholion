---
title: "UNITY 3D – GAME PROGRAMMING – PART 2"
date: '2015-02-26T19:34:17-03:00'
category: webclip
summary: 'The article expands on Unity 3D basics with Transform use, scripted rotation of cubes, dynamic primitive creation, and adding light to improve how the scene renders.'
tags: ["unity-3d", "game-programming", "transform", "lighting"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "UNITY 3D – GAME PROGRAMMING – PART 2 - CodeProject"
    url: "http://www.codeproject.com/Articles/876478/UNITY-D-GAME-PROGRAMMING-PART"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-02/codeproject-com--unity-3d-game-programming-part-2.md"
    kind: repo
---

The article continues the series by moving from basic editor use to more scripting in Unity 3D. It focuses on Transform for position, rotation, and scale, shows how to rotate cubes on different axes, and then creates cubes dynamically in code before adding a light source to the scene.

## Reading notes

- It assumes familiarity with programming, C#, object-oriented concepts, and basic 3D graphics and vector math.
- It uses Unity 3D version 4.6.1 and notes that the UI pipeline changed in that version.
- It reviews Transform as the component for storing and changing position, rotation, and scale.
- It shows three cube primitives placed at (0,0,0), (3,0,0), and (-3,0,0).
- It assigns separate scripts to rotate Cube1 on the Y axis, Cube2 on the X axis, and Cube3 on the Z axis.
- It then presents a single script that creates three more cubes in Start() and positions them at (0,2,0), (3,2,0), and (-3,2,0).
- It explains that CreatePrimitive(PrimitiveType.Cube) instantiates a cube and that localPosition is used to move it.
- It says the script can be attached to the camera because it does not modify the object it is attached to.
- It lists four light types available in Unity 3D: Directional Light, Point Light, Spotlight, and Area Light.
- It uses a Point Light placed at (0, 1.5, 3.5) to light the scene and show the result at design time and runtime.
- It ends by telling the reader to keep practicing and review C# basics if needed.
