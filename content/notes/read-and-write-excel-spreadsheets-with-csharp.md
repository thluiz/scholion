---
title: "Read and Write Excel Spreadsheets With C#"
date: '2021-06-30T13:17:52-03:00'
category: webclip
summary: 'The post shows how ExcelMapper lets .NET developers read Excel rows into POCOs or records, edit the data, and save it back to a spreadsheet with a few lines of C# 9.'
tags: ["dotnet", "csharp", "excelmapper"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Read and Write Excel Spreadsheets With C# | Khalid Abuhakmeh"
    url: "https://khalidabuhakmeh.com/read-write-excel-spreadsheets-with-csharp"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2021-06/khalidabuhakmeh-com--read-and-write-excel-spreadsheets-with-csharp.md"
    kind: repo
---

The post presents ExcelMapper as a simple .NET package for reading and writing Excel files with POCOs, dynamic objects, and records. It works cross-platform through NPOI and also supports formulas, formatting, and sheets.

## Reading notes

- ExcelMapper is an MIT-licensed .NET OSS package for reading and writing Excel files with plain C# objects.
- It uses NPOI under the hood, so it works cross-platform instead of relying on the Windows-only Jet database engine.
- The library feels similar to Entity Framework Core or Dapper for people familiar with data access tools.
- It can also work with dynamic objects and records, along with Excel features such as formulas, formatting, and sheets.
- To read a movie spreadsheet, the post defines a `Movie` record with `Id`, `Name`, and `StreamingService` fields that match the column names.
- A new `ExcelMapper` instance calls `FetchAsync<Movie>(excelFile)` to load the rows into a list.
- The example then iterates through the loaded movies and prints them in the console.
- To write data back, the post creates another `ExcelMapper`, reads the same rows, and changes `StreamingService` to `disney+`.
- The modified rows are copied with C# 9 `with` expressions and saved with `SaveAsync`, using `sheetName: disney`.
- After saving, the spreadsheet contains a new sheet named `disney+`.
- The conclusion says ExcelMapper lets .NET developers focus on the data while still using Excel as a general-purpose business tool.
