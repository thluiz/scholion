---
url: "https://dev.to/ahmedshahjr/efficient-event-communication-implementing-event-bus-and-outbox-patterns-with-cap-in-net-core-microservices-36oe"
captured_at: "2026-11-16T20:19:03+00:00"
title: "Efficient Event Communication RabbitMQ: Implementing Event Bus and Outbox Patterns with CAP in .NET Core Microservices"
domain: "dev-to"
---

## [](#softwares-needed)Software's needed

1.  Visual Studio 2022
2.  Docker Desktop with RabbitMQ image.

## [](#introduction)Introduction

In the process of building an SOA or MicroService system, we usually need to use the event to integrate each service. In the process, simple use of message queue does not guarantee reliability. CAP adopts local message table program integrated with the current database to solve exceptions that may occur in the process of the distributed system calling each other. It can ensure that the event messages are not lost in any case.

You can also use CAP as an EventBus. CAP provides a simpler way to implement event publishing and subscriptions. You do not need to inherit or implement any interface during subscription and sending process.

## [](#what-is-cap)what is CAP?

CAP is a library based on .net standard, which is a solution to deal with distributed transactions, also has the function of EventBus, it is lightweight, easy to use, and efficient.

**CAP implements the Outbox Pattern described in the eShop ebook**  
[![Image](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F1gd5j4zd4wnfuty3tm96.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F1gd5j4zd4wnfuty3tm96.png)

Learn how to build a microservices event bus architecture using CAP, which offers advantages over direct integration of message queues, and what out-of-the-box features it provides.

![](https://i.giphy.com/media/3aGZA6WLI9Jde/giphy.gif)

Create 2 new .NET core 8.0 web api projects name **Consumer** and **Publisher**.

[![Image](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Ft44klaoi67o5p49yldk8.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Ft44klaoi67o5p49yldk8.png)  
Add these Nuget packages in **Publisher** web api project.  

```
 <PackageReference Include="DotNetCore.CAP" Version="7.1.4" />
 <PackageReference Include="DotNetCore.CAP.Dashboard" Version="7.1.4" />
 <PackageReference Include="DotNetCore.CAP.RabbitMQ" Version="7.1.4" />
 <PackageReference Include="DotNetCore.CAP.SqlServer" Version="7.1.4" />
 <PackageReference Include="Microsoft.AspNetCore.OpenApi" Version="8.0.0-preview.5.23302.2" />
 <PackageReference Include="Microsoft.EntityFrameworkCore" Version="6.0.20" />
 <PackageReference Include="Microsoft.EntityFrameworkCore.Tools" Version="6.0.20">
```

Enter fullscreen mode Exit fullscreen mode

**Adding Customer Entity**  
Create a new folder data and a new class named **Customer**  
that inherits from customerinsert classs.  

```
 public class Customer: CustomerInsert
 {

     [Key]
     public Guid Id { get; set; }= Guid.NewGuid();
 }
 public class CustomerInsert
 {
     public string FirstName { get; set; }
     public string LastName { get; set; }
     public string MobilNumber { get; set; }
 }
```

Enter fullscreen mode Exit fullscreen mode

**Creating Db Context**  
Create **ServiceDbContext** class that inherits from DbContext.  

```

    public class ServiceDbContext : DbContext
    {
        public DbSet<Customer> customers { get; set; }
        public ServiceDbContext(DbContextOptions<ServiceDbContext> options)
            : base(options)
        {
        }
        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            base.OnModelCreating(modelBuilder);
        }

    }
```

Enter fullscreen mode Exit fullscreen mode

Now right click controller folder and add a new controller name Customer Controller with this code.  

```
 [Route("api/[controller]")]
 [ApiController]
 public class CustomerController : ControllerBase
 {

     private readonly ICustomerService _customerService;


     public CustomerController(ICustomerService customerService)
     {
         _customerService = customerService;

     }

     // POST api/<OrderController>
     [HttpPost]
     public async Task<IActionResult> Post([FromBody] CustomerInsert customer)
     {
         try
         {
             return Ok( await _customerService.AddCustomer(customer));
         }
         catch (Exception ex)
         {

             throw;
         }
     }


 }
```

Enter fullscreen mode Exit fullscreen mode

Create a new folder Services where we will create our **ICustomerService** and **CusomterService**

ICustomerService  

```
    public interface ICustomerService
    {
        Task<bool> AddCustomer(CustomerInsert order);

    }
```

Enter fullscreen mode Exit fullscreen mode

Customer Service  

```
    public class CustomerService : ICustomerService
    {
        private readonly ServiceDbContext _dbContext;
        private readonly ICapPublisher _capPublisher;

        public CustomerService(ServiceDbContext dbContext, ICapPublisher capPublisher)
        {
            _dbContext = dbContext;
            _capPublisher = capPublisher;
        }

        public async Task<bool> AddCustomer(CustomerInsert customerInsert)
        {
            Customer customer = new Customer
            {
                FirstName = customerInsert.FirstName,
                LastName = customerInsert.LastName,
                MobilNumber = customerInsert.MobilNumber,
            };

            await _dbContext.AddAsync(customer);
            await _dbContext.SaveChangesAsync();
            var content = JsonSerializer.Serialize(customer);
            await _capPublisher.PublishAsync<string>("CustomerAdded", content);
            return true;
        }
    }

```

Enter fullscreen mode Exit fullscreen mode

In our customer service we are injecting **ICapPublisher** and interface provided by **DotNetCore.CAP** package.  
in our add customer method we are adding a new customer in our database and informing other services using cappublished event handler that an event is being published. That event that is being published will be stored in our database which we will see later.

Let Configure our **program.cs** and **appdevelopment.json** for using database and configuration of our services and events.  
**appsettings**  

```
  "ConnectionStrings": {
    "DefaultConnection": "Data Source=.;Initial Catalog=Publisher;Trusted_Connection=True;Encrypt=False;"
  }
```

Enter fullscreen mode Exit fullscreen mode

**Program.cs**  

```
#region Creating Db Context
builder.Services.AddDbContext<ServiceDbContext>(options => options.UseSqlServer(builder.Configuration.GetConnectionString("DefaultConnection")));
#endregion
#region Add Cap library
builder.Services.AddCap(options =>
{
    options.UseEntityFramework<ServiceDbContext>();
    options.UseSqlServer(builder.Configuration.GetConnectionString("DefaultConnection"));
    options.UseDashboard(path => path.PathMatch = "/cap-dashboard");
    options.UseRabbitMQ(options =>
    {
        options.ConnectionFactoryOptions = options =>
        {
            options.Ssl.Enabled = false;
            options.HostName = "localhost";
            options.UserName = "guest";
            options.Password = "guest";
            options.Port = 5672;
        };
    });
});

#endregion
///adding services
builder.Services.AddScoped<ICustomerService, CustomerService>();
```

Enter fullscreen mode Exit fullscreen mode

Create New Database name **Publisher** in Sql Server Managment Studio.  
Generate Migrations in **Publisher** web api project using .net CLI  
`dotnet ef migrations add InitialCreate`  
and update our database and schema using this command

`dotnet ef database update`

> now our **publisher** project has been completed lets go to our **consumer** project and add the implementation for consuming our events that are being published.

add these Nuget packages in the project.  

```
    <PackageReference Include="DotNetCore.CAP" Version="7.1.4" />
    <PackageReference Include="DotNetCore.CAP.RabbitMQ" Version="7.1.4" />
    <PackageReference Include="DotNetCore.CAP.SqlServer" Version="7.1.4" />
    <PackageReference Include="Microsoft.EntityFrameworkCore.SqlServer" Version="6.0.20" />
```

Enter fullscreen mode Exit fullscreen mode

Create a new folder named event and add a class named **CustomerAddedEventSubscriber** that inherits from **ICapSubscribe** because we need to need listen to events that being published in this class.  

```
    public class CustomerAddedEventSubscriber : ICapSubscribe
    {
        [CapSubscribe("CustomerAdded")]
        public void Consumer(JsonElement customerData)
        {
            Console.WriteLine(customerData);
        }
    }
```

Enter fullscreen mode Exit fullscreen mode

we have added a cosnumer class that receives a json element as a pramater.

adding connection string in appsettings.json

> note the connection string needs to be same as our **publisher api project** since events are stored in database table.  

```
  "ConnectionStrings": {
    "DefaultConnection": "Data Source=.;Initial Catalog=Publisher;Trusted_Connection=True;Encrypt=False;"
  }
```

Enter fullscreen mode Exit fullscreen mode

Create **DbContext** and Configure **Program.cs** file.

## [](#dbcontext)DbContext

```
    public class MainDbContext:DbContext
    {
     //   public DbSet<CustomerData> customers { get; set; }
        public MainDbContext(DbContextOptions<MainDbContext> options)
            : base(options)
        {
        }
        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            base.OnModelCreating(modelBuilder);
        }

    }
```

Enter fullscreen mode Exit fullscreen mode

## [](#programcs)Program.cs

```
// Add dbcontext.
builder.Services.AddDbContext<MainDbContext>(options => options.UseSqlServer(builder.Configuration.GetConnectionString("DefaultConnection")));
//add cap implementation
builder.Services.AddCap(options =>
{
    options.UseEntityFramework<MainDbContext>();
    options.UseSqlServer(builder.Configuration.GetConnectionString("DefaultConnection"));

    options.UseRabbitMQ(options =>
    {
        options.ConnectionFactoryOptions = options =>
        {
            options.Ssl.Enabled = false;
            options.HostName = "localhost";
            options.UserName = "guest";
            options.Password = "guest";
            options.Port = 5672;
        };
    });
});
//add event handler service
builder.Services.AddSingleton<CustomerAddedEventSubscriber>();
```

Enter fullscreen mode Exit fullscreen mode

### [](#our-both-project-are-being-configured)Our both project are being configured

let install **RabbitMQ** image in docker desktop using this command.

> docker pull rabbitmq:3.10-management

Run Docker desktop and run start our RabbitMq image present in images section.

[![Image](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fjd9s4vh7ycxzyl9bgkcx.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fjd9s4vh7ycxzyl9bgkcx.png)  
RabbitMQ image is running run lets run our project.

Right click your solution and click select startup project use multiple projects select consumer and publisher project.  
Image Taken From RabbitMQ  
[![Image](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Ftvldrsy3pzbfhursm3xw.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Ftvldrsy3pzbfhursm3xw.png)  
Start the project  

![](https://i.giphy.com/media/uurtMtTKqkJda4dk8Y/giphy-downsized-large.gif)

Go to the database first we can see CAP has Created 2 new tables for us **CAP.Published** and **CAP.Received** lets examine them.

[![Image](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fxt4vntfli10g3um23t72.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fxt4vntfli10g3um23t72.png)

Both table has same number of column's. when we publish you event it will be saved in CAP.Published table and when our consumer consume the event the it will be added in CAP.Received table.  
Go the Customer Controller and add a new customer so we can publish some events too.

[![Image](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fjeklfidbah0lncs7gq0i.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fjeklfidbah0lncs7gq0i.png)

[![Image](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fwupvjzyr17uud5xj157a.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fwupvjzyr17uud5xj157a.png)  
In Publisher app console the event is being added in database for publishing

[![Image](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F5f4toxn5n3jcyusyczjp.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F5f4toxn5n3jcyusyczjp.png)

In Consumer Console we can see the output of our data the we published from Publisher api received successfully in consumer app.

[![Image](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fjcd2j4z2y8u2ykj9if3u.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fjcd2j4z2y8u2ykj9if3u.png)

Examine the database and select cap.published and received table  

```
select * From cap.Published
select * From cap.Received 
```

Enter fullscreen mode Exit fullscreen mode

[![Image](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F0zzjqd5ywilive1gfqhp.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F0zzjqd5ywilive1gfqhp.png)  
**Name:** Event Name this is being published.  
**Group:** Used to group Events  
**Content:** This the main column where our data is present.  
**Status Name:** Identifying that event is Succeeded or Failed.  
In Content column we have a Json Element parsed and saved in our column from the event examine it and see your data there.  
We can also see our data in **CAP Dashboard** that we added in publisher project by going to published and received tabs there. using the url the we configured for dashboard access in **Program.cs** file.  
`https://localhost:{yourport}/cap-dashboard`

[![Image](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fvkat54xy84fuhblzu18t.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fvkat54xy84fuhblzu18t.png)

[![Image](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F6xse6axt5mzgnzezgw61.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F6xse6axt5mzgnzezgw61.png)

![](https://i.giphy.com/media/zTyOZBq1WUY78bmqUv/giphy.gif)

### [](#key-take-away)Key Take Away

That’s the simplest example. And it’s pretty simple and hopefully gives you an idea of how CAP works with implementing the outbox pattern. There are various message brokers it supports such as Kafka, RabbitMQ, and Azure Service Bus. On the database side it supports SQL Server, MySQL, PostgreSQL, and MongoDB.

> In this project we are using EventBus implementation in our publish class but most of the time in real world application scenarios we implement EventBus implementation using generic classes in separate dll and that can be used in our overall microservices project. this is just simple demo project for beginners.
