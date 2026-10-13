---
title: "Remote visual debugging with RubyMine"
date: '2013-02-19T08:28:00-03:00'
category: webclip
summary: 'The post explains how to set up remote visual debugging for Ruby and Rails apps in RubyMine with Vagrant: forward a port, install debugger gems, configure remote roots, and run Rails through rdebug-ide.'
tags: ["ruby", "rubymine", "vagrant", "rails"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Žiga : Remote visual debugging with RubyMine"
    url: "https://coderwall.com/p/fus7na"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-02/coderwall-com--remote-visual-debugging-with-rubymine.md"
    kind: repo
---

The post says virtual machines do not have to get in the way of visual debugging for Ruby and Rails development with RubyMine. It lays out the setup needed to debug a Rails app running on a VM from the IDE.

## Reading notes

- Use Vagrant for projects, then forward port 1234 in the Vagrantfile.
- Install the ruby-debug-ide and debugger gems on the VM server.
- Create a Ruby remote debug run configuration in RubyMine and set the remote root and local root folders correctly.
- Start the Rails app with rdebug-ide on the VM, using host 0.0.0.0 so it listens on port 1234.
- Set breakpoints in RubyMine by clicking in the gutter next to the line you want to inspect.
- The debugger stops on that line when the matching request reaches the running app.
