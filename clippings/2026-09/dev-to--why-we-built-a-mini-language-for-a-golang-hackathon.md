---
url: "https://dev.to/skysingh04/why-we-built-a-mini-language-for-a-golang-hackathon-42a3"
captured_at: "2026-09-25T01:02:43+01:00"
title: "Why we Built a Mini-Language for a Golang Hackathon"
domain: "dev-to"
---

## [](#a-hackathon-again)A Hackathon, Again?

At this point, I have been to _9 hackathons_, one of them being an _international one_, even winning at **4** of them. Then again, when my juniors [Dhruv](https://www.linkedin.com/in/dhruvpuri-slashex/) and [Tushar](https://www.linkedin.com/in/tusharmohapatra07/) told me about a Golang Specific hackathon, I dragged [Harsh](https://www.linkedin.com/in/harsh-joshi-82b83530b/) along with us because why not. And not just Harsh, I dragged along 40+ people from our team [Point Blank](https://www.linkedin.com/company/point-blank-d), which ended up making the hackathon our own internal competition haha.

All of us in our team **GoGoingGone** (lmao) had good experience working with Golang, But we wanted to do more than just build another tool. We wanted to innovate. That’s when the idea struck—**let's build a mini-language** to define dynamic, configurable data pipelines.

## [](#introduction)Introduction

I am Akash Singh, a third year engineering student and Open Source Contributor from Bangalore.  
Here is my [LinkedIn](https://www.linkedin.com/in/skysingh04/), [GitHub](https://github.com/SkySingh04) and [Twitter](https://x.com/SkySingh04)

[![Sky Singh](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F4eayocft44kkbwoqpc8z.JPG)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F4eayocft44kkbwoqpc8z.JPG)

> I go by the name SkySingh04 online.

## [](#introducing-fractal)Introducing **Fractal**

Fractal started as a data processing tool for seamless migration from legacy systems (like SQL databases and CSV files) to modern platforms such as **MongoDB** or **AWS S3**. But we wanted more than just another ETL tool. The idea was to make it **highly flexible and user-friendly**, allowing users to define **validation** and **transformation rules** with a simple, declarative syntax—a mini-language within the tool.

## [](#why-a-minilanguage)Why a Mini-Language?

We observed that most tools in the data pipeline space rely on rigid configurations or custom scripts. This approach often requires significant programming expertise, which limits accessibility for non-developers. A declarative mini-language provides:

1.  **Simplicity**: Users define rules in an intuitive, human-readable format.
2.  **Flexibility**: It accommodates a wide range of use cases, from basic validations to complex transformations.
3.  **Scalability**: The mini-language can evolve as new requirements arise.

This mini-language wasn’t about reinventing the wheel—it was about providing an abstraction to streamline data transformations and validations.

When this is combined with a simple yaml file configuration, we thought we hit the mark of making a easy to configure data pipeline that can process data from one source to another on scale.

[![YAML FILE](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F866zlhwdw951e4c89420.jpg)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F866zlhwdw951e4c89420.jpg)

## [](#the-core-validation-and-transformation-syntax)The Core: Validation and Transformation Syntax

We designed the syntax to be simple yet expressive, focusing on two primary operations:

1.  **Validation Rules** These ensure incoming data meets specific quality standards before further processing. For example:

```
   FIELD("age") TYPE(INT) RANGE(18, 65)
   FIELD("email") MATCHES(EMAIL_REGEX)
   FIELD("status") IN ("active", "inactive")
```

Enter fullscreen mode Exit fullscreen mode

1.  **Transformation Rules** These enable data enrichment or restructuring. For example:

```
   RENAME("old_field", "new_field")
   MAP("status", {"0": "inactive", "1": "active"})
   ADD_FIELD("processed_at", CURRENT_TIME())
   IF FIELD("age") > 50 THEN ADD_FIELD("senior_discount", TRUE)
```

Enter fullscreen mode Exit fullscreen mode

This abstraction allowed users to process diverse datasets with minimal effort, enhancing productivity and reducing complexity.

> In the middle of figuring out how to make the lexer and parser of this language, the team at [GoFr.dev](https://www.linkedin.com/company/gofr-dev/) took us all upstairs for a stress busting session, which was full of late night sharayis and jam sessions!

## [](#building-fractal-at-the-hackathon)Building Fractal at the Hackathon

The hackathon wasn’t just about creating the mini-language. We also had to build the surrounding infrastructure, ensuring Fractal was:

1.  **Extensible**: Supporting multiple input/output formats like JSON, CSV, SQL databases, and message queues.
2.  **Configurable**: YAML-based configuration for defining pipeline workflows, integrating the mini-language seamlessly.
3.  **Robust**: Handling errors gracefully with options like `LOG_AND_CONTINUE` or `STOP`.

We divided the work into four modules:

*   **Mini-Language Implementation**: Designing the lexer and parser to interpret the custom syntax.
*   **Data Integrations**: Adding support for common data sources and destinations.
*   **Pipeline Engine**: Orchestrating validation, transformation, and error handling.
*   **CLI Interface**: Providing a simple interface for defining and running pipelines.

## [](#challenges-we-faced)Challenges We Faced

1.  **Designing the Syntax** Striking a balance between simplicity and flexibility was a challenge. We iterated multiple times to finalize the syntax.
2.  **Building the Parser** Implementing a custom lexer and parser in Golang was time-consuming but rewarding.
3.  **Real-Time Feedback** Ensuring that the mini-language provided meaningful error messages to guide users was critical for usability.
4.  **Time Constraints** Building a tool of this scale in a hackathon setting required precise planning and seamless coordination.

## [](#and-what-happened-after-that)And what happened after that?

Despite our strong showing at the GO for GOFR hackathon, we faced a critical challenge during the final evaluation. The judges requested a live demonstration in addition to our recorded demo, and unfortunately, we encountered an unexpected bug in our parser logic during the live run. Given the complexity of building a robust custom parser within just 24 hours, it was an ambitious feature to develop, and while our recorded demo showcased its functionality, achieving 100% accuracy under time constraints proved difficult. This hiccup ultimately cost us the top prize. However, our efforts were still highly regarded, and our team's clear vision and compelling delivery earned us the honor of "Best Pitch," highlighting our potential and ingenuity.

## [](#so-hackathons-huh)So Hackathons huh?

Hackathons are often about pushing boundaries and exploring uncharted territories. Fractal was our attempt to redefine how data processing tools can work—by making them accessible, modular, and developer-friendly.

I couldn't have asked for a more likeminded set of people to work with me on this, absolute best and hardworking teammates without a shadow of a doubt. Looking forward to what brings me to my next hackathon, dare I say, A RUST based hackathon? xD

**Check out Fractal on GitHub**

## Fractal

**Fractal** is a flexible, configurable data processing tool built with **GoFr** and **Golang**. Fractal is designed to handle data ingestion from multiple sources, apply powerful transformations and validations, and deliver output to a wide range of destinations. With Fractal, you can automate complex data workflows without needing to manage low-level details Here's the documentation for setting up a new integration in your project:

### **Custom Syntax Documentation for Validation and Transformation Rules**

## **1\. Overview**

The custom syntax enables users to:

1.  Validate incoming data to ensure it meets predefined conditions.
2.  Transform data fields to fit desired formats, structures, or requirements.
3.  Define flexible error-handling strategies for data processing pipelines.

Rules can be written for any data source or destination, such as **JSON**, **YAML**, **CSV**, **SQL Databases**, **Message Brokers**, or **Cloud Services**.

* * *

## **2\. Validation Rules**

Validation rules ensure that data meets specific quality and integrity requirements.

…

**Or Try it Yourself and let us know what do you think!**

[![FRACTAL QR](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fr95jo37sqp0wgtf7u4s8.jpg)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fr95jo37sqp0wgtf7u4s8.jpg)
