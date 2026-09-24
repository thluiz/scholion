---
url: "https://dev.to/koladev/how-senior-software-engineers-document-their-project-1nf4?ref=dailydev"
captured_at: "2026-09-25T00:25:18+01:00"
title: "How Senior Software Engineers Document Their Project"
domain: "dev-to"
---

There’s one task that software engineers hate, yet this small attention to detail is what separates a good software engineer from a bad one: **How do they document their project?📝**

A few years ago, I was responsible for setting up a fintech project. Because we decided to move quickly, planning for scalability wasn’t a priority. Our focus was on validating the idea, so we pushed forward, creating APIs, architectures, and systems with simple solutions, not overly concerned about the future.

However, as the person in charge of the backend and infrastructure, I knew that while my memory was reliable, it wouldn’t be enough to recall all the details six months down the line.

In my research, I discovered a convention I liked: **ADR**, or **Architectural Decision Record**.

[![ADR of the fintech API](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Ft5qxoe2oi753u33y3jat.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Ft5qxoe2oi753u33y3jat.png)

It’s essentially a document that traces all changes made to an architecture: the change itself, its impact, and what we learned from it.

Think of it as a personal journal but for the team.

_If you are interested in more content covering topics like this, subscribe to my_ [**_newsletter_**](https://buttondown.email/koladev) _for regular updates on software programming, architecture, technical writing, and tech-related insights._

## [](#why-is-it-important)**Why is it important?**

*   **Humans forget:** Documenting changes helps us because we easily forget the reasons behind choosing one architecture over another.
    
*   **It makes the team better:** Let’s say you’ve tried various solutions for an issue and documented the successes and failures. You learn from it, and others can too, even developers who come in after you.
    
*   **Future developers will thank you:** Imagine a dev coming to a codebase and trying to understand why a change was made five years ago. Somewhere, a developer is likely struggling with this because the previous engineer left without documenting it, and they’re not thrilled. Meanwhile, in another company, a developer finds an ADR explaining those changes, and they’re incredibly grateful.
    

## [](#how-do-you-write-one-then)**How do you write one then?**

There are several conventions to follow, but you can always adapt them to what works best for you.

The convention that inspired me is here: [https://adr.github.io/madr/](https://adr.github.io/madr/). You can also check Amazon’s ADR process here: [https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html).

Here is an example of a template you can use.  

```
# Example Title: Database Choice for User Data

## Context and Problem Statement

We need a scalable database to store and manage user data efficiently as our user base grows.

## Decision Drivers

* Scalability
* Data consistency
* Ease of integration with existing services

## Considered Options

* PostgreSQL
* MongoDB
* Amazon DynamoDB

## Decision Outcome

Chosen option: **PostgreSQL** because it provides strong data consistency and aligns well with our need for complex queries.

### Consequences

* **Good:** Supports ACID compliance, enhancing data reliability.
* **Bad:** May require more tuning to achieve high performance with large datasets.

### Confirmation

We’ll confirm this decision through periodic load tests and performance reviews as the user base scales.

## Pros and Cons of the Options

### PostgreSQL

* **Good:** ACID compliance, robust community support.
* **Neutral:** Setup and tuning can be time-consuming.
* **Bad:** Lacks native horizontal scaling.

### MongoDB

* **Good:** Schema flexibility, horizontal scaling.
* **Bad:** No ACID compliance across collections, limiting data integrity.

## More Information

For additional details, see the database performance evaluation [here](link-to-evaluation).
```

Enter fullscreen mode Exit fullscreen mode

This kind of document can be present within the project repository, or a notion, or JIRA.

In my last company, where I worked as a frontend engineer, we didn’t have a single document for all architectural changes.

Using GitLab issues and linking every change to an issue branch helped us track the reasons behind changes, even months after implementation.

This practice saved us countless times. As I always say, no matter how smart you or your teammates are—your CTO, manager, or anyone involved in the project—they won’t remember every technical decision made two years ago.

Unless, of course, you’re working with 10x engineers. 😆

![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fds6jk9itufkc29d1vf3w.gif)

## [](#conclusion)Conclusion

And that’s it for this article. We have discussed how companies and tech team leaders use ADRs to document architectural decisions on their projects and how much it helps them, teammates, or even the people who worked there after they left.

If you have experiences to share or any thoughts on the article, feel free to drop them in the comments below.

I’m always open to feedback and happy to engage in discussions that can help us all learn and grow.

_If you enjoyed this article and want more insights like this, subscribe to my_ [_newsletter_](https://buttondown.com/koladev) _for weekly tips, tutorials, and stories delivered straight to your inbox!_
