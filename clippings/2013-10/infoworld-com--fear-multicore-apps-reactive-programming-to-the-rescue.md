---
url: "http://www.infoworld.com/print/227985"
captured_at: "2013-10-06T23:31:19-03:00"
title: "Fear multicore apps? Reactive programming to the rescue"
domain: "infoworld-com"
---

# Fear multicore apps? Reactive programming to the rescue

By InfoWorld Tech Watch

Created *2013-10-02 03:00AM*

Reactive programming, in which programs react to events, is gathering steam as a mechanism for programming on multicore processors and for Web development. The concept is growing in importance in the Java realm, in particular. Typesafe, which has [built its Akka middleware stack around the Scala language and reactive programming](http://www.infoworld.com/d/application-development/6-technologies-you-should-learn-year-225344)  [1], is an advocate, and Netflix has been touting functional, reactive programming with its [RxJava library for asynchronous and event-based programs](https://github.com/Netflix/RxJava)  [2], based on Microsoft's Reactive Extensions project.

InfoWorld Editor at Large Paul Krill met with Typesafe Senior Software Engineer Josh Suereth at the recent JavaOne technical conference in San Francisco to talk about reactive programming. Suereth also commented on the importance of Lambdas in the upcoming Java Standard Edition 8 release.

**InfoWorld:** What is reactive programming?

**Suereth:** It's a concept that really has been around for a long time, but it's now becoming viable for Java. The basics of it is essentially instead of writing code that you say, "Do this, do this, do this, do this," you say, "After this event, do something. After that is complete, do something." So it's about reacting when something is done. The main reason this matters is because as we go multicore, if you program in this style, there are new techniques to optimize across CPUs.... I would say [reactive programming is becoming important now] because of the explosion in cores on CPUs. You're no longer able to stick your logic on a single thread and have that be the most efficient path. In the past, it definitely was. And now we're starting to see less CPU utilization, and we need to improve it. This is a mechanism that will let us improve utilization of the CPU and still retain performance.

**InfoWorld:** New techniques as far as what?

**Suereth:** [Java 7 introduced the fork/join library](http://www.infoworld.com/d/application-development/oracle-ships-java-7-rc-428)  [3] where if you program in a reactive style the fork/join library can actually retain some really good performance characteristics in that style. Similar to if you were writing just sequential code.

**InfoWorld:** Is reactive programming intended for Web development?

**Suereth:** It's really for any development, but I think it really shines when you're doing Web [application] development.

**InfoWorld:** Why?

**Suereth:** Just the nature of that style of programming. You get a request, and on that request, you have to perform some work, and that work usually entails making requests to other services that come back later, and you want to try to make sure when you're responding to these requests that you're not passing the data just across the CPUs and threads willy-nilly. You want to keep it local to where it comes in. So this way of partitioning your workflow can help the framework optimize your code.

**InfoWorld:** Which framework?

**Suereth:** In this particular case, I think the best example of this style is the Play Web Framework. It started off as a Java-only framework, and now the core is written in Scala; Typesafe is the primary provider. It's actually designed by Zenexity, a consulting company in France.

**InfoWorld:** What's the link between asynchronous programming and reactive programming?

**Suereth:** I use them interchangeably. The only thing asynchronous means is when an event happens, I do something else. So asynchronous and reactive, by definition, are effectively the same.

**InfoWorld:** Talk about your [JavaOne](http://www.infoworld.com/t/java-programming/oracle-were-getting-java-security-under-control-227404)  [4] presentation.

**Suereth:** Basically we're going to go through the motivation for why reactive matters on Java. Fork/join enables us to do this efficiently. We have multicore programs. We need to fragment things out. Then we're going to step through [some Java 8 features](http://www.infoworld.com/t/java-programming/java-8-developer-preview-ready-testing-226417)  [5] that you need to make use of for reactive. That's the Lambdas and the method handles and the functional interfaces.

**InfoWorld:** There is a lot of talk [about Lambda being the most revolutionary change in Java](http://www.infoworld.com/t/java-programming/oracle-claims-java-se-me-convergence-boon-developers-227293)  [6]. Do you see it as a revolutionary change, and how does it apply to reactive programming?

**Suereth:** Yes. I would say it's a revolutionary change, and I think it's what enables reactive programming to be elegant in Java. [Currently, with the Java Swing framework] you would make event handlers so that when somebody clicks a mouse, you do an action. You had to instantiate an anonymous class that had a single method.... It was a big block of code. It made things a little harder to maintain. With Lambdas, you fix two problems. One is the syntax. You bring the syntax for this style [of] code down to something that is easier to look at and understand what's going on. And the second thing you do is actually about scoping. You can actually reference variables inside the same scope without confusing what this is, this being the current instance.

**InfoWorld:** What is Typesafe's big interest in reactive programming?

**Suereth:** We actually have a reactive programming platform. All of our tools that we provide really promote and feature reactive programming.

**InfoWorld:** Does reactive programming apply to JavaScript or .Net languages?

**Suereth:** Yes. .Net has something called [the Reactive Extensions](http://www.infoworld.com/d/developer-world/microsoft-previews-rx-asynchronous-programming-391)  [7] APIs. It's nice and elegant and if you're doing Windows UIs, it's actually really easy to consume Web services and feed things into the UI itself. [Node.js [leverages reactive programming]](http://www.infoworld.com/d/application-development/nodejs-inventor-extends-javascript-programming-beyond-browsers-184963)  [8]. Typesafe recently released [the Reactive Manifesto](http://www.reactivemanifesto.org/)  [9] in coordination with Eric Meijer from Microsoft, and the Node.js guys have gotten involved as well. It's a description of what reactive programming is.

*This story, "[Fear multicore apps? Reactive programming to the rescue](http://www.infoworld.com/t/java-programming/fear-multicore-apps-reactive-programming-the-rescue-227985?source=footer)  [10]," was originally published at [InfoWorld.com](http://www.infoworld.com/?source=footer)  [11]. Get the first word on what the important tech news really means with the [InfoWorld Tech Watch blog](http://www.infoworld.com/blogs/infoworld-tech-watch?source=footer)  [12]. For the latest developments in business technology news, follow [InfoWorld.com on Twitter](http://twitter.com/infoworld)  [13].*

---

**Source URL (retrieved on *2013-10-06 07:01PM*):** <http://www.infoworld.com/t/java-programming/fear-multicore-apps-reactive-programming-the-rescue-227985>

**Links:**  
[1] http://www.infoworld.com/d/application-development/6-technologies-you-should-learn-year-225344  
[2] https://github.com/Netflix/RxJava  
[3] http://www.infoworld.com/d/application-development/oracle-ships-java-7-rc-428  
[4] http://www.infoworld.com/t/java-programming/oracle-were-getting-java-security-under-control-227404  
[5] http://www.infoworld.com/t/java-programming/java-8-developer-preview-ready-testing-226417  
[6] http://www.infoworld.com/t/java-programming/oracle-claims-java-se-me-convergence-boon-developers-227293  
[7] http://www.infoworld.com/d/developer-world/microsoft-previews-rx-asynchronous-programming-391  
[8] http://www.infoworld.com/d/application-development/nodejs-inventor-extends-javascript-programming-beyond-browsers-184963  
[9] http://www.reactivemanifesto.org/  
[10] http://www.infoworld.com/t/java-programming/fear-multicore-apps-reactive-programming-the-rescue-227985?source=footer  
[11] http://www.infoworld.com/?source=footer  
[12] http://www.infoworld.com/blogs/infoworld-tech-watch?source=footer  
[13] http://twitter.com/infoworld
