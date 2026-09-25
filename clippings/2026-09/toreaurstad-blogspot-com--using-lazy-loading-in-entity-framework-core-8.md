---
url: "https://toreaurstad.blogspot.com/2024/09/using-lazy-loading-in-entity-framework.html?_bhlid=efd39774a29b3493b98805aa251f5eb60eb7366e&m=1"
captured_at: "2026-09-25T21:38:11+01:00"
title: "Using lazy loading in Entity Framework Core 8"
domain: "toreaurstad-blogspot-com"
---

This article will show some code how you can opt in something called _lazy loading_ in EF. This means you do not load in all the related data for an entity until you need the data. Lets look at a simple entity called _Customer_. We will add to navigational properties, that is related entities. Without _eager loading_ enabled automatically or _lazy loading_ enabled automatically, EF Core 8 will not populated these navigational properties, which is pointing to the related entities. The fields will be null without active measure on the loading part. Let's inspect how to lazy load such navigational properties.

**Customer.cs**

```


 public class Customer {
 
  // more code.. 
 
  public Customer()
  {
      AddressCustomers = new HashSet<AddressCustomer>();
  }
  
  // more code .. 
 
  private Customer(ILazyLoader lazyLoader)
  {
    LazyLoader = lazyLoader;
  }

  public CustomerRank CustomerRank { get; set; }

  public virtual ICollection<AddressCustomer> AddressCustomers { get; set; }
  
 }
  
  
 
```

First off, the _ILazyLoader_ service is from _Microsoft.EntityFrameworkCore.Infrastructure_. It is injected inside the entity, preferably using a private constructor of the entity. Now you can set up lazy loading a for a navigational property like this :

```


 public CustomerRank CustomerRank
 {
     get => LazyLoader.Load(this, ref _customerRank);
     set => _customerRank = value;
 }
  
  
 
```

If it feels a bit unclean to mix entity code with behavioral code since we inject a service into our domain models or entities, you can use the Fluent api instead while setting up the DbContext.

```


  modelBuilder.Entity<Customer>()
      .Navigation(e => e.AddressCustomers)
     .AutoInclude();

  modelBuilder.Entity<Customer>(entity =>
  {
      entity.HasKey(e => e.Id);
     entity.Navigation(e => e.CustomerRank).AutoInclude();
  });


 
```

If automatically lazy loading the data (the data will be loaded upon access of the navigational property) seems a bit little flexible, one can also set up loading manually wherever in the application code using the methods _Entry_ and either _Reference_ or _Collection_ and then the _Load_ method.

```


var customer = _dbContext.Customers.First();

_dbContext
    .Entry(customer)
    .Reference(c => c.CustomerRank)
    .Load();


_dbContext
    .Entry(customer)
    .Collection(c => c.AddressCustomers)
    .Load();

```

Once more, note that the data is still lazy loaded, their content will only be loaded when you access the particular navigational property pointing to the related data. Also note that if you debug in say VS 2022, data might look like they are automatically loaded, but this is because the debugger loads the contents if it can and will even do so for lazy loaded navigational fields. If you instead make in your application code a programmatic access to this navigational property and output the data you will see the data also being loaded, but this happens once it is programatic access. For example if we made the private field \_customerRank public (as we should not do to protect our domain model's data) you can see this while debugging :

```


//changed a field in Customer.cs to become public for external access :
//  public CustomerRank _customerRank;

Console.WriteLine(customer._customerRank);
Console.WriteLine(customer.CustomerRank);

// considering this set up 

  public CustomerRank CustomerRank
  {
      get => LazyLoader.Load(this, ref _customerRank);
      set => _customerRank = value;
  }

```

The field \_customerRank is initially null, it is when we access the property CustomerRank which I set to be AutoInclude i.e. lazy loaded I see that data is loaded.
