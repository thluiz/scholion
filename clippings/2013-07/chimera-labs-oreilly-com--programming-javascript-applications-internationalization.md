---
url: "http://chimera.labs.oreilly.com/books/1234000000262/ch06.html#internationalization"
captured_at: "2013-07-13T11:11:02-03:00"
title: "Programming JavaScript Applications — Internationalization (chapter 6)"
domain: "chimera-labs-oreilly-com"
---

|  |
| --- |
| Programming JavaScript Applications**SourceURL:** <http://chimera.labs.oreilly.com/books/1234000000262/ch06.html#internationalization> |

## nternationalization

Internationalization or localization is the process of converting text strings, numbers, dates, and currency into localized languages and representations. When you build a web application which grows to or near the saturation point in one country or culture, the easiest way to grow your user base is to expand to other cultures. One of the biggest hurdles to cross is obviously the translation of your app, but before you can even start down that road, you need to have some mechanisms in place to make that possible.

So when is the right time to get started? *Right now.* The biggest obstacle to translation is that you must plan for it, or budget a whole lot more time and energy to painstakingly go through the app, find all the strings that need translating, and then add support for it after the fact. By far, the easiest way to support internationalization is to plan for it up front, as soon as you start building templates. Any string that gets displayed to the user should be run through a translation function, first.

Instead of rolling your own translation solution, I recommend that you find a good library to handle it for you. Some good ones include [Moment.js](http://momentjs.com/) for dates, and [i18next](http://i18next.com/) for strings.

Microsoft produced a very thorough solution that works with strings, numbers, currency, percentages, and dates. It's called [Globalize](https://github.com/jquery/globalize), and it was generously donated to the jQuery project, but it has since been made stand-alone and converted to work with AMD and node-style modules. You don't need to use jQuery to use Globalize.

One advantage of Globalize is that it uses a fairly comprehensive database of locale information that is hard to match in JavaScript. The only comparable solution that I'm aware of is the [Unicode Common Locale Data Repository (CLDR)](http://cldr.unicode.org/). CLDR is used by many of the top software development companies, including Apple, Google, IBM, and Adobe. Anybody can contribute to it. You could think of it is the Wikipedia of globalization data. There has even been talk of using CLDR data to generate culture files for Globalize, and that may become available in a future version.

If you don't want to wait, and you don't mind Twitter's choice of which locales to support, you may be able to use [twitter-cldr-js](https://github.com/twitter/twitter-cldr-js). Twitter's CLDR package has a dependency on Ruby, so it may need to be shoe-horned into your Node project if you decide to go that route.

For now, I recommend Globalize.

  

|  |
| --- |
| Programming JavaScript Applications**SourceURL:** <http://chimera.labs.oreilly.com/books/1234000000262/ch06.html#getting-started-with-node-and-express> |

##### Let it Crash

Processes crash. Like all things, your server's runtime will
expire. Don't sweat it. Log the error, shut down the server,
and launch a new instance. You can use Node's cluster module,
forever (a Node module available on npm), or a wide range of
other server monitor utilities to detect crashes and repair
the service in order to keep things running smoothly, even in
the face of unexpected exceptions.

  

|  |
| --- |
| Programming JavaScript Applications**SourceURL:** <http://chimera.labs.oreilly.com/books/1234000000262/ch06.html> |

*Separation of concerns* is the idea that each module or layer in an application should only be responsible for one thing, and should not contain code that deals with other things. Separating concerns reduces code complexity by breaking a large application down into many smaller units of encapsulated functionality.

It's easy to confuse separation of concerns with employing modules for the construction of your application, but separation of concerns also implies the layering of functionality in your application. For example, n-tier architecture and MVC architectures are the result of separating concerns across the entire application, rather than at the individual module level. The goal of MVC and related patterns is to separate data management and presentation.

Separation of concerns can be expressed as functions, modules, controls, widgets, layers, tiers, services, and so on. The various units of concern vary from one app to the next, and each different app may use a different combination. Functions and modules have already been discussed.

A *control* is a reusable GUI input that enables user interaction with your application. For example, combo boxes, calendar inputs, sliders, buttons, switches, and knobs are all controls.

A *widget* is a small application which is intended to be embedded in other applications. For example, [WordPress](http://wordpress.org/) allows developers to offer embeddable units of functionality to blog owners through its plugin ecosystem. There are many widgets to manage calendars, comments, maps, and all sorts of services from third party providers.

The word widget is historically used to mean the same thing as controls. To avoid confusion, this book will always refer to interactive form inputs as controls (or inputs), and widgets will always refer to embeddable mini applications.

*Layers* are logical groupings of functionality. For example, a data layer might encapsulate functionality related to data and state, while a presentation layer handles display concerns, such as rendering to the DOM and binding UI behaviors.

*Tiers* are the runtime environments that layers get deployed to. A runtime environment usually consists of at least one physical computer, an operating system, the runtime engine (e.g., Node, Java, or Ruby) and any configuration needed to express how the application should interact with its environment.

It's possible to run multiple layers on the same tier, but tiers should be kept independent enough that they can easily be deployed to separate machines, or even separate data centers. For large scale applications, it's usually also necessary that tiers can scale horizontally, meaning that as demand increases, you can add machines to a tier in order to improve its capacity to meet that demand.

  

|  |
| --- |
| Programming JavaScript Applications**SourceURL:** <http://chimera.labs.oreilly.com/books/1234000000262/ch06.html> |

A *control* is a reusable GUI input that enables user interaction with your application. For example, combo boxes, calendar inputs, sliders, buttons, switches, and knobs are all controls.

A *widget* is a small application which is intended to be embedded in other applications. For example, [WordPress](http://wordpress.org/) allows developers to offer embeddable units of functionality to blog owners through its plugin ecosystem. There are many widgets to manage calendars, comments, maps, and all sorts of services from third party providers.

  

|  |
| --- |
| Programming JavaScript Applications**SourceURL:** <http://chimera.labs.oreilly.com/books/1234000000262/ch05.html#principles_of_modularity> |

## Principles of Modularity

You can think of modules as small, independent applications that are fully functional and fully testable in their own right. Keep them as small and simple as possible to do the job that they are designed to do.

Modules should be:

- Specialized: Each module should have a very specific function. The module's parts should be integral to solving the single problem that the module exists to solve. The public API should be simple and clean.
- Independent: Modules should know as little as possible about other modules. Instead of calling other modules directly, they should communicate between mediators, such as a central event handling system or command object.
- Decomposable: It should be fairly simple to test and use modules in isolation from other modules. It's common to compare them to components in an entertainment system. You could have a disc player, radio receiver, TV, amplifier and speakers, all of which can operate independently of each other. If you remove the disc player, the rest of the components continue to function properly.
- Recomposable: It should be possible to fit various modules together in different ways, in order to build a different version of the same software, or an entirely different application.
- Substitutable: It should be possible to completely substitute one module with another, as long is it supplies the same interface. The rest of the application should not be adversely impacted by the change. The substitute module doesn't have to perform the same function. For example, you might want to substitute a data module that uses REST endpoints as its data source with one that uses a local storage database as its data source.

  

|  |
| --- |
| Programming JavaScript Applications**SourceURL:** <http://chimera.labs.oreilly.com/books/1234000000262/ch03.html#closures> |

Some principles to keep in mind when you design your methods. This bears repeating:

- Keep It Simple, Stupid (KISS)
- Do One Thing, and do it well (DOT)
- Don't Repeat Yourself (DRY)
