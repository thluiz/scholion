---
title: "Create a blog reader (Windows Store apps using JavaScript and HTML) (Windows)"
date: '2013-02-04T04:24:11-03:00'
category: webclip
summary: 'Tutorial that shows how to build a blog reader with the Split App template, load RSS feeds with Windows.JS.xhr, bind data to a ListView, and move between pages and post details.'
tags: ["windows-store-apps", "javascript", "listview", "rss"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Part 6: Create a blog reader (Windows Store apps using JavaScript and HTML) (Windows)"
    url: "http://msdn.microsoft.com/en-us/library/windows/apps/hh974582.aspx?utm_source=javascriptweekly&utm_medium=email"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-02/msdn-microsoft-com--create-a-blog-reader-windows-store-apps-using-javascript-and.md"
    kind: repo
---

This tutorial shows how to use the Split App Visual Studio template to build a Windows Store blog reader in JavaScript and HTML. It replaces sample data with ATOM feed data, binds blogs and posts to a ListView, and adds navigation to a split page and an item detail page.

## Reading notes

- Starts from the Split App template and creates a project named WindowsBlogReader.
- Uses PageControl files for the items page, split page, and item detail page.
- Replaces the template sample data in data.js with hard-coded blog feed URLs.
- Uses WinJS.xhr to fetch RSS or ATOM feed content asynchronously.
- Uses WinJS.Promise.join to wait for all feed requests before showing the ListView.
- Reads feed metadata with responseXML and querySelector, then formats dates with Windows.Globalization.DateTimeFormatting.DateTimeFormatter.
- Stores blog post data in a WinJS.Binding.List and groups items by blog.
- Updates the items page template to show the blog title and last updated date.
- Updates the split page template to show the post date, title, and author, while removing unused sample fields.
- Adds styling for the blog tiles, the split page date block, and the article layout.
- Adds an item detail PageControl that shows the selected post title and content.
- Adds an AppBar button labeled Full View that is hidden on the items and detail pages and shown on the split page.
- Uses WinJS.Navigation.navigate to open the item detail page with the selected post.
- Notes that the template already handles landscape and portrait layouts.
