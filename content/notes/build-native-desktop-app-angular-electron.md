---
title: "Build a Native Desktop App with Angular and Electron"
date: '2020-02-22T12:11:43+00:00'
category: webclip
summary: 'The article shows how to bootstrap an Electron app from an Angular Electron boilerplate, rename the project, wire up the NYT API, add NgRx store, and build home and search views with Angular Material.'
tags: ["angular", "electron", "ngrx-store", "new-york-times-api"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Build a Native Desktop App with Angular and Electron"
    url: "https://dev.to/aumayeung/build-a-native-desktop-app-with-angular-and-electron-2259"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--build-native-desktop-app-angular-electron.md"
    kind: repo
---

The article walks through building a desktop app with Angular and Electron from a boilerplate repository. It renames the project to "new-york-times", adjusts Electron, Angular, and environment config files, and adds the New York Times API key and base URL so the app can request headlines and search results.

It then sets up NgRx store for menu state and search results, creates a toolbar, sidenav layout, routing, and two pages. The home page loads section-based NYT top stories, and the search page lets users query articles by keyword, date range, and sort order, then displays the returned docs in a results component.

## Reading notes

- Electron lets a web app become a cross-platform desktop app and can use Node.js features such as file handling and hardware access.
- Angular needs a boilerplate such as angular-electron to work with Electron more easily.
- The project is renamed across electron-builder.json, package.json, and angular.json to new-york-times.
- The build script in package.json adds --base-href ./ so scripts and styles load from relative paths in Electron.
- environment.ts, environment.prod.ts, and environment.dev.ts receive apikey and apiUrl values for the New York Times API.
- The app installs Angular Material and NgRx store, then generates home, search, results, toolbar, reducer, and service files.
- app.module.ts imports Angular Material modules, HttpClientModule, FormsModule, and StoreModule.forRoot(reducers).
- NytService defines search and getArticles methods that call NYT search and top stories endpoints with HttpParams.
- menu-reducer.ts and search-result-reducer.ts store menu state and article results in memory.
- app.component.ts listens for clicks outside the sidenav and closes the menu.
- app.component.html defines the sidenav with Home and Search links, plus the toolbar and router outlet.
- HomePageComponent loads NYT sections, fetches top stories for the selected section, and renders titles, dates, links, bylines, abstracts, and images.
- ArticleSearchPageComponent builds a form with keyword, start date, end date, and sort order, formats dates with moment, and dispatches the returned docs to the store.
- ArticleSearchResultsComponent reads searchResults from the store and displays headline, publication date, link, byline, lead paragraph, and snippet.
- The app uses Angular Material styling, including the prebuilt indigo-pink theme and Roboto fonts.
- The project is run with npm run ng:serve:web for browser preview and npm run electron:local for Electron preview.
- A Windows executable is built with npm run electron:windows and placed in the release folder.
