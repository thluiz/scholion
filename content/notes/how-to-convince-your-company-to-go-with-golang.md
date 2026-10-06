---
title: "How to Convince Your Company to Go With Golang"
date: '2015-04-20T09:13:14-03:00'
category: webclip
summary: 'SendGrid explains why it moved its backend development to Go, arguing that concurrency needs, developer interest, maintenance costs, and community building outweighed Java, Scala, and library-support drawbacks.'
tags: ["golang", "concurrency", "backend-development", "developer-hiring"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to Convince Your Company to Go With Golang"
    url: "https://sendgrid.com/blog/convince-company-go-golang/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-04/sendgrid-com--how-to-convince-your-company-to-go-with-golang.md"
    kind: repo
---

SendGrid says it switched its primary development language to Go after finding that Perl, Python, and Gevent did not solve its underlying backend problems. The company frames the decision around concurrency at scale, developer enthusiasm for Go, and the expectation that lower maintenance costs would justify the upfront migration work.

## Reading notes

- SendGrid moved to Go after years of backend work in Perl/AnyEvent and later Python/Twisted, and after seeing that Gevent would not solve the same underlying problems.
- The main choice came down to Scala, Java, and Go, but the company felt a functional language would make hiring and training harder.
- The core development problem was concurrent programming at a scale of over 500 million messages per day.
- Go was attractive because concurrent asynchronous programming is built into the language.
- The team argued that being able to do asynchronous work in Java did not make it the best approach.
- Many developers at SendGrid were already experimenting with Go on their own time.
- The company saw that as evidence of real interest and a reason to channel that effort into work that benefits SendGrid.
- SendGrid expected the switch to cost time at the start but to save more time later through lower maintenance costs.
- The post says many of the company’s problems had been concurrency issues, so avoiding that pain early was worth the investment.
- Java’s larger developer pool was seen as a hiring advantage, but Go candidates were viewed as more likely to enjoy learning new things and pushing limits.
- Library support was described as the hardest downside of Go compared with Java’s larger ecosystem.
- SendGrid suggests open sourcing its own Go libraries as a way to strengthen the Go community and improve hiring.
- The article ends by saying each organization has to choose what is best for it.
