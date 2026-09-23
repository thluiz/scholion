---
url: "https://blog.elmah.io/3-essential-techniques-for-managing-transactions-in-ef-core/"
captured_at: "2026-09-23T18:58:18+01:00"
title: "3 Essential Techniques for Managing Transactions in EF Core"
domain: "blog.elmah.io"
---

3 Essential Techniques for Managing Transactions in EF Core
   
Written by Ali Hamza Ansari, September 24, 2024

Transaction are a crucial concept in database operations. It helps in updating related data safely without leaving the database state inconsistent. Entity Framework Core (EF Core) provides a mechanism to wrap database operations as transactions. In this blog post, we will see what a transaction is and how we can implement it in EF Core.

What is a Database Transaction

A transaction is a set of database operations treated as a work unit. If one of the operations fails, the whole transaction fails. This ensures data consistency and integrity when adding, updating, or deleting data. If any operation fails in the transaction, all the preceding successful operations are rolled back to keep the database consistent.

What are Transactions in EF Core?

EF Core provides different transaction techniques. We will implement three of the most common methods.

Automatic Transaction: The SaveChangesAsync() method of DbContext commits all the changes in a transaction. If any operation fails,  all changes are rolled back.
Manual Transaction: This technique allows the user to manually place the begin, commit, and rollback commands for transactions. It uses the Database property of the DbContext to call the commands.
Transaction with strategy: This highly customized technique works above the SaveChangesAsync method. It creates a strategy that may have multiple SaveChangesAsync updates to the database. However, those changes are not committed until the transaction commits them using the transaction.CommitAsync() method.
Technique 1: How to add Automatic transactions 

Consider we have to add multiple buildings. Simply add them and commit them using SaveChangesAsync().

We are not going to do any pre-code setup or explanation. Just this is the Building model.

public partial class Building
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Address { get; set; }
}

try
{
    using var context = new ApplicationDbContext();
    Building building1 = new Building()
    {
        Name = "Alma Tower",
        Address = "13th Street. 47 W 13th St, New York"
    };

    context.Buildings.Add(std1);

    // This will automatically use a transaction.
    context.SaveChangesAsync();
    
    Building building2 = new Building()
    {
        FirstName = "Betway House",
        LastName = "101 Independence Avenue, S.E.. Washington, D.C"
    };

    context.Buildings.Add(std2);

    // This will automatically use a new transaction.
    context.SaveChangesAsync();
    Console.WriteLine("Entities are Saved");
    Console.Read();
}
catch (Exception ex)
{
    Console.WriteLine($"Error: {ex.Message}"); ;
}


Each call to SaveChangesAsync automatically starts a new transaction if one is not already in progress. This means that all the changes made to the context up until that point are saved in the database as a single unit of work, ensuring data consistency. 

 Pros

The simplest way for transactions, as no additional method is required.
For saving data, the context is already called SaveChangesAsync by default. Hence, it is automatic.
Performs transactions asynchronously, improving the application's responsiveness.

Cons

SaveChangesAsync has limited Transaction Scope because it treats every operation as a transaction. 
There is no control over transactions because they are automatically managed.
Cannot apply for interdependent operations.
Technique 2: How to add manual transactions

This transaction treats each SaveChangesAsync call as the completion of one operation. Different calls are enclosed in the transaction, which starts with Database.BeginTransaction. Upon successful execution of all the operations, the transaction.Commit() method commits all changes as one transaction. Consider a web API that saves multiple Buildings in one API call.

public class BuildingRepo: IBuildingRepo
{
    private readonly ApplicationDbContext _context;
    public BuildingRepo(ApplicationDbContext context)
    {
        _context = context;
    }

    public async Task<bool> CreateBuildingsAsync(List<Building> building)
    {
        // Begin a new transaction
        using (var transaction = context.Database.BeginTransaction())
        {
            try
            {
                foreach (var building in buildings)
                {
                    _context.Buildings.Add(building);
                    _context.SaveChangesAsync();
                }

                // If everything works until here, commit the transaction
                transaction.Commit();
                return true;
            }
            catch (Exception ex)
            {
                // If an exception is thrown, roll back the transaction
                transaction.Rollback();
                // Handle or throw the exception as needed
                Console.WriteLine(ex.Message);
                throw;
            }
        }
    }
}


Pros

This technique provides full control over the transaction. Hence, you can manually commit and roll back. 
It provides better error handling with catch exceptions and liberty to handle different errors differently.
Suitable for complex scenarios where multiple data need to be inserted.

