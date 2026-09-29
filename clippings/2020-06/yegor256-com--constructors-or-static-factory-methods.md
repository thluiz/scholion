---
url: "https://www.yegor256.com/2017/11/14/static-factory-methods.html"
captured_at: "2020-06-11T12:04:55-03:00"
title: "Constructors or Static Factory Methods?"
domain: "yegor256-com"
---

# Constructors or Static Factory Methods?

  
  

I believe Joshua Bloch said it first in his very good book [*Effective Java*](http://amzn.to/2zgpiRI): static factory methods are the preferred way to instantiate objects compared with constructors. I disagree. Not only because I believe that static methods are pure evil, but mostly because in this particular case they pretend to be good and make us think that we have to love them.

![extract.jpg](yegor256-com--constructors-or-static-factory-methods/75f8bdb1dd49bde872ce168c5028230d.jpg)

Extract (2009) by Mike Judge

Let’s analyze the reasoning and see why it’s wrong, from an object-oriented point of view.

This is a class with one primary and two secondary constructors:

```
class Color {
  private final int hex;
  Color(String rgb) {
    this(Integer.parseInt(rgb, 16));
  }
  Color(int red, int green, int blue) {
    this(red << 16 + green << 8 + blue);
  }
  Color(int h) {
    this.hex = h;
  }
}
```

This is a similar class with three static factory methods:

```
class Color {
  private final int hex;
  static Color makeFromRGB(String rgb) {
    return new Color(Integer.parseInt(rgb, 16));
  }
  static Color makeFromPalette(int red, int green, int blue) {
    return new Color(red << 16 + green << 8 + blue);
  }
  static Color makeFromHex(int h) {
    return new Color(h);
  }
  private Color(int h) {
    this.hex = h;
  }
}
```

Which one do you like better?

Giving birth to an object through its constructor is the most “sacred” moment in any object-oriented software, don’t miss the beauty of it!

According to Joshua Bloch, there are three basic advantages to using static factory methods instead of constructors (there are actually four, but the fourth one is not applicable to Java [anymore](https://docs.oracle.com/javase/7/docs/technotes/guides/language/type-inference-generic-instance-creation.html)):

- They have names.
- They can cache.
- They can subtype.

I believe that all three make perfect sense … if the design is wrong. They are good excuses for workarounds. Let’s take them one by one.

## They Have Names

This is how you make a [red tomato](http://www.rapidtables.com/web/color/red-color.htm) color object with a constructor:

```
Color tomato = new Color(255, 99, 71);
```

This is how you do it with a static factory method:

```
Color tomato = Color.makeFromPalette(255, 99, 71);
```

It seems that `makeFromPalette()` is semantically richer than just `new Color()`, right? Well, yes. Who knows what those three numbers mean if we just pass them to the constructor. But the word “palette” helps us figure everything out immediately.

True.

However, the right solution would be to use polymorphism and encapsulation, to decompose the problem into a few semantically rich classes:

```
interface Color {
}
class HexColor implements Color {
  private final int hex;
  HexColor(int h) {
    this.hex = h;
  }
}
class RGBColor implements Color {
  private final Color origin;
  RGBColor(int red, int green, int blue) {
    this.origin = new HexColor(
      red << 16 + green << 8 + blue
    );
  }
}
```

Now, we use the right constructor of the right class:

```
Color tomato = new RGBColor(255, 99, 71);
```

See, Joshua?

## They Can Cache

Let’s say I need a red tomato color in multiple places in the application:

```
Color tomato = new Color(255, 99, 71);
// ... sometime later
Color red = new Color(255, 99, 71);
```

Two objects will be created, which is obviously inefficient, since they are identical. It would be better to keep the first instance somewhere in memory and return it when the second call arrives. Static factory methods make it possible to solve this very problem:

```
Color tomato = Color.makeFromPalette(255, 99, 71);
// ... sometime later
Color red = Color.makeFromPalette(255, 99, 71);
```

Then somewhere inside the `Color` we keep a private static `Map` with all the objects already instantiated:

```
class Color {
  private static final Map<Integer, Color> CACHE =
    new HashMap<>();
  private final int hex;
  static Color makeFromPalette(int red, int green, int blue) {
    final int hex = red << 16 + green << 8 + blue;
    return Color.CACHE.computeIfAbsent(
      hex, h -> new Color(h)
    );
  }
  private Color(int h) {
    return new Color(h);
  }
}
```

It is very effective performance-wise. With a small object like our `Color` the problem may not be so obvious, but when objects are bigger, their instantiation and garbage collection may waste a lot of time.

True.

However, there is an object-oriented way to solve this problem. We just introduce a new class `Palette`, which becomes a store of colors:

```
class Palette {
  private final Map<Integer, Color> colors =
    new HashMap<>();
  Color take(int red, int green, int blue) {
    final int hex = red << 16 + green << 8 + blue;
    return this.computerIfAbsent(
      hex, h -> new Color(h)
    );
  }
}
```

Now, we make an instance of `Palette` once and ask it to return a color to us every time we need it:

```
Color tomato = palette.take(255, 99, 71);
// Later we will get the same instance:
Color red = palette.take(255, 99, 71);
```

See, Joshua, no static methods, no static attributes.

## They Can Subtype

Let’s say our class `Color` has a method `lighter()`, which is supposed to shift the color to the next available lighter one:

```
class Color {
  protected final int hex;
  Color(int h) {
    this.hex = h;
  }
  public Color lighter() {
    return new Color(hex + 0x111);
  }
}
```

However, sometimes it’s more desirable to pick the next lighter color through a set of available [Pantone](https://en.wikipedia.org/wiki/Pantone) colors:

```
class PantoneColor extends Color {
  private final PantoneName pantone;
  PantoneColor(String name) {
    this(new PantoneName(name));
  }
  PantoneColor(PantoneName name) {
    this.pantone = name;
  }
  @Override
  public Color lighter() {
    return new PantoneColor(this.pantone.up());
  }
}
```

Then, we create a static factory method, which will decide which `Color` implementation is the most suitable for us:

```
class Color {
  private final String code;
  static Color make(int h) {
    if (h == 0xBF1932) {
      return new PantoneColor("19-1664 TPX");
    }
    return new RGBColor(h);
  }
}
```

If the [true red](https://www.pantone.com/color-finder/19-1664-TPX) color is requested, we return an instance of `PantoneColor`. In all other cases it’s just a standard `RGBColor`. The decision is made by the static factory method. This is how we will call it:

```
Color color = Color.make(0xBF1932);
```

It would not be possible to do the same “forking” with a constructor, since it can only return the class it is declared in. A static method has all the necessary freedom to return any subtype of `Color`.

True.

However, in an object-oriented world we can and must do it all differently. First, we would make `Color` an interface:

```
interface Color {
  Color lighter();
}
```

Next, we would move this decision making process to its own class `Colors`, just like we did in the previous example:

```
class Colors {
  Color make(int h) {
    if (h == 0xBF1932) {
      return new PantoneColor("19-1664-TPX");
    }
    return new RGBColor(h);
  }
}
```

And we would use an instance of class `Colors` instead of a static faсtory method inside `Color`:

```
colors.make(0xBF1932);
```

[![mqdefault.jpg](yegor256-com--constructors-or-static-factory-methods/a21ea4f0f3d959785603d6fc74b4872a.jpg)](https://www.youtube.com/watch?v=9yjtsCK6Wdk)

A Few Thoughts About Constructors in OOP (webinar #7); 7 October 2015.

However, this is still not really an object-oriented way of thinking, because we’re taking the decision-making away from the object it belongs to. Either through a static factory method `make()` or a new class `Colors`—it doesn’t really matter how—we tear our objects into two pieces. The first piece is the object itself and the second one is the decision making algorithm that stays somewhere else.

A much more object-oriented design would be to put the logic into an object of class `PantoneColor` which would decorate the original `RGBColor`:

```
class PantoneColor {
  private final Color origin;
  PantoneColor(Color color) {
    this.origin = color;
  }
  @Override
  public Color lighter() {
    final Color next;
    if (this.origin.hex() == 0xBF1932) {
      next = new RGBColor(0xD12631);
    } else {
      next = this.origin.lighter();
    }
    return new PantoneColor(next);
  }
)
```

Then, we make an instance of `RGBColor` and decorate it with `PantoneColor`:

```
Color red = new PantoneColor(
  new RGBColor(0xBF1932)
);
```

We ask `red` to return a lighter color and it returns the one from the Pantone palette, not the one that is merely lighter in RGB coordinates:

```
Color lighter = red.lighter(); // 0xD12631
```

Of course, this example is rather primitive and needs [further improvement](https://www.yegor256.com/2016/12/20/can-objects-be-friends.html) if we really want it to be applicable to all Pantone colors, but I hope you get the idea. The logic must stay *inside* the class, not somewhere outside, not in static factory methods or even in some other supplementary class. I’m talking about the logic that belongs to this particular class, of course. If it’s something related to the management of class instances, then there can be containers and stores, just like in the previous example above.

To summarize, I would strongly recommend you *never* use static methods, especially when they are going to replace object constructors. Giving birth to an object through its constructor is [the most](https://www.yegor256.com/2014/10/03/di-containers-are-evil.html) “sacred” moment in any object-oriented software, don’t miss the beauty of it.

> The best place to make a new object is...
>
> — Yegor Bugayenko (@yegor256) [March 1, 2020](https://twitter.com/yegor256/status/1234047114252034048?ref_src=twsrc%5Etfw)
