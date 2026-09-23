---
url: "https://app.daily.dev/posts/k7yR5YBI5?utm_source=notification&utm_medium=email&utm_campaign=digest"
captured_at: "2025-08-14T20:53:47+01:00"
title: "What's the difference between Type and Interface in TypeScript?"
domain: "app-daily-dev"
---

What's the difference between Type and Interface in TypeScript?
Anatoly Nevzorov

Ever stared at a TypeScript file and thought: "Wait… why did I just use `type` here instead of `interface`?" Yeah. Me too. And honestly? It's not always obvious. Feels like choosing between ketchup and mustard on a hot dog, both kinda work, but someone out there will judge you hard.

Let's cut through the noise. No fluff. Just real talk, weird analogies, and a few hot takes. We're diving into the Type vs Interface tango in TypeScript. Not the textbook way. The way, like explaining quantum physics using pizza toppings.

Imagine you're building a Lego city.
`interface`? That's your modular Lego baseplate. You snap pieces together. Want to extend a house? Just click another block on top. Need a balcony? Attach it. Tomorrow? Add solar panels. It's open-ended. Evolves. Grows. Like a Tamagotchi, but less tragic when you forget it.

Now `type`? That's your custom 3D-printed Lego piece. Precise. Sharp edges. Does exactly what you designed. But once it's printed? No modifications. Want changes? Recreate the whole thing. Brutal. Efficient. Final.

That's the vibe.

### So What's the Real Difference?

Let's not sugarcoat it, in 90% of cases, they do almost the same thing. You can define object shapes, functions, even unions. But the devil's in the details. And TypeScript's devil wears Prada and judges your code style.

#### 1. Extensibility: The Big One

`interface` can be reopened. Like a restaurant that closes at 3 PM and magically reopens at 7 with a new menu.

```ts
interface Cat { meow: () => string; }
// Later, somewhere else in your code...
interface Cat { purr: () => string; }
// Boom. Cat now has both meow AND purr. TypeScript just… merged them. No drama.
```

Try that with `type`? Nope. Compiler throws a fit. "Cannot redeclare 'Cat'". It's a one-shot deal. Like a tattoo you regret at 2 AM.

```ts
type Dog = { bark: () => string; };
type Dog = { wagTail: () => void; };
// Error. TypeScript says: "Nah, bro. Pick one."
```

So if you're building a library, or expect your types to evolve across files? `interface` is your BFF.

#### 2. Flexibility in Shape

`type` doesn't play by the same rules. It's… wilder. Can represent unions, tuples, mapped types, conditional types, stuff `interface` just can't handle.

```ts
type Status = 'loading' | 'success' | 'error';
type Coordinates = [number, number];
type Maybe<T> = T | null | undefined;
```

Try doing that with `interface`? Good luck. You'll end up with 17 interfaces and a therapist.

`interface` is strict. It likes objects. It likes structure. It drinks black coffee and reads the spec before bed.

`type`? It's the one at the party doing handstands on the couch, yelling, "I can be a string OR a function OR a recursive tree, deal with it!"

#### 3. Merging vs. Intersection

`interface` merges automatically. Like two rivers joining.

```ts
interface User { id: number; }
interface User { name: string; }
// User now has id + name. Magic? Or just TypeScript being slick?
```

`type`? No merging. But you can intersect:

```ts
type Id = { id: number };
type Name = { name: string };
type User = Id & Name;
// Same result, but manual work.
```

It's like building a sandwich. `interface` hands you a fully stacked one. `type` gives you ingredients and a knife. You do the slicing.

#### 4. Performance & Tooling

Here's a spicy take: interfaces are slightly better for large-scale projects. Why? Because TS can optimize them. Faster autocomplete. Smoother refactoring. Less "TS Server is thinking…" moments.

Types? They're heavier. Especially complex unions. Can slow down IDEs. Not a dealbreaker. But if you're working on a codebase the size of a small moon? Every millisecond counts.

### So… What Should You Use?

Let's get real. There's no one answer. But here's my rule of thumb, forged in fire, broken builds, and late-night debugging:

> Use `interface` for public APIs, objects, and things that might grow.
> Use `type` when you need flexibility, unions, tuples, or complex logic.

Examples?

Go for `interface`:
- Shapes of objects (users, config, API responses)
- Classes implementing contracts
- Libraries or shared code
- Anything you might extend later

Go for `type`:
- Union types (`'dark' | 'light'`)
- Tuples (`[string, number]`)
- Function signatures with overloads
- Conditional or mapped types
- When you need `&` or `|` in the definition

And hey, don't overthink it. If you're just starting? Pick `interface` for objects. It's safer. More predictable. Like wearing socks with sandals, functional, even if not trendy.

### A Few Curveballs

You can extend an `interface` from a `type`, but only if the type is object-like.

```ts
type Animal = { sound: string };
interface Dog extends Animal { breed: string; }
// Works
```

But not the other way around if the type uses unions or primitives.

And `type` can mimic `interface` using `&`, but it's clunkier. Like using duct tape to fix a Rolex.

### Final Thoughts?

It's not about which is better. It's about fit.

Think of `interface` as a well-tailored suit, clean, structured, meant to be built upon.
`type`? That's your Swiss Army knife. Not pretty, but damn useful when things get weird.

Use both. Respect both. And for the love of linting, don't religiously stick to one. That way lies madness.

Oh, and if your teammate insists `type` is always superior? Ask them to define a union with it… then walk away slowly.
