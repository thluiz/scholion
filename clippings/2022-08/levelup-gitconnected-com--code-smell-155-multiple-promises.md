---
url: "https://levelup.gitconnected.com/code-smell-155-multiple-promises-67cccd8795c"
captured_at: "2022-08-05T10:27:57-03:00"
title: "Code Smell 155 — Multiple Promises | by Maximiliano Contieri | Aug, 2022 | Level Up Coding"
domain: "levelup-gitconnected-com"
---

# Code Smell 155 — Multiple Promises

## *You have promises. You need to wait. Wait for them all*

![1*A40NCRJXl_4rIa6aNRhiqQ.jpeg](levelup-gitconnected-com--code-smell-155-multiple-promises/4c20b8879047c825c7624ac50680df1e.jpeg)

> *TL;DR: Don’t block yourself in a sorted way.*

# Problems

- Indeterminism
- Performance bottleneck

# Solutions

1. Wait for all promises at once.

# Context

We heard about semaphores while studying Operating Systems.

We should wait until all conditions are met no matter the ordering.

# Sample Code

## Wrong

```
async fetchOne() { /* long task */ }  
async fetchTwo() { /* another long task */ }async fetchAll() {  
  let res1 = await this.fetchOne();   
  let res2 = await this.fetchTwo();  
  // they can run in parallel !!    
}
```

## Right

```
async fetchOne() { /* long task */ }  
async fetchTwo() { /* another long task */ }async fetchAll() {  
  let [res3, res4] = await Promise.all([this.fetchOne(), this.fetchTwo()]);  
  //We wait until ALL are done  
}
```

# Detection

[X] Semi-Automatic

This is a semantic smell.

We can tell our linters to find some patterns related to promises waiting.

# Tags

- Performance

# Conclusion

We need to be as close as possible to [real-world](https://medium.com/@mcsee/what-is-software-9a78c1172cf9) business rules.

If the rule states we need to wait for ALL operations, we should not force a particular order.

# Credits

Thanks for the idea

[## JavaScript is not available.

### Edit description

twitter.com](https://twitter.com/1542249552480174081)

Photo by [Alvin Mahmudov](https://unsplash.com/es/@alvinmahmudov) on [Unsplash](https://unsplash.com/s/photos/flowers-boyfriend)
