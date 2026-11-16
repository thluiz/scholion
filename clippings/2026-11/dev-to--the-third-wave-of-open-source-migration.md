---
url: "https://dev.to/tidelift/the-third-wave-of-open-source-migration-em3"
captured_at: "2026-11-16T02:04:09+00:00"
title: "The third wave of open source migration"
domain: "dev-to"
---

A few weeks ago, Dries Buytaert, creator of Drupal and co-founder of Acquia, published a blog post entitled [Is open source recession-proof?](https://dri.es/is-open-source-recession-proof) He wrote: 

> “...during an economic downturn, organizations will look to lower costs, take control of their own destiny, and strive to do more with less. Adopting Open Source helps these organizations survive and thrive.”

I joined Red Hat in the aftermath of the dotcom crash in the early 2000s, and lived through the rapid growth of open source during that recession. At the time, the main driver of open source expansion was UNIX to Linux migration.

And what was the single biggest driver of people abandoning their Sun Solaris servers and HP-UX or AIX installations and moving over to Linux? 

Saving money.

It was simply much less expensive to run Linux than UNIX, because Linux could run on relatively inexpensive Intel hardware. Companies of all stripes made the jump because—in the midst of a painful recession—they could save a lot of money without sacrificing performance, all while avoiding vendor lock-in.

In the early days of the enterprise business at Red Hat, Sun Microsystems was a goliath with over 30,000 employees and Solaris was arguably the de facto web server platform. By the end of the decade, Sun was a shadow of its former self—in large part due to UNIX to Linux migration—and ended up being gobbled up by Oracle.

But UNIX to Linux was only the beginning of the proprietary to open source workload exodus. What started with the all-open source LAMP stack (Linux operating system, Apache web server, MySQL database, and PHP/Perl/Python programming languages) quickly expanded as the cost saving benefits of open source became more pronounced.

Proprietary databases such as Oracle and IBM DB2 started being replaced by more modern open source databases like MySQL, PostgreSQL, and MongoDB. At the same time, open source middleware—including application servers and servlet containers like Jetty and Tomcat—started to make inroads into the customer bases of big companies like BEA. More recently, open source has been critical to the open source strategies of storage management systems and networking solutions companies like Juniper and Cisco.

And when the financial crisis hit in 2008, the [rise of hosted cloud services](https://www.computerworld.com/article/3412382/the-history-of-aws--a-timeline-of-defining-moments-from-2002-to-now.html) like AWS, Google Cloud, and Microsoft Azure (all of whom actually built most of their IaaS using open source too!) capped the second powerful wave of open source migration, as organizations looking to cut costs and improve flexibility moved workloads out of their own data centers and into the cloud, where the value prop for using open source was even stronger. 

Now, after one of the longest bull market runs in history, the road ahead is again uncertain. As the COVID-19 outbreak upends entire industries, organizations attempting to get leaner without sacrificing competitiveness will return to the tried-and-true playbook, cutting IT costs by finding the next place to migrate to open source. At the same time, the pandemic has caused changes in consumer, corporate, and public sector spending that are effectively boosting other sectors, demanding that they quickly step up or alter operations to meet demand. These organizations also rely on open source throughout their technology stacks. 

So where is the low-hanging fruit in 2020? A recent survey by Tidelift found that [over 92% of all application libraries contain open source components](https://dev.to/open-source-is-everywhere-survey-results-part-1). Yet in many organizations, development teams have balked at fully embracing open source for their application development projects.

Why? Despite clear advantages in other areas like technology flexibility, developer satisfaction, cost, quality, and security, the Achilles heel for open source applications has historically been the consistent availability of [support and commercial assurances](https://thenewstack.io/reliable-support-inhibits-open-source-growth/) for the independently maintained open source components used to develop applications using JavaScript, Python, Ruby, PHP, Java, .NET, and other open source frameworks.

Often, these components are created by independent open source maintainers who have historically not been financially compensated to keep these components maintained to a commercial standard. So using them comes with more risk than using the earlier wave open source backed by big commercial open source companies.

And what workloads are primed for this next round of migration? Certainly any web application that is not yet built using modern open source frameworks like React, Angular, or Vue would be a great place to start. Or organizations still utilizing expensive data science platforms like SAS or MATLAB might find that they can save money, modernize, and attract top talent by instead using some of the new and powerful data science tools like NumPy, pandas, and SciPy. More broadly, for any technology-driven organization that hasn’t embraced the reality that the modern application development platform is a polyglot mix of open source languages, frameworks, and packages: the time is now.

The first and second open source migration waves were periods of rapid expansion for companies that rose up to provide commercial assurances for Linux and the open source databases, like Red Hat, MongoDB, and Cloudera. Or platforms that made it easier to host open source workloads in a reliable, consistent, and flexible manner via the cloud, like Amazon Web Services, Google Cloud, and Microsoft Azure.

This trend will continue in the third wave of open source migration, as organizations interested in reducing cost without sacrificing development speed will look to migrate more of their applications to open source. They’ll need a new breed of vendor—akin to Red Hat or AWS—to provide the commercial assurances they need to do it safely. 

It’s been hard to be optimistic the last few weeks. But as I look for a silver lining in the current crisis, I believe there is an enormous opportunity for organizations to get even more nimble in their use of open source. The last 20+ years of technology history have shown that open source is a powerful weapon organizations can use to navigate a global downturn. In a few years, once the economy has recovered and global industry is humming along, hopefully we’ll look back at this as the moment the third great wave of open source migration began.

_Photo by [Dawid Zawiła](https://unsplash.com/@davealmine?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on Unsplash_
