---
url: "https://dev.to/walpolesj/learn-the-solid-principles-for-object-oriented-programming-53e1"
captured_at: "2026-11-16T01:57:45+00:00"
title: "Learn the SOLID principles for Object Oriented Programming"
domain: "dev-to"
---

Object oriented programming (or OOP) is a style of programming that encapsulates data and behaviours into models known as objects. In this way, related code is grouped together and kept separate from other code, and provides reusable blocks that can be used to rationalise the problem at hand.

OOP is probably one of the most common forms programming, and many popular programming languages, including C#, Java, and JavaScript, are built with this in mind.

In a lot of languages, the blueprint for the object is known as a class. The class contains all the definitions for that object, including properties and functions (more commonly known as methods).

To create an actual object, we say that we create an instance of the class, in which all of the property definitions are given actual values. Importantly, we can have multiple instances of the same class existing at the same time, each with different values.

For example, we could create a simple Person class that has a name property and a speak method:  

```
public class Person
{
    public Person(string name)
    {
        Name = name;
    }

    public int Id { get; set; }

    public string Name { get; set; }

    public void Speak()
    {
        Console.WriteLine($"My name is {Name}");
    }
}
```

Enter fullscreen mode Exit fullscreen mode

This is the blueprint. Now we can create two separate instances of the class, and the speak methods will give different outputs because each actual object is instantiated with a different value for the name property.  

```
var bernard = new Person("Bernard");
var sally = new Person("Sally");

bernard.Speak(); // outputs "My name is Bernard"
sally.Speak(); // outputs "My name is Sally"
```

Enter fullscreen mode Exit fullscreen mode

Although these are very simple examples, hopefully you can see the benefit of being able to create these object blueprints and create separate instances of actual objects.

However, it can be easy to misuse objects and create difficult-to-read or unstable code, if you're not careful. For example, you could potentially end up with a "God" class that has lots of unrelated behaviour crammed into the same object.

To help write good, maintainable, stable code, the SOLID principles have been described below.

*   **S** - Single responsibility principle
*   **O** - Open/closed principle
*   **L** - Liskov substitution principle
*   **I** - Interface segregation principle
*   **D** - Dependency inversion principle

## [](#s-single-responsibility-principle)S - Single Responsibility Principle

The title here is pretty self-explanatory. A class should only have one responsibility. This is to avoid the "God" class scenario, where one class does everything, and helps split up your code into smaller, sensible chunks.

Although the single responsibility principle, is quite easy to understand, in practice it is not always so simple to spot when something belongs in a class and when it should be moved to a different class. Making this judgement is mostly a matter of experience, and you will get better at it with time.

If we go back to our Person class, we might decide that we want to save each person into a database. Therefore, it might seem sensible to create a method on the Person class:  

```
public class Person
{
    // ... other properties and methods

    public void SaveToDatabase()
    {
        // logic to save person
    }
}
```

Enter fullscreen mode Exit fullscreen mode

However, the problem here is that the details of how to save a person to the database is an additional responsibility, and so that responsibility should be moved to another class.

Therefore, we could create a database class, with a SavePerson method, and pass the instance of the Person into that class. That way the Person class only deals with the details of the person, and the database class deals with the details of saving the person.  

```
public class Database 
{
    public void SavePerson(Person person)
    {
        // logic to save person
    }
}
```

Enter fullscreen mode Exit fullscreen mode

## [](#o-openclosed-principle)O - Open/closed principle

The open/closed principle states that an object should be open for extension but closed for modification. This means that you should design you objects in such a way that they can be easily extended, without having to directly modify them.

For example, we could define two new classes, Employee and Manager, which are derived from the Person class, and a SalaryCalculator class.  

```
public class Employee : Person
{
    // employee methods and properties
}

public class Manager : Person
{
    // manager methods and properties
}

public class SalaryCalculator
{
    public decimal CalculateSalary(Person person)
    {
        if (person is Employee)
        {
            return 100 * 365;
        }
        else if (person is Manager)
        {
            return 200 * 365;
        }
    }
}
```

Enter fullscreen mode Exit fullscreen mode

In this example, the SalaryCalculator class violates the open/closed principle because, if we extend the program by adding a Director class, we would have to modify the CalculateSalary method to account for this.

To fix this, we could add a DailyRate property to each of the Person types. That way, we can add as many Person types as we want, and never have to modify SalaryCalculator.  

