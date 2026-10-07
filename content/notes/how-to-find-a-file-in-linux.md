---
title: "How to find a file in linux"
date: '2012-08-02T10:27:57-03:00'
category: webclip
summary: 'The page shows the basic `find` command in Unix-like systems, with examples for searching the whole root filesystem or a specific directory for a file named `testing.txt`.'
tags: ["linux", "find-command", "file-search"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to find a file in linux"
    url: "http://www.mkyong.com/linux/how-to-find-a-file-in-linux/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-08/mkyong-com--how-to-find-a-file-in-linux.md"
    kind: repo
---

The page explains that in Unix-like systems you can use the `find` command to locate a file. It gives the basic pattern `find {directory-name} -name {filename}` and then shows two uses: searching from `/` when you do not know where the file is, and searching inside a specific directory such as `/Users/mkyong`.

## Reading notes

- Use `find {directory-name} -name {filename}` to search for a file.
- To search the whole system, run `sudo find / -name 'testing.txt'`.
- Searching from `/` may require permission, so the example uses `sudo`.
- To search only within one directory and its subdirectories, run `sudo find /Users/mkyong -name 'testing.txt'`.
