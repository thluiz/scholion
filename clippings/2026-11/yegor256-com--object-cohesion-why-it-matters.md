---
url: "https://yegor256.com/2020/02/11/object-cohesion.html"
captured_at: "2026-11-16T02:21:31+00:00"
title: "Object Cohesion: Why It Matters"
domain: "yegor256-com"
---

You most probably know about [Elegant Objects](https://www.elegantobjects.org/) (EO), an alternative object-oriented paradigm, which claims that objects must be immutable, have no [static methods](https://yegor256.com/2014/05/05/oop-alternative-to-utility-classes.html), never use [NULL](https://yegor256.com/2014/05/13/why-null-is-bad.html) in their code, use [no annotations](https://yegor256.com/2016/04/12/java-annotations-are-evil.html), and so on. We, the EO adepts, claim many things, but not so many people believe us. Those non-believers [say](https://yegor256.com/testimonials.html) that we are trolls, [at best](https://yegor256.com/2020/05/13/career-killer.html). Their main argument is: everybody works differently, why should we listen to you? I have no answer for them… well I had no answer, until I created [jPeek](https://www.jpeek.org/) and started researching object _cohesion_.

![Кин-дза-дза! by Георгий Данелия](https://yegor256.com/images/2020/02/kin-dza-dza.jpg)

Кин-дза-дза! by Георгий Данелия

Let me explain how cohesion can help us, EO adepts, to _prove_ some of our assumptions.

[Cohesion](https://en.wikipedia.org/wiki/Cohesion_%28computer_science%29), as a characteristic of a software module, was invented by [Larry Constantine](https://en.wikipedia.org/wiki/Larry_Constantine) when I didn’t even exist yet, in 1974. Here is what it means; take a look at this simple Java class:

```
class Books {
  private List<String> titles;
  private List<Integer> prices;
  void addTitle(String title) {
    this.titles.add(title);
  }
  void addPrice(Integer price) {
    this.prices.add(price);
  }
}
```

There are two attributes and two methods. The method `addTitle()` works with the attribute `titles`, while the method `addPrice()` works only with the attribute `prices`. The cohesion is _low_ in this class, because the attributes `titles` and `prices` are not related to each other in any way. We can easily break this class into two pieces without losing anything:

```
class Books1 {
  private List<String> titles;
  void addTitle(String title) {
    this.titles.add(title);
  }
}
class Books2 {
  private List<Integer> prices;
  void addPrice(Integer price) {
    this.prices.add(price);
  }
}
```

Now, we have two much more cohesive classes: their attributes and methods are related to each other. We can’t break `Books1` anymore, since each attribute is needed by each method.

Here is yet another example of a _highly_ cohesive class:

```
class Books {
  private List<String> titles;
  void add(String title) {
    this.titles.add(title);
  }
  void delete(int id) {
    this.titles.remove(id);
  }
}
```

Can we break it into smaller pieces? No, we can’t. We can’t take any part of the class out. The attribute `titles` and both of the methods must stay together. This means that the class is _highly_ cohesive.

It was demonstrated a long time ago that more cohesive classes are better, in terms of their error-proneness, than the ones with low cohesion, for example by Victor R. Basili et al. in their study [A Validation of Object-Oriented Design Metrics as Quality Indicators](https://pdfs.semanticscholar.org/2bb8/c1f4eeb5e5ae353adeea0fd6933551b9e932.pdf).

Now, if we can empirically prove that, for example, classes without static methods are, on average, more cohesive than their static-rich fellows, we can say that the claim that “static methods are evil” (postulated by Elegant Objects) is scientifically validated. We can take a large set of random Java classes and calculate their cohesion. Then, we can separate those with static methods from those without them. Next, we can calculate which group has higher average cohesion. If the group without static methods wins, the assumption would be valid.

Of course, another random set of Java classes may produce different results, but this is how empirical science works: we can’t prove the theorem other than by some experiments.

[![badge](https://www.jpeek.org/logo.svg)](https://www.jpeek.org/)

I created an open source software library to help me do these experiments and called it [jPeek.org](https://www.jpeek.org/). It is a calculator of cohesion metrics for Java code. No surprise, there are many metrics we can use to calculate cohesion. At least [thirty](https://web.archive.org/web/20240619181537/http://www.math.md/files/csjm/v25-n1/v25-n1-\(pp44-74\).pdf) of them are published, while only a few of them were properly implemented. In jPeek, thanks to its contributors, we managed to implement over a dozen.

Using this tool we can empirically prove some of the key points of EO. For example, we can prove that [mutable](https://yegor256.com/2014/06/09/objects-should-be-immutable.html) classes are less cohesive, annotations negatively affect cohesion, [DTOs](https://yegor256.com/2016/07/06/data-transfer-object.html) are low-cohesion creatures, and many other things. Thus cohesion will become the vehicle which will drive Elegant Objects to a place where most of its claims will be scientifically proven. Give us a few more years and we will have very interesting results.