Cons

The code adds complexity with additional transaction handling code and block usage.
The process is prone to overhead if used unnecessarily.
It requires manual management of transaction code, hence slightly down readability.
Technique 3 How to add transactions strategy 

Our final method creates an execution strategy in which transactions are managed. It keeps trying database operations a specified number of times if the transaction fails due to a transient error. This iterative behavior ensures that minor issues do not affect the actual operations. 

Here, we assume a scenario for complex API input. The database now has different units in addition to buildings. Building Units are dependent on buildings:

public class BuildingUnit
{
    public int Id { get; set; }
    public string UnitNumber { get; set; } = string.Empty;
    public string UnitType { get; set; } = string.Empty; // e.g., "Office", "Apartment"
    public int FloorNumber { get; set; }

    // Foreign key to Building
    public int BuildingId { get; set; }

    // Navigation property
    public Building Building { get; set; }
}


Creating its input model:

public class BuildingUnitInp 
{ 
    public string UnitNumber { get; set; } = string.Empty;
    public string UnitType { get; set; } = string.Empty; 
    public int FloorNumber { get; set; }
}

public class BuildingDtoInp
{
    public string Name { get; set; }
    public string Address { get; set; }

    // Taking multiple Units for a building
    public List<BuildingUnitInp> BuildingUnits { get; set; } = new List<BuildingUnitInp>();
}

public class BuildingRepo: IBuildingRepo
{
    private readonly ApplicationDbContext _context;

    public BuildingRepo(ApplicationDbContext context)
    {
        _context = context;
    }

    public async Task<bool> CreateBuildingsAsync(BuildingDtoInp input)
    {
        // Create an execution strategy for handling transient failures
        var strategy = _context.Database.CreateExecutionStrategy();

        // Use the execution strategy to execute the following block of code
        return await strategy.ExecuteAsync(async () =>
        {
            // Start a new database transaction asynchronously
            using (var transaction = await _context.Database.BeginTransactionAsync())
            {
                try
                {
                    var building = new Building()
                    {
                        Name = input.Name,
                        Address = input.Address
                    };

                    // First saving the Building
                    _context.Buildings.Add(building);
                    await _context.SaveChangesAsync();

                    foreach (var unit in input.BuildingUnits)
                    {
                        _context.Add(new BuildingUnit()
                        {
                            // Adding foreign key of the newly created building
                            BuildingId = building.Id,
                            UnitNumber  = unit.UnitNumber,
                            UnitType   = unit.UnitType ,
                            FloorNumber   = unit.FloorNumber 
                        });
                    }

                    await _context.SaveChangesAsync();

                    // Commit the transaction if all operations succeed
                    await transaction.CommitAsync();      
                }
                catch (Exception ex)
                {
                    // Rollback the transaction if any operation fails
                    await transaction.RollbackAsync();
                    throw; // Re-throw the exception to let the execution strategy handle it
                }
            }
        }
    });
}


The whole block works as a transaction. Upon a transient failure, the execution strategy retries the entire operation, starting from the beginning of the block as defined in ExecuteAsync.

Pros

Strategy can handle transient failure, which improves the responsiveness and robustness of the application.
Ideal for complex scenarios and interdependent operations.
Offers customization for the transaction along with resilience over network failures. 

Cons

It is complex to write and understand strategy along with transactions.
Multiple blocks and scopes affect code readability 
The strategy-based transaction can downgrade application performance if not correctly configured.
Summary

This article profoundly dives into using transactions in the EF Core world. Transactions are essential to database applications to prevent critical data from being inconsistent. The article discussed 3 most common ways to write transactions: Automatic, manual, and strategy-based. Then we compared all of them based on their pros and cons. 

 PREVIOUS POST
Caching Strategies in ASP.NET Core
NEXT POST 
Boosting Code Readability and Manageability in ASP.NET Core
elmah.io: Error logging and Uptime Monitoring for your web apps

This blog post is brought to you by elmah.io. elmah.io is error logging, uptime monitoring, deployment tracking, and service heartbeats for your .NET and JavaScript applications. Stop relying on your users to notify you when something is wrong or dig through hundreds of megabytes of log files spread across servers. With elmah.io, we store all of your log messages, notify you through popular channels like email, Slack, and Microsoft Teams, and help you fix errors fast.

See how we can help you monitor your website for crashes

Copyright

•

Guest posts
