---
url: "https://levelup.gitconnected.com/typescript-advanced-types-nullable-types-and-type-aliases-847f03b08fae"
captured_at: "2026-11-16T05:48:56+00:00"
title: "TypeScript Advanced Types — Nullable Types and Type Aliases | by John Au-Yeung | Level Up Coding"
domain: "levelup-gitconnected-com"
---

Member-only story

JavaScript
Typescript
Software Development
Programming
Technology
TypeScript Advanced Types — Nullable Types and Type Aliases
John Au-Yeung
5 min read
·
Jan 14, 2020

Photo by Gary Bendig on Unsplash

TypeScript has many advanced type capabilities and which make writing dynamically typed code easy. It also facilitates the adoption of existing JavaScript code since it lets us keep the dynamic capabilities of JavaScript while using the type-checking capability of TypeScript. There are multiple kinds of advanced types in TypeScript, like intersection types, union types, type guards, nullable types, and type aliases, and more. In this article, we look at nullable types and type aliases.

Nullable Types

To let us assign undefined to a property with the --strictNullChecks flag on, TypeScript supports nullable types. With the flag on, we can’t assign undefined to type members that don’t have the nullable operator attached to it. To use it, we just put a question mark after the member name for the type we want to use.

If we have the strictNullChecks flag on and we set a value of a property to null or undefined , then like we do in the following code:

interface Person {
name: string;
age: number;
}
let p: Person = {
name: 'Jane',
age: null
}

Then we get the following errors:

Type 'null' is not assignable to type 'number'.(2322)
input.ts(3, 3): The expected…
