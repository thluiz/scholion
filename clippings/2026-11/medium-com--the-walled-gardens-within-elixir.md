---
url: "https://medium.com/@MarcelOttoDE/the-walled-gardens-within-elixir-d0507a568015"
captured_at: "2026-11-16T06:09:31+00:00"
title: "The Walled Gardens within Elixir. Elixir is great, in this article… | by Marcel Otto | Medium"
domain: "medium-com"
---

Photo by Malcolm Lightbody on Unsplash
The Walled Gardens within Elixir
Marcel Otto
14 min read
·
May 12, 2020

Elixir is great. In this article, however, I want to talk about the feature I’m missing most, a wall I’ve hit several times since I’m working with Elixir. After describing the problem in general I will present some solutions to it in the context of some real-world occurrences of the problem in the RDF.ex projects, where alone I’ve hit this wall multiple times. Along the way, I’ll present the new behaviour _reflection library I’ve published, which implements one approach for solving the problem.

This article is not about RDF.ex, but since all examples will be in the context of this or related projects, I will just say a few words about what it is. RDF.ex is an Elixir implementation of the W3C RDF specification which defines a very simple graph data model. The RDF specification itself is quite foundational as there are a plethora of other specifications on top of it. Some of them are implemented in RDF.ex directly, for example some basic serialization formats for RDF graphs, others are implemented in separate Hex packages. The most important one is SPARQL.ex, an Elixir implementation of parts of the W3C specs on SPARQL, the query language for RDF graphs. SPARQL.ex also contains a query engine executing SPARQL queries on RDF.ex graphs.

With these basics out of the way let’s look at the problem in general and define a generic example we can come back to throughout the article.

The problem

The problem is the lack of a possibility to reflect all modules implementing a Behaviour. Let’s say we have the following Behaviour for an adapter or plugin facility in a library so that it can be extended with custom implementations:

We have a function for some operation and a function for an identifier of the adapter implementation which we want to use for some kind of registry with which we want to access the modules. For the implementation of this registry now, we need a function to get all the modules implementing our behaviour:

This lack of a __behaviour_impls__/1 function is the problem. When I first encountered it I was a bit surprised and thought I must have missed something, especially with extensibility being one of Elixir’s initial design goals. But having seen other people dealing with the same problem, this has become the most missing feature of Elixir to me.

A notable variation of this problem is the lack of the possibility to reflect all modules using another module. Here you have a module defining a __using__ macro and you want to get all the modules applying it via use. Although seemingly unrelated, both problems could be reduced to one another, so that a solution for one of them would also provide a solution for the other one: a solution for the behaviour-reflection problem could be used to solve the using-reflection problem by introducing a pseudo behaviour and in the other direction you could introduce a __using__ macro on the behaviour and require implementations to use it (which is often already the case).

So, let’s look at some real-world examples of the behaviour-reflection problem.

Case 1: RDF serialization format registry

The RDF graph data model has an enormous number of serialization formats for all kinds of situations. Although RDF.ex provides implementations for the most important and most widely used ones it doesn’t aim to provide implementations for all existing ones. So, it defines a behaviour which can be implemented in separate packages. An implementation of a serialization format in RDF.ex consists of an encoder and a decoder, but the core entry point is an implementation of the RDF.Serialization.Format behaviour. The implementation for the Turtle formation format, for example, looks like this:

We don’t want to discuss the details of the implementation here (also not the decision to let the parameters of the format be specified as module attributes; it was my first Elixir project and I would use simple functions for this today). The key point in this example is that we have multiple identifiers under which we want to get an implementation from a registry, including those which aren’t provided out-of-the-box in RDF.ex itself. We want to use the correct format when we encounter a file with the registered extension or serve the right content-negotiated representation on HTTP requests for the registered media type from an Accept header and so on.

Solution 1: Static listings and configuration

For this instance of the problem I actually followed the advice given in many questions regarding this problem on Stackoverflow or on the ElixirForum: don’t aim to solve it by giving up on automatic registration and just list the modules statically instead.

A more flexible variation on this would be to list or extend a static list via a config option:

This approach is taken for example to register Repos in Ecto. But while perfectly fine for cases like Ecto, where the adapter-implementations are usually application-specific only, it seems not suitable for cases when there might be many adapter implementations and they are contributed by potentially several external dependencies. It just doesn’t feel right to me to wire up basic functionality via configuration (Elixir isn’t and shouldn’t become Java ;-).

