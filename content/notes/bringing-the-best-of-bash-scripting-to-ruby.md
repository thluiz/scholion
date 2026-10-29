---
title: "Bringing the best of Bash scripting to Ruby (by @radekpazdera)"
date: '2015-07-16T04:03:08-03:00'
category: webclip
summary: 'The post argues for keeping Ruby scripts as quick to start as Bash, while gaining flexibility and reuse. It recommends docopt for CLI parsing and Scriptster for running commands and logging.'
tags: ["ruby", "bash", "docopt", "scriptster"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Bringing the best of Bash scripting to Ruby (by @radekpazdera)"
    url: "http://radek.io/2015/07/13/ruby-scripting/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-07/radek-io--bringing-the-best-of-bash-scripting-to-ruby.md"
    kind: repo
---

The post says Bash is fast for small tasks, but scripts become harder to maintain when they grow. Its goal is to keep the first version simple while leaving room for reuse and extension in Ruby.

## Reading notes

- Bash works well for small tasks because it is fast to write and run.
- As scripts grow, the author sees reuse and extensibility as more valuable.
- Docopt is presented as a simple way to define CLI arguments from a usage string.
- Scriptster is described as a small gem for running shell commands and logging what happens.
- Scriptster includes a wrapper for docopt, which reduces boilerplate when starting a Ruby script.
- The author suggests putting a small template command in a shell rc file so a new Ruby script can be created quickly.
- The setup aims to keep Ruby close to Bash speed for scripting while keeping Ruby available when the task grows.
