---
title: "Install Oh My ZSH on Ubuntu 14.04"
date: '2026-09-27T00:27:39+01:00'
category: webclip
summary: 'The gist lists the commands to install ZSH and Git, run the Oh My ZSH installer, check the ZSH path, and switch the login shell to ZSH.'
tags: ["zsh", "ubuntu-14-04", "oh-my-zsh", "git"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Install Oh My ZSH on Ubuntu 14.04"
    url: "https://gist.github.com/richardtape/269b3c1500fc46049a5d"
    kind: repo
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/gist-github-com--install-oh-my-zsh-on-ubuntu-14-04.md"
    kind: repo
---

The gist gives a short command sequence for setting up Oh My ZSH on Ubuntu 14.04. It first checks the current shell, then installs zsh and git-core, runs the Oh My ZSH installer, verifies the zsh path, and changes the login shell to /bin/zsh or the path returned by which zsh.

## Reading notes

- Check the current shell with echo $0 before changing anything
- Install zsh with sudo apt-get install zsh
- Install Git with sudo apt-get install git-core
- Install Oh My ZSH with curl -L http://install.ohmyz.sh | sh or with the wget command that pipes the installer into zsh
- Use which zsh to find the installed shell path
- Run chsh, enter the sudo password, and set the shell to /bin/zsh or the path found earlier
