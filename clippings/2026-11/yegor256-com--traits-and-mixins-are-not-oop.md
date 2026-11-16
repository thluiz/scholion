---
url: "https://yegor256.com/2017/03/07/traits-and-mixins.html"
captured_at: "2026-11-16T02:43:14+00:00"
title: "Traits and Mixins Are Not OOP"
domain: "yegor256-com"
---

Let me say right off the bat that the features we will discuss here are pure _poison_ brought to object-oriented programming by those who desperately needed a lobotomy, just like David West suggested in his [Object Thinking](https://amzn.to/2ass77O) book. These features have different names, but the most common ones are [traits](https://en.wikipedia.org/wiki/Trait_%28computer_programming%29) and [mixins](https://en.wikipedia.org/wiki/Mixin). I seriously can’t understand how we can still call programming object-oriented when it has [these features](http://stackoverflow.com/questions/925609/mixins-vs-traits).

![Fear and Loathing in Las Vegas (1998) by Terry Gilliam](https://yegor256.com/images/2014/04/fear-and-loathing-adrenochrome.png)

Fear and Loathing in Las Vegas (1998) by Terry Gilliam

First, here’s how they work in a nutshell. Let’s use [Ruby modules](http://phrogz.net/programmingruby/tut_modules.html) as a sample implementation. Say that we have a class `Book`:

```
class Book
  def initialize(title)
    @title = title
  end
end
```

Now, we want class `Book` to use a static method (a procedure) that does something useful. We may either define it in a [utility class](https://yegor256.com/2014/05/05/oop-alternative-to-utility-classes.html) and let `Book` call it:

```
class TextUtils
  def self.caps(text)
    text.split.map(&:capitalize).join(' ')
  end
end
class Book
  def print
    puts "My title is #{TextUtils.caps(@title)}"
  end
end
```

Or we may make it even more “convenient” and `extend` our module in order to access its methods directly:

```
module TextModule
  def caps(text)
    text.split.map(&:capitalize).join(' ')
  end
end
class Book
  extend TextModule
  def print
    puts "My title is #{caps(@title)}"
  end
end
```

It seems nice—if you don’t understand the [difference](https://yegor256.com/2014/05/05/oop-alternative-to-utility-classes.html) between [object-oriented programming](https://yegor256.com/2016/08/15/what-is-wrong-object-oriented-programming.html) and static methods. Moreover, if we forget [OOP purity](https://yegor256.com/2014/11/20/seven-virtues-of-good-object.html) for a minute, this approach actually looks less readable to me, even though it has fewer characters; it’s difficult to understand where the method `caps()` is coming from when it’s called just like `#{caps(@title)}` instead of `#{TextUtils.caps(@title)}`. Don’t you think?

Mixins start to play their role better when we `include` them. We can combine them to construct the behavior of the class we’re looking for. Let’s create two mixins. The first one will be called `PlainMixin` and will print the title of the book the way it is, and the second one will be called `CapsMixin` and will capitalize what’s already printed:

```
module CapsMixin
  def to_s
    super.to_s.split.map(&:capitalize).join(' ')
  end
end
module PlainMixin
  def to_s
    @title
  end
end
class Book
  def initialize(title)
    @title = title
  end
  include CapsMixin, PlainMixin
  def print
    puts "My title is #{self}"
  end
end
```

Calling `Book` without the included mixin will print its title the way it is. Once we add the `include` statement, the behavior of `to_s` is overridden and method `print` produces a different result. We can combine mixins to produce the required functionality. For example, we can add one more, which will [abbreviate](http://stackoverflow.com/a/25136035/187141) the title to 16 characters:

```
module AbbrMixin
  def to_s
    super.to_s.gsub(/^(.{16,}?).*$/m,'\1...')
  end
end
class Book
  def initialize(title)
    @title = title
  end
  include AbbrMixin, CapsMixin, PlainMixin
  def print
    puts "My title is #{self}"
  end
end
```

I’m sure you already understand that they both have access to the private attribute `@title` of class `Book`. They actually have full access to _everything_ in the class. They literally are “pieces of code” that we _inject_ into the class to make it more powerful and complex. What’s wrong with this approach?

It’s the same issue as with [annotations](https://yegor256.com/2016/04/12/java-annotations-are-evil.html), [DTOs](https://yegor256.com/2016/07/06/data-transfer-object.html), [getters](https://yegor256.com/2014/09/16/getters-and-setters-are-evil.html), and [utility classes](https://yegor256.com/2014/05/05/oop-alternative-to-utility-classes.html)—they tear objects apart and place pieces of functionality in places where objects don’t see them.

In the case of mixins, the functionality is in the Ruby `modules`, which make assumptions about the internal structure of `Book` and further assume that the programmer will still understand what’s in `Book` after the internal structure changes. Such assumptions completely violate the very idea of [encapsulation](https://yegor256.com/2016/11/21/naked-data.html).

Such a tight coupling between mixins and object private structure leads to nothing but unmaintainable and difficult to understand code.

The very obvious alternatives to mixins are [composable decorators](https://yegor256.com/2015/02/26/composable-decorators.html). Take a look at the example given in the [article](https://yegor256.com/2015/02/26/composable-decorators.html):

```
Text text = new AllCapsText(
  new TrimmedText(
    new PrintableText(
      new TextInFile(new File("/tmp/a.txt"))
    )
  )
);
```

Doesn’t it look very similar to what we were doing above with Ruby mixins?

However, unlike mixins, decorators leave objects small and cohesive, layering extra functionality on top of them. Mixins do the opposite—they make objects more complex and, thanks to that, less readable and maintainable.

I honestly believe they are just poison. Whoever invented them was a long ways from understanding the philosophy of object-oriented design.
