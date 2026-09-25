---
url: "https://curiosum.com/blog/bringing-solid-to-elixir?ref=dailydev"
captured_at: "2026-09-25T19:14:03+01:00"
title: "Bringing SOLID to Elixir"
domain: "curiosum-com"
---

The SOLID principles, originally designed for object-oriented programming, can also be adapted effectively to functional programming languages like Elixir. Read how to apply it to create more maintainable, scalable, and adaptable software systems.

## What is SOLID?

The SOLID principles are a collection of software architecture design guidelines in object-oriented programming (OOP) that assist software architects and development team in building software systems in the agile development manner that are more maintainable, scalable, and adaptable. The acronym SOLID stands for five key principles:

1.  **S - Single Responsibility Principle (SRP):**
    
    A class should have only one reason to change, meaning it should only have one responsibility or functionality. This helps in making classes easier to maintain and understand.
    
2.  **O - Open/Closed Principle (OCP):**
    
    Architectural elements like software entities should be designed to allow for extension while being closed to modification. This means you can introduce new features without altering the existing code, thereby preserving the integrity of the current functionality.
    
3.  **L - Liskov Substitution Principle (LSP):**
    
    Subtypes must be substitutable for their base types without affecting the correctness of the program. In other words, derived classes should extend the base class without changing its behavior.
    
4.  **I - Interface Segregation Principle (ISP):**
    
    Clients should not be forced to depend on interfaces they do not use. This encourages the creation of small, specific interfaces, rather than large, general-purpose ones.
    
5.  **D - Dependency Inversion Principle (DIP):**
    
    High-level modules should not rely on low-level modules; instead, both should depend on abstractions (such as interfaces). Furthermore, abstractions should not depend on specific implementations, but rather on other abstractions.
    

These patterns are aimed at reducing tight coupling, improving app architecture, code reuse, and enhancing flexibility in software design… but as you see - they are suited for object-oriented programming, not functional programming in Elixir. So how can we adapt these guidelines for our work?

## Single Responsibility Principle

It states that **a class or module should have only one reason to change**, meaning that a class should have only **one responsibility** or perform **one function** within a program. By adhering to this principle, you ensure that a module focuses on a single task or concern, making it easier to maintain, test, and modify.

The idea is to keep modules small and focused, reducing complexity and improving code clarity, and the best way to check if our code follows this pattern is to slice our module into smaller pieces and ask yourself a question - can any of these change independently?

