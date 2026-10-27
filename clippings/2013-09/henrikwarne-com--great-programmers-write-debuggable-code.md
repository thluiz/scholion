---
url: "http://henrikwarne.com/2013/05/05/great-programmers-write-debuggable-code/"
captured_at: "2013-09-27T10:17:58-03:00"
title: "Great Programmers Write Debuggable Code | Henrik Warne's blog"
domain: "henrikwarne-com"
---

# **G**reat Programmers Write Debuggable Code

All programs need some form of logging built in to them, so we can observe what it is doing**.** This is especially important when things go wrong**.** One of the differences between a great programmer and a bad programmer is that a great programmer adds logging and tools that make it easy to debug the program when things fail**.**

When the program works as expected, there is often no difference in the quality of the logging**.** However, as soon as the program fails, or you get the wrong result, you can almost immediately tell the good programmers from the bad**.**

### Example 1: “Let’s make a debug version”

For example, a tester came to me with a call case that didn’t work**.** We looked at the logs, and saw that the problem seemed to be in a neighboring module**.** A call to the other module to get a list of values simply returned null**.** When we enabled logging in the neighboring module and re-ran the test case, there was no more information available**.** No clues to why null was returned – did we supply the wrong arguments, did some external system fail, was there an error in the neighboring module, or what**?**

When asking the developer responsible for the code, the answer we got was: “Oh, then we have to make a debug version to see what happens”**.** Fail**!** It must be possible to get some sense of where the problem is just from the logs**.** If this had been in a production system, adding a debug version would have been a lot of work**.** The code needs to include enough information in the log statements so you at least have some idea of why it fails**.**

### Example 2: Show Me How We Got Here

One of our products at work finds the cheapest route for the delivery of SMS:s (text messages) to mobile phones**.** Depending on the current location of the phone, and the operator the destination subscriber belongs to, there are many possible routes to choose from, each with a given cost and other characteristics**.**  In addition, there can be exceptions that forbid some routes, and promote other routes**.** There are typically many thousands of routes defined**.** The system finds the cheapest route in each case, given the constraints, and delivers the SMS.

Now, suppose a certain SMS gets delivered using route A, but we believe it should have used route B. Why was route A chosen**?** If there is no logging information (other than “route A was chosen”), we are left with hundreds of possible routes, their costs, the exceptions, and a complex algorithm**.** Good luck figuring out why A was chosen**.**

In our implementation, the log includes all potential routes, in cost order**.** As routes are eliminated due to different restrictions, the eliminated routes are listed in the log, together with the reason for elimination**.** With all the information on the input to the algorithm, as well as the steps taken, listed in the log, it is fairly easy to see why a certain route was picked**.**

### Why Not**?**

So, why don’t all programmers write debuggable code**?** I can think of three reasons:

1. You have to be humble enough to realize that there will be cases when your code doesn’t work as expected**.** I believe many programmers have a hard time with this**.**
2. If you test your own code thoroughly, you will make sure it works (or fails gracefully) in a lot of different scenarios**.** For each scenario, it is natural to add logging. If you don’t test those cases, you are less likely to add logging there**.**
3. Many programmers don’t trouble-shoot their own code in production systems often enough**.** If you have a problem in a live system, and the logs tell you nothing about why there is a problem, you have a strong incentive to add logging that will actually help you the next time you are in a similar situation**.**

### Is *Your* Code Debuggable**?**

There are of course cases where even good logging messages don’t give you the full story on why something fails**.** You may still have to make that debug version. But your regular logging should at the very least give you some hints on what the problem might be**.**

So, how well have you prepared? When your code fails, will the logs tell you what’s going on**?**
