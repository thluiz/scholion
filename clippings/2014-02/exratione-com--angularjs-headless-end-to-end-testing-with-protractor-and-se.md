---
url: "https://www.exratione.com/2013/12/angularjs-headless-end-to-end-testing-with-protractor-and-selenium/"
captured_at: "2014-02-24T22:57:21-03:00"
title: "AngularJS Headless End to End Testing With Protractor and Selenium"
domain: "exratione-com"
---

# AngularJS Headless End to End Testing With Protractor and Selenium

By Reason
December 1, 2013
[Permalink](https://www.exratione.com/2013/12/angularjs-headless-end-to-end-testing-with-protractor-and-selenium/)

For those of you who are already somewhat familiar with Protractor and Selenium and want to skip right to the end, you might take a look at my [Vagrant VM for headless browser testing in Ubuntu](https://github.com/exratione/protractor-selenium-server-vagrant), and [Chef cookbook](https://github.com/exratione/protractor-selenium-server-cookbook) for the same. These set up a standalone server that can be used to run end to end tests of AngularJS sites in Chrome, Firefox, or PhantomJS, and address some of the issues that you will run into along the way.

What is an End to End Test?

An end to end test runs against the front-end of a fully functional application. In the case of a web application, this implies driving a browser that loads pages, runs Javascript, interacts with the DOM, fills and submits forms, and so forth. The web application is served from a machine with a fully functional backend and suitably populated database. The setup is intended to mimic as closely as possible the live application, environment, and use cases.

You might compare this with unit testing, wherein a unit test runs against a small piece of functionality in isolation. Any data that might come from the rest of the application is mocked for the purposes of a unit test.

An AngularJS Test Philosophy

A fair way to approach design of an AngularJS application is to use a REST-like backend, push all of the business logic into [services](http://docs.angularjs.org/guide/dev_guide.services.understanding_services), and treat [controllers](http://docs.angularjs.org/guide/controller) as little more than glue holding together routes, [directives](http://docs.angularjs.org/guide/directive), and the aforementioned services. When doing this, you will find that pretty much every piece of code worthy of a unit test ends up in a service and can be somewhat decoupled from [$http](http://docs.angularjs.org/api/ng.$http) requests. Thus you need only unit test the client-side business logic, and whether that involves the use of the [mock $httpBackend](http://docs.angularjs.org/api/ngMock.$httpBackend) or just ad-hoc construction of mock data is up to you. Personally I find that the latter is more easily set up and maintained.

The remaining test coverage of the codebase can be ensured with end to end tests. These by their nature will exercise directives, the glue controllers, and the functionality of the application when running against a known backend. A build and deployment system should incorporate the setup of a site database and server that is used for this purpose.

I find that a combination of more limited service-focused unit testing followed by a layer of end to end testing is more cost-effective than trying to push out to a high level of coverage for unit tests alone. Writing mock server responses for unit tests is exceedingly time-consuming, both to create the things and then to later maintain them: to my eyes it is better to use that time to set up a known database and backend and build end to end tests to run against it.

Karma and ngScenario: the Obsolete End to End Test Setup for AngularJS

The AngularJS documentation discusses the use of [Karma](http://karma-runner.github.io/) and [ngScenario](http://docs.angularjs.org/guide/dev_guide.e2e-testing) to run end to end tests against a running web application server. The ngScenario framework provides a Selenium-like API for driving a browser and the odds are good that you are already using Karma for unit tests, so it seems like a simple evolution of existing work to start using it. That said, I have not been able to make ngScenario work to my satisfaction: local tests function but the same tests running against remote sites fail for deep reasons I have not put in the time to debug. Judging by what I've read I seem to be in a minority there, unfortunately, so it's hard to say what it is that I am doing wrong.

Either way, this framework for end to end testing is now obsolete and is in the process of being replaced by Protractor. So don't put any time into it.

Protractor, WebDriver, and Selenium

[Selenium](http://en.wikipedia.org/wiki/Selenium_(software)) and [WebDriver](http://www.seleniumhq.org/projects/webdriver/) provide local and server APIs for driving a browser and manipulating and inspecting the DOM on loaded pages - and thus running tests against a site. Selenium, like most of the tools in this ecosystem, is presently evolving into a new configuration, but is reliable. A typical Selenium set up is:

- A Selenium standalone server listens at a port for API commands.
- Commands arrive indicating that Selenium should start a browser session.
- Selenium loads a WebDriver implementation to control a particular browser.
- The browser is started and pointed to a web site, usually on another server.

Typically test scripts run on server A and connect to Selenium on server B. Selenium fires up a browser on server B to connect to a web application running on server C. The test scripts on server A instruct Selenium on server B to drive the browser around the site served from server C, checking the state of the DOM and content in response to various actions.

It is perfectly possible, but painful, to write end to end tests for an AngularJS site using only Selenium tools. The challenge lies in determining when AngularJS is actually done with a given action, such as a change of view - this is somewhat more difficult than is the case for straightforward old-school AJAX operations. So Selenium test scripts for AngularJS tend to bloat with wait commands and checks.

[Protractor](https://github.com/angular/protractor) is a Node.js framework that sits on top of the Selenium / WebDriver APIs. It acts as an abstraction layer to make it easier to write and run end to end tests against AngularJS web applications.

Using Protractor With an Existing Selenium Infrastructure

If your organization has an existing Selenium infrastructure, such as a set of Selenium servers, or images that can be spun up as needed to provide controllable browsers behind the WebDriver APIs, or a third party service that does the same, then introducing Protractor is straightforward. If you are already using Selenium, then you will have QA or build environments for your web application set up for end to end testing. Thus using Protractor in this scenario is as easy as installing it, writing some tests, and running it.

To install Protractor, first [install Node.js by building from source](https://github.com/joyent/node/wiki/Installation) to get a suitably recent version. Or make use of the [Node.js binaries or installer](http://nodejs.org/download/) for your platform, one or the other. Then run:

|  |  |
| --- | --- |
|  | `sudo` `npm` `install` `-g protractor` |

Next you will need to create a configuration file, **protractor.conf.js**. If you've used Karma at all, this should look fairly familiar. The example below:

- Uses Jasmine as the test framework.
- Uses a Selenium standalone server at selenium.example.com.
- Tests against an AngularJS application running at testapp.example.com.
- Runs all the tests found in files matching spec/\*.spec.js.

|  |  |
| --- | --- |
|  | `/*global`  `describe: false,`  `protractor: false`  `*/`  `/*jshint`  `node: true,`  `strict: false`  `*/`  `/**`  `* @fileOverview`  `* An example Protractor configuration that uses a Selenium server at`  `* selenium.example.com to run tests against a web application hosted`  `* on testapp.example.com.`  `*/`  `exports.config = {`  `// -----------------------------------------------------------------`  `// Selenium Setup: An existing Selenium standalone server.`  `// -----------------------------------------------------------------`  `// The address of an existing selenium server that Protractor will use.`  `//`  `// Note that this server must have chromedriver in its path for Chromium`  `// tests to work.`  `seleniumAddress:` `'http://selenium.example.com:4444/wd/hub'``,`  `// -----------------------------------------------------------------`  `// Specify the test code that will run.`  `// -----------------------------------------------------------------`  `// Spec patterns are relative to the location of this config.`  `specs: [`  `'spec/*.spec.js'`  `],`  `// -----------------------------------------------------------------`  `// Browser and Capabilities`  `// -----------------------------------------------------------------`  `// For a full list of available capabilities, see`  `//`  `// https://code.google.com/p/selenium/wiki/DesiredCapabilities`  `// -----------------------------------------------------------------`  `// Browser and Capabilities: PhantomJS`  `// -----------------------------------------------------------------`  `// Blocking issues prevent most uses of PhantomJS and Protractor as of`  `// Q4 2013. See, for example:`  `//`  `// https://github.com/angular/protractor/issues/85`  `//`  `// It is also hard to pass through needed command line parameters.`  `/*`  `capabilities: {`  `browserName:` `'phantomjs'``,`  `version:` `''``,`  `platform:` `'ANY'`  `},`  `*/`  `// -----------------------------------------------------------------`  `// Browser and Capabilities: Chrome`  `// -----------------------------------------------------------------`  `capabilities: {`  `browserName:` `'chrome'``,`  `version:` `''``,`  `platform:` `'ANY'`  `},`  `// -----------------------------------------------------------------`  `// Browser and Capabilities: Firefox`  `// -----------------------------------------------------------------`  `/*`  `capabilities: {`  `browserName: 'firefox',`  `version: '',`  `platform: 'ANY'`  `},`  `*/`  `// -----------------------------------------------------------------`  `// Application configuration.`  `// -----------------------------------------------------------------`  `// A base URL for your application under test. Calls to browser.get()`  `// with relative paths will be prepended with this.`  `baseUrl:` `'http://testapp.example.com/index.html'``,`  `// Selector for the element housing the angular app - this defaults to`  `// body, but is necessary if ng-app is on a descendant of`  `rootElement:` `'body'``,`  `// -----------------------------------------------------------------`  `// Other configuration.`  `// -----------------------------------------------------------------`  `// The timeout for each script run on the browser. This should be longer`  `// than the maximum time your application needs to stabilize between tasks.`  `allScriptsTimeout: 11000,`  `/**`  `* A callback function called once protractor is ready and available,`  `* and before the specs are executed.`  `*`  `* You can specify a file containing code to run by setting onPrepare to`  `* the filename string.`  `*/`  `onPrepare:` `function``() {`  `// At this point, global 'protractor' object will be set up, and`  `// jasmine will be available.`  `},`  `// ----- Options to be passed to minijasminenode -----`  `jasmineNodeOpts: {`  `/**`  `* onComplete will be called just before the driver quits.`  `*/`  `onComplete:` `function` `() {},`  `// If true, display spec names.`  `isVerbose:` `true``,`  `// If true, print colors to the terminal.`  `showColors:` `true``,`  `// If true, include stack traces in failures.`  `includeStackTrace:` `true``,`  `// Default time to wait in ms before a test fails.`  `defaultTimeoutInterval: 30000`  `}`  `};` |

Jasmine tests look much like this example - only much longer once you start to get into the details of a complicated web interface. It is still far easier to write and maintain Protractor test code than the corresponding Selenium / WebDriver scripts. You might put this example into **spec/example.spec.js**:

|  |  |
| --- | --- |
|  | `/*global`  `beforeEach: false,`  `browser: false,`  `by: false,`  `describe: false,`  `expect: false,`  `it: false,`  `protractor: false`  `*/`  `describe(``'Example:'``,` `function` `() {`  `'use strict'``;`  `beforeEach(``function` `() {`  `// Load up a view and wait for it to be done with its rendering and epicycles.`  `browser.get(``'#/example'``);`  `browser.waitForAngular();`  `});`  `it(``'view title'``,` `function` `() {`  `var` `element = browser.findElement(by.css(``'.page-header h4'``));`  `expect(element.isDisplayed()).toBe(``true``);`  `expect(element.getText()).toBe(``'An example route'``);`  `});`  `});` |

Now to run your tests:

|  |  |
| --- | --- |
|  | `protractor` `/path/to/protractor``.conf.js` |

Selenium may or may not be running the browsers headless, but it doesn't matter to you because that all happens on another server, far, far away from your uncluttered screen.

Protractor Tests are Promise-Based and Asynchronous

Consider a set of commands such as:

|  |  |
| --- | --- |
|  | `var` `element = browser.findElement(by.css(``'.page-header h4'``));`  `expect(element.isDisplayed()).toBe(``true``);`  `expect(element.getText()).toBe(``'An example route'``);` |

What is actually happening here? These commands are not running synchronously: behind the scenes they are being queued up to await completion of browser actions. The return values for **element.isDisplayed()** and **element.getText()** are promises, to be resolved at a later date, not the actual values from the DOM. The key here is to understand that **expect()** effectively unwraps promises, waiting on their resolution to run any associated assertion.

You can structure much of your Protractor test code as above so as to ignore the asynchronous activity taking place under the hood. Flow control (loops, if-else, and so on) in response to returned values is a pain, however, so you'll probably want to read up on how to that when it comes to be necessary, and avoid it when it isn't.

Setting up a Selenium Standalone Server on Ubuntu 12.04

What if you don't have an existing Selenium infrastructure to work with? Third party services such as [Sauce Labs](https://saucelabs.com/) are one option - there is something to be said for not managing your own Selenium servers, especially if you absolutely must test on many, many different combinations of OS and browser. Even using virtual machines, and integrating them into the build process, it's a pain to set up, maintain, and use twenty different test environments.

The following outline shows how to set up a Selenium standalone server to run on an Ubuntu server without a GUI, such that it can run headless with Chrome, Firefox, and PhantomJS. This is really only a fraction of the picture for even a simple Selenium infrastructure of course - you will also need Windows machines for the various major IE versions and Safari, and a solution for mobile browsers. But this is a starting point, and it illustrates some of the pitfalls you might run into.

1. Install Node.js From Source

As noted above, install Node.js by [building from source](https://github.com/joyent/node/wiki/Installation) to get a suitably recent version.

|  |  |
| --- | --- |
|  | `cd` `/tmp`  `wget http:``//nodejs``.org``/dist/v0``.10.22``/node-v0``.10.22.``tar``.gz`  `tar` `-xf node-v0.10.22.``tar``.gz`  `cd` `node-v0.10.22`  `sudo` `.``/configure`  `sudo` `make`  `sudo` `make` `install` |

2. Install Xvfb as a Service

Firstly you'll want to set up [X virtual frame buffer (Xvfb)](https://en.wikipedia.org/wiki/Xvfb) to run as a service. Installation is trivial:

|  |  |
| --- | --- |
|  | `sudo` `apt-get` `install` `xvfb` |

Then place this start script into **/etc/init.d/xvfb**:

|  |  |
| --- | --- |
|  | `#!/bin/bash`  `#`  `# Xvfb init script for Debian-based distros.`  `#`  `# The display number used must match the DISPLAY environment variable used`  `# for other applications that will use Xvfb. e.g. ':10'.`  `#`  `# From: https://github.com/gmonfort/xvfb-init/blob/master/Xvfb`  `#`  `### BEGIN INIT INFO`  `# Provides:          xvfb`  `# Required-Start:    $remote_fs $syslog`  `# Required-Stop:     $remote_fs $syslog`  `# Default-Start:     2 3 4 5`  `# Default-Stop:      0 1 6`  `# Short-Description: Start/stop custom Xvfb`  `# Description:       Enable service provided by xvfb`  `### END INIT INFO`  `NAME=Xvfb`  `DESC=``"$NAME - X Virtual Frame Buffer"`  `SCRIPTNAME=``/etc/init``.d/$NAME`  `XVFB=``/usr/bin/Xvfb`  `PIDFILE=``/var/run/``${NAME}.pid`  `# Using -extension RANDR doesn't seem to work anymore. Firefox complains`  `# about not finding extension RANDR whether or not you include it here.`  `# Fortunately this is a non-fatal warning and doesn't stop Firefox from working.`  `XVFB_ARGS=``":10 -extension RANDR -noreset -ac -screen 10 1024x768x16"`  `set` `-e`  `if` `` [ ` ```id` `` -u` - ```ne` `0 ];` `then`  `echo` `"You need root privileges to run this script"`  `exit` `1`  `fi`  `[ -x $XVFB ] ||` `exit` `0`  `.` `/lib/lsb/init-functions`  `[ -r` `/etc/default/Xvfb` `] && .` `/etc/default/Xvfb`  `case` `"$1"` `in`  `start)`  `log_daemon_msg` `"Starting $DESC"` `"$NAME"`  `if` `start-stop-daemon --start --quiet --oknodo --pidfile $PIDFILE \`  `--background --``make``-pidfile --``exec` `$XVFB -- $XVFB_ARGS ;` `then`  `log_end_msg 0`  `else`  `log_end_msg 1`  `fi`  `log_end_msg $?`  `;;`  `stop)`  `log_daemon_msg` `"Stopping $DESC"` `"$NAME"`  `start-stop-daemon --stop --quiet --oknodo --pidfile $PIDFILE --retry 5`  `if` `[ $? -``eq` `0 ] && [ -f $PIDFILE ];` `then`  `/bin/rm` `-rf $PIDFILE`  `fi`  `log_end_msg $?`  `;;`  `restart|force-reload)`  `log_daemon_msg` `"Restarting $DESC"` `"$NAME"`  `$0 stop &&` `sleep` `2 && $0 start`  `;;`  `status)`  `status_of_proc -p $PIDFILE $XVFB $NAME &&` `exit` `0 ||` `exit` `$?`  `;;`  `*)`  `log_action_msg` `"Usage: ${SCRIPTNAME} {start|stop|status|restart|force-reload}"`  `exit` `2`  `;;`  `esac`  `exit` `0` |

Make sure it is executable, owned by root, and that the service definitions are updated:

|  |  |
| --- | --- |
|  | `sudo` `chown` `root:root` `/etc/init``.d``/xvfb`  `sudo` `chmod` `a+x` `/etc/init``.d``/xvfb`  `sudo` `update-rc.d` `/etc/init``.d``/xvfb` `defaults` |

Anything running with the environment DISPLAY=:10 will use Xvfb, meaning that the Ubuntu server can now run software with a GUI in a headless mode. As you'll quickly find out, however, most software will require some additional packages that are not present on an Ubuntu server.

3. Install Packages Required by Browsers

You will have to install these packages to keep Chrome and Firefox happy:

|  |  |
| --- | --- |
|  | `sudo` `apt-get` `install` `x11-xkb-utils xfonts-100dpi xfonts-75dpi`  `sudo` `apt-get` `install` `xfonts-scalable xserver-xorg-core`  `sudo` `apt-get` `install` `dbus-x11` |

Further, this package is necessary to prevent PhantomJS from failing silently in a very annoying fashion:

|  |  |
| --- | --- |
|  | `sudo` `apt-get` `install` `libfontconfig1-dev` |

4. Install Browsers

Installing Chrome and Firefox:

|  |  |
| --- | --- |
|  | `sudo` `apt-get` `install` `chromium-browser firefox` |

Installing PhantomJS via NPM:

|  |  |
| --- | --- |
|  | `sudo` `npm` `install` `-g phantomjs` |

5. Install WebDriver Implementations

WebDriver implementations for PhantomJS (called Ghostdriver) are bundled with the PhantomJS installation. For Firefox the implementation comes included with Selenium standalone server. This leaves Chromium, and the easiest way to install the [ChromeDriver](http://code.google.com/p/selenium/wiki/ChromeDriver) package is to get the Node.js implementation via NPM:

|  |  |
| --- | --- |
|  | `sudo` `npm` `install` `-g chromedriver` |

6. Install Java If Not Already Present

If you don't have Java out of the box, then install the default version.

|  |  |
| --- | --- |
|  | `sudo` `apt-get` `install` `default-jdk` |

7. Set Up the Selenium Standalone Server as a Service

The Selenium standalone server comes as a single packaged JAR file. We want to create a user to run the service, create a directory to place the JAR into and then download it. Note that the Selenium user absolutely must have a home directory. If we run the Selenium service with this user, then the browsers will also run as this user, as it is Selenium that is piloting the browsers as directed by the test scripts. Firefox especially will be cranky if it is running under a user with no home directory.

|  |  |
| --- | --- |
|  | `sudo` `/usr/sbin/useradd` `-m -s` `/bin/bash` `-d` `/home/selenium` `selenium`  `sudo` `mkdir` `/usr/local/share/selenium`  `wget http:``//selenium``.googlecode.com``/files/selenium-server-standalone-2``.37.0.jar`  `sudo` `mv` `selenium-server-standalone-2.37.0.jar` `/usr/local/share/selenium`  `sudo` `chown` `-R selenium:selenium` `/usr/local/share/selenium` |

We will also want a log directory for Selenium:

|  |  |
| --- | --- |
|  | `sudo` `mkdir` `/var/log/selenium`  `sudo` `chown` `selenium:selenium` `/var/log/selenium` |

Place the following start script into **/etc/init.d/selenium**, and note that it uses the same DISPLAY value as for the Xvfb start script above:

|  |  |
| --- | --- |
|  | `#!/bin/bash`  `#`  `# Selenium standalone server init script.`  `#`  `# For Debian-based distros.`  `#`  `### BEGIN INIT INFO`  `# Provides:          selenium-standalone`  `# Required-Start:    $local_fs $remote_fs $network $syslog`  `# Required-Stop:     $local_fs $remote_fs $network $syslog`  `# Default-Start:     2 3 4 5`  `# Default-Stop:      0 1 6`  `# Short-Description: Selenium standalone server`  `### END INIT INFO`  `DESC=``"Selenium standalone server"`  `USER=selenium`  `JAVA=``/usr/bin/java`  `PID_FILE=``/var/run/selenium``.pid`  `JAR_FILE=``/usr/local/share/selenium/selenium-server-standalone-2``.37.0.jar`  `LOG_FILE=``/var/log/selenium/selenium``.log`  `DAEMON_OPTS=``"-Xmx500m -Xss1024k -jar $JAR_FILE -log $LOG_FILE"`  `# See this Stack Overflow item for a delightful bug in Java that requires the`  `# strange-looking java.security.egd workaround below:`  `# http://stackoverflow.com/questions/14058111/selenium-server-doesnt-bind-to-socket-after-being-killed-with-sigterm`  `DAEMON_OPTS=``"-Djava.security.egd=file:/dev/./urandom $DAEMON_OPTS"`  `# The value for DISPLAY must match that used by the running instance of Xvfb.`  `export` `DISPLAY=:10`  `# Make sure that the PATH includes the location of the ChromeDriver binary.`  `# This is necessary for tests with Chromium to work.`  `export` `PATH=$PATH:``/usr/local/bin`  `case` `"$1"` `in`  `start)`  `echo` `"Starting $DESC: "`  `start-stop-daemon -c $USER --start --background \`  `--pidfile $PID_FILE --``make``-pidfile --``exec` `$JAVA -- $DAEMON_OPTS`  `;;`  `stop)`  `echo`  `"Stopping $DESC: "`  `start-stop-daemon --stop --pidfile $PID_FILE`  `;;`  `restart)`  `echo` `"Restarting $DESC: "`  `start-stop-daemon --stop --pidfile $PID_FILE`  `sleep` `1`  `start-stop-daemon -c $USER --start --background \`  `--pidfile $PID_FILE  --``make``-pidfile --``exec` `$JAVA -- $DAEMON_OPTS`  `;;`  `*)`  `echo` `"Usage: /etc/init.d/selenium-standalone {start|stop|restart}"`  `exit` `1`  `;;`  `esac`  `exit` `0` |

As before, make sure it is executable, owned by root, and that the service definitions are updated:

|  |  |
| --- | --- |
|  | `sudo` `chown` `root:root` `/etc/init``.d``/selenium`  `sudo` `chmod` `a+x` `/etc/init``.d``/selenium`  `sudo` `update-rc.d` `/etc/init``.d``/selenium` `defaults` |

8. Work Around a Protractor / PhantomJS Issue

You will have to create a default logfile for the PhantomJS WebDriver that is writable by the selenium user, as it will otherwise not be able to create it. It is possible to tell PhantomJS to put the log file somewhere else, but not via Protractor and Selenium at this point.

|  |  |
| --- | --- |
|  | `sudo` `touch` `/phantomjsdriver``.log`  `sudo` `chmod` `666` `/phantomjsdriver``.log` |

9. Done!

This Ubuntu machine is now a Selenium server listening on port 4444 for instructions to run Firefox, Chromium, or PhantomJS.

Protractor and PhantomJS Don't Play Nice Together

As of the time of writing there is a [known issue](https://github.com/angular/protractor/issues/85) that prevents PhantomJS from working with Protractor. Hopefully this will be fixed at some point in the near future, though admittedly if you can run headless Chrome there is less of a need to include PhantomJS in your browser stable.

Imagemagick or Similar Required for Snapshots

If you want the ability to take screen snapshots, then you are going to have to install imagemagick at a minimum on your Selenium server:

|  |  |
| --- | --- |
|  | `sudo` `apt-get` `install` `imagemagick` |

A Vagrant / Chef Configuration For All of the Above

Rather than do all of this work, you could instead use Vagrant and Chef to launch and provision an Ubuntu virtual machine with Protractor, Selenium standalone server, and Chome, Firefox, and PhantomJS ready for use:
