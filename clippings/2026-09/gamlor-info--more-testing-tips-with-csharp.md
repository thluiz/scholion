---
url: "https://gamlor.info/posts-output/2024-12-11-csharp-testing-stuff/en/?utm_source=newsletter.csharpdigest.net&utm_medium=newsletter&utm_campaign=the-impact-of-locks-and-waits-on-latency&_bhlid=c6a32769d7d59536ee2ffdf5867fbd7fbe6a953b"
captured_at: "2026-09-25T08:48:53+01:00"
title: "More Testing Tips With C#"
domain: "gamlor-info"
---

_This post is part of [C# Advent Calendar 2024](https://www.csadvent.christmas/). Visit [it](https://www.csadvent.christmas/) for all the awesome upcoming posts! It was released on 11 December as a substitution for the 8th December spot, as another blogger couldn’t make it._

The traditional [C# Advent](https://www.csadvent.christmas/) is here. It also seems tradition I talk about some testing aspect \[[1](#_footnotedef_1 "View footnote.")\] or some outsider view approach to C# \[[2](#_footnotedef_2 "View footnote.")\] here. Let’s not break this tradition and I share some more testing tips.

[![Excitement](https://gamlor.info/posts/2024-12-11-csharp-testing-stuff/excited.jpg)](https://gamlor.info/posts/2024-12-11-csharp-testing-stuff/excited.jpg)

Figure 1. Excitement

## Fake Data with Faker.NET or Bogus.NET

In testing you often need example data. Creating data yourself isn’t hard, but tedious work. Therefore, the test data often does not look realistic at all. This is where test data generator libraries come it and give you decent test data.

[![Test Data](https://gamlor.info/posts/2024-12-11-csharp-testing-stuff/test-data.jpg)](https://gamlor.info/posts/2024-12-11-csharp-testing-stuff/test-data.jpg)

Figure 2. Test Data

### Faker.NET

The first one is `Faker`. It originated in the Ruby world and there exists multiple forks for the C#/.Net. For example I used this [Faker.Net](https://github.com/oriches/faker-cs) one.

Once you’ve added it to your project, use the static `Faker` class to generate some test data:

```
var city = Faker.Address.City();
var street = Faker.Address.StreetAddress();
var someText = Faker.Lorem.Paragraph();

Console.WriteLine($"City: {city}");
Console.WriteLine($"Street: {street}");
Console.WriteLine($"Text: {someText}");

// Example output:
// City: New Toyville
// Street: 4787 Cole Squares
// Text: Voluptas et omnis enim dignissimos quis aliquam omnis sit.....
```

Faker will give you sane and English centric data. It is not a library to find edge cases, but to get "human" samples.

### Bogus.NET

[Bogus.NET](https://github.com/bchavez/Bogus) goes further and provides a whole slew of utilities to create test data.

Like factories for your data objects:

```
var studentFaker = new Bogus.Faker<Student>(locale:"de_CH")
    .CustomInstantiator(f => new Student(f.Name.FirstName(), f.Address.StreetAddress(), f.Address.City()));

Console.WriteLine(studentFaker.Generate());

// Example output:
// Student { Name = Abigayle, Street = 42252 Abbie Trace, City = Angietown }
```

It supports multiple locales, if you want go beyond the English speaking world:

```
var studentFaker = new Bogus.Faker<Student>(locale:"ko")
    .CustomInstantiator(f => new Student(f.Name.FirstName(), f.Address.StreetAddress(), f.Address.City()));

Console.WriteLine(studentFaker.Generate());

// Example output:
// Student { Name = 민서, Street = 959 방배동, City = 구리구 }
```

Bogus has tons of other goodies:

*   More data sets
    
*   Some edge case testing data sets
    

### Seeds and Testing

I often use test data generators for testing to write more generalized tests that do not repeat the same hard coded values.

A simple example looks something like this:

```
[Test]
public void Find_Student_By_Name()
{
    var studentGenerator = new Bogus.Faker<Student>(locale:"ko")
        .CustomInstantiator(f => new Student(f.Name.FirstName(), f.Address.StreetAddress(), f.Address.City()));
    var toTest = new StudentApi();

    var student = studentGenerator.Generate();
    toTest.Store(student);

    var found = toTest.FindStudent(student.Name);
    Assert.AssertThat(found, Is.EqualTo(found));
}
```

If you write tests like that, you want to control the seed you use. So that, when a test fails you can reuse the same seed to reproduce the data. You can do that globally or per `Bogus.Faker` instance:

```
// Setting the global see for the Bogus libra
var seed = Random.Shared.Next();
Console.WriteLine($"Test suite is using seed: {seed}");
Bogus.Randomizer.Seed = new Random(seed);

// Or a seed for a specific faker instance
var seed = Random.Shared.Next();
Console.WriteLine($"Test suite is using seed: {seed}");
var studentGenerator = new Bogus.Faker<Student>(locale: "ko")
    .UseSeed(seed)
```

Last note: This style of tests are simple property based tests, as they use random data and test if certain property of the system holds. There are whole testing approaches based on this idea, but that outside the scope of this post.

## Test Against Know Reference Data

This is a basic test idea: Store a `good` reference of some output and compare it against the current result. This works well for things like rendering code (eg generated HTML, pictures, SVG).

[![Compare](https://gamlor.info/posts/2024-12-11-csharp-testing-stuff/compare.jpg)](https://gamlor.info/posts/2024-12-11-csharp-testing-stuff/compare.jpg)

Figure 3. Compare

Basically, do something like this:

```
[Test]
public void RenderTitleToHtml()
{
    TestRender(new ThingToRender("h1", "test"), "title-render");
}

[Test]
public void RenderParagraphToHtml()
{
    TestRender(new ThingToRender("p","test"),"p-render");
}

void TestRender(ThingToRender toRender, string testName)
{
    Directory.CreateDirectory("current");
    Directory.CreateDirectory("reference");
    var currentResult = SystemToTest(toRender);
    File.WriteAllText($"current/{testName}.html", currentResult);
    var readPrevious = File.ReadAllText($"reference/{testName}.html");
    Assert.That(readPrevious, Is.EqualTo(currentResult), $"Expected the rendering for {testName} to not change");
}
```

If the test breaks, you inspect the differences. If they are expected changes, you copy references from the `current` directory back to the `reference` directory and commit it.

Again, this works great for quite stable, rendering like code code. If the output changes frequently, this won’t work.

## Free-Ports, Free IPs

For integration test you often have to spawn some kind of mock server. How do you ensure this server can start on an unused port?

[![Free Ports](https://gamlor.info/posts/2024-12-11-csharp-testing-stuff/free-port.jpg)](https://gamlor.info/posts/2024-12-11-csharp-testing-stuff/free-port.jpg)

Figure 4. Free Ports

You can use the Socket class to find a free port:

```
Socket s = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
s.Bind(IPEndPoint.Parse("127.0.0.1:0"));
var port = ((IPEndPoint)s.LocalEndPoint).Port;
s.Close();

Console.WriteLine($"Free port {port}");
```

I had even more rare case where the port was fixed, because a library/external app doesn’t support reconfiguring the port. Lucky you, your machine has tons of IPs! The IP `127.0.0.1` is well known, but the whole 127.0.0.0/8 IP range is your machine! You have 16Million IPs for your tests:

Socket serverOne= new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
serverOne.Bind(IPEndPoint.Parse("127.0.0.2:8080"));

Socket serverTwo= new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
serverTwo.Bind(IPEndPoint.Parse("127.0.0.3:8080"));

## Summary

Ok, happy holidays and testing in C#.
