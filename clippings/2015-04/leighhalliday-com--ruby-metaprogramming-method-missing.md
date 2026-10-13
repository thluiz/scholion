---
url: "http://www.leighhalliday.com/ruby-metaprogramming-method-missing"
captured_at: "2015-04-10T11:22:57-03:00"
title: "Ruby Metaprogramming - Method Missing"
domain: "leighhalliday-com"
---

# Ruby Metaprogramming - Method Missing

## What is method\_missing?

`method_missing` is a method that ruby gives you access inside of your objects a way to handle situations when you call a method that doesn't exist. It's sort of like a Begin/Rescue, but for method calls. It gives you one last chance to deal with that method call before an exception is raised.

## What does it look like?

`method_missing` accepts 3 parameters.  
1. The first is the name of the method you were trying to call.  
2. The second is the args (`*args`) that were passed to the method.  
3. The third is a block (&block) that was passed to the method.

The 2nd and 3rd params may be empty if the method was called without arguments, but they are there anyway for you to use and/or pass on to another method.

```
def method_missing(m, *args, &block)
end
```

## Using method\_missing

I can immediately think of 2 uses for using method\_missing in your code.  
1. **Dealing with repetitive methods that function the same**: I recently wrote an article on [creating a DSL in Ruby](http://www.leighhalliday.com/creating-ruby-dsl). For the example I created a DSL for generating HTML tags. I didn't want to define a method for every single HTML tag, so instead I just used method\_missing, to sort of dynamically create HTML tags as they were called.  
2. **Delegating method calls to another object**: You could write a simple presenter and define your own delegation method using `method_missing`. This is the example I am going to present below. Most likely you would want to use [SimpleDelegator](http://ruby-doc.org/stdlib-2.1.0/libdoc/delegate/rdoc/SimpleDelegator.html) to implement this, but for the sake of demoing how it works we will do it ourselves.

## Creating a Presenter

### Using Delegation and Method Missing

We are going to create a Presenter class. The purpose of the class is to accept an object in the constructor, and any methods we call that aren't specifically implemented by our Presenter will be delegated to the object it was instantiated with.

```
class Presenter
  attr_accessor :object

  initialize(object)
    .object = object
  

  # If a method we call is missing, pass the call onto 
  # the object we delegate to.
  method_missing(m, *args, &block)
    puts "Delegating "
    object.send(m, *args, &block)
```

We are going to extend from our Presenter class to create a UserPresenter, specifically used for presenting User objects.

```
class UserPresenter < Presenter

  # We just want to display the first letter of the last name
  last_name
    "#{object.last_name[]}."
  

  full_name
    "#{first_name} #{last_name}"
  

# A mini User object to work with
 = Struct.new(:first_name, :last_name, )
user = .new("Leigh", "Halliday", )
user_presenter = UserPresenter.new(user)

puts user_presenter.full_name
puts user_presenter.age
```

Here is the output for our calls above. Notice that it delegates the `first_name` method to the User object, as well as the `age` method, but `last_name` isn't delegated because we wrote our own method to handle it.

```
Delegating first_name
Leigh H.
Delegating age
30
```

## Re-Creating the Alias method

To illustrate `method_missing` being used another way, we'll re-implement the `alias` method, calling it `mimic`. What we'll do is create a `mimic` method which is called at the class level. Its job is to build a lookup table of the different aliases our methods have.

Once we call a method that doesn't exist, our code will attempt to find an alias for that method before having to fail.

```
class Mimic
  @@mimic_lookup = {}

  .mimic(to, from)
    @@mimic_lookup[to] = from
  

  method_missing(m, *args, &block)
     @@mimic_lookup.include?(m.to_sym)
      .send(@@mimic_lookup[m.to_sym], *args, &block)
    
      raise ArgumentError.new("Method `` doesn't exist.")
    
  

class Alpaca < Mimic
  mimic :saludar, :greet

  greet
    puts "Hey there"
  

buddy = Alpaca.new
buddy.saludar
buddy.welcome
```

We see that it was able to successfully greet using the alias `saludar` (Spanish for greet), and then it correctly raised an exception when we called the `welcome` method.

```
Hey there
alias.rb:13:in `method_missing': Method `welcome` doesn't exist. (ArgumentError)
    from alias.rb:31:in `'
```
