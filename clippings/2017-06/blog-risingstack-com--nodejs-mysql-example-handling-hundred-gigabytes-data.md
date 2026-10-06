---
url: "http://blog.risingstack.com/node-js-mysql-example-handling-hundred-gigabytes-of-data/"
captured_at: "2017-06-08T15:45:39-03:00"
title: "Node.js + MySQL Example: Handling 100's of GigaBytes of Data | @RisingStack"
domain: "blog-risingstack-com"
---

# Node.js + MySQL Example: Handling 100's of GigaBytes of Data

Through this Node.js & MySQL example project, we will take a look at how you can efficiently handle **billions of rows** that take up **hundreds of gigabytes** of storage space.

My secondary goal with this article is to help you decide if Node.js + MySQL is a good fit for your needs, and to provide help with implementing such a solution.

The actual code we will use throughout this blogpost [can be found on GitHub](https://github.com/RisingStack/mysql-large-data-handling).

## Why Node.js and MySQL?

We use MySQL to store the distributed tracing data of the users of our [Node.js Monitoring & Debugging Tool](https://trace.risingstack.com/) called Trace.

We chose MySQL, because at the time of the decision, Postgres was not really good at updating rows, while for us, updating immutable data would have been unreasonably complex.

Unfortunately, these solutions are not [ACID compliant](https://en.wikipedia.org/wiki/ACID) which makes them difficult to use when data consistency is extremely important.

**However, with good indexing and proper planning, MySQL can be just as suitable for the task as the above-mentioned NoSQL alternatives.**

MySQL has several storage engines. InnoDB is the default one, which comes with the most features. However, one should take into account that InnoDB tables are immutable, meaning every `ALTER TABLE` statement will copy all the data into a new table. *It will make matters worse when the need arises to migrate an already existing database.*

If you have nominal values, each having a lot of associated data — e.g. each of your users have millions of products and you have tons of users — it is probably the easiest by creating tables for each of them and giving them names like `<user_id>_<entity_name>`. **This way you can reduce the size of individual tables significantly.**

Also, getting rid of a user's data in case of an account removal is an O(1) operation. This is very important, because if you need to remove large amount of values from big tables, MySQL may decide to use the wrong index or not to use indexes at all.

It does not help either that you cannot use index hints for `DELETE`s. You might need to `ALTER` your table to remove your data, but that would mean copying each row to a new table.

**Creating tables for each user clearly adds complexity, but it may be a big win when it comes to removing users or similar entities with huge amount of associated data.**

However, before going for dynamically created tables, you should try deleting rows in chunks as it may help as well and results in less added complexity. Of course, if you have data coming in faster than you can delete, you might get stuck with the aforementioned solution.

But what if your tables are still huge after partitioning them by users and you need to delete outdated rows as well? You still have data coming in faster than you can remove. **In this case, you should try MySQL's built in table partitioning.** It comes handy when you need to cut your tables by values that are defined on an ordinal or continuous scale, such as a creation timestamp.

## Table partitioning with MySQL

With MySQL, a partitioned table will work as if it was multiple tables, but you can use the same interface you got used to, while no additional logic is needed from the application's side. This also means you can drop partitions as if you dropped tables.

The [documentation](https://dev.mysql.com/doc/refman/5.7/en/partitioning-management.html) is good, but pretty verbose as well (after all this is not a simple topic), so let's take a quick look at how you should create a partitioned table.

The way we handled our partitions was taken from [Rick James](http://mysql.rjweb.org/doc.php/partitionmaint)'s post on the topic. He also gives quite some insight on how you should plan your tables.

```
CREATE TABLE IF NOT EXISTS tbl (  
      id INTEGER NOT NULL AUTO_INCREMENT,
      data VARCHAR(255) NOT NULL,
      created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
      PRIMARY KEY (id, created_at)
    )

PARTITION BY RANGE (TO_DAYS(created_at)) (  
        start        VALUES LESS THAN (0),
        from20170514 VALUES LESS THAN (TO_DAYS('2017-05-15')),
        from20170515 VALUES LESS THAN (TO_DAYS('2017-05-16')),
        from20170516 VALUES LESS THAN (TO_DAYS('2017-05-17')),
        future       VALUES LESS THAN MAXVALUE
    );
```

It is nothing unusual until the part `PARTITION BY RANGE`.

In MySQL, you can partition by `RANGE`, `LIST`, `COLUMN`, `HASH` and `KEY` you can read about them in the [documentation](https://dev.mysql.com/doc/refman/5.7/en/partitioning-types.html). Notice that the partitioning key must be part of the primary key or any unique indexes.

The ones starting with `from<date>` should be self-explanatory. Each partition holds values for which the `created_at` column is less than the date of the next day. This also means that `from20120414` holds all data that are older than 2012-04-15, so this is the partition that we will drop when we perform the cleanup.

The `future` and `start` partitions need some explanation: `future` holds the values for the days we have not yet defined. So if we cannot run repartitioning in time, all data that arrives on `2017-05-17` or later will end up there, making sure we don't lose any of it. `start` serves as a safety net as well. We expect all rows to have a `DATETIME` `created_at` value, however, we need to be prepared for possible errors. If for some reason a row would end up having `NULL` there, it will end up in the `start` partition, serving as a sign that we have some debugging to do.

When you use partitioning, MySQL will keep that data on separate parts of the disk as if they were separate tables and organizes your data automatically based on the partitioning key.

There are some restrictions to be taken into account though:

- Query cache is not supported.
- Foreign keys are not supported for partitioned InnoDB tables.
- Partitioned tables do not support FULLTEXT indexes or searches.

There are [a lot more](https://dev.mysql.com/doc/refman/5.7/en/partitioning-limitations.html), but these are the ones that we felt the most constraining after adopting partitioned tables at [RisingStack](https://risingstack.com/).

If you want to create a new partition, you need to reorganize an existing one and split it to fit your needs:

```
ALTER TABLE tbl  
    REORGANIZE PARTITION future INTO (
        from20170517 VALUES LESS THAN (TO_DAYS('2017-05-18')),
        from20170518 VALUES LESS THAN (TO_DAYS('2017-05-19')),
        PARTITION future VALUES LESS THAN MAXVALUE
);
```

Dropping partitions takes an alter table, yet it runs as if you dropped a table:

```
ALTER TABLE tbl  
    DROP PARTITION from20170517, from20170518;
```

As you can see you have to include the actual names and descriptions of the partitions in the statements. They cannot be dynamically generated by MySQL, so you have to handle it in the application logic. That's what we'll cover next.

## Table partitioning example with Node.js & MySQL

**Let's see the actual solution.** For the examples here, we will use [knex](http://knexjs.org/), which is a query builder for JavaScript. In case you are familiar with SQL, you shouldn't have any problem understanding the code.

First, let's create the table:

```
const dedent = require('dedent')  
const _ = require('lodash')  
const moment = require('moment')

const MAX_DATA_RETENTION = 7  
const PARTITION_NAME_DATE_FORMAT = 'YYYYMMDD'

Table.create = function () {  
  return knex.raw(dedent`
    CREATE TABLE IF NOT EXISTS \`${tableName}\` (
      \`id\` INTEGER NOT NULL AUTO_INCREMENT,
      \`data\` VARCHAR(255) NOT NULL,
      \`created_at\` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
      PRIMARY KEY (\`id\`, \`created_at\`)
    )
    PARTITION BY RANGE ( TO_DAYS(\`created_at\`)) (
      PARTITION \`start\` VALUES LESS THAN (0),
      ${Table.getPartitionStrings()}
      PARTITION \`future\` VALUES LESS THAN MAXVALUE
    );
  `)
}

Table.getPartitionStrings = function () {  
  const days = _.range(MAX_DATA_RETENTION - 2, -2, -1)
  const partitions = days.map((day) => {
    const tomorrow = moment().subtract(day, 'day').format('YYYY-MM-DD')
    const today = moment().subtract(day + 1, 'day').format(PARTITION_NAME_DATE_FORMAT)
    return `PARTITION \`from${today}\` VALUES LESS THAN (TO_DAYS('${tomorrow}')),`
  })
  return partitions.join('\n')
}
```

It is practically the same statement we saw earlier, but we have to create the names and descriptions of partitions dynamically. That's why we created the `getPartitionStrings` method.

The first row is:

```
const days = _.range(MAX_DATA_RETENTION - 2, -2, -1)
```

`MAX_DATA_RETENTION - 2 = 5` creates an sequence from 5 to -2 (last value exclusive) -> `[ 5, 4, 3, 2, 1, 0, -1 ]`, then we subtract these values from the current time and create the name of the partition (`today`) and its' limit (`tomorrow`). The order is vital as MySQL throws an error if the values to partition by do not grow constantly in the statement.

### Large Scale Data Removal Example with MySQL and Node.js

Now let's take a step by step look at data removal. You can see the whole code [here](https://github.com/RisingStack/mysql-large-data-handling/blob/master/src/partitioning.js#L75).

The first method, `removeExpired` gets the list of current partitions then passes it on to `repartition`.

```
const _ = require('lodash')

Table.removeExpired = function (dataRetention) {  
  return Table.getPartitions()
    .then((currentPartitions) => Table.repartition(dataRetention, currentPartitions))
}

Table.getPartitions = function () {  
  return knex('information_schema.partitions')
    .select(knex.raw('partition_name as name'), knex.raw('partition_description as description')) // description holds the day of partition in mysql days
    .where('table_schema', dbName)
    .andWhere('partition_name', 'not in', [ 'start', 'future' ])
    .then((partitions) => partitions.map((partition) => ({
      name: partition.name,
      description: partition.description === 'MAX_VALUE' ? 'MAX_VALUE' : parseInt(partition.description)
    })))
}

Table.repartition = function (dataRetention, currentPartitions) {  
  const partitionsThatShouldExist = Table.getPartitionsThatShouldExist(dataRetention, currentPartitions)

  const partitionsToBeCreated = _.differenceWith(partitionsThatShouldExist, currentPartitions, (a, b) => a.description === b.description)
  const partitionsToBeDropped = _.differenceWith(currentPartitions, partitionsThatShouldExist, (a, b) => a.description === b.description)

  const statement = dedent
    `${Table.reorganizeFuturePartition(partitionsToBeCreated)}
    ${Table.dropOldPartitions(partitionsToBeDropped)}`

  return knex.raw(statement)
}
```

First, we select all currently existing partitions from the `information_schema.partitions` table that is maintained by MySQL.

Then we create all the partitions that should exist for the table. If `A` is the set of partitions that exist and `B` is set of partitions that should exist then

`partitionsToBeCreated = B \ A`

`partitionsToBeDropped = A \ B`.

`getPartitionsThatShouldExist` creates set `B`.

```
Table.getPartitionsThatShouldExist = function (dataRetention, currentPartitions) {  
  const days = _.range(dataRetention - 2, -2, -1)
  const oldestPartition = Math.min(...currentPartitions.map((partition) => partition.description))
  return days.map((day) => {
    const tomorrow = moment().subtract(day, 'day')
    const today = moment().subtract(day + 1, 'day')
    if (Table.getMysqlDay(today) < oldestPartition) {
      return null
    }

    return {
      name: `from${today.format(PARTITION_NAME_DATE_FORMAT)}`,
      description: Table.getMysqlDay(tomorrow)
    }
  }).filter((partition) => !!partition)
}

Table.getMysqlDay = function (momentDate) {  
  return momentDate.diff(moment([ 0, 0, 1 ]), 'days') // mysql dates are counted since 0 Jan 1 00:00:00
}
```

The creation of partition objects is quite similar to the creation of the `CREATE TABLE ... PARTITION BY RANGE` statement. It is also vital to check if the partition we are about to create is older than the current oldest partition: it is possible that we need to change the `dataRetention` over time.

Take this scenario for example:

> Imagine that your users start out with 7 days of data retention, but have an option to upgrade it to 10 days. In the beginning the user has partitions that cover days in the following order: `[ start, -7, -6, -5, -4, -3, -2, -1, future ]`. After a month or so, a user decides to upgrade. The missing partitions are in this case: `[ -10, -9, -8, 0 ]`.
>
> At cleanup, the current script would try to reorganize the `future` partition for the missing partitions appending them *after* the current ones.
>
> Creating partitions for days older than -7 does not make sense in the first place because that data was meant to be thrown away so far anyways, and it would also lead to a partition list that looks like `[ start, -7, -6, -5, -4, -3, -2, -1, -10, -9, -8, 0, future ]` which isn't monotonously increasing, thus MySQL will throw an error, and the cleanup will fail.

MySQL's `TO_DAYS(date)` function calculates the number of days passed since year 0 January 1, so we replicate this in JavaScript.

```
Table.getMysqlDay = function (momentDate) {  
  return momentDate.diff(moment([ 0, 0, 1 ]), 'days')
}
```

Now that we have the partitions that have to be dropped, and the partitions that have to be created, let's create our new partition first for the new day.

```
Table.reorganizeFuturePartition = function (partitionsToBeCreated) {  
  if (!partitionsToBeCreated.length) return '' // there should be only one every day, and it is run hourly, so ideally 23 times a day it should be a noop
  const partitionsString = partitionsToBeCreated.map((partitionDescriptor) => {
    return `PARTITION \`${partitionDescriptor.name}\` VALUES LESS THAN (${partitionDescriptor.description}),`
  }).join('\n')

  return dedent`
    ALTER TABLE \`${tableName}\`
      REORGANIZE PARTITION future INTO (
        ${partitionsString}
        PARTITION \`future\` VALUES LESS THAN MAXVALUE
      );`
}
```

We simply prepare a statement for the new partition(s) to be created.

**We run this script hourly just to make sure nothing goes astray and we are able to perform the cleanup properly at least once a day.**

So the first thing to check is if there's a partition to be created at all. This should happen only at the first run, then be a noop 23 times a day.

We also have to drop the outdated partitions.

```
Table.dropOldPartitions = function (partitionsToBeDropped) {  
  if (!partitionsToBeDropped.length) return ''
  let statement = `ALTER TABLE \`${tableName}\`\nDROP PARTITION\n`
  statement += partitionsToBeDropped.map((partition) => {
    return partition.name
  }).join(',\n')
  return statement + ';'
}
```

This method creates the same `ALTER TABLE ... DROP PARTITION` statement we saw earlier.

And finally, everything is ready for the reorganization.

```
  const statement = dedent
    `${Table.reorganizeFuturePartition(partitionsToBeCreated)}
    ${Table.dropOldPartitions(partitionsToBeDropped)}`

  return knex.raw(statement)
```

## Wrapping it up

As you can see, contrary to popular belief, ACID compliant DBMS solutions such as MySQL can be used when you are handling large amounts of data, so you don't necessarily need to give up the features of transactional databases.

However, table partitioning comes with quite a few restrictions, meaning you are cut off from using all the power InnoDB provides for keeping your data consistent. You might also have to handle in the app logic what otherwise would be available such as foreign key constraints or full-text searches.

**I hope this post helps you decide whether MySQL is a good fit for your needs and helps you implement your solution. Until next time: Happy engineering!**

If you have any Node + MySQL questions, let me know in the comments below!
