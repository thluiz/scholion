---
url: "http://blog.elpassion.com/ruby-gotchas/?utm_source=rubyweekly&utm_medium=email"
captured_at: "2014-03-05T11:04:25-03:00"
title: "Ruby Gotchas that will come back to haunt you"
domain: "blog-elpassion-com"
---

# Ruby Gotchas that will come back to haunt you

Most Ruby on Rails beginners get excited by the framework and start crafting applications without any knowledge of the language. And there’s nothing wrong about it. At least, unless those beginners persist in such approach and become *senior* developers without any knowledge of the language.

Anyway, sooner or later, beginners or experienced programmers, we all run into so-called Ruby Gotchas – those small language subtleties that hide from our sight for hours of hardcore debugging (*puts “1″*) and then we go *That was that??! Really, this time I promise, I WILL read that book with a hammer on the cover!* Or, rather, we go *shit!* and fall asleep.

Here is a list of popular Ruby gotchas and curiosities that developers should be aware of. For each case, there’s an example of confusing and/or error-prone code.

There are also good practices that will simplify your (and your code’s maintainer’s) life if you just stick to them. If you do not believe they are really good practices, read further through the details with more verbose explanation on why the particular gotcha can cause bugs (mostly because it does something else than most people think).

---

## `and / or` is NOT the same as `&& / ||`

```
surprise = true and false # => surprise is true
surprise = true && false  # => surprise is false
```

```
surprise = true and false # => surprise is true
surprise = true && false  # => surprise is false
```

**Good practice**

Use only `&& / ||` operators.

**In detail**

