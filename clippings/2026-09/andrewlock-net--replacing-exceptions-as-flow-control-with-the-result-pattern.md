---
url: "https://andrewlock.net/working-with-the-result-pattern-part-1-replacing-exceptions-as-control-flow/?ref=dailydev"
captured_at: "2026-09-23T17:41:55+01:00"
title: "Replacing Exceptions-as-flow-control with the result pattern"
domain: "andrewlock.net"
---

October 08, 2024 ~12 min read
C#
.NET CORE
Replacing Exceptions-as-flow-control with the result pattern

Working with the result pattern - Part 1

Share on: 
 
 
 
 
 

This is the first post in the series: Working with the result pattern.

Part 1 - Replacing Exceptions-as-flow-control with the result pattern (this post)
Part 2 - Safety and simplicity with LINQ
Part 3 - Adding more extensions to Result<T>
Part 4 - Is the result pattern worth it?

In this post I provide a worked example of going from using exceptions for flow-control to using a result pattern to avoid throwing exceptions. There are lots of similar posts out there (such as this one from Milan Jovanović or this one), but this post is intended primarily as a prelude to the more interesting posts in the series about how to improve working with the result pattern in practice!

Background: do we need another post about the result pattern?
The starting point: happy path handling only
Using exceptions for flow control
Using a basic result pattern
Making the result pattern safer
Summary
Background: do we need another post about the result pattern?

A while back, I saw a tweet from Jeremy Miller describing how he doesn't like the "Result pattern", and that he has been recommending people remove it from their codebase

Having followed Jeremy for a long time, and knowing his appreciation for minimal code and strong dislike of boilerplate code, I wasn't surprised. I can't deny I was a little disappointed though, as I've seen this pattern used to dramatically simplify code rather than introduce noise.

Note that I'm obviously not suggesting that would always be the case, just that it can.

Reading through Jeremy's replies there, his biggest gripe appears to be with people trying to thread Result<T> objects back through a mediator handler to then be interpreted by MVC (or similar) at a higher level, potentially adding a lot of additional abstraction and complexity on the way. I can't really comment on that, though I will point out that the Ardalis.Result and Ardalis.Result.AspNetCore packages from Steve Smith take this approach and are very popular.

For me, the main benefits of the result pattern are:

You don't need to use exceptions for normal control flow. Exceptions are relatively expensive performance-wise in .NET, so throwing thousands of exceptions is generally Bad™. You can still use exceptions for exceptional cases of course.
Using a Result object can make the API failure conditions more explicit, and can therefore sometimes be easier to reason about, and reduce the chance of incorrect usages.

The accusation that Result increases verbosity certainly can be true, and until we get native typed unions support in C# that's probably always going to be true to an extent. But in this series, I'm hoping to show how you can use Result types with LINQ to actually reduce clutter.

The starting point: happy path handling only

For this post I'm going to slowly refactor a hypothetical simple API which takes a login request from an external provider, validates it, and gets or creates a new user in an application. The details aren't important here, I just wanted to work with a method that performs some significant work, so we can more easily see what's going on.

The code below shows the UserProvisioningService which exposes the ProvisionUser() method. This method takes in some details that came from an external login request, and attempts to get or create a user account in the system. There's currently no error handling for now (and all the dependency methods are just stubs) but the method itself is pretty easy to read:

Copy
public class UserProvisioningService(CreateUserService createUserService)
{
    public UserAccount ProvisionUser(ExternalLoginInfo info)
    {
        // Attempt to fetch the claims associated with the provided info
        Claim[]? claims = GetClaimValues(info);

        // We've retrieved the claims based on the login info, but we can't
        // necessarily trust that, so validate and sanitize the claims
        Claim[]? validatedClaims = ValidateClaims(claims);

        // Now we have the claims, fetch the appropriate tenant ID based on the claims
        Guid tenantId = GetTenantId(validatedClaims);

        // Combine the tenantId and claims to create the provisioning request
        ProvisionUserRequest createRequest = CreateProvisionUserRequest(tenantId, validatedClaims);

        // Call the service to actually create the account.
        // Maybe this calls a database, or something else 
        var identityResult = createUserService.GetOrCreateAccount(createRequest);

        // Return the user
        return identityResult;
    }

    // Helper methods (just stubs)
    private Claim[]? GetClaimValues(ExternalLoginInfo loginInfo) => null;
    private Claim[]? ValidateClaims(Claim[]? claims) => claims;
    private Guid GetTenantId(Claim[]? claims) => Guid.NewGuid();
    private ProvisionUserRequest CreateProvisionUserRequest(Guid employerId, Claim[]? claims) => new();
}

