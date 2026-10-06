---
url: "https://sendgrid.com/blog/convince-company-go-golang/"
captured_at: "2015-04-20T09:13:14-03:00"
title: "How to Convince Your Company to Go With Golang"
domain: "sendgrid-com"
---

# How to Convince Your Company to Go With Golang

---

[March 6, 2014](https://sendgrid.com/blog/convince-company-go-golang/ "8:00 am")

Recently, SendGrid decided to move to using Go as its primary development language. This has been a long-standing internal battle, which I hear has happened and is continuing to happen in a number of organizations. I figured it would be productive to share our experience here, not just in why we chose to move forward with Go, but how this process played out, so that others in a similar situation can make a compelling argument for Go.

## Why We Needed a Change

For some background, the backend systems of SendGrid were primarily written in Perl/AnyEvent in the first years, moving to Python/Twisted later on. We looked into using the Gevent framework for Python, but during an inception meeting we realized it was just the same problems we had, dressed a different way. It wasn’t going to help solve our underlying challenges. At that point, we realized we needed to make a fundamental shift in our development language, and it boiled down to a contest between Scala, Java, and Go.

While many shops that have been using Java have moved to Scala for concurrency reasons, we felt that moving to a functional programming language was going to really up the learning curve. I’ve worked at a shop previously where we used a functional language. It was difficult to hire and train new people. From an academic perspective, I get it, but the reality is people have a very hard time thinking this way, and I’d rather our developers not be fighting our language. We’ve had enough of that using Perl.

## Why We Chose Go

Fundamentally, the biggest challenge that SendGrid faces in development is concurrent programming. While what we do isn’t rocket science, doing it at a scale of [over 500 million messages per day](http://venturebeat.com/2014/03/05/sendgrid-has-sent-out-almost-as-many-emails-as-mcdonalds-has-sold-burgers/) is extremely challenging (I’ve done rocket science, this is way harder). One of the most compelling reasons for using Go at SendGrid is having the concept of concurrent asynchronous programming as part of the language. The argument always came up that you can do asynchronous programming in Java, but it isn’t pretty. My argument was always that “We can keep doing it in Perl,” which usually helped people to understand that just because you can do something with a technology doesn’t mean its the best way to do it.

Another advantage for Go here was that a large number of our developers were excited about it, and had been experimenting on their own time with how to use it to solve SendGrid’s problems using it. Even after we’d decided to go with Python/Gevent and had told people we weren’t going to use Go here, they continued to pursue Go at home. Because of this, I was able to make the compelling argument that “Our people are already doing this in their free time. Would we rather that be something that benefits us or just them?”

## We Love Developers Who Love Go

Switching to Go is going to cost SendGrid in terms of initial development time, but if our engineers are excited enough to invest their own time to make this work, we feel it’s worth it. I also believe we’ll recoup that time in maintenance costs, which is usually way more than the time to develop a feature. A large portion of the issues that we’ve had to solve here have been because of concurrency issues, and a little time spent up front to avoid all that pain later is a good investment in my book.

One of the biggest arguments for Java was that there are a ton of engineers who already know it, so hiring should be easier. This is a tough thing to argue against. While the pool of Go developers is definitely smaller, from what I’ve seen, the people who are excited/knowledgeable about Go tend to be the developers who are truly interested in learning new things and pushing the envelope. These are the types of developers we want at SendGrid, and if choosing Go helps filter out candidates, great! And yes, shameless plug, [we are aggressively hiring](http://sendgrid.com/careers). [anexo ausente]

## How We’ll Overcome the Downsides

The hardest hurdle to overcome for Go was the library support. While Go can fairly easily integrate libraries written in C, Java has a very large base to draw on with less effort. As mentioned before, the majority of time SendGrid spends on problems is concurrency, not functionality that already exists elsewhere. That being said, even with libraries we’ve used in the past, we’ve run into major problems. I lost count long ago of the number of messages that deadlocked an open source library we used, and this cost us a ton of development time to fix/work around.

While library support is still a weakness for Go, I prefer to turn it into a strength by open sourcing libraries that we have to develop in Go. This benefits SendGrid in a couple of ways. First, if we can help build the community around Go, other developers will have an easier time switching to it, and we’ll be able to benefit from work they will open source. The other benefit is that as we become more well known in the Go community, more Go developers will know about us and our hiring process will improve. Did I mention we’re [hiring Go developers](http://sendgrid.com/careers)? [anexo ausente]

In the end, the decision for your own organization will have to be what is best for them. Hopefully, some of the reasons we’ve made the switch to Go will resonate with your company and can help convince people to give it a Go.
