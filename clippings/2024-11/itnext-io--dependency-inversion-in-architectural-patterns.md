---
url: "https://itnext.io/dependency-inversion-in-architectural-patterns-aab2323f4118"
captured_at: "2024-11-22T13:27:56+00:00"
title: "Dependency inversion in architectural patterns | ITNEXT"
domain: "itnext-io"
---

[

![Denys Poltorak](https://miro.medium.com/v2/resize:fill:88:88/1*h7aQtRSEV2EBK5hMwsvVXA.png)

](https://denyspoltorak.medium.com/?source=post_page---byline--aab2323f4118--------------------------------)

[

![ITNEXT](https://miro.medium.com/v2/resize:fill:48:48/1*yAqDFIFA5F_NXalOJKz4TA.png)

](https://itnext.io/?source=post_page---byline--aab2323f4118--------------------------------)

Published in

4 min read

2 hours ago

\--

> This is a chapter from my book [Architectural Metapatterns: the Pattern Language of Software Architecture](https://medium.com/itnext/the-list-of-architectural-metapatterns-ed64d8ba125d). Any feedback is warmly welcome. The book is free (CC BY license) and available for download ([PDF](https://github.com/denyspoltorak/publications/blob/main/ArchitecturalMetapatterns/Architectural%20Metapatterns.pdf) and [ePub](https://github.com/denyspoltorak/publications/blob/main/ArchitecturalMetapatterns/Architectural%20Metapatterns.epub)) [from GitHub](https://github.com/denyspoltorak/publications/tree/main/ArchitecturalMetapatterns). This chapter will appear in version 0.9 of the book.

I am no fan of [SOLID](https://en.wikipedia.org/wiki/SOLID) — to the extent of being unable to remember what those five letters mean — thus I was really surprised to notice that one of its principles — [dependency inversion](https://en.wikipedia.org/wiki/Dependency_inversion_principle) — is quite common with architectural patterns, which means that it is way more generic than OOP it is promoted for.

Let’s see how dependency inversion is used on the system level.

## Patterns that build around it

Both [_Plugins_](https://medium.com/itnext/plugins-a70bd06bd36f) and the derived [_Hexagonal Architecture_](https://medium.com/itnext/hexagonal-architecture-fe1250fb52be) rely on dependency inversion for the same reason — to protect the _core_, which contains the bulk of the code, from variability in the external components that it uses. The _core_ operates interfaces ([SPI](https://en.wikipedia.org/wiki/Service_provider_interface)s) which it defines so that it may not care what exactly is behind an interface.

It is the nature of the polymorphic components that distinguishes the patterns:

*   [_Plugins_](https://medium.com/itnext/plugins-a70bd06bd36f) allow for small pieces of code, typically contributed by outside developers, to provide customizable parts of the system’s algorithms and decision making. Oftentimes the _core_ team has no idea of how many diverse plugins will be written for their product.
*   [_Hexagonal Architecture_](https://medium.com/itnext/hexagonal-architecture-fe1250fb52be) is about breaking dependency of the _core_ on external libraries or services by employing _adapters_. Each adapter depends both on the core’s SPI and on the API of the component which it adapts. As interfaces and contracts vary among vendors and even versions of software, while we want it to be interchangeable, we need adapters to wrap the components to make them look identical to our core. Besides, stub adapters help develop and test the core in isolation.

## Patterns that often rely on it

A few more metapatterns tend to apply the approach to earn its benefits, even though dependency inversion is not among their integral features:

*   [_Microkernel_](https://medium.com/itnext/microkernel-abb60773e469), yet another metapattern derived from [_Plugins_](https://medium.com/itnext/plugins-a70bd06bd36f), distributes resources of providers among consumers. Polymorphism is crucial for some of its variants, including _operating system_, but may rarely benefit others, such as _software framework_.
*   _Top-Down_ [_Hierarchy_](https://medium.com/itnext/hierarchy-7352e21f301f) spreads responsibility over a tree of components. If the nodes of the tree are polymorphic, they are easier to operate, and we have dependency inversion. However, in practice, a parent node may often be strongly coupled to the types of its children and access them directly.
*   In another kind of [_Hierarchy_](https://medium.com/itnext/hierarchy-7352e21f301f), namely _Cell-Based Architecture_ (aka _Services of Services_), each _cell_ [may employ](https://github.com/wso2/reference-architecture/blob/master/reference-architecture-cell-based.md) a [_cell gateway_](https://medium.com/itnext/proxy-f378298d0bf1) and outbound [_adapters_](https://medium.com/itnext/proxy-f378298d0bf1) to isolate its business logic from the environment — just like [_Hexagonal Architecture_](https://medium.com/itnext/hexagonal-architecture-fe1250fb52be) does for its monolithic _core_.

## Patterns that may use it

Finally, the basic architectures, [_Layers_](https://medium.com/itnext/layers-138e793adf51) and [_Services_](https://medium.com/itnext/services-ab8a45878621), may resort to something similar to dependency inversion to decouple their constituents:

*   We often see a higher layer to depend on and a lower layer to implement a standardized interface, like POSIX or SQL, to achieve interoperability with other implementations (which is yet another wording for polymorphism).
*   A service may follow the concept of [_Hexagonal Architecture_](https://medium.com/itnext/hexagonal-architecture-fe1250fb52be) by using an [_anti-corruption layer_](https://medium.com/itnext/services-ab8a45878621) \[DDD\] or [_CQRS views_](https://medium.com/itnext/polyglot-persistence-21a6e5bc5f9e) \[MP\] as [_adapters_](https://medium.com/itnext/proxy-f378298d0bf1) that protect it from changes in other system components.

## Summary

Many architectural patterns employ dependency inversion by adding:

*   an _interface_ to enable polymorphism of their lower-level components or
*   _adapters_ to protect a component from changes in its dependencies.

The two approaches apply in different circumstances:

*   If you can enforce your rules of the game on the suppliers of the external components, you merely _define an SPI_, expecting the suppliers to implement and obey it.
*   If the suppliers are independent and it is your side that adapts to their rules, you should _add adapters_ to translate between your lovely SPI and their whimsical APIs.

## References

\[DDD\] Domain-Driven Design: Tackling Complexity in the Heart of Software. _Eric Evans. Addison-Wesley (2003)._

\[MP\] Microservices Patterns: With Examples in Java. _Chris Richardson._ _Manning Publications (2018)_.
