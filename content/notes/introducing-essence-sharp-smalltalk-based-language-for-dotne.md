---
title: "Introducing Essence#: A Smalltalk-based Language for .NET"
date: '2014-11-12T23:23:38-03:00'
category: webclip
summary: 'The article presents Essence# as a Smalltalk-based .NET language built for trading plan scripts, with dynamic typing, DLR integration, namespaces as objects, object state architectures, and traits.'
tags: ["essence-sharp", "dotnet", "smalltalk", "dynamic-typing"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Article: Introducing Essence#: A Smalltalk-based Language for .NET"
    url: "http://www.infoq.com/articles/Introducing-Essence-Sharp?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-11/infoq-com--introducing-essence-sharp-smalltalk-based-language-for-dotne.md"
    kind: repo
---

Essence# is described as a .NET-compatible language built by Alan Lovejoy as a Smalltalk-based superset for a specific trading use case. The language was created so non-programmer trading partners could write trading plan scripts, and it is designed to be easier for them than C# or EasyLanguage.

The article explains that Essence# is dynamically typed, strongly typed at run time, and built on the DLR. It emphasizes interoperability with other .NET languages, where Essence# objects can be called from foreign code and can also work with foreign types. It also highlights several design ideas that differ from C#, including namespaces as objects, object state architectures, and traits as a way to compose behavior.

## Reading notes

- Essence# was built for trading financial markets, especially for writing trading plan scripts triggered by buy or sell signals.
- The language was created for trading partners who are not programmers and should not need to master computer science.
- Essence# is presented as easier for that use case than TradeStation’s EasyLanguage and much easier than C#.
- The language runs on top of the Dynamic Language Runtime and was implemented as a .NET language because NinjaTrader is implemented in C#.
- Essence# can be used with a Java or C# style, a Python style, or a Smalltalk style, depending on the use case.
- The design favors minimal syntax and assumes the programmer is competent.
- Essence# uses dynamic typing with no static type checking in the language syntax, while still enforcing type safety at run time.
- The DLR is used for code generation, parameters, closures, message sends, and interoperability with foreign objects.
- Essence# objects implement IDynamicMetaObjectProvider and can interact with other languages that use the DLR protocol.
- The compiler emits a DLR CallSite for every message send and resolves message sending at run time.
- Namespaces are actual objects, and code can store loose variables, constants, and functions in them.
- The main namespaces are Root, default, CLR, and Undeclared.
- Namespace entries can be Public, Local, or InHierarchy.
- The article introduces object state architecture as a way to describe classes by how their instances behave at runtime.
- It lists architectures such as Abstract, Stateless, NamedSlots, IndexedObjectSlots, and Indexed[Type]Slots.
- It also lists system architectures such as Message, Namespace, Pathname, Block, Method, Behavior, Class, Metaclass, BehavioralTrait, and HostSystemObject.
- Traits are presented as Essence#’s answer to multiple inheritance.
- Traits can be combined with +, with conflicting methods excluded, and can also be adjusted with - and @.
- Essence# is available on CodePlex under the Simplified BSD License.
- Alan Lovejoy is described as a discretionary trader and former software engineer with experience in trading and Smalltalk.