- `and / or` operators have lower [precedence](http://www.techotopia.com/index.php/Ruby_Operator_Precedence#Operator_Precedence_Table "precedence") than `&& / ||`
- `and / or` have lower precedence than `=` assignment operator, while `&& / ||` are of higher precedence
- `and` and `or` have the same precedence, while `&&` has higher precedence than `||`

The first example becomes clearer when we add parentheses that illustrate how using `and` differs from `&&`:

```
(surprise = true) and false # => surprise is true
surprise = (true && false)  # => surprise is false
```

```
(surprise = true) and false # => surprise is true
surprise = (true && false)  # => surprise is false
```

Some say: use `and / or` for flow control and `&& / ||` for boolean operations. I will say: don’t use keyword versions (`and / or / not`) at all (and go with more verbose `if`s and `unless`es). Less ambiguity, less confusion, less bugs.

More: [Difference between “or” and || in Ruby?](http://stackoverflow.com/questions/2083112/difference-between-or-and-in-ruby "Difference between “or” and || in Ruby?")

---

## `eql?` is NOT the same as `==` (and NOT the same as `equal?` or `===`)

```
1 == 1.0   # => true
1.eql? 1.0 # => false
```

```
1 == 1.0   # => true
1.eql? 1.0 # => false
```

**Good practice**

Use only `==` operator.

**In detail**

`==`, `===`, `eql?` and `equal?` are all different operators, meant for different usage in different situations. You should always use `==` operator for comparing things, unless you have some specific needs (like you *really* need to differ `1.0` from `1`) or manually override one of the equality operators for whatever reason.

Yes, the `eql?` version may look *smarter* than plain old `==` comparison, but does it really do what you meant it to do, like, just *compare some things*?

More: [What’s the difference between equal?, eql?, ===, and ==?](http://stackoverflow.com/questions/7156955/whats-the-difference-between-equal-eql-and "What’s the difference between equal?, eql?, ===, and ==?")

---

## `super` is NOT the same as `super()`

```
class Foo
  def show
    puts 'Foo#show'
  end
end

class Bar < Foo
  def show(text)
    super

    puts text
  end
end

Bar.new.show('test') # ArgumentError: wrong number of arguments (1 for 0)
```

```
class Foo
  def show
    puts 'Foo#show'
  end
end

class Bar < Foo
  def show(text)
    super

    puts text
  end
end

Bar.new.show('test') # ArgumentError: wrong number of arguments (1 for 0)
```

**Good practice**

This is one of the places where omitting the parentheses is not only a matter of taste (or conventions), but actually changes the program logic.

**In detail**

- `super` (without parentheses) will call parent method **with exactly the same arguments that were passed to the original method** (so `super` inside `Bar#show` becomes `super('test')` here, causing an error, because parent method does not take any arguments).
- `super()` (with parentheses) will call parent method **without any arguments**, just as expected.

More: [Super keyword in Ruby](http://stackoverflow.com/questions/4632224/super-keyword-in-ruby "Super keyword in Ruby")

---

## Your exception must not be an `Exception`

```
class MyException < Exception
end

begin
  raise MyException
rescue
  puts 'Caught it!'
end

# MyException: MyException
#       from (irb):17
#       from /Users/karol/.rbenv/versions/2.1.0/bin/irb:11:in `<main>'
```

```
class MyException < Exception
end

begin
  raise MyException
rescue
  puts 'Caught it!'
end

# MyException: MyException
#       from (irb):17
#       from /Users/karol/.rbenv/versions/2.1.0/bin/irb:11:in `<main>'
```

(This code will not catch `MyException` and the message `'Caught it!'` will not be displayed.)

**Good practice**

- When defining your own exception class, inherit from `StandardError` or any of its descendants (the more specific, the better). Never use `Exception` for the parent.
- Never `rescue Exception`. If you want to do some general rescue, leave `rescue` statement empty (or use `rescue => e` to access the error).

**In detail**

- When you leave `rescue` statement empty, it means it will catch exceptions that inherit from `StandardError`, not `Exception`.
- When you `rescue Exception` (which you should not), you’ll catch errors you won’t be able to recover from (like out of memory error). Also, you’ll catch system signals like SIGTERM, and in effect you won’t be able to terminate your script using CTRL-C.

More: [Why is it bad style to `rescue Exception => e` in Ruby?](http://stackoverflow.com/questions/10048173/why-is-it-bad-style-to-rescue-exception-e-in-ruby "Why is it bad style to `rescue Exception => e` in Ruby?")

---

## `class Foo::Bar` is NOT the same as `module Foo; class Bar`

```
MY_SCOPE = 'Global'

module Foo
  MY_SCOPE = 'Foo Module'

  class Bar
    def scope1
      puts MY_SCOPE
    end
  end
end

class Foo::Bar
  def scope2
    puts MY_SCOPE
  end
end

Foo::Bar.new.scope1 # => "Foo Module"
Foo::Bar.new.scope2 # => "Global"
```

```
MY_SCOPE = 'Global'

module Foo
  MY_SCOPE = 'Foo Module'

  class Bar
    def scope1
      puts MY_SCOPE
    end
  end
end

class Foo::Bar
  def scope2
    puts MY_SCOPE
  end
end

Foo::Bar.new.scope1 # => "Foo Module"
Foo::Bar.new.scope2 # => "Global"
```

**Good practice**

Always use longer, more verbose version with classes wrapped by modules:

```
module Foo
  class Bar
  end
end
```

```
module Foo
  class Bar
  end
end
```

**In detail**

- `module` keyword (as well as `class` and `def`) will create new lexical scope for all the things you put inside. So, our `module Foo` creates the scope `'Foo'` in which our `MY_SCOPE` constant with `'Foo Module'` value resides.
- Inside this module, we declare `class Bar`, which creates new lexical scope (named `'Foo::Bar'`), which has access to its parent scope (`'Foo'`) and all constants declared in it.
- However, when you declare Foo::Bar with this `::` “shortcut”: `class Foo::Bar`, it creates another lexical scope, which is also named `'Foo::Bar'`, but here, it has no parent, and thus, no access to things from `'Foo'` scope.
- Therefore, inside `class Foo::Bar`, we have only access to `MY_SCOPE` constant declared at the beginning of the script (without any module) with value `'Global'`.

More: [Ruby – Lexical scope vs Inheritance](http://stackoverflow.com/questions/15119724/ruby-lexical-scope-vs-inheritance "Ruby – Lexical scope vs Inheritance")

---

## Most `bang!` methods return `nil` when they do nothing

```
'foo'.upcase! # => "FOO"
'FOO'.upcase! # => nil
```

```
'foo'.upcase! # => "FOO"
'FOO'.upcase! # => nil
```

**Good practice**

Never depend on built-in `bang!` methods return value, e.g. in conditional statements or in control flow:

```
@name.upcase! and render :show
```

```
@name.upcase! and render :show
```

Above code can cause some unpredictable behaviour (or, to be more specific, very predictable failure when `@name` is already in uppercase). Also, it is another example why you should not use `and / or` for control-flow shortcuts. No trees will be cut if you add those two enters there:

```
@name.upcase!

render :show
```

```
@name.upcase!

render :show
```

  
  

---

## `attribute=(value)` method always returns passed `value`, regardless of method return value

```
class Foo
  def self.bar=(value)
    @foo = value

    return 'OK'
  end
end

Foo.bar = 3 # => 3
```

```
class Foo
  def self.bar=(value)
    @foo = value

    return 'OK'
  end
end

Foo.bar = 3 # => 3
```

(Note that the assignment method `bar=` returns `3` even though we explicitly `return 'OK'` at the end of its body.)

**Good practice**

Never rely on anything that happens inside assignment method, eg. in conditional statements like this:

```
puts 'Assigned' if (Foo.bar = 3) == 'OK' # => nil
```

```
puts 'Assigned' if (Foo.bar = 3) == 'OK' # => nil
```

This will obviously not work.

More: [ruby, define []= operator, why can’t control return value?](http://stackoverflow.com/questions/6366834/ruby-define-operator-why-cant-control-return-value "ruby, define []= operator, why can’t control return value?")

---

## `private` will NOT make your `self.method` private

```
class Foo

  private
  def self.bar
    puts 'Not-so-private class method called'
  end

end

Foo.bar # => "Not-so-private class method called"
```

```
class Foo

  private
  def self.bar
    puts 'Not-so-private class method called'
  end

end

Foo.bar # => "Not-so-private class method called"
```

(Note that if the method were private, `Foo.bar` would raise `NoMethodError`.)

**Good practice**

In order to make your class method private, you have to use `private_class_method :method_name` or put your private class method inside `class << self` block:

```
class Foo

  class << self
    private    
    def bar
      puts 'Class method called'
    end    
  end

  def self.baz
    puts 'Another class method called'
  end
  private_class_method :baz

end

Foo.bar # => NoMethodError: private method `bar' called for Foo:Class
Foo.baz # => NoMethodError: private method `baz' called for Foo:Class
```

```
class Foo

  class << self
    private    
    def bar
      puts 'Class method called'
    end    
  end

  def self.baz
    puts 'Another class method called'
  end
  private_class_method :baz

end

Foo.bar # => NoMethodError: private method `bar' called for Foo:Class
Foo.baz # => NoMethodError: private method `baz' called for Foo:Class
```

More: [creating private class method](http://stackoverflow.com/questions/4952980/creating-private-class-method "creating private class method")

---

## I ain’t afraid of no Ruby Gotchas

Ruby gotchas listed above may not look like a big deal, and at first sight they may seem they are simple matter of aesthetics or conventions.

Trust me – if you don’t deal with them, eventually they will lead to some nasty headaches during [Ruby on Rails development](http://www.elpassion.com/ruby-on-rails-development/ "Ruby on Rails development"). And will cause heartbreak. Because you’ll fall out of love with Ruby. And then you’ll stay alone. Forever.
