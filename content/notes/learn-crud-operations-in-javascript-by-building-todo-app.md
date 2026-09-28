---
title: "Learn CRUD Operations in JavaScript by Building TODO App"
date: '2022-04-15T16:09:15-03:00'
category: webclip
summary: 'The page explains CRUD as create, read, update, and delete, then walks through two JavaScript projects: a social media post demo and a todo app that use form validation, template literals, and local storage.'
tags: ["crud", "javascript", "todo-app", "local-storage"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Learn CRUD Operations in JavaScript by Building TODO APP"
    url: "https://www.freecodecamp.org/news/learn-crud-operations-in-javascript-by-building-todo-app/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-04/freecodecamp-org--learn-crud-operations-in-javascript-by-building-todo-app.md"
    kind: repo
---

The page defines CRUD as create, read, update, and delete, then uses a simple social media app to show how posts can be added, edited, and removed with JavaScript. It also shows basic form validation and how data can be stored in an object before rendering it with template literals.

## Reading notes

- CRUD stands for create, read, update, and delete.
- The first example is a social media app with a form on the left and posts on the right.
- The form rejects blank input and shows a message when the field is empty.
- Submitted text is stored in an object and rendered with template literals.
- Edit and delete icons use click handlers tied to the clicked element.
- Delete removes the post by moving up through parent elements.
- Edit copies the post text back into the input and removes the original post.
- The todo app uses Bootstrap for a modal form and Font Awesome for icons.
- The todo form has task title, due date, and description fields.
- Blank task titles are blocked with validation.
- Task data is stored in an array and saved to localStorage as JSON.
- New tasks are rendered from the data array with a map loop.
- Deleting a task removes it from the page, the array, and localStorage.
- Editing a task fills the modal fields with the selected task values and deletes the old entry.
- An IIFE reads data back from localStorage when the page loads.
