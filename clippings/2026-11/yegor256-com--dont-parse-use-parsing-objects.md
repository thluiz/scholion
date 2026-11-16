---
url: "https://yegor256.com/2018/02/27/parsing-objects.html"
captured_at: "2026-11-16T02:41:51+00:00"
title: "Don't Parse, Use Parsing Objects"
domain: "yegor256-com"
---

The traditional way of integrating object-oriented back-end with an external system is through [data transfer objects](https://yegor256.com/2016/07/06/data-transfer-object.html), which are serialized into JSON before going out and deserialized when coming back. This way is as much popular as it is wrong. The serialization part should be replaced by [printers](https://yegor256.com/2016/04/05/printers-instead-of-getters.html), which I explained earlier. Here is my take on deserialization, which should be done by—guess what—objects.

![La science des rêves (2006) by Michel Gondry](https://yegor256.com/images/2018/02/la-science-des-reves.jpg)

La science des rêves (2006) by Michel Gondry

Say there is a back-end entry point, which is supposed to register a new book in the library, arriving in JSON:

```
{
  "title": "Object Thinking",
  "isbn: "0735619654",
  "author: "David West"
}
```

Also, there is an object of class `Library`, which expects an object of type `Book` to be given to its method `register()`:

```
class Library {
  public void register(Book book) {
    // Create a new record in the database
  }
}
```

Say also, type `Book` has a simple method `isbn()`:

```
interface Book {
  String isbn();
}
```

Now, here is the HTTP entry point (I’m using [Takes](https://yegor256.com/2015/03/22/takes-java-web-framework.html) and [Cactoos](https://yegor256.com/2017/06/22/object-oriented-input-output-in-cactoos.html)), which is accepting a POST [`multipart/form-data`](https://www.ietf.org/rfc/rfc2045.txt) request and registering the book in the library:

```
public class TkUpload implements Take {
  private final Library library;
  @Override
  public Response act(Request req) {
    String body = new RqPrint(
      new RqMtSmart(new RqMtBase(req)).single("book")
    ).printBody();
    JsonObject json = Json.createReader(
      new InputStreamOf(body)
    ).readObject();
    Book book = new BookDTO();
    book.setIsbn(json.getString("isbn"));
    library.register(book);
  }
}
```

What is wrong with this? Well, a few things.

First, it’s not reusable. If we were to need something similar in a different place, we would have to write this HTTP processing and JSON parsing again.

Second, error handling and [validation](https://yegor256.com/2018/05/29/object-validation.html) are not reusable either. If we add it to the method above, we will have to copy it everywhere. Of course, the DTO may encapsulate it, but that’s not what DTOs are usually for.

Third, the code above is rather procedural and has a lot of [temporal coupling](https://yegor256.com/2015/12/08/temporal-coupling-between-method-calls.html).

A better design would be to hide this parsing inside a new class `JsonBook`:

```
class JsonBook implements Book {
  private final String json;
  JsonBook(String body) {
    this.json = body;
  }
  @Override
  public String isbn() {
    return Json.createReader(
      new InputStreamOf(body)
    ).readObject().getString("isbn");
  }
}
```

Then, the RESTful entry point will look like this:

```
public class TkUpload implements Take {
  private final Library library;
  @Override
  public Response act(Request req) {
    library.register(
      new JsonBook(
        new RqPrint(
          new RqMtSmart(
            new RqMtBase(req)
          ).single("book")
        ).printBody()
      )
    );
  }
}
```

Isn’t that more elegant?

Here is an example from my projects: [`RqUser`](https://github.com/yegor256/jare/blob/0.11.2/src/main/java/io/jare/tk/RqUser.java) from [yegor256/jare](https://github.com/yegor256/jare/blob/0.11.2/src/main/java/io/jare/tk/RqUser.java).

As you can see from the examples above, sometimes we can’t use `implements` because some primitives in Java are not interfaces but `final` classes: `String` is a “perfect” example. That’s why I have to do this:

```
class RqUser implements Scalar<String> {
  @Override
  public String value() {
    // Parsing happens here and returns String
  }
}
```

But aside from that, these examples perfectly demonstrate the principle of “parsing objects” suggested above.
