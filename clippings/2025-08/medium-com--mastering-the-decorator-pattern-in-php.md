---
url: "https://medium.com/@murilolivorato/mastering-the-decorator-pattern-in-php-from-code-explosion-to-elegant-solutions-75fb47c8f458"
captured_at: "2025-08-14T20:52:30+01:00"
title: "Mastering the Decorator Pattern in PHP: From Code Explosion to Elegant Solutions | by Murilo Livorato | Jul, 2025 | Medium"
domain: "medium-com"
---

How to avoid the class explosion nightmare and build flexible, maintainable code
Have you ever found yourself creating …

---
[

![Murilo Livorato](https://miro.medium.com/v2/resize:fill:40:40/1*k3RfZvJpfBb4Y9gBS645sg.png)

](https://medium.com/@murilolivorato?source=post_page---byline--75fb47c8f458---------------------------------------)

_How to avoid the class explosion nightmare and build flexible, maintainable code_

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:875/1*JZVmeA6Rh8FWxoxgRbxa4A.png)

Have you ever found yourself creating dozens of classes just to handle different combinations of features? If you’re nodding your head, you’ve likely encountered the “class explosion” problem. Today, we’ll explore how the Decorator Pattern can save you from this maintenance nightmare and transform your PHP code into something elegant and extensible.

## The Problem: When Good Intentions Go Wrong

Let’s start with a real-world scenario. Imagine you’re building a coffee shop system. You start simple:

```
<span id="8865" data-selectable-paragraph=""><span>class</span> <span>SimpleCoffee</span> {<br>    <span><span>public</span> function <span>getCost</span>(): <span>float</span></span> {<br>        <span>return</span> <span>10.0</span>;<br>    }<br>    <br>    <span><span>public</span> function <span>getDescription</span>(): <span>string</span></span> {<br>        <span>return</span> <span>"Simple coffee"</span>;<br>    }<br>}</span>
```

Great! But then the business requirements expand. Customers start asking for milk, sugar, whipped cream… You think: ‘No problem, I’ll just create a class for each combination:

```
<span id="ec71" data-selectable-paragraph=""><span>class</span> <span>CoffeeWithMilk</span> {<br>    <span><span>public</span> function <span>getCost</span>(): <span>float</span></span> {<br>        <span>return</span> <span>12.0</span>; <br>    }<br>    <br>    <span><span>public</span> function <span>getDescription</span>(): <span>string</span></span> {<br>        <span>return</span> <span>"Simple coffee with milk"</span>;<br>    }<br>}<br><br><span>class</span> <span>CoffeeWithSugar</span> {<br>    <span><span>public</span> function <span>getCost</span>(): <span>float</span></span> {<br>        <span>return</span> <span>11.0</span>; <br>    }<br>    <br>    <span><span>public</span> function <span>getDescription</span>(): <span>string</span></span> {<br>        <span>return</span> <span>"Simple coffee with sugar"</span>;<br>    }<br>}<br><br><span>class</span> <span>CoffeeWithMilkAndSugar</span> {<br>    <span><span>public</span> function <span>getCost</span>(): <span>float</span></span> {<br>        <span>return</span> <span>13.0</span>; <br>    }<br>    <br>    <span><span>public</span> function <span>getDescription</span>(): <span>string</span></span> {<br>        <span>return</span> <span>"Simple coffee with milk with sugar"</span>;<br>    }<br>}</span>
```

## The Nightmare Unfolds

Now, let’s add whipped cream to the mix. Suddenly, you need:

-   `CoffeeWithWhippedCream`
-   `CoffeeWithMilkAndWhippedCream`
-   `CoffeeWithSugarAndWhippedCream`
-   `CoffeeWithMilkAndSugarAndWhippedCream`

That’s 8 classes for just 3 add-ons!This leads to exponential growth: with `n` ingredients, you need up to `2^n` classes. Add vanilla, caramel, and cinnamon, and you’re looking at 64 classes. Add one more ingredient? 128 classes!

## The Factory Becomes a Monster

Your factory method becomes unwieldy:

```
<span id="2957" data-selectable-paragraph=""><span><span>class</span> <span>CoffeeFactory</span> </span>{<br>    <span>public</span> <span><span>function</span> <span>createCoffee</span>(<span><span>array</span> <span>$ingredients</span></span>): <span>object</span> </span>{<br>        <span>$key</span> = <span>implode</span>(<span>'_'</span>, <span>array_unique</span>(<span>$ingredients</span>));<br>        <br>        <span>switch</span> (<span>$key</span>) {<br>            <span>case</span> <span>''</span>:<br>                <span>return</span> <span>new</span> <span>SimpleCoffee</span>();<br>            <span>case</span> <span>'milk'</span>:<br>                <span>return</span> <span>new</span> <span>CoffeeWithMilk</span>();<br>            <span>case</span> <span>'sugar'</span>:<br>                <span>return</span> <span>new</span> <span>CoffeeWithSugar</span>();<br>            <span>case</span> <span>'milk_sugar'</span>:<br>                <span>return</span> <span>new</span> <span>CoffeeWithMilkAndSugar</span>();<br>            <br>            <span>default</span>:<br>                <span>throw</span> <span>new</span> <span>Exception</span>(<span>"Unsupported combination: "</span> . <span>$key</span>);<br>        }<br>    }<br>}</span>
```

## The Red Flags

This approach violates several fundamental principles:

1.  **❌ Class Explosion**: Every combination requires its own class
2.  **❌ Code Duplication**: Similar logic repeated everywhere
3.  **❌ Violates Open/Closed Principle**: Adding features requires modifying existing code
4.  **❌ Maintenance Nightmare**: Price changes require updating dozens of classes
5.  **❌ Testing Complexity**: You need to test every possible combination

## Enter the Decorator Pattern

The Decorator Pattern is a structural design pattern that allows you to attach new behaviors to objects by placing them inside special wrapper objects. Think of it like gift wrapping: you can wrap a gift, then wrap the wrapped gift, and so on.

## The Four Key Components

1.  **Component Interface**: Defines what all coffee objects can do
2.  **Concrete Component**: The basic coffee implementation
3.  **Decorator**: Abstract wrapper that implements the component interface
4.  **Concrete Decorators**: Specific wrappers that add behaviors

## The Elegant Solution

Let’s rebuild our coffee system using the Decorator Pattern:

```
<span id="b3dd" data-selectable-paragraph=""><span><span>interface</span> <span>Coffee</span> </span>{<br>    <span>public</span> <span><span>function</span> <span>getCost</span>(): <span>float</span></span>;<br>    <span>public</span> <span><span>function</span> <span>getDescription</span>(): <span>string</span></span>;<br>}<br><br><br><span><span>class</span> <span>SimpleCoffee</span> <span>implements</span> <span>Coffee</span> </span>{<br>    <span>public</span> <span><span>function</span> <span>getCost</span>(): <span>float</span> </span>{<br>        <span>return</span> <span>10.0</span>;<br>    }<br>    <br>    <span>public</span> <span><span>function</span> <span>getDescription</span>(): <span>string</span> </span>{<br>        <span>return</span> <span>"Simple coffee"</span>;<br>    }<br>}<br><br><br><span>abstract</span> <span><span>class</span> <span>CoffeeDecorator</span> <span>implements</span> <span>Coffee</span> </span>{<br>    <span>protected</span> <span>$coffee</span>;<br>    <br>    <span>public</span> <span><span>function</span> <span>__construct</span>(<span>Coffee <span>$coffee</span></span>) </span>{<br>        <span>$this</span>-&gt;coffee = <span>$coffee</span>;<br>    }<br>    <br>    <span>public</span> <span><span>function</span> <span>getCost</span>(): <span>float</span> </span>{<br>        <span>return</span> <span>$this</span>-&gt;coffee-&gt;<span>getCost</span>();<br>    }<br>    <br>    <span>public</span> <span><span>function</span> <span>getDescription</span>(): <span>string</span> </span>{<br>        <span>return</span> <span>$this</span>-&gt;coffee-&gt;<span>getDescription</span>();<br>    }<br>}<br><br><br><span><span>class</span> <span>MilkDecorator</span> <span>extends</span> <span>CoffeeDecorator</span> </span>{<br>    <span>public</span> <span><span>function</span> <span>getCost</span>(): <span>float</span> </span>{<br>        <span>return</span> <span>parent</span>::<span>getCost</span>() + <span>2.0</span>;<br>    }<br>    <br>    <span>public</span> <span><span>function</span> <span>getDescription</span>(): <span>string</span> </span>{<br>        <span>return</span> <span>parent</span>::<span>getDescription</span>() . <span>" with milk"</span>;<br>    }<br>}<br><br><span><span>class</span> <span>SugarDecorator</span> <span>extends</span> <span>CoffeeDecorator</span> </span>{<br>    <span>public</span> <span><span>function</span> <span>getCost</span>(): <span>float</span> </span>{<br>        <span>return</span> <span>parent</span>::<span>getCost</span>() + <span>1.0</span>;<br>    }<br>    <br>    <span>public</span> <span><span>function</span> <span>getDescription</span>(): <span>string</span> </span>{<br>        <span>return</span> <span>parent</span>::<span>getDescription</span>() . <span>" with sugar"</span>;<br>    }<br>}<br><br><span><span>class</span> <span>WhippedCreamDecorator</span> <span>extends</span> <span>CoffeeDecorator</span> </span>{<br>    <span>public</span> <span><span>function</span> <span>getCost</span>(): <span>float</span> </span>{<br>        <span>return</span> <span>parent</span>::<span>getCost</span>() + <span>3.0</span>;<br>    }<br>    <br>    <span>public</span> <span><span>function</span> <span>getDescription</span>(): <span>string</span> </span>{<br>        <span>return</span> <span>parent</span>::<span>getDescription</span>() . <span>" with whipped cream"</span>;<br>    }<br>}</span>
```

## The Magic in Action

Now, creating any combination is simple and elegant:

```
<span id="2721" data-selectable-paragraph=""><span>$coffee</span> = <span>new</span> <span>SimpleCoffee</span>();<br><span>echo</span> <span>$coffee</span>-&gt;<span>getDescription</span>() . <span>": $"</span> . <span>$coffee</span>-&gt;<span>getCost</span>() . <span>"\n"</span>;<br><br><br><br><span>$coffeeWithMilk</span> = <span>new</span> <span>MilkDecorator</span>(<span>$coffee</span>);<br><span>echo</span> <span>$coffeeWithMilk</span>-&gt;<span>getDescription</span>() . <span>": $"</span> . <span>$coffeeWithMilk</span>-&gt;<span>getCost</span>() . <span>"\n"</span>;<br><br><br><br><span>$coffeeWithMilkAndSugar</span> = <span>new</span> <span>SugarDecorator</span>(<span>$coffeeWithMilk</span>);<br><span>echo</span> <span>$coffeeWithMilkAndSugar</span>-&gt;<span>getDescription</span>() . <span>": $"</span> . <span>$coffeeWithMilkAndSugar</span>-&gt;<span>getCost</span>() . <span>"\n"</span>;<br><br><br><br><span>$coffeeWithEverything</span> = <span>new</span> <span>WhippedCreamDecorator</span>(<span>$coffeeWithMilkAndSugar</span>);<br><span>echo</span> <span>$coffeeWithEverything</span>-&gt;<span>getDescription</span>() . <span>": $"</span> . <span>$coffeeWithEverything</span>-&gt;<span>getCost</span>() . <span>"\n"</span>;<br></span>
```

## Adding New Features? No Problem!

Want to add vanilla? Just create one decorator:

```
<span id="54be" data-selectable-paragraph=""><span><span>class</span> <span>VanillaDecorator</span> <span>extends</span> <span>CoffeeDecorator</span> </span>{<br>    <span>public</span> <span><span>function</span> <span>getCost</span>(): <span>float</span> </span>{<br>        <span>return</span> <span>parent</span>::<span>getCost</span>() + <span>2.5</span>;<br>    }<br>    <br>    <span>public</span> <span><span>function</span> <span>getDescription</span>(): <span>string</span> </span>{<br>        <span>return</span> <span>parent</span>::<span>getDescription</span>() . <span>" with vanilla"</span>;<br>    }<br>}</span>
```

## Real-World Example: Image Upload System

Let’s look at a practical example from web development:

```
<span id="3c95" data-selectable-paragraph=""><span><span>interface</span> <span>ImageUploaderInterface</span> </span>{<br>    <span>public</span> <span><span>function</span> <span>upload</span>(<span><span>string</span> <span>$path</span></span>): <span>void</span></span>;<br>    <span>public</span> <span><span>function</span> <span>getFilename</span>(): <span>string</span></span>;<br>}<br><br><span><span>class</span> <span>BaseImageUploader</span> <span>implements</span> <span>ImageUploaderInterface</span> </span>{<br>    <span>protected</span> <span>string</span> <span>$filename</span>;<br><br>    <span>public</span> <span><span>function</span> <span>__construct</span>(<span><span>string</span> <span>$filename</span></span>) </span>{<br>        <span>$this</span>-&gt;filename = <span>$filename</span>;<br>    }<br><br>    <span>public</span> <span><span>function</span> <span>upload</span>(<span><span>string</span> <span>$path</span></span>): <span>void</span> </span>{<br>        <span>echo</span> <span>"Uploading image to <span>{$path}</span>/<span>{$this-&gt;filename}</span>\n"</span>;<br>    }<br><br>    <span>public</span> <span><span>function</span> <span>getFilename</span>(): <span>string</span> </span>{<br>        <span>return</span> <span>$this</span>-&gt;filename;<br>    }<br>}<br><br><span>abstract</span> <span><span>class</span> <span>ImageUploaderDecorator</span> <span>implements</span> <span>ImageUploaderInterface</span> </span>{<br>    <span>protected</span> ImageUploaderInterface <span>$uploader</span>;<br><br>    <span>public</span> <span><span>function</span> <span>__construct</span>(<span>ImageUploaderInterface <span>$uploader</span></span>) </span>{<br>        <span>$this</span>-&gt;uploader = <span>$uploader</span>;<br>    }<br><br>    <span>public</span> <span><span>function</span> <span>upload</span>(<span><span>string</span> <span>$path</span></span>): <span>void</span> </span>{<br>        <span>$this</span>-&gt;uploader-&gt;<span>upload</span>(<span>$path</span>);<br>    }<br><br>    <span>public</span> <span><span>function</span> <span>getFilename</span>(): <span>string</span> </span>{<br>        <span>return</span> <span>$this</span>-&gt;uploader-&gt;<span>getFilename</span>();<br>    }<br>}<br><br><span><span>class</span> <span>ResizeImageDecorator</span> <span>extends</span> <span>ImageUploaderDecorator</span> </span>{<br>    <span>public</span> <span><span>function</span> <span>upload</span>(<span><span>string</span> <span>$path</span></span>): <span>void</span> </span>{<br>        <span>parent</span>::<span>upload</span>(<span>$path</span>);<br>        <span>$this</span>-&gt;<span>resize</span>();<br>    }<br><br>    <span>protected</span> <span><span>function</span> <span>resize</span>(): <span>void</span> </span>{<br>        <span>$filename</span> = <span>$this</span>-&gt;uploader-&gt;<span>getFilename</span>();<br>        <span>echo</span> <span>"Resizing image: <span>{$filename}</span>\n"</span>;<br>    }<br>}<br><br><span><span>class</span> <span>WatermarkImageDecorator</span> <span>extends</span> <span>ImageUploaderDecorator</span> </span>{<br>    <span>public</span> <span><span>function</span> <span>upload</span>(<span><span>string</span> <span>$path</span></span>): <span>void</span> </span>{<br>        <span>parent</span>::<span>upload</span>(<span>$path</span>);<br>        <span>$this</span>-&gt;<span>addWatermark</span>();<br>    }<br><br>    <span>protected</span> <span><span>function</span> <span>addWatermark</span>(): <span>void</span> </span>{<br>        <span>echo</span> <span>"Adding watermark to image...\n"</span>;<br>    }<br>}<br><br><span><span>class</span> <span>CompressionDecorator</span> <span>extends</span> <span>ImageUploaderDecorator</span> </span>{<br>    <span>public</span> <span><span>function</span> <span>upload</span>(<span><span>string</span> <span>$path</span></span>): <span>void</span> </span>{<br>        <span>parent</span>::<span>upload</span>(<span>$path</span>);<br>        <span>$this</span>-&gt;<span>compress</span>();<br>    }<br><br>    <span>protected</span> <span><span>function</span> <span>compress</span>(): <span>void</span> </span>{<br>        <span>echo</span> <span>"Compressing image...\n"</span>;<br>    }<br>}</span>
```

Usage is flexible and intuitive:

```
<span id="3a6f" data-selectable-paragraph=""><br><span>$resize</span> = <span>true</span>;<br><span>$watermark</span> = <span>true</span>;<br><br><br><span>$filename</span> = <span>'profile.jpg'</span>;<br><span>$uploader</span> = <span>new</span> <span>BaseImageUploader</span>(<span>$filename</span>);<br><br><span>if</span> (<span>$resize</span>) {<br>    <span>$uploader</span> = <span>new</span> <span>ResizeImageDecorator</span>(<span>$uploader</span>);<br>}<br><br><span>if</span> (<span>$watermark</span>) {<br>    <span>$uploader</span> = <span>new</span> <span>WatermarkImageDecorator</span>(<span>$uploader</span>);<br>}<br><br><span>$uploader</span>-&gt;<span>upload</span>(<span>'uploads'</span>);</span>
```

## When to Use the Decorator Pattern

The Decorator Pattern is perfect when you need to:

-   **Add responsibilities dynamically**: Features can be added or removed at runtime
-   **Avoid class explosion**: Instead of creating classes for every combination
-   **Follow Single Responsibility**: Each decorator has one specific purpose
-   **Maintain flexibility**: Easy to add new features without modifying existing code

## Common Use Cases

1.  **UI Components**: Adding borders, shadows, animations
2.  **File Operations**: Compression, encryption, validation
3.  **Text Processing**: Formatting, highlighting, transformation
4.  **HTTP Requests**: Authentication, logging, caching
5.  **Database Operations**: Logging, caching, validation

## Best Practices

1.  **Keep interfaces simple**: The component interface should be focused and minimal
2.  **Single responsibility**: Each decorator should add exactly one behavior
3.  **Order matters**: Consider the sequence of decorators carefully
4.  **Document behavior**: Make it clear what each decorator does
5.  **Use composition**: Favor decorator composition over inheritance

## Advantages vs. Disadvantages

## ✅ Advantages

-   More flexible than inheritance
-   Follows SOLID principles
-   Runtime behavior modification
-   Easy to extend and maintain
-   Avoids class explosion

## ❌ Disadvantages

-   Can result in many small classes
-   May increase code complexity
-   Can make debugging harder
-   Stack of decorators can be hard to understand

## Conclusion

The Decorator Pattern transforms code that would otherwise explode into dozens of classes into an elegant, maintainable solution. Instead of creating a class for every possible combination of features, you create small, focused decorators that can be combined in any way.

## Get Murilo Livorato’s stories in your inbox

Join Medium for free to get updates from this writer.

Remember: **composition over inheritance**. The Decorator Pattern exemplifies this principle beautifully, allowing you to build complex behaviors by combining simple, focused components.

Next time you find yourself creating multiple classes for feature combinations, take a step back and consider whether the Decorator Pattern might be the elegant solution you’re looking for.

## Thanks a lot for reading till end. Follow or contact me via:

Github:[https://github.com/murilolivorato](https://github.com/murilolivorato)  
LinkedIn: [https://www.linkedin.com/in/murilo-livorato-80985a4a/](https://www.linkedin.com/in/murilo-livorato-80985a4a/)
