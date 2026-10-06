---
title: "7 timeless lessons of programming graybeards"
date: '2015-03-10T11:46:10-03:00'
category: webclip
summary: 'The article argues that older programmers still have practical advantages because experience teaches limits that hype hides: memory, network latency, compiler bugs, user speed, algorithmic complexity, and library costs.'
tags: ["programming", "software-performance", "algorithms", "developer-experience"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "7 timeless lessons of programming ‘graybeards’"
    url: "http://www.infoworld.com/article/2891806/application-development/7-timeless-lessons-of-programming-graybeards.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-03/infoworld-com--7-timeless-lessons-of-programming-graybeards.md"
    kind: repo
---

The piece says experienced programmers know things that cannot be learned quickly from current trends. It frames those lessons as hard-earned responses to real limits in software systems, especially when code has to scale beyond a small test case.

## Reading notes

- Memory is still limited, so programmers need to manage allocation and cleanup instead of assuming garbage collection or cloud RAM will solve the problem.
- Networks are slow, so code should do as much work locally as possible and send only the smallest final result to remote services.
- Compilers and interpreters can have bugs, so debugging sometimes has to test the tools as well as the application code.
- Users notice delay quickly, and slow interfaces or heavy browser-side code can make an application feel unusable.
- The public web is slower than an office network, so demos can hide delays that real users on weaker connections will still face.
- Algorithmic complexity matters because code that looks fine on small inputs can become unusable when data grows.
- Libraries and APIs can hurt performance when they are used in hot paths, especially if they add repeated parsing or other hidden overhead.
