---
url: "https://devcarrots.com/blog/why-you-should-use-ash/"
captured_at: "2025-06-27T00:40:30+01:00"
title: "Why you should use Ash? | devCarrots"
domain: "devcarrots-com"
---

---
May 15, 2025

___

![](https://devcarrots.com/images/blog/why-you-should-use-ash/header.png)

This post is an excerpt from the book Domain Modeling with Ash Framework

[Buy the book](https://devcarrots.com/) to dive deeper into mastering Ash!

> _“Marketing is the generous act of helping someone solve a problem. Their problem.”_  
> — Seth Godin

Let’s keep this direct: in this chapter, we want to sell you on Ash. Not because we, as the authors, gain anything from Ash Framework’s success directly, but because we’re developers like you. We’ve used Ash ourselves, and it has significantly improved our productivity. We want to help you solve your problems, and we genuinely believe Ash is a _game changer_—whether you’re building small apps or large systems.

This chapter addresses common concerns about adopting Ash for your project and demonstrates how it solves real-world challenges, drawing on our experiences. These concerns broadly fall into two categories:

1.  Temporary issues tied to Ash’s small but growing community, which will diminish as the community expands, and
2.  Misconceptions about Ash’s purpose, which will persist until we shift our perspective to understand the complex business logic problems Ash is designed to solve.

Our goal is to convince you that Ash is worth your time.

Some challenges stem from Ash’s relatively small but growing community. These are temporal issues and let these not stop you from using Ash. Doing this causes a vicious feedback loop which is difficult to get out.

-   Inadequate learning resources - fewer tutorials compared to Elixir’s ecosystem.
-   Documentation can be difficult to read - though improvements are ongoing.
-   Fewer experts in Ash - limited support compared to Phoenix or Ecto.

Ash’s creator, Zach Daniel, and core team members like Rebecca Le are active on the Elixir Forum, answering questions daily. We’ve seen bugs addressed within an hour, sometimes with a minor version bump—a level of support we’ve rarely experienced. The documentation is improving, with one book published by the Ash creators and this book as another step towards making Ash more accessible.

Of course, we need more and that’s where we need you to grow Ash’s community and its support. By seeing past the learning curve and experiencing Ash’s benefits, our hope is that you’ll help accelerate its momentum.

## Inherent Challenges

Other challenges are tied to Ash’s ambitious goals:

-   New concepts: Resources, actions, and policies require learning.
-   Declarative style: Configuring code feels unfamiliar.
-   Perceived “magic”: It’s not always clear what happens behind the scenes.

If any of the above reasons stop you from adopting Ash, then it’s probable that you are using a wrong lens to see what Ash does. These perceived challenges will never go away from Ash because these are in fact the core strength of Ash as we see below. The solution here is to do the right kind of comparison to understand what benefit Ash gives you and you will be able to automatically acknowledge the worth of spending time to learn Ash. These concerns vanish once you accept to learn Ash and not fight with it with your previous mental constructs on how to build apps.

## Why Ash Solves Real Problems

Speaking from our personal experience, we, the authors, have worked on large-scale projects that started as small prototypes. Narendra and Shankar worked on a payment service for Auroville that powers the entire township’s digital transactions. Shankar also worked with startups in synthetic data generation and worked with sports clubs that processed massive volumes of data. All of these projects were created with vanilla Phoenix. We had the pleasure of working on a greenfield project using our favorite framework but the pleasure was short lived due to growing complexity.

In 2024, we started using Ash for our newer projects and after a year now, we could retrospectively feel how much Ash would have relieved the pain in our previous projects. Unfortunately, Ash wasn’t available when we started working on those projects and if we are to restart doing the same projects from scratch, we would do it in Ash. We have spoken to different people in the community, some of whom are startup founders and they don’t immediately see the benefit of Ash but rather see obstacles in using Ash. This is primarily due to the reference point of comparison chosen by them.

The reference point of comparison should not be _“how easy or difficult it’s to create a new project”_ in vanilla Phoenix vs Phoenix with Ash

rather it should be _“how easy or difficult it’s to manage this project as it matures with all its complexities”_ in vanilla Phoenix vs Phoenix with Ash.

Once we fix our point of comparison, we can truly see the real benefit of Ash and also see the necessity of why Ash has to introduce new concepts, bring in declarative style and all the magic it comes with.

Below, we use these experiences to highlight three major pain points how Ash addresses them.

### Problem 1: Onboarding New Developers

In all these projects using vanilla Phoenix, we consistently noticed how difficult it is to onboard new developers later in the lifecycle. Even with decent test coverage and documentation, a lot of the critical knowledge lives only in the heads of long-term contributors. For example, in Auroville’s payment service, new developers struggled to understand custom logic scattered across contexts, or even understand the purpose of a simple attribute named `channel_reference_id` because it’s not clear what it refers here, slowing their ramp-up. Developers don’t know where to start to understand a huge codebase. Simple things like field names that we defined in our payment service were not meaningful enough for the new developers to understand. We had a spaghetti of inline comments to explain what those did, inventing our own framework.

With Ash, we now have a clear structure to our code. Each Ash resource contains the information needed for new developers to understand what each of these entities do. The `describe` macro allows us to document any piece of information that we have on our resource module. The declarative style, along with a clean structure in itself is better than reading long pages of documentation or reading through 1000s of test cases.

### Problem 2: Managing Code Complexity

As the product features grew, we—the original developers—struggled with managing the rising code complexity. Under delivery pressure, we often compromised best practices in favor of quick hacks or inefficient solutions. Duplication of code to add new features was favored than refactoring existing ones or making them composable. These decisions kept coming back to haunt us because we never got around to fixing them once they were live. For instance, what started as a simple nice policy check using pattern matched function in our controllers grew into an ugly unmanageable chore of managing permissions. Adding and removing permissions was brittle as there were duplicates due to non-composable policy checking functions.

Ash’s declarative resources act as a single source of truth, reducing duplication. Defining an entity once generates migrations, APIs, and validations, keeping complexity manageable. Authorization policy is managed at resource level for all actions in a highly structured way. Being able to filter on attributes, relationships, aggregates and calculations using the same method removes the complexity of managing different join queries for complex operations.

### Problem 3: Long-Term Maintenance

From those experiences, we’ve learned that writing a Phoenix app with just plain Ecto is easy in the beginning—but the complexity grows significantly over time. Using Phoenix Contexts to organize your business logic works well initially. We tend to write new functions or modify existing ones as product grows but we need to remember every piece of code written, including any comments and tests, adds to the maintenance burden in long term. Anything that is written must be maintained for long term.

Ash reduces the number of implementation we write. We write less code resulting in less maintenance. We stick to the declarative nature and define what is required and even that is centralized under resources. There is hardly any duplication of what has been already said to Ash. All the implementation details are managed internally by Ash which doesn’t carry the maintenance burden for us.

| Phase | Phoenix + Contexts | Phoenix + Ash |
| --- | --- | --- |
| Getting Started | Easy setup, minimal learning | Steeper learning curve for your very first project |
| Team Onboarding in early stage of the product | Easy early on | Easier over time due to conventions |
| Team Onboarding in later stage of the product | Difficult going forward | For anyone using Ash, onboarding on new Ash project should be easy at any stage as the framework deals with the complexity internally |
| Code Growth | Becomes fragile and harder to evolve | Remains consistent and declarative |
| Maintenance | Manual conventions, more bugs due to undocumented custom implementation | Less bugs and easy maintenance due to reliance on Ash’s implementation |

### Declarative Design and Ash Magic

Declarative coding in Ash means your app feels like a configuration file you write to spell out _what_ you need: “I want a user with an email that’s required and unique.” Instead of coding every step—database queries, validations, API endpoints—you define it once in a **resource**, and Ash handles the rest. It’s a big shift from traditional apps where you’re used to writing the same logic over and over. With Ash, except for custom validations, actions or policies that are not built in Ash, you’re mostly configuring, not coding from scratch.

This declarative nature is the very strength of Ash. Ecto is also declarative in design like Ash but it requires us to declare our requirements in multiple places even if we have already declared the same requirement elsewhere. For example, in Ecto, the developer would define the schema and then also write manually, once again, the same requirements in the migration file to create the underlying database table with the same set of constraints that is already defined in Ecto Schema. If the developer needs a JSONApi for fetching the Ecto records, then the developer would write again all or subset of the same requirements in the Phoenix layer depending on the business requirements. Ash flips this on its head with resource files acting as the single source of truth.

Define a resource like this:

```
<span><span>defmodule</span><span> User</span><span> do</span></span>
<span><span>  use</span><span> Ash</span><span>.</span><span>Resource</span></span>
<span><span>  attributes </span><span>do</span></span>
<span><span>    uuid </span><span>:id</span></span>
<span><span>    string </span><span>:email</span><span>, </span><span>allow_nil?:</span><span> false</span></span>
<span><span>  end</span></span>
<span><span>  actions </span><span>do</span></span>
<span><span>    create </span><span>:register</span><span> do</span></span>
<span><span>      accept [</span><span>:email</span><span>]</span></span>
<span><span>    end</span></span>
<span><span>  end</span></span>
<span><span>end</span></span>
```

This resource says: “Users have an email, it’s required, and you can create them.” From that alone, Ash generates the database migration with the right columns and constraints—no extra work. Later, if you want a JSON API, Ash’s JSON API extension (a separate add-on) reads the same resource and spins up endpoints automatically. If you want GraphQL API, no problem. Just plugin the AshGraphQL library and it will work seamlessly using the same configuration already defined in the resource file. No controllers, no duplicate code. One definition, reused everywhere.

While this ability of Ash of doing everything automatically feels like magic and might make us feel not having control of how things are done, in reality, it’s simply an efficient way of reusing the data and managing a single source of truth. In this sense, Ash framework’s slogan “Model your domain and derive the rest” truly conveys how Ash works internally.

Hopefully we have sold you Ash! Now, let’s dive into the practical chapters to learn Ash hands-on. We can’t wait to see how you will use Ash to make your code cleaner and your work easier.

Loved the article? We hope you love our book Domain Modeling with Ash Framework too

[Buy the book](https://devcarrots.com/) to dive deeper into mastering Ash!
