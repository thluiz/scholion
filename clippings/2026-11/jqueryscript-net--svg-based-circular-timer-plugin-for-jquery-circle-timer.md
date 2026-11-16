---
url: "https://jqueryscript.net/time-clock/SVG-Based-Circular-Timer-Plugin-For-jQuery-Circle-Timer.html"
captured_at: "2026-11-16T03:33:44+00:00"
title: "SVG Based Circular Timer Plugin For jQuery - Circle Timer"
domain: "jqueryscript-net"
---

![SVG Based Circular Timer Plugin For jQuery - Circle Timer](https://www.jqueryscript.net/images/SVG-Based-Circular-Timer-Plugin-For-jQuery-Circle-Timer.jpg)

Discover more

jQuery tutorials

jQuery plugins

Plugin development service

Circle Timer is a very lightweight jQuery plugin that lets you create a SVG-based circular pie-style countdown timer and triggers a custom callback function once the timer is complete.

## See also:

*   [Graphical and Circular Timer with jQuery and CSS3 - pietimer](https://www.jqueryscript.net/loading/Graphical-Circular-Timer-with-jQuery-CSS3-pietimer.html)
*   [Circular Pie-Style Countdown Timer Plugin with jQuery - Pietimer](https://www.jqueryscript.net/time-clock/Circular-Pie-Style-Countdown-Timer-Plugin-with-jQuery-Pietimer.html)

## How to use it:

1\. Add references to jQuery library, `circletimer.min.js` and `circletimer.css` in your document.

`1`

`<``script` `src``=``"jquery.min.js"``></``script``>`

`2`

`<``script` `src``=``"dist/circletimer.min.js"``></``script``>`

`3`

`<``link` `href``=``"dist/circletimer.css"` `rel``=``"stylesheet"``>`

2\. Create the html elements for the countdown timer.

`1`

`<``div` `id``=``"example-timer"``></``div``>`

`2`

`<``p``>Time Elapsed: <``span` `id``=``"time-elapsed"``>0</``span``>ms</``p``>`

3\. Create controls to start, stop, pause, resume the countdown timer.

`1`

`<``button` `id``=``"start"``>Start</``button``>`

`2`

`<``button` `id``=``"pause"``>Pause</``button``>`

`3`

`<``button` `id``=``"stop"``>Stop</``button``>`

4\. Initialize the countdown timer and enable the controls.

`01`

`$(document).on(``"ready"``,` `function``() {`

`02`

  `$(``"#example-timer"``).circletimer({`

`03`

    `onComplete:` `function``() {`

`04`

      `alert(``"Time is up!"``);`

`05`

    `},`

`07`

      `$(``"#time-elapsed"``).html(Math.round(elapsed));`

`08`

    `},`

`09`

    `timeout: 5000`

`10`

  `});`

`11`

 

`12`

  `$(``"#start"``).on(``"click"``,` `function``() {`

`13`

    `$(``"#example-timer"``).circletimer(``"start"``);`

`14`

  `});`

`15`

 

`16`

  `$(``"#pause"``).on(``"click"``,` `function``() {`

`17`

    `$(``"#example-timer"``).circletimer(``"pause"``);`

`18`

  `});`

`19`

 

`20`

  `$(``"#stop"``).on(``"click"``,` `function``() {`

`21`

    `$(``"#example-timer"``).circletimer(``"stop"``);`

`22`

  `});`

`23`

`})`

4\. Default options.

`01`

`$(``"#example-timer"``).circletimer({`

`02`

 

`03`

  `// timeout`

`04`

  `timeout: 5000,`

`05`

 

`06`

  `// callbacks`

`07`

  `onComplete: (``function``() {}),`

`08`

  `onUpdate: (``function``() {})`

`09`

   

`10`

`});`

## Change log:

2015-12-12

*   v1.0.0

2015-08-22

*   Add option to increase time while timer is going

* * *

This awesome jQuery plugin is developed by [abejfehr](https://www.jqueryscript.net/plus/search.php?keyword=abejfehr). For more Advanced Usages, please check the [demo page](https://jqueryscript.net/demo/SVG-Based-Circular-Timer-Plugin-For-jQuery-Circle-Timer) or visit the official website.

Discover more

script

Learn Java

Try Dev Tools

*   Prev: [Circular Pie-Style Countdown Timer Plugin with jQuery - Pietimer](https://www.jqueryscript.net/time-clock/Circular-Pie-Style-Countdown-Timer-Plugin-with-jQuery-Pietimer.html)
*   Next: [Simple Daily Schedule Plugin with jQuery and jQuery UI - Schedule](https://www.jqueryscript.net/time-clock/Simple-Daily-Schedule-Plugin-with-jQuery-and-jQuery-UI-Schedule.html)
