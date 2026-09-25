---
title: "Interview Question: how do you ensure you only virus scan once?"
date: '2026-09-25T19:16:00+01:00'
category: webclip
summary: 'The article argues for interview questions based on real work, using a file-upload and virus-scanning scenario to test system design, performance, fault tolerance, and UX rather than rote algorithms.'
tags: ["interview-questions", "system-design", "virus-scanning", "developer-hiring"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Interview Question: how do you ensure you only virus scan once?"
    url: "https://dev.to/miketalbot/interview-question-ensure-you-only-virus-scan-once-349j?"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--interview-question-how-do-you-ensure-you-only-virus-scan-onc.md"
    kind: repo
---

The article argues that interview questions should reflect problems developers face in practice, not just DSA or low-level algorithm drills. It uses a file-upload case to probe how a candidate thinks about repeated virus scanning, storage reuse, UX, fault tolerance, and scaling.

## Reading notes

- The author prefers interview questions that test reasoning about frequent real-world challenges.
- The example asks how to avoid scanning the same uploaded file multiple times.
- A proposed answer is to name files from their contents using a V5 GUID, check whether that name already exists in storage, and scan only when the file is new.
- If the file already exists, the system can reuse the stored result and report whether it is infected.
- The same approach stores the file only once and uses the generated name as a reference.
- The method is presented as friendly to users because they can just upload files without extra work.
- For fault tolerance, the article suggests recording the filename together with the scan version, or changing the V5 GUID namespace so future uploads are scanned again.
- Suggested tools include a database for the file name and Redis for faster lookup.
- The author says the lookup becomes O(1) after the name is created, while creating the name is O(N) in file size and already part of the upload work.
- If an interviewee pushes responsibility onto users, the author recommends steering them back toward UX and cost concerns.
- The conclusion is that interviewers should learn how candidates reason about real problems, not whether they can repeat memorized algorithms.
