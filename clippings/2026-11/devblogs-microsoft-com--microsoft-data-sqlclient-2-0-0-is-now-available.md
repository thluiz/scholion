---
url: "https://devblogs.microsoft.com/azure-sql/microsoft-data-sqlclient-2-0-0-is-now-available"
captured_at: "2026-11-16T03:38:20+00:00"
title: "Microsoft.Data.SqlClient 2.0.0 is now available"
domain: "devblogs-microsoft-com"
---

June 19th, 2020

0 reactions

![](https://devblogs.microsoft.com/azure-sql/wp-content/uploads/sites/56/2022/05/IMG_5861-96x96.jpeg)

Principal Product Manager

As you probably already know, one year ago a new Microsoft.Data.SqlClient library was released to replace the well-know System.Data.SqlClient. This was done to add support to .Net Core, to be [**Open Source**](https://github.com/dotnet/SqlClient), and to serve as the starting point for all future development and investments Azure SQL and SQL Server data access drivers. If you missed such news, you can read all the details here:

[Introducing the new Microsoft.Data.SqlClient](https://devblogs.microsoft.com/dotnet/introducing-the-new-microsoftdatasqlclient/)

A few days ago the version 2.0.0 has been released with some interesting news. All you have to do to use this new version, if you are already using version 1.x is just update it via NuGet or the .NET Core CLI.

dotnet add package Microsoft.Data.SqlClient

If you are still using System.Data.SqlClient, you just have to replace the old library with the new one, as it is a true drop-in replacement. All you code will still work as before. But it will be more future-proof.

## New Features

The new version 2.0.0 introduces quite a few [interesting features](https://github.com/dotnet/SqlClient/releases/tag/v2.0.0):

*   [Added internal driver support to provide resiliency to DNS failures](https://github.com/dotnet/SqlClient/pull/594)
*   [Added support for Active Directory Integrated, Active Directory Interactive and Active Directory Service Principal authentication mode for .NET Core and .NET Standard](https://github.com/dotnet/SqlClient/blob/master/release-notes/2.0/2.0.0.md#additional-active-directory-authentication-modes)
*   [Added support for Active Directory Service Principal authentication mode for .NET Framework](https://github.com/dotnet/SqlClient/blob/master/release-notes/2.0/2.0.0.md#active-directory-service-principal)
*   [Added support for optional ORDER hints in SqlBulkCopy for improved performance](https://github.com/dotnet/SqlClient/blob/master/release-notes/2.0/2.0.0.md#order-hints-for-sqlbulkcopy)
*   [New Connection String properties synonyms](https://github.com/dotnet/SqlClient/blob/master/release-notes/2.0/2.0.0.md#new-connection-string-property-synonyms)

My favorite among those are the support for the ORDER hints in the SqlBulkCopy class and the better resilency to DNS failures.

The ORDER hint it allow to you to greatly improve performances if the data you want to import is _already_ ordered by the target’s table clustered index. By informing the database engine that data is coming in already ordered, data can be loaded as is, without an additional sorting step, that usually is the most expensive on the whole operation.

Make sure you take a look at the very long and detailed [release note document](https://github.com/dotnet/SqlClient/blob/master/release-notes/2.0/2.0.0.md#summary-of-changes-in-20). It won’t take much of your time, and it will provide a great overview of what you can use to improve your solution.

## Ordered Bulk Load

Without the ORDER option, in fact, this is the query plan you’ll get:

[![Image sort](https://devblogs.microsoft.com/azure-sql/wp-content/uploads/sites/56/2020/06/sort.png)](https://devblogs.microsoft.com/azure-sql/wp-content/uploads/sites/56/2020/06/sort.png)

and in my specific case the sort was impacting for up to **50%** the performance of my bulk load! After using the new library where sort order was specified, the plan didn’t show the Sort operator anymore:

[![Image no sort](https://devblogs.microsoft.com/azure-sql/wp-content/uploads/sites/56/2020/06/no-sort.png)](https://devblogs.microsoft.com/azure-sql/wp-content/uploads/sites/56/2020/06/no-sort.png)

This also means I can bulk load the table without having to drop and recreate the clustered index to get the maximum throughput, which in turns means better overall performances. Here’s the code snipped I used to inform bulk load API of the existing ordering:

foreach (var ci in tableInfo.ClusteredIndex) { 
    bulkCopy.ColumnOrderHints.Add(ci.ColumnName, ci.IsDescending ? SortOrder.Descending : SortOrder.Ascending); 
}

## DNS Failure Resiliency

The other feature that I really love is the better resiliency to DNS failures. Resiliency is _really_ a key point when developing for the cloud, but unfortunately the majority of developers are not used to properly deal with it, so is quite often overlooked. Having the client library to deal with this for us solves the problem at the root and also removes the need to manually deal with this plumbing code.

Last but not least, as a [former MVP](https://mvp.microsoft.com/en-us/PublicProfile/36809) and lover of everything community, I really love the fact that SqlClient is really becoming a community effort as you can see from the contributor list.

## Author

![Davide Mauri](https://devblogs.microsoft.com/azure-sql/wp-content/uploads/sites/56/2022/05/IMG_5861-96x96.jpeg)

Principal Product Manager

Principal Product Manager in Azure SQL, with a career in IT spanning since 1997, earning the prestigious Data Platform MVP status for 12 consecutive years. Currently, he serves as the Principal Product Manager for Azure SQL Database, focusing on developers and AI.
