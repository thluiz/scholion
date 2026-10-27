---
url: "http://encosia.com/first-class-functions-as-an-alternative-to-javascripts-switch-statement/"
captured_at: "2013-05-24T10:21:28-03:00"
title: "My favorite alternative to JavaScript's switch statement » Encosia"
domain: "encosia-com"
---

# [My favorite alternative to JavaScript’s switch statement](http://encosia.com/first-class-functions-as-an-alternative-to-javascripts-switch-statement/ "Permanent Link: My favorite alternative to JavaScript’s switch statement")

[JavaScript](http://encosia.com/category/javascript/ "View all posts in JavaScript") 
By **[Dave Ward](http://encosia.com/about-dave-ward/ "About Dave Ward")** **.**
Posted May 23, 2013

One of my least favorite parts of nearly every programming language I’ve spent much time with has been the ubiquitous `switch` statement**.** Though it does [serve a useful purpose](http://en.wikipedia.org/wiki/Switch_statement#Compilation) in some compiled languages, I think switch is a clunky eyesore in most code**.** Its structure is prone to taking root and only growing larger and more cumbersome over time**.**

If you’re coming to JavaScript from a background in procedural languages like C#, Java, or PHP, it’s natural to reach for the same tools, like switch, that you’re accustomed to using in those languages**.** However, **JavaScript’s flexible object literal syntax and first-class functions offer alternatives to switch that I believe are cleaner, more extensible, and more maintainable****.**

So, in this post I want to show you a few ways that you can refactor a JavaScript `switch` statement to use this alternate technique, and improve its extensibility and maintainability in the process**.**

### Starting with a switch

To start with a concrete example, let’s say we need find the pricing for line items on an invoice and that those line items might be discounted based on the type of customer that’s being invoiced**.**

To do that, you might iterate over each line item and multiply the price times quantity and apply the correct discount depending on customer type**.** The latter bit being something like the following:

```
function getItemPricing(customer, item) {
  switch(customer.type) {
    // VIPs are awesome. Give them 50% off.
    case 'VIP':
      return item.price * item.quantity * 0.50;
 
    // Preferred customers are no VIPs, but they still get 25% off.
    case 'Preferred':
      return item.price * item.quantity * 0.75;
 
    // No discount for other customers.
    case 'Regular':
    case default:
      return item.price * item.quantity;
  }
}
```

That’s simple enough, but you’ve probably seen code that started like this and then spiraled out of control over time as more and more complexity was needed**.** I know I have (and been responsible for that myself a few times too)**.**

### Turn off the switch

JavaScript’s flexible object literal syntax makes it easy to replace the switch with something that looks similar, but can be decomposed later**.** To get started on that, we can define our pricing rules in an object literal like this one:

```
// This should be namespaced somehow in the real world,
//  not hanging off the global object.
pricing = {
  // VIPs are awesome. Give them 50% off.
  'VIP': 0.50,
 
  // Preferred customers are no VIPs, but they still get 25% off.
  'Preferred': 0.75,
 
  // No discount for other customers.
  'Regular': 1.0
}
```

Putting that into action is straightforward enough**.** We can check that pricing object for a key matching our customer’s type and then apply that custom pricing if it is available:

```
function getItemPricing(customer, item) {
  if (pricing[customer.type])
    return item.price * item.quantity * pricing[customer.type];
  else
    return item.price * item.quantity * pricing.Regular;
}
```

Now, instead of explicitly stepping through a case statement, we’ve separated the pricing rules from the actual pricing mechanism**.**

### Embrace the functional side

Using the object literal is fine for the simple example of multiplying a few numbers together**.** What if our pricing rules needed to be more powerful than simple multiplication though**?** To complicate the example a bit, let’s say that the discount for “Preferred” customers should only apply to items costing up to $100**.**

One of the beautiful things about a functional language like JavaScript is that you can define and pass functions around just as easily as a basic type like a string or boolean**.**

We could approach our new object literal “switch” a little bit differently to take advantage of that:

```
function getItemPricing(customer, item) {
  var pricing = {
    'VIP': function(item) {
      return item.price * item.quantity * 0.50;
    },
    'Preferred': function(item) {
      if (item.price <= 100.0)
        return item.price * item.quantity * 0.75;
 
      // Else
      return item.price * item.quantity;
    },
    'Regular': function(item) {
      return item.price * item.quantity;
    }
  };
 
  if (pricing[customer.type])
    return pricing[customer.type](item);
  else
    return pricing.Regular(item);
}
```

That’s a bit more verbose than the original switch, but it’s worth the extra LoC in the long run**.** Now we’ve got all the power of arbitrary code in a switch, but none of the syntactical restrictions keeping us from breaking it into separate pieces**.**

The functional approach is a departure from the procedural languages you might be used to, and from JavaScript code rooted in those same old practices**.** It can take a while for the utility and flexibility of first-class functions to really sink in, but it’s well worth internalizing this approach in your day-to-day JavaScript**.**

### Modularity === Maintainability

Now that we’ve refactored our pricing logic to be decoupled and functional, the `getItemPricing` method doesn’t really need to know anything about *how* the pricing works**.** The method only needs to understand how to choose which function, if one exists, to apply for a given line item**.**

In fact, they don’t even need to be in the same file anymore:

```
// Pricing.VIP.js
pricing = pricing || { };
 
pricing.VIP = function(item) {
  return item.price * item.quantity * 0.50;
}
```

```
// Pricing.Preferred.js
pricing = pricing || { };
 
pricing.Preferred = function(item) {
  if (item.price <= 100)
    return item.price * item.quantity * 0.75;
 
  // Else
  return item.price * item.quantity;
}
```

```
// Pricing.Regular.js
pricing = pricing || { };
 
pricing.Regular = function(item) {
  return item.price * item.quantity;
}
```

```
// Pricing.js
function getItemPricing(customer, item) {
  if (pricing[customer.type])
    return pricing[customer.type](item);
  else
    return pricing.Regular(item);
}
```

Now, adding a new pricing type to our program is as easy as dropping new file in a directory and referencing it in your program (e**.**g**.** a script reference for website code). As long as it augments the Pricing object with a key/function pair that matches the new customer type, everything “just works”**.**

If you use something like [ASP.NET’s Web Optimization framework](http://www.asp.net/mvc/tutorials/mvc-4/bundling-and-minification) or Rails’ Asset Pipeline, you can configure server-side bundling to automate that work**.** Then, simply dropping a new pricing logic file into the right directory will affect pricing without any extra configuration or script reference**.**

### Conclusion

To me, one of the nicest things about this approach is the flexibility and modularity**.** You can drop a discrete bit of logic in a file in the right directory and change the behavior of your program without touching the program’s core logic**.**

In this example, adding, modifying, or removing a custom pricing type doesn’t require touching pricing**.**js. That means we avoid even the potential for a range of regression errors that centralized logic constructs, like switch statements, are prone to**.**

Ultimately, my experience has been that this technique finds an ideal middle ground between inflexible switch/if-then cruft and [over-complicated “rules engines”](http://thedailywtf.com/Articles/The_Enterprise_Rules_Engine.aspx) **.** I hope you find it as useful as I have.

My question to you is: Did you find this useful**?** Are you going to replace your switch statements with the functional approach going forward**?** Were you already doing this**?**
