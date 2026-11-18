---
title: "C# 8 is old news. Onward, to C# 9!"
date: '2019-12-27T09:28:42+00:00'
category: webclip
summary: 'Post from the 2019 C# Advent Calendar briefly walks through five proposed C# 9 features that reduce boilerplate and add new modeling options, plus a community thank-you.'
tags: ["csharp", "language-features", "dotnet", "community"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "C# 8 is old news. Onward, to C# 9!"
    url: "https://web.archive.org/web/20191227001401id_/https://dev.to/calvinallen/c-8-is-old-news-onward-to-c-9-d32"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--csharp-9-preview-language-features-overview.md"
    kind: repo
---

The post notes that planning for C# 9 has been underway well before C# 8 shipped in September 2019, and uses Christmas Day as a framing to preview five possible C# 9 "gifts" targeted for 2020. Each proposal aims to simplify common C# patterns or add more expressive ways to model data and behavior, with links to the corresponding discussions in the csharplang GitHub repo.

After presenting these language ideas, the author encourages readers to explore and participate in the GitHub discussions, highlights that Microsoft now welcomes community opinions, and closes with gratitude toward the C# Advent Calendar community and organizer Matthew D. Groves, along with holiday wishes.

## Reading notes

- The post is part of the 2019 C# Advent Calendar and links to the calendar site for other posts.
- Planning for the ninth version of C# has been ongoing long before C# 8 shipped in September 2019, as shown by the age of GitHub issues.
- The author notes that most people, including themselves, do not follow daily language planning but finds it interesting to occasionally look into the discussions.
- The article focuses on five potential C# 9 features that might arrive in 2020, explicitly marked as subject to change.

- Simplified parameter null validation would use an annotation on a method parameter to avoid manual null checks and guard clauses inside the method body.
- The example contrasts a method that throws `ArgumentNullException` when a string argument is null with a revised signature `void Insert(string s!)` that omits the explicit check.

- A proposal for using a switch expression as an expression statement is still in discussion but would allow switch expressions without assigning to a variable or returning a value.
- The first example shows a `void M` method where a `c switch { ... }` expression directly assigns to `x` or `s` inside a block.
- A second example uses an expression-bodied method `=> c switch { ... }` that performs the same assignments.

- The primary constructors proposal aims to reduce boilerplate around constructors, backing fields, and property accessors.
- A traditional `Person` class example has a private field, a constructor that sets it, and a property with a null check in the setter.
- The rewritten example uses `class Person(string firstName)` and accesses the constructor parameter directly in the `FirstName` property, preserving the null-checking setter logic.

- The record proposal is described as slightly similar in nature to primary constructors, with the goal of cutting down boilerplate for new classes or structs.
- The author suggests that if record types are accepted, primary constructors might not be included, marking that as their opinion.
- The example replaces a `Person` class with read-only properties and a constructor taking `Name` and `DateOfBirth` with a concise `public class Person(string Name, DateTime DateOfBirth);` declaration.

- Discriminated unions / `enum class` are presented as harder to grasp at first and involve familiar keywords plus a new one, along with records.
- In the author’s words, this is a cleaner way to build abstract base classes and their concrete subtypes.
- The before example uses an abstract `Shape` base class with `Rectangle` and `Circle` subclasses, each with properties and constructors.
- The after example declares `enum class Shape` with `Rectangle(float Width, float Length);` and `Circle(float Radius);` entries that encode the different shape cases.

- The author states that these five proposals only scratch the surface of C# 9 discussions and invites readers to visit the GitHub project and get involved.
- They describe Microsoft as changed and receptive to community opinions.

- The post closes with thanks to everyone who participated in the Advent event by volunteering, writing, sharing, or reading.
- The author expresses appreciation for the C# community and feeling grateful to be considered part of it.
- They offer inclusive holiday wishes, hoping that whatever holiday readers celebrate is wonderful, and sign off with "See you next year, friends."

- In a final note, the author thanks Matthew D. Groves for creating and running the Advent tradition, now in its third year.
- They say they feel lucky to call Matthew a friend and claim the community is better because of him.
- Readers are encouraged to follow him on Twitter and watch his Twitch streams, with the assurance they will not be disappointed, and the author wishes him a Merry Christmas.
