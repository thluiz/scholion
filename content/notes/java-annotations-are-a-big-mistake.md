---
title: "Java Annotations Are a Big Mistake"
date: '2026-11-16T02:42:45+00:00'
category: webclip
summary: 'The page argues that annotations push behavior out of objects and hide composition behind containers, marshallers, and weavers. It prefers explicit object composition and `new` over annotations and configurations.'
tags: ["java", "annotations", "object-composition", "dependency-injection"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Java Annotations Are a Big Mistake"
    url: "https://yegor256.com/2016/04/12/java-annotations-are-evil.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/yegor256-com--java-annotations-are-a-big-mistake.md"
    kind: repo
---

The page argues that Java annotations are a design mistake because they move behavior outside the object and weaken encapsulation. In the examples, injection, XML marshalling, and retry logic are all handled by external mechanisms that act behind the scenes instead of being part of the object itself.

The author prefers explicit composition: inject dependencies through constructors, wrap objects with decorators, and model retrying with a separate retry object. The conclusion is that objects should be instantiated directly with `new`, while annotations and configuration mechanisms hide the real composition of the program.

## Reading notes

- Annotations were first welcomed for making Java code shorter and reducing XML configuration and marker interfaces.
- The main objection is that annotations encourage implementing object behavior outside the object, which goes against encapsulation.
- With `@Inject`, the class does not control how its dependency is created or provided; the container does that behind the scenes.
- The suggested alternative is constructor injection, where the object receives its dependency directly.
- The same criticism is applied to ORM use of annotations, where object behavior is split across different places.
- With `@XmlElement`, XML creation is done by JAXB outside the `Book` object.
- The preferred alternative is to keep XML-printing behavior inside the object, either directly or through a decorator.
- With `@RetryOnFailure`, AspectJ uses the annotation as a signal to wrap the class and alter its bytecode.
- The author objects to hidden composition and prefers an explicit wrapper such as `FooThatRetries` around `Foo`.
- The page ends by saying annotations are bad, composition is better, and configurations are worse because objects should be instantiated, not configured.
