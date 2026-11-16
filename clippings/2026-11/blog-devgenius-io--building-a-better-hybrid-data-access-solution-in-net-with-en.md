---
url: "https://blog.devgenius.io/building-a-better-hybrid-data-access-solution-in-net-with-entity-framework-repodb-d1039a648301"
captured_at: "2026-11-16T17:52:51+00:00"
title: "Building a Better Hybrid Data Access Solution in .NET with Entity Framework + RepoDb"
domain: "blog-devgenius-io"
---

Building a Better Hybrid Data Access Solution in .NET with Entity Framework + RepoDb
Michael Camara Pendon
13 min read
·
Jul 12, 2020

TL;DR: Entity Framework is so “good” to use, but it is “best” if combined with RepoDb. Please do not miss this gem! 💎

Entity Framework, an ORM developed by Microsoft, is the most common ORM used by most .NET developers. It is coupled enough to the language and almost have everything implemented on its own way.

RepoDb is a new hybrid micro-ORM library for .NET, designed to cater the missing pieces of micro-ORMs and macro-ORMs (aka full-ORMs). It helps the developer to simplify the software development when using the advance features for advance use-cases.

I am Mike, the author of RepoDb, an open-source contributor and a technical blogger. I am currently working as Senior Application Architect of Offshore Wind at Orsted A/S, a Danish-based Renewable Energy company, named as the most sustainable company in the world. I worked hard on RepoDb to improve the space of data access in .NET. I personally ask your support towards this library. I hope you share, you blog and use it.

I am writing this article to showcase the real-world problems we had collected while designing and developing software applications for our businesses while using Entity Framework and, how did we solved those. The use-cases covered on this article could be “basics” or “advance”, but mostly those “unseen” by most .NET developers during the software development. Though some are realized after the production deployment, but is often ignored due to time-constraints, technical capabilities, limited resources, etc.

Disclaimer: Entity Framework is hugely used ORM in our organization. But the topics could be huge to cover everything, so, I will limit the content of this article only to our findings and, how did we solved those with RepoDb.

Basic Problems are Often Ignored 💥

Entity Framework is an ORM that has huge feature-set. It has too many abstractions implemented on top of the underlying RDBMS, resulting to a less development controllability and limited accessibility on the database capability/features.

What is it all about? You as a developer is limited to what Entity Framework can provide you, but not to what the underlying RDBMS can provide you.

But what’s the basic problem that I am talking about? It is pertained to the unseen problems we usually overlooked during the development, since the code implementation we wrote is working-as-expected. I am aiming to showcase the “deviations” when being compared to “writing it on a more robust way”.

Let us see some simple real-world scenarios and use-cases.

Simple Scenario #1 — Inline Update

Supposed you are aiming to only update a single column from the Customer table with 15 columns. You wrote the code below.

The code above seems to be perfectly fine as the aim is to only update the Address column. However, without you knowing behind the scene, Entity Framework does the update to “all” columns of the Customer table.

The risk is huge in relation to concurrency-conflict. Data at hand needs to be always the “latest” prior to the modification, otherwise, a dirty and an outdated data may be committed to the database.

Do not push and invent; avoid injecting a data entity directly like the code below. By doing such, other columns will be set to null or empty.

On the other hand, by creating a separate model that only contains the targeted columns and have a dedicated DbSet<T> created will also not work if your use-case is dynamic.

So the last resort is to fall-back to a raw-SQL execution, forcing you to leave the desired code-fluency. It is doable, but with some discretion on your side.

RepoDb solves this problem in a very efficient manner. The way we update the row is targeted by simply passing only the “key” + the “target columns”. Please see the code below.

Simple Scenario #2 — Delete

Supposed you would like to delete an existing record. By doing such activity, you first need the reference to the actual object and then delete that referenced-object afterwards. In short, you need to do a round-trip from the database.

Below is the ideal call, but such method is not present in Entity Framework.

Though, you can do the hack like the code below if you project the value of the primary/identity property for “John Doe”.

RepoDb solves this delete operation in a more direct way with the code below. Either way will work.

Simple Scenario #3 — Upsert/Merge

Supposed you would like to insert a new record (if not yet exists) or update (if already exists) in the database. This kind of use-case is quietly important in most cases.

In the case of Entity Framework, we usually write the code below.

The code above did a round-trip from the database. The data is first checked for existence and then get inserted or updated afterwards. Imagine if such code is part of one-of-the-busiest method in the application, it may utilize double resources than normal in the server.

RepoDb solves this upsert operation by simply calling the “Merge” operation. There is no round-trip in the database, but it does the same functionality.

By default, if the qualifier is not defined, then it uses the primary column of the table.

Always ensure to have the proper indexed provisioned on the qualifier columns to further maximize the RDBMS performance.

The “Best” Solution is with Micro-ORM(s) 🙌

With micro ORM, you “as developer” controls the flow of the development. Though some basic operations are given by default, but it is mainly you are responsible for most of the implementation. In short, you are not limited to what the framework can provide you.

What RepoDb has brought you are the solutions that can be found in-between micro-ORM(s) and full ORM(s). These solutions help you simplify the implementation of the “things” during the development (i.e: 2nd Layer Caching, Tracing, Repositories, Batch/Bulk Operations, etc).

Try to look at the things like inserting thousand or even million of rows into the database. Such operations could not be handled by Entity Framework in a very fast and efficient manner. It is also “very tedious” to implement the solutions in micro-ORM. Whereas in RepoDb, it is an out-of-the-box feature.

Entity Framework is no-doubt a really cool library to use, but in some cases, it is not practical and/or nor optimal. It is highly recommended to combine it with a much more robust framework like RepoDb. I, itself, tend to always look and recommend a “proper” solution over a “niche” solution.

There may be few hidden RDBMS accessibility-limitation when using Entity Framework because of its huge features. Nonetheless, we all need “extra” spices to cook-up the proper solutions.

Edge Scenario #1: Bulk Operations are out-of-scope in Entity Framework, out-of-the-box in RepoDb 🏃

These operations are widely-known to be the most fastest solution to process thousand or million of rows in one-go. Though Entity Framework supported the “batch” operations by default, but such operations are not enough to cater huge load of data.

Try to see an engaging example, below is a very basic benchmark of the differences between the actual method calls. (Tested with Person table with 7 columns for 100 K rows, Batch Operations: RepoDb.InsertAll, EF.AddRange, Bulk Operations: RepoDb.BulkInsert).

The project above can be found here

Imagine how much “resources” and “time” your application has saved when using the real “bulk” operations. It turns the 18.96 seconds down to less than a second.

Implementing the Bulk operations (i.e.: BulkInsert, BulkMerge, BulkUpdate and BulkDelete) requires too much time and effort for the developers to accomplish. It is not just tedious, it is also difficult to maintain afterwards. In RepoDb, it is an out-of-the-box feature for SQL Server.

For you to have a high-level idea, the diagram below show the actual data-flow of the BulkInsert operation.

And simply click any of the links below to visit the corresponding diagram.

BulkMerge
BulkUpdate
BulkDelete

That being said, the “bulk” operations are worth having feature.

Edge Scenario #2: Dynamic Execution for Targeted Operations 🚀

Entity Framework is highly-coupled to a model via DbSet<T>, with this, you are limited to make a targeted operation. Mentioned in the above basic problems (i.e: Inline-Update, Delete, Merge), there is “no way” we can do the most optimal targeted operation with Entity Framework.

Targeted operation

It is an atomic and minute execution, only does the thing on its sole purpose. No more, no less!

If you work in the back-end, deleting a row from the DB only requires writing a SQL like below:

> DELETE FROM Table WHERE Id = @Id;

But Entity Framework always does the call below.

> SELECT Id, ... FROM Table WHERE Id = @Id;
> DELETE FROM Table WHERE Id = @Id;

You are always required to get the reference of the object before deleting it. That is how the implementation is and you have no choice but to inherit it. Though writing a customized raw-SQL is an option, but it would affect the code-fluency uniformity.

