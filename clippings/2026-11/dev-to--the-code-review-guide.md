---
url: "https://dev.to/camilaleniss/the-code-review-guide-4gfo"
captured_at: "2026-11-16T02:04:23+00:00"
title: "The Code Review Guide"
domain: "dev-to"
---

Code reviews are a common pratice in tech industry. When you do a Pull Request / Merge Request someone has to review it, give feedback, and approve it when it’s ready to be part of master branch - if that is the branch to which the PR is directed, of course -

When it’s your first time being a reviewer, maybe you’ve already learned a little from the comments you’ve received. **Don’t be scared, it’s not a big deal**. Code reviews are also made to learn. You’re not attacking your teammates, _it’s not a personal thing_. You’re questioning their code, looking at how to improve it.

> Remember that code reviews are not just for looking at what’s wrong, but for learning from others.

With this mindset let’s see how to do that:

## [](#have-context)Have context

Every PR has a purpose. It could be part of a proposal, a bug fix, a new feature and so on. **Make sure to read and understand the caption of the PR before looking at the code**.  
It will give you better picture of what you are going to review. You can help by looking at which files were modified to give you more context of their scope.  
Make sure that the modified files are part of what that PR is supposed to do _(maybe they suddenly uploaded a file by mistake)_

* * *

Ok, we already know what the PR is suppose to do. Let’s see the code. You can review it by two approaches: _readability and functionality._  
No matter what approach you choose, always keep these two questions in mind:

*   How could I improve that?
*   What could go wrong?

## [](#reviewing-by-readability)Reviewing by readability

Maybe this is the most superficial way you can begin to review it, but it ensures that **the code is easily maintained over time**. If you can’t understand that code now, in one year you won’t get it either.

> Every piece of code you write has a price: maintenance. Do others a favor and check carefully.

These are some of the things you can review:

*   Look for typos -they happen all the time- in variables and functions names, in comments descriptions or even in files names.
*   Class and functions are well-named. The responsibility of the function goes according to the name.
*   Descriptive and well-written comments. This does not mean it should be long, be assertive.
*   Consistency. The code is not written as an isolated piece in the repository. Make sure it is consistent with the practices. Try to make sure that the code you are reviewing is in line with the rest.

For example, it happens with case styles:  

```
// camelCase
// PascalCase
// snake_case
// kebab-case
```

Enter fullscreen mode Exit fullscreen mode

See that all the code has harmony and that the piece they are going to add doesn’t make noise.

*   No print statements. Maybe they forgot it while debuging.
*   Avoid unnecessary nested statements.
*   Return early whenever you can If you see code like this:

```
var myVar = "I am a variable"

if strings.ContainsAny("a", myVar){
   return myVar
}else{
   return nil
}
```

Enter fullscreen mode Exit fullscreen mode

You can refactor it doing this:  

```
var myVar = "I am a variable"

if strings.ContainsAny("a", myVar){
   return myVar
}

return nil
```

Enter fullscreen mode Exit fullscreen mode

Suggest anything you think is necessary to make the code better understood.

## [](#reviewing-by-functionality)Reviewing by functionality

As a reviewer you’re also responsible for the **quality of the code that the company ships to production**. Please pay attention to the detail, scalability and especially security.

*   Does the flow makes sense?
*   Are there innecessary validations, loops, whatever?
*   Single responsability for methods and classes. So testing can be more atomic.
*   Is it susceptible to failure? For example, make sure that it’s checking the length of the array before accessing it. Or at least ensure that it will not end up in an error -NullPointer alert-
*   How would I have done it? Is it my way better? Could that logic improve the current one?
*   Tests are not changing without a reason. For example, if the test was used to validate that the function is not throwing an error, but then it’s validating that the function throws and error, ask why. Maybe there will be breaking changes that affect the operation.
*   Don’t delete tests without a reason. Ask why if you don’t get why the test has been deleted. Isn’t it necessary anymore? Why?
*   The tests are enough to fulfill the impact of the change. And also, review that tests are asserting what they should.

## [](#what-should-i-do-when-i-dont-know-the-language-of-the-code)What should I do when I don’t know the language of the code?

This is a classic. You don’t know about a certain coding language or technology and you have to review it.  
First, don’t be scared. Make sure that the other reviewers know the language just because they can detect things that you can’t. And ask them if it’s necessary.  
A good starting point is the _superficial review_: look for typos and well-name of variables.  
If you want, you can search for other code in the repository of the same language and try to discover patterns. Remember that you can ask if something isn’t clear.

* * *

And the most important advice: **Don’t follow the “Best Practices” blindly**. Always think first. Each piece of code is trying to add value to the product. Think how it could add value and make life easier for the developer who will maintain that code later, maybe it’s you.

This article was first posted in [Medium](https://medium.com/@camilaleniss/the-code-review-guide-9e793edcd683)  
Thanks for reading :)
