---
url: "https://craftbettersoftware.com/p/clean-code-7-tips-to-write-clean?ref=dailydev"
captured_at: "2026-09-24T23:24:13+01:00"
title: "Clean Code: 7 tips to write clean functions"
domain: "craftbettersoftware-com"
---

Exciting News: I'm now accepting sponsorship for this newsletter. If you'd like to promote your brand to an audience of 28,000+ engaged software engineers, [read more here.](https://craftbettersoftware.com/p/sponsorship)

If it takes more than 3 seconds to understand what a function does, it's time to refactor it. The quality of your functions is inversely proportional to the time it takes to understand them.

Complex functions can lead to errors, make changes difficult, and slow down the onboarding process for new developers. Remember, code is read far more often than written, so investing time in writing clean functions is one of the best investments you can make in the long run.

Here are 7 tips on how I write clean functions:

As Uncle Bob once said:

> The first rule of functions is that they should be small. The second rule of functions is that they should be smaller than that.

A function should do one thing and do it well. But what is the ideal function size? There is no hard rule for it. **Sometimes 5 lines are just perfect, while other times a function may need 50 lines to achieve a single responsibility.**

The best is to always use your judgment based on the context. Be pragmatic, never be dogmatic. The trick is to strive for small functions but avoid making so many that they clutter your code.

There is no week that I don’t see poorly named functions. Contrary to popular belief, naming your code is not hard. It just requires additional effort, several trials, and continuous refinements.

Here are 4 tips I use to name my functions:

1.  **Use intention-revealing naming relating to the business domain.** Remember, if your code doesn't speak the customer's language, you’re not focusing on their problems.
    
2.  **Use verb and verb phrases.** Using nouns or adjectives for function names can be problematic because they don’t clearly tell what the function does
    
3.  Use **naming conventions** within your team
    
4.  Don't use different terms for the same concept. It makes your code inconsistent, confusing yourself and your colleagues. Instead, use only **one word per concept**:
    
    [
    
    ![](https://substackcdn.com/image/fetch/$s_!FXwh!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa4f01cb1-8680-414b-baec-a00bd6f557e2_1200x483.png)
    
    ](https://substackcdn.com/image/fetch/$s_!FXwh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa4f01cb1-8680-414b-baec-a00bd6f557e2_1200x483.png)
    

The ideal number of arguments for a function is zero. The problem with functions having too many parameters is that it increases complexity and makes the function harder to test.

[

![](https://substackcdn.com/image/fetch/$s_!QqFp!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F96264fe5-f919-4bbe-99d2-46673fdd5129_640x576.png)

](https://substackcdn.com/image/fetch/$s_!QqFp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F96264fe5-f919-4bbe-99d2-46673fdd5129_640x576.png)

Aim for a maximum of three parameters per function. A great solution to this is to group related parameters together:

[

![](https://substackcdn.com/image/fetch/$s_!gp9W!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbf87e853-984b-48b6-bab5-4874099082d1_992x352.png)

](https://substackcdn.com/image/fetch/$s_!gp9W!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbf87e853-984b-48b6-bab5-4874099082d1_992x352.png)

Avoid using nested IF statements in a function. They add noise and reduce maintainability:

[

![](https://substackcdn.com/image/fetch/$s_!gvMo!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8d920269-0580-4fe1-ba15-be94e483e273_1218x986.png)

](https://substackcdn.com/image/fetch/$s_!gvMo!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8d920269-0580-4fe1-ba15-be94e483e273_1218x986.png)

**Instead, invert the conditions and use guard clauses.** It will make your code easier to follow. As a bonus, you will get rid of the ELSE statements:

[

![](https://substackcdn.com/image/fetch/$s_!dSeK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9e64277b-bd00-435f-b2b6-a55380460208_1184x836.png)

](https://substackcdn.com/image/fetch/$s_!dSeK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9e64277b-bd00-435f-b2b6-a55380460208_1184x836.png)

What is a pure function? A function is pure if it always produces the same result given the same input. Secondly, it has no side effects. In other words, the output depends only on the input while there are no hidden behaviors.

There are 3 benefits of pure functions:

1.  Code is more predictable
    
2.  They are easier to test
    
3.  We can run them in parallel
    

**You know you are working on clean code when every function you read does exactly what you expect.** Pure functions make your code clean.

Using booleans as parameters often leads to code that is hard to understand. There are two main problems with it. First, when calling a function with a _true_ or _false_ flag, it’s unclear what the value means. Second, it’s difficult to extend the behavior associated with those flags.

Now, tell me, what is the difference between the following two function calls?

[

![](https://substackcdn.com/image/fetch/$s_!CM8t!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fddfc2309-7854-4314-91c9-144e3b72cc96_511x232.png)

](https://substackcdn.com/image/fetch/$s_!CM8t!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fddfc2309-7854-4314-91c9-144e3b72cc96_511x232.png)

And now tell me, what is the difference between these two:

[

![](https://substackcdn.com/image/fetch/$s_!r7np!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F19ed111c-fdc6-44c9-b83d-87ad8f8f7d1a_630x232.png)

](https://substackcdn.com/image/fetch/$s_!r7np!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F19ed111c-fdc6-44c9-b83d-87ad8f8f7d1a_630x232.png)

**Instead of booleans, use Enums, making your code self-documenting.** Small change, big impact.

When a function is not understandable, don't try to improve it by adding comments. Comments are one of the biggest code smells:

*   They become easily outdated
    
*   They are redundant many times
    
*   If used extensively, nobody reads them
    

[

![](https://substackcdn.com/image/fetch/$s_!06vB!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2377dcf3-65d2-44a2-8f64-78a7ce1718e0_1014x390.png)

](https://substackcdn.com/image/fetch/$s_!06vB!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2377dcf3-65d2-44a2-8f64-78a7ce1718e0_1014x390.png)

Comments are good tools for explaining the WHY, but they should be the last resort for explaining the WHAT. In most cases, you can replace comments by using proper function names. Never forget: **A long descriptive name is better than a long descriptive comment.**

[

![](https://substackcdn.com/image/fetch/$s_!IduN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd5ec48dd-9bd1-40eb-9976-238e5a8e7ff6_1014x352.png)

](https://substackcdn.com/image/fetch/$s_!IduN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd5ec48dd-9bd1-40eb-9976-238e5a8e7ff6_1014x352.png)

Remember: **Coding is not just telling the computer what to do. It's telling another programmer what you want the computer to do.** My TDD course covers this and much more—helping you become a professional developer who writes quality software confidently.

What you get:

*   The fundamentals of **Test-Driven Development (TDD)**
    
*   **3 real-world TDD examples** in C#, TypeScript and Rust
    
*   Using TDD to **design high-quality software**
    
*   **The two schools** of testing with the **5 test doubles**
    
*   Testing **legacy code**
    
*   **Refactoring best practices**
    

[Get instant access by clicking here](https://transformyourcraft.com/).

[Get Instant Access](https://transformyourcraft.com/)
