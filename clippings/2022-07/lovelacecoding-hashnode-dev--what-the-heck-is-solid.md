---
url: "https://lovelacecoding.hashnode.dev/what-the-heck-is-solid?mkt_tok=NDI2LVFWRC0xMTQAAAGFbee8hcp2lDLSYrNQYAyzS07xDLppHmKD_9n0yaQfq3wGKBX7mzjUZfFMfxbj57GR8Es3NChOwtCOHXQeZlXtMx0_cYc7GohNhBjIcFvgW130Gkxv"
captured_at: "2022-07-06T11:46:36-03:00"
title: "What the heck is SOLID?"
domain: "lovelacecoding-hashnode-dev"
---

# Pre-requirements

This blog post discusses how to write cleaner and better structured Object Oriented code. It discusses virtual methods, enums, and interfaces. If these terms sound unfamiliar to you, it's probably too early to focus on SOLID, which is fine!

If you need a roadmap to learn Object Oriented Programming, [look at this awesome roadmap from GeeksforGeeks](https://www.geeksforgeeks.org/a-step-by-step-approach-to-learn-object-oriented-programming/)

# What actually is SOLID?

SOLID is an acronym for five very important design principles in software development that you should follow to keep your code structured, readable, and maintainable for others and yourself.
Keeping these principles in mind will make your life easier in the future, especially if your project grows in size or you haven't worked on it in a while.

The 5 design principles we’re talking about are:

**S**ingle Responsibility Principle

**O**pen-Closed Principle

**L**iskov Substitution Principle

**I**nterface Segregation Principle

**D**ependency Inversion Principle

Software engineer Robert Martin (Uncle Bob) coined the term "SOLID" to describe these principles.
He's also known from books such as 'Clean Code,' which is widely used in the field of software development.

Now with all this information, lets get started with the first principle.

# Single Responsibility Principle

The Single Responsibility Principle states that each method or function should have only one goal or reason for change.

Here’s an example:

```
public class Signup {

        public void checkDetailsUser()
        {
            //some code about validating the user input
        }

        public void registerUser() 
        {
            //some code about registering the user
        }

        public void sendWelcomeEmail()
        {
            //some code about sending a welcome email after signup
        }
}
```

Why? Using this principle means that if you get an unexpected result or exception in your code, you'll know almost exactly where it came from. It is also much easier for other developers to understand what is going on if you do not put all of your code in a single method

**Tip:** While we're talking about methods. Always strive to make the names as descriptive as possible (without making the name unreasonably long). Many software developers try to keep their methods under 20 lines long in order to keep everything readable.

# Open-Closed Principle

According to the open-closed principle, software entities should be open for extension but closed for modification.

This means that new entities in your project, such as classes, should be written in such a way that the functionality can be extended with other classes without having to rewrite the already existing class.

Let me show you an insufficient example:

```
public class Program
{
    public static void Main()
    {
        TaxStuff taxStuff = new TaxStuff();
        double amount = taxStuff.GetTax(12.96, ProductType.WithTaxLow);
        Console.WriteLine(amount); //prints 13.86

    }
}

public class TaxStuff
{
    public double GetTax(double amount, ProductType productType)
    {
        double finalAmount = 0;

        if(productType == ProductType.WithTaxHigh)
        {
            finalAmount = amount + (amount * 0.21);
        }

        else if(productType == ProductType.WithTaxLow)
        {
            finalAmount = amount + (amount * 0.07);
        }

        else
        {
            finalAmount = amount;
        }

        return finalAmount;
    }
}

public enum ProductType
{
    WithTaxHigh, WithTaxLow, WithoutTax    
}
```

This is a simple example of how different types of taxes can be applied to a product. The new price based on the tax is returned in the GetTax method.

The issue here is that if you want to add another ProductType, such as WithTaxMedium, you must add another else if statement. This means that the TaxStuff class will have to be altered if that happens. That is inconvenient, and the if-else block can quickly become lengthy, which can be risky.

This is a more sufficient way to do it:

```
public class Program
{
    public static void Main()
    {
        Product product = new Product();
        ProductHighTax highTax = new ProductHighTax();
        ProductLowTax lowTax = new ProductLowTax();

        double productAmount = product.GetTax(12.00);
        double productHighAmount = highTax.GetTax(12.00);
        double productLowAmount = lowTax.GetTax(12.00);

        Console.WriteLine(productAmount);
        Console.WriteLine(productHighAmount);
        Console.WriteLine(productLowAmount);

    }
}

public class Product
{
    public virtual double GetTax(double amount)
    {
        return amount;
    }
}

public class ProductHighTax : Product
{
    public override double GetTax(double amount)
    {
        return base.GetTax(amount) + amount * 0.21;
    }
}

public class ProductLowTax : Product
{
    public override double GetTax(double amount)
    {
        return base.GetTax(amount) + amount * 0.07;
    }
}
```

When you build a TaxCalculator with inheritance, you never have to change a class again. If you require an additional product tax type, you create a new class and include the product class in it. This way, it's extensible, but you don't have to modify the existing ones to do so.

# **L**iskov Substitution Principle

The Liskov substitution principle was initially introduced by [Barbara Liskov](https://en.wikipedia.org/wiki/Barbara_Liskov)
in a 1988 conference keynote address titled *Data abstraction and hierarchy.*

It says that every base class should be interchangeable with a subclass without breaking the program you wrote. For example if you have a base class called Animal and a subclass called Bird, which inherits from Animal, you should be able to replace an object based on the Animal class with an object based on the Bird class everywhere without errors.

Let me show you an example of just using the base class Animal for objects:

```
public class Program
{
    public static void Main()
    {
        var cat = new Animal();
        var bird = new Animal();

        cat.PrintGreeting("Meow"); //prints Meow
        bird.PrintGreeting("Chirp"); //prints Chirp
    }
}

public class Animal
{
    public void PrintGreeting(string sound)
    {
        Console.WriteLine(sound);
    }
}

public class Bird : Animal
{
}
```

Now you probably noticed that we have a bird class, so why not replace the bird var with Bird as object instead of Animal. If this works the same way, you are adhering to the L in SOLID!

```
public class Program
{
    public static void Main()
    {
        var cat = new Animal();
        var bird = new Bird();

        cat.PrintGreeting("Meow");
        bird.PrintGreeting("Chirp");
    }
}

public class Animal
{
    public void PrintGreeting(string sound)
    {
        Console.WriteLine(sound);
    }
}

public class Bird : Animal
{
}
```

# Interface Segregation Principle

The I in SOLID is all about Interfaces. It describes how you should separate interfaces into separate files rather than allowing a single interface to handle all possible functionalities. You should do this as soon as you notice that some methods are unnecessary for a class to implement that inherits an interface

Let me illustrate the principle with an example from real life.
Self-scan checkouts with card payment are becoming more common in grocery stores.
There are also cash-only checkouts available.
Previously, we only had checkouts that allowed both card and cash payments; the disadvantage of this is that it is slower than separating cash and card. This is why it was eventually split up.

Lets start with an insufficient example:

```
public interface IWorker
{
    public void Work();
    public void Sleep();
}

public class Worker : IWorker
{
    public void Work()
    {
        // Do some work
    }

    public void Sleep()
    {
        //Sleep after a while
    }
}

public class Robot : IWorker
{
    public void Work()
    {
        //do a lot of work
    }

    public void Sleep()
    {
        //Robots don't sleep, right????
    }
}
```

This is an example of a factory that employs both robots and humans.
It is a human necessity to sleep after a long day at work; however, for robots, this is not the case. By using the interface we’re currently using, we are forced to implement both sleep and work for both the Robot and worker class regardless of need.

Here’s a more sufficient way to do it:

```
public interface IWorker : IWork, ISleep
{
}

public interface IWork
{
    public void Work();
}

public interface ISleep
{
    public void Sleep();
}

public class Worker : IWorker
{
    public void Work()
    {
        // Do some work
    }

    public void Sleep()
    {
        //Sleep after a while
    }
}

public class Robot : IWork
{
    public void Work()
    {
        //do a lot of work
    }
}
```

The Worker class uses IWorker, which has both ISleep and IWork is implemented. For the Robot class I use only the IWork interface because a robot doesn’t need to sleep. That’s how you use the Interface Segregation Principle.

# Dependency Inversion Principle

If we google the definition for Dependency Inversion Principle, we get this:

*The Dependency Inversion Principle (DIP) states that high-level modules should not depend on low-level modules; both should depend on abstractions. Abstractions should not depend on details. Details should depend upon abstractions.*

This might sound confusing but hear me out. High-level modules in DIP are considered Interfaces and abstract classes. Low-level modules are details of your interfaces or abstract classes.

Consider it being like a car: the steering wheel, gas, and brake are your high-level modules.
The engine is your low-level module. The engine makes the car drive, but you interact with it directly through the steering wheel and brakes. If you replace the engine, nothing changes with the steering wheels and brakes; it should still drive.

Let me show you an insufficient example:

```
public class GradeReport
{
    private readonly MySqlDatabase _db;

    public GradeReport(MySqlDatabase db)
    {
        _db = db;
    }

    public void GetGrades()
    {
        _db.Get();
    }

    public void InsertNewGrade()
    {
        _db.Insert();
    }
}

public class MySqlDatabase
{
    public void Get()
    {
        // Get all grades
    }    

    public void Insert()
    {
        // Insert grade
    }

    public void Delete()
    {
        // Delete grade
    }

    public void Update()
    {
        // Update grade
    }
}
```

This example uses a database to create a grade report for a student. Everything works as expected, but this is against the Dependency Inversion Principle. It also violates the open-closed principle because, for example, if you wanted to add a MongoDB or PostgresDB class to it, you would have to change the GradeReport file to include an if-else statement.

So lets add a PostgresDB class but use an interface for it so we don’t have to depend on the MySqlDatabase anymore:

```
public class Program
{
    public void Main()
    {
        var mysql = new MySqlDatabase();
        var postgres = new PostgresDatabase();

        var reportMySql = new GradeReport(mysql);
        var reportPostgres = new GradeReport(postgres);

        reportMySql.GetGrades();
        reportPostgres.GetGrades();
    }
}

public class GradeReport
{
    private readonly IDatabase _db;

    public GradeReport(IDatabase db)
    {
        _db = db;
    }

    public void GetGrades()
    {
        _db.Get();
    }

    public void InsertNewGrade()
    {
        _db.Insert();
    }
}

public interface IDatabase
{
    public void Get();
    public void Insert();
    public void Delete();
    public void Update();
}

public class MySqlDatabase: IDatabase
{
    public void Get()
    {
        // Get all grades
    }    

    public void Insert()
    {
        // Insert grade
    }

    public void Delete()
    {
        // Delete grade
    }

    public void Update()
    {
        // Update grade
    }
}

public class PostgresDatabase : IDatabase
{
    public void Get()
    {
        // Get all grades
    }    

    public void Insert()
    {
        // Insert grade
    }

    public void Delete()
    {
        // Delete grade
    }

    public void Update()
    {
        // Update grade
    } 
}
```

# That’s a wrap!

You now know all the SOLID principles. I hope you found it useful. Who doesn’t love pretty looking code, right?

If you have any suggestions or questions, feel free to leave a comments or contact me on Twitter on [@lovelacecoding](https://hashnode.com/@lovelacecoding). See you later!
