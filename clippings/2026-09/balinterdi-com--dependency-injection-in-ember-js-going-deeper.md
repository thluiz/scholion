---
url: "http://balinterdi.com/2014/05/16/dependency-injection-in-ember-dot-js-going-deeper.html?utm_source=Ember+Weekly&utm_campaign=92cbf50a88-Ember_Weekly_Issue_58&utm_medium=email&utm_term=0_e96229d21d-92cbf50a88-99490097"
captured_at: "2026-09-27T00:30:58+01:00"
title: "Dependency injection in Ember.js - Going deeper"
domain: "balinterdi-com"
---

*   [Home](http://balinterdi.com/)
*   [Blog](http://balinterdi.com/blog)
*   [Services](http://balinterdi.com/services/)
*   [Book](http://balinterdi.com/rock-and-roll-with-emberjs/)

16 May 2014

In a previous post [I introduced the basic elements of Dependency Injection in Ember](http://balinterdi.com/blog/dependency-injection-in-ember-dot-js) and showed how to set up a dependency on the objects it is needed on. I also mentioned the framework itself uses this same mechanism to establish its dependencies.

In this post, I'll expand on this latter. I'll point at where these dependencies are set up which gives me the possibility to introduce the options of the basic parts, `register` and `inject`.

I'll also share a couple of tricks to prevent using the abominable `this.__container__` and finish by showing how these pieces fit together in the main method of the container, `container.lookup`.

### How does Ember do it?

When an Ember app is created, the first thing it does is creating a container it uses internally:

([link to soure code](https://github.com/emberjs/ember.js/blob/v1.6.0-beta.4/packages_es6/ember-application/lib/system/application.js#L263))

(Note: Here is where `App.__container__` gets set and thus you, as an application developer has access to the underlying container. Notice the double underscores, though. It tells you that you should not ever use that in "real" apps. There are officially supported ways, public API methods to achieve whatever you strive to achieve the forbidden way. It is sometimes enough [to ask on Twitter.](https://twitter.com/mixonic/status/461595081607503872))

Let's see how the container is built up (as usual, I cut out the parts that are not relevant to the current subject):

([link to source code](https://github.com/emberjs/ember.js/blob/v1.6.0-beta.4/packages_es6/ember-application/lib/system/application.js#L826))

The faithful reader knows from the [first part in the DI series](http://balinterdi.com/blog/dependency-injection-in-ember-dot-js) that the above makes it so that e.g `this.namespace` points to the application in all controllers or that `this.router` refers to the router in all routes.

Let's now turn out attention to the first definition block to learn new things.

### optionsForType

`optionsForType` is a comfortable way to define options that should be used when looking up any instance of a particular type from the container.

It can be seen above that components and views are defined as non-singletons which mean that any time a component or view is looked up on the container, a new instance is created and returned.

I got me some code to prove it:

If you then write a template for the index route that just displays the `equal` property you'll see that its value is false, thus a new object is in fact instantiated each time.

Here is [a link to the jsbin](http://emberjs.jsbin.com/zefuk/2/edit) if you would like to see it.

If you replace `{ singleton: false }` with `{ singleton: true }` the equal property is going to be true, the model object is going to be a true singleton.

#### Singletons are the default

As Ember core team meber [Stefan Penner points out](http://balinterdi.com/blog/dependency-injection-in-ember-dot-js#comment-1386980817), the `{ singleton: true }` option is the default, so there is no need to explicitly state it.

As a consequence, `container.register('store:main', Store, { singleton: true })` is exactly the same as `application.register('store', Store)`.

#### Objects that come from the container can access it

I learned this from [Matthew Beale](http://madhatted.com/), a prolific Ember contributor and presenter. It's well worth your time [to watch his presentation](https://www.youtube.com/watch?v=6FlWyOoo6hQ) on "Containers and Dependency Injection" he gave at an Ember NYC meetup.

Amongst other useful stuff, he also reveals that all objects that come from the container have access to it via a `container` property on them.

That allowed me to write `this.container.lookup` in the route above since routes are created by the container, too.

This also does away with the need to use the private `__container__` in most cases.

### To instantiate or not to instantiate

Above, in the code for `buildContainer` you can see another option, `instantiate`, which is false for templates and helpers. To save you from scrolling all the way up, here are the relevant lines:

This option permits the registration of entities (yeah, stuff) that do not need to be instantiated (or cannot be). Templates and helpers fit the bill since they are functions and thus cannot be instantiated.

### container.lookup

The lookup method in the container is a great summary for all the things discussed here.

First, if a singleton is needed and the object has already been looked up, we just return the object saved in the cache. (see 1 above)

Next, we instantiate an object for the fullName (e.g 'controller:artists' or 'route:index'). The instantiate method takes care of just returning the value if the `instantiate` option is set to false. (see 2 above)

If the instantiation was successful (the factory was found) and a singletion was demanded, we set this value in the cache so that we can return it the next time it is looked up. (see 3 above)

Finally, we return what was looked up. (see 4 above)

`container.lookup` just calls the above function after verifying the fullName has the right syntax, that is it has a type and a name part joined together by a `:`.

And that's where everything comes together.

* * *
