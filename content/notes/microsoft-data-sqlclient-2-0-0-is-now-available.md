---
title: "Microsoft.Data.SqlClient 2.0.0 is now available"
date: '2020-07-05T14:10:32+00:00'
category: webclip
summary: 'The post announces Microsoft.Data.SqlClient 2.0.0, says it replaces System.Data.SqlClient as a drop-in library, and highlights ORDER hints in SqlBulkCopy, DNS resiliency, and new authentication support.'
tags: ["microsoft-data-sqlclient", "sqlbulkcopy", "dns-resiliency", "azure-sql"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Microsoft.Data.SqlClient 2.0.0 is now available"
    url: "https://devblogs.microsoft.com/azure-sql/microsoft-data-sqlclient-2-0-0-is-now-available"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/devblogs-microsoft-com--microsoft-data-sqlclient-2-0-0-is-now-available.md"
    kind: repo
---

Microsoft.Data.SqlClient 2.0.0 is presented as the new version to use if you are already on 1.x, and as a true drop-in replacement for System.Data.SqlClient. The post points readers to the release notes and calls out features aimed at future-proofing SQL Server and Azure SQL data access.

## Reading notes

- If you are using version 1.x, the update path is to install 2.0.0 through NuGet or the .NET Core CLI.
- If you are still on System.Data.SqlClient, the new library is described as a drop-in replacement and existing code should keep working.
- The release adds internal driver support for resiliency to DNS failures.
- The release adds Active Directory Integrated, Active Directory Interactive, and Active Directory Service Principal authentication for .NET Core and .NET Standard.
- The release adds Active Directory Service Principal authentication for .NET Framework.
- The release adds optional ORDER hints in SqlBulkCopy for improved performance.
- The release adds new connection string property synonyms.
- The author says the ORDER hint can improve bulk load performance when the input data is already ordered by the target table clustered index.
- The author says the ORDER hint can avoid an extra sort step and, in his case, the sort affected bulk load performance by up to 50%.
- The author says the new library made it possible to bulk load without dropping and recreating the clustered index.
- The author says better DNS failure resiliency matters for cloud development and removes the need to handle that plumbing manually.
- The author also says the contributor list shows SqlClient becoming more of a community effort.
