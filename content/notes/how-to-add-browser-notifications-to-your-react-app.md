---
title: "How to Add Browser Notifications to Your React App"
date: '2020-02-22T12:11:43+00:00'
category: webclip
summary: 'Explains how to use the HTML5 Notification API and react-web-notification in a React password manager, including permission handling and notifications for add, edit, copy, and delete actions.'
tags: ["react", "browser-notifications", "notification-api", "password-manager"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to Add Browser Notifications to Your React App - The Web Dev"
    url: "https://web.archive.org/web/20201101014159id_/https://thewebdev.info/2020/01/16/how-to-add-browser-notifications-to-your-react-app/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--how-to-add-browser-notifications-to-your-react-app.md"
    kind: repo
---

The page shows how to use the HTML5 Notification API in a React app and how to rely on react-web-notification to display native popup notifications and handle notification events. It also builds a password manager that shows notifications when passwords are added, edited, copied, or deleted.

## Reading notes

- Browsers can display native popup notifications with the HTML5 Notification API, including text, icons, and sound.
- Users must grant permission before a web app can show browser notifications.
- React-Web-Notification is presented as a React component for showing popups and handling click, permission granted, and permission denied events.
- The example app is a password manager built with React.
- Create React App is used to start the project.
- The app uses Axios for HTTP requests, Formik and Yup for forms and validation, MobX for state management, React Bootstrap for styling, React-Copy-To-Clipboard for clipboard actions, and React Router for routing.
- `App.js` adds a React Bootstrap navbar and a route to the home page.
- `HomePage.js` renders a table of passwords, modal dialogs for adding and editing entries, and buttons for copying usernames and passwords, editing entries, and deleting entries.
- Notifications are shown when a username or password is copied and when an entry is deleted.
- `PasswordForm.js` uses Formik and Yup to validate name, URL, username, and password fields, then calls add or edit requests and refreshes the store.
- `requests.js` defines GET, POST, PUT, and DELETE calls to a local backend at `http://localhost:3000`.
- `store.js` defines a MobX store with a passwords array and a setter action.
- `index.html` changes the page title and adds Bootstrap CSS.
- The app is run on a different port from the backend, and the backend is served with json-server using `db.json` with an empty passwords array.
