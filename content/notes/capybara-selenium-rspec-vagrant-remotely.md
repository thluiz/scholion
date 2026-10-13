---
title: "Capybara Using Selenium, With RSpec, in the Vagrant (Remotely)"
date: '2014-03-12T09:22:11-03:00'
category: webclip
summary: 'The post shows how to run Capybara JavaScript specs from a Vagrant box through Selenium Server on the host machine, so RSpec can use the real browser instead of a local Firefox inside Vagrant.'
tags: ["capybara", "selenium", "rspec", "vagrant"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Capybara using Selenium, with RSpec, in the Vagrant (remotely) - softr.li"
    url: "http://www.softr.li/blog/2012/11/08/capybara-selenium-rspec-vagrant-remotely"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-03/softr-li--capybara-selenium-rspec-vagrant-remotely.md"
    kind: repo
---

The post describes a setup where RSpec runs Capybara integration and acceptance specs inside a Vagrant box, but JavaScript examples need a browser available on the host machine. The proposed fix is to use Selenium Server so Capybara can drive the browser on the real development machine instead of trying to use Firefox inside Vagrant.

## Reading notes

- The starting point is a test stack using RSpec, Capybara, and a Vagrant box.
- JavaScript specs fail in Vagrant because Selenium cannot find a local Firefox binary.
- Installing Firefox inside the box is presented as a poor fit for a headless Vagrant environment.
- The post prefers using the browsers already installed on the developer’s machine.
- Selenium Server is the mechanism that makes Capybara talk to those host browsers.
- A linked article explains the general approach, but not the RSpec setup.
- The practical change is to require `support/capybara_remote` from `spec_helper.rb`.
- If Spork is used, that require should go in the `prefork` block.
- A support file defines `SELENIUM_SERVER`, `SELENIUM_APP_HOST`, and `CAPYBARA_DRIVER`.
- The file sets `Capybara.javascript_driver` to `:selenium_remote_firefox`.
- RSpec hooks set `Capybara.app_host` before each example and clean up after each example.
- A helper method checks whether a selenium remote driver is in use.
- A registrar class adds local and remote Selenium drivers.
- The remote driver points to `http://#{SELENIUM_SERVER}:4444/wd/hub`.
- The Selenium Server jar is launched on the host machine with `java -jar selenium-server-standalone-2.25.0.jar`.
- After that, examples marked with `:js => true` run in Firefox on the real machine.
