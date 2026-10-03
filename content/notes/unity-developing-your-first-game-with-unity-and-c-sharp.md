---
title: "Developing Your First Game with Unity and C#"
date: '2016-09-07T09:37:56-03:00'
category: webclip
summary: 'The article explains what Unity is, what it is not, and how its editor, scenes, GameObjects, components, and script lifecycle fit together for building and testing games across platforms.'
tags: ["unity", "c-sharp", "game-development", "cross-platform"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Unity - Developing Your First Game with Unity and C#"
    url: "https://msdn.microsoft.com/en-us/magazine/dn759441.aspx"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-09/msdn-microsoft-com--unity-developing-your-first-game-with-unity-and-c-sharp.md"
    kind: repo
---

The article presents Unity as a 2D and 3D engine and framework for building game and app scenes, with cross-platform export, scriptable editor workflows, and a large Asset Store. It also explains that Unity is not primarily an asset-creation tool, even though third-party modeling and terrain tools extend what you can do inside it.

## Reading notes

- Unity provides a system for designing 2D, 2.5D, and 3D scenes for games and apps.
- It supports visual components and code, and exports to major mobile platforms and other targets.
- The Unity Asset Store is described as a major source for artwork, models, audio, plug-ins, shaders, textures, and scripting tools.
- Unity is not, by default, an asset-creation tool like Maya, 3DS Max, Blender, or Photoshop.
- Microsoft and Unity work together for platform support across Windows standalone, Windows Phone, Windows Store, Xbox 360, and Xbox One.
- The editor runs on Windows, Linux, and OS X, and the same download can be used in free or pro mode.
- Unity code is written in C#, JavaScript/UnityScript, or Boo, while the engine itself is native C++.
- Game code runs on Mono or the .NET Framework, with iOS using AOT compilation instead of JIT.
- You can test a game in the IDE without exporting or building first.
- Unity uses MonoDevelop by default, but Visual Studio can be configured as the editor, with UnityVS for debugging.
- A Unity project is a folder-based project with Assets, Library, ProjectSettings, and Temp folders, and changes should be made through the editor rather than directly in the file system.
- Scenes hold the running content of a game, and a scene should be saved often.
- A GameObject is the base object in a scene, and its Transform controls position, rotation, and scale.
- Components add behavior and functionality to GameObjects, including rendering, audio, physics, particles, and scripts.
- A script component can be attached to a GameObject by dragging the script onto an object.
- MonoBehavior-derived classes commonly use Awake, Start, Update, and FixedUpdate.
- Update runs every frame, while FixedUpdate runs on a fixed timestep and is better for physics-related work.
- Unity creates code projects automatically for different script folders and compilation phases, including editor and firstpass assemblies.
- Building a game involves importing assets, writing code, testing in Unity, exporting to a platform, testing there, and deploying.
