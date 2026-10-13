---
title: "Don't rescue Exception, rescue StandardError"
date: '2012-11-01T11:19:25-03:00'
category: webclip
summary: 'The page says Ruby should almost never rescue Exception; the safer default is StandardError, unlike C# or Java where catch(Exception) covers all exception types.'
tags: ["ruby", "exception-handling", "standarderror"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Don't rescue Exception, rescue StandardError"
    url: "http://rails-bestpractices.com/posts/702-don-t-rescue-exception-rescue-standarderror"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-11/rails-bestpractices-com--dont-rescue-exception-rescue-standarderror.md"
    kind: repo
---

Ruby should almost never rescue `Exception`. The page contrasts Ruby with C# and Java, where `catch (Exception)` can be used to rescue all exception types, and says Ruby code should instead rescue `StandardError`.

## Reading notes

- In C# or Java, `catch (Exception)` rescues all exception types.
- In Ruby, `Exception` should almost never be rescued.
- The recommended default in Ruby is to rescue `StandardError`.
