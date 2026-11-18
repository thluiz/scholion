---
url: "https://dev.to/francescoxx/strategy-pattern-5oh"
captured_at: "2026-11-18T12:56:34+00:00"
title: "Strategy Pattern"
domain: "dev-to"
---

[![Cover image for Strategy Pattern](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fn99idm35iik30qu5mppd.jpg)](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fn99idm35iik30qu5mppd.jpg)

[![Francesco Ciulla](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F344808%2F8986fcb1-61a0-4888-a85e-13c115030558.jpeg)](https://dev.to/francescoxx)

## [](#strategy-pattern)Strategy Pattern

### [](#algorithm-encapsulation)_Algorithm Encapsulation_

GitHub Link: [https://github.com/FrancescoXX/Design-Patterns-Strategy-Javascript](https://github.com/FrancescoXX/Design-Patterns-Strategy-Javascript)

* * *

## [](#behavioral-design-pattern)Behavioral Design Pattern

## [](#intro)Intro

The Strategy pattern, also called policy pattern, enables selecting an algorithm at runtime.  
Deferring the decision about which algorithm to use, allows more flexibility and reusability

## [](#%EF%B8%8Frecognize)⚡️Recognize

When we want to change the behavior of our application at runtime

For example, change the behavior to:

*   aggressive
*   defensive
*   balanced

* * *

## [](#intent)💡Intent

*   Define different algorithms
*   Make them interchangeable at runtime, with a setStrategy() method

* * *

## [](#apply-when)🔧 Apply when

*   Classes only change in behavior
*   We want Different variants of an algorithm

* * *

## [](#pro)✅Pro

*   Algorithm families use inheritance for common parts Avoid conditional statements using this pattern Clients can choose the required behavior

* * *

## [](#cons)⚠️Cons

*   Increased number of objects
*   Strategies are shared between objects

* * *

## [](#great-for)🏆 Great for

*   Encapsulate an algorithm
*   Change algorithm at runtime

* * *

```
/**
 * STRATEGY PATTERN JAVASCRIPT IMPLEMENTATION
 */

//Concrete Strategy A
class AggressiveStrategy {
    constructor() {
        this.next = move => "Next aggressive move";
    }
}

//Concrete Strategy B
class BalancedStrategy {
    constructor() {
        this.next = move => "Next balanced move";
    }
}

//Concrete Strategy C
class DefensiveStrategy {
    constructor() {
        this.next = move => "Next defensive move";
    }
}

//Strategy
class AIGameStrategy {
    constructor() {
        this.setStrategy = (game) => this.game = game;
        this.next = move => this.game.next(move);
    }
}

// --- MAIN ---

//Strategies initialization
const aggressive = new AggressiveStrategy();
const balanced = new BalancedStrategy();
const defensive = new DefensiveStrategy();

//Implement Strategy Pattern
const AI = new AIGameStrategy();

//Set Defensive Strategy
AI.setStrategy(defensive);

//Perform defensive action
console.log(AI.next()); //Next defensive move

//Set Balanced Strategy...
AI.setStrategy(balanced);

//Perform balanced actions
console.log(AI.next()); //Next balanced move
console.log(AI.next()); //Next balanced move
console.log(AI.next()); //Next balanced move

//Change Strategy to Aggressive
AI.setStrategy(aggressive);

//Perform aggressive actions
console.log(AI.next()); //Next aggressive move
console.log(AI.next()); //Next aggressive move
```

Enter fullscreen mode Exit fullscreen mode

GitHub Link: [https://github.com/FrancescoXX/Design-Patterns-Strategy-Javascript](https://github.com/FrancescoXX/Design-Patterns-Strategy-Javascript)

[![Strands harness](https://media2.dev.to/dynamic/image/width=775%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fhw6m8qng9z1njxbtewf9.png)](https://strandsagents.com/?trk=1c097af3-4db9-4f1f-b0c4-4ea3fa25f1c3&sc_channel=display+ads&bb=264932)

## [](#strands-harness-is-a-stateoftheart-fully-assembled-agent-harness)[Strands harness is a state-of-the-art, fully assembled agent harness.](https://strandsagents.com/?trk=1c097af3-4db9-4f1f-b0c4-4ea3fa25f1c3&sc_channel=display+ads&bb=264932)

Strands harness is a complete, production-ready agent the moment you install it. Shell, file, and web tools, plus context management, memory, sessions, and subagents, are tuned and ready. Run it as a library or from the strands CLI, on any model and any cloud. Every default is yours to change through the open-source Harness SDK.

[Get Started with Strands](https://strandsagents.com/?trk=1c097af3-4db9-4f1f-b0c4-4ea3fa25f1c3&sc_channel=display+ads&bb=264932)
