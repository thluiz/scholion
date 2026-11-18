---
url: "https://blog.ploeh.dk/2025/08/04/testing-races-with-a-synchronizing-decorator"
captured_at: "2026-11-18T11:09:31+00:00"
title: "Testing races with a synchronizing Decorator"
domain: "blog-ploeh-dk"
---

_Synchronized database reads for testing purposes._

In a previous article, you saw how to use a [slow Decorator to test for race conditions.](https://blog.ploeh.dk/2025/06/02/testing-races-with-a-slow-decorator) Towards the end, I discussed how that solution is only near-deterministic. In this article, I discuss a technique which is, I think, properly deterministic, but unfortunately less elegant.

In short, it works by letting a [Decorator](https://en.wikipedia.org/wiki/Decorator_pattern) synchronize reads.

### The problem [#](#867f586443864351a77bbeb8d2e00859)

In the previous article, I used words to describe the problem, but really, I should be showing, not telling. Here's a variation on the previous test that exemplifies the problem.

\[Fact\]
public async Task NoOverbookingRace()
{
    var date = DateTime.Now.Date.AddDays(1).AddHours(18.5);
    using var service = new RestaurantService();
    using var slowService =
        from repo in service
        select new SlowReservationsRepository(TimeSpan.FromMilliseconds(100), repo);

    var task1 = slowService.PostReservation(new ReservationDtoBuilder()
        .WithDate(date)
        .WithQuantity(10)
        .Build());
    await Task.Delay(TimeSpan.FromSeconds(1));
    var task2 = slowService.PostReservation(new ReservationDtoBuilder()
        .WithDate(date)
        .WithQuantity(10)
        .Build());
    var actual = await Task.WhenAll(task1, task2);

    Assert.Single(
        actual,
        msg => msg.StatusCode == HttpStatusCode.InternalServerError);
    var ok = Assert.Single(actual, msg => msg.IsSuccessStatusCode);
    // Check that the reservation was actually created:
    var resp = await service.GetReservation(ok.Headers.Location);
    resp.EnsureSuccessStatusCode();
    var reservation = await resp.ParseJsonContent<ReservationDto\>();
    Assert.Equal(10, reservation.Quantity);
}

Apart from a single new line of code, this is is identical to the test shown in the previous article. The added line is the `Task.Delay` between `task1` and `task2`.

What's the point of adding this delay there? Only to _demonstrate_ a problem. That's one of the situations I described in the previous article: Even though the test starts both tasks without awaiting them, they aren't guaranteed to run in parallel. Both start as soon as they're created, so `task2` is going to be ever so slightly behind `task1`. What happens if there's a delay between the creation of these two tasks?

Here I've explicitly introduced such a delay for demonstration purposes, but such a delay could happen on a real system for a number of reasons, including garbage collection, thread starvation, the OS running a higher-priority task, etc.

Why might that pause matter?

Because it may produce [false negatives](https://en.wikipedia.org/wiki/False_positives_and_false_negatives). Imagine a situation where there's _no_ transaction control; where there's no [TransactionScope](https://learn.microsoft.com/dotnet/api/system.transactions.transactionscope) around the database interactions. If the pause is long enough, the tasks effectively run in sequence (instead of in parallel), in which case the system correctly rejects the second attempt.

This is even when using the `SlowReservationsRepository` Decorator.

How long does the pause need to be before this happens?

As described in the previous article, with a configured delay of 100 ms for the `SlowReservationsRepository`, creating a new reservation is delayed by 300 ms. This bears out. Experimenting on my own machine, if I change that explicit, artificial delay to 300 ms, and remove the transaction control, the test sometimes fails, and sometimes passes. With the above one-second delay, the test always passes, even when transaction control is missing.

You could decide that a 300 ms pause at just the worst possible time is so unlikely that you're willing to simply accept those odds. I would probably be, too. Still, [what to test, and what not to test](https://blog.ploeh.dk/2018/11/12/what-to-test-and-not-to-test) is a function of context. You may find yourself in a context where that's not good enough. What other options are there?

### Synchronizing Decorator [#](#702b62450cb24cdc95f384b15d80a07c)

What you _really_ need to reproduce the race condition is to synchronize the database reads. If you could make sure that the Repository only returns data when enough reads have been performed, you can deterministically reproduce the problem.

Again, start with a Decorator. This time, build into it a way to synchronize reads.

internal sealed class SynchronizedReaderRepository : IReservationsRepository
{
    private readonly CountdownEvent countdownEvent = new CountdownEvent(2);

    public SynchronizedReaderRepository(IReservationsRepository inner)
    {
        Inner = inner;
    }

    public IReservationsRepository Inner { get; }

Here I've used a [CountdownEvent](https://learn.microsoft.com/dotnet/api/system.threading.countdownevent) object to ensure that reads only progress when the countdown reaches zero. It's possible that more appropriate threading APIs exist, but this serves well as a proof of concept.

The method you need to synchronize is `ReadReservations`, so you can leave all the other methods to delegate to `Inner`. Only `ReadReservations` is special.

public async Task<IReadOnlyCollection<Reservation\>> ReadReservations(
    int restaurantId,
    DateTime min,
    DateTime max)
{
    var result = await Inner .ReadReservations(restaurantId, min, max);
    countdownEvent.Signal();
    countdownEvent.Wait();
    return result;
}

This implementation also starts by delegating to `Inner`, but before it returns the `result`, it signals the `countdownEvent` and blocks the thread by waiting on the `countdownEvent`. Only when both threads have signalled it does the counter reach zero, and the methods may proceed.

If we assume that, while the test is running, no other calls to `ReadReservations` is made, this guarantees that both threads receive the same answer. This will make both competing threads come to the answer that they can accept the reservation. If no transaction control is in place, the system will overbook the requested time slot.

### Testing with the synchronizing Repository [#](#008987e40f7e4d5baeda6b245d086a43)

The test that uses `SynchronizedReaderRepository` is almost identical to the previous test.

\[Fact\]
public async Task NoOverbookingRace()
{
    var date = DateTime.Now.Date.AddDays(1).AddHours(18.5);
    using var service = new RestaurantService();
    using var syncedService =
        service.Select(repo => new SynchronizedReaderRepository(repo));

    var task1 = syncedService.PostReservation(new ReservationDtoBuilder()
        .WithDate(date)
        .WithQuantity(10)
        .Build());
    var task2 = syncedService.PostReservation(new ReservationDtoBuilder()
        .WithDate(date)
        .WithQuantity(10)
        .Build());
    var actual = await Task.WhenAll(task1, task2);

    Assert.Single(
        actual,
        msg => msg.StatusCode == HttpStatusCode.InternalServerError);
    var ok = Assert.Single(actual, msg => msg.IsSuccessStatusCode);
    // Check that the reservation was actually created:
    var resp = await service.GetReservation(ok.Headers.Location);
    resp.EnsureSuccessStatusCode();
    var reservation = await resp.ParseJsonContent<ReservationDto\>();
    Assert.Equal(10, reservation.Quantity);
}

Contrary to using the slow Repository, this test doesn't allow false negatives. If transaction control is missing from the System Under Test (SUT), this test fails. And it passes when transaction control is in place.

### Disadvantages [#](#c261a239b7a44a819eed3d4526adefed)

That sounds great, so why not just do this, instead of using a delaying Decorator? Because, as usual, there are trade-offs involved. This kind of solution comes with some disadvantages that are worth taking into account.

In short, this could make the test more [fragile](http://xunitpatterns.com/Fragile%20Test.html). As shown above, `SynchronizedReaderRepository` makes a specific assumption. It assumes that it needs to synchronize exactly two parallel readers. One problem with this is that this may be coupled to exactly one test. If you had other tests, you'd need to write a new Decorator, or generalize this one in some way.

Another problem is that this makes the test sensitive to changes in the SUT. What if a code change introduces a new call to `ReadReservations`? If so, the `countdownEvent` may unblock the threads too soon. One such change may be that the SUT decides to also query for surrounding times slots. You might be able to make `SynchronizedReaderRepository` robust against such changes by keeping a dictionary of synchronization objects (such as the above `CountdownEvent`) per argument set, but that clearly complicates the implementation.

And even so, it doesn't protect against identical 'double reads', even though these may be less likely to happen.

This Decorator is also vulnerable to caching. If you have a read-through cache that wraps around `SynchronizedReaderRepository`, only the first query may get to it, which would then cause it to block forever. Perhaps, again, you could fix this with the [Wait](https://learn.microsoft.com/dotnet/api/system.threading.countdownevent.wait) overload that takes a timeout value.

That said, if you cache reads, the pessimistic locking that [TransactionScope](https://learn.microsoft.com/dotnet/api/system.transactions.transactionscope) uses isn't going to work. You could, perhaps, address that concern with optimistic concurrency, but that comes with its own problems.

### Conclusion [#](#d7dcb5c138e1451499f5c2c2162fb416)

You can address race conditions in various ways, but synchronization has been around for a long time. Not only can you use synchronization primitives and APIs to make your code thread-safe, you can also use them to deterministically reproduce race conditions, or to test that such a bug is no longer present in the system.

I don't want to claim that this is universally possible, but if you run into such problems, it's at least worth considering if you could take advantage of synchronization to reproduce a problem.

Of course, the implication is that you understand what the problem is. This is often the hardest part of dealing with race conditions, and the ideas described in this article don't help with that.
