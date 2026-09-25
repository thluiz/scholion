---
url: "https://mwaseemzakir.substack.com/p/ep-66-clean-code-tips-for-net-developers?ref=dailydev"
captured_at: "2026-09-25T18:00:06+01:00"
title: "EP 66 : Clean Code Tips for .NET Developers - Part I"
domain: "mwaseemzakir-substack-com"
---

[Sponsor this newsletter](https://mwaseemzakir.com/sponsorship/)

[

![](https://substackcdn.com/image/fetch/$s_!MkI9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6a411ea7-d6d9-4b90-b634-2c7099910252_1200x600.png)

](https://substackcdn.com/image/fetch/$s_!MkI9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6a411ea7-d6d9-4b90-b634-2c7099910252_1200x600.png)

Writing clean code is crucial for development. If writing code is art then writing clean code would be a masterpiece.

Check out the first post of the clean code tips series :

Using meaningful names makes code self-explanatory, reducing the need for additional comments.

Bad Example :

```
public class Emp
{
    public string n;
    public int a;

    public void d()
    {
       Console.WriteLine($"Name: {name}, Age: {age}");
    }
}
```

Good Example :

```
public class Employee
{
    public string name;
    public int age;

    public void DisplayInfo()
    {
        Console.WriteLine($"Name: {name}, Age: {age}");
    }
}
```

Returning null can lead to `NullReferenceException` errors when the caller attempts to access properties or methods on the returned object. It can also make the code harder to read and maintain, as the caller must always check for null before using the returned value.

Suppose we have this piece of code :

```
public class UserService
{
    public User? GetUserById(int id)
    {
        if (id <= 0)
        {
            return null; 
        }
        .... Rest logic of method ...
        return user;
    }
}
```

We can improve it with this, instead of returning null we can throw an exception and then handle it separately :

```
public sealed class UserService
{
    public User GetUserById(int id)
    {
        if (id <= 0)
        {
            // throws an exception instead of returning null
            throw new ArgumentException("Invalid user Id"); 
        }
        .... Rest logic of method ...
        return user;
    }
}
```

A class should have one reason to change.

Smaller classes are easier to manage, test, and maintain.

At some points, this asks us to follow the _**Single Responsibility Principle**_.

Suppose we have this example in which we have a lot of code, with different concerns :

```
public sealed class OrderProcessing
{
    public void ProcessOrder(Order order)
    {
        if (!ValidateOrder(order))
        {
            throw new ArgumentException("Invalid order");
        }

        ChargePayment(order);
      
        UpdateInventory(order);

        SendConfirmationEmail(order);

        LogOrderDetails(order);
    }

    private bool ValidateOrder(Order order) {  }
    private void ChargePayment(Order order) {  }
    private void UpdateInventory(Order order) {  }
    private void SendConfirmationEmail(Order order) { }
    private void LogOrderDetails(Order order) { }
}
```

This could be improved like this where we have separate classes for each concern :

```
public sealed class OrderValidator
{
    public bool Validate(Order order){}
}

public sealed class PaymentProcessor
{
    public void Charge(Order order){}
}

public sealed class InventoryManager
{
    public void Update(Order order){}
}

public sealed class EmailService
{
    public void SendConfirmation(Order order){}
}

public sealed class OrderProcessing
{
    private readonly OrderValidator _validator;
    private readonly PaymentProcessor _paymentProcessor;
    private readonly InventoryManager _inventoryManager;
    private readonly EmailService _emailService;

    public OrderProcessing(
      OrderValidator validator, 
      PaymentProcessor paymentProcessor,
      InventoryManager inventoryManager,
      EmailService emailService)
    {
        _validator = validator;
        _paymentProcessor = paymentProcessor;
        _inventoryManager = inventoryManager;
        _emailService = emailService;
    }

    public void ProcessOrder(Order order)
    {
        if (!_validator.Validate(order))
        {
            throw new ArgumentException("Invalid order");
        }

        _paymentProcessor.Charge(order);
        _inventoryManager.Update(order);
        _emailService.SendConfirmation(order);
    }
}
```

Although there is no hard-code rule about how many lines of code a method should contain, 20-40 lines are enough for a method.

Reinventing the wheel can lead to unnecessary duplication of effort, wasting valuable time and resources that could be better spent on developing unique features.

What exactly is reinventing the wheel, it means when we already have code for some issue and we start writing manually code to solve that cause then we are reinventing the wheel :

```
public sealed class CustomLogger
{
    public void Log(string message)
    {
        using (var writer = new StreamWriter("log.txt", true))
        {
            writer.WriteLine($"{DateTime.Now}: {message}");
        }
    }
}
```

We can achieve that by just injecting the ILogger interface, considering logging is already configured :

```
public sealed class Application
{
    private readonly ILogger _logger;

    public Application(ILogger logger)
    {
        _logger = logger;
    }
}
```

Read about how to implement logging in .NET :

*   [Logging with NLog](https://mwaseemzakir.com/newsletters/episode1/)
    
*   [Logging with Serilog](https://mwaseemzakir.com/newsletters/episode60/)
    

Using the right tools or IDE enhances productivity by providing features like syntax highlighting, code completion, and error checking, which help catch mistakes early.

Keep reading the new update of Visual Studio, and invest time in learning about existing features of tools as well.

Additionally, these are two practices that I follow in my .NET projects, and I would recommend that you do the same:

Enabling the editor config file in .NET projects to apply some sort of rules on all code

```
root = true

# C# files
[*.cs]

#### Core EditorConfig Options ####

# Indentation and spacing
indent_size = 4
indent_style = space
tab_width = 4

#### .NET Coding Conventions ####

# Organize usings
dotnet_separate_import_directive_groups = false
dotnet_sort_system_directives_first = true
```

This props file is used to configure common settings and apply them across all projects for example:

```
<Project>
  <PropertyGroup>
    <TargetFramework>net7.0</TargetFramework>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
    <TreatWarningsAsErrors>true</TreatWarningsAsErrors>
  </PropertyGroup>
</Project>
```

1.  If you want to boost your .NET skills and do some code in action you can do that by subscribing to my **[YouTube Channel](https://www.youtube.com/channel/UCgKGlfkNAmIBprbI35C6SpQ?sub_confirmation=1)**
    
2.  **[Promote yourself to 11,000+ subscribers](https://mwaseemzakir.com/sponsorship/)** by sponsoring this newsletter
