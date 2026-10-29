---
title: "Peeking Under the Hood of ActionController Parameters, Part 2"
date: '2015-12-23T15:03:31-03:00'
category: webclip
summary: 'The post explains why Rails params are not plain hashes, how ActionController::Parameters inherits HashWithIndifferentAccess, and how permit and permit! manage the permitted flag.'
tags: ["rails", "ruby", "strong-parameters", "actioncontroller-parameters"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Peeking Under the Hood of ActionController Parameters, Part 2 - Words and Code"
    url: "http://vaidehijoshi.github.io/blog/2015/11/24/peeking-under-the-hood-of-actioncontroller-parameters-part-2"
    kind: repo
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-12/vaidehijoshi-github-io--peeking-under-the-hood-of-actioncontroller-parameters-part-2.md"
    kind: repo
---

The post explains that Rails params look like a hash, but they are instances of ActionController::Parameters. That class inherits from ActiveSupport::HashWithIndifferentAccess, which lets keys be accessed with either strings or symbols, while adding strong-parameters behavior.

It also shows that new params objects start unpermitted, that permit and permit! set the @permitted attribute, and that controller params come from ActionController::Metal through a memoized params method.

## Reading notes

- Rails can feel like a black box because much of its logic is abstracted away.
- params in controllers are instances of ActionController::Parameters, not plain Ruby Hashes.
- ActionController::Parameters inherits from ActiveSupport::HashWithIndifferentAccess.
- HashWithIndifferentAccess treats :foo and "foo" as the same key and returns keys as strings.
- A Hash can be converted with with_indifferent_access.
- ActionController::Parameters objects are unpermitted by default.
- permitted? returns the @permitted attribute.
- permit calls permit! after filtering permitted scalar values.
- permit! sets @permitted to true and returns self.
- permit! can be used for mass assignment when all attributes should be allowed.
- ActionController::Base inherits from ActionController::Metal.
- ActionController::Metal is the simplest Rails controller and provides a Rack interface.
- controller params are stored in @_params through a memoized params method that reads request.parameters.
- The post notes a Rails 5 change in which ActionController::Parameters will return an object instead of a Hash instance.
