---
title: "How To Store Huge Information in A Single Integer Value"
date: '2026-11-16T02:05:23+00:00'
category: webclip
summary: 'The page shows how to encode multiple user roles in one integer by assigning each role a power of two, then recover the roles by reading the binary remainders.'
tags: ["roles-and-permissions", "bitmask", "integer-storage"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How To Store Huge Information in A Single Integer Value"
    url: "https://bridge-global.com/blog/the-magic-of-a-single-integer-number-to-contain-huge-information"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/bridge-global-com--how-to-store-huge-information-in-a-single-integer-value.md"
    kind: repo
---

The page explains a compact way to store multiple user roles in one integer. Instead of saving role IDs as a comma-separated string or in a separate table, it assigns each role a power of two and adds the matching values together.

## Reading notes

- The example uses user roles and permissions for an application.
- Roles are assigned integer IDs, then reassigned as powers of two, such as 1, 2, 4, 8, 16, 32, and 64.
- A user with Data Entry and View Only roles is stored as 32 + 64 = 96 in one integer column.
- To recover the roles, the number is divided by 2 repeatedly and the remainders are recorded.
- The iterations with remainder 1 identify the active powers of two.
- For 96, the active values are 32 and 64.
- The page includes C# code that returns the powers of two found in a long integer.
- The same method can store other kinds of combination data, not only user roles.
