---
url: "http://www.mikeperham.com/2015/12/14/how-to-test-multithreaded-code"
captured_at: "2015-12-23T13:15:34-03:00"
title: "How to Test Multithreaded Code"
domain: "mikeperham-com"
---

# How to Test Multithreaded Code

Dec 14, 2015 • Mike Perham

![TangledMess.png](mikeperham-com--how-to-test-multithreaded-code/ff0e2635decc88d66fe69968452c54d7.png)

Multithreaded code is hard to write and even harder to test.
Since much of my work is dedicated to making Ruby
threading easier for my users and customers, I thought some might be
interested in the patterns I’ve developed to make multithreaded code as simple
and testable as possible.

## Separate Threading from Work

> If you can’t test a big block of code, break it into a set of smaller testable pieces.

[Sidekiq::Processor](https://github.com/mperham/sidekiq/blob/master/lib/sidekiq/processor.rb#L24) is an object which is designed to run in its own
thread and doesn’t have any public API aside from starting/stopping the
thread.

```
  SidekiqProcessor
start
```

Interally it has quite a bit of complexity - think of it like an iceberg.
In order to test those complex internals, I make its [internal API public](https://github.com/mperham/sidekiq/blob/master/lib/sidekiq/processor.rb#L62) so that the test suite has full
access to the methods. The `start` method spins up a thread which calls a very simple `run` loop similar this:

```
  while @done
      fetch
    process
```

I’ve kept the run method as simple as possible since we can’t call it in
the test suite but we can call `fetch` and `process` in order to test them:

```
 test_process_fake_job
    SidekiqProcessor
  result  processsome_fake_job
  # asserts...
```

In this case, I’ve kept the thread management code as simple as
possible and pushed as much of the code complexity into separate methods
which can be called directly by the test suite and deterministically
verified.

How do I test the thread management code? Simple: in some cases I don’t. 100% test
coverage is for fundamentalists. Keep the code simple, verify it
manually and then don’t change it. Code complexity leads to churn which
leads to bugs. Since most of the complexity in Sidekiq::Processor is in the `process` and
`fetch` methods, they are most likely to change so we test those methods directly.

## Use Callbacks

If you must test multithreaded code, you’ll want to design testability
into the API. Ever seen or written a test littered with `sleep` calls?
We’ve all been there but you can test threaded code without sleep calls, I swear!
Generally the pattern is:

1. Start the other thread
2. Tell the other thread to process something
3. Wait for the result
4. Assert results

Most people don’t know how to do (3) properly so they use `sleep` as a
hack. Here’s a complete example of how to do it in Ruby:

```
require 'thread'

# We want to test Upcaser by exercising its full API,
# including the internal threading.
class Upcaser
  Request  Struct:args :block

   initialize
    @queue  Queue
  

   start
    @thread  Threadmethod
  

   process block
    @queue << Request block
    
  

   terminate
    @queue << 
  

  private

   
     
        @queue
      break unless 
      # perform the actual work
      result  upcase
      # call the block with the result
      blockresult
    
  

 test_upcaser
    Mutex
    ConditionVariable

    Upcaser
  # Step 1
  # tell Upcaser to start its internal thread
  start

  results  

  # the main thread will lock the mutex so it can pass data
  # to Upcaser and then wait for the results
  synchronize 

    # Step 2
    # pass "something" to Upcaser for its internal thread to process
    # the internal thread must call the block with results when done
    process"something"  
      results  
      synchronize 
        signal
      
    

    # Step 3
    # the main thread will wait here for Upcaser's thread to finish.
    
  

  # Step 4
  # assert whatever you want about the results
  assert_equal "SOMETHING" results

  # shut down Upcaser's internal thread
  terminate
```

The “trick” is the callback block passed to the `process` method. That callback
will save the results and unlock the main thread once Upcaser’s thread is finished processing. If your API
exposes a similar callback mechanism, it can be properly tested across threads.

I hope this helps people untangle some of their messy threading. Got any other
patterns for making threading easier to manage? Please link to them in
the comments.
