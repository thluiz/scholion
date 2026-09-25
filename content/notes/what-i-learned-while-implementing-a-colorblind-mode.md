---
title: "What I learned while implementing a colorblind mode for my Belgian Wage Calculator site"
date: '2026-09-25T00:09:49+01:00'
category: webclip
summary: 'The author describes what he learned while creating a colorblind mode for the Belgian Wage Calculator, including how colors change with different deficiencies and why two versions worked better than one.'
tags: ["colorblindness","web-accessibility","css"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "What I learned while implementing a colorblind mode for my Belgian Wage Calculator site"
    url: "https://dev.to/illarious/what-i-learned-while-implementing-a-colorblind-mode-for-my-belgian-wage-calculator-site-51f0?"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--what-i-learned-while-implementing-a-colorblind-mode.md"
    kind: repo
---

The article is a retrospective on building a colorblind mode for the Belgian Wage Calculator. It explains the differences between red, green, and blue colorblindness, describes what the author learned from simulation tools and feedback, and shows why separate modes for red and green deficiencies worked better than a single combined palette.

## Reading notes

- The author presents the work as a retrospective on creating a colorblind mode for the Belgian Wage Calculator.
- He describes colorblindness as a spectrum and distinguishes complete and partial forms for red, green, and blue.
- The initial expectation was to choose opposite colors for a receptor and trust that they would remain distinguishable even in total deficiency.
- When simulating these conditions in Firefox, he realized that the total loss of red or green greatly reduces the available palette.
- The author concluded that the effect for red and green is much more similar than he imagined, with smaller differences than in the case of blue.
- He also observed that the extension used for simulation seemed less faithful in the case of blue deficiency in darker parts of the spectrum.
- Another lesson was that colors change according to the severity of the deficiency, so the intuitive choice of neighboring shades can fail.
- To obtain a light blue equivalent in the case of green colorblindness, the path he considered intuitive for cyan proved wrong; the solution went through the purple and pink range.
- He received the suggestion to give more weight to light and dark gradations in the backgrounds instead of relying only on color.
- After that, the author considered it more manageable to find a better palette for the site.
- In the original state, the site used red for negative values and green for positive ones, with contrast that seemed clear to people with normal vision.
- In the simulation of severe green colorblindness, negative and positive became difficult to distinguish, especially in combination with certain backgrounds.
- The author began testing specific versions for green colorblindness and for red colorblindness.
- He noticed that, in his simulation of green colorblindness, the result became quite purple and that this seemed strange at first glance.
- With 100% green colorblindness, however, this version starts to make sense within the shift of the color range.
- In the simulation of 50% green colorblindness, the version was still legible and closer to pink and purple tones.
- After testing a single version for green and red, he decided to split the mode into two options that the user can switch between.
- He did not create a specific mode for blue colorblindness, because the normal layout still seemed distinguishable.
- The author comments that the red mode is also useful for some people with certain degrees of green colorblindness.
- His hope is that at least one of the modes works well for each person, including those with total color deficiency.
- For these cases, he says he used basic design principles, such as clear plus and minus signs for positive and negative values.
- The text ends with thanks to the r/Colorblind subreddit for the feedback given and with the indication that the page is still being adjusted, especially in the backgrounds and contrast.
