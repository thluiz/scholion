---
url: "https://dev.to/ddarrko/how-to-write-more-testable-code-oi7"
captured_at: "2026-11-16T19:06:55+00:00"
title: "How to write testable code"
domain: "dev-to"
---

_This is something I put together for the engineering team at Howsy. Hopefully it will be of some assistance for others. The examples are in PHP but can be abstracted to any OOP language_

## [](#what-is-unit-testing)What is Unit Testing?

It’s simply a test that runs against an individual ‘unit’ or component of software. We are testing the smallest possible implementation of a class/method. A unit test does not rely on any dependencies (other classes/libraries or even the database)

Read more about unit testing [here](http://softwaretestingfundamentals.com/unit-testing/).

## [](#why-is-it-important)Why is it important?

I mean we could just stick with integration tests right? They are easy to write, however ...

The goal of any Software Project is to produce a maintainable, extensible codebase which meets business requirements. Writing effective unit tests help us to ensure we are writing SOLID code.

Read more about solid [here](https://scotch.io/bar-talk/s-o-l-i-d-the-first-five-principles-of-object-oriented-design).

## [](#how-can-we-write-more-testable-code)How can we write more testable code?

I have taken a very simple class and it is typical of some of the code I have seen over the years.  

```
class ToActive
{
    public function transition(int $accountId): void
    {
        $account = Account::find($accountId);
        if ($this->canTransition($accountId)) {
            $account->setState('active')->save();
        }
    }

    private function canTransition(Account $account): bool
    {
        $validator = new ToActiveValidator();

        if ($validator->validate($account)) {
            return true;
        }
        return false;
    }
}
```

Enter fullscreen mode Exit fullscreen mode

On the surface the class appears to work. It finds an account from the DB, calls a validation method in another class and returns true/false. Based on the result the Account may or may not be updated.

Although this class works it is **impossible to unit test** due to two different dependencies being instantiated rather than injected. The two offending pieces of code are  

```
$account = Account::find($accountId);
```

Enter fullscreen mode Exit fullscreen mode

```
$validator = new ToActiveValidator();
```

Enter fullscreen mode Exit fullscreen mode

As they are in the body of our methods they will be called during unit testing. This will cause us to rely on the responses from other classes in order to run a test. This makes any resulting tests we write for this class not true unit tests.

We can refactor this class very easily to make it more easily testable and therefore more extensible and loosely coupled.

## [](#refactoring)Refactoring

```
class ToActive
{
   private $account;
   private $validator;

   public function __construct(AccountInterface $account, StateTransitionValidatorInterface $validator)
   {
       $this->account   = $account;
       $this->validator = $validator;
   }

   public function transition(): void
   {
       if ($this->validator->validate($this->account)) {
           $this->account->setState('active')->save();
       }
   }
}
```

Enter fullscreen mode Exit fullscreen mode

As you can see from the above we are now injecting dependencies.

Our class does not care about the concrete implementation of the Account or the Validator - only that they adopt the required interfaces. This again makes our code more loosely coupled. In the future maybe we may completely change the StateTransitionValidator implementation or even add additional validators. Our code is now less tightly coupled and therefore more testable.

## [](#now-lets-get-to-testing)Now let’s get to testing

Looking at the class we have one public method. We should not be trying to test private methods as they are implementation details. If you find your class has too many private methods or feel that they need testing it is a sure fire sign that your class could do with splitting out into smaller components.

There are two paths within the public method - the validation passes and we save the entity or the validation does not pass and we don't save it.

I will write the test assuming the validation passes first. We are going to be mocking our dependencies (something not possible with the original class architecture).  

```

public function testToActiveWithPassingValidationShouldTransition()
{
   /** @var Mockery\MockInterface|Account $account */
   $account = Mockery::Mock(Account::class);
   $account->shouldReceive('setState')
       ->with('active')
       ->andReturn($account)
       ->once();
   $account->shouldReceive('save')
       ->andReturn($account)
       ->once();

   /** @var Mockery\MockInterface|ToNotActiveValidator $validator */
   $validator = Mockery::mock(ToActiveValidator::class);
   $validator->shouldReceive('validate')
       ->with($account)
       ->andReturn(true)
       ->once();

   $service = new ToActive($account, $validator);
   $service->transition();
}


public function testToActiveWithFailingValidationShouldNotTransition()
{
   /** @var Mockery\MockInterface|Account $account */
   $account = Mockery::Mock(Account::class);
   $account->shouldReceive('setState')
       ->with('active')
       ->andReturn($account)
       ->never();
   $account->shouldReceive('save')
       ->andReturn($account)
       ->never();

   /** @var Mockery\MockInterface|ToNotActiveValidator $validator */
   $validator = Mockery::mock(ToActiveValidator::class);
   $validator->shouldReceive('validate')
       ->with($account)
       ->andReturn(false)
       ->once();

   $service = new ToActive($account, $validator);
   $service->transition();
}

```

Enter fullscreen mode Exit fullscreen mode

## [](#breaking-it-down)Breaking it down

First of all we use [Mockery](https://github.com/mockery/mockery) to mock our account class.

We tell our mock that we will call the method setState with an argument of active. We also assert that this function will be called exactly once (this is our actual test assertion)  
We also assert that the save() method will be called exactly one time.

We also mock our concrete validator class. We tell our mock that the validate method shall be called once and that it will always return true.

The tests will pass and you can see we have done so without actually relying on our dependencies. These were mocked and injected into our class with all of their methods returning exactly what we defined in our test.

### [](#testing-the-reverse)Testing the reverse

We also want to test the second path (what if the validation returns false, business rules dictate we should therefor not transition the object)

Take a look at the second test and you can see our test is pretty similar only now we are forcing the validator to return false. As such our assertions have changed and we now expect setState and Save to never be called on our account object.

## [](#what-we-achieved)What we achieved

The original code was hard to test and tightly coupled. The refactor has allowed us to make the code more testable but a great side affect of this is that the code is also now more flexible.

Let me know if you have any questions in the comments!
