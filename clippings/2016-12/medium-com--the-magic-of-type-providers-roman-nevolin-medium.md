---
url: "https://medium.com/@nevoroman/the-magic-of-type-providers-7f6825acd54#.5fmk7p56f"
captured_at: "2016-12-28T08:44:48-03:00"
title: "The magic of type providers – Roman Nevolin – Medium"
domain: "medium-com"
---

# The magic of type providers

Every programmer sometimes processing many different formats of data — it can be some JSON api response, SQL data or XML configuration. And it’s always boring, routine and problematic process. Is there at least one programmer who didn’t make typo in names or types of JSON fields?

Let’s do something with StackOverflow API response — it returns JSON For example, print titles of last questions. In C# it can look like this:

There’s not really much logic, but a lot of boiler-plate code for data models. Of course, we can use some language with dynamic type checking — Python, for example. And this code will be much shorter:

But now we have all problems of dynamic type system — for example, autocompletion can’t help us here. And, of course, it’s much easier to do some typo.

So we can’t say, that it really better.But maybe there is some way to combine advantages of both variants? Something like this:

Here we aren’t writing any data models, but have all advantages of static type checking — as you can see at screenshot below, IntelliSense give us full autocomplete, with correct names and types.

![1*O4hxW5qawX6lXrZn9b5EKg.png](medium-com--the-magic-of-type-providers-roman-nevolin-medium/ac6fa863a4573902ec3688cf55f3d78c.png)

![1*O4hxW5qawX6lXrZn9b5EKg.png](medium-com--the-magic-of-type-providers-roman-nevolin-medium/a343ddefb6fcdf2be784441fe4fd3e41.png)

You see? We haven’t implemented any data models, but… it works! How?

All this magic possible because of F # language mechanism, named “Type providers”. Every type providers — it’s some library, that provides functionality to work with certain type. By the way, we can easily replace one provider by the other. For example, if SO API will return us XML response, code will be almost unchanged:

How does this magic work? Let’s take a look at the use of JSON provider. When we creating it, we pass the example JSON URL. JsonProvider pulls it, determines its schema and create corresponding F# types. After that F# Compiler catch created types and we can use all the advantages of strong type checking, like autocomplete. Now it’s possible to map any JSON with appropriate schema to created types.

It can also decide some other problems. For example, if API will be changed, your code will stop stop working anyway. But if you are using type providers, you’ll know about it on compilation stage — because type provider will load new data scheme.

So, type providers are awesome. I’ll show you, how much it can be awesome with some other examples.

### **Not only for reading**

It’s obvious that sometimes we need more than reading data. A good example is interaction with SQL database — we need some other functions here, like updating or deleting records. It would not be too good if type providers can’t do simple CRUD operations… but, of course, type providers can.

SQL Provider can easily do all CRUD operations — it is easy to compare with ORM. To show how it works let’s solve some simple problem. For example fill “IsHoliday” field of Sales table, according to “Date” field using SQL Provider

It really looks like ORM, isn’t it? But we don’t create any data models.

### **Not only for simple data types**

It isn’t really hard to parse something like JSON, but what about other data sources, like HTML? Anyone who has ever parsed HTML, know — this is unusually dull and dreary task. It’s so easy to make a stupid mistake in selector!  
 Fortunately, we can use type providers to avoid HTML parsing problems. There is HTML provider which allows you to use all advantages of strong type checking when you working with HTML. Let’s use it for some simple real-life task. Recently I had to get a list of heads of government of members of the United Nations. Let’s try to parse it from Wikipedia.

I didn’t even look at HTML-code of Wiki page, HTML provider gave me all the necessary information. And the code has turned out much more readable than if we had used for this purpose more common tools like HTML Agility Pack.

### **Not only for data**

In fact, type providers functionality are not limited by data manipulations. There are other, much more interesting cases.  
 For instance, cross-language interoperability. As you know, it can be challenging task with a lot of pitfalls. But we can do it much easier through type providers.  
 R provider shows this perfectly. As you can guess, it makes possible to use R capabilities from the F#. Let’s take a look at usage example from R Provider documentation

As you can see, this type provider allows you to use functions of another language as some of the NuGet libraries. By the way, this example shows you how several type providers can be used together.

### **Conclusion**

So, type providers can help you to write very efficient and reliable code. Of course, I haven’t shown all of the possible type provider usages — they are really limitless. There is type providers to interact with JavaScript, Swagger and much more. And nothing prevents you from creating you own type provider — excellent recommendations on this subject can be found in [Sergey Tikhon’s blog](https://sergeytihon.wordpress.com/2016/07/11/f-type-providers-development-tips-not-tricks/).
