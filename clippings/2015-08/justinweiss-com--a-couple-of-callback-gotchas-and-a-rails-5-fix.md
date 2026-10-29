---
url: "http://www.justinweiss.com/blog/2015/03/10/a-couple-callback-gotchas-and-a-rails-5-fix"
captured_at: "2015-08-03T20:49:57-03:00"
title: "A couple of callback gotchas (and a Rails 5 fix) - Weissblog"
domain: "justinweiss-com"
---

# A Couple of Callback Gotchas (and a Rails 5 Fix)

[ActiveRecord callbacks](http://guides.rubyonrails.org/active_record_callbacks.html) are an easy way to run code during the different stages of your model’s life.

For example, say you have a Q&A site, and you want to be able to search through all the questions. Every time you make a change to a question, you’ll want to index it in something like [ElasticSearch](http://www.elasticsearch.org/). Indexing takes a while and isn’t urgent, so you’ll do it in the background with [Sidekiq](http://sidekiq.org/).

**This seems like the perfect time to use an `after_save` callback!** So in your model, you’ll write something like:

app/models/question.rb

|  |
| --- |
| ``` class Question  ActiveRecord   after_save :index_for_search   private    index_for_search     QuestionIndexerJobperform_later ``` |

app/jobs/question\_indexer\_job.rb

|  |
| --- |
| ``` class QuestionIndexerJob  ActiveJob   queue_as :default    performquestion     # ... index the question ... ``` |

This works great! Or, at least, it seems to. **Until you queue a lot more jobs and see these errors show up:**

|  |
| --- |
| ``` 2015-03-10T05:29:02.881Z 52530 TID-oupf889w4 WARN: Error while trying to deserialize arguments: Couldn't find Question with 'id'=3 ``` |

Sure, Sidekiq will retry the job and it’ll probably work next time. But it’s still a little weird. **Why can’t Sidekiq find the question you just saved?**

## A race condition between processes

Rails calls `after_save` callbacks immediately after the record saves. **But that record can’t be seen by other database connections, like the one Sidekiq is using, until the database *transaction* is committed, which happens a little later.** This means there’s a chance that Sidekiq will try to find your question after you save it, but before you commit it. It can’t find your record, and it explodes.

This problem is so common that [Sidekiq has an FAQ entry about it](https://github.com/mperham/sidekiq/wiki/FAQ#why-am-i-seeing-a-lot-of-cant-find-modelname-with-id12345-errors-with-sidekiq). And there’s an easy fix.

Instead of `after_save`:

app/models/question.rb

|  |
| --- |
| ``` class Question  ActiveRecord   after_save :index_for_search ``` |

use [`after_commit`](http://guides.rubyonrails.org/active_record_callbacks.html#transaction-callbacks):

app/models/question.rb

|  |
| --- |
| ``` class Question  ActiveRecord   after_commit :index_for_search ``` |

**And your job won’t get queued until Sidekiq can see your model.**

So, when you queue a background job or tell another process about a change you just made, use `after_commit`. If you don’t, they might not be able to find the record you just touched.

## But there’s one more problem…

OK, you switched a bunch of your `after_save` hooks to use `after_commit` instead. Everything seems to work. Time to check it all in and go home, right?

First, you’ll want to run your tests:

test/models/question\_test.rb

|  |
| --- |
| ``` require 'test_helper' class QuestionTest  ActiveSupportTestCase    "A saved question is queued for indexing"      assert_enqueued_with QuestionIndexerJob        Questioncreatetitle "Is it legal to kill a zombie?" ``` |

|  |
| --- |
| ```   1 Failure: QuestionTest#test_A_saved_question_is_queued_for_indexing /Users/jweiss/Source/testapps/after_commit/test/models/question_test.rb:7: No enqueued job found with :job>QuestionIndexerJob ``` |

Whoops! Shouldn’t the test have queued the job? **What just happened there?**

By default, [Rails wraps each test case in its own database transaction](http://api.rubyonrails.org/classes/ActiveRecord/FixtureSet.html). This can really speed things up. It takes just one database command to undo all the changes you made during the test.

But this also means your `after_commit` callback won’t run. **Because `after_commit` callbacks only run when the *outermost* transaction has been committed.**

When you call `save` inside a test case, it still commits a transaction (more or less), but that’s the *second-most-outermost* transaction now. So your `after_commit` callbacks won’t run when you expect them to. And you can’t test what happens inside them.

This problem also has an easy fix. Include the [`test_after_commit`](https://github.com/grosser/test_after_commit) gem in your Gemfile:

Gemfile

|  |
| --- |
| ``` group :test     "test_after_commit" ``` |

**And your `after_commit` hooks will run after your *second-to-last* transaction commits.** Which is what you were expecting to happen.

You might be thinking, “That’s weird. Why do I have to use a whole separate gem to test a callback that comes with Rails? Shouldn’t it just happen automatically?”

You’re right. It is weird. But it won’t stay weird for long.

Once Rails 5 ships, you won’t have to worry about `test_after_commit`. [Because this problem was fixed in Rails about a month ago](https://github.com/rails/rails/pull/18458).

---

In my own code, I use `after_commit` a lot. I probably use it more than I use `after_save`! But it hasn’t come without its problems and strange edge cases.

**Version by version, though, it’s getting better.** And when you use `after_commit` in the right places, a lot of weird, random exceptions just won’t happen anymore.

#### Did you like this post? You should read these:

Posted by Justin Weiss
 
[rails](http://www.justinweiss.com/blog/categories/rails/), [software development](http://www.justinweiss.com/blog/categories/software-development/)

Follow me on twitter:
