---
title: "Why developers should get excited about Java 9"
date: '2014-08-26T18:06:33-03:00'
category: webclip
summary: 'Java 9 is presented as a major step for the platform, led by modularity through Project Jigsaw and supported by new APIs and runtime improvements for JSON, processes, locking, code cache, and compilation.'
tags: ["java-9", "project-jigsaw", "json-api", "jvm"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Why developers should get excited about Java 9 | Java programming - InfoWorld"
    url: "http://www.infoworld.com/t/java-programming/why-developers-should-get-excited-about-java-9-248771"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-08/infoworld-com--why-developers-should-get-excited-about-java-9.md"
    kind: repo
---

Java 9 is described as the next edition of standard Java, with several updated JEPs pointing to a release planned for early 2016. The article highlights modular source code as the main change, along with API updates and runtime work aimed at scalability, maintainability, security, and performance.

## Reading notes

- JDK 9 is based on Java SE 9 and was targeted for release in early 2016.
- The headline change is a modular source code system through Project Jigsaw.
- Modularization is meant to make Java more scalable to smaller devices and easier to maintain.
- The module system is meant to be powerful enough for the JDK and other large legacy code bases.
- JSON support is listed as a key feature for Java 9.
- The JSON API is meant for consuming and generating documents and data streams.
- The article says JSON has become the lingua franca for web services.
- The process API is being updated to improve management of operating system processes.
- The current API often forces developers to use native code.
- The new process API needs to account for operating system differences, especially on Windows.
- Contended locking improvements are intended to benefit real-world applications and benchmarks.
- Segmented code cache is intended to divide compiled code into segments to improve performance and allow extensions.
- Smart Java Compilation, Phase 2, aims to improve javac and make it usable by default in the JDK build.
- The current javac implementation improves build speed and incremental builds, but is not yet satisfactory for public release.
