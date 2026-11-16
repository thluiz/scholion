---
url: "https://blogs.windows.com/msedgedev/2019/11/12/enterprise-new-tab-page"
captured_at: "2026-11-16T02:50:19+00:00"
title: "Find your flow with the Enterprise New Tab Page"
domain: "blogs-windows-com"
---

How much time do you think you spend looking for things at work? Because our files and information are stored in so many places it’s probably quite a bit. In fact, according to McKinsey, we spend 20% of our work week just searching for internal information, tracking down colleagues, and trying to pick up where we left off.  That’s one whole day a week.

That’s why we’re excited for you to try a new way to manage your work with the new Microsoft Edge, now available in [Microsoft Edge Insider preview builds](https://www.microsoftedgeinsider.com/download?form=MI13E8&OCID=MI13E8). When signed in with an Azure Active Directory work account, opening a new tab in Microsoft Edge delivers a dynamic and personalized set of your most relevant Office documents, internal web sites, company resources, and other Microsoft 365 content.

Each new tab layout is populated by features that leverage the intelligence of the Office 365 graph to find what you need, right when you need it.

*   **Microsoft Search in Bing****:** Search bar for the web _and_ the intranet; find people, documents, and internal sites, just by searching.
*   **Dynamic Site Tiles:** Below the search bar you’ll find a set of tiles populated with your most commonly used websites or important internal sites configured by a company admin.
*   **Recommended Content:** Easy access to recently shared or often accessed files that are most important to you and your team.
*   **Recent files & sites:** Immediately below Recommended documents are lists of recent Office files (on the left) and frequently used SharePoint sites (on the right).
*   **Content and Layout Selection:** An easy toggle allows navigation between content feeds (‘Office 365’ and ‘Microsoft News’)

Please check out the additional details on the capabilities below, then try it yourself by downloading a [Microsoft Edge Insider build](https://www.microsoftedgeinsider.com/download?form=MI13E8&OCID=MI13E8). Tell us what you like, what doesn’t work for you, and anything else you think could help you find your flow on the Enterprise new tab experience.

![Screenshot showing the Enterprise New Tab Page in Microsoft edge](https://blogs.windows.com/wp-content/uploads/prod/sites/33/2019/11/9281c612c9ce8b0478344d2ff9af307a-1024x674.jpg)

## Microsoft Search in Bing

If you’re looking for something you haven’t used in a while, just perform a search. Artificial intelligence technology from Bing and personalized insights from the Microsoft Graph connect you to the best of the web and work in a single experience. Whether you’re working in SharePoint, OneDrive, Office, or Bing, and communicating with Microsoft Teams or Yammer, you can search all of your files and conversations in one place, giving you the information you need, right when you need it most. Try searching for a document, conversation, colleague, or even yourself. [Click here to explore Microsoft Search in Bing](https://www.bing.com/business/explore). You can also [click here to read documentation on how to get set up and running with Microsoft Search in Bing](https://docs.microsoft.com/en-us/microsoftsearch/) in your organization.

## Dynamic Site Tiles

Eight tiles provide visual links back to the sites you use most; the algorithm to compute these is run locally on your device, based on your browsing history, also stored locally. No data needs to leave your machine for these to work. We’re also introducing a new policy enabling IT Administrators to program up to 3 of these tiles. These can be enabled via enforced policy, which pins the tile permanently or recommended policy, which allows more frequently used sites to replace that tile. Administrators will also specify the URL, title. [Click here to learn more about this policy](https://docs.microsoft.com/en-us/deployedge/microsoft-edge-policies#newtabpagemanagedquicklinks). [To learn about all Microsoft Edge policies, click here](https://docs.microsoft.com/en-us/deployedge/microsoft-edge-policies#microsoft-edge---policies).

## Recommended Content

In the face of ever-expanding file, email, and discussion traffic, the Recommended Documents feature is the ‘magic’ that surfaces what you need most. It is the intelligence that monitors all file activity and uses machine learning to produce a short list of files, saving you time and allowing you to pick up right where you left off.

The Office Graph provides brains behind the Recommended content module. The Office Graph continuously collects and analyses signals that you and your colleagues send when you work in Office 365. For example, when you and a colleague modify or view the same document, it’s a signal that you’re likely to be working together. Other signals include who you communicate with through e-mail, and who you’ve shared documents with, who your manager is, and who has the same manager as you.

With Recommended content, you’ll be served a series of cards that provide information about the content and collaboration status of a few documents that we believe you should pay attention to. For example, a Microsoft Word file that has had 3 different edits in the last day, an Excel file where you’ve been @mentioned with a couple of questions, and an important presentation your team is working on with 5 unread comments.

Each card contains easily scannable information so you can quickly prioritize what to work on next without breaking your flow.

*   **The center of the card:** features a thumbnail so you can quickly recognize the file.
*   **The top:** features an icon to indicate what type of activity is most significant and who it was associated with and when the activity occurred.
*   **At the bottom:** of the card, you’ll find the file name as well as the location of the file for reference.

Please note that for documents to appear in the Recommended section, they must be stored on OneDrive for Business or SharePoint. [Click here to learn more about the Office Graph](https://support.office.com/en-us/article/What-is-Office-Delve-1315665a-c6af-4409-a28d-49f8916878ca).

## Recent Files & Sites

Another way to stay focused and in your workflow is to organize the work you’ve been doing most recently. That’s why, immediately below Recommended documents, you’ll see lists of recent files (on the left) and frequent SharePoint sites (on the right).  Organized into 4 helpful views:

*   **Recent:** Your recently accessed files. Hovering over an item allows additional actions like pinning, sharing, and opening in browser or desktop.
*   **Pinned:** Filters your recent documents down to only those you’ve pinned.
*   **Shared with me:** A list of files that have been shared with you, whether you’ve recently opened them or not.
*   **Discover:** In discover, you’ll see a mix of both your own documents, and documents your colleagues are working on so you have additional awareness about team projects. These are documents that are stored in OneDrive for Business or SharePoint in Office 365, or that have been shared with you as attachments in emails. These documents aren’t organized according to a timeline, for example last modified, or in alphabetical order. Instead, these documents are organized according to what’s likely to be most relevant to you right now.

## Settings Flyout

In the upper right is a quick way for you to switch back to the Microsoft News content & layout choices, and coming soon, the ability to choose various layouts that best suit your flow.

![Screenshot showing the New Tab Page "Settings" flyout menu](https://blogs.windows.com/wp-content/uploads/prod/sites/33/2019/11/c086018ac1c40c005a69a4561ce84297.png)

We’re also introducing a policy enabling IT Administrators to set page content. This can be enabled via enforced policy, which prevents switching or recommended policy, which allows switching between Microsoft News and Office 365 page content. [Click here to learn more about this policy](https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Fdeployedge%2Fmicrosoft-edge-policies%23newtabpagesetfeedtype&data=04%7C01%7Ckypflug%40microsoft.com%7Ca3f7ffa32b75492c53c308d765310e4a%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637089133679049520%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C-1&sdata=h7t5mBV8n0wEX2tT0Wee661B8OYqveJKcW4UiittGvg%3D&reserved=0).  [To learn about all Microsoft Edge policies, click here](https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Fdeployedge%2Fmicrosoft-edge-policies%23microsoft-edge---policies&data=04%7C01%7Ckypflug%40microsoft.com%7Ca3f7ffa32b75492c53c308d765310e4a%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637089133679049520%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C-1&sdata=u%2F%2FeYVxgYPMVl7Rc8DGFFUO1BRSfzisAGTfc8iw8Zro%3D&reserved=0).

## Microsoft 365 Compliance

The Enterprise new tab experience integrates compliant M365 services and is architected so that your data stays within your organization’s boundaries.

*   **Microsoft Search in Bing:** Address bar and in-page search is supported by Microsoft Search in Bing. Explore the links in the “Microsoft Search in Bing” section to learn more about how your data is protected.
*   **Dynamic Site Tiles:** computed locally using local device data. For these, nothing leaves your device.
*   **Office content:** This content is powered by existing compliant M365 services like the Recommended Content service, recent file service, and recent SharePoint sites service.

If your organization needs to comply with legal or regulatory standards, [start here to learn about compliance in Microsoft 365](https://docs.microsoft.com/en-us/microsoft-365/compliance/).

## More to Come for Enterprise New Tab Experience

We are looking forward for you to [download the new Microsoft Edge](https://www.microsoftedgeinsider.com/download?form=MI13E8&OCID=MI13E8) and experience these new workflows to collect your feedback. Providing feedback is easy. Just click the smiley face in the top-right corner of the browser to let us know what you like or want to see improved:

![Screenshot highlighting the Send Feedback button in Microsoft Edge](https://blogs.windows.com/wp-content/uploads/prod/sites/33/2019/08/da6cd3c59ba79f61a9010194d89e263c-300x169.png)

In the meantime, we’re working on adding support for new and compliant ways for enterprise end users to and IT admins to personalize, configure, and use the Enterprise New Tab Page for productivity in their day-to-day workflows.

Thank you for trying out the new Microsoft Edge. We welcome your comments below!

– Chad Rothschiller, Senior Program Manager, Microsoft Edge  
– Matt Betz, Product Marketing Manager, Microsoft Edge
