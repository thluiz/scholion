---
title: "Learning More About JRuby from Charles Nutter"
date: '2012-03-19T02:21:36-03:00'
category: webclip
summary: 'Interview with Charles Nutter about JRuby 1.6.7, JRubyConf, why Rubyists use JRuby, Maven-based Java library access, JRuby internals, InvokeDynamic, and the IR compiler.'
tags: ["jruby", "ruby", "java", "maven"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Learning More About JRuby from Charles Nutter » RubySource"
    url: "http://rubysource.com/learning-more-about-jruby-from-charles-nutter/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-03/rubysource-com--learning-more-about-jruby-from-charles-nutter.md"
    kind: repo
---

Charles Nutter says JRuby 1.6.7 is a quick follow-up release that fixes many issues found after 1.6.6, especially Ruby 1.9 and encoding problems. He also points to JRubyConf, the RubyConf India keynote, and the current work on JRuby 1.7 and InvokeDynamic.

## Reading notes

- JRuby 1.6.7 followed 1.6.6 to fix about 40 issues found after release, with many Ruby 1.9 feature and encoding fixes.
- JRubyConf is scheduled for May 21st to 23rd in Minneapolis.
- Charles Nutter recommends the book Using JRuby: Bringing Ruby to Java as a starting point.
- JRuby is presented as attractive for performance on small or computation-intensive apps, strong garbage collection and memory management through the JVM, and cross-platform stability.
- The deployment experience is described as close to regular Ruby, with Engine Yard, Heroku, Trinidad, Tomcat, Unicorn, and Passenger mentioned.
- JRuby supports real concurrent threads, but some operations such as concurrent mutations of strings, arrays, and hashes are not guaranteed thread safe.
- Startup time is a drawback, and TDD workflows can feel slower because JRuby code still needs JVM compilation at runtime.
- If libraries are compatible, development can use MRI while testing and production use JRuby, as in Square’s workflow.
- JRuby hides Java classpaths, app servers, and much of Java verbosity from most users.
- Maven is described as a global repository of Java libraries and dependencies, and JRuby patches RubyGems so Maven artifacts can be installed with gem-style commands.
- Charles Nutter says you can install Java libraries, including Clojure, and use them from IRB.
- JRuby starts with Java implementations of core classes, an AST-based interpreter, and a parser modeled on Ruby’s parser using Jay.
- Repeated code paths are compiled to JVM byte code after about 50 calls, after which the JVM can continue compiling to native code.
- InvokeDynamic lets JRuby describe method linking in a way the JVM can optimize more directly, improving dynamic call performance on Java 7.
- JRuby 1.7 is the master branch for InvokeDynamic work.
- The planned IR compiler would add an intermediate instruction set above the JVM, with inlining and optimization before generating JVM byte code.
