---
url: "https://dev.to/claranet/solid-principles-3kld?ref=dailydev"
captured_at: "2026-09-24T23:53:41+01:00"
title: "Let's talk: SOLID Principles 🇬🇧"
domain: "dev-to"
---

## [](#why-do-we-need-principles-)Why do we need principles ?

Software would be a pain without clean code rules. But getting well written bricks of code is not enough: you can make a mess if those bricks are not well assembled.

That's were architecture principles comes in.

S.O.L.I.D. rules stands for:

*   **S**RP: Single Responsibility Principle
*   **O**CP: Open Closed Principle
*   **L**SP: Liskov Substitution Principle
*   **I**SP: Interface Segregation Principle
*   **D**IP: Dependency Inversion Principle

## [](#single-responsibility-principle)Single Responsibility Principle

| _A module should be responsible to one, and only one, actor._

Let's understand this principle with an example.  

```
class Employee {
  calculatePay()
  reportHours()
}
```

Enter fullscreen mode Exit fullscreen mode

A product got two methods to calculate a pay and report working hours of an employee.

Calculate pay is used by an Actor responsible of financial stuff, and hours reporting by another Actor, a manager for example.

We broke the Single Responsibility Principle.

Furthermore, imagine that these methods have some lines of code in common because we care about code reusability.

A change in the common lines of code would satisfy the result of a method but can make the second fail.

## [](#open-closed-principle)Open Closed Principle

| _Code entities should be open to extensions and closed to modifications_  

```
class Player {
  printRole() {
    switch(this.role) {
        case "elf":
            console.log("Player is elf !");
            break;
        case "warrior": 
            console.log("Player is warrior !");
            break;
        case "..."
    }
  }
}
```

Enter fullscreen mode Exit fullscreen mode

What happens if you need to add another Player role ?

You will have to modify the existing function and then violate the principle.

To be compliant with the principle, you will need to use abstractions.  

```
class Player {
    constructor(private readonly role: PlayerRole) {}
    printRole() {
        console.log("Player is ", this.role.getRole());
    }
}

interface PlayerRole {
    getRole(): string
}

class RoleElf implements PlayerRole {
    getRole() {
        return 'elf';
    }
}

class RoleWarrior implements PlayerRole {
    getRole() {
        return 'warrior';
    }
}

const player = new Player(new RoleWarrior());
player.printRole();
```

Enter fullscreen mode Exit fullscreen mode

This way, if you want to add a new Role, you will not have to modify existing code, but only implement PlayerRole.

## [](#liskov-substitution-principle)Liskov Substitution Principle

| _When extending a class, remember that you should be able to pass objects of the subclass in place of objects of the parent class without breaking the client code._

Imagine this Player class, we define a property and a method to make player flying...  

```
class Player {
    items: string[];
    flying: boolean;

    fly(): {
        this.flying = true;
    }
}

class Warrior extends Player {
    fly(): void {
        throw new Error("Warriors can't fly, only Elves can !!!!");
    }
}
```

Enter fullscreen mode Exit fullscreen mode

But we break the Liskov principle as defining a subclass of Player, Warrior, may break the code.

Let's see how we can be compliant easily.  

```
class Player {
    items: string[];
}

class Elf extends Player {
    items: string[];
    flying: boolean;

    fly(): void {
        this.flying = true;
    }
}
```

Enter fullscreen mode Exit fullscreen mode

## [](#interface-segregation-principle)Interface Segregation Principle

| _No client should be forced to depend on methods it does not use._

Let's start by an example which breaks ISP.  

```
interface CharacterActions {
    throwMagicPower(): number;
    speak(): string;
}
class PlayableCharacter implements CharacterActions {
    throwMagicPower(): number {
        return 100;
    }
    speak(): string {
        return "I am a playable character";
    }
}
class NonPlayableCharacter implements CharacterActions {
    throwMagicPower(): number {
        // not applicable to NPC...
        return 0;
    }
    speak(): string {
        return "I am a non playable character";
    }
}
```

Enter fullscreen mode Exit fullscreen mode

This breaks ISP because `NonPlayableCharacter` is forced to depend of method `throwMagicPower` it doesn't use.

To be compliant, we can split `CharacterActions` into smaller interfaces and only implement when needed.  

```
interface Speaker {
    speak(): string;
}

interface Magician {
    throwMagicPower(): Damage;
}

class PlayableCharacter implements Magician, Speaker {
    throwMagicPower(): Damage {
        return 100;
    }
    speak(): string {
        return "I am a playable character";
    }
}
class NonPlayableCharacter implements Speaker {
    speak(): string {
        return "I am a non playable character";
    }
}
```

Enter fullscreen mode Exit fullscreen mode

## [](#dependency-inversion-principle)Dependency Inversion Principle

| _Depend upon abstractions, not concretions._

Dependency Inversion proposes that instead of depending on concrete class implementations, we should depend on abstractions.

Even more important when it concerns business logic !

Let's see what would be a bad code example  

```
class NotifyUserUseCase {
    constructor(private readonly emailSender = new EmailSender()) {}
    execute({order, buyer}) {
        const text = `An order of ${order.price}${order.currency} have been created with your account`;
        this.emailNotificationSender.send({
            text,
            to: buyer
        })
    }
}
```

Enter fullscreen mode Exit fullscreen mode

Here, our notify use-case is directly dependent of EmailSender.

First, it would be hard to unit test our use-case because we cannot easily fake our Notifier.

Secondly, we're coupled with an implementation detail: what if our product owner want to change from mail to SMS ?

Here is a proper version implementing DIP  

```
interface NotificationProvider {
    send(): void;
}

class EmailNotificationProvider implements NotificationProvider {
    send(): {
        // stuff to send email
    }
}

class SMSNotificationProvider implements NotificationProvider {
    send(): {
        // stuff to send SMS
    }
}

class FakeNotificationProvider implements NotificationProvider {
    send(): {}
}

class NotifyUserUseCase {
    constructor(private readonly notificationProvider: NotificationProvider) {}
    execute({order, buyer}) {
        const text = `An order of ${order.price}${order.currency} have been created with your account`;
        // business logic don't care about notification being a SMS or Mail
        this.notificationProvider.send({
            text,
            to: buyer
        })
    }
}
```

Enter fullscreen mode Exit fullscreen mode

* * *

I'm Baptiste FAMCHON, Tech Lead specialized in frontend at Claranet.  
I write regularly on [dev.to](https://dev.to/claranet) and [LinkedIn](https://www.linkedin.com/in/baptiste-famchon/) about web and software crafting topics.

At [Claranet](https://www.claranet.com/), we can also help you think about IT modernization, cloud infrastructure, security and web development.

Don't hesitate to contact us! 🚀
