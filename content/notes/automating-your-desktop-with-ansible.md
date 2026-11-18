---
title: "Automating your desktop with Ansible"
date: '2020-05-04T11:30:19+00:00'
category: webclip
summary: 'The author explains why he uses Ansible to keep the same desktop configuration across machines, from GNOME preferences and shell tools to installed apps, scripts, and hostname-specific setup.'
tags: ["ansible", "desktop-configuration", "gnome", "ubuntu"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Automating your desktop with Ansible"
    url: "https://dev.to/iancleary/automating-your-desktop-with-ansible-20jk"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--automating-your-desktop-with-ansible.md"
    kind: repo
---

The post describes a desktop setup built around Ansible so the same base configuration can be applied across machines without repeating manual setup. It covers GNOME settings, installed software, Makefile helpers, and a new-machine workflow driven by a shell script and Ansible playbooks.

## Reading notes

- The author wants to avoid thinking too much about setup when moving between machines and prefers the same base configuration everywhere.
- The idea came from learning infrastructure as code and applying it to a desktop environment.
- The path to Ansible went through bash scripts and Makefiles before settling on Ansible for configuration.
- Supported Ubuntu versions are 18.04 and 20.04, with no plans to support non-LTS releases.
- The script can check GNOME settings and change them when they differ from the desired state.
- Two example dconf tasks set modal dialogs to move independently and the clock format to 24-hour time.
- The post says these settings are managed with dconf and gsettings, with dconf-editor and gsettings as the related tools.
- The configuration also installs a long list of core software, including development tools, browsers, chat apps, media apps, and utilities.
- Makefiles are used to run existing Ansible roles or scripts and make editing or updating the configuration easier.
- The article shows a group_vars/all.yml file that stores versions, packages, snap apps, VS Code extensions, and zsh plugins.
- For an existing machine, the author points readers to separate documentation for the Makefile workflow.
- For a new machine, the setup uses a wget command piped to bash, then asks for sudo and Ansible become passwords.
- The script creates a private inventory file and a hostname-specific group_vars file so the playbook runs on that host name.
- After editing those files, the user runs make all.
- Documentation is hosted on Netlify, and the project is on GitHub under GPL-3.0.
