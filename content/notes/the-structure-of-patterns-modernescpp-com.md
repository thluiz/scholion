---
title: "The Structure of Patterns"
date: '2022-08-15T10:57:48-03:00'
category: webclip
summary: 'The post explains the three-part definition of a pattern and walks through the 13-step structure used in classic pattern books, using the Strategy pattern in C++ as the example.'
tags: ["design-patterns", "strategy-pattern", "c-plus-plus"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The Structure of Patterns - ModernesCpp.com"
    url: "https://www.modernescpp.com/index.php/the-structure-of-patterns"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-08/modernescpp-com--the-structure-of-patterns-modernescpp-com.md"
    kind: repo
---

The post starts from Christopher Alexander’s definition of a pattern as a three-part rule linking context, problem, and solution. It also notes that patterns should be useful, usable, and used, with the rule of three saying a pattern is only a pattern after real-world use at least three times.

## Reading notes

- A pattern describes a generic solution to a recurring design problem in a specific context.
- The context is the design situation, the problem is the forces acting in that situation, and the solution is the configuration that balances those forces.
- Alexander describes patterns as useful, usable, and used.
- The rule of three says a pattern counts only after it has been applied to a real-world solution at least three times.
- The article says the classic pattern books present patterns in 13 repeating steps, which can feel monotonous.
- The Strategy pattern is used as the example for that structure.
- Its intent is to define a family of algorithms, encapsulate them in objects, and make them interchangeable at run time.
- It is also known as Policy.
- The motivation example is sorting strings in different ways without hard-coding the sorting criteria.
- The pattern applies when related classes differ only in behavior, when different algorithm variants are needed, and when algorithms should be transparent to the client.
- The participants are Context, Strategy, and ConcreteStrategy classes.
- The context and the concrete strategy together implement the chosen algorithm, and the context forwards client requests to the selected strategy.
- The listed consequences are uniform use of related algorithms, hiding implementation details from the client, and exchanging algorithms at run time.
- The implementation section says to define the context and Strategy interface, implement concrete strategies, and let the context take arguments either at run time or at compile time as a template parameter.
- The sample code shows `std::sort` with different sorting criteria and `std::greater` for reverse order.
- The container example treats policies as configurable generic behavior, with `std::vector` and `std::unordered_map` as examples.
- The article points to C++17 execution policies for STL algorithms and C++20 ranges customization points such as projections.
- It ends by saying strategy objects should be lightweight, making lambda expressions a good fit.