There’s one particular detail that makes the simple static listing a viable option for this particular case. As you can see in the @format list of modules, the entry JSON.LD is for a behaviour implementation in an external package. It is totally fine to list names of modules not part of the package itself. In the end, module names are just atoms. However, you’ll have to check then which ones are actually modules present in an application using the library in conjunction with the other libraries. This can be done by filtering with Code.ensure_loaded?/1 and building your registry over this filtered list:

This and considering the fact that the amount of external formats is quite manageable for now allows for postponing the solution until it really becomes a problem or is requested by users for justified reasons. Actually, this might never be the case, since with that many standardized serialization formats available for all sorts of use cases and the effort it requires to implement one, it’s not that likely people will just develop one for their application, requiring them to be registered automatically. Most implementations will hopefully be published as open-source packages and could be added manually to the list.

Case 2: SPARQL function extension registry

For the next occurrence of the problem, this wasn’t an option, unfortunately. In this case, the problem occurred in SPARQL.ex. The W3C spec for SPARQL specifies an extension point for graph database vendors to extend SPARQL with vendor-specific functions. The following example query shows the usage of an extension function with the id http://example.org/geo#distance which one or more RDF graph store vendors might support:

In order to support this in SPARQL.ex this extension function could be implemented with the SPARQL.ExtensionFunction behaviour.

So, whenever we encounter SPARQL function call for this id we want to get the respective module implementing the behaviour and call the function.

Again we have the need for a registry and this time no excuse to actually tackle the problem since we definitely don’t want to maintain a list of all possible extension functions. Users might want to implement application-specific extension functions and should not be required to request their extension to be added to the list or fork the project for this. They also shouldn’t require listing their extension functions together with all the ones they might be using from other external libraries in some configuration.

Before discussing the solution that was chosen, let’s look at a couple of characteristics and requirements for this instance of the problem:

Extension functions aren’t structs, but just simple modules of functions. That means the use of protocols isn’t an option.
Having the registry available for reflection at runtime would be sufficient since we don’t need to generate code for the registered extension functions at compile-time.
Accessing the registry to retrieve a function is a performance-critical operation since it might be called many, many times during the execution of a query (for any possibly matching query solution) and we don’t want the registry access to add that much overhead on top of the actual execution of the function.
Solution 2: BEAM introspection

The solution for our problem in SPARQL.ex is to make use of BEAM introspection by getting all modules and checking their metadata if they implement the behaviour in question. Every module in Elixir comes with a module_info function that gives access to various information about the module. In particular, we can ask for all the module attributes with mod.module_info(:attributes), which will include the list of all behaviours a module has specified with the @behaviour module attribute under the :behaviour key. So, we can write a function which checks whether a module implements a certain behaviour like this:

Now, we’ll have to get all the modules to apply this function, which is a problem, unfortunately. The closest we can get to that with the builtin Erlang functions is :code.all_loaded/0. But as its name says, this function returns just the modules that have already been loaded and at what time modules are loaded depends on the mode in which the BEAM runtime system was started.

The modes are as follows:

In interactive mode, which is default, only some code is loaded during system startup, basically the modules needed by the runtime system. Other code is dynamically loaded when first referenced. When a call to a function in a certain module is made, and the module is not loaded, the code server searches for and tries to load the module.

In embedded mode, modules are not auto loaded. Trying to use a module that has not been loaded results in an error. This mode is recommended when the boot script loads all modules, as it is typically done in OTP releases. (Code can still be loaded later by explicitly ordering the code server to do so).

— https://erlang.org/doc/man/code.html

So, in interactive mode, the results of :code.all_loaded/0 is dependent on when the call happens and which modules were accidentally loaded before :code.all_loaded/0, so it must be considered to return non-determinant results in interactive mode.

An alternative approach that also works in interactive mode goes a level deeper and directly looks into the metadata of the compiled .beam files of the Mix project and filters the modules in a similar way as our implements_behaviour?/2 function by checking the :behaviour attribute. This approach is used for example by Paul Schoenfelder for plugins in exrm:

This approach, however, has its own limitations. First, it relies on Mix which isn’t available in releases normally ( i.e. unless explicitly added to the :extra_dependencies). It also doesn’t work with behaviour implementations in .exs files, most notably in test files, as these are only compiled in memory and don’t produce .beam files.

