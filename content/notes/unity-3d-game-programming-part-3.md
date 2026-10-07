---
title: "UNITY 3D – GAME PROGRAMMING – PART 3"
date: '2015-02-26T19:34:21-03:00'
category: webclip
summary: 'This third part of the series shows how to process keyboard input in Unity 3D, create primitives only after Space is pressed, and map keys to rotation and movement.'
tags: ["unity-3d", "keyboard-input", "game-programming"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "UNITY 3D – GAME PROGRAMMING – PART 3 - CodeProject"
    url: "http://www.codeproject.com/Articles/877371/UNITY-D-GAME-PROGRAMMING-PART"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-02/codeproject-com--unity-3d-game-programming-part-3.md"
    kind: repo
---

This third article in the series continues the Unity 3D walkthrough by focusing on user input from the keyboard. It explains how the Input Manager works, then shows how a script can create cube primitives only after Space is pressed and use other keys to rotate and move them.

## Reading notes

- The article is the third part of a Unity 3D series about getting started with 3D projects.
- It says the reader should already know programming, C#, object-oriented concepts, and basic 3D graphics and vector math.
- It notes that the article uses Unity 3D version 4.6.1.
- Unity handles inputs through the Input Manager, which is found under Edit > Project Settings > Input.
- The Input Manager lists built-in axis configurations such as Horizontal and Vertical.
- The article describes the important Input Manager fields as Name, Positive Button, Negative Button, Alt. Positive Button, Alt. Negative Button, Type, and Axis.
- The keyboard example creates three cube primitives after the Space Bar is pressed.
- The script uses Input.GetKey(KeyCode.Space) inside Update() to trigger CreateMyPrimitives().
- A boolean named PRIMITIVES_CREATED is used to prevent creating the primitives more than once.
- The article then refines the code so Update() checks PRIMITIVES_CREATED before either creating objects or applying rotation.
- It maps A to rotating Cube1 on the Y axis, B to rotating Cube2 on the X axis, and C to rotating Cube3 on the Z axis.
- It adds translation controls for Cube1 with the arrow keys: Up moves forward on Z, Down moves backward on Z, Left moves left on X, and Right moves right on X.
- The movement uses Translate with Vector3.forward, Vector3.back, Vector3.left, and Vector3.right multiplied by Time.deltaTime.
- The article closes by pointing to future UI topics and inviting the reader to practice with the provided source code.
