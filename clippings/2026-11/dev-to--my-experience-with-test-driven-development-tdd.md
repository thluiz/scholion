---
url: "https://dev.to/russ/my-experience-with-test-driven-development-tdd-3fb5"
captured_at: "2026-11-16T00:51:33+00:00"
title: "My Experience With Test Driven Development (TDD)"
domain: "dev-to"
---

## [](#what-is-test-driven-development-tdd)What is Test Driven Development (TDD)?

[TDD](https://www.techopedia.com/definition/25850/test-driven-development-tdd) is a software development approach in which a test is written before writing the code. Once the new code passes the test, it is refactored to an acceptable standard. TDD ensures that the source code is thoroughly unit tested and leads to modularized, flexible and extensible code. It focuses on writing only the code necessary to pass tests, making the design simple and clear.

[Unlce Bob](http://butunclebob.com/ArticleS.UncleBob.TheThreeRulesOfTdd) has three rules for TDD:

1.  You are not allowed to write any production code unless it is to make a failing unit test pass.
2.  You are not allowed to write any more of a unit test than is sufficient to fail, and compilation failures are failures.
3.  You are not allowed to write any more production code than is sufficient to pass the one failing unit test.

* * *

## [](#my-experience)My Experience

**What I'm Working On**

I'm refactoring a project of mine to use SQL instead of NoSQL and I was going to do certain things a little differently so I decided to rewrite my whole backend.

**First Thoughts**

I was completely lost about where I needed to start because I was thinking "how could I reference something that doesn't exist?" but then I'm like "oh duh the test will fail so then I would need to create all those files to make the test pass".

**How I Immediately Broke The Rules**

I started by forking a boilerplate that I had created and created the basic files `.env`, `error-handler.js`, `logger.js`, `validate-bearer-token.js` and set up the test file. Looking back now I think I immediately broke rule #1 because I wasn't trying to pass any test and later on I corrected this by not creating files until I had a test asking for that file.

The next thing I proceeded to do was create my SQL files and get my schema's defined and add the correct `npm` packages to make my database connection work. I decided to define my schema before writing my test for it because I need to see what query strings I would be writing and have it all defined in one place so that I wouldn't be going back and forth on my tests. I believe this breaks rule #1 as well.

**My First Test**

My first test was simple and I was able to make it pass very easily. I was testing that my empty database responded with an empty array.

**My Second Test**

My second test would insert data into the database and it would respond with all the data that was just inserted. The test immediately failed because of a schema design flaw from my end. I had circular references in my tables. In the business table, I had this column: `address_id UUID REFERENCES address(business_id) NOT NULL UNIQUE` and in the address table I had this column `business_id UUID PRIMARY KEY REFERENCES business(business_id) NOT NULL`. This would require that both tables be created at the same time to even make the insertion possible.

I was thinking that my second test should be just as easy to make it pass but it showed me that I couldn't even design my schema correctly and I spent a lot of time rewriting and rethinking the design of my schema. It showed I still had a lot to learn about SQL schema design and I was able to learn a lot about schema design from the dev community on slack.

**The Tests After**

After I had defined my schema correctly, writing the tests after seemed so much easier and required less research on how to set things up correctly.

* * *

## [](#conclusion)Conclusion

I believe using TDD would have saved me a lot of time by not doing a lot of manual testing each time I made a change to my schema or code. The test will do the comparing for you and immediately tells you why it's failing.

Using the TDD approach allowed me to dictate how I wanted to see the response from the server and then writing and rewriting the code to make it pass. It showed me the areas that I was shallow on as a developer and it made me go out and learn more about that particular subject just so I could make my test pass.

TDD will immediately show you how well you know what the response should look like from the server. Still being an entry-level developer it has shown me that I still have a lot to learn about how Postgres responds and how it inserts data. Sometimes I had to `console.log` responses just so I could write the tests and know what to anticipate from the server.

I see the TDD approach very beneficial to helping entry-level developers become better developers and will make my best effort to continue using TDD in my projects.

* * *

**HELP WANTED:** I'm not much of a writer so if you know of good articles that helped you become a better blogger on dev.to please do share them with me in the comment section.