“Code-fluency” helps simplify the readability and unit-of-code. To some developers, it is a strict “compliance”.

As already mentioned above, RepoDb address this with the code below (any approach will work).

Well how about inserting and updating a specific column?

It is important to take note, not all columns of your table is “required” for you to limit the targeted operation towards it.

In some cases, a scenario of creating a “preliminary record” is necessary. This preliminary record only requires 2 to 3 columns of the table to have the initial values. Though the job can be done in Entity Framework, but there is no way to target specific columns, and again, you are bound to a model-based approach operation.

Entity Framework is asking you to fill-up the model and bring this model (with “all” columns) back to the database.

RepoDb on the other hand solve this problem with an “Insert” call like below. A dynamic object can be passed in the operation targeting only the desired table and columns.

This use-case is also true for the “Update” operation.

Do you like reusing a model to “project” multiple tables?

This scenario is quite important at some cases. If you ahead of time projected the schema of the tables and, you think some columns can be shared, then a common model can be reused any time. Entity Framework does not support this, where in RepoDb, it is an out-of-the-box feature using dynamics.

BTW, dynamic is rich in RepoDb, therefore, you can also work “without” having a model.

Though in general, using dynamic is known to be slow in C#. So do to whatever framework you use. Please be mindful of this.

Edge Scenario #3: You are just an Expert in Writing Raw SQL✍️️

Most developers tend to fall-back writing SQL in response to the use-cases cannot be handled by ORM alone. This is true to most cases as business demands are emergent most of the time.

Therefore, in the world of agile, we also need a fast-changing hybrid-solution to address it.

Triggered by the community request, it is the reason why “FromSqlRaw” and “FromSqlInterpolated” methods are now available in Entity Framework. However, Entity Framework is not designed to “dynamically” execute a raw-SQL statement. The mentioned methods was introduced late on top of its huge core features. Therefore the implementation is limited and not as performant and efficient as micro-ORM.

Micro-ORM on the other hand, the core implementations are to execute raw-SQL with “high-performance” and “memory-efficiency”, followed by the desired features that utilize those core implementations.

There is a huge difference in the implementation if you compare Entity Framework from a micro-ORM.

The FromSql* Mapping problem

In Entity Framework, both methods mentioned above (i.e.: FromRawSql, FromSqlInterpolated) has mapping problem that is also a candidate for a healthy debate. The developers cannot just simply execute the raw-SQL dynamically, some requirements need to strictly be followed (see below).

Model must be of type of DbSet<T>, still bound to a specific model
Resultset properties must always be present within the models

If you are working with Person table (of DbSet<Person>), you are always limited to that model. The resultset of the raw-SQL must be identical to the Person model “always”.

The code below will work as SQL<Person> to DbSet<Person>.

But the code below will fail as SQL<Customer> to DbSet<Person>.

An exception below is thrown.

System.InvalidOperationException: ‘The required column ‘XXX’ was not present in the results of a ‘FromSql’ operation.’

The execution is still bound to the model. The alternative solution is to create a new DbSet<Customer> property in the DbContext. Therefore such requirements limit the developers to execute the query “dynamically”.

Developers cannot map any model from the SQL statement
SQL statement must only be of the DbSet<T> generic type
Cannot add extra properties, specially for the resultsets returned by executing a stored procedure

RepoDb is designed to be dynamic ORM to cater such scenarios. Imagine writing a raw-SQL and just execute it in any way you liked.

Whether your resultset has an extra columns or your model has an extra properties, everything will be handled accordingly.

That being said, Entity Framework together with RepoDb has some spices that can be brought into the table.

Edge Scenario #4: Limit the Round-Trips, Just Cache It 🐢 → 🐇

Entity Framework does not support 2nd-Layer cache by default. It is one of the very-important feature that most solution is needed. It is also one of the reason why RepoDb exists nowadays.

Below is the diagram how the 2nd-layer caching works.

Assuming you are working on an E-Commerce site and one of the busiest page is the “Customer Product” page. The list of Product per Customer is not frequently changing or, at some cases, not changing at all.

