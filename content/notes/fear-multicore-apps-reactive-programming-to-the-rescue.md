---
title: "Fear multicore apps? Reactive programming to the rescue"
date: '2013-10-06T23:31:19-03:00'
category: webclip
summary: 'The piece says reactive programming helps multicore and web development by reacting to events, improving CPU use, and fitting Java better with fork/join, lambdas, and async workflows.'
tags: ["reactive-programming", "java", "multicore", "web-development"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Fear multicore apps? Reactive programming to the rescue"
    url: "http://www.infoworld.com/print/227985"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-10/infoworld-com--fear-multicore-apps-reactive-programming-to-the-rescue.md"
    kind: repo
---

Reactive programming is presented as a style where code reacts to events instead of following a fixed sequence. The article says it is becoming more important in Java because multicore CPUs make single-threaded logic less efficient, and it points to fork/join, lambdas, method handles, and functional interfaces as part of the shift.

It also says reactive programming is useful for web application development because requests often depend on work done by other services, and the workflow should keep data local so frameworks can optimize it. The Play Web Framework is given as the main example, and the article links reactive programming with asynchronous programming, RxJava, Reactive Extensions, Node.js, and the Reactive Manifesto.

## Reading notes

- Reactive programming means responding to events instead of writing a fixed chain of instructions.
- It is becoming viable for Java because multicore processors make better CPU utilization important.
- Java 7 fork/join can work well with a reactive style.
- Web application development is a strong fit because requests often trigger work in other services.
- Keeping data local to where a request arrives helps frameworks optimize the workflow.
- The Play Web Framework is presented as the best example in this style.
- Asynchronous programming and reactive programming are treated as effectively the same here.
- Java 8 lambdas, method handles, and functional interfaces are presented as tools that make reactive code easier in Java.
- Lambdas simplify event handlers and scope handling compared with anonymous classes.
- Typesafe says its tools promote and feature reactive programming.
- The article also connects the topic to RxJava, Reactive Extensions, Node.js, and the Reactive Manifesto.
