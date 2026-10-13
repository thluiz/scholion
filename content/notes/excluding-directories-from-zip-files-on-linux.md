---
title: "Excluding directories from zip files on Linux"
date: '2013-05-20T10:50:12-03:00'
category: webclip
summary: 'The post says File Roller cannot easily exclude directories from a zip archive, so the author switches to the command-line zip utility and uses the -x option to leave out Mercurial and NetBeans files.'
tags: ["zip", "linux", "command-line", "file-roller"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Excluding directories from zip files on Linux : David R. Heffelfinger"
    url: "http://www.ensode.net/roller/dheffelfinger/entry/excluding_directories_from_zip_files"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-05/ensode-net--excluding-directories-from-zip-files-on-linux.md"
    kind: repo
---

The post describes a need to package source code in zip files while leaving out files and directories that should not be distributed. The examples given are Mercurial's .hg folder and NetBeans-specific project files and folders.

It says File Roller can create archives easily, but it does not provide an easy way to exclude directories. The solution is to use the command-line zip utility with the -x switch and list the paths to omit.

## Reading notes

- Source code is often turned in as zip files.
- The project uses plain ANT build files and is loaded into NetBeans as a free form project.
- NetBeans creates its own folders and files for the project.
- Mercurial creates an .hg folder that should not be distributed.
- File Roller is used on Linux to create zip files.
- File Roller does not easily exclude files or directories from the archive.
- Deleting unwanted directories after archiving leaves the directory entry in the zip file.
- The command-line zip utility can exclude files and directories with the -x switch.
- The example command zips a directory while excluding .hg, nbproject, and catalog.xml.
