---
title: "How to Implement Audit Trail in ASP.NET Core with EF Core"
date: '2025-08-11T15:25:14+01:00'
category: webclip
summary: 'The post shows how to add audit trails in an ASP.NET Core app with EF Core by using a separate AuditTrail entity, current-user lookup, and DbContext change tracking.'
tags: ["audit-trails", "ef-core", "aspnet-core", "change-tracking"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to Implement Audit Trail in ASP.NET Core with EF Core"
    url: "https://antondevtips.com/blog/how-to-implement-audit-trail-in-asp-net-core-with-ef-core?utm_source=email&utm_medium=email&utm_campaign=website"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-08/antondevtips-com--how-to-implement-audit-trail-in-aspnet-core-ef-core.md"
    kind: repo
---

The post explains how to implement audit trails in an ASP.NET Core application with EF Core by keeping audit data in a separate table and using change tracking to record create, update, and delete operations. It also shows how to capture the current user, update auditable entities, and store old and new values with changed columns.

## Reading notes

- Audit trails are used to track who changed data, when it changed, and what changed, for monitoring, compliance, and debugging.
- The example application is a Books app with Books, Authors, and Users, and auditable entities inherit from an IAuditableEntity interface.
- The interface includes CreatedAtUtc, UpdatedAtUtc, CreatedBy, and UpdatedBy.
- The post chooses one automatic implementation for all auditable entities instead of handling each entity manually.
- An AuditTrail entity stores Id, UserId, User, TrailType, DateUtc, EntityName, PrimaryKey, OldValues, NewValues, and ChangedColumns.
- TrailType can be Create, Update, or Delete.
- The EF Core configuration maps the audit trails table, sets indexes and lengths, and stores TrailType as a string.
- ChangedColumns, OldValues, and NewValues are stored as jsonb columns in Postgres.
- If the database does not support JSON columns, the post suggests using string properties with an EF Core conversion.
- With .NET 8 and EF 8 on Postgres, EnableDynamicJson is needed for dynamic JSON in jsonb columns.
- A CurrentSessionProvider reads the current user id from the HTTP context claims using the userid claim.
- The provider and IHttpContextAccessor are registered in DI.
- The DbContext injects ICurrentSessionProvider and overrides SaveChangesAsync.
- Before saving, it sets auditable properties and creates audit trail entries.
- When no user id is available, the code uses system as the source.
- Created entities get CreatedAtUtc and CreatedBy, while modified entities get UpdatedAtUtc and UpdatedBy.
- Audit trail creation iterates over IAuditableEntity entries with Added, Deleted, or Modified states.
- The code skips temporary properties and excludes PasswordHash from audit trails.
- For Added entities, CurrentValue goes into NewValues and TrailType becomes Create.
- For Deleted entities, OriginalValue goes into OldValues and TrailType becomes Delete.
- For Modified entities, changed properties are added to ChangedColumns and both old and new values are stored.
- Reference entries that are modified add the related entity name to ChangedColumns.
- Collection navigations that are modified also add their related entity name to ChangedColumns.
- The post says audit trail records are added before base.SaveChangesAsync so everything persists in one transaction.
