---
url: "https://levelup.gitconnected.com/code-smell-149-optional-chaining-b8830d7206ae"
captured_at: "2022-07-21T13:05:55-03:00"
title: "Code Smell 149 — Optional Chaining | by Maximiliano Contieri | Jul, 2022 | Level Up Coding"
domain: "levelup-gitconnected-com"
---

# Code Smell 149 — Optional Chaining

## *Our code is more robust and legible. But we hide NULL under the rug*

![1*c7clIROwMqLg96sZvJryFg.jpeg](levelup-gitconnected-com--code-smell-149-optional-chaining/5752b463a1df672c77a4fc5526ab629d.jpeg)

> *TL;DR: Avoid Nulls and undefined. If you avoid them you will never need Optionals.*

# Problems

- Nulls
- [IF Polluting](https://blog.devgenius.io/how-to-get-rid-of-annoying-ifs-forever-317033474484)

# Solutions

1. Remove nulls
2. Deal with undefined

# Context

[Optional Chaining](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining), Optionals, Coalescence, and many other solutions help us deal with the infamous nulls.

There’s no need to use them once our code is mature, robust, and without nulls.

# Sample Code

## Wrong

```
const user = {  
  name: 'Hacker'  
};if (user?.credentials?.notExpired) {  
  user.login();  
}user.functionDefinedOrNot?.();// Seems compact but it is hacky and has lots  
// of potential NULLs and Undefined
```

## Right

```
function login() {}const user = {  
  name: 'Hacker',  
  credentials: { expired: false }  
};if (!user.credentials.expired) {  
  login();  
}// Also compact   
// User is a real user or a polymorphic NullUser  
// Credentials are always defined.  
// Can be an instance of InvalidCredentials  
// Assuming we eliminated nulls from our codeif (user.functionDefinedOrNot !== undefined) {    
    functionDefinedOrNot();  
}// This is also wrong.  
// Explicit undefined checks are yet another code smell
```

# Detection

[X] Automatic

This is a *Language Feature*.

We can detect it and remove it.

# Tags

- Null

# Conclusion

Many developers feel safe polluting the code with null dealing.

In fact, this is safes than not treating NULLs at all.

[Nullish Values](https://developer.mozilla.org/en-US/docs/Glossary/Nullish), Truthy and Falsy are also code smells.

We need to aim higher and make cleaner code.

*The good*: remove all nulls from your code

*The bad*: use optional chaining

*The ugly*: not treating nulls at all

# Relations

[## Code Smell 145 — Short Circuit Hack

### Don’t use boolean evaluation as a readability shortcut

levelup.gitconnected.com](https://levelup.gitconnected.com/code-smell-145-short-circuit-hack-606ffb351c2d)

[## Code Smell 12 — Null

### Programmers use Null as different flags. It can hint an absence, an undefined value, en error etc.

blog.devgenius.io](https://blog.devgenius.io/code-smell-12-null-64fbd7792a7c)

[## Code Smell 69 — Big Bang (JavaScript Ridiculous Castings)

blog.devgenius.io](https://blog.devgenius.io/code-smell-69-big-bang-javascript-ridiculous-castings-870f20469322)

# More Info

[Optional Chaining Reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining)

[## Null: The Billion Dollar Mistake

### He is not our friend. It does not simplify life or make us more efficient. Just more lazybones. It is time to stop…

codeburst.io](https://codeburst.io/null-the-billion-dollar-mistake-c2918c92f7e0)

[## How to Get Rid of Annoying IFs Forever

### Why the first instruction we learn to program should be the last to use.

blog.devgenius.io](https://blog.devgenius.io/how-to-get-rid-of-annoying-ifs-forever-317033474484)

[## Wat

### This talk does not represent anyone's actual opinion. For a more serious take on software, try Destroy All Software…

www.destroyallsoftware.com](https://www.destroyallsoftware.com/talks/wat)

# Credits

Photo by [engin akyurt](https://unsplash.com/@enginakyurt) on [Unsplash](https://unsplash.com/s/photos/chains)
