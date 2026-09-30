---
title: "Why OO Sucks by Joe Armstrong"
date: '2019-12-27T05:46:16-03:00'
category: webclip
summary: 'Joe Armstrong argues that OOP binds data and functions together, turns everything into objects, scatters type definitions, and hides state in the wrong way. He says OO grew popular through hype and industry incentives.'
tags: ["object-oriented-programming", "erlang", "state"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Why OO Sucks by Joe Armstrong"
    url: "http://harmful.cat-v.org/software/OO_programming/why_oo_sucks"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2019-12/harmful-cat-v-org--why-oo-sucks-by-joe-armstrong.md"
    kind: repo
---

Joe Armstrong says his objection to OOP starts with the basic model. He argues that functions and data structures belong to different worlds, that objects force everything into one form, that data type definitions become scattered, and that private state hides what should be handled more openly.

He also says OO became popular because it seemed easy, promised reuse, was hyped, and helped create a software industry. He treats those social reasons as a stronger explanation for OO’s spread than technical merit.

## Reading notes

- Functions transform inputs to outputs, while data structures just are, so binding them together is a basic error.
- An OO language makes even time into an object, while non-OO languages can represent time as a data type with clear type declarations.
- In OO languages, data type definitions are spread across objects instead of being collected in one place.
- He prefers a small number of ubiquitous data types with many small functions over many data types with few functions.
- He says state exists in the real world, but OO hides state from the programmer instead of exposing it and limiting its nuisance.
- He lists four reasons for OO’s popularity: ease of learning, code reuse, hype, and the creation of a new software industry.
- He says there is no evidence for the first two reasons and treats hype and industry incentives as the real drivers.
