---
url: "https://jesseliberty.com/2025/01/16/mastering-c-pattern-matching/?utm_source=newsletter.csharpdigest.net&utm_medium=newsletter&utm_campaign=the-impact-of-locks-and-waits-on-latency&_bhlid=e5606aad9f3e29637bbb5934351f5e4772f95516"
captured_at: "2026-09-25T19:28:36+01:00"
title: "Mastering C# – Pattern Matching"
domain: "jesseliberty-com"
---

[Microsoft](https://learn.microsoft.com/) has a wonderful tutorial on pattern matching, in which you model a lock (to raise or lower a ship when there would otherwise be a waterfall). They model the two doors and the water level.

While their example is excellent it is long, and in this blog post I’m going to take the essence of pattern matching using their example.

We start with a state machine:  

![](https://jesseliberty.com/wp-content/uploads/2025/01/image-800x380.png)

The chart indicates whether the gate should be opened or closed based on the new setting and the current status of the gate as well as the water level. We read it as follows: _if the new setting is closed, it doesn’t matter what the starting state of the gate is, nor the water level, we close the gate (first three lines)._

On the other hand, if the gate is closed (line 4) and we give it a new state of open and the water level is high, then we open the gate. If, on line 5, we tell it to open from a closed state, but the water level is low then we have an error (don’t open when the water is low).

Finally, if we say open and it is open and the water level is high, then we do, in fact, open.

These states can be modeled in a [switch expression](https://jesseliberty.com/wp-admin/post.php?post=12810&action=edit&classic-editor) using pattern matching where true = open and false = closed:

```
HighWaterGateOpen = (open, HighWaterGateOpen, CanalLockWaterLevel) switch
{
(false, false, WaterLevel.High) => false,
(false, false, WaterLevel.Low) => false,
(false, true, WaterLevel.High) => false,
(true, false, WaterLevel.High) => true,
(true, false, WaterLevel.Low) => throw new InvalidOperationException("Cannot open high gate when the water is low"),
(true, true, WaterLevel.High) => true,
```

As you can see, the first three _arms_ of this expression start false and end false, as we saw above. Next, we have the case where the new state is true, the current state is false and the Water level is high. This causes the gate to open (true).

But it gets easier. First, we need the default case. In the latest C# an underscore matches anything. So we add

\_ => throw new InvalidOperationException(“Invalid internal state”),

as the default, meaning if anything else comes up, it is invalid.

Note that, as we said, the first three arms all evaluate to false. We can replace them with  
(false, \__, \__) => false,  
You read this as, _if the first value is false (the new condition) then no matter what the second and third conditions are, we will evaluate to false_.

Next we need to know what to do if the new state is true. This is slightly tricker as it depends on the water level:

```
(true, _, WaterLevel.High) => true, 
(true, false, WaterLevel.Low) => throw new InvalidOperationException("Cannot open high gate when the water is low"), => throw new InvalidOperationException("Invalid internal state"),
```

Thus, if the new state is true, and the water level is high (no matter the state of the gate), then we do open the gate. If the new state is open (from on original state o closed) and the water level is low then, uh oh.

Here is the final version of the method:

```
// Change the upper gate.
public void SetHighGate(bool open)
{
    HighWaterGateOpen = (open, HighWaterGateOpen, CanalLockWaterLevel) switch
    {
        (false, _,    _)               => false,
        (true, _,     WaterLevel.High) => true,
        (true, false, WaterLevel.Low)  => throw new InvalidOperationException("Cannot open high gate when the water is low"),
        _                              => throw new InvalidOperationException("Invalid internal state"),
    };
}
```

All of this is simpler, cleaner and thus easier to understand and maintain than a series of if statements or even a set of switch statements.

![Unknown's avatar](https://secure.gravatar.com/avatar/0cab2119c23ed16cd7f09b824bae850648d76ad943a1aa70fbb8f216a0944b83?s=60&d=mm&r=g)

## About Jesse Liberty

Jesse Liberty has three decades of experience writing and delivering software projects and is the author of 2 dozen books and a couple dozen online courses. Liberty is a Senior AI Engineer at the University of Pittsburgh Medical Center, and was a Team Lead and Senior Software Engineer for various corporations, a Senior Technical Evangelist for Microsoft, a Distinguished Software Engineer for AT&T, a VP for Information Services for Citibank and a Software Architect for PBS. He is a 21 year Microsoft MVP.
