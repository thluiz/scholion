---
url: "http://www.infoworld.com/t/java-programming/why-developers-should-get-excited-about-java-9-248771"
captured_at: "2014-08-26T18:06:33-03:00"
title: "Why developers should get excited about Java 9 | Java programming - InfoWorld"
domain: "infoworld-com"
---

# Why developers should get excited about Java 9

## The next generation of the enterprise development platform will feature major improvements, including modularity and API updates

[Follow @pjkrill](http://www.twitter.com/pjkrill)

![74a8363e37c13e400db2ac13e56ac59b.jpg](infoworld-com--why-developers-should-get-excited-about-java-9/74a8363e37c13e400db2ac13e56ac59b.jpg)

With work moving forward on the next edition of standard Java, developers can start looking forward to what they will get with the planned upgrade.

Several JEPs (JDK Enhancement Proposals) for Java Development Kit 9 were updated this week, offering the latest perspectives on what to expect with JDK 9, which has been [targeted for release in early 2016](http://www.javaworld.com/article/2078927/java-se/oracle-to-limit-backward-compatibility-from-java-9-to-java-8.html) and is based on the Java Standard Edition 9 platform. Headlining the release at this juncture is a modular source code system. Oracle has planned a modular Java via Project Jigsaw, [which had been planned for JDK 8 but was pushed back](http://www.infoworld.com/d/application-development/project-jigsaw-delayed-until-java-9-198007); the existing JEP is part of Project Jigsaw. Standard Edition Java becomes more scalable to smaller devices with this technology. "The module system should be powerful enough to modularize the JDK and other large legacy code bases, yet still be approachable by all developers," says Oracle's Mark Reinhold, chief architect in Java Platform Group, [in a recent blog post](http://openjdk.java.net/projects/jigsaw/goals-reqs/03).

Jigsaw isn't the only new addition slated for Java 9. Support for the popular JSON (JavaScript Object Notation) data interchange format is key feature as well, along with process API, code cache, and locking improvements. "The key message is that there's a tremendous investment in the continuing evolution of Java," says Scott Sellers, CEO at Azul Systems, which offers JVM technology.

Here is a rundown of what's in store with JDK 9:

**Modular source code**  
JDK source code will get reorganized into modules, the build system will get enhanced to compile modules, and module boundaries will be enforced at build time. "Project Jigsaw aims to design and implement a standard module system for the Java SE Platform and to apply that system to the platform itself and to the JDK. Its primary goals are to make implementations of the platform more easily scalable down to small devices, improve the security and maintainability, enable improved application performance, and provide developers with better tools for programming," the JEP document says. Another project, Penrose, is looking into interoperability between Jigsaw and the OSGi component system for Java. Subsequent JEPs will modularize the Java Runtime Environment and JDK images and introduce a module system.

**Lightweight JSON API**  
This is an API is for consuming and generating documents and data streams via the JavaScript Object Notation data interchange format, which is based on a subset of JavaScript and serves as an alternative to XML. "JSON has become the lingua franca for Web services, and it is time for Java SE to adopt functionality for interacting with and utilizing JSON documents and data streams," the corresponding JEP document says. "This proposal is designed [to] provide the most commonly needed functionality and take advantage of Java 8/9 language and library features."

**Process API updates**  
This will improve the API for managing operating system processes and is intended to overcome limitations of the current API that often forces developers to use native code. Java SE 7, the JEP notes, offers limited support for native operating system processes; the new API, though, needs to account for operating system differences, particularly on Windows. "The design of this API needs to accommodate possible deployment on smaller devices with different operating system models. It should also take into account environments where multiple Java virtual machines are running in the same operating system process," the JEP document states.

**Improve contended locking**  
The goal is to improve contended Java object monitors. The documentation says that "improving contended locking will significantly benefit real-world applications in addition to industry benchmarks such as Volano and DaCapo."

**Segmented code cache**  
This effort is intended to divide code cache into segments, each containing compiled code of a particular type, to improve performance and allow extensions.

**Smart Java Compilation, Phase 2**  
This project is intended to improve the s javac (Java programming language compiler) tool enabling it to be used by default in the JDK build and also to generalize it so it can be used to build large projects other than the JDK. "The current implementation has proved to be useful and does indeed improve build speed and allow for incremental builds. The quality of the code and stability of the tool as a whole, however, is not satisfactory and it is certainly not ready for public release," the JEP document states.

*This story, "[Why developers should get excited about Java 9](http://www.infoworld.com/t/java-programming/why-developers-should-get-excited-about-java-9-248771?source=footer)," was originally published at [InfoWorld.com](http://www.infoworld.com/?source=footer). Get the first word on what the important tech news really means with the [InfoWorld Tech Watch blog](http://www.infoworld.com/blogs/infoworld-tech-watch?source=footer). For the latest developments in business technology news, follow [InfoWorld.com on Twitter](http://twitter.com/infoworld).*
