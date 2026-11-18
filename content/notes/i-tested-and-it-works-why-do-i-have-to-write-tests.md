---
title: "Me: \"I tested and it works, why do I have to write tests?\""
date: '2019-06-26T10:04:18+00:00'
category: webclip
summary: 'The author argues that manual testing cannot cover every case, while tests make behavior explicit, catch overlooked flaws, and define the software’s specification.'
tags: ["software-testing", "continuous-integration", "specifications"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Me: \"I tested and it works, why do I have to write tests?\""
    url: "https://dev.to/briwa/me-i-tested-and-it-works-why-do-i-have-to-write-tests-4292"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--i-tested-and-it-works-why-do-i-have-to-write-tests.md"
    kind: repo
---

The author says manual testing used to be the only way to check code, but it could not cover all possible cases. He presents automated testing as a way to cover use cases systematically, keep software stable, and ship with more confidence.

## Reading notes

- Manual testing in the browser was the only way he knew at first.
- He remembers launch checklists in spreadsheets, yet bugs still appeared.
- Automated testing with Continuous Integration is described as systematic and confidence-building.
- He sees resistance to testing as fear of leaving the comfort of “I coded it and it works.”
- Tests are presented as a way to cover cases that the developer or reviewer might overlook.
- He says tests define the specification of the code and make clear what it can and cannot do.
- He browses test folders in libraries to understand behavior when API or demo pages do not explain it.
- When code changes, all tests should still pass because the code must remain within its specification.
- New code should come with new tests because it adds new specifications to the software.
- Shipping code without tests means shipping code without a specification.
- Open source repositories are described as treating tests seriously because code stability matters to many people.
- He concludes that the article may not apply to everyone, but it may help readers rethink why testing matters.
