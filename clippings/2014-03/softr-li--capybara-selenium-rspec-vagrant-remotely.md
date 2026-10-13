---
url: "http://www.softr.li/blog/2012/11/08/capybara-selenium-rspec-vagrant-remotely"
captured_at: "2014-03-12T09:22:11-03:00"
title: "Capybara using Selenium, with RSpec, in the Vagrant (remotely) - softr.li"
domain: "softr-li"
---

# Capybara Using Selenium, With RSpec, in the Vagrant (Remotely)

Nov 8th, 2012

### Let’s assume:

- you’re using RSpec for your tests,
- you use Capybara for your integration/acceptance specs,
- you run your tests in a Vagrant box.

Let’s also say everything is working fine (I won’t deal with any issue you may have before this point).

Now, **you have some features / user stories / whatever that requires some Javascript action**.

### Well.

**If you weren’t using Vagrant**, I’d say everything should go fine too. Just append `:js => true` to your RSpec example, it will use Selenium and everything will go fine using your installed Firefox binary.

But **you’re testing in a Vagrant box**. So here’s what you’ll get:

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` Failure/Error: visit "/whatever"      Selenium::WebDriver::Error::WebDriverError:        Could not find Firefox binary (os=linux). Make sure Firefox is installed or set the path manually with Selenium::WebDriver::Firefox::Binary.path= ``` |

### So you may say, fine, let’s install Firefox!

But… your Vagrant box is meant to be **used in headless mode**, and Firefox requires something to draw on. Still, you may have it to work. But I’ll assume (again) that **you don’t want to bother with setting things for the client-side of the test on the development/test box** (which is more server-side) **, and use everything that’s already on you real development machine** (your day-to-day browsers).

*If my assumption is false, you can have a look to [this article](http://www.without-brains.net/blog/2012/08/01/capybara-and-selenium-with-vagrant/), which explains both approaches (but not for RSpec, that’s the why of this article).*

### The solution? selenium server!

What you want is Capybara to use its selenium driver, but **instead of running a local copy of the browser**, use [selenium server](http://seleniumhq.org/download/) which will **allows Capybara to use browsers running in your real development machine** (the host of your Vagrant development box).

### Ok I got it, how do I do it?

[This article](http://www.without-brains.net/blog/2012/08/01/capybara-and-selenium-with-vagrant/) is pretty well made, with far more explanations that I provide, so I encourage you to have a look to fully understand how it works. However, **it doesn’t provide the solution if you’re using RSpec**, since it builds a simple `Unit::TestCase` example.

**This is where I truly do something.**

### Here’s how to get it working with RSpec (and even in Spork)

Add this one line in your `spec_helper.rb` file (one line?!!!):

|  |  |
| --- | --- |
| ``` 1 ``` | ```   require_relative 'support/capybara_remote' ``` |

After the `require 'capybara/rspec'` would be great. If you’re using Spork, it should be in the `prefork` block.

Well, not truly a one-liner. Add this to a `spec/support/capybara_remote.rb` file too:

|  |  |
| --- | --- |
| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 | # SELENIUM\_SERVER is the IP address or hostname of the system running Selenium  # Server, this is used to determine where to connect to when using one of the  # selenium\_remote\_\* drivers  SELENIUM\_SERVER = "10.10.11.1"  # SELENIUM\_APP\_HOST is the IP address or hostname of this system (where the  # tests run against) as reachable for the SELENIUM\_SERVER. This is used to set  # the Capybara.app\_host when using one of the selenium\_remote\_\* drivers  SELENIUM\_APP\_HOST = "10.10.11.2"  # CAPYBARA\_DRIVER is the Capybara driver to use, this defaults to Selenium with  # Firefox  CAPYBARA\_DRIVER = "selenium\_remote\_firefox"  # At this point, Capybara.default\_driver is :rack\_test, and  # Capybara.javascript\_driver is :selenium. We can't run :selenium in the Vagrant box,  # so we set the javascript driver to :selenium\_remote\_firefox which we're going to  # configure.  Capybara.javascript\_driver = :selenium\_remote\_firefox  RSpec.configure do |config|  config.before(:each) do  if selenium\_remote?  Capybara.app\_host = "http://#{SELENIUM\_APP\_HOST}:#{page.driver.rack\_server.port}"  config.after(:each) do  Capybara.reset\_sessions!  Capybara.use\_default\_driver  Capybara.app\_host = nil  # Determines if a selenium\_remote\_\* driver is being used  def selenium\_remote?  !(Capybara.current\_driver.to\_s =~ /\Aselenium\_remote/).nil?  # CapybaraDriverRegistrar is a helper class that enables you to easily register  # Capybara drivers  class CapybaraDriverRegistrar  # register a Selenium driver for the given browser to run on the localhost  def self.register\_selenium\_local\_driver(browser)  Capybara.register\_driver "selenium\_#{browser}".to\_sym do |app|  Capybara::Selenium::Driver.new(app, browser: browser)  # register a Selenium driver for the given browser to run with a Selenium  # Server on another host  def self.register\_selenium\_remote\_driver(browser)  Capybara.register\_driver "selenium\_remote\_#{browser}".to\_sym do |app|  Capybara::Selenium::Driver.new(app, browser: :remote, url: "http://#{SELENIUM\_SERVER}:4444/wd/hub", desired\_capabilities: browser)  # Register various Selenium drivers  CapybaraDriverRegistrar.register\_selenium\_remote\_driver(:firefox) |

Be sure to adjust the constants (`SELENIUM_SERVER`, `SELENIUM_APP_HOST`, `CAPYBARA_DRIVER`) to match your configuration (as explained in the comments).

Now, get the selenium server `.jar` and run it on your real machine (the host of your Vagrant) with this command:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` java -jar selenium-server-standalone-2.25.0.jar ``` |

Now, any RSpec example with the `:js => true` metadata should be running in your Firefox browser on your real machine, where you can see it!

### Wrapping up

We’ve seen how to use **selenium server** to allow **Capybara** running in a **Vagrant box** to use the host’s **browsers** to run **RSpec** specs requiring **Javascript**.

### References
