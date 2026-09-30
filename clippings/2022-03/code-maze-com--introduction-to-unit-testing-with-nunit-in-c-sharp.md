---
url: "https://code-maze.com/csharp-nunit-unit-testing/"
captured_at: "2022-03-26T20:00:34-03:00"
title: "Introduction to Unit Testing With NUnit in C# - Code Maze"
domain: "code-maze-com"
---

In this article, we are going to learn about unit testing with NUnit in C# through examples.

[Testing](https://code-maze.com/asp-net-core-testing/) is one of the essential parts of the software development cycle, and there are many different test types. We’ll concentrate our attention on programmatic tests, such as unit tests, functional tests, or integrational tests. 

To download the source code for this article, you can visit our [GitHub repository](https://github.com/CodeMazeBlog/CodeMazeGuides/tree/main/dotnet-testing/NUnitProject).

We need a test framework that conveniently defines a single test case or a group of test cases and runs them to cover our code with tests. NUnit is one of the testing frameworks available for .NET developers. It has convenient tools for writing tests and good documentation.

Before we start, let’s revise what unit tests are, and let’s talk about some best practices.

## **What is Unit Testing?**

Unit test is an automated test written and run by the developer to ensure that a piece of an application behaves as intended. Usually, unit tests cover the smallest logic unit of an application, and it helps developers to be sure that the application’s pieces work correctly. 

A single unit test has a proper structure – well-known as triple A. **Arrange, Act, Assert**. It helps to identify what happens inside the test case. 

Let’s take a look at the test case where we have triple-A separation: 

public void WhenCallPlusWithTwoOperands\_ThenItSumsValues()
{
    // Arrange
    var a = 1;
    var b = 2;

    var expected = 3;

    // Act
    var sum = a + b;

    // Assert
    Assert.AreEqual(sum, expected);
}

This test case verifies that operator `+` correctly sums two operands `a` and `b`. To keep the assertion part as simple as possible, we should define the expected value in the Arrange part. 

The test case in our example verifies the result. But also, we can be interested in verifying a component interaction. We’ll have a look at how to test it later. 

### **Test Method Naming Convention**

The most important part of the development and unit testing is a proper naming convention. The name of the unit test should reflect what we are trying to test and the conditions for the test case. 

Let’s take a look at one of the commonly used naming conventions:

`[GivenX]_When[Y]_Then[Z]`

It starts with an optional “Given” part that gives some context to the test, after which we describe some action that needs to be done in the “When” part. Finally, we describe what we expect to happen for a particular test case in the “Then” part of the method name.

### **Test Project and Files Naming Convention** 

It’s common good practice to keep separate test projects for each business project inside the solution. So if our solution has a business project named `Project.Business` than test’s project name should be `Project.Business.UnitTests`.

We use a proper suffix to show the intention of tests. For functional tests, the name would be `Project.Business.FunctionalTests`.

We should keep the same structure that we have in our business project. Each class we cover with tests should have a test class in the test project named accordingly with `Test` suffix. 

![The Web API Production Checklist, free ebook](https://code-maze.com/wp-content/uploads/ebooks/covers/cover-beige-2-chevron-400.webp)

Free ebook

Is your Web API ready for production?

33 things to check before you ship, with the fix for each one. A free 76-page PDF for .NET 10.

[Get the free checklist](https://code-maze.com/free-ebook-aspnetcore-webapi-best-practices/?box=1)

Free PDF. One email to send it. Unsubscribe any time.

## **NUnit Project Setup**

Let’s define the simplest business logic class that we are going to test in this article. We are going to create a  `NUnitProject` project with a single `Calculator` class that has just one method, `Divide`. It’s enough for our purposes:

public class Calculator
{
    public double Divide(int a, int b)
    {
        return a / b;
    }
}

The next step would be to add a test project to the solution. We should rely on the naming convention and name it `NUnitProject.UnitTests`. It’s a simple class library. Also, we are going to add the reference from the main project to the testing project. 

Now it’s time to add the required NuGet packages. 

 Let’s run the command to install the NUnit package in the `Test` project:

dotnet add package NUnit

`dotnet add package NUnit`

To be able to integrate with visual studio properly, we should also add the NUnit adapter package and Microsoft test SDK:

dotnet add package NUnit3TestAdapter

dotnet add package Microsoft.NET.Test.Sdk

### **First Test Case** 

Now when we have the test project ready, we can start covering the `Calculator` class with unit tests. 

Let’s define a simple test case to verify that the `Divide` method works properly:

\[Test\]
public void WhenDivideTwoNumbers\_ThenReturnDivisionOfTwoNumbers()
{
    // Arrange
    var a = 300;
    var b = 100;

    var expected = 3;
    var calculator = new Calculator();

    // Act
    var actual = calculator.Divide(a, b);

    // Assert
    Assert.AreEqual(expected, actual);
}

To mark a method as a test case, we need to add a `Test` attribute. It tells the `NUnit` framework that it should run this method.

We can run all tests in a solution using Visual Studio with a few simple steps: 

`TopMenu -> Tests -> Run All Tests`, with a shortcut `Ctrl R + T`, or from the console – navigate to the test project directory and run the command:

dotnet test

`dotnet test`

It’s a good approach to run our test methods with different arguments, without copy-pasting our test methods. We can define test method parameters by using the `[TestCase]` attribute.

The `[TestCase]` attribute allows us to provide params for the test method:

\[TestCase(300,100, 3)\]
\[TestCase(400, 200, 2)\]
public void WhenDivideTwoNumbers\_ThenReturnDivisionOfTwoNumbers(int a, int b, double expected)
{
    // Arrange
    var calculator = new Calculator();

    // Act
    var actual = calculator.Divide(a, b);

    // Assert
    Assert.AreEqual(expected, actual);
}

The `[TestCase]` attribute allows only constant values for params, but we can find ourselves in a situation where we need to create a value on the fly.

### Providing a Source With the TestCaseSource Attribute

We can solve this by using the `[TestCaseSource]` attribute. It accepts the name of the static method or property, which provides values for the test method:

\[TestCaseSource(nameof(SourceProvider))\]
public void WhenDivideTwoNumbers\_ThenReturnDivisionOfTwoNumbersProvidedBySource(int a, int b, double expected)
{
    // Arrange
    var calculator = new Calculator();
    // Act
    var actual = calculator.Divide(a, b);

    // Assert
    Assert.AreEqual(expected, actual);
}

public static IEnumerable<int\[\]> SourceProvider()
{
    yield return new int\[\] { 300, 100, 3 };
    yield return new int\[\] { 400, 200, 2 };
}

Now, we face the problem of creating a calculator instance inside each test method. `NUnit` provides a convenient way to execute a piece of code before all test methods or before each test method run. 

With the `[Setup]` attribute, we can execute a method before each test case run, and we can create a `Calculator` class instance inside this method:

private Calculator \_calculator;
\[SetUp\]
public void Setup()
{
    \_calculator = new Calculator();
}

We have another attribute that runs just once before all test cases run. It’s named `OneTimeSetup`. 

![The Web API Production Checklist, free ebook](https://code-maze.com/wp-content/uploads/ebooks/covers/cover-beige-2-chevron-400.webp)

Free ebook

Is your Web API ready for production?

33 things to check before you ship, with the fix for each one. A free 76-page PDF for .NET 10.

[Get the free checklist](https://code-maze.com/free-ebook-aspnetcore-webapi-best-practices/?box=1)

Free PDF. One email to send it. Unsubscribe any time.

It depends on what kind of resources we are going to set up before test case execution. Sometimes we have a strict restriction to use a single instance of an object between all test cases and using the `OneTimeSetup` method to create such an object is the best option.

Also, we have replacements for the `Setup` attributes that we can use to execute code after the test case is finished. The attributes as `TearDown` and, accordingly, `OneTimeTearDown` give us such ability. 

## **Unit Test Metadata**

In a huge project, we can end up with a very large number of unit tests. In that case, we can use additional metadata attributes to add information to our unit tests.

Later we can run tests relying on specific values provided by metadata attributes. 

### **Author**

Test framework can’t check git history and determine the author of a test. To do that, we need to mark the test method with the `[Author]` attribute:

\[Author("Andrew")\]
\[Test\]
public void WhenHasAuthor\_ThenCanAccessItInCode()
{
    var expected = "Andrew";
    // Act
    var author = (string)TestContext.CurrentContext.Test.Properties.Get("Author");
    // Assert
    Assert.AreEqual(author, expected);
}

### **Description**

If the intention of the test case is not clear, it’s possible to provide additional descriptions to clarify what exactly is tested inside the test case. It’s helpful when we run tests automatically and give the test framework additional information to display in the log message:

\[Test\]
\[Description("this is simple test case")\]
public void WhenHaveDescription\_ThenItsEasierToGetWhatItTests()
{
    //test logic
}

### MaxTime

In some cases, we need to verify that method works fast enough. We can use `[MaxTime]` attribute to specify a maximum time for a test case to succeed. When the method exceeds the defined time it fails with a proper explanation:

\[MaxTime(1000)\]
public async Task WhenTakesMoreTime\_ThenItFails()
{
     await Task.Delay(1100);

     // Assert
     Assert.IsTrue(true);
}

### **Category**

The `[Category]` attribute marks that test related to a specific feature, and it allows us to run a set of unit tests for the feature without running all other tests. 

In huge projects, this saves a lot of time to run just a few tests for a new feature instead of running thousands of existing tests:

\[Test\]
\[Category("simple\_tests")\]
public void WhenHaveCategory\_ThenItCanBeInvokedWithCategoryFilder()
{
    //test logic
}

## **Conclusion**

NUnit provides a variety of tools for writing unit tests in C#. This test framework is pretty popular in the .NET community. In this article, we’ve learned how to use it to create unit tests and how to provide additional metadata for these tests.