```
public class Person
{
    public virtual decimal DailyRate => 0;
}

public class Employee : Person
{
    public override decimal DailyRate => 100;
}

public class Manager : Person
{
    public override decimal DailyRate => 200;
}

public class Director : Person
{
    public override decimal DailyRate => 300;
}

public class SalaryCalculator
{
    public decimal CalculateSalary(Person person)
    {
        return person.DailyRate * 365;
    }
}
```

Enter fullscreen mode Exit fullscreen mode

## [](#l-liskov-substitution-principle)L - Liskov substitution principle

The Liskov substitution principle states that every sub-class should be substitutable for it's base class and the program will still behave as expected.

The example for the open/closed principle is also a good example for the Liskov substitution principle.

In the SalaryCalculator class, the method takes the base class Person but at runtime we can pass any of its sub-classes too. Because we have used the virtual and override keywords in the Person and sub-classes respectively, the value of the DailyRate inside the CalculateSalary method will be that of the sub-class i.e even though we have substituted the sub-classes for the base class in the CalculateSalary method, the method still behaves correctly.

As an example of violating the Liskov substitution principle, we could redefine our classes as:  

```
public class Person 
{
    public decimal DailyRate => 0;
}

public class Employee
{
    public new() decimal DailyRate => 100;
}
```

Enter fullscreen mode Exit fullscreen mode

With this definition we violate the Liskov substitution principle because the DailyRate will always evaluate to 0 in the SalaryCalculator and not the value of the sub-class.

## [](#i-interface-segregation-principle)I - Interface segregation principle

The interface segregation principle states that a client should not be forced to implement properties and methods of an interface that it will not use. Therefore, it is better to define lots of small, specific interfaces, rather than few large, general interfaces.

As an example, we could define an IRepository interface for performing CRUD operations for our Person class on a database and implement it:  

```
public interface IRepository
{
    bool Create(Person person);
    Person Get(int id);
    IEnumerable<Person> GetAll();
    bool Update(Person person);
    bool Delete(int id);
}

public class Repository : IRepository
{
    public bool Create(Person person)
    {
        // create logic
    }

    public Person Get(int id)
    {
        // get logic
    }

    // etc
}
```

Enter fullscreen mode Exit fullscreen mode

This is fine if we know that we will always need full CRUD functionality. But what if actually, we only require the repository to be readonly? At the minute, we're forced to implement the full CRUD operations, even if we don't need them.

Instead we can define multiple interfaces, and only implement the ones that we need.  

```
public interface ICreatableRepository
{
    bool Create(Person person);
}

public interface IGettableRepository
{
    Person Get(int id);
    Person GetAll();
}

public interface IUpdateableRepository
{
    bool Update(Person person);
}

public interface IDeletableRepository
{
    bool Delete(int id);
}
```

Enter fullscreen mode Exit fullscreen mode

Then we can optionally choose to make a implement readonly repository or a full CRUD repository.  

```
public class ReadonlyRepository : IGettableRepository
{
    public Person Get(int id)
    {
        // get logic
    }

    public IEnumerable<Person> GetAll()
    {
        // get all logic
    }
}

public class CrudRepository : ICreateableRepository, IGettableRepository, IUpdateableRepository, IDeleteableRepository
{
    public bool Create(Person person)
    {
        // create logic
    }

    public Person Get(int id)
    {
        // get logic
    }

    // etc
}
```

Enter fullscreen mode Exit fullscreen mode

## [](#d-dependency-inversion-principle)D - Dependency Inversion principle

The dependency inversion principle states that classes shouldn't depend on other classes, but instead should depend on the interfaces that those classes implement. This has the effect of inverting the direction of dependencies.

For example, a traditional 3-tier app consisting of only classes might have a PersonPresenter class, which depends on a PersonLogic class, which depends on a PersonRepository class. E.g.  

```
PersonPresenter --> PersonLogic --> PersonRepository
```

Enter fullscreen mode Exit fullscreen mode

The problem with this is that it tightly couples the high level presentation to the low level implementation details. It's much better to have loosely coupled code, which can be achieved using interfaces. For more reasons for using interfaces, please see my previous blog post:

To invert the dependencies, we can create interfaces of each of the low level classes, and have those classes implement them:  

```
PersonPresenter --> IPersonLogic <-- PersonLogic --> IPersonRepository <-- PersonRepository
```

Enter fullscreen mode Exit fullscreen mode

## [](#conclusion)Conclusion

So there are the 5 SOLID principles of Object Oriented Programming. If you've found it useful, please like and share this post. And feel free to follow me on [twitter](https://twitter.com/dr_sam_walpole) If you want, you can also [buy me a coffee](https://ko-fi.com/samwalpole) ! 😊
