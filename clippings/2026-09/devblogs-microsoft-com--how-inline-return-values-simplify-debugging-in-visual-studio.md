---
url: "https://devblogs.microsoft.com/visualstudio/how-inline-return-values-simplify-debugging-in-visual-studio-2022/"
captured_at: "2026-09-25T07:58:57+01:00"
title: "How Inline Return Values Simplify Debugging in Visual Studio 2022"
domain: "devblogs-microsoft-com"
---

Have you ever found yourself creating temporary variables just to inspect return values from functions? It’s a small task that can quickly become tedious, breaking your rhythm and cluttering up your code. Visual Studio 2022 introduces a smarter way to handle this with “Inline Return Values,” allowing you to stay focused on coding without the extra steps.

[![Image Screenshot 2024 12 03 130526](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2024/12/Screenshot-2024-12-03-130526.png)](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2024/12/Screenshot-2024-12-03-130526.png)

This new feature allows you to view return values directly in your code, right where you need them. With Copilot integration, you can go a step further by analyzing the return values in real time. It simplifies understanding and verifying your code’s behavior, cutting out unnecessary steps. Whether you’re working with native or managed code, this feature is designed to enhance your workflow, providing a seamless, intuitive debugging experience tailored to your needs.

## How It Works

Previously you might have used the return values shown in the Autos / Locals windows. These values would appear after the function has exited and returned to the caller. Inline return values show this information before the function exits and directly in the editor. And with Copilot integration, you can now receive explanations and solutions without ever leaving your code.

When you hit a breakpoint or step through your code, Visual Studio 2022 automatically displays “the value which will be returned inline, right next to the closing brace of the method. This provides immediate, clear feedback, making it easy to spot issues and verify that your functions are returning the expected results.

Gif showcasing inline return values with copilot, image

To explore the return values further, simply hover over the inline display and click “Ask Copilot” icon on the datatip. A new Copilot chat window will open, and the debugger will gather relevant context and pass it to Copilot for analysis. Copilot will not only explain why you’re seeing those values, but also provide insights into potential issues. If necessary, it can even suggest code fixes to ensure the correct return values, streamlining your debugging process.

You will experience similar Copilot-assisted variable analysis capabilities for Locals, Autos, Watch windows, and DataTips as well , learn more here : [AI-Powered Insights: Streamlining Variable Analysis with GitHub Copilot in Visual Studio – Visual Studio Blog](https://devblogs.microsoft.com/visualstudio/ai-powered-insights-streamlining-variable-analysis-with-github-copilot-in-visual-studio/)

## Tell us what you think!

We hope the inline return values feature enhances your debugging experience! As we continue to develop seamless inline data inspection, your feedback is invaluable. Consider completing our **[quick survey](https://www.surveymonkey.com/r/P3WK629)** to help us improve this feature.

If you have comments or questions about this or any other Visual Studio features, please use the [Report a Problem tool](https://learn.microsoft.com/en-us/visualstudio/ide/how-to-report-a-problem-with-visual-studio?view=vs-2022). Stay connected with the Visual Studio team by following us on [Twitter @VS\_Debugger](https://twitter.com/VS_Debugger), [Twitter @VisualStudio](https://twitter.com/VisualStudio), [YouTube](https://www.youtube.com/user/VisualStudio), and [LinkedIn.](https://www.linkedin.com/showcase/microsoft-visual-studio/)

## Author

![Harshada Hole](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2021/07/Capture-1-150x150.png)

Product Manager

Harshada Hole is a Product Manager on the Visual Studio Debugging, Diagnostics, and Copilot team.
