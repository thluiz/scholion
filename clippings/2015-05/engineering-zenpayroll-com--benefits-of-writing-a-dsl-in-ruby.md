---
url: "http://engineering.zenpayroll.com/benefits-of-writing-a-dsl/"
captured_at: "2015-05-06T17:47:23-03:00"
title: "Benefits of Writing a DSL in Ruby"
domain: "engineering-zenpayroll-com"
---

# Benefits of Writing a DSL in Ruby

Monday, September 29, 2014

Here at ZenPayroll, we're all about abstracting away the complexities that come with compensation. Payroll has traditionally been a bureaucratic hornet's nest, and implementing a modern and delightful product in such an atmosphere is an engaging technical challenge--one that is difficult to achieve without automation.

ZenPayroll is currently pushing to provide nationwide service (we're at 24 states and counting!), which demands we satisfy a bevvy of unique requirements for each state. Initially, we found ourselves writing a lot of boilerplate code by hand, instead of concentrating on what made each state a snowflake. We soon realized that this was a problem that could reap enormous benefits from tooling--namely, creating a *domain specific language* to accelerate and streamline the development process.

In this article, we're going to build one such DSL that broadly resembles what we use in-house, if a bit simpler.

# Identifying Use Cases for a DSL

Writing a DSL is a lot of hard work, and it isn't a silver bullet for all problems. In our case, however, the pros far outweighed the cons:

1. **Consolidation of state-specific code**   
   In our Rails app, we have several models where we have to implement specific code for each state. We need to generate forms, store and manipulate mandatory information pertaining to employees, companies, filing schedules and tax rates. We make payments to government agencies, file the generated forms, calculate payroll taxes, and more. A DSL implementation allows us to consolidate and organize all of the state-specific code into a dedicated directory and primary file.
2. **Scaffolding for states**   
   Rather than starting from scratch for every new state, using a DSL provides scaffolding to automate common tasks across states, while still providing flexibility for full customization.
3. **Reduced surface area for errors**   
   Having a DSL creates the classes and methods we need to eliminate boilerplate code and provides fewer touch points for developers. By thoroughly testing a DSL and guarding against invalid input, chances for error are reduced dramatically.
4. **Provides a toolkit to accelerate expansion**   
   We've created a framework that makes it easier to implement unique compliance requirements for new states. A DSL is a focused toolkit that reduces the time it takes to develop going forward.

# Writing the DSL

For the scope of this tutorial, we will focus on creating a domain specific language that will allow us to collect identification numbers for companies and payroll parameters for employees (used for calculating taxes). While this is a mere glimpse into what we can accomplish with a DSL, it still provides a comprehensive introduction to the subject. Our final DSL will look something like this:

```
StateBuilder.build('CA') do  
  company do
    edd { format '\d{3}-\d{4}-\d' }
    sos { format '[A-Z]\d{7}' }
  end

  employee do
    filing_status { options ['Single', 'Married', 'Head of Household'] }
    withholding_allowance { max 99 }
    additional_withholding { max 10000 }
  end  
end
```

Awesome! This is clean, concise, and expressive code, using an interface designed for solving our challenge. Let's get started.

### Define Parameters

First, let's define what we need our DSL to accomplish. First question to ask: *what kind of information do we need to store?*

Every state requires companies to register with local authorities. Upon registration in most states, companies are provided with identification numbers to pay taxes and file forms. On a company level, we need a dynamic way to *store different identification numbers* for each state.

Withholding tax is computed based on the number of allowances an employee claims. These are values that are found on state level W-4 forms. For each state, a variety of different questions can be asked to determine state income tax rates, such as your filing status, dependent exemptions, disability allowances, and more. For employees, we need a flexible method of *defining different attributes for each state*, in order to compute taxes accordingly.

The DSL we will write will handle company identification numbers and basic payroll information for employees. We will then use the tool to implement California. While California has several other details that are necessary to consider when computing payroll, we will focus on these areas in order to get an overview of how to implement a DSL.

I have provided a link to a basic Rails application in order to easily follow along with this tutorial that can be found [here](https://github.com/ZenPayroll/zen-dsl-tutorial).

The setup of the app models is as follows:

- **Company**: Represents the company entity. Stores information such as the name, the corporation type, and date established.
- **Employee**: Represents a single employee that works at a company. Stores information such as name, payment information, and when they were hired.
- **CompanyStateField**: A `Company` has many `CompanyStateFields`, and each one handles one state's information pertaining to a company. This includes state identification numbers. California requires two numbers from employers, the Employment Development Department number (EDD) and the Secretary of State number (SoS), more information can be found [here](http://help.zenpayroll.com/customer/portal/articles/1084488-what-is-a-california-edd-number-).
- **EmployeeStateField**: An `Employee` has many `EmployeeStateFields`, and each one handles one state's specific information for a employee. This includes information found on state W-4's like withholding allowance and filing status. California's form, [the DE 4](http://www.edd.ca.gov/pdf_pub_ctr/de4.pdf), requires that we collect withholding allowances, an additional withholding dollar amount, and the employee's filing status (Single, Married, or Head of Household).

We have setup [single table inheritance](http://api.rubyonrails.org/classes/ActiveRecord/Base.html#label-Single+table+inheritance) for the `CompanyStateField` and `EmployeeStateField` models. This allows us to define state specific subclasses for `CompanyStateField` and `EmployeeStateField` and use only one table per model to handle states. To bolster this, both tables have a serialized data hash that we wil use to store values specific to a state. Although this data will not be queryable, it allows us to store state specific information without cluttering our database with unnecessary columns.

Our app is setup to handle states, and now our DSL must create the state specific classes that will implement California's functionality.

## Tools of the Trade

Metaprogramming is where Ruby really shines as a language. We can define methods and classes at runtime as well as make use of a variety of metaprogramming tools that make creating a DSL in Ruby a joy. Rails itself is a DSL for creating web applications, and the framework draws a lot of its "magic" from Ruby's metaprogramming capabilities. Below are a list of the some of the methods and objects that are useful for metaprogramming.

### [Blocks](http://rubymonk.com/learning/books/1-ruby-primer/chapters/34-lambdas-and-blocks-in-ruby/lessons/78-blocks-in-ruby)

The block syntax allows us group code together and pass it as an argument to a method. They can be defined with `do` `end` syntax, or be encapsulated within curly braces, they are synonymous. You will have most likely seen these when using a method like `each`.

`[1,2,3].each { |number| puts number*2 }`

This is an excellent tool for creating DSL's because they allow you to define code in one context and execute it in another. This is powerful for creating readable DSL's by abstracting method definitions into other classes; we will go through many examples of this throughout the tutorial.

### *[send](http://ruby-doc.org/core-2.1.2/Object.html#method-i-send)*

The `send` method allows you to invoke a method (even private ones) on an object by passing in the name as a symbol. This is useful for invoking methods that are usually called within the class definition, as well as for interpolating variables for dynamic method calls.

### *[define\_method](http://www.ruby-doc.org/core-2.1.2/Module.html#method-i-define_method)*

Ruby's `define_method` provides the ability to create methods without having to use the traditional `def` within the class definition. `define_method` takes a string for the method name and a block to determine what code should be executed when the method is invoked.

### *[instance\_eval](http://www.ruby-doc.org/core-2.1.2/BasicObject.html#method-i-instance_eval)*

`instance_eval` is an essential tool for developing DSL's, much like blocks are. `instance_eval` takes a block and executes it within the context of the receiver. For example:

```
class MyClass  
  def say_hello
    puts 'Hello!'
  end
end

MyClass.new.instance_eval { say_hello }   # => 'Hello!'
```

In the above example, the block contains a call to the method `say_hello`, even though there is no corresponding method definition in the context. The instance returned by `MyClass.new` is the receiver and we execute `say_hello` within that context.

```
class MyOtherClass  
  def initialize(&block)
    instance_eval &block
  end

  def say_goodbye
    puts 'Goodbye!'
  end
end

MyOtherClass.new { say_goodbye }   # => 'Goodbye!'
```

We again define a block that will call a method that is not defined in the context. This time, we pass the block to the `MyOtherClass` constructor and evaluate its contents within the context of the default receiver `self`, which is an instance of `MyOtherClass`. Pretty sweet!

### *[method\_missing](http://www.ruby-doc.org/core-2.1.2/BasicObject.html#method-i-method_missing)*

This is the magic behind Rails's `find_by_*` methods that match every column of your tables. With `method_missing`, any method you call that is not defined will go through this method, passing its name and any arguments along as well. This is another great tool for DSL's because it allows methods to be defined dynamically with no prior knowledge of what might be called, leading to highly customized syntax.

## Designing and Implementing the DSL

Now that we have some background about our toolkit, we should think about how we want our DSL to look and what it would be like to use it for developing states. In this sense, we are working backwards; rather than starting by defining classes and methods, we will invent an ideal syntax and build classes around it to suit our needs. Think of this as an outline of how we want our DSL to be implemented. Let's take a look again at what our final implementation will look like:

```
StateBuilder.build('CA') do  
  company do
    edd { format '\d{3}-\d{4}-\d' }
    sos { format '[A-Z]\d{7}' }
  end

  employee do
    filing_status { options ['Single', 'Married', 'Head of Household'] }
    withholding_allowance { max 99 }
    additional_withholding { max 10000 }
  end  
end
```

Let's break this down piece by piece and incrementally write the code that will turn this into the classes and methods we need to implement CA.

---

If you want to follow along with the repo provided, you can `git checkout step-0` and fill in the code as we go through it.

---

Our DSL is called the `StateBuilder` and is a class. We start each state by calling a class level `build` method with a state abbreviation and a configuration block. Within this block, we can then make calls to methods we will define called `company` and `employee`, and pass them each a block to configure our specific models (`CompanyStateField::CA`, `EmployeeStateField::CA`).

##### *app/states/ca.rb*

```
StateBuilder.build('CA') do  
  company do
    # CompanyStateField::CA configuration
  end

  employee do
    # EmployeeStateField::CA configuration
  end
end
```

As mentioned before, our logic is encapsulated in a `StateBuilder` class. We call the block passed to `self.build` within the context of a new instance of `StateBuilder`, so `company` and `employee` must be defined methods that each accept a block of their own. Let's setup the scaffolding for this by defining a `StateBuilder` class that fits this specification.

##### *app/models/state\_builder.rb*

```
class StateBuilder  
  def self.build(state, &block)
    # If no block is passed in, raise an exception
    raise "You need a block to build!" unless block_given?

    StateBuilder.new(state, &block)
  end

  def initialize(state, &block)
    @state = state

    # Evaluate the contents of the block passed in within the context of this instance of StateBuilder
    instance_eval &block
  end

  def company(&block)
    # Configure CompanyStateField::CA
  end

  def employee(&block)
    # Configure EmployeeStateField::CA
  end
end
```

We've got the basic setup of our `StateBuilder`! Since our `company` and `employee` methods will define our `CompanyStateField::CA` and `EmployeeStateField::CA` classes, let's design how we want each of the blocks passed to their respective methods to look. We need to define each of the attributes our models should have, as well as some basic information about them. What's great about creating a custom DSL is that we do not have to use traditional Rails syntax for getters/setters and validations; instead let's use the concise syntax we looked at earlier in the article.

---

It's time to `git checkout step-1`, folks!

---

For companies in California, we need to store two identification numbers: the California Employment Development Department number (or EDD number) and the California Secretary of State number (or SoS number).

The EDD number has a format of "###-####-#" and the SoS number has a format of '@#######', where `@` is any letter and `#` is any digit.

Ideally, we would use the name of our attribute as a method call and pass in a block that defines a format for that particular attribute (I smell a use case for `method_missing`!). Let's go ahead and write out what these method calls would look like for the EDD and SoS numbers.

##### *app/states/ca.rb*

```
StateBuilder.build('CA') do  
  company do
    edd { format '\d{3}-\d{4}-\d' }
    sos { format '[A-Z]\d{7}' }
  end

  employee do
    # EmployeeStateField::CA configuration
  end  
end
```

Notice here we have switched out Ruby's do end syntax for curly braces, but it still accomplishes the same task of passing in a block with code to be executed to the method. Let's follow this same process for the employee side configuration for California.

On the [California Employee's Withholding Allowance Certificate (DE4)](http://www.edd.ca.gov/pdf_pub_ctr/de4.pdf), employees are asked for their filing status, number of withholding allowances, and any additional withholding amounts an employee may have. The filing status can be either Single, Married, or Head of Household, the withholding allowance must be under 99, and let's set a maximum of $10,000 for the additional withholding dollar amount. Let's implement these attributes and validations like we did for the company method.

##### *app/states/ca.rb*

```
StateBuilder.build('CA') do  
  company do
    edd { format '\d{3}-\d{4}-\d' }
    sos { format '[A-Z]\d{7}' }
  end

  employee do
    filing_status { options ['Single', 'Married', 'Head of Household'] }
    withholding_allowance { max 99 }
    additional_withholding { max 10000 }
  end  
end
```

And we've arrived at our final CA implementation! Our DSL now defines attributes and validations for both our `CompanyStateField::CA` and our `EmployeeStateField::CA` using custom syntax.

Now, we need to translate our syntax into class definitions, attribute getters/setters, and validations. Let's move on to implementing the `company` and `employee` methods within the `StateBuilder` itself and get this functionality working.

---

Proceed to `git checkout step-2`, metaprogrammers!

---

We will implement our methods and validations by defining what to do with each block in the `StateBuilder#company` and `StateBuilder#employee` methods. Let's take a similar approach to what we did when we first defined the `StateBuilder`: create a "scope" that will handle these methods and `instance_eval` our block in its context.

Let's call our scopes `StateBuilder::CompanyScope` and `StateBuilder::EmployeeScope` and setup our `StateBuilder` methods to create a new instance of each class.

##### *app/models/state\_builder.rb*

```
class StateBuilder  
  def self.build(state, &block)
    # If no block is passed in, raise an exception
    raise unless block_given?

    StateBuilder.new(state, &block)
  end

  def initialize(state, &block)
    @state = state

    # Evaluate the contents of the block passed in within the context of this instance of StateBuilder
    instance_eval &block
  end

  def company(&block)
    StateBuilder::CompanyScope.new(@state, &block)
  end

  def employee(&block)
    StateBuilder::EmployeeScope.new(@state, &block)
  end
end
```

##### *app/models/state\_builder/company\_scope.rb*

```
class StateBuilder  
  class CompanyScope
    def initialize(state, &block)
      @klass = CompanyStateField.const_set state, Class.new(CompanyStateField)

      instance_eval &block
    end
  end
end
```

##### *app/models/state\_builder/employee\_scope.rb*

```
class StateBuilder  
  class EmployeeScope
    def initialize(state, &block)
      @klass = EmployeeStateField.const_set state, Class.new(EmployeeStateField)

      instance_eval &block
    end
  end
end
```

We use `const_set` to define a subclass of `CompanyStateField` and `EmployeeStateField` with the name of our state. This yields a `CompanyStateField::CA` class and a `EmployeeStateField::CA` class, both inheriting from their respective parents.

Now we can focus on the final level, the blocks passed to each of our attributes (like `sos`, `edd`, `additional_withholding`, etc). These will be executed within the context of `CompanyScope` and `EmployeeScope`, but if you run the server you will see `undefined method` errors.

Let's use the `method_missing` method to catch these cases. With our current setup, we can assume every method being called is the name of an attribute and the blocks passed into these methods are how we want to configure that attribute. This gives us the "magic" ability to define the attributes we want and store them in the database.

**Warning**: using `method_missing` without any cases to call `super` can lead to unexpected behavior. Misspellings will be hard to track down as they will all fall into `method_missing`. Be sure to create cases for when `method_missing` should call `super` when expanding on these principles.

Let's define a `method_missing` function and pass those parameters to a final scope we will create called `AttributesScope`, which will define our `store_accessors` and `validates` according to what methods are called within each attribute block.

##### *app/models/state\_builder/company\_scope.rb*

```
class StateBuilder  
  class CompanyScope
    def initialize(state, &block)
      @klass = CompanyStateField.const_set state, Class.new(CompanyStateField)

      instance_eval &block
    end

    def method_missing(attribute, &block)
      AttributesScope.new(@klass, attribute, &block)
    end
  end
end
```

##### *app/models/state\_builder/employee\_scope.rb*

```
class StateBuilder  
  class EmployeeScope
    def initialize(state, &block)
      @klass = EmployeeStateField.const_set state, Class.new(EmployeeStateField)

      instance_eval &block
    end

    def method_missing(attribute, &block)
      AttributesScope.new(@klass, attribute, &block)
    end
  end
end
```

Now whenever we call a method in the `company` block of our `app/states/ca.rb` file, it will hook into this `method_missing` function. The name of the method that was called will be the first argument to `method_missing` and it is also the name of the attribute we defining. We create a new instance of `AttributesScope` with the class we will be modifying, the name of attribute we are defining, and a block to configure that attribute. In our `AttributesScope`, we will call `store_accessor` to define getters/setters for the attribute, and we'll use the serialized data hash to store it.

```
class StateBuilder  
  class AttributesScope
    def initialize(klass, attribute, &block)
      klass.send(:store_accessor, :data, attribute)
      instance_eval &block
    end
  end
end
```

Last but not least, we need to define the methods we call in our attributes blocks (`format`, `max`, and `options`) and turn them into validations. We accomplish this by manipulating our method calls into `validates` calls that Rails expects.

```
class StateBuilder  
  class AttributesScope
    def initialize(klass, attribute, &block)
      @validation_options = []

      klass.send(:store_accessor, :data, attribute)
      instance_eval &block
      klass.send(:validates, attribute, *@validation_options)
    end

    private
    def format(regex)
      @validation_options << { format: { with: Regexp.new(regex) } }
    end

    def max(value)
      @validation_options << { numericality: { greater_than_or_equal_to: 0, less_than_or_equal_to: value } }
    end

    def options(values)
      @validation_options << { inclusion: { in: values } }
    end
  end
end
```

And our DSL is up and running! We have successfully defined a `CompanyStateField::CA` model that stores and validates our EDD and SoS numbers as well as a `EmployeeStateField::CA` model that stores and validates the withholding allowance, filing status, and additional withholding amounts of our employees. While our DSL was implemented to automate fairly simple tasks, each of our scopes is setup to be expanded. We can easily add new hooks to our DSL, define more methods on our models, and build upon the functionality we created here.

Our implementation effectively reduces repetition and boilerplate code across the backend, but it still requires each state to have a unique view on the client side. We have expanded our in house implementation to also drive our frontend for new states, and if there is interest in the comments, I will write another blog post to expand on what we have created here.

This tutorial details just a portion of how we used our own DSL to tackle state expansion. Tools like this have proved extremely valuable in expanding our payroll services to the rest of the US, and if problems of this nature interest you, we are [hiring](https://zenpayroll.com/careers)!

Happy Metaprogramming!

Comments on [Hacker News](https://news.ycombinator.com/item?id=8391836)
