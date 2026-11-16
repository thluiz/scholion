---
url: "https://dev.to/iancleary/automating-your-desktop-with-ansible-20jk"
captured_at: "2026-11-16T20:00:52+00:00"
title: "Automating your desktop with Ansible"
domain: "dev-to"
---

Hello there,

First off, I hope you are doing well 😊.

* * *

When it comes to my laptop set up, I care about not having to think too much about my setup between machines. Especially when I want to get right to work, gaming, etc.

For that reason, it is very comfortable for me to have the same base configuration on each machine (look, feel, keyboard shortcuts, core software, etc.).

When I learned about infrastructure as code concept, I thought it would be a fun learning experience to try it on my desktop.

Here is my story of the ways I found to help configure and maintain my desktop configuration.

## [](#ansible-newbie-a-true-underdog-story)Ansible Newbie: A true underdog story

*   I found a cool bash script on the internet (_I didn't understand most of it_) 🤷
*   I modified cool bash script for my needs and it worked! 🚀
*   I learned about Makefiles. 😄
*   I proceeded to do everything with Makefiles. 🤩🤩🤩
*   I got tired of running successive Make targets over and again 😐.
*   I used Ansible at work and decided to take a course to learn more about it. 🤓
*   I put off actually taking the plunge to use Ansible. 🕒🕕🕘🕛
*   I finally took the plunge and decided to use Ansible for my configuration. ✔️

## [](#supported-ubuntu-lts-versions)Supported Ubuntu LTS Versions

*   Ubuntu 18.04
*   Ubuntu 20.04

> There are no plans to ensure non-LTS versions are supported.  
> Software support is LTS version dependent.

## [](#why-script-this)Why script this?

While these changes don't take long to do, we could have a script check and assert that they are set the way you want, and change them if they are different than your desired state.

Lets get into an example to see why I went this route.

### [](#gnome-settings-and-configuration)GNOME Settings and configuration

If you have ever install GNOME Tweak Tools, you've been exposed to some of these settings. The Settings application exposes some of them as well.

The settings are organized in a hierarchical manner

```


- name: GNOME Preferences - Shell - Attach Modal Dialogues
  dconf:
    key: "/org/gnome/shell/overrides/attach-modal-dialogs"
    value: "false"
    state: present

- name: GNOME Preferences - Nautilus - Clock Format
  dconf:
    key: "/org/gnome/desktop/interface/clock-format"
    value: "'24h'"
    state: present


```

Enter fullscreen mode Exit fullscreen mode

The two tasks above allow modal dialogues to be moved independently of the application (so you can see what is behind the dialog) and change the clock to 24 hour time.

The underlying tools that manage these settings are `dconf` and `gsettings`. The `dconf-editor` is a graphical application for editing these items. `gsettings` is a way to get, set, and query the schema of entries on the command line.

The two Ansible tasks use `dconf` to set the value for each key. The `state: present` flag tells ansible that we want the key/value pair to be present on our system.

## [](#what-else-can-be-configured-and-source-controlled)What else can be configured and source controlled

### [](#core-software)Core Software

This isn't exactly the list of Ansible roles,  
but below is a list of what the software installs.

*   `ansible`,
*   `cherrytree` (like OneNote for Linux)
*   [Breaktimer](https://snapcraft.io/breaktimer),
*   `Visual Studio Code`,
*   [kite AI Autocompletion and Docs for Python](https://kite.com/), runs locally
*   [VSCodium](https://vscodium.com/),
*   [carbon-cli](https://github.com/mixn/carbon-now-cli) for beautiful images of my code - right inside my terminal,
*   `Chromium`,
*   `docker`,
*   `docker-compose`,
*   [Flameshot](https://flameshot.js.org/#/),
*   Flameshot keybinding to the Print Screen key using `gsettings`,
*   `Firefox`,
*   `Flatpak`,
*   `gh` [GitHub CLI](https://github.com/cli/cli#installation-and-upgrading)
*   `Nordvpn`,
*   `nodejs`,
*   [Peek](https://github.com/phw/peek) animated GIF screen recorder,
*   [Postman](https://www.postman.com/) for API testing,
*   `Protonmail-bridge` [https://protonmail.com/bridge/install](https://protonmail.com/bridge/install),
*   `python3.6`,
*   `python3.7`,
*   `python3.8`,
*   `Signal Desktop`,
*   `Slack`,
*   `Snap`,
*   `Spotify`,
*   `Stacer` [https://github.com/oguzhaninan/Stacer](https://github.com/oguzhaninan/Stacer),
*   `Standard Notes`,
*   `Steam`,
*   `Sublime Text`,
*   `Telegram`,
*   `TickTick` using [nativefier](https://github.com/jiahaog/nativefier/),
*   `Timeshift` [https://github.com/teejee2008/timeshift](https://github.com/teejee2008/timeshift),
*   `Tresorit`,
*   `yarn`,
*   `zsh`

### [](#makefile-help-out)Makefile help out

I use Makefiles to help run existing Ansible roles or scripts to make editing/updating my configuration easier.

[![Makefile help output text for the repositories' code](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fvif9crocr2owz2jk5v65.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fvif9crocr2owz2jk5v65.png)

### [](#more-details)More details

To give you a sense of more details around what some of the make targets do, below is my `group_vars/all.yml` file at the time of this article.

This file sets global variables for all hosts I want to run the playbook on. In my case, this generally is just the local machine.

```


---
docker_compose_version: 1.25.4
flameshot_version: 0.6.0
flatpak_applications:
  - "com.uploadedlobster.peek"
  # - "com.github.alainm23.planner" # not used
  - "com.valvesoftware.Steam"
  - "org.gnome.Evolution"
  - "ch.protonmail.protonmail-bridge"
  - "org.libreoffice.LibreOffice"
gh_version: 0.7.0
jetbrains_mono_version: 1.0.3
protonmail_bridge_version: 1.2.6-1
nodejs_version: "12.x"
nodejs_yarn_global_packages:
  - name: "@vue/cli"
  - name: "@gridsome/cli"
  - name: "nativefier"
  - name: "markdownlint-cli"
  - name: "carbon-now-cli"
snaps_chat:
  - "signal-desktop"
  - "telegram-desktop"
snaps_chat_classic:
  - "slack"
snaps_common:
  - "snap-store"
  - "breaktimer"
  - "cherrytree"
  - "drawio"
  # https://github.com/jgraph/drawio-desktop/issues/138,
  # snap 12.6.5 > flatpak 12.4 (as of 2020-02-28)
  - "spotify"
  - "ncspot"
  - "standard-notes"
snaps_development:
  - "postman"
snaps_development_classic:
  - "code"
  # - "codium" # Code without telemetry
  - "sublime-text"
snaps_web_browsers:
  - "chromium"
  - "firefox"
snaps_web_browsers_plugs:
  - plug: "home"
    app: "chromium"
code_extensions:
  ## Ansible
  - vscoss.vscode-ansible

  ## Docker and Remote Development
  - ms-azuretools.vscode-docker
  - ms-vscode-remote.remote-containers
  - ms-vscode-remote.remote-ssh
  - ms-vscode-remote.remote-ssh-edit
  # - ms-vscode-remote.remote-wsl
  - ms-vscode-remote.vscode-remote-extensionpack

  ## General Development
  - christian-kohler.path-intellisense
  - vscode-icons-team.vscode-icons
  - riccardoNovaglia.missinglineendoffile
  - shardulm94.trailing-spaces
  # - Shan.code-settings-sync

  ## Git Utilities
  - eamodio.gitlens
  - donjayamanne.githistory

  ## Markdown Linting
  - DavidAnson.vscode-markdownlint

  ## Python Development
  - ms-python.python
  - himanoa.Python-autopep8
  - njpwerner.autodocstring
  - wholroyd.jinja
  # Pyright Attribution to tiangolo and florimondmanca
  # https://twitter.com/tiangolo/status/1252891149708275713?s=21
  # > Disabled type checking in the extension settings as I rely on mypy,
  # > but autoimport and unused import colouring alone make it a
  # > 100% worthwhile companion on VSCode
  - ms-pyright.pyright

  ## Spellchecking
  - streetsidesoftware.code-spell-checker

  ## Travis-CI
  # - felixrieseberg.vsc-travis-ci-status # has issues with status resolution

  ## Vue.js Development
  - octref.vetur
  - dbaeumer.vscode-eslint
  - pranaygp.vscode-css-peek

  ## YAML
  - redhat.vscode-yaml # doesn't allow hostname in .travis.yml
stacer_version: 1.1.0
zsh_theme: robbyrussell
zsh_plugins:
  - ansible
  - aws
  - docker
  - docker-compose
  - git
  - pipenv


```

Enter fullscreen mode Exit fullscreen mode

### [](#existing-machine)Existing Machine

For a walk through of my process on existing machine, please visit  
[https://ansible-desktop.iancleary.me/makefile](https://ansible-desktop.iancleary.me/makefile).

## [](#new-machine-setup)New Machine Setup

For a new machine, I run the following command  
to set up my computer:

> I like to do this during the initial configuration of the machine.

```


wget -qO- \
https://github.com/iancleary/ansible-desktop/raw/main/run.sh | \
bash


```

Enter fullscreen mode Exit fullscreen mode

This will prompt you for your `sudo` password  
for the bash script and then once later for  
`ansible`'s "BECOME PASSWORD" prompt.

Voila! 🎉🎉🎉

### [](#customization)Customization

If you want to edit the variables, hit `CTRL + C` at `ansible`'s "BECOME PASSWORD" prompt.

The script created two extra files that ensure that the `ansible-playbook` will on your host name.

> Note: Both files are intentionally not version controlled.  
> This allows hostname specific group\_vars relative to the playbook.

*   a private `.inventory` file

```


#.inventory
[$(hostname)]
127.0.0.1


```

Enter fullscreen mode Exit fullscreen mode

*   a group\_vars file

```


# group_vars/$(hostname)/all.yml
---
# You can copy and modify variables over from ../all.yml


```

Enter fullscreen mode Exit fullscreen mode

Then run `make all`

Voila (with your edits)! 🚀🚀🚀

## [](#documentation)Documentation

Detailed documentation is hosted by Netlify at [https://ansible-desktop.iancleary.me](https://ansible-desktop.iancleary.me/).

## [](#thanks)Thanks

I hope you enjoyed reading about my desktop configuration and feel free to use/modify/share.

[iancleary/ansible-desktop/](https://github.com/iancleary/ansible-desktop/) is on GitHub and licensed [GPL-3.0](https://github.com/iancleary/ansible-desktop/blob/main/LICENSE).

If you like it give it a star ⭐ and let me know if you have any questions!

> Especially if you a suggestion for cool application or piece of software you use 😎😎😎.

Cheers,  
Ian

Edit: Changed default branch from `master` to `main`
