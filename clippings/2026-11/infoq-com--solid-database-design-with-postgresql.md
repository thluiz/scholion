---
url: "https://www.infoq.com/news/2013/02/solid-database-design/"
captured_at: "2026-11-16T16:52:41+00:00"
title: "SOLID Database Design With PostgreSQL"
domain: "infoq-com"
---

SOLID Database Design With PostgreSQL

FEB 26, 2013

by Roopesh Shenoy

Chris Travers recently published a series of articles titled “Building SOLID Databases”. He explains several ideas on how to apply some of the common OOP principles such as Single Responsibility Principle, Interface Segregation, Dependency Inversion to improve data models and database code. While some of the ideas can be applied in part to any relational databases, the articles showcase scenarios involving object-relational features such as table inheritance, available in databases like PostgreSQL.

In Single Responsibility And Normalization, Chris explains the similarities and subtle differences between data models and class models. Normalization is normally sufficient for meeting the SRP in pure relational databases, but table inheritance can be further used to manage commonly co-occurring fields which are dependent on other fields in the database. He provides an example -

A common case where composition makes a big difference is in managing notes. People may want to attach notes to all kinds of other data in a database, and so one cannot say that the text or subject of a note is mutually dependent.

A typical purely relational approach is to either have many independently managed notes tables or have a single global note table which stores notes for everything, and then have multiple join tables to add join dependencies.

An object-relational approach might be to have multiple notes tables, but have them inherit the table structure of a common notes table.

In the Open/Closed Principle, the goal would be to keep the system extendable, without causing extensions to break when the base version changes. Again table inheritance can provide a flexible way to provide extension points for data models – the example here is how the pg_message_queue 0.2 can handle various data types by having a separate table to support each data type, all inheriting from a common table. Chris also provides another simple example where a secure API is kept extendable for security controls but closed for modifications.

The Liskov Substition Principle is normally not a problem for purely Relational databases, but could come to the fore-front when you use table inheritance. An example here is a my_square table inheriting a my_rectangle table –

CREATE TABLE my_rectangle ( id serial primary key, height numeric, width numeric );
CREATE TABLE my_square ( check (height = width) ) INHERITS (my_rectangle);

and run an update on my_rectangle -

UPDATE my_rectangle SET height = height * 2

then it will cause referential issues in the square table and fail. Ways to handle this would be to either avoid updates altogether (keep rows immutable) or use triggers to delete rows from my_square and insert into my_rectangle whenever such updates are run.

Interface Segregation when applied to databases would involve mainly user-defined functions or stored procedures. Chris consider these as interfaces to the underlying data and suggests that the ideal function or stored procedure would have one large query with minimal surrounding logic – anything more than 5 queries or large number of optional parameters might point to reducible complexity which should be dealt with by breaking into multiple separate functions or stored procedures, each one for a specific purpose. This again goes hand in hand with the Single Responsibility Principle.

In Dependency Inversion and Robust DB Interfaces, Chris explains how close binding between application logic and stored procedures can lead to leaky abstractions and suggests a few potential solutions. Some of them are using something akin to a service locator pattern, using Views or functions, using custom datatypes, triggers and notifications. They key suggestion here is to look at various options and design the database itself as an application exposing an appropriate API.