// Helper types/services
public record ExternalLoginInfo;
public record ProvisionUserRequest;
public record UserAccount;

public class CreateUserService
{
    public UserAccount GetOrCreateAccount(ProvisionUserRequest request) => new();
}


For the most part, this code just assumes everything will be fine, but there's some hidden behaviour in the way of exceptions. What if the ValidateClaims stage can't find any valid claims, should we continue with the process? If not, the only way to "break out" of the chain is to return null or throw an exception. Similarly, will createUserService.GetOrCreateAccount() always succeed? Or do we need to handle exceptions there? What do we do in that situation?

Using exceptions for flow control

One of the common traps to fall into in this situation is using Exceptions for flow control. This is where you throw an exception as a way of "returning" from a method but without returning a value, breaking out of the normal method execution.

As an example, consider why you might add this to the previous example. What if the validatedClaims are empty, should we continue with the method? Probably not. Similarly, what if we can't retrieve a tenant ID, there's no point continuing right?

Using exceptions for flow control can seem attractive because it means you can throw different exceptions for different types of errors, and handle those in the calling method. That differs to the approach of returning null (for example), which tells you that something went wrong, but not what went wrong.

The following shows an example of how someone might address these concerns, using exceptions to break out of the normal method flow:

Copy
public class UserProvisioningService(CreateUserService createUserService)
{
    // No longer return UserAccount? as we throw if something is wrong
    public UserAccount ProvisionUser(ExternalLoginInfo info)
    {
        Claim[]? claims = GetClaimValues(info);
        if (claims is null)
        {
            // Throwing an exception instead of returning null
            throw new ValidationException("The info provided was not valid");
        }

        Claim[] validatedClaims = ValidateClaims(claims);
        if (validatedClaims.Length == 0)
        {
            // Throwing an exception instead of ignoring the issue
            throw new ValidationException("The claims provided were not valid");
        }

        var tenantId = GetTenantId(validatedClaims);
        if (tenantId == Guid.Empty)
        {
            // Using custom exceptions to "describe" the issue
            throw new UnknownTenantException(validatedClaims);
        }

        var createRequest = CreateProvisionUserRequest(tenantId, validatedClaims);
        var identityResult = createUserService.GetOrCreateAccount(createRequest);
        return identityResult;
    }
}


Using exceptions for flow control is "easy" to some extent:

You can throw an exception anywhere, arbitrarily "deep" into the method stacks.
You can create specialised exceptions to describe the error (e.g. UnknownTenantException in the example above).
You don't need to change your method signatures to use them.

There are downsides though:

Throwing exceptions for "normal" scenarios is expensive. When you throw an exception, the runtime has to do quite a lot of work to create the stack trace and to unwind the method stack as appropriate.
You need to remember to handle the exceptions in the calling code, but it's not clear from the method signature which types of exceptions you will need to handle.
Explicitly checking and throwing exceptions repeatedly is verbose.
If you want to provide "correct" semantic exceptions (e.g. UnknownTenantException) then you might need to wrap each method call with an exception handler before throwing the correct exception.

To expand on that last point, if GetTenantId() could sometimes throw other types of exceptions, you might need to wrap the call something like this:

Copy
Guid tenantId;
try
{
    tenantId = GetTenantId(validatedClaims);
}
catch (Exception ex)
{
    throw new UnknownTenantException(claims, ex);
}


Changing every method call inside ProvisionUser to use that pattern could get very verbose 😅

The result pattern is a general solution to the first two issues, by making the error cases explicit in the method signature.

Using a basic result pattern

Ok, in the next section I'm going to show pretty much the most basic version of a result pattern you could implement. Note that I'm not suggesting you roll your own Result<T> class; there's plenty of libraries out there that do this, and the .NET base class library might have its own implementation soon. This is purely so that you can see the basics of what it might look like to use the result pattern in place of exceptions.

First of all we'll see the Result<T> class. This is a simple type that can be in one of two states:

IsSuccess: true, in which case Value is defined and has a value, and Error is null.
IsSuccess: false, in which case Value is undefined and instead Error contains an exception.

A basic implementations might look something like this:

Copy
public class Result<T>
{
    // Success constructor
    private Result(T value)
    {
        IsSuccess = true;
        Value = value;
        Error = null;
    }

    // Failure constructor
    private Result(Exception error)
    {
        IsSuccess = false;
        Value = default;
        Error = error;
    }

    [MemberNotNullWhen(true, nameof(Value))]
    [MemberNotNullWhen(false, nameof(Error))]
    public bool IsSuccess { get; }
    public T? Value { get; }
    public Exception? Error { get; }

