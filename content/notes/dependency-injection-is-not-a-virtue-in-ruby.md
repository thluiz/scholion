---
title: "Dependency injection is not a virtue in Ruby"
date: '2013-11-13T10:04:22-03:00'
category: webclip
summary: 'DHH argues that dependency injection is a Java habit that can be overvalued in Ruby. He says Ruby lets hard-coded references stay simple while still being easy to test, so language shape matters more than cross-language best practices.'
tags: ["ruby", "dependency-injection", "testing", "language-design"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Dependency injection is not a virtue in Ruby (DHH)"
    url: "http://david.heinemeierhansson.com/2012/dependency-injection-is-not-a-virtue.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-11/david-heinemeierhansson-com--dependency-injection-is-not-a-virtue-in-ruby.md"
    kind: repo
---

DHH argues that dependency injection is mainly a response to rigid languages where hard-coded references make testing difficult. In Ruby, he says, code can keep simple direct references and still be tested easily, so the pattern can become a taste issue rather than a necessity.

He also warns against treating Java-derived habits as universal best practices. The larger point is that programming languages shape how developers think, so ideas that fit one language can clash with another even when they look similar on the surface.

## Reading notes

- In Ruby, hard-coded references can remain simple and still be easy to test.
- `Time.stub(:now)` and the Timecop gem are used as examples of testing time-dependent code without dependency injection.
- Dependency injection is described as a pattern that has been promoted across languages on the strength of flexibility claims.
- The post says patterns can move from being tools to becoming matters of taste.
- DHH questions the divide between designing for tests and designing for API in a language like Ruby.
- He connects the argument to the idea that languages shape thought and that not all practices transfer cleanly across languages.
