---
title: "What’s Hot (and Not) in Tech Skills"
date: '2016-02-10T17:05:34-03:00'
category: webclip
summary: 'The article defines a “Demand Ratio” by comparing skill supply on resumes with job-post demand, then uses it to show which tech skills and job titles are hot or less in demand.'
tags: ["tech-skills", "job-market", "supply-and-demand", "data-visualization"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "What's Hot (and Not) in Tech Skills - Dice Insights"
    url: "http://insights.dice.com/2016/02/01/whats-hot-and-not-in-tech-skills/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-02/insights-dice-com--whats-hot-and-not-in-tech-skills.md"
    kind: repo
---

The article explains a supply-and-demand way to judge tech skills and job titles. It calls the result a “Demand Ratio,” where values above 1 mean demand is higher than supply and values below 1 mean the opposite.

## Reading notes

- Demand Ratio is calculated by normalizing supply and demand, then dividing demand by supply.
- “Hot” skills have a number higher than 1; less in-demand skills have a number lower than 1.
- The chart uses the top 700 technology skills and top 400 job titles in the dataset, but defaults to 200 for performance.
- Red points mark hot skills, blue points mark less-in-demand skills, and the black line separates the two groups.
- The chart suggests demand is centered on DevOps, front-end development, and Big Data.
- Examples of in-demand skills named in the text are ASP.NET, Angular.js, MongoDB, Hadoop, NoSQL, AWS, and HTML5.
- Legacy technologies such as COBOL, Mainframe, and Solaris appear among the less in-demand skills.
- The article says management titles tend to be high supply and low demand.
- It says project managers and business analysts also show the same pattern.
- The chart was built with C3.js on top of D3.js.
