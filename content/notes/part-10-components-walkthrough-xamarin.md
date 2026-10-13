---
title: "Part 10 - Components Walkthrough | xamarin"
date: '2013-08-05T13:55:33-03:00'
category: webclip
summary: 'The page shows how Xamarin Components work in iOS and Android apps and walks through adding one from the Xamarin Components Store in Xamarin Studio or Visual Studio.'
tags: ["xamarin-components", "xamarin-studio", "visual-studio", "component-store"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Part 10 - Components Walkthrough | xamarin"
    url: "http://docs.xamarin.com/guides/cross-platform/application_fundamentals/components_walkthrough"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-08/docs-xamarin-com--part-10-components-walkthrough-xamarin.md"
    kind: repo
---

Xamarin Components provide controls, code libraries, and themes for Xamarin.iOS and Xamarin.Android apps. The walkthrough shows how to add a component from the Xamarin Components Store, using the HelloComponents project as the example.

It compares the workflow in Xamarin Studio and Visual Studio, including signing into a Xamarin account, opening the Component Manager, browsing the component list, and adding a component to the project. The page uses the Alert Center component to show how the component details include Getting Started code, samples, and assemblies, and how the sample code and image files make the app show an alert when run.

## Reading notes

- Xamarin Components include user interface controls, code libraries, and user interface themes for Xamarin.iOS and Xamarin.Android applications.
- The article focuses on how to include a component in a project and on the tool chain that makes the process seamless.
- In Xamarin Studio, the Component Manager is opened from the Components folder or the Component Manager menu option.
- Access to the Components Store requires a Xamarin Store account, and logging in is done from the Component Manager.
- In Visual Studio, a Xamarin account must be connected before creating an iOS project.
- The workflow in Visual Studio starts with Tools > Xamarin Account, then File > New > Project, then Get More Components from the Components folder.
- The Components List supports searching by name, filtering by category and tag, sorting by featured status, downloads, and name, suggesting components, submitting components, and selecting a component for a project.
- The Alert Center component is added by opening its page and choosing Add to Project.
- The component detail screen includes Getting Started, Samples, and Assemblies.
- The Getting Started tab provides code snippets, and the article shows code that posts a message through AlertCenter.Default.PostMessage.
- The example also requires a sample_icon.png image, and the article mentions Default-568h@2x.png for full-screen launch on iPhone 5.
- After adding the code and images, running the application displays an alert.
