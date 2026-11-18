---
title: "Efficient Event Communication RabbitMQ: Implementing Event Bus and Outbox Patterns with CAP in .NET Core Microservices"
date: '2023-10-24T14:26:34+00:00'
category: webclip
summary: 'Step‑by‑step demo showing how to use CAP in .NET 8 microservices with RabbitMQ and SQL Server to implement an outbox‑style event bus between a publisher and consumer.'
tags: ["dotnet-core", "microservices", "event-bus", "rabbitmq"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Efficient Event Communication RabbitMQ: Implementing Event Bus and Outbox Patterns with CAP in .NET Core Microservices"
    url: "https://dev.to/ahmedshahjr/efficient-event-communication-implementing-event-bus-and-outbox-patterns-with-cap-in-net-core-microservices-36oe"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--cap-rabbitmq-outbox-event-bus-dotnet-core.md"
    kind: repo
---

The article introduces CAP, a .NET Standard library that implements the outbox pattern and acts as an EventBus to make distributed transactions and event communication more reliable. It walks through building two .NET 8 Web API projects (Publisher and Consumer) that use CAP with SQL Server and RabbitMQ so that customer creation events are stored in a local message table and delivered to subscribers, with monitoring via CAP’s dashboard and CAP.Published/CAP.Received tables.

## Reading notes

- CAP is presented as a way to integrate services in SOA/microservices using events while avoiding reliability issues that arise when using a simple message queue alone.
- CAP uses a local message table in the existing database to handle exceptions in distributed calls and to ensure event messages are not lost.
- The library is based on .NET Standard, targets distributed transactions, and also provides lightweight, efficient EventBus functionality.
- CAP is described as implementing the Outbox Pattern as referenced in the eShop ebook.
- The tutorial aims to show how to build a microservices event bus architecture with CAP, highlighting advantages over directly wiring services to a message queue and its built‑in features.
- Two .NET 8 Web API projects are created: one named Publisher and one named Consumer.
- The Publisher project adds NuGet packages for DotNetCore.CAP, CAP.Dashboard, CAP.RabbitMQ, CAP.SqlServer, OpenAPI, and Entity Framework Core.
- A Customer entity is defined, inheriting from a CustomerInsert class and adding an Id property initialized with a new Guid.
- The CustomerInsert class contains FirstName, LastName, and MobilNumber properties used as the input model.
- A ServiceDbContext is created inheriting from DbContext, with a DbSet<Customer> and a basic OnModelCreating override.
- A CustomerController is added, injecting ICustomerService and exposing a POST endpoint that calls AddCustomer and returns its result.
- The ICustomerService interface defines an AddCustomer method that accepts a CustomerInsert and returns a Task<bool>.
- CustomerService is implemented with dependencies on ServiceDbContext and ICapPublisher from DotNetCore.CAP.
- In AddCustomer, the service maps CustomerInsert into a Customer, saves it with EF Core, serializes the entity to JSON, and publishes a "CustomerAdded" event via ICapPublisher.
- The text explains that CAP’s publisher interface is injected into the service so that after inserting into the database, an event is published and stored in the database, to be examined later.
- appsettings.json in the Publisher project defines a DefaultConnection string pointing to a SQL Server database named Publisher.
- In Program.cs of Publisher, ServiceDbContext is registered with AddDbContext using SQL Server and the DefaultConnection string.
- CAP is configured to use Entity Framework with ServiceDbContext, SQL Server with the same connection string, the CAP dashboard under "/cap-dashboard", and RabbitMQ connection options pointing to localhost:5672 with guest credentials and SSL disabled.
- ICustomerService and CustomerService are registered in DI with AddScoped.
- A SQL Server database named Publisher is created, and EF Core migrations (InitialCreate) and database update are run for the Publisher Web API project.
- The Consumer project adds NuGet references for DotNetCore.CAP, CAP.RabbitMQ, CAP.SqlServer, and Microsoft.EntityFrameworkCore.SqlServer.
- A CustomerAddedEventSubscriber class is created in an event folder and implements ICapSubscribe to listen for events.
- The subscriber defines a Consumer method marked with [CapSubscribe("CustomerAdded")] that receives a JsonElement and writes the payload to the console.
- The article notes that this consumer class accepts a JSON element parameter representing the published data.
- The Consumer appsettings.json includes the same DefaultConnection string used by the Publisher project so both can share the events table.
- A MainDbContext is defined for the Consumer project, inheriting from DbContext with an empty OnModelCreating override and optional commented DbSet.
- In the Consumer’s Program.cs, MainDbContext is registered with AddDbContext using SQL Server and the shared connection string.
- CAP in the Consumer is configured with UseEntityFramework<MainDbContext>, UseSqlServer with the same connection, and RabbitMQ settings identical to the Publisher.
- The CustomerAddedEventSubscriber is registered as a singleton service so it can handle incoming events.
- RabbitMQ is pulled as a Docker image using `docker pull rabbitmq:3.10-management` and run through Docker Desktop.
- The solution is configured to start both Publisher and Consumer projects simultaneously as multiple startup projects in Visual Studio.
- When the applications run, CAP automatically creates two tables in the SQL Server database: CAP.Published and CAP.Received.
- Both CAP tables share the same columns; published events go into CAP.Published and consumed events are recorded in CAP.Received.
- The article suggests using the CustomerController in the Publisher to post a new customer and trigger event publishing.
- The Publisher app console output shows that an event is being inserted into the database in preparation for publishing.
- The Consumer app console shows the JSON data received from the Publisher’s event, confirming successful event delivery.
- The database can be queried with `select * From cap.Published` and `select * From cap.Received` to inspect event records.
- Column descriptions are given: Name is the event name, Group is used to group events, Content holds the main data, and StatusName indicates success or failure.
- The Content column stores the JSON payload of the event, which can be opened to view the customer data.
- The CAP Dashboard configured in the Publisher project allows viewing published and received events through the browser at the /cap-dashboard URL.
- Screenshots show the Dashboard’s ability to inspect event details in the Published and Received sections.
- The key takeaway emphasizes that the example is a minimal illustration of how CAP works with the outbox pattern and notes support for brokers like Kafka, RabbitMQ, and Azure Service Bus.
- CAP is said to support multiple databases, including SQL Server, MySQL, PostgreSQL, and MongoDB.
- The author remarks that in this demo EventBus logic is built directly into the Publisher, while real applications often encapsulate EventBus behavior in generic classes within a separate DLL shared across microservices.
