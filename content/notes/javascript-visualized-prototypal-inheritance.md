---
title: "JavaScript Visualized: Prototypal Inheritance"
date: '2022-08-23T07:47:29-03:00'
category: webclip
summary: 'Explains how JavaScript objects inherit through the prototype chain, why built-in methods are available on strings, arrays, and objects, and how constructor functions, classes, and Object.create relate to that model.'
tags: ["javascript", "prototypal-inheritance", "prototype-chain", "object-create"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "🎉👨‍👩‍👧‍👧 JavaScript Visualized: Prototypal Inheritance - DEV Community"
    url: "https://dev.to/lydiahallie/javascript-visualized-prototypal-inheritance-47co"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-08/dev-to--javascript-visualized-prototypal-inheritance.md"
    kind: repo
---

This page explains prototypal inheritance in JavaScript through dogs, classes, and objects created with `Object.create`. Instances keep their own properties, while shared behavior lives on the prototype and is reached through the `__proto__` chain.

It also shows that built-in methods come from the prototype chain, that classes are syntactical sugar for constructor functions, and that `extends` and `super` connect child classes to parent constructors and methods.

## Reading notes

- A constructor function creates both instances and a prototype object, and the prototype contains a `constructor` reference back to that function.
- Instance objects have a non-enumerable `__proto__` reference to their constructor's prototype.
- Shared methods such as `bark` belong on the prototype so every instance can use the same function instead of creating a new one.
- When a property is not found on the object itself, JavaScript looks it up through the prototype chain.
- The prototype chain can continue through several objects, including `Object.prototype`.
- Built-in methods like `.toString()` are found on the prototype chain rather than on each instance.
- ES6 classes use the same prototype model, but with a different syntax.
- Class bodies define prototype methods, and class constructors handle instance initialization.
- A subclass can access the parent constructor with `super` and inherit methods from the parent class prototype.
- `Object.create` makes a new object with a chosen prototype object.
- If a property is nowhere on the object or its prototype chain, the result is `undefined`.
