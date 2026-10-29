---
url: "http://vaidehijoshi.github.io/blog/2015/06/23/to-serialize-or-not-to-serialize-activemodel-serializers"
captured_at: "2015-06-26T12:34:33-03:00"
title: "To Serialize or Not to Serialize: ActiveModel Serializers - Words and Code"
domain: "vaidehijoshi-github-io"
---

# To Serialize or Not to Serialize: ActiveModel Serializers

[#technicaltuesdays](http://vaidehijoshi.github.io/blog/categories/number-technicaltuesdays/), [rails](http://vaidehijoshi.github.io/blog/categories/rails/), [ruby](http://vaidehijoshi.github.io/blog/categories/ruby/)

Lesson number one when it comes to developing for the web: everything is just data. When you send something to the server in a request, or when you get something back from the server as a response, all you’re really dealing with is data. Simple enough to remember, right? Wrong. Because data can be complicated. Especially when you consider the fact that it has to be passed back and forth in very specific ways. And if you don’t format your data correctly, your computer is going to be very, very mad at you (or probably just throw a really unhelpful error message).

I encountered the complications of data formatting the hard way, while trying to pass data between two parts of my application. I wanted to send some data to update a Ruby object in my Postgres database on the server-side, and then I wanted the Rails side to send back an updated response. As if that wasn’t enough, I then needed the Ember front end to grab the updated data and immediately render it to the user on the client-side. Data formatting can already be complex when you have only one framework or language; throw in another framework and language, and, well…you might feel like you’re having a little bit of a meltdown.

But fear not! Because here’s one awesome thing about data: once you understand the way that it’s structured, it’s pretty simple to use. And when it comes to working on a more intricate Rails + JavaScript application (like the one I was building recently), there’s one kind of data manipulation you’re probably going to have to do at some point or another: data serialization. When working with a JavaScript front end, you’ll probably have to serialize your data into a **JSON format**, which is short for *JavaScript Object Notation*. Thankfully, there’s a handy gem that makes this so easy that you’ll never again question whether or not to serialize your data.

## Why Serialize?

The time has finally come: it’s time for us to spiff up our Bookstore application with some JavaScript. (I know, I know, it sounds horrible – but it’ll be so good for our users, I promise). But let’s start off simple and keep working with the Rails API we’ve been building out.

Let’s pretend for a second that we’ve already implemented authentication in our application, which means we have access to the `current_user` who is logged in at the highest controller level of our application: the `ApplicationController`. In our `UsersController`, we want an `index` action that will be invoked when the `current_user` logs into their account page. On that page, we’ll want to show the user’s “wish lists”, or the list of books that they want to read. Each `WishList` object belongs to a `User` and has many `Books`, and a `Book` can belong to a `WishList`. Right now in our controller, we are rendering all the `WishLists` that are associated with the `current_user` as JSON:

|  |  |
| --- | --- |
|  | ``` class UsersController  ApplicationController    index     @wish_lists  current_userwish_lists     render  @wish_lists ``` |

Cool, we have our `WishLists` already rendered as JSON. Why serialize anything in that case? I’m sure our JSON is structured perfectly well, and that we can convert our Ruby object data into Ember models seamlessly!

|  |  |
| --- | --- |
|  | ```       "user"               "username" "Vaidehi"       "name""Favorite Shakespeare Plays To Re-Read"       "created_at""2015-06-23T21:07:30.108Z"       "updated_at""2015-06-23T21:07:30.108Z"       "books"                   "title" "A Midsummer Night's Dream"                   "author" "William Shakespeare"                   "title" "The Tempest"                   "author" "William Shakespeare"                   "title" "Much Ado About Nothing"                   "author" "William Shakespeare" ``` |

Oh my. That is *definitely* not how we want our JSON to look!

For one thing, if we give this JSON to Ember, it won’t know how to turn it into an Ember model. But there are also some other issues with exactly how this data is structured.

For now, we don’t need to render anything to our user about when the created or updated their list, so that’s some superfluous data that we shouldn’t be requesting from the server.

We also don’t want to render anything about our actual `User` object – we probably just want to include the `user_id`, and nothing else. And because we can load the correct `Book` models via Ember itself, let’s not bother with requesting all the details of every `Book` in our `WishList`. Instead, let’s just get an array of associated `book_ids`, and then have Ember render the appropriate ones for us from its data store.

So, to serialize or not to serialize? That is the question. And I think you and I both know the answer.

## ActiveModel Serializers

Before we can get our serializing on, we’ll need to add our new favorite gem to our `Gemfile`:

|  |  |
| --- | --- |
|  | ```  'active_model_serializers' ``` |

and then run the `bundle` command.

Now, we’ll want to actually create our serializer, which will work with Rails’ ActiveModel functionality to serialize your persisted Ruby objects into the exact JSON format that we’ll specify. Luckily, we can just generate our serializer instead of creating those files:

|  |  |
| --- | --- |
|  | ``` rails  serializer wishList ``` |

This will create a `serializers` directory inside of our top-level `/app` directory since this is the first serializer we’ve generated. And it’ll add both an empty `application_serializer` and a `wish_list_serializer.rb` file inside of that new directory, which looks like this:

|  |  |
| --- | --- |
|  | ``` class WishListSerializer  ApplicationSerializer   attributes  :name   has_many :books   belongs_to :user ``` |

The attributes that we’ve listed (`id` and `name`) are the ones that are *whitelisted* to be serialized. This basically means that these are the attributes we are allowing the `active_model_serializers` gem to serialize and make into JSON. The serializer we generated through Rails also recognized the associations that we set up; it created the `has_many` and `belongs_to` relationships that we setup inside of our `Book`, `User`, and `WishList` Rails models.

Cool, but how can we check what our data structure looks like? Well, we can start our server (`rails server`) and then head over to where our index route lives (`http://localhost:3000/wish_list`). Our JSON response will be rendered through our `index` action in our `WishListsController`:

|  |  |
| --- | --- |
|  | ```   "wish_lists"               "name""Favorite Shakespeare Plays To Re-Read"               "user"                       "username" "Vaidehi"               "books"                           "title" "A Midsummer Night's Dream"                           "author" "William Shakespeare"                           "title" "The Tempest"                           "author" "William Shakespeare"                           "title" "Much Ado About Nothing"                           "author" "William Shakespeare" ``` |

Well, our data looks a *little* bit better. For one thing, our whitelisted attributes and associations have been put under a `wish_lists` key, which will have an array of `WishList` objects for the `current_user`, just as we wrote out in our `WishListsController`.

Although it’s great that this gem generated all this for us, and for free, we already know that we’re going to have to tweak this a bit. First, let’s get rid of that `belongs_to :user` line, and instead just render a `user_id` attribute:

|  |  |
| --- | --- |
|  | ``` class WishListSerializer  ApplicationSerializer   attributes  :name :user_id   has_many :books ``` |

Because we’ve set up the associations in both models, the `active_model_serializer` will look directly for an `id` attribute on a `User` association, and add that as a key in our JSON object, rather than creating a `user` key that points to an entire JSON `User` object. What does our JSON object look like now?

|  |  |
| --- | --- |
|  | ```   "wish_lists"               "name""Favorite Shakespeare Plays To Re-Read"               "user_id"               "books"                           "title" "A Midsummer Night's Dream"                           "author" "William Shakespeare"                           "title" "The Tempest"                           "author" "William Shakespeare"                           "title" "Much Ado About Nothing"                           "author" "William Shakespeare" ``` |

Okay, another step in the right direction. But, what about those annoying `Book` objects – how do we turn those objects into just an array of `book_ids`?

The answer is…through another serializer, of course! And also some snazzy customization.

## Customizing Your Serializer

Before we can go about spicing up the JSON response generated by our `WishList Serializer`, we are going to have to generate a new serializer for our `Book` objects. Thank goodness we already know how to do all that:

|  |  |
| --- | --- |
|  | ``` rails  serializer ``` |

which will generate a `book_serializer.rb` file like this:

|  |  |
| --- | --- |
|  | ``` class BookSerializer  ApplicationSerializer   attributes  :title :author   belongs_to :wish_list ``` |

Step one, successfully accomplished! Now, time to bedazzle our serializer. Let’s say that the front end of our application doesn’t need all that information – instead, it needs just an array of `book_ids`. We can just edit our serializer so that we’re only using the information that we want to use:

|  |  |
| --- | --- |
|  | ``` class BookSerializer  ApplicationSerializer   attributes ``` |

Now comes step two: telling our `WishList Serializer` to refer to our `BookSerializer`, and use *that* to serialize each book associated with a wish list. If only there was an easy way to do that…

|  |  |
| --- | --- |
|  | ``` class WishListSerializer  ApplicationSerializer   attributes  :name :user_id :books   private    books       BookSerializerobjectbooksattributes ``` |

Oh, interesting! We’ve just created our *very own* attribute on the `WishListSerializer`. And what does that method (which is private, because we don’t wany any other part of our application to call it) do, exactly? Well, it creates a new instance of our `BookSerializer`, and runs that serializer for each `Book` object, returning the attributes that we told it to serializer.

What’s really awesome about this is that if we suddenly decide that we now want not just an array of `ids`, but also the `title` of each `Book` object, we can just add that attribute into our `BookSerializer` by modifying the line to `attributes :id, :title`, and *tada*! We have an array of `Book` objects that have both an `id` *and* a `title`. So easy, right?!

The super cool thing about implementing serializers is that our `UsersController` hasn’t changed at all in this process:

|  |  |
| --- | --- |
|  | ``` class UsersController  ApplicationController    index     @wish_lists  current_userwish_lists     render  @wish_lists ``` |

All that’s happening now is that Rails is looking for a serializer for our `WishList` objects on the `current_user`, and if it finds one (which it will, since we made it!), it uses that to serialize the appropriate data and render it into a JSON format.

Serializers are pretty fantastic because they’re easy to generate, customize, and use. In fact, we could even create multiple serializer for the same *type* of object. We could have a `BookDetails Serializer`, which might return a ton of information about a book, rather than just its `id` and `title`. All we’d have to do to use it is specify the serializer within our controller action:

|  |  |
| --- | --- |
|  | ``` render  @books each_serializer BookDetailsSerializer ``` |

Pretty amazing stuff, right? This will make integrating our JavaScript front end with our Rails API so much easier. We can serialize all of the things! And then we should probably teach this doggy how to serialize things, too. He’s probably confused because he hasn’t read this blog post yet:

## tl;dr?

- The `active_model_serializers` gem provides a ton of functionality for structuring a JSON response from your Rails API. Read about all the methods it provides in its [great documenation](https://github.com/rails-api/active_model_serializers).
- Still curious about serializers? Check out [this cool post](https://robots.thoughtbot.com/better-serialization-less-as-json) and [this one](https://blog.engineyard.com/2015/active-model-serializers), too!
- Serializers are also great for caching. To learn more about why they matter, read this [more advanced](https://robots.thoughtbot.com/fast-json-apis-in-rails-with-key-based-caches-and) blog post!
