---
title: "UsingTheJRubyDebugger"
date: '2012-04-15T19:23:43-03:00'
category: webclip
summary: 'Explains how to use the JRuby debugger, including which versions already include ruby-debug, how to install the needed gems on older versions, and how to start debugging Rails apps or local Ruby programs.'
tags: ["jruby", "ruby-debug", "debugging"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "JRuby: Wiki: UsingTheJRubyDebugger — Project Kenai"
    url: "http://kenai.com/projects/jruby/pages/UsingTheJRubyDebugger"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-04/kenai-com--using-the-jruby-debugger.md"
    kind: repo
---

The page explains that JRuby has a Java-based implementation of the fast Ruby debugger rdebug. It says newer JRuby versions, especially 1.5, already bundle the gem, while JRuby 1.6 can install it directly with gem install ruby-debug.

For older JRuby versions, it lists a manual setup using ruby-debug-base, ruby-debug, ruby-debug-ide for IDE use, and columnize. It also shows how to start debugging a Rails app or a local Ruby script, and warns that the --debug option only works from JRuby 1.1.3 onward.

## Reading notes

- JRuby has a Java-based implementation of the fast Ruby debugger rdebug.
- JRuby 1.5 already includes the gem pre-bundled.
- JRuby 1.6 can install ruby-debug with jruby -S gem install ruby-debug.
- Older JRuby versions need manual installation of ruby-debug-base-0.10.3.2-java.gem.
- ruby-debug and ruby-debug-ide are installed with --ignore-dependencies in the older setup.
- columnize must also be installed unless it is already present.
- The --debug option works only with JRuby 1.1.3 and later.
- For older JRuby versions, the page says to use -J-Djruby.reflection=true and -J-Djruby.compile.mode=OFF instead of --debug.
- A Rails app can be started under the debugger with jruby --debug -S rdebug script/server.
- A local Ruby program can be started with ruby --debug -S rdebug -Ilib rubyprogram.rb.
- The debugger can also be invoked programmatically with require 'ruby-debug' and debugger.
