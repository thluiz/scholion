---
title: "Package Ruby Scripts as Executables with Ocra"
date: '2012-02-13T20:40:44-03:00'
category: webclip
summary: 'Ocra packages a Ruby script and its dependencies into a Windows .exe. The writer shows using `ocra quickcheck.rb --gem-full` to include the Whois gem and notes the resulting executable is larger and slower to start.'
tags: ["ruby", "windows-executable", "gems", "ocra"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Package Ruby Scripts as Executables with Ocra | Beginner Ruby"
    url: "http://www.beginnerruby.com/ruby-executables/package-ruby-scripts-as-executables-with-ocra/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-02/beginnerruby-com--package-ruby-scripts-as-executables-with-ocra.md"
    kind: repo
---

Ocra is described as a Ruby gem that packages a script and all of its dependencies into a Windows .exe. The post says the basic command is `ocra script.rb`, and that the tool runs the program while building it so it can detect which dependencies need to be included.

The writer uses a domain name availability script called Quickcheck as an example. After dependency problems with the Whois gem, the command `ocra quickcheck.rb --gem-full` is presented as the fix, though it makes the executable much larger. The resulting `Quickcheck.exe` works, but the post notes that it takes about 15 to 20 seconds to load and suggests experimenting with flags to reduce that delay.

## Reading notes

- Ocra packages a Ruby script and all dependencies into a Windows .exe.
- The basic command shown is `ocra script.rb`.
- Ocra runs the program while building it to detect required dependencies.
- The Quickcheck script needed the Whois gem.
- `ocra quickcheck.rb --gem-full` is used to include everything.
- The executable grows from 2kb to 1,493kb.
- The writer says the .exe works on other Windows computers without Ruby installed.
- The .exe loads slowly, with a black prompt screen for about 15 to 20 seconds.
- The writer wants to test different flags to reduce loading time.
