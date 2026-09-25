---
url: "https://snyk.io/pt-BR/blog/preventing-sql-injection-entity-framework/?ref=dailydev"
captured_at: "2026-09-25T20:43:01+01:00"
title: "Preventing SQL injection in C# with Entity Framework"
domain: "snyk-io"
---

## The importance of preventing SQL injection

SQL injection (SQLi) is one of the most severe security vulnerabilities in web applications. It occurs when an attacker is able to manipulate the SQL queries executed by an application by injecting malicious SQL code into user input fields. SQLi can lead to unauthorized access to sensitive data, data corruption, or even complete control over the database server. Preventing SQLi is crucial for maintaining the integrity, confidentiality, and availability of the data and the overall security of the application.

One of the most common mistakes developers make is using string concatenation to build SQL queries. In this approach, the parameters introduced by the user are part of the SQL query that can influence the execution path or a query. Here's an example of a vulnerable C# code:

When using characters like `;` and `--` we can influence the execution path of the query by terminating the query earlier than intended (`;`) and defining the rest of the string as comments (`--`).

If the name is set to **Brian'; DROP TABLE Users;--** , the query becomes:

The initial query stops after the `;`. A new query that drops the Users table is then executed, and the remainder of the original query is considered comments. In a similar way, it is possible to modify or insert new data in the database if SQL queries are implemented like this.

## Escaping vs. prepared statements

The key is to split the input parameters from the actual query so that user input can no longer influence the query's execution path. In many languages, functions are available that provide parameterized queries and, therefore, split the user input from the actual query.

The question remains how this is implemented under the covers as there are roughly two ways of establishing this. Either by escaping or using prepared statements

### Escaping

Escaping refers to the process of sanitizing user inputs by adding escape characters before potentially dangerous characters (like quotes). However, escaping is error-prone and not foolproof. Escaping happens on the client side (the application) and the escaped query will be sent to the database as a single statement. It requires careful handling of various edge cases and is generally not recommended as the primary defense against SQLi.

### Prepared statements

Prepared statements with parameterizing the SQL queries, on the other hand, work a little differently. The SQL structure is defined separately and sent to the database server in a first pass. The database can already create the execution path before the parameters come in play. In a second pass, the parameters are sent to the database. Because the execution plan was already created, the parameters are always treated as data rather than executable code and can't influence the execution.

## Using Entity Framework to prevent SQL injection

Entity Framework (EF) provides several methods to safely interact with the database without exposing the application to SQLi vulnerabilities. These methods include LINQ queries, FromSqlInterpolated, and FromSqlRaw with explicit parameters.

### Using LINQ

Language Integrated Query (LINQ) offers a secure way to interact with databases. This is the recommended way to query the database in EF for most queries. LINQ provides a high level of abstraction, allowing you to write queries in C# directly without knowing SQL syntax. It is integrated into C#, so you benefit from compile-time syntax checking  
Entity Framework automatically converts LINQ queries into SQL using prepared statements and parameterization, which prevents SQL injection.

While LINQ is highly convenient and secure, it can sometimes generate less efficient SQL than hand-crafted SQL queries, especially for complex queries. The translation layer could introduce performance overhead. Also, LINQ is limited by the EF provider's ability to translate C# code into SQL. Some complex SQL functionalities, like certain types of joins, subqueries, or window functions, might be cumbersome or impossible to express in LINQ.

### Using FromSqlInterpolated

FromSqlInterpolated is another safe way to execute raw SQL queries. It uses string interpolation and automatically handles parameterization, also using prepared statements.

With `FromSqlInterpolated`, EF ensures that the name variable is safely parameterized, thus protecting against SQL injection. Entity Framework Core parses the interpolated string and identifies the interpolated expressions. It then replaces these expressions with parameter placeholders within the SQL command. Corresponding SQL parameters are created, and the values of the interpolated expressions are assigned to these parameters.

Under the covers, the FromSqlInterpolated function uses a prepared statement with parameterized queries. Therefore, it is safe against SQL injection. When you need to do more complicated queries that are easier to express in SQL than the LINQ syntax, this FromSqlInterpolated is a great alternative. 

### Using FromSqlRaw with explicit parameters

In the initial example, we created the query first and passed it as a whole to the FromSQLRaw statement. However, FromSqlRaw can be used safely. By using explicit parameters with `FromSqlRaw`, EF ensures that the user input is properly parameterized, preventing SQL injection. This method involves defining SQL queries with parameter placeholders and supplying values separately, ensuring user inputs are treated as data, not executable code.

In this version, the placeholder `{0}` is used in the SQL query string, and the parameter value is passed directly as an argument to `FromSqlRaw`. This ensures that the user input is safely parameterized, protecting against SQL injection.

## Finding, fixing, and preventing

The difference between using FromSqlRaw safely or unsafely is pretty small and easily overlooked. Therefore, every developer should use tools like [Snyk Code](https://snyk.io/pt-BR/product/snyk-code/) to warn you about using unsafe code construction in C#.

![Snyk Code screen flags unsanitized HTTP input flowing into FromSqlRaw, identifying an SQL injection vulnerability in TasksController.cs.](https://res.cloudinary.com/snyk/image/upload/f_auto,w_2560,q_auto/v1722352862/blog-sql-injection-c.jpg)

In the example above, a similar SQL injection problem is recognized based on the git integration. Checking for these kinds of problems during the development lifecycle is crucial when you care about security but do not want to sacrifice velocity.

However, a great deal of education and knowledge about the frameworks used is also critical. When working with EF, your default should use the LINQ syntax. LINQ should be sufficient unless you need to be super performant or create very complex queries. When you need to make very specific and complex SQL queries, use the FromSqlInterpolated approach described above. My advice is to avoid FromSqlRaw. Even though FromSqlRaw can be used safely, the difference between a good and a wrong approach is subtle and can easily be overlooked.

To sum it all up in an easily digestible list. When using Entity Framework:

*   Use LINQ syntax to interact with the database and avoid SQL.
    
*   Only for complex situations use FromSQLInterpolated.
    
*   Use a code scanning tool like Snyk Code to help you detect mistakes.
    

Now that you know a bit more, you’re ready to use Entity Framework in C# to protect your code from SQL injection vulnerabilities. To make the process easier, [create a free Snyk account](https://app.snyk.io/login) or [book a demo](https://snyk.io/pt-BR/schedule-a-demo/) today to learn about how Snyk secures your code as it’s written.

## Primeiros passos com Capture the Flag

Saiba como resolver desafios de Capture the Flag assistindo ao nosso workshop virtual de conceitos básicos sob demanda.
