---
title: "Tasks.md - Self-Hosted Markdown Based Task Manager"
date: '2026-09-25T18:27:54+01:00'
category: webclip
summary: 'Tasks.md is a self-hosted task board that stores tasks as Markdown files, organizes them into cards and lanes, and offers Docker setup, themes, and reverse-proxy support.'
tags: ["self-hosted-task-management", "markdown", "docker", "kanban"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Tasks.md - Self-Hosted Markdown Based Task Manager"
    url: "https://noted.lol/tasks-md/?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/noted-lol--tasks-md-self-hosted-markdown-based-task-manager.md"
    kind: repo
---

Tasks.md is presented as a self-hosted, Markdown file-based task management board. The page frames it as a simple Kanban-style option for people who want local control, with tasks stored as files and organized into lanes and cards.

It highlights a modern responsive interface, PWA support, Markdown task content, a single Docker image for installation, light and dark themes that follow system settings, three default color themes, and subpath-based reverse-proxy support.

## Reading notes

- Self-hosted task management board based on Markdown files
- Tasks are organized with cards, lanes, and tags
- Works as a responsive PWA
- Tasks are written as Markdown files
- Installable with a single Docker image
- Supports light and dark themes that sync with system settings
- Includes Adwaita, Nord, and Catppuccin as default color themes
- Supports subpath-based reverse proxy setup through an environment variable
- Each lane maps to a directory on the filesystem
- Each task is represented by a file
