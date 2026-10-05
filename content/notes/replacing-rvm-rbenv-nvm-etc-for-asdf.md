---
title: "Replacing RVM/Rbenv/Nvm/etc for ASDF"
date: '2017-10-25T10:06:45-03:00'
category: webclip
summary: 'The page recommends ASDF as a single version manager for Ruby and many other languages, with setup steps, plugin management, local and global versions, and notes on reshimming and Ruby build issues.'
tags: ["asdf", "ruby", "version-manager", "nodejs"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Replacing RVM/Rbenv/Nvm/etc for ASDF | AkitaOnRails.com"
    url: "http://www.akitaonrails.com/2017/10/24/replacing-rvm-rbenv-nvm-etc-for-asdf"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2017-10/akitaonrails-com--replacing-rvm-rbenv-nvm-etc-for-asdf.md"
    kind: repo
---

The page recommends ASDF over RVM, Rbenv, NVM, and even Docker for managing language versions on a developer machine. It says ASDF can handle Ruby and many other languages with one command set, and explains how to install it, configure the shell, add plugins, and choose global or project-specific versions.

## Reading notes

- ASDF is presented as the author's main Ruby version manager and as a replacement for more familiar tools like RVM and Rbenv.
- The same tool is said to manage many languages, so the author says virtualenv for Python and NVM for Node.js are no longer needed.
- Installation is described as following the project's README, after installing the base development tools required by the environment.
- The setup includes cloning ASDF into `~/.asdf` and adding shell configuration for `asdf.sh` and completion scripts.
- The author lists several plugins already installed, including clojure, elixir, erlang, golang, python, ruby, and nodejs.
- Plugins can be updated together with `asdf plugin-update --all`.
- Available versions for a language can be listed with `asdf list-all`, and specific versions can be installed with `asdf install`.
- A global default version can be set with `asdf global`, and a project directory can use a different version with `asdf local`, which writes a `.tool-versions` file.
- If installed packages add executables that should be on the PATH, `asdf reshim` is needed.
- The page mentions compilation problems when installing Ruby versions before 2.4 and gives a command that uses gcc-5 and openssl-1.0.
- If an install fails because of a missing dependency, the author says the version should be removed manually before reinstalling.
- To show the current language version in the prompt, the page suggests using `asdf current ruby | awk -F' ' '{print $1}'`.
