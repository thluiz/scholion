---
title: "A Monadic Approach to Error Handling in Collection Pipelines"
date: '2015-02-20T00:04:07-03:00'
category: webclip
summary: 'Michael Feathers shows how chained computation can carry both results and errors in a single pipeline, using a Ruby version of Haskell’s Either to record validation failures while skipping later stages.'
tags: ["error-handling", "collection-pipelines", "either", "ruby"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Michael Feathers - A Monadic Approach to Error Handling in Collection Pipelines"
    url: "https://michaelfeathers.silvrback.com/a-monadic-approach-to-error-handling-in-collection-pipelines"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-02/michaelfeathers-silvrback-com--a-monadic-approach-to-error-handling-in-collection-pipelines.md"
    kind: repo
---

Michael Feathers describes error handling as part of the larger problem of passing the right information through a single sequential pipeline. In his view, a pipeline should be able to keep producing results while also carrying error messages forward when something goes wrong.

He applies that idea to a guitar tablature program. Instead of throwing an exception at the first bad line, he uses a hacked-up Ruby version of Haskell’s Either type so the pipeline can collect errors such as the wrong number of fields, non-numeric values, or out-of-range string and fret numbers. When a check fails, later stages skip their work, and the run ends with either errors or output. He then sketches an implementation by monkey patching Enumerable and delegating through an ErrorEnumerable wrapper.

## Reading notes

- chained computation is useful for utility programming, but a pipeline still has to manage the information each stage needs
- extra arguments in a sequential flow are presented as a design problem when they are only needed later
- error handling is treated as a special case of that same extra-arguments problem
- passing an empty array is described as the simplest failure response, but it does not preserve error messages
- the tablature program splits input lines into fields and assumes each line has a string number and a fret number
- possible input problems include the wrong field count, non-numeric fields, and values outside the allowed ranges
- exceptions are presented as too coarse because they stop the pipeline at the first detected error
- the Either type is borrowed from Haskell to track both results and errors in one pipeline
- the pipeline with checks records errors and skips later computation after a failure
- the implementation sketch uses a monkey-patched Enumerable and an ErrorEnumerable class with delegation
