---
title: "Generating Mazes in a Browser"
date: '2020-02-22T12:11:48+00:00'
category: webclip
summary: 'The post describes moving a maze generator from a console app to a browser-based .NET Core version, so it works better across platforms and lets users choose maze size, color, and algorithm.'
tags: ["dotnet-core", "browser-based-app", "maze-generation"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Generating Mazes in a Browser"
    url: "https://jeremybytes.blogspot.com/2020/01/generating-mazes-in-browser.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/jeremybytes-blogspot-com--generating-mazes-in-a-browser.md"
    kind: repo
---

The post revisits the Mazes for Programmers project and explains a shift from a console app that opened bitmaps with shell execute to a browser-based version that is friendlier to macOS and Linux. It points readers to the GitHub repo and notes that the bitmaps are generated in memory and streamed to the browser.

## Reading notes

- The project is based on Mazes for Programmers by Jamis Buck, with the book’s Ruby samples rewritten in C#.
- The earlier console approach used shell execute to show the maze bitmap, which worked on Windows but was not a good cross-platform solution.
- The new MazeWeb project shows a parameter page in the browser.
- The page lets the user choose maze size, color, and maze algorithm.
- Example outputs are shown for 50, Purple, Recursive Backtracker and for 150, Mustard, Aldous-Broder.
- Larger values take longer to generate, and the delay appears to come from bitmap creation rather than maze generation.
- A large output image is mentioned as 4500x4500 and about 2 MB when saved.
- The project uses .NET Core 3.1.
- In Visual Studio 2019, MazeWeb must be set as the startup project and selected in the Start Debugging dropdown instead of IIS Express.
- The site can also be run from the command line with dotnet run inside the MazeWeb folder.
- The author says there is still work to do, including default values on the parameter page and possible inefficiencies in bitmap generation.