    // Helper methods for constructing the `Result<T>`
    public static Result<T> Success(T value) => new(value);
    public static Result<T> Fail(Exception error) => new(error);
    
    // Allow converting a T directly into Result<T>
    public static implicit operator Result<TSuccess>(TSuccess value) => Success(value);
}


Most practical Result<T> types will have way more to them than this, but it's sufficient for showing the basics. The following code shows how you might convert the previous exception-based flow handling to use the above simple result type.

Copy
public class UserProvisioningService(CreateUserService createUserService)
{
    // Note 👇 The return type has changed
    public Result<UserAccount> ProvisionUser(ExternalLoginInfo info)
    {
        // Each of the methods returns a `Result<T>` type which we can inspect
        Result<Claim[]> claims = GetClaimValues(info);
        if (!claims.IsSuccess)
        {
            // If the method call wasn't successful, we can return a "failed" Result<T> 
            return Result<UserAccount>.Fail(new ValidationException("The info provided was not valid"));
        }

        // Using Value to extract the T from the Result<T>      👇
        Result<Claim[]> validatedClaims = ValidateClaims(claims.Value);
        if (!validatedClaims.IsSuccess)
        {
            return Result<UserAccount>.Fail(new ValidationException("The claims provided were not valid"));
        }

        var tenantId = GetTenantId(validatedClaims.Value);
        if (!tenantId.IsSuccess)
        {
            return Result<UserAccount>.Fail(new UnknownTenantException(validatedClaims.Value));
        }

        var createRequest = CreateProvisionUserRequest(tenantId.Value, validatedClaims.Value);
        if (!createRequest.IsSuccess)
        {
            return Result<UserAccount>.Fail(new InvalidOperationException("Failed to create provision user request"));
        }

        return createUserService.GetOrCreateAccount(createRequest.Value);
    }

    // Each of the methods we called return a Result<T> which we check
    private Result<Claim[]> GetClaimValues(ExternalLoginInfo loginInfo) => Array.Empty<Claim>();
    private Result<Claim[]> ValidateClaims(Claim[] claims) => claims;
    private Result<Guid> GetTenantId(Claim[] claims) => Guid.NewGuid();
    private Result<ProvisionUserRequest> CreateProvisionUserRequest(Guid employerId, Claim[] claims)
        => new ProvisionUserRequest(); // 👈 Relying on the implicit conversion from T to Result<T>


The above code shows the basics of how a Result<T> type could replace using exceptions for flow handling, but it's not a great example of the pattern, for many reasons:

The overall flow of the code is still hard to follow, with lots of verbose "check and return" statements.
The "error" type is still a generic "Exception" which is an unbounded possibility of values.
We're checking IsSuccess before accessing Value in the above example, but there's nothing stopping you accessing Value or Error "incorrectly", at which point you will likely get a "real" NullReferenceException!

Frankly, the only real benefit we have here is that callers of ProvisionUser can easily see from the method signature that the method is "expected" to fail for some subset of cases, given that it now returns a Result<UserAccount> instead of UserAccount. Is that worth the tradeoff? Maybe, but probably not for this implementation. If this was what the result pattern always looked like, it would be very hard to recommend.

But we don't have to stop here. With one small change we can address the final point above, and make our types "safe" so you can't accidentally call Value or Error.

Making the result pattern safer

The Result<T> pattern in the previous section is slightly problematic in that it doesn't stop you trying to access the Value (or Error) property when you shouldn't. As a guard around this, many Result<T> implementations don't expose these properties directly. Instead, you have a Switch() method (sometimes called Match() or various other names).

The Switch() method works a bit like a switch statement or switch expression; you provide a method to run in each possible case for a given Result<T> object:

If the Result<T> has a value, you provide a Func<T> which is passed the value
If the Result<T> has an error, you provide a Func<Exception> which is passed the error.

There are also variations where you provide a Func<T, TReturn> and return a value. That's the version I show in the example below (the reason why will become clear soon):

Copy
public class Result<T>
{
    // We don't expose these publicly any more
    private readonly T? _value;
    private readonly Exception? _error;

    // Same constructors
    private Result(T value)
    {
        IsSuccess = true;
        _value = value;
        _error = null;
    }

    private Result(Exception error)
    {
        IsSuccess = false;
        _value = default;
        _error = error;
    }
    
    [MemberNotNullWhen(true, nameof(_value))]
    [MemberNotNullWhen(false, nameof(_error))]
    private bool IsSuccess { get; }

