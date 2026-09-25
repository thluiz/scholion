---
url: "https://thetshaped.dev/p/3-software-development-principles?ref=dailydev"
captured_at: "2026-09-25T21:25:25+01:00"
title: "3 software development principles I wish I knew earlier in my career"
domain: "thetshaped-dev"
---

Many software development principles are worth exploring and applying. However, I found 3 of them to be extremely helpful and powerful throughout my career. They **shaped the way I write software and ship products**. They’re **fundamental building blocks** if you want to grow into a Regular and Senior Developer. Today, I want to share them with you, so you can start applying them and **skyrocket your career trajectory**.

After reading this article, **you’ll learn**:

*   what is **YAGNI**
    
*   what is **KISS**
    
*   what is **DRY**
    
*   the importance of these 3 principles
    

[

![](https://substackcdn.com/image/fetch/$s_!tdue!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F380456f7-c4c1-4b3c-9a2b-b49d0b7508c4_1710x678.png)

](https://substackcdn.com/image/fetch/$s_!tdue!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F380456f7-c4c1-4b3c-9a2b-b49d0b7508c4_1710x678.png)

The **key essence** of this principle is:

> **💡 Don’t add features or functionality to our software that we currently don’t need.**

The YAGNI rule is about not adding stuff to your project or codebase just because you think you might need it later. Most of the time, you won’t end up needing it, and it just wastes time. It’s better to **stick to what you know you need at the moment**. **Don’t add code for the imaginary future**.

**⛔ Avoid**

```
interface User {
  name: string;
  age: number;
  // Future-proofing for possible new features
  address?: string;
  phoneNumber?: string;
}

function createUser(name: string, age: number): User {
  // Simplified for current needs
  return { name, age };
}
```

**✅ Prefer**

```
interface User {
  name: string;
  age: number;
}

function createUser(name: string, age: number): User {
  return { name, age };
}
```

The **key essence** of this principle is:

> **💡 Don’t add unnecessary complexity to our software.**

The KISS rule means keeping our code **easy to read and understand**. Instead of making things complicated and “smart”, try to write **code that’s straight to the point**. This makes it easier for you and others to keep track of what’s going on and fix things when they go wrong.

> **Instead of being too "smart" in your code, think about your colleagues and future teammates.** Maybe it's better to write 2-3 lines more, but guarantee that your future teammates will understand it.

**⛔ Avoid**

```
function getEvenNumbers(numbers: number[]): number[] {
  let evenNumbers: number[] = [];

  for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] % 2 === 0) {
      evenNumbers.push(numbers[i]);
    }
  }

  return evenNumbers;
}
```

**✅ Prefer**

```
function getEvenNumbers(numbers: number[]): number[] {
  return numbers.filter(number => number % 2 === 0);
}
```

It’s important to note that sometimes adding more layers of abstraction in our codebase may seem to conflict with the KISS principle because we add layers of complexity. However, when done carefully, **abstraction can simplify the overall design by hiding complex logic behind simpler interfaces or functions**. In the end, it makes our **code easier to read, understand, and maintain which is our end goal**.

The **key essence** of this principle is:

> **💡 Don’t duplicate code or data in our software.**

The DRY rule is about **not writing the same code over and over again**. If you find yourself doing the same thing in several places, find a way to do it just once. This **makes your code cleaner and easier to change later**.

**⛔ Avoid**

```
interface Product {
  id: number;
  name: string;
  price: number;
}

function getProductName(product: Product): string {
  return product.name;
}

function getProductPrice(product: Product): number {
  return product.price;
}
```

**✅ Prefer**

```
interface Product {
  id: number;
  name: string;
  price: number;
}


function getProductProperty<T extends keyof Product>(
  product: Product,
  property: T,
): Product[T] {
  return product[property];
}
```

_**Note:** All examples intent to only illustrate the idea behind each principle. They’re not meant for production._

The **YAGNI**, **KISS**, and **DRY** principles are not just coding strategies. They’re **philosophies that guide crafting quality software**. They’re **foundational elements for professional growth and efficiency**.

> **💡 Life Hack: These principles can be applied in our personal lives as well.**

Try them out in your work and see how they can make a difference!

*   **[How Tinder Scaled to 1.6 Billion Swipes per Day](https://newsletter.systemdesign.one/p/tinder-architecture)** by **[System Design Newsletter](https://newsletter.systemdesign.one/?r=643nm)**
    
*   **[My Strategies for Work Life Balance](https://thehustlingengineer.substack.com/p/my-strategies-for-work-life-balance)** by **[The Hustling Engineer](https://thehustlingengineer.substack.com/?r=643nm)**
    
*   **[The Ultimate Guide to Writing an Engineering Newsletter (Part 2)](https://hybridhacker.email/p/guide-to-grow-an-engineering-newsletter-part2)** by **[The Hybrid Hacker](https://hybridhacker.email/?r=643nm)**
    
*   **[Context-switching - one of the worst productivity killers in the engineering industry](https://newsletter.eng-leadership.com/p/context-switching-one-of-the-worst)** by **[Engineering Leadership](https://newsletter.eng-leadership.com/?r=643nm)** and **[Crushing Tech Education](https://blog.crushingtecheducation.com/)**
