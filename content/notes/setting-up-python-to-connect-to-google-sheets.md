---
title: "Setting up Python to Connect to Google Sheets"
date: '2020-04-20T21:22:27+00:00'
category: webclip
summary: 'The post describes two problems while connecting Python to Google Sheets: outdated API scopes caused 403 permission errors, and pytest used a different root directory, which broke the JSON file path.'
tags: ["python", "google-sheets", "pytest", "gspread"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Setting up Python to Connect to Google Sheets"
    url: "https://dev.to/rosejcday/setting-up-python-to-connect-to-google-sheets-2ak7"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--setting-up-python-to-connect-to-google-sheets.md"
    kind: repo
---

The post follows the author's work on a migraine-tracking project that uses Twilio and Google Sheets to request survey details by SMS and store them for later doctor's appointments. It focuses on two issues encountered while using Google APIs and testing the spreadsheet connection.

## Reading notes

- The first error came from scope settings when using gspread with Google Sheets API access.
- The author first thought the configuration file was wrong, but later linked the problem to API version changes and older tutorials.
- The error was a 403 insufficient authentication scopes message.
- The scopes that worked were `https://spreadsheets.google.com/feeds` and `https://www.googleapis.com/auth/drive`.
- The issue was tied to gspread being upgraded and based on API v4.
- A later problem appeared in pytest when the spreadsheet constructor could not read the JSON credentials file.
- The constructor expected the credential filename path and the sheet name.
- `../client_secret.json` worked in the executor file, but it failed in the test file.
- A small path test showed that `client_secret.json` existed while `../client_secret.json` did not.
- Changing the constructor input to `client_secret.json` fixed the tests.
- The root directory for pytest was different from the one expected, which explained the path mismatch.
- The post ends by noting that the next update will cover using the Twilio API with Flask for the migraine survey app.
