---
url: "http://martinfowler.com/articles/two-stack-cms"
captured_at: "2014-10-07T09:11:00-03:00"
title: "Two Stack CMS"
domain: "martinfowler-com"
---

[![](http://martinfowler.com/twlogo.svg)](http://www.thoughtworks.com/)

Building a Two-Stack CMS for a global product catalog

We build many websites with rich content, often using popular Content Management Systems (CMS). A recent project involved a marketing website for a global manufacturer which demanded complex interactive content with high availability and traffic needs.

Our response was to apply the editing-publishing separation pattern and build two distinct stacks of software for content creation and delivery. In this deck you can see an overview of this architecture and our response to the issues of integration between the stacks, providing a secure preview of the live site, and handling the evolution and scaling of the system.

Many thanks to all our friends and colleagues who were involved in building this system and helped with the review of the Infodeck.

6 October 2014

![](http://martinfowler.com/articles/sunit.jpg)

**[Sunit Parekh](http://www.sunitparekh.in/)** is an application developer from Thoughtworks who likes to work on complex business problems with modern technologies. He specializes in distributed agile development working from Pune, India.

![](http://martinfowler.com/mf.jpg)

**[Martin Fowler](https://martinfowler.com/)** is an author and speaker who enjoys helping his colleagues write about their experiences in building important software systems.

Hints for using this deck

A call to build a marketing website for a global manufacturer had two big challenges

The site needs to be fresh and engaging, requiring design-heavy page structure, lots of graphics and video, interactive pages and links to internal systems for product specifications.

Writers for the website use a wide range of tools, some purchased, some built in-house. We must support these tools and provide a way to coordinate the workflow between tools and the various groups involved.

An important part of the coordination problem is translation - the global site must support over twenty countries with nearly a hundred locales. Imagery, product availability and pricing all vary between countries.

A global marketing site serves heavy traffic: daily visitors in six figures and **over two million daily page views**.

The site needs high availability, with no downtime for the frequent updates it will receive.
