---
url: "https://dev.to/adiatiayu/how-i-built-a-curated-automated-open-source-portfolio-18o0?"
captured_at: "2025-10-22T11:20:11+01:00"
title: "How I Built a Curated, Automated Open Source Portfolio - DEV Community"
domain: "dev-to"
---

---
I've been on a continuous journey in open source since 2020. First, as a contributor, and for the last few years, also as a project maintainer. It's a space where I've learned so much and given back what I can.

I've always wanted a way to track my progress and showcase my contributions in a portfolio. It's not just about highlighting achievements; it's about monitoring growth, celebrating milestones, and having a resource to share with potential collaborators or employers.

For a long time, this was a manual, frustrating task.

## [](https://dev.to/adiatiayu/how-i-built-a-curated-automated-open-source-portfolio-18o0?#the-spreadsheet-struggle)The Spreadsheet Struggle

My first attempts at tracking were old-school. I tried maintaining a Google Sheet, logging every merged Pull Request (PR), every issue I opened, and every valuable code review. Then I tried creating a dedicated GitHub repository, where I'd manually add Markdown files for each contribution.

You can probably guess how this story goes.

Yes, life got in the way, and I became busy with other tasks. Suddenly, a few days turned into a few weeks, and before I knew it, my tracker was totally outdated. It just became stale and useless.

