---
url: "https://michaelfeathers.silvrback.com/a-monadic-approach-to-error-handling-in-collection-pipelines"
captured_at: "2015-02-20T00:04:07-03:00"
title: "Michael Feathers - A Monadic Approach to Error Handling in Collection Pipelines"
domain: "michaelfeathers-silvrback-com"
---

# A Monadic Approach to Error Handling in Collection Pipelines

February 16, 2015

If you read my last blog you know that I’ve been pushing the idea of chained computation rather far. It’s been fun to just try to use it for all of my utility programming to see where it breaks down. When you build a program as a single expression in a single sequential flow, one of the things that you have to deal with is making sure that you have all of the information you need at each stage of the pipeline. If you don’t organize your design well, you’ll be passing along extra arguments that you “kinda/sorta need later" - and that’s messy.

Error handling can be seen as a specific case of the extra arguments problem. If we want to write a piece of a program as a single flow we have to figure out what to do when something goes wrong. The easiest thing to do is pass an empty array to the next stage in the pipeline but what if we want to say more? We should be able to record an error message, or even a series of error messages when things go wrong.

Here’s the core of the guitar tablature program I described in my last blog.

```
 each_line
         split
          string tab_columnstring  
         transpose
```

It takes text files on the command line, breaks them into lines and then splits them into whitespace separated fields. Notice that the map operation makes the assumption that each line has two fields. The first is the number of a string on the guitar and the second is a fret number.

The way the program is written there are quite a few errors that could turn up in the input. We could have lines that do not have exactly two fields, the fields could be non-numeric, or the values of the fields could be out of their appropriate ranges. How should we handle this? We could throw exceptions from within the pipeline but that’s a rather coarse mechanism - once you detect the first error you’re done. It would be nice to have more control.

We can solve the problem by borrowing an idea from Haskell - the Either type. `Either’ allows you to keep track of two sets of values in a pipeline - the results you are producing and any errors you’ve seen along the way.

Here’s code for the pipeline using my hacked-up version of Either in Ruby:

```
each_line
    either
    split
    check"two fields per line"  count   
    check"two ints per line"       
    check"string # in [1..6]"    >=    <=  
    check"fret # in [0..24]"     >=    <=  
     string tab_columnstring  
    transpose
```

If any of the checks in the pipeline fail the pipeline records the error and all subsequent stages of the pipeline skip their computation. At the end of the calls we either have a list of errors or their results in the string that we produce.

This is not exactly the same as Either in Haskell but helps us achieve the same effect when we want to inline our error handling.

At this point I’m trying to find a better way to implement and generalize this. My current implementation monkey patches Enumerable and does some simple delegation.

```
module Enumerable
   either
    ErrorEnumerable.()
  

class ErrorEnumerable
   initialize 
    @enum = 
    @errors = []
  

   check error_message, &block
    @enum.each_with_index  |,line_no|
      unless yield 
        @errors << "expected #{error_message} on line #{line_no + 1}"
      
    
    
  

    &block
    in_error? ?  : ErrorEnumerable.(@enum.(&block))
  

   transpose
    in_error? ?  : ErrorEnumerable.(@enum.transpose)
  

    delimiter
    in_error? ? @errors.(delimiter) : @enum.(delimiter)
  

  private

   in_error?
     @errors.empty?
```

I’m sure that I’ll end up with something better than this. Right now, I just like the direction.