![https://cdn.prod.website-files.com/6780f4139ab3ae7f7313b0f4/688a27d7bfa77a81cc765d63\_fail-list-you-had-one-job-751621.jpeg](https://cdn.prod.website-files.com/6780f4139ab3ae7f7313b0f4/688a27d7bfa77a81cc765d63_fail-list-you-had-one-job-751621.jpeg)

Let’s take a look at the example:

```
defmodule User do
  defstruct [:name, :email]
end

defmodule UserBusinessLogic do
  def save_to_database(%User{name: name}) do
    # Code to save user information to the database
  end

  def send_welcome_email(%User{email: email}) do
    # Code to send a welcome email
  end

  def delete_user_account(%User{} = user) do
    # Code to delete user
  end
end
```

In this example, we have a module with business logic functions for a User struct. At first glance, it might seem reasonable to group features like this. However, we need to consider the potential growth of these functions.

If we decide to use an integration with some third-party service for emails, integrate analytics tools, or implement more complex user deletion processes—such as GDPR-compliant anonymization and soft deletion instead of just Repo.delete/1—the module could become large and harder to manage. Finding and modifying specific parts of the logic would become increasingly difficult as responsibilities continue to accumulate.

By following the **Single Responsibility Principle**, we avoid this problem by splitting the code into smaller, focused modules. This makes the software system easier to maintain and scale, as each module handles a specific task, reducing the risk of bloating and complexity in one place.

```
defmodule UserRepository do
  def save_to_database(%User{name: name}) do
    # Code to save user information to the database
  end
end

defmodule WelcomeEmailService do
  def call(%User{email: email}) do
    # Code to send a welcome email
  end
end

defmodule DeleteUserService do
  def call(%User{} = user) do
    # Code to delete user
  end
end
```

## Open/Closed

It states that **modules should be open for extension but closed for modification**.

This means you should be able to extend the behavior of a system (add new features or something) without changing its existing source code. By adhering to OCP, you minimize the risk of introducing bugs into existing code when adding new features, promoting stability and encouraging reuse.

Imagine we have a module responsible for calculating discounts for various types of users. As new user types (e.g., "VIP") are added in the future, we need to modify this module, which violates the **Open/Closed Principle** because the existing code has to change whenever a new discount type is introduced.

```
defmodule DiscountCalculator do
  def calculate(user_type, price) do
    case user_type do
      :regular -> price
      :premium -> price * 0.9
      :student -> price * 0.8
      _ -> price
    end
  end
end
```

Here, the DiscountCalculator module is **not closed for modification**. Whenever a new user type, such as :vip, is introduced, we would have to modify the calculate/2 function, leading to possible errors and making the system harder to maintain as it grows.

In practice, OCP is often achieved using techniques like inheritance, interfaces, abstract classes, or dependency injection but in [Elixir](https://curiosum.com/blog/elixir-programming-language-guide) we have a very similar tool called - **Behaviour**.

To adhere to the Open/Closed Principle, we can refactor the code by defining a behavior (or protocol) for discount calculation, which allows us to extend the system without modifying the existing logic.

New discount types can be introduced by adding new modules, not by changing the existing DiscountCalculator.

```
# DEFINING BEHAVIOUR
defmodule Discount do
  @callback calculate(float()) :: float()
end

# IMPLEMENTING calculate/1 for each user type
defmodule RegularUser do
  @behaviour Discount

  def calculate(price), do: price
end

defmodule PremiumUser do
  @behaviour Discount

  def calculate(price), do: price * 0.9
end

defmodule StudentUser do
  @behaviour Discount

  def calculate(price), do: price * 0.8
end

defmodule VIPUser do
  @behaviour Discount

  def calculate(price), do: price * 0.7
end
```

Then we can adjust DiscountCalculator module to be more generic and work with any module that implements the Discount behaviour:

```
defmodule DiscountCalculator do
  def calculate(user_module, price) when is_atom(user_module) do
    user_module.calculate(price)
  end
end
```

This keeps the system **open for extension** (new user types) but **closed for modification** (no changes to existing services when new discounts are introduced) minifying the risk of technical debt in the future.

## **Liskov Substitution Principle**

It states that **objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program**. In other words, if a class S is a subclass of class T, objects of type T should be able to be replaced with objects of type S without altering the desirable properties of the program (e.g., correctness, performance, etc.)… saying that - don’t try to understand it cause definitions for this principle are always complex.

Let’s try to simplify it to: “**Where you have a variable that’s of the base type you should be able to switch in any of the ‘subclass’ types without having an undesirable effect on your system.**” and take a look at the example:

We’ll define a behavior for sending notifications and implement two modules: EmailNotification and SMSNotification.

```
defmodule Notification do
  @callback send(String.t()) :: :ok | {:error, String.t()}
end

defmodule EmailNotification do
  @behaviour Notification

  def send(message) do
    # Simulate sending an email notification
    :ok
  end
end

defmodule SMSNotification do
  @behaviour Notification

  def send(message) do
    # Simulate sending an SMS notification
    :ok
  end
end
```

Now, let’s see how we can use these notifications interchangeably, adhering to the **Liskov Substitution Principle**.

```
defmodule NotificationService do
  def notify(notification_module, message) when is_atom(notification_module) do
    notification_module.send(message)
  end
end
```

In the NotificationService module, we have a notify/2 function that accepts any module implementing the Notification behavior. This allows us to substitute EmailNotification with SMSNotification seamlessly.

But what if we want to extend SMSNotification of some kind of validation:

```
defmodule SMSNotification do
  @behaviour Notification

  def send(message) when is_binary(message) and byte_size(message) <= 160 do
    # Simulate sending an SMS notification
    :ok
  end

  def send(_message) do
    {:error, "Message is too long for SMS notification"}
  end
end
```

This can lead to a violation of LSP when used interchangeably with EmailNotification. When we substitute SMSNotification for EmailNotification, it is expected that the notify/2 function can call send/1 on any notification type without needing to check specifics.

However, SMSNotification introduces a limitation (message length) that breaks this expectation. The send/1 function in SMSNotification behaves differently than expected by the client of the Notification behavior. If the message length exceeds 160 characters, it results in an error, which may not be handled gracefully in the same way as an email notification.

We can identify violation here, because the SMSNotification cannot be used interchangeably with the EmailNotification without additional checks, it violates the **Liskov Substitution Principle**.

Any code that assumes both notifications can be used interchangeably would not function correctly when it encounters a message that doesn’t meet the SMSNotification requirements.

This demonstrates the important stuff of designing subclasses (or implementations) in a way that maintains expected behaviors to ensure correct substitutability. To resolve such issues, we should find some trade offs, either unify the message constraints across all notifications or ensure that clients are aware of the constraints for specific types.

## Interface Segregation

It states that **no client should be forced to depend on methods it does not use**. In other words, interfaces should be small and specific to the needs of the clients that use them, rather than large and general-purpose.

Instead of creating a single, large interface that includes many methods, you should create multiple smaller interfaces that cater to specific client needs.

Smaller, more focused interfaces make it easier to change or extend the system without impacting clients that do not use certain features.

By segregating interfaces, you reduce the number of methods that a client needs to implement or depend on, which can lead to cleaner and more maintainable code.

Let's create an example in Elixir that illustrates a violation of this principle:

We’ll write a Vehicle system behavior that includes multiple methods

```
defmodule Vehicle do
  @callback drive() :: :ok
  @callback fly() :: :ok
  @callback sail() :: :ok
end
```

Now, let’s implement a Car module that implements the Vehicle behavior. Since a car can only drive, it will have to provide dummy implementations for the fly/0 and sail/0 methods, violating the ISP.

```
defmodule Car do
  @behaviour Vehicle

  @impl Vehicle
  def drive() do
    IO.puts("Driving a car.")
    :ok
  end

  @impl Vehicle
  def fly() do
    :ok
  end

  @impl Vehicle
  def sail() do
    :ok
  end
end
```

Next, let’s implement a Boat module. Like the Car, it will also be forced to implement methods it doesn’t need.

```
defmodule Boat do
  @behaviour Vehicle

  @impl Vehicle
  def drive() do
    :ok
  end

  @impl Vehicle
  def fly() do
    :ok
  end

  @impl Vehicle
  def sail() do
    IO.puts("Sailing a boat.")
    :ok
  end
end
```

Can we identify the next principle violation here? Both Car and Boat are forced to implement methods (fly/0 and sail/0 for the car, and drive/0 and fly/0 for the boat) that are irrelevant to their functionality. This results in code that is cluttered and does not serve the purpose of the respective modules.

To adhere to the **Interface Segregation Principle**, we should define more specific interfaces for each type of vehicle.

```
defmodule Drivable do
  @callback drive() :: :ok
end

defmodule Flyable do
  @callback fly() :: :ok
end

defmodule Sailable do
  @callback sail() :: :ok
end
```

```
defmodule Car do
  @behaviour Drivable

  @impl Drivable
  def drive() do
    IO.puts("Driving a car.")
    :ok
  end
end

defmodule Boat do
  @behaviour Sailable

  @impl Sailable
  def sail() do
    IO.puts("Sailing a boat.")
    :ok
  end
end
```

By refactoring the code to use smaller, more specific interfaces, we adhered to ISP, making the code cleaner, more maintainable, and better aligned with client needs.

## Dependency Inversion

In general, it states that: **High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details. Details should depend on abstractions.**

Let’s use the previous example when we will have a notification system where a NotificationService sends messages using different notification channels (like email and SMS) defined through behaviors.

```
defmodule NotificationSender do
  @callback send_notification(String.t()) :: :ok | {:error, String.t()}
end

defmodule EmailNotification do
  @behaviour NotificationSender

  @impl NotificationSender
  def send_notification(message) do
    IO.puts("Sending email: #{message}")
    :ok
  end
end

defmodule SMSNotification do
  @behaviour NotificationSender

  @impl NotificationSender
  def send_notification(message) do
    IO.puts("Sending SMS: #{message}")
    :ok
  end
end
```

Now, we’ll create a NotificationService module that depends on the NotificationSender behavior rather than concrete implementations. We'll configure which notification method to use via application configuration so iex. we won’t send emails and SMS during our test runs or on the dev environment.

```
defmodule NotificationService do
  @notification_sender Application.get_env(:your_app, :notification_sender)

  def notify(message) do
    @notification_sender.send_notification(message)
  end
end
```

The service depends on the NotificationSender behavior rather than concrete implementations (like EmailNotification or SMSNotification). This allows us to change the implementation used without modifying the NotificationService code.

This design makes the codebase modular, and you can easily test NotificationService by providing a mock implementation of the NotificationSender behavior.

By using application configuration, we can easily switch between different notification methods without changing the core logic of the service and struggling about some external API integration limits.

## Building SOLID blocks

The SOLID principles serve as foundational guidelines for designing robust, maintainable, and scalable software leading to developing and finalizing long term goals faster. While these patterns originated in the context of object-oriented programming, now we should have a clear understanding that they are equally relevant and applicable in Elixir and functional programming paradigms, albeit with some adaptations.

1.  **Encouraging Modularity**: The SOLID principles promote a modular architecture, enabling developers to break down complex systems into smaller, well-defined components. In Elixir, leveraging modules, behaviors, and functions aligns well with these principles, allowing for clear boundaries and responsibilities, thereby enhancing code readability and maintainability.
2.  **Flexibility and Extensibility**: By adhering to the Open/Closed and Dependency Inversion principles, Elixir users can build systems that are flexible and easily extensible. The use of behaviors for defining interfaces allows for polymorphic designs that can adapt to changing requirements without significant rewrites, a crucial aspect in rapidly evolving applications.
3.  **Testing and Reliability**: The Single Responsibility Principle and Interface Segregation Principle aid in isolating functionalities, making testing more straightforward. In functional programming, where functions are first-class citizens, it becomes easier for developer to write unit tests for isolated components, improving reliability and robustness in production environments.
4.  **Reducing Complexity**: The Liskov Substitution Principle and Dependency Inversion Principle encourage developers to focus on abstractions rather than concrete implementations. This reduces the coupling between different parts of the system and allows for easier refactoring and modification of code without introducing bugs.
5.  **Alignment with Functional Paradigms**: While some SOLID principles are more naturally aligned with object-oriented practices, they can still be effectively implemented in functional programming. For instance, instead of classes, Elixir’s modules can encapsulate related functions, and behaviors can create contracts for those functions, ensuring compliance with principles like LSP and ISP.

Applying SOLID principles at a high level design to provide good architecture in [Elixir programming](https://curiosum.com/blog/elixir-programming-language-guide) not only leads to cleaner and more maintainable code but also enhances collaboration among people involved, facilitates testing, helps to get rid of technical debt, and supports scalability.

By embracing these patterns in their design decisions, developers can build and manage robust software systems that are adaptable to change, ultimately resulting in higher-quality software solutions that meet users needs effectively.

## Want to power your product with Elixir? We’ve got you covered.
