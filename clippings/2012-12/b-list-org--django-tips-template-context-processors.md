---
url: "http://www.b-list.org/weblog/2006/jun/14/django-tips-template-context-processors/"
captured_at: "2012-12-20T09:02:59-03:00"
title: "Django tips: Template context processors"
domain: "b-list-org"
---

# **D**jango tips: Template context processors

Published [June 14, 2006](http://www.b-list.org/weblog/2006/jun/14/) **.** Filed under:
[Django](http://www.b-list.org/weblog/categories/django/) **.**

Last time around we looked at [how to write an effective template tag](http://www.b-list.org/weblog/2006/06/07/django-tips-write-better-template-tags) , with the focus on writing a flexible template tag that would make it easy to pull in various types of recent content in any page; I use a tag similar to the one in that entry to pull out the recent entries, links and comments in the footer of every page on this site**.**

For situations where you want to get content out of your database, a template tag is typically the best way to go, but consider a related situation: what happens when you want a particular variable — not a content object — to be available in the context of every template**?**

You *could* write a template tag to populate that variable, and it’d be extremely easy to do with a convenience function Django provides: the [simple\_tag](http://www.djangoproject.com/documentation/templates_python/#shortcut-for-simple-tags) decorator, which lets you omit a lot of the boilerplate of writing a template tag when all you want is to spit out some value into the template**.**

A recent example that came up on the django-users mailing list was a template tag to retrieve the base URL for your media (typically you want to store “media” like images, stylesheets and JavaScript in a particular location on your server, or possibly even have a separate server for them if you’re using Apache and mod\_python — incurring the overhead of mod\_python on a request which will just serve up a file from disk wastes resources)**.** Django lets you specify where your media files come from via the [MEDIA\_URL](http://www.djangoproject.com/documentation/settings/#media-url) setting**.**

So you’d write a simple tag which imports your settings file and returns the value of the `MEDIA_URL` setting into the template context; you could maybe call it `get_media_url`**.** But having to call that in *every single template* will probably get a bit cumbersome and feels like it violates the DRY principle; wouldn’t it be nice if Django provided an easier way to do this**?**

## Enter `RequestContext` and context processors

As it turns out, Django provides an extremely easy way to do this**.** Every time you render a template, you give it a “context”; this is a dictionary-like object whose keys are variable names and whose values are the values of the variables**.** When you render a template with a given context, every key in the context dictionary becomes a variable in the template that you can access and use**.**

The base class for Django template contexts is `django.template.Context`, and typically you use it somewhat like this:

```
from django.template import Context
# view code here...    
c = Context({'some_var': 'some_value', 'some_other_var': 'some_other_value'})
```

But because `Context` is a Python class, you can subclass it and do all sorts of nifty tricks with it**.** And Django provides a particularly useful pre-defined `Context` subclass: `django.template.RequestContext`**.** Old hands will recognize this as a variation of `DjangoContext`, a `Context` subclass present in older releases of Django which would automatically add useful variables like the logged-in user who requested the page**.** But `RequestContext` is `DjangoContext` on steroids**.**

`RequestContext` looks in your settings file for a setting called [TEMPLATE\_CONTEXT\_PROCESSORS](http://www.djangoproject.com/documentation/settings/#template-context-processors), which should be a tuple of callable objects, each of which should return a dictionary; `RequestContext` will loop over each one of them, call it, and add the key/value pairs from its returned dictionary to the template context as variables**.** Django includes a few built-in context processors (found in `django.core.context_processors`) which can add:

- The user who requested the page (`django.core.context_processors.auth`)
- A test for the `DEBUG` setting and a list of SQL executed in the request (`django.core.context_processors.debug`)
- Information about the language settings used for any translations performed by the internationalization system (`django.core.context_processors.i18n`)
- The full `HttpRequest` object for the current request (`django.core.context_processors.request`)

Using `RequestContext` and a context processor *automatically* adds these variables in every template, which avoids the repetitiveness of having to call a template tag in each template just to add some variables**.**

## Let’s write a context processor

And, even better, it’s absurdly simple**.** Let’s use the example above — getting the `MEDIA_URL` setting — and see how we can add it the context of our templates by using `RequestContext`**.**

First we write the context processor**.** It’s an extremely simple function:

```
def media_url(request):
    from django.conf import settings
    return {'media_url': settings.MEDIA_URL}
```

Notice that it takes the current request’s `HttpRequest` instance as an argument; in this example we’re not using that, but if you want to return different things based on attributes of the request it’ll be there for you**.**

This function can live anywhere in your application’s code, but for sake of consistency and being able to remember where it is, I’d recommend creating a new file in your application’s directory called “context\_processors**.**py” and putting the function there**.**

Then we open up our settings file and add this (keep in mind that Django enables the `auth`, `debug` and `i18n` context processors by default, and editing the `TEMPLATE_CONTEXT_PROCESSORS` setting will override that, so if you want to keep those you’ll need to add them back manually):

```
TEMPLATE_CONTEXT_PROCESSORS = ('myapp.context_processors.media_url',)
```

Note the trailing comma there; even if you’re only putting one item into a Python tuple it still needs a comma**.**

Finally, we change our view code to use `RequestContext` instead of the base `Context` class**.** In most cases, this is as simple as changing one line at the top of the view file; instead of

```
from django.template import Context
```

we do this:

```
from django.template import RequestContext
```

Now when we instantiate a context, we can do it by `RequestContext(request, context_dictionary)` instead of `Context(context_dictionary)`**.**

If you’re using the `render_to_response` shortcut, just pass it as the `context_instance` keyword argument to `render_to_response`, like so:

```
return render_to_response("my_app/my_template.html", {'some_var': 'foo'},
                           context_instance=RequestContext(request))
```

If you’re using a [generic view](http://www.djangoproject.com/documentation/generic_views/) , you don’t have to do anything except define the `TEMPLATE_CONTEXT_PROCESSORS` setting; generic views use `RequestContext` by default**.**

And you’re done; now you’ll get your `media_url` variable available in all of your templates without having to repetitively call a template tag**.**
