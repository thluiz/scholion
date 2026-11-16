---
url: "https://jimmybogard.com/domain-driven-refactoring-defactoring-and-pushing-behavior-down"
captured_at: "2026-11-16T04:44:43+00:00"
title: "Domain-Driven Refactoring: Defactoring and Pushing Behavior Down"
domain: "jimmybogard-com"
---

Posts in this series:

*   [Intro](https://www.jimmybogard.com/domain-driven-refactoring-intro/)
*   [Procedural Beginnings](https://www.jimmybogard.com/domain-driven-refactoring-procedural-beginnings/)
*   [Long Methods](https://www.jimmybogard.com/domain-driven-refactoring-long-methods/)
*   [Extracting Domain Services](https://www.jimmybogard.com/domain-driven-refactoring-extracting-domain-services/)
*   [Defactoring and Pushing Behavior Down](https://www.jimmybogard.com/domain-driven-refactoring-defactoring-and-pushing-behavior-down/)
*   [Encapsulating Data](https://www.jimmybogard.com/domain-driven-refactoring-encapsulating-data/)
*   [Encapsulating Collections](https://www.jimmybogard.com/domain-driven-refactoring-encapsulating-collections/)

In the last post, we looked at our procedural handler and pulled behavior out that called to external services into its own domain service. This let our handler become more unit testable by creating a [test seam](https://understandlegacycode.com/blog/key-points-of-working-effectively-with-legacy-code/?ref=jimmybogard.com#identify-seams-to-break-your-code-dependencies), and we could now alter the behavior of the abstraction through mocks/stubs etc.

Our resulting handler is still procedural in nature:

```
// Calculate offer value
var value = await _offerValueCalculator.CalculateOfferValue(
    member, 
    offerType, 
    cancellationToken);

// Calculate expiration date
var dateExpiring = CalculateExpirationDate(offerType);

// Assign offer
var offer = AssignOffer(
    member, 
    offerType, 
    value, 
    dateExpiring);
```

We see the first set of logic is extracted out into a separate object, but the other two methods are simply static methods in this class. But it's a little difficult to discern where to go next because our behavior is pushed down into methods.

Which brings us to our next refactoring step: Defactoring!

### Defactor before refactor

Defactoring technically is still refactoring, but it involves reversing a refactoring. It's an "undo", but a logical undo, not necessarily a reverting of a commit. Because our code could have changed since we did a refactoring, we're not necessarily guaranteed that a `git revert` will safely work. Instead, we need to perform some reversals of our previous refactorings:

*   [Extract Method](https://www.refactoring.com/catalog/extractFunction.html?ref=jimmybogard.com) -> [Inline Method](https://www.refactoring.com/catalog/inlineFunction.html?ref=jimmybogard.com)
*   [Extract Variable](https://www.refactoring.com/catalog/extractVariable.html?ref=jimmybogard.com) -> [Inline Variable](https://www.refactoring.com/catalog/inlineVariable.html?ref=jimmybogard.com)
*   [Extract Class](https://refactoring.com/catalog/extractClass.html?ref=jimmybogard.com) -> [Inline Class](https://refactoring.com/catalog/inlineClass.html?ref=jimmybogard.com)
*   [Introduce Field](https://www.jetbrains.com/help/resharper/Refactorings__Introduce_Field.html?ref=jimmybogard.com) -> [Inline Field](https://www.jetbrains.com/help/resharper/Refactorings__Inline_Field.html?ref=jimmybogard.com)
*   [Introduce Parameter](https://www.jetbrains.com/help/resharper/Refactorings__Introduce_Parameter.html?ref=jimmybogard.com) -> [Inline Parameter](https://www.jetbrains.com/help/resharper/Refactorings__Inline_Parameter.html?ref=jimmybogard.com)

> Most refactoring tools give you the refactorings on the left. Very few give the ones on the right. In my experience, both directions are equally important to be able to effectively refactor code

For us, we mainly used the Extract Method refactoring, so let's instead perform a defactor and inline those two methods. I place my carat on the method and tell ReSharper to inline the method:

![](https://jimmybogardsblog.blob.core.windows.net/jimmybogardsblog/images/2021/8/51339_image.png)

Inline Method dialog

And ReSharper will find ALL usages of this method and replaces the usages with the contents of this method, fixing all the parameters with values passed in. After my defactoring, the code in question is now:

```
// Calculate expiration date
var dateExpiring = offerType.ExpirationType switch
{
    ExpirationType.Assignment => DateTime.Today.AddDays(offerType.DaysValid),
    ExpirationType.Fixed => offerType.BeginDate?.AddDays(offerType.DaysValid) ??
                            throw new InvalidOperationException(),
    _ => throw new ArgumentOutOfRangeException(nameof(offerType))
};

// Assign offer
var offer = new Offer
{
    MemberAssigned = member,
    Type = offerType,
    Value = value,
    DateExpiring = dateExpiring
};
member.AssignedOffers.Add(offer);
member.NumberOfActiveOffers++;
```

Now that I've got my code defactored, we can now focus on our next step: pushing the behavior DOWN into our domain model.

### Pushing behavior down

Although my last step was defactoring, I still like to perform one more refactoring to figure out where this code should go: Extract Method. Instead of each commented part, let's instead refactor that entire block of code into a single method, mainly so that we can isolate direct and indirect inputs and outputs. Our extracted method is:

```
private static Offer AssignOffer(Member member, OfferType offerType, int value)
{
    var dateExpiring = offerType.ExpirationType switch
    {
        ExpirationType.Assignment => DateTime.Today.AddDays(offerType.DaysValid),
        ExpirationType.Fixed => offerType.BeginDate?.AddDays(offerType.DaysValid) ??
                                throw new InvalidOperationException(),
        _ => throw new ArgumentOutOfRangeException(nameof(offerType))
    };

    var offer = new Offer
    {
        MemberAssigned = member,
        Type = offerType,
        Value = value,
        DateExpiring = dateExpiring
    };
    member.AssignedOffers.Add(offer);
    member.NumberOfActiveOffers++;
    return offer;
}
```

Our handler is now quite compact:

```
public async Task<Unit> Handle(
    AssignOfferRequest request, 
    CancellationToken cancellationToken)
{
    var member = await _appDbContext.Members
        .FindAsync(request.MemberId, cancellationToken);
    var offerType = await _appDbContext.OfferTypes
        .FindAsync(request.OfferTypeId, cancellationToken);

    var value = await _offerValueCalculator.CalculateOfferValue(
        member, 
        offerType, 
        cancellationToken);

    var offer = AssignOffer(member, offerType, value);

    await _appDbContext.Offers.AddAsync(offer, cancellationToken);
    await _appDbContext.SaveChangesAsync(cancellationToken);

    return Unit.Value;
}
```

Back on our original extracted method, we can see that this method is now static, meaning it has no indirect inputs (no static or instance fields that it accesses), and no indirect outputs either. It's not exactly a pure function but I can reason about the behavior since it only operates on the direct inputs.

The next thing I look for are code smells. In a method like this that only operates on the parameters, the most typical code smell I find is [Feature Envy](https://refactoring.guru/smells/feature-envy?ref=jimmybogard.com). You have a set of code that mainly deals with data owned by other objects.

In the extracted method, I can see a few objects being interacted with:

*   Member
*   OfferType
*   Offer

Member seems to be the primary actor here, with two values set. OfferType is secondary, just used to calculate a final value. Finally there's Offer, which is a return value. If we're looking to push this behavior down to one of our domain objects, it would be either Member or Offer. Offer doesn't seem quite right because it's merely constructed and assigned, whereas Member is the target of the action.

One way to approach this is to simply try the refactoring both ways, and see which one "feels" right. Our tools let us do this safely and easily.

However, there can be a method to the madness, and I look at it as an exercise in describing the overall action/behavior. (A User) Assigns an Offer to a Member. Here, the Member is the noun receiving the action of the verb, the transitive object, while Offer is the direct object (User being the subject). A User Assigns an Offer. To whom? A Member.

The "whom" of the sentence is the object on which the action is performed, and a great candidate for where the method should reside because a method on an object captures "performing an action on a subject". Grade-school grammar aside, I look for "Whom" to guide me. Or just try both ways, but it would be a bit weird that constructing an Offer would do so much work - calculating values, assigning them to a member and so on.

Regardless, we've got a method and we want to move it to another type, the [Move Method](https://www.refactoring.com/catalog/moveFunction.html?ref=jimmybogard.com) refactoring. I'm going to use a special version of this refactoring with ReSharper, [Make Method Non-Static](https://www.jetbrains.com/help/resharper/Refactorings__Make_Method_Non-Static.html?ref=jimmybogard.com), which will move this method to one of the method parameters I specify, converting the method to instance along the way:

![](https://jimmybogardsblog.blob.core.windows.net/jimmybogardsblog/images/2021/8/5167_image.png)

Make Method Non-Static dialog with parameter choices for member and offerType

Clicking Next, my handler gets updated from a static to instance usage:

```
var value = await _offerValueCalculator.CalculateOfferValue(
    member, 
    offerType, 
    cancellationToken);

var offer = member.AssignOffer(offerType, value);
```

And the `AssignOffer` method moved and updated as well to `Member`:

```
public Offer AssignOffer(OfferType offerType, int value)
{
    var dateExpiring = offerType.ExpirationType switch
    {
        ExpirationType.Assignment => DateTime.Today.AddDays(offerType.DaysValid),
        ExpirationType.Fixed => offerType.BeginDate?.AddDays(offerType.DaysValid) ??
                                throw new InvalidOperationException(),
        _ => throw new ArgumentOutOfRangeException(nameof(offerType))
    };

    var offer = new Offer
    {
        MemberAssigned = this,
        Type = offerType,
        Value = value,
        DateExpiring = dateExpiring
    };
    AssignedOffers.Add(offer);
    NumberOfActiveOffers++;
    return offer;
}
```

What's great is by making this method non-static, ReSharper updated all of the usages to use the instance properties of the `Member` object automatically. Now this method, the bulk of the behavior, is able to be easily unit tested without mocks or stubs or anything like that! We took a standard code smell - feature envy - and used it to move our behavior to the object receiving the action.

Domain-Driven refactoring is exactly this - taking behavior at the edges of our application, and pushing them down into our domain model.

In the next post, we'll look at hardening up our domain model to ensure we properly encapsulate access to our data.
