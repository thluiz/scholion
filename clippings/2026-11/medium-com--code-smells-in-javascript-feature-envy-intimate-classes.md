---
url: "https://medium.com/better-programming/more-code-smells-in-javascript-113067dbd89f"
captured_at: "2026-11-16T05:49:16+00:00"
title: "Code Smells in JavaScript. We look at feature envy and intimate… | by John Au-Yeung | Better Programming"
domain: "medium-com"
---

Member-only story

JavaScript
Programming
Software Development
Web Development
Technology
Code Smells in JavaScript
We look at feature envy and intimate classes
John Au-Yeung
4 min read
·
Jan 16, 2020

Photo by Mimi Thian on Unsplash

In programming, a code smell is a characteristic of a piece of code that indicates there may be deeper problems. It’s a subjective characteristic used to judge whether code is of decent quality by looking at it.

In this article, we look at more code smells in JavaScript code, including feature envy, and classes that are too intimate.

Feature Envy

Feature envy means that one class uses too many features of another class. This means that most of one class reference something in another class.

This is especially applicable to using fields from one in class in another class excessively

For example, if we have the following:

The ShapeCalculator class uses lots of fields from Rectangle. We get all the fields from Rectangle in the ShapeCalculator class when we don’t have to.

This breaks encapsulation in the Rectangle class since we exposed the fields height and width when we don’t have…
