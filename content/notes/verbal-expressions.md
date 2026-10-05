---
title: "verbal_expressions"
date: '2016-01-05T13:06:19-03:00'
category: webclip
summary: 'Ruby library that helps construct difficult regular expressions, with examples for URL matching, string replacement, and capturing, plus a note that documentation is limited and the JavaScript wiki covers most methods.'
tags: ["ruby", "regular-expressions", "library", "javascript-port"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "ryan-endacott/verbal_expressions"
    url: "https://github.com/ryan-endacott/verbal_expressions"
    kind: repo
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-01/github-com--verbal-expressions.md"
    kind: repo
---

VerbalExpressions is a Ruby library for building difficult regular expressions more easily. It is ported from the JavaScript VerbalExpressions project and includes examples for URL testing, replacing strings, and capturing values.

## Reading notes

- It is installed with `gem install verbal_expressions`, then loaded with `require verbal_expressions`.
- The README shows an example for testing a valid URL and printing the generated regex.
- It shows a replacement example where the expression finds `bird` and `gsub` changes the string.
- It shows capturing syntax with `begin_capture` and `end_capture`, including a named capture example.
- The repo says documentation is limited, and points to the original JavaScript repo wiki for more method documentation.
- It says most methods were ported as of v0.1.0 of the JavaScript repo.
- It asks contributors to clone the repo, fork it, and open pull requests.
- It notes that modifier code has not been ported yet because Ruby Regexp handles modifiers differently.
- It says `or` is aliased to `alternatively`, and `then` must be replaced with `find` because both names are reserved in Ruby.
