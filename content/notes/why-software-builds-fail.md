---
title: "Why software builds fail"
date: '2014-06-30T10:01:59-03:00'
category: webclip
summary: 'Google researchers analyzed 26 million builds to ask how often builds fail, why they fail and how long fixes take. Dependency errors dominated, and build failure rates did not track frequency or experience.'
tags: ["software-builds", "build-errors", "dependency-errors", "developer-productivity"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Why software builds fail | ITworld"
    url: "http://www.itworld.com/big-data/424262/why-software-builds-fail"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-06/itworld-com--why-software-builds-fail.md"
    kind: repo
---

The article reports on a Google-led study of build failures in Java and C++ and uses it to point toward ways to improve developer productivity. The data cover more than 26 million builds from 18,000 Google engineers between November 2012 and July 2013.

## Reading notes

- The study asked how often builds fail, why they fail and how long it takes to fix them.
- Build failure rates did not correlate with how often a developer built code.
- Build failure rates also did not show a lower ratio for experienced developers than for novice developers.
- Dependency-related errors made up most Java build errors, with missing symbols the most common case.
- Dependency-related errors also made up most C++ build errors, including undeclared identifiers and missing class variables.
- C++ had a higher median build failure rate than Java.
- Syntax errors occurred more often in C++ builds than in Java builds.
- The researchers link the Java and C++ difference partly to wider IDE use in Java development.
- The study suggests tool developers should help engineers prevent or resolve dependency errors.
- The Google infrastructure team is said to be trying to reduce these errors and the time needed to resolve them.
