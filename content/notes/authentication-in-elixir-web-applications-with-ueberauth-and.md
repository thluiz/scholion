---
title: "Authentication in Elixir Web Applications with Ueberauth and Guardian: Part 1"
date: '2020-07-05T14:11:21+00:00'
category: webclip
summary: 'This post sets up a basic Phoenix app with registration and login pages, then adds Wallaby browser tests and the routes, controllers, views, and templates those pages need.'
tags: ["elixir", "phoenix", "authentication", "wallaby"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Authentication in Elixir Web Applications with Ueberauth and Guardian: Part 1"
    url: "https://thoughtbot.com/blog/authentication-in-elixir-web-applications-with-guardian-part-1"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/thoughtbot-com--authentication-in-elixir-web-applications-with-ueberauth-and.md"
    kind: repo
---

This post outlines the setup for a basic Phoenix application that will support registration, login, logout, and protected access. It chooses Guardian and Ueberauth as the authentication approach and begins by creating the pages needed for those flows.

## Reading notes

- The series builds a Phoenix app that lets a user register with email and password or Google, log in with either method, log out, and reach protected resources only after logging in.
- The tutorial assumes basic familiarity with Elixir, Phoenix, and command-line usage.
- It starts by generating a new Phoenix app named Yauth and checking that it runs.
- Browser-based feature tests are written with Wallaby, using ChromeDriver instead of PhantomJS.
- The test setup adds Wallaby as a dependency, starts it in the test helper, enables the Phoenix endpoint as a server during tests, and configures SQL sandbox mode for concurrent testing.
- A shared `FeatureCase` checks out the repository sandbox, sets shared mode when needed, starts a Wallaby session, and exposes browser-test helpers.
- The first feature tests visit `/register` and `/login` and assert that each page shows the expected form fields and social login links.
- The router maps `/register` to `RegistrationController.new/2` and `/login` to `SessionController.new/2`.
- The controllers render `:new` templates and pass a changeset and an action path even though the application does not yet have a schema.
- View modules are created for registration and session pages, along with templates for the registration form, login form, and shared social links partial.
- The registration page includes email, password, and password confirmation fields, while the login page includes email and password fields, and both pages show links for Google and Twitter.
- The post ends by noting that the next installment will add account creation and login during registration.
