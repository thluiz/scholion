---
title: "WinDirStat"
date: '2017-03-17T12:20:11-03:00'
category: webclip
summary: 'WinDirStat is a Windows disk-usage viewer and cleanup tool. It scans a directory tree once and shows results in a directory list, treemap, and extension list.'
tags: ["windows", "disk-usage", "cleanup-tool"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "WinDirStat"
    url: "https://windirstat.net/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2017-03/windirstat-net--windirstat.md"
    kind: repo
---

WinDirStat is a disk usage statistics viewer and cleanup tool for Microsoft Windows. It reads the whole directory tree at startup and then shows the results in three views: a directory list sorted by file or subtree size, a treemap of the full tree, and an extension list with file type statistics.

The treemap draws each file as a colored rectangle whose area matches its size. Directories are shown as rectangles that contain their files and subdirectories, so their area matches the size of the subtree, and the color indicates file type.

## Reading notes

- Disk usage statistics viewer and cleanup tool for Microsoft Windows.
- On startup, it reads the whole directory tree once.
- The directory list is like Windows Explorer’s tree view, but sorted by file or subtree size.
- The treemap shows the whole contents of the directory tree straight away.
- The extension list serves as a legend and shows statistics about file types.
- Each file appears as a colored rectangle whose area is proportional to its size.
- Directories are rectangles containing their files and subdirectories, so their area is proportional to subtree size.
- The rectangle color indicates the file type as shown in the extension list.
- Cushion shading helps bring out the directory structure.
