---
url: "https://medium.com/@cjbell_/sharing-methods-between-phoenix-controllers-358ab6d36e22#.53ajwxyfo"
captured_at: "2016-01-07T16:47:27-03:00"
title: "Sharing Functions Between Phoenix Controllers — Medium"
domain: "medium-com"
---

# Sharing Functions Between Phoenix Controllers

When building applications in Phoenix we often need to share some functions between controllers in order to DRY-up our code.

Lets say we have some helpers that we’d like to be able to use in our controllers:

I usually put these into a *helpers.ex* file in my *web/controllers* directory.

We *could* write an import statement at the top of each of the controllers we want to have this functionality:

This approach is fine but what if we wanted to do this across *all* of the controllers in our application withoutduplicating this line each time?

The answer lies in the *web/web.ex* filethat contains our definitions for the controllers, views, and models in our application. These are just functions that *use*, *alias* or *import* some useful modules and functions for you.

*(If you’re unfamiliar with use, import, and alias you can read more about the differences between them* [*here*](http://elixir-lang.org/getting-started/alias-require-and-import.html)*).*

Each time we create a new controller in Phoenix you actually call the *controller/0* method in this file explicitly with *use MyApp.Web, :controller* (usually the first line under the controllers definition). The use call here will call the *MyApp.Web* modules *\_\_using\_\_* macro, passing the atom *:controller* as the first argument.

The *\_\_using\_\_* macro calls *apply/3* on the Web module with the passed in atom as the function name and an empty list. Given the atom :*controller,* this then calls the *controller/0* method and expands the quoted code inside of your controller — just like manually defining each one of those *use*, *alias,* and *import* statements yourself in the controller.

Armed with this knowledge, we can now share our helper module between all of our controllers by adding another *import* line to *controller/0* in the *web/web.ex* file (notice the import statement on line 13 that corresponds to our Helper module):

Et voila, we are done 🎉!

As an added bonus this technique can be used to bring other external functionality to other parts of the application (views, channels, router, models).
