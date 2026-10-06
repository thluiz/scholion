---
title: "Common Misconceptions About Inheritance in JavaScript"
date: '2015-04-25T22:09:49-03:00'
category: webclip
summary: 'The article argues that prototypal inheritance is distinct from classical inheritance, and that JavaScript’s usual object patterns are literals, factories, delegation, and composition rather than classes or constructors.'
tags: ["javascript", "prototypal-inheritance", "object-composition"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Common Misconceptions About Inheritance in JavaScript — JavaScript Scene — Medium"
    url: "https://medium.com/javascript-scene/common-misconceptions-about-inheritance-in-javascript-d5d9bab29b0a"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-04/medium-com--common-misconceptions-about-inheritance-in-javascript.md"
    kind: repo
---

The article argues that JavaScript inheritance is commonly misunderstood. It says prototypes are objects, not blueprints, and that instances inherit from other instances through delegation or concatenation, while class inheritance creates hierarchies and brittleness.

It also says constructors, `new`, and `instanceof` are often overvalued, that factories and object literals are common and flexible, and that performance or memory arguments for class-based patterns are overstated. The author concludes that composition and prototypal patterns fit JavaScript better than ES6 `class`.

## Reading notes

- Prototypes are described as objects, while classes are described as blueprints.
- Class inheritance is presented as creating subclass hierarchies as a side effect.
- Prototypal inheritance is described as instances inheriting from other instances.
- Object literals, `Object.create()`, and `Object.assign()` are presented as common ways to create and combine objects.
- Factory functions are recommended over constructor functions.
- Closures are described as a way to get privacy without constructors.
- `new` is explained as creating an instance, binding `this`, and linking the instance to a prototype.
- `instanceof` is said to be an identity check on the prototype object, not reliable type checking.
- Performance differences between classical and prototypal inheritance are described as overstated.
- Memory use is said to be flexible in both approaches, with factory functions offering more freedom.
- The article says many JavaScript libraries and frameworks use factories and prototype extension.
- The author argues that class is not idiomatic in JavaScript and that composition is usually a better choice.
- ES6 `class` is described as an awkward fit for JavaScript's object system.