But the limitations of this approach actually complement very well with our first described method of using :code.all_loaded/0, since releases usually run in :embedded mode where all modules are loaded by the boot script upfront. It also seems that modules defined in the tests are always loaded already, at least I didn’t experience any problems yet (if you know why I would be eager to hear an explanation in the comments).

So, the solution finally taken for the SPARQL function extension modules in SPARQL.ex is to combine both approaches. It is implemented in a separate Hex package behaviour_reflection.

With its Behaviour.Reflection.impls/1 function it seems we now have a candidate that could be used for the __behaviour_impls__/1 pseudo-function in our generic example. But this function just works at runtime, which means our registry can no longer be implemented with module attributes and we’re losing all the benefits this brings with it like their performance or their possibility to be used in guards. We are also losing the possibility to use the registry in macros to generate code for the available adapter implementations. We already noticed that for this instance of the problem a runtime solution would suffice, but that we also need to have an eye on the performance characteristics.

Before digressing a little bit from our actual problem by looking at alternative ways of storing the modules at runtime, a remaining problem with our solution must be mentioned. The careful reader might have noticed already that there’s still an edge case where modules aren’t caught by both approaches. When modules implementing a behaviour are dynamically loaded later at runtime and this happens after both of our detection methods were run, they still aren’t found. This means whatever our runtime registry looks like, when such modules are dynamically loaded at runtime, we have to reinitialize the registry with the results of another Behaviour.Reflection.impls/1 call.

Excursion: Runtime registry

Let’s rethink our initial generic example registry as a runtime store for cases when our __behaviour_impls__/1 function does not work at compile-time. The natural choices for this are of course processes or ETS. Here’s an example implementation with ETS:

But if our registry lookups are a performance-critical operation for our library, as it is the case in our SPARQL extension function example, even ETS might not be acceptable. In this case, a library implementing the mochiglobal objects could be used.

The mochiglobal objects technique utilizes an optimization in Erlang for constant pools for functions that return static data. The method is named after its first occurrence in the mochiweb library. There are several libraries implementing this method, the most popular ones being Discord’s FastGlobal and Basho’s Fling. Here’s an example implementation for our initial generic example with the FastGlobal library:

Case 3: Datatype registry

The last example we want to examine is again in RDF.ex and actually motivated me to write this article.

The leaves of a graph in RDF are called literals and consist of untyped or typed values. The datatype of a literal is specified with a URI determining the semantics of its value. In RDF.ex a typed literal is in its most generic form created like this:

RDF.literal("foo", datatype: "http://example.com/datatype")

From the beginning, RDF.ex implemented the most important XSD datatypes as a behaviour. But being one of the first things I’ve implemented in Elixir and the occasion where I’ve hit the wall of being unable to reflect the behaviour implementations first, I took the approach of just listing the implementations statically, although it was clear from the beginning that this was just a postponing of the problem since RDFs datatype system is inherently open and users, therefore, should be able to define their own datatypes in RDF.ex.

For the upcoming new version of RDF.ex, the literal system got an overhaul redesign. The main goal was to deliver the missing derived XSD datatypes by implementing XSD facets for constrained datatype derivations. This makes it easier now in general to derive custom datatypes. So the problem finally had to be solved, since otherwise, this capability wouldn’t be actually usable.

Again we have the need for a registry with a mapping of datatype URIs to their datatype behaviour implementations. But the basic conditions and requirements are a bit different in this case compared to our last example. First, the datatypes are structs, which means the definition of a protocol can be considered. But in this case, I’d also like to have the list of all available datatypes at compile-time, so I can generate code from it. For example, we want to generate function clauses on the generic literal constructor function so it can construct literals from already existing instances of the datatype structs:

RDF.literal(%Example.MyDatatype{value: "foo"})

Unfortunately, this requirement of having a dynamic registry at compile-time seems impossible, even if we ignore the case of modules created at runtime. But I would be happy to be proved wrong on this assumption in the comments.

Solution 3: Protocols

Above their core feature of providing polymorphism, protocols have the interesting feature of exposing various metadata as a result of the protocol consolidation process via the __protocol__ function. In particular, we can get all the modules for which implementations exist with a __protocol__(:impls) call, so exactly what we’re looking for. Unfortunately, this only works at runtime. If we replace the __behaviour_impls__ function call in our initial generic example above with a __protocol__(:impls) call, we’re just getting the :not_consolidated atom back:

