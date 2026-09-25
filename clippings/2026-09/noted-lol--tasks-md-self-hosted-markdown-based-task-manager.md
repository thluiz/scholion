---
url: "https://noted.lol/tasks-md/?ref=dailydev"
captured_at: "2026-09-25T18:27:54+01:00"
title: "Tasks.md - Self-Hosted Markdown Based Task Manager"
domain: "noted-lol"
---

![Tasks.md - Self-Hosted Markdown Based Task Manager](https://noted.lol/content/images/2024/08/tasks.md-self-hosted-noted.jpg)

*   [Self Hosted Task Management & To-do Lists](https://noted.lol/tag/self-hosted-to-do-project-management/)
*   [Self Hosted Note-taking & Editors](https://noted.lol/tag/self-hosted-note-taking-apps/)

I'm completely honest when I say that organization just doesn't come naturally to me. Notes are scattered all over the place, reminders are stuck to random surfaces, and my calendars feel like wishful thinking rather than actual planning tools. It's as if my brain is a black hole for tasks and deadlines and anything that goes in seems to get sucked down and never makes it back out again! And let's be real, cloud-based solutions can be intimidating too. I get that they're supposed to make life easier, but I'm just not comfortable entrusting my entire life to some company's servers. So, what I really need is a self-hosted solution that lets me get organized (or at least pretend to!). And that's exactly what Tasks.md is, the perfect antidote to my organizational chaos!

## What is Tasks.md

[Tasks.md](https://github.com/BaldissaraMatheus/Tasks.md?ref=noted.lol) is a self-hosted, Markdown file-based task management board.

![](https://noted.lol/content/images/2024/08/tasks.md-noted-main.png)

## Tasks.md Core Features

**Design & Interface**

*   Craft your task management system with ease using our modern, responsive interface that adapts to any device as a PWA.
*   Create cards, lanes, and tags to organize your tasks in a way that suits your workflow

**Content Creation**

*   Write tasks as Markdown files for a seamless and enjoyable experience
*   Take advantage of the power of Markdown to add rich formatting and style to your task descriptions

**Installation & Customization**

*   Get started quickly with our easy-to-install single Docker image
*   Personalize your experience with light or dark themes that sync with your operating system settings
*   Choose from three default color themes (Adwaita, Nord, and Catppuccin) to match your unique style

**Flexibility & Integration**

*   Seamlessly integrate Tasks.md into your existing workflow using subpath-based reverse-proxy support with an environment variable for base path

## Install Tasks.md using Docker

To install Tasks.md on your server, use this Docker Compose stack, which makes the process easy to follow. If you're new to self-hosting, don't worry, we have guides available to help you [get started with self-hosting](https://noted.lol/get-started-self-hosting/). For information on the latest features and updates, refer to the [Tasks.md releases](https://github.com/BaldissaraMatheus/Tasks.md/releases?ref=noted.lol).

```
version: "3"
services:
  tasks.md:
    image: baldissaramatheus/tasks.md
    container_name: tasks.md
    environment:
      - PUID=1000
      - PGID=1000
      - Title=Noted Tasks
    volumes:
      - /path/to/tasks:/tasks
      - /path/to/config:/config
    restart: unless-stopped
    ports:
      - 3333:8080
```

Let's begin! Set up your task management system by adding lanes and cards. Organizing can be a enjoyable experience with Tasks.md.

![](https://noted.lol/content/images/2024/08/demo.gif)

Easily organize your tasks by dragging and dropping cards into different lanes. This simple feature makes task management a seamless experience.

Tasks.md offers an effortless approach to organization. Each lane you create serves as a corresponding directory on your filesystem, making it easy to navigate and manage. Additionally, each task is represented by a file, providing a clear and structured system for tracking and managing your tasks.

![](https://noted.lol/content/images/2024/08/directories-organization-1.png)

![](https://noted.lol/content/images/2024/08/directories-organization-2.png)

![](https://noted.lol/content/images/2024/08/directories-organization-3.png)

## Final Notes and Thoughts

If you're looking for Kanban-style task management software, Tasks.md is an excellent choice. It offers a minimalist approach that even those new to task management can easily use. For those who prioritize simplicity, Tasks.md is a great option that gets the job done without overwhelming features. Give it a try and discover how simple it is to manage your tasks!

Swing by the [Tasks.md GitHub repo](https://github.com/BaldissaraMatheus/Tasks.md?ref=noted.lol) and give it a star. If you have questions or would like to suggest new features, visit the issue tracker to get involved. Your feedback is important in helping to improve Tasks.md.

  [![Jeremy](https://www.gravatar.com/avatar/ab32df3785e9d1a2e15660d757cc9b5f?s=250&r=x&d=mp)](https://noted.lol/author/jeremy/)[Jeremy](https://noted.lol/author/jeremy/)

Hello! I'm Jeremy, the creative force behind Noted. With a blend of self-taught expertise in homelab tech and professional experience with Docker, I'm eager to connect with fellow innovators.

## Read Next

 ![How I Built a Voice-First AI Mirror You Can Run at Home](https://noted.lol/content/images/2026/01/PXL_20260106_130137218.MP.jpg)

6 min read

 ![Romm - Self-Hosted ROM Manager with EmulatorJS Baked In](https://noted.lol/content/images/2024/11/romm-self-hosted-noted.jpg)

6 min read

 ![Block Everything You Hate Online with AdGuard Home](https://noted.lol/content/images/2025/12/adguard-home-self-hosted-noted.jpg)

5 min read

 ![EverShelf - The AI-Powered, Self-Hosted Inventory Brain for Your Kitchen](https://noted.lol/content/images/2026/05/everShelf_Banner_noted.png)

3 min read

 ![Issued - Small, Fast, Self-Hosted Comic Library Server](https://noted.lol/content/images/2026/05/SCR-20260510-kdru.png)

4 min read

 ![Why I Built Vykar Backup: A Faster, Simpler Rust Backup Tool](https://noted.lol/content/images/2026/03/vykar-backup-simple.jpg)

5 min read

 ![Scanopy: Self-Hosted Network Scanner That Builds a Live Topology Map](https://noted.lol/content/images/2026/03/scanopy-self-hosted-network-topology-mapping-that-updates-itself.jpg)

4 min read

 ![OpenDroneLog: A Self Hosted DJI Flight Log Dashboard](https://noted.lol/content/images/2026/03/opendronelog-self-hosted-dji-log-dashboard.jpg)

4 min read

 ![HarborFM - Self-Hosted Podcast Creator](https://noted.lol/content/images/2026/03/harborfm-self-hosted-podcast-host-and-creator.jpg)

8 min read

 ![Self-Hosted Push Notifications with Ntfy on iOS](https://noted.lol/content/images/2025/10/ntfy-self-hosted-push-notifications-noted.png)

5 min read

## Subscribe to Noted

Subscribe to our newsletter to get news and reviews delivered to your inbox!
