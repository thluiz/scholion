---
url: "https://jeremydmiller.com/2024/08/29/why-and-how-marten-is-a-great-document-database/"
captured_at: "2026-09-25T17:05:55+01:00"
title: "Why and How Marten is a Great Document Database"
domain: "jeremydmiller-com"
---

_Just a reminder, [JasperFx Software](https://jasperfx.net/) offers [support contracts and consulting services](https://jasperfx.net/support-plans/) to help you get the most out of the “Critter Stack” tools ([Marten](https://martendb.io/) and [Wolverine](https://wolverinefx.io/))._ _If you’re building server side applications on .NET, the Critter Stack is the most feature rich tool set for Event Sourcing and Event Driven Architectures around. And as I hope to prove to you in this post, Marten is a great option as a document database too!_

[![](https://jeremydmiller.com/wp-content/uploads/2016/09/banner.png?w=1024)](https://jeremydmiller.com/wp-content/uploads/2016/09/banner.png)

[Marten](https://martendb.io/) as a project started as an ultimately successful attempt to replace my then company’s usage of an early commercial “document database” with the open source PostgreSQL database — but with a small, nascent event store functionality bolted onto the side. With the exception of LINQ provider related issues, most of my attention these days is focused on the event sourcing side of things with the document database features in Marten just being a perfect complement for [event projections](https://martendb.io/events/projections/).

This week and last though, I’ve had cause to work with a different document database option and it served to remind me that hey, Marten has a very strong technical story as a document database option. With that being said, let me get on with lionizing Marten by starting with a quick start.

Let’s say that you are building a server side .NET application with some kind of customer data and you at least start by modeling that data like so:

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

`public` `class` `Customer`

`{`

    `public` `Guid Id {` `get``;` `set``; }`

    `public` `Dictionary<IncidentCategory, IncidentPriority> Priorities {` `get``;` `set``; }`

        `=` `new``();`

    `public` `string``? Region {` `get``;` `set``; }`

    `public` `ContractDuration Duration {` `get``;` `set``; }`

`}`

`public` `record ContractDuration(DateOnly Start, DateOnly End);`

`public` `enum` `IncidentCategory`

`{`

    `Software,`

    `Hardware,`

    `Network,`

    `Database`

`}`

`public` `enum` `IncidentPriority`

`{`

    `Critical,`

    `High,`

    `Medium,`

    `Low`

`}`

And once you have those types, you’d like to have that customer data saved to a database in a way that makes it easy to persist, query, and load that data with minimal developmental cost while still being as robust as need be. Assuming that you have access to a running instance of PostgreSQL (it’s very Docker friendly and I tend to use that as a development default), bring in Marten by first adding a reference to the “Marten” Nuget. Next, write the following code in a simple console application that also contains the C# code from above:

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

`using` `Marten;`

`using` `Newtonsoft.Json;`

`await` `using` `var` `store = DocumentStore`

    `.For(``"Host=localhost;Port=5432;Database=marten_testing;Username=postgres;password=postgres"``);`

`var` `customer =` `new` `Customer`

`{`

    `Duration =` `new` `ContractDuration(``new` `DateOnly(2023, 12, 1),` `new` `DateOnly(2024, 12, 1)),`

    `Region =` `"West Coast"``,`

    `Priorities =` `new` `Dictionary<IncidentCategory, IncidentPriority>`

    `{`

        `{ IncidentCategory.Database, IncidentPriority.High }`

    `}`

`};`

`await` `using` `var` `session = store.LightweightSession();`

`session.Store(customer);`

`await` `session.SaveChangesAsync();`

`var` `customer2 =` `await` `session.LoadAsync<Customer>(customer.Id);`

`Console.WriteLine(JsonConvert.SerializeObject(customer2, Formatting.Indented));`

And that’s that, we’ve got a working usage of Marten to save, then load `Customer` data to the underlying PostgreSQL database. Right off the bat I’d like to point out a couple things about the code samples above:

*   **We didn’t have to do any kind of mapping** from our `Customer` type to a database structure. Marten is using JSON serialization to persist the data to the database, and as long as the `Customer` type can be bi-directionally serialized to and from JSON, Marten is going to be able to persist and load the type.
*   **We didn’t specify or do anything about the actual database structure**. In its default “just get things done” settings, Marten is able to happily detect that the necessary database objects for `Customer` are missing in the database, and build those out for us on demand

So that’s the easiest possible quick start, but what about integrating Marten into a real .NET application? Assuming you have a reference to the Marten nuget package, it’s just an `IServiceCollection.AddMarten()` call as shown below from a sample web application:

1

2

3

4

5

6

7

8

9

10

`builder.Services.AddMarten(opts =>`

    `{`

        `var` `connectionString = builder.Configuration.GetConnectionString(``"postgres"``);`

        `opts.Connection(connectionString);`

    `})`

    `.UseLightweightSessions();`

At this point in the .NET ecosystem, it’s more or less idiomatic to use an `Add[Tool]()` method to integrate tools with your application’s `IHost`, and Marten tries to play within the typical .NET rules here.

_I think this idiom and the generic host builder tooling has been a huge boon to OSS tool development in the .NET space compared to the old wild, wild west days. I do wish it would stop changing from .NET version to version though._

So that’s all a bunch of simple stuff, so let’s dive into something that shows off how Marten — really PostgreSQL — has a much stronger transactional model than many document databases that only support eventual consistency:

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

`public` `static` `async` `Task manipulate_customer_data(IDocumentSession session)`

`{`

    `var` `customer =` `new` `Customer`

    `{`

        `Name =` `"Acme"``,`

        `Region =` `"North America"``,`

        `Class =` `"first"`

    `};`

    `session.Insert(customer);`

    `session.Patch<Customer>(x => x.Region ==` `"EMEA"``)`

        `.Set(x => x.Class,` `"First"``);`

    `await` `session.SaveChangesAsync();`

    `var` `customers =` `await` `session.Query<Customer>()`

        `.Where(x => x.Class ==` `"First"``)`

        `.Take(100)`

        `.ToListAsync();`

`}`

That’s a completely contrived example, but the point is, because Marten is completely ACID-compliant, you can make a range of operations within transactional boundaries and not have to worry about eventual consistency issues in immediate queries that other document databases suffer from.

So what else does Marten do? Here’s a bit of a rundown because Marten has a significantly richer built in feature set than many other low level document databases:

*   Multi-tenancy options built in, with both [a “conjoined” model](https://jeremydmiller.com/2024/05/20/multi-tenancy-martens-conjoined-model/) and [a first class database per tenant model](https://martendb.io/configuration/multitenancy.html)
*   [LINQ provider support](https://martendb.io/documents/querying/linq/) with some Marten specific features.
*   [Batch querying support](https://martendb.io/documents/querying/batched-queries.html)
*   [Indexing options](https://martendb.io/documents/indexing/)
*   [Optional soft delete suppor](https://martendb.io/documents/deletes.html#soft-deletes)t
*   Fine-grained control over identity map or automatic dirty checking to run lighter for better performance — or to opt into the heavier automatic dirty checking for convenience. The point here is that you have control
*   [Optimistic concurrency protections](https://martendb.io/documents/concurrency.html) on a document by document type

And quite a bit more than that, including some test automation support I really need to better document:/

And on top of everything else, because Marten is really just a fancy library on top of PostgreSQL — the most widely used database engine in the world — Marten instantly comes with a wide array of solid cloud hosting options as well as being deployable to local infrastructure on premise. PostgreSQL is also very Docker-friendly, making it a great technical choice for local development.

If you’re not familiar with the term “document database,” it refers to a type of NoSQL database where data is almost inevitably stored as JSON data, where the database allows you to quickly marshal objects in code to the database, then query that data later right back into the same object structures. The huge benefit of document databases at development time is being able to code much more productively because you just don’t have nearly as much friction as you do when dealing with any kind of object-relational mapping with either an ORM tool or by writing SQL and object mapping code by hand.

**Published** August 29, 2024August 29, 2024

## Post navigation