Once, [Polywork](https://dev.to/adiatiayu/my-impression-of-polywork-as-a-web-developer-and-a-technical-blogger-4cc1) was a great platform for showcasing my achievements. I highlighted everything, from open source contributions to recognition from notable individuals. However, it eventually came to an end.

Then, I learned about [OpenSauced](https://opensauced.pizza/), and long story short, I became one of the documentation maintainers and learned much more about the project. It was an awesome tool that had a cool feature for highlighting open source contributions, making it super easy to link my highlights page on my resume. It was the perfect solution... until it wasn't. When it was deprecated, I was back to square one.

Well, sometimes, inspiration strikes in the least expected places.

## [](https://dev.to/adiatiayu/how-i-built-a-curated-automated-open-source-portfolio-18o0?#inspiration-on-the-couch)Inspiration on the Couch

Yes, that's correct. The moment of inspiration struck me during a family summer vacation, while I was relaxing on the couch.

A few months ago, I took a long summer vacation with my family. I was intentionally tech-free, laptop-less, and simply enjoying the time together.

One day, while I was lounging on the couch and watching a series, the idea of having an open source portfolio suddenly came to mind. I thought, "There must be a way to automate this process." I decided to explore using the GitHub API to build the portfolio.

But here's the thing. I didn't have the deep API knowledge, and I certainly didn't want to ruin my family time by reading documentation for hours. 😅

So, with no laptop and stuck on this idea, I figured I’d try vibe coding a shot—something I’ve never tried before. Honestly, I’m a bit of a skeptic when it comes to AI, and I really struggle with creating effective prompts. I'm aware that if my prompts aren't optimal, I could quickly use up my free credits, and I don't want to wait a long time to get new ones.

But there will always be a first time for everything, and you don't know how it goes unless you try, right?

## [](https://dev.to/adiatiayu/how-i-built-a-curated-automated-open-source-portfolio-18o0?#the-four-filters-of-meaningful-open-source-contribution)The Four Filters of Meaningful Open Source Contribution

I want my portfolio to not only track and record all progress, but also reflect personal truths about my contributions. So, I had some ideas about what to include and exclude in the project.

### [](https://dev.to/adiatiayu/how-i-built-a-curated-automated-open-source-portfolio-18o0?#1-the-collaborative-work-why-only-tracking-outside-repos)1\. The Collaborative Work: Why Only Tracking "Outside" Repos?

I primarily contribute to and maintain projects owned by organizations or other individuals. I don’t currently have my own dedicated open source repository. This means if the tool tracks _all_ my activity, it would include things like personal configuration changes or quick sandbox tests in my own repos, which aren't open source contributions.

My portfolio must be a log of pure collaboration work. Therefore, the script had to be designed from the ground up to only capture activity (PRs, issues) outside of my personal GitHub repositories.

### [](https://dev.to/adiatiayu/how-i-built-a-curated-automated-open-source-portfolio-18o0?#2-the-ethical-line-why-exclude-private-repositories)2\. The Ethical Line: Why Exclude Private Repositories?

As a contributor or maintainer, I sometimes interact with private repositories belonging to the organizations I work with. Including these activities in a public portfolio feels ethically wrong—I don't own the data, and the work is not (yet) open source.

To keep the portfolio clean, public, and ethically sound, the script needed a strict filter to exclude all contributions made in any organization's private repositories.

### [](https://dev.to/adiatiayu/how-i-built-a-curated-automated-open-source-portfolio-18o0?#3-the-quality-filter-why-ignore-bots-and-routine-merges)3\. The Quality Filter: Why Ignore Bots and Routine Merges?

As a maintainer, a significant chunk of my workflow is routine: reviewing and merging PRs from bots like Dependabot. While this is important hygiene work, it doesn't showcase my technical expertise or human interaction.

Therefore, the log needed to reflect genuine human collaboration. The solution had to actively exclude any PRs that were reviewed, merged, or closed if they were authored by a bot account.

### [](https://dev.to/adiatiayu/how-i-built-a-curated-automated-open-source-portfolio-18o0?#4-capturing-the-quiet-value-why-track-collaborations)4\. Capturing the Quiet Value: Why Track "Collaborations"?

Maintainer tasks aren't just about merging PRs. So much value is created by answering questions, providing technical advice, helping a new contributor debug an issue in a comment thread, or explaining why an issue/PR is closed or reopened, without ever needing to hit the "Submit review" button. This is crucial work, but it's often invisible and unrecognized.

My portfolio must capture these kinds of contributions. The script needed a dedicated category to track "Collaborations"—any issue or PR where I commented to discuss or assist, but didn't submit a formal review.

I needed to filter information, set ethical boundaries, and consider efforts as a whole. So, I decided to create a smart, opinionated tracker.

## [](https://dev.to/adiatiayu/how-i-built-a-curated-automated-open-source-portfolio-18o0?#building-an-automation-from-my-phone)Building an Automation from My Phone

This project, the [**Curated Open Source Portfolio**](https://github.com/adiati98/oss-portfolio), was built using my phone.

I pieced together the project using my smartphone, the GitHub mobile app, a mobile browser, and [Gemini 2.5 Flash](https://gemini.google.com/) as my AI coding assistant (because it's free!).

It was a tough way to work. The small screen made navigation and testing a nightmare. The only way to test my changes was to push them directly to my `main` branch and let the GitHub Action workflow run. It was an intense, time-consuming debugging process.

I was relying heavily on the AI to help me structure the Node.js script and compose the necessary GitHub API queries.

## [](https://dev.to/adiatiayu/how-i-built-a-curated-automated-open-source-portfolio-18o0?#automation-achieved)Automation Achieved

My Curated Open Source Portfolio is a system that finally puts my contribution tracking on autopilot. What used to take me hours of manual logging and formatting now happens automatically in minutes. It’s built around a Node.js script and a GitHub Actions workflow, adhering strictly to my definition of a valuable, ethical contribution.

Here’s how the project works:

### [](https://dev.to/adiatiayu/how-i-built-a-curated-automated-open-source-portfolio-18o0?#1-a-nodejs-script-the-brain)1\. A Node.js Script (The Brain)

This script uses the GitHub API to find my activity. The core here is the "Smart Syncing" logic, which dictates _how_ and _what_ data is fetched. To balance efficiency and data integrity, the script is designed to run in two modes:

-   A fast **incremental update**, which fetches only new activity to minimize API calls and keep the system running efficiently.
    
-   A **full synchronization**, which rebuilds the portfolio from scratch to clear the cache and verify all data since the tracking began.
    

The script then applies the “Four Filters” and looks for four key contribution types outside of my own repositories:

-   **Merged PRs:** Tracking my PRs that are merged
    
-   **Issues:** Tracking bug reports or feature requests that I submitted
    
-   **Reviewed PRs:** Tracking PRs that I formally review
    
-   **Collaborations:** Tracking my first comments and discussions on someone else's issues/PRs
    

Achieving all four ethical filters required careful query construction. For instance, to ensure quality and collaboration, the search query for finding reviewed PRs had to use specific exclusion filters. This is one part of the complex query string the script generates:  

```
<span>// Snippet of the search query logic:</span>
<span>`is:pr -author:</span><span>${</span><span>GITHUB_USERNAME</span><span>}</span><span> ... -user:dependabot -user:github-actions[bot] updated:&gt;=</span><span>${</span><span>yearStart</span><span>}</span><span>`</span>
```

The complete solution uses a combination of these search operators and additional JavaScript logic in the script to ensure that no PRs from known bots or contributions within my personal repositories are included in the final report.

### [](https://dev.to/adiatiayu/how-i-built-a-curated-automated-open-source-portfolio-18o0?#2-a-github-actions-workflow-the-automation)2\. A GitHub Actions Workflow (The Automation)

This is what makes it hands-free. It has two schedules, effectively minimizing API requests while ensuring total data history:

1.  A light **daily update** (`'0 1 * * *'`) that triggers the script's incremental sync to keep things fresh.
    
2.  A thorough **monthly full sync** (`'1 0 1 * *'`) that initiates a complete data refresh. It deletes the local cache and data files to rebuild the entire contribution history from the year I started tracking, ensuring accuracy.
    

The Action runs the script, and then automatically commits the newly generated Markdown reports back to the repository.

The final output is a collection of detailed, quarterly Markdown reports that summarize my work, including statistics and top contributed projects. It's a clean, verifiable, and constantly updated portfolio that I can be proud of.

[![Quarterly Markdown reports in Markdown that summarize open source contributions, including statistics and top contributed projects](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fu48ecdwp9kxap5q5bu58.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fu48ecdwp9kxap5q5bu58.png)

## [](https://dev.to/adiatiayu/how-i-built-a-curated-automated-open-source-portfolio-18o0?#what-i-learned-from-vibe-coding-my-open-source-portfolio)What I Learned from Vibe Coding My Open Source Portfolio

This "vibe coding" experience taught me some invaluable lessons about building with AI, especially for developers who are still learning certain technologies.

### [](https://dev.to/adiatiayu/how-i-built-a-curated-automated-open-source-portfolio-18o0?#1-you-remain-the-architect)1\. You Remain The Architect

The AI can write the code, but you have to be the architect. You still need a fundamental understanding of what you're building. Even though I struggled with the GitHub API syntax, I understood the _logic_ of what I needed: fetch data, process it, and write it to a file. This basic knowledge lets me guide the AI effectively.

### [](https://dev.to/adiatiayu/how-i-built-a-curated-automated-open-source-portfolio-18o0?#2-be-a-critical-thinker-not-a-copypaster)2\. Be a Critical Thinker, Not a Copy-Paster

This is the biggest takeaway. Don't just accept the code the AI gives you. Get critical. Ask questions. Challenge the approach. I found that I had to push back on Gemini a lot:

-   "Can you run me through the code line by line and explain what they do?"
    
-   "That suggested query seems too complex and takes a while to process. Can we simplify it?"
    
-   "This script needs to only look for activity _outside_ of my own repositories. How can we ensure the API query handles that exclusion?"
    
-   "You're suggesting a whole new library, but can we just do this with native Node.js?"
    
-   "Why did you come with this approach and not that approach? What's the difference? What's the impact?"
    

Sometimes, the AI would change its approach and agree with a simpler solution. Other times, it would persistently suggest things that were far too complicated or unnecessary for my simple application. Always be critical, and still check your facts with a quick Google search.

Vibe coding is an accelerator, especially when you need to bridge a knowledge gap quickly (like crafting the GitHub API query without hours of documentation reading). But the final code quality—its simplicity, efficiency, and effectiveness—is entirely up to the human review and critical challenge.

## [](https://dev.to/adiatiayu/how-i-built-a-curated-automated-open-source-portfolio-18o0?#your-turn-getting-started-with-automation)Your Turn: Getting Started with Automation

If my story resonates with you—the contributor who wants to track their journey but is tired of the manual effort—I encourage you to try out this automation or build one your own!

## Curated Open Source Portfolio

This repository serves as a portfolio of my open source contributions. You can check out the contributions log in the [contributions folder](https://github.com/adiati98/oss-portfolio./contributions) to see my work.

My goal in creating this log is to maintain a detailed and organized record of my work, containing pull requests (PRs), bug reports, and general collaborations. It's a way for me to track my journey and share my contributions with the community.

The content in this repository is generated automatically using a GitHub Action. I plan to add more details and functions in the future.

___

## 💡 How It Works

This project is powered by a **Node.js script** and a **GitHub Actions workflow** that automatically fetches, processes, and presents GitHub activity.

### The Brain: The Automation Script

The core logic is designed to track and categorize activity **outside of the owner's own repositories**. The script performs the following key functions:

1.  **Smart**…
    

  

  
  

You can finally focus on what matters most: **contributing to open source**, not managing a spreadsheet.

## [](https://dev.to/adiatiayu/how-i-built-a-curated-automated-open-source-portfolio-18o0?#looking-ahead-and-staying-critical)Looking Ahead and Staying Critical

While the current system is stable and fully automated, this project is far from finished. I plan to add more features in the future. This ongoing development means one thing is constant: I must continue to manually check and refine the code the AI helped generate. I'll focus on ensuring the logic—from the Node.js implementation to the underlying data requests—remains simple, efficient, and, most importantly, true to the ethical and collaborative principles on which I built this portfolio.

This project is a testament to the power of a good idea, even if it starts on a phone during a vacation. It shows that with modern AI tools, you don't need to be an API expert to build sophisticated solutions. You only need curiosity, critical thinking, and a willingness to try something new.

What are you building with the help of AI to make your life easier as a developer? I'd love to hear your stories!
