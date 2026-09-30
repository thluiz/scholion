---
title: "Introduction to Unit Testing With NUnit in C#"
date: '2022-03-26T20:00:34-03:00'
category: webclip
summary: 'The article explains unit testing in C# with NUnit, covering the AAA structure, naming conventions, test project setup, parameterized tests, setup and teardown, and metadata attributes.'
tags: ["unit-testing", "nunit", "csharp", "testing"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Introduction to Unit Testing With NUnit in C# - Code Maze"
    url: "https://code-maze.com/csharp-nunit-unit-testing/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-03/code-maze-com--introduction-to-unit-testing-with-nunit-in-c-sharp.md"
    kind: repo
---

The article introduces unit testing in C# with NUnit and explains the basic structure of a unit test through Arrange, Act, Assert. It also covers naming conventions for test methods and test projects, plus how to set up a simple test project for a Calculator class.

## Reading notes

- Unit tests are automated tests written and run by the developer to check that a small part of an application behaves as intended.
- A unit test typically follows Arrange, Act, Assert, with the expected value defined in Arrange to keep Assert simple.
- A common naming pattern is `[GivenX]_When[Y]_Then[Z]`.
- Test projects are usually separated by business project, with names like `Project.Business.UnitTests` or `Project.Business.FunctionalTests`.
- In the example, the main project contains a `Calculator` class with a `Divide` method, and the test project is named `NUnitProject.UnitTests`.
- The article says to install `NUnit`, `NUnit3TestAdapter`, and `Microsoft.NET.Test.Sdk`.
- A test method is marked with the `[Test]` attribute.
- Tests can be run in Visual Studio or with `dotnet test`.
- `[TestCase]` lets the same test run with different constant inputs.
- `[TestCaseSource]` accepts a static method or property that provides test values.
- `[SetUp]` runs before each test case, while `OneTimeSetup` runs once before all test cases.
- `TearDown` and `OneTimeTearDown` run after tests.
- The article describes metadata attributes such as `[Author]`, `[Description]`, `[MaxTime]`, and `[Category]`.
- `[Category]` can be used to group tests and run only the tests for a specific feature.
- The conclusion says NUnit is a popular .NET testing framework with tools for unit tests and metadata.