But the reason why this approach wasn’t finally chosen for the datatype registry in RDF.ex is, that although the RDF literal datatypes are structs it still doesn’t make sense to use protocols for a couple of reasons. First, protocols require all of the functions to have the struct for which the protocol is implemented as their first argument, which isn’t the case for all functions. Besides the `new` constructor we also have for example a `cast` function which casts literals of another datatype to the caller datatype:

int = RDF.integer(42)
short = RDF.Short.cast(int)

We could still apply this approach by just introducing an internal protocol and still define the interface as a behaviour which generates the protocol implementations for the functions by just delegating to the behaviour implementation:

That might make sense when the protocol is indeed useful for their polymorphism capability. But in our RDF literal datatype example, we wouldn’t need that, because the RDF.Literal module essentially acts as the generic interface which implements the polymorphism manually by delegating to the module for the respective datatype.

For this reason and because I would need to introduce an additional dependency anyway (FastGlobal for the runtime registry, since datatype resolution is again a performance-critical operation), I decided to go with an external dependency able to solve the problem.

Solution 4: ProtocolEx

ProtocolEx is a library by OvermindDL1 that implements a generalization of the protocols provided by Elixir which can not only be implemented for certain base datatypes and structs, but for anything which can be distinguished with pattern matching. This allows us to circumvent the problem by defining a Registration protocol with a function which returns the behaviour implementation module for an identifier:

As opposed to Elixir protocols, ProtocolEx also allows optional function bodies which serve as a fallback for the case when no implementation exists for a pattern.

With that, we can now generate implementations of the protocol in a __using__ macro of the adapter behaviour:

The registry implementation is now a simple delegation to the ProtocolEx protocol:

ProtocolEx also implements protocol consolidation in a compiler which must be integrated in the mix.exs file:

This makes the resolution of ids to behaviour implementations incredibly fast since it just becomes a function call using the highly optimized pattern-matching clauses. But it also allows dynamic consolidation with the ProtocolEx.resolve_protocol_ex/2 function, which would allow us to solve our problem with dynamically generated behaviour implementations.

Note that this solution is also applicable in non-struct scenarios since the Registration ProtocolEx protocol isn’t defined over the behaviour implementations, but over the identifiers as patterns instead. However, this also means ProtocolEx can’t provide something like __protocol__(:impls) to get all modules for which the protocol is implemented.

Regarding the need for compile-time access to the RDF literal datatype behaviour implementations in the particular problem case to generate constructor clauses for the datatype structs, I could eliminate this need by having a general struct clause instead which checks if the struct module implements the behaviour at runtime via introspection with a function similar to the implements_behaviour? function as discussed in the second solution.

Conclusion

The goal of this article was to show a number of ways to climb the wall when you really have to. With all of the solutions feeling hacky though, I still wish that one-day Elixir or the BEAM will provide something for this problem. With already quite a number of questions on it on the web I think the core team is aware of it and has their reasons for not providing something for it. Especially for solving it at the compile-time level, I can hardly see how this could be solved without opening up other rabbit holes. So, although I’m not very optimistic that this wall will completely disappear, I hope this article will raise awareness of the problem and spark a wider discussion of it in the community, which might finally lead to some improvements of the situation.

Update (2020–05–15)

In case 3 about the datatype registry, I’ve mentioned that I’ve worked around the need for compile-time access on the registry by providing a fallback which does the behaviour implementation check at runtime with a implements_behaviour?/2 function like the one presented in the second solution. There turned out to be more places where this check had to be performed. So, I did some benchmarking which revealed that this check is relatively costly. In the scenario case where it was presented this is done at application startup where it should still be acceptable but for the reoccurring runtime checks now an alternative faster check was needed. The only thing I could come up with was to introduce a synthetic __rdf_literal_datatype_indicator__/0 function on all implementations of the datatype behaviour which could be used for a function check via module.__info__(:functions) which seems to be the fastest check on average over the positive and negative cases. However, as modules names are indistinguishable from other atoms an exception rescue would be needed anyway (for the call to __info__), so the function check could be done with a call to the synthetic function into the blue directly. The positive case is actually even faster than the module.__info__(:functions) check. The negative case, however, is more costly. Here are the benchmarking results: https://tinyurl.com/y9ahhphy
