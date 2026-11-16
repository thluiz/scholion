---
url: "https://jqueryscript.net/loading/Progress-Bar-Countdown-Timer-jQuery-circlebars.html"
captured_at: "2026-11-16T03:35:30+00:00"
title: "Circular Progress Bar And Countdown Timer With jQuery - circlebars"
domain: "jqueryscript-net"
---

![Circular Progress Bar And Countdown Timer With jQuery - circlebars](https://www.jqueryscript.net/images/Progress-Bar-Countdown-Timer-jQuery-circlebars.jpg)

Discover more

Clean Your PC

Try Spreadsheets

Shop Wall Clocks

The jQuery Circle Bars plugin makes it easier to draw animated, customizable, circular progress bars and/or countdown timers using pure CSS/CSS3.

## How to use it:

1\. Load jQuery library and the jQuery Circle Bars plugin's core JavaScript and CSS files in the html file.

`1`

`<``link` `rel``=``"stylesheet"` `href``=``"assets/circle.css"``>`

`2`

`<``script` `src``=``"//code.jquery.com/jquery.min.js"``></``script``>`

`3`

`<``script` `src``=``"assets/circle.js"``></``script``>`

2\. Load the theme CSS files of your choice in the html file.

`1`

`<``link` `rel``=``"stylesheet"` `href``=``"skins/yellowcircle.css"``>`

`2`

`<``link` `rel``=``"stylesheet"` `href``=``"skins/purplecircle.css"``>`

`3`

`<``link` `rel``=``"stylesheet"` `href``=``"skins/firecircle.css"``>`

`4`

`<``link` `rel``=``"stylesheet"` `href``=``"skins/whitecircle.css"``>`

`5`

`<``link` `rel``=``"stylesheet"` `href``=``"skins/simplecircle.css"``>`

3\. Create a basic progress indicator/countdown timer as these:

`1`

`<``div` `id``=``"myInstance"``>`

`2`

  `<``div` `class``=``"loader-bg"``>`

`3`

    `<``div` `class``=``"text"``>00:00:00</``div``>`

`4`

  `</``div``>`

`5`

`</``div``>`

`1`

`new` `Circlebar({`

`2`

    `element :` `"#myInstance"`

`3`

`});`

`4`

 

`5`

`// or`

`6`

 

`7`

`$(``".myInstance"``).Circlebar()`

4\. Config the plugin with the following options.

`01`

`Circlebar({`

`02`

 

`03`

  `// starting time`

`04`

  `startValue: 0,`

`05`

 

`06`

  `// max time`

`07`

  `maxValue: 60,`

`08`

 

`09`

  `// in milliseconds`

`10`

  `counter: 1000,`

`11`

 

`12`

  `// should the circles styling alters according to progress level`

`13`

  `triggerPercentage:` `false``,`

`14`

 

`15`

  `// timer, progress or manual`

`16`

  `type:` `"timer"``,`

`17`

 

`18`

  `// the width of the dial`

`19`

  `dialWidth: 5,`

`20`

 

`21`

  `// font size`

`22`

  `fontSize:` `"20px"``,`

`23`

 

`24`

  `// font color`

`25`

  `fontColor:` `"rgb(135, 206, 235)"``,`

`26`

 

`27`

  `// skin name`

`28`

  `skin:` `""``,`

`29`

 

`30`

  `// the size of the circle`

`31`

  `size:` `"150px"`

`32`

   

`33`

`});`

5\. You can also initialize & config the plugin via `data` attributes like so:

`01`

`<``div` `class``=``"circlebar"`

`02`

     `data-circle-startTime``=``0`

`03`

     `data-circle-maxValue``=``"90"`

`04`

     `data-circle-dialWidth``=``10`

`05`

     `data-circle-size``=``"100px"`

`06`

     `data-circle-type``=``"progress"``>`

`07`

  `<``div` `class``=``"loader-bg"``>`

`08`

      `<``div` `class``=``"text"``>00:00:00</``div``>`

`09`

  `</``div``>`

`10`

`</``div``>`

* * *

This awesome jQuery plugin is developed by [itaditya](https://www.jqueryscript.net/plus/search.php?keyword=itaditya). For more Advanced Usages, please check the [demo page](https://jqueryscript.net/demo/Progress-Bar-Countdown-Timer-jQuery-circlebars) or visit the official website.

Discover more

Try Web Tools

Learn Scripting

Build a Website

*   Prev: [Defer Image Loading Until In Viewport - jQuery Late images](https://www.jqueryscript.net/loading/Defer-Image-Loading-Until-In-Viewport-jQuery-Late-images.html)
*   Next: [Minimal Accessible Progress Bar Plugin With jQuery - aria-progressbar](https://www.jqueryscript.net/loading/Accessible-Progress-Bar-Plugin-jQuery-Aria-Progressbar.html)
