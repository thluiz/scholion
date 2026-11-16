---
title: "Introduction to Functional Programming in F# - Part 6"
date: '2026-11-16T15:51:12+00:00'
category: webclip
summary: 'The post shows how to read and parse a CSV file in F#, handle file errors with Result, and make the import logic testable by abstracting the file reader behind a type signature.'
tags: ["fsharp", "seq", "result", "higher-order-functions"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Introduction to Functional Programming in F# - Part 6 — Softwarepark"
    url: "https://web.archive.org/web/20201108124458id_/https://www.softwarepark.cc/blog/2019/12/22/introduction-to-functional-programming-in-f-part-6"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--introduction-to-functional-programming-in-f-part-6.md"
    kind: repo
---

The post walks through reading external data in F# with `Seq`, parsing a pipe-delimited customers file, and separating file access from parsing and output. It then refactors the import flow so the file reader can be replaced with a fake implementation for testing.

## Reading notes

- `readFile` uses `System.IO`, `StreamReader`, and a sequence expression to return the file contents line by line.
- `Seq.iter` is used in `main` to print the loaded lines to the terminal.
- `readFile` is changed to return `Result<seq<string>, exn>` so file loading errors can be handled.
- `import` matches on the `Result`, printing either the data or the error message.
- A `Customer` record is introduced with fields for the six columns in the CSV file.
- `parse` skips the header row, splits each line on `|`, and keeps only lines that match the expected shape.
- `Seq.choose id` removes `None` values and unwraps `Some` values into a sequence of `Customer` records.
- `parseLine` is extracted from the mapping step to make the parsing logic separate and reusable.
- `import` is refactored to accept a `fileReader` function so the code can work with different data sources.
- A `FileReader` type alias is introduced for the function signature `string -> Result<string seq, exn>`.
- `readFile` is rewritten to fit the `FileReader` signature.
- Partial application is used to create `importWithFileReader` from `import readFile`.
- A `fakeFileReader` is shown as a test double that returns fixed CSV data without touching the file system.
- The final code combines file reading, parsing, output, and error handling, and the post says the next step will be data validation.