Do you really need to do round-trip to the database to fetch those Products? Well, the solution is to simply cache it. As Entity Framework does not support it by default, you are obliged to create a customized caching mechanism and inject it as you query the data.

This feature is out-of-the-box to RepoDb. Just simply pass the “cacheKey” and everything will work like a charm.

Such feature also address important scenarios like:

Lookup tables
Joining multiple tables (client side)

By skipping the on-the-wire traffic is always best pertaining to efficiency and performance. By having a 2nd-layer cache mechanism, it is proven that 95% to 97% of the execution time is being saved.

Edge Scenario #5: Simplifying the Access for Multiple RDBMS Data Sources 💥

Within your solution, you might be working with SQL Server as your main data source. It is great if your use-case is only to use such RDBMS data provider.

There are use-cases in which the data is stored into multiple RDBMS data sources. It is quite tedious to bring all data into into a single solution if your framework is not generic enough. Though Entity Framework supports multiple RDBMS data provider, but you may sometime find yourself stuck when working with it.

Whereas, micro-ORM can be used to any RDBMS data sources for as long the IDbConnection object is open.

Multiple Data Source Combination Scenario

If you have a requirement of like “Experience API” and would like to bundle everything in one place, then it is quite hard to implement it in Entity Framework.

Imagine, you have your Customer record in Azure SQL Server, your Sales record and Orders record in AWS PostgreSQL, your Products record in Azure MySQL, etc. Bringing the data together in the “Experience API” is quite-tough for Entity Framework.

RepoDb address such scenarios for as long you have a open connection towards the data sources. See the sample code below.

Such implementation can be used in a dynamic way. You can even bring the data from one RDBMS data source to another RDBMS data source.

Multiple Data Source Integration Scenario

Imagine you would like to make a report of all the Customer records from SQL Server about the Orders made for the last month in which residing in PostgreSQL.

You can temporarily copy the data from Sales table of PostgreSQL and bulk-insert it towards the SQL Server.

It is easy and direct to do such thing in RepoDb. See the sample code below.

In the event the fluent calls are not supported from the source, then raw-SQL can be used in combination to the fluent operations in the destination.

Other Features, Not Discussed 🍕♻️

There are lot of things hidden in Entity Framework that could affect the efficiency and performance of your application. You just have to discover and find a better solution on top of it.

RepoDb is an ORM that most likely will give you the solutions but with almost EF-like experience when it comes to coding.

Below are the features you might as well be using on top of Entity Framework.

Hints / Query Optimizers
Tracing
Property Handlers
Implicit Mapping

The not-discussed features mentioned above are hugely used within our organization to support the advanced business use-cases. Most are already running in the Production environment.

Piece of Advice: Do not Overdo Everything, Consider Using the Other Libraries 🐧

Entity Framework is an ORM that is so cool to use. But I tried to explain the position where the Entity Framework is “best” and “not” to use. Different micro-ORM(s) exists on top of Entity Framework to address the things it cannot do.

There is the place where RepoDb comes from. The features were introduced to address the different problems encountered during the software development (probably in different domain and industry). The introduced solutions was validated and used itself by those people who has collected the knowledge.

OSS community is there to help addressing our problems. With the OSS libraries available in the market, various real-world problems has most likely been collected, discussed and solved already.

At the end of the day, it is up to you as a developer what to use. Either create a customize or leverage the already publicly available solution. Time is money, effort is knowledge!

Overall Conclusion 👋

Below are the conclusion in relation to this article, we hope you apply it on your own use-case.

Do not overdo the things with Entity Framework. It is no-doubt a cool framework but it has some limitations explained in this article. If you think it is not practical on your use-case, then combine it with RepoDb.
Always spend time finding the correct solution and the OSS world is there to help. Other solution can be beyond what Entity Framework and RepoDb can offer.
RepoDb is frank and direct; will give you the hybrid-solutions you may be needing in your software development.
Hybrid solution is always the “best” tool you can have during the software development.

~Thank you for reading this article!~ 🙏🏻👍🕵
