---
title: "Using Symlinks in Windows Vista"
date: '2012-05-26T02:40:55-03:00'
category: webclip
summary: 'The article explains Vista’s mklink command, the difference between soft links, hard links, and directory junctions, and notes limits such as network shares and safe deletion.'
tags: ["windows-vista", "mklink", "symbolic-links", "directory-junctions"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Using Symlinks in Windows Vista - How-To Geek"
    url: "http://www.howtogeek.com/howto/windows-vista/using-symlinks-in-windows-vista/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-05/howtogeek-com--using-symlinks-in-windows-vista.md"
    kind: repo
---

Windows Vista adds symbolic links with the mklink command. The post shows the basic syntax, gives an example of mapping one folder path to another, and separates the options for directory symbolic links, hard links, and directory junctions. It also says hard links point directly to a file, while soft links act more like shortcuts.

## Reading notes

- mklink is used from the command line to create symbolic links
- /D creates a directory symbolic link, or soft link
- /H creates a hard link and is used for files
- /J creates a Directory Junction for directories
- a hard link points directly to the file and acts to the operating system as if it is the file itself
- a soft link works more like a shortcut to a file or folder
- Vista symlinks cannot be used from another operating system or from a network share
- deleting a symlink means deleting the link, not the original file