    // This Method takes two Func<T>, one for the success case and one for the error case
    public Result<TReturn> Switch<TReturn>(
        Func<T, TReturn> onSuccess,
        Func<Exception, Exception> onFailure)
    {
        if (IsSuccess)
        {
            // If this result has a value, run the success method,
            // which returns a different value, and then we create a
            // Result<TReturn> from it (implicitly)
            var result = onSuccess(_value);
            return result;
        }
        else
        {
        {
            // If this result is an error, run the error method
            // to allow the user to manipulate/inspect the error.
            // We then create a new Result<TReturn> result object
            // from the error it returns
            var err = onFailure(_error);
            return Result<TReturn>.Fail(err);
        }
    }

    public static Result<T> Success(T value) => new(value);
    public static Result<T> Fail(Exception error) => new(error);
    public static implicit operator Result<T>(T value) => Success(value);
}


Ok, we have our "safe" Result<T> class, which enforces that we can't access Value if it's not available. But what does it look like to use this in code?

Well, the bad news is, it's kind of horrible 😅 I've annotated the below code best I can, but the reality is that even though the code is guaranteed to block certain types of errors by encapsulating the IsSuccess checking, it's just awful to read…

Copy
public class UserProvisioningService(CreateUserService createUserService)
{
    public Result<UserAccount> ProvisionUser(ExternalLoginInfo info)
    {
        // 1. Try to get the initial claim results
        Result<Claim[]> claimsResult = GetClaimValues(info);

        return claimsResult.Switch(
            onSuccess: claims => // if the claims we retrieved successfully, run this function
            {
                // 2. Try to validate the claims
                Result<Claim[]> validatedClaimsResult = ValidateClaims(claims);
                return validatedClaimsResult.Switch(
                    onSuccess: validatedClaims =>  // validation was successful
                    {
                        // 3. Try to extract the tenant ID
                        Result<Guid> tenantIdResult = GetTenantId(claims);
                        return tenantIdResult.Switch(
                            onSuccess: tenantId => // extracted successfully
                            {
                                // 4. Create the ProvisionUserRequest object
                                Result<ProvisionUserRequest> createRequestResult =
                                    CreateProvisionUserRequest(tenantId, validatedClaims);
                                return createRequestResult.Switch<Result<UserAccount>>(
                                    onSuccess: createRequest => // created the request successfully
                                    {
                                        // 5. Try to create the account, and return the Result<UserAccount>
                                        return createUserService.GetOrCreateAccount(createRequest);
                                    },
                                    onFailure: ex => Result<UserAccount>.Fail(ex)); // Step 4 failed, return the error 
                            },
                            onFailure: ex => Result<UserAccount>.Fail(ex)); // Step 3 failed, return the error 

                    },
                    onFailure: ex => Result<UserAccount>.Fail(ex)); // Step 2 failed, return the error 
            },
            onFailure: ex =>  Result<UserAccount>.Fail(ex)); // Step 1 failed, return the error 
    }

    private Result<Claim[]> GetClaimValues(ExternalLoginInfo loginInfo) => Array.Empty<Claim>();
    private Result<Claim[]> ValidateClaims(Claim[] claims) => claims;
    private Result<Guid> GetTenantId(Claim[] claims) => Guid.NewGuid();
    private Result<ProvisionUserRequest> CreateProvisionUserRequest(Guid employerId, Claim[] claims) => new ProvisionUserRequest();
}


This code is really hard to follow. There's the ever increasing indentation (the pyramid of doom) caused by (effectively) lots of nested if statements. The error case arguments (onFailure) are a long way from the matching (onSuccess) arguments, which makes it hard to match them up. And what's more, the error cases aren't doing anything other than re-wrapping the exception from a failed Result<T> type into a Result<TReturn>.

Note that because they'll be built into the language, the type-unions proposal uses switch statements and expressions rather than a Switch method, but functionally it works in the same way.

The very repetitive nature of the code above is exactly the sort of boilerplate and cruft that Jeremy Miller often rails against, and is the sort of thing I hope he's referring to in his original post. The good news is that we don't have to stop there—in the next post we'll make all that cruft disappear!

Summary

In this post I provided a brief motivation for using the result pattern in applications to avoid using exceptions for flow control. I started with a simple implementation without any error checking, then added exceptions to handle error cases. Unfortunately using Exceptions for common error cases can be very slow and means the caller has to remember to catch those exceptions.

As a "solution" to exceptions, I replaced the Exceptions with a Result<T> type and the result pattern. For safety, we enforced that you had to use a Switch() method to "extract" the result. Unfortunately, this made the final code incredibly cumbersome and verbose, so in the next post we'll see how we can simplify it significantly!
