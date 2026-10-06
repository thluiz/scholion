---
title: "Get Started With Vagrant On Windows — zamboni 0.8 documentation"
date: '2012-06-23T21:37:20-03:00'
category: webclip
summary: 'Guide to install Zamboni inside a Vagrant virtual machine on Windows, including VirtualBox, Git, Ruby, Vagrant, VM setup, SSH access, and starting the dev server.'
tags: ["vagrant", "windows", "zamboni", "virtualbox"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Get Started With Vagrant On Windows — zamboni 0.8 documentation"
    url: "http://mozilla.github.com/zamboni/topics/install-zamboni/vagrant-on-windows.html"
    kind: repo
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-06/mozilla-github-com--get-started-with-vagrant-on-windows-zamboni-0-8.md"
    kind: repo
---

This page explains how to set up Zamboni inside a Vagrant virtual machine on Windows. It walks through the required tools, getting the code, adjusting the Vagrantfile, starting the VM, and opening the development server in a browser. It also points to related setup pages for later steps.

## Reading notes

- Install Oracle VirtualBox first if it is not already on the machine.
- Install msysgit and choose the PATH, SSH, and line-ending options listed in Git Setup.
- Install RubyInstaller, add Ruby to the executable PATH, and install the Development Kit from the linked instructions.
- Install Vagrant with `gem install vagrant`, and use v0.9.6 or above on 64-bit Windows so VirtualBox is detected correctly.
- Clone the Zamboni repository with `git clone --recursive git://github.com/mozilla/zamboni.git`.
- Edit `Vagrantfile` so the host-only network line is enabled and the old 0.8.* line is commented out.
- Run `vagrant up` in the Zamboni folder to download and build the virtual machine.
- Use PuTTY and PuTTYgen to create an SSH session for the VM, with host `127.0.0.1`, port `2222`, username `vagrant`, and the generated private key.
- The first login can show long database migration output, and nothing should be done until the prompt returns.
- Start the dev server from the VM with `./project/vagrant/bin/start.sh`, then visit `http://33.33.33.24:8000/`.
- The page also notes extra configuration topics for MySQL, Memcached, RabbitMQ and Celery, Elasticsearch, Redis, and LESS CSS.
