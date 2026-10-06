---
title: "How to master the art of Git"
date: '2017-04-04T12:18:09-03:00'
category: webclip
summary: 'The article explains what Git is, how GitHub fits in, and the basic workflow of cloning, checking status, staging, committing, pushing, pulling, and reverting changes.'
tags: ["git", "github", "version-control"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to master the art of Git"
    url: "https://dev.to/raha198/how-to-master-the-art-of-git"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2017-04/dev-to--how-to-master-the-art-of-git.md"
    kind: repo
---

The article introduces Git as version control software and GitHub as a place to store and view repositories online. It is aimed at aspiring developers and college freshmen, and it focuses on the basic commands used to learn Git faster.

It walks through creating a repository, cloning it to a local machine, checking file status, staging changes with `git add`, committing with a message, pushing to GitHub, pulling updates, and undoing mistakes with `git checkout` and `git reset --hard`.

## Reading notes

- Git is described as version control software that lets developers see versions of their code and track changes, revisions, and improvements.
- GitHub is presented as a hub for repositories, where code can be stored and viewed online.
- The article recommends installing Git, creating a GitHub account, and making a new repository before working locally.
- Cloning is explained as copying the repository from GitHub to the computer and linking the local folder to the origin repository.
- `git status` is presented as the main command for seeing edited files and the difference between the origin and the local working directory.
- `git add -A` stages all changed files, while `git add <file>` lets the user choose files one by one.
- `git commit -m "meaningful messages"` stores the staged files in a new commit with a message.
- `git push` uploads committed changes to GitHub, and `git pull` brings the latest version of the code base to the local machine.
- The article advises checking status often, changing only the files you want, staging changes carefully, committing before pushing, and pulling before pushing.
- `git checkout -- pineapple.txt` is shown as a way to discard unwanted changes in a file.
- `git reset --hard` is shown as a way to discard all changes since the last commit.
