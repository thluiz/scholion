---
url: "https://dev.to/marcinwosinek/how-to-write-unit-tests-52dl"
captured_at: "2022-04-14T09:17:31-03:00"
title: "How to write unit tests - DEV Community 👩‍💻👨‍💻"
domain: "dev-to"
---

# DEV Community ‍‍

As a beginner programmer, you often hear advice to test your code. It’s good advice—let’s look at how you can start doing it!

## What are unit tests

Tests are a way to explicitly set expectations about code. You establish them to allow the machine to check whether your code meets the expectations.

It’s a program that verifies your program.

Usually, in JavaScript projects, you’ll use some testing library, such as:

- Jest,
- Jasmine, or
- Chai

But those are just tools. What matters is that you have some way of automatically validating your application.

[![rfdbcv96lv4nobcgub5h.jpg](dev-to--how-to-write-unit-tests-dev-community/40094311ef13d9014a412eec267f4310.jpg)](https://res.cloudinary.com/practicaldev/image/fetch/s--I3riIaKK--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/rfdbcv96lv4nobcgub5h.jpg)

## How unit tests help you

There are four ways writing tests will make your coding life easier:

1. It’s a fast and reliable way of checking whether the code works as expected. You don’t have to think about edge cases to have all of them covered by unit tests.
2. Good test coverage is a safety net that allows you to refactor code with more courage. Thus, you’re more likely to take the necessary steps to keep your codebase in good shape.
3. Writing *unit* tests forces you to think about units—and how the responsibility should be spent between them, making your code more modular and easier to maintain.
4. Unit tests can make you a faster coder. At first, you have to invest time in creating the test case, but once it’s ready, you can rerun it very cheaply. The investment can pay dividends even during the initial development.

## Build up scaffolding

Before testing functionality, make sure you can test *anything*. Install the testing library and set up your testing script. Once you have something running, you can start setting up scaffolding for some of your tests. You need to decide on a naming convention. For example, if your code is `my-project/plane-ticket.js`, your testing code can be sitting in `my-project/plane-ticket.spec.js`.

Build everything needed to test a given class, and then check some trivial aspects:

- if an object is an object, or
- if a function is a function

In this way, you will prove that you can test things.

## Set up mocking

Mocks are objects created to replace dependencies of the unit you are testing. For example, if you test the `saveBlogPost` function, you will want to intercept the HTTP request before the function sends it. You will want to find what your function uses for sending the request and replace it with a mock. Mocking should be easy if you build your code using a dependency injection pattern.

[![suc0wipicw2v6vu4iq03.jpg](dev-to--how-to-write-unit-tests-dev-community/ca64332946a228c6a4cbc678c41c8d60.jpg)](https://res.cloudinary.com/practicaldev/image/fetch/s--wJod7OJd--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/suc0wipicw2v6vu4iq03.jpg)

## Keep a structure

As you can see, a lot is going on in each test. You can distinguish three main phases:

1. Setting up mocks
2. Running code you want to check
3. Check expectations

Keeping this separation in your code makes sense; it will be easier to read this way. An easy way of organizing it is to group all lines together and maybe add a comment saying which part it is.

## Test-driven development

Test-driven development is a common approach to creating nice code with good test coverage. You start with adding a test for a function before there is an implementation for it. You run tests, and it should fail—if not, there is something seriously wrong and you need to investigate it. The tests fail, and you add the missing implementation to the code. Again, the expectation is that this alone will fix the failure. If all goes well, you invest a bit of time in improving your solution—on both the code and test side, without changing the logic. This way allows you to [iterate](https://how-to.dev/how-to-make-small-steps-go-a-long-way) quickly in creating the code and its tests.

If you follow this practice, you should never miss any tests for your logic. There is no temptation to skip writing tests—a common issue when you leave writing tests at the end of your sprint.

[![q1qqzirnlc3vo5hezyib.jpg](dev-to--how-to-write-unit-tests-dev-community/9e32cf59cb6e6ea3c7bac00ecae9493d.jpg)](https://res.cloudinary.com/practicaldev/image/fetch/s--Fuo1iH5X--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/q1qqzirnlc3vo5hezyib.jpg)

### Counter-recommendation

To lead, you have to know where you are going. Ignore the tests for a while if you need to explore what solutions are doable. Once you have your path clear, you can either add tests or approach the problem again in a test-driven way.

## Missing tests

If you are unlucky, you might be working with legacy code without tests and any other quality-related measures—something like [I describe here](https://how-to.dev/how-to-manage-fragile-legacy-code). In such a case, it’s still better late than never; you can start writing tests as you work on the codebase. In this way, you will be improving the situation for the future, and maybe you will find some nasty bugs hidden in some rare edge cases.

## How about you?

How difficult do you find learning how to test? I’ve seen complaints online from people who struggle to find good resources for it. Let me know what experiences you have had so far.
