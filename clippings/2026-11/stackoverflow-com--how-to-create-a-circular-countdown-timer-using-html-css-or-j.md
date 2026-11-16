---
url: "https://stackoverflow.com/questions/29649643/how-to-create-a-circular-countdown-timer-using-html-css-or-javascript"
captured_at: "2026-11-16T17:50:46+00:00"
title: "How to create a circular countdown timer using HTML, CSS or JavaScript?"
domain: "stackoverflow-com"
---

Currently, I am working on a quiz game and in that, for each question, I wish to place a countdown timer. I got some plugins, but I wish if I could create it myself. What I am trying to create looks like the one in the image below.Can you please tell me how I can do it?

Is there a way to assign a border to only up to a specified percentage of the perimeter, so that I could give a border, first in full, and then as each second advances, I can keep decreasing/increasing it so that I would get it in the perfect way.

The timer I wish to create should look somewhat like this (hope you understand how its blue border will increase every second):

javascripthtmlcsstimer

asked Apr 15, 2015 at 12:00
Arun Sivaraj

almost the same question here: stackoverflow.com/questions/18835477/… – cdm
May not be 100% exactly as you want but you should get some ideas here - stackoverflow.com/questions/13059190/… – Harry

2 Answers

Answer 1 (score 63):

Here is something i was playing around with a while ago. It uses a combination of SVG, css transitions and javascript. You should be able to rip it apart and use as a starting point...

/**
* The setTimeout({},0) is a workaround for what appears to be a bug in StackSnippets.
* It should not be required. See JSFiddle version.
*/

setTimeout(function() {

var time = 10; /* how long the timer will run (seconds) */
var initialOffset = '440';
var i = 1

/* Need initial run as interval hasn't yet occured... */
$('.circle_animation').css('stroke-dashoffset', initialOffset-(1*(initialOffset/time)));

var interval = setInterval(function() {
$('h2').text(i);
if (i == time) {
clearInterval(interval);
return;
}
$('.circle_animation').css('stroke-dashoffset', initialOffset-((i+1)*(initialOffset/time)));
i++;
}, 1000);

}, 0)

.item {
position: relative;
float: left;
}

.item h2 {
text-align:center;
position: absolute;
line-height: 125px;
width: 100%;
}

svg {
-webkit-transform: rotate(-90deg);
transform: rotate(-90deg);
}

.circle_animation {
stroke-dasharray: 440; /* this value is the pixel circumference of the circle */
stroke-dashoffset: 440;
transition: all 1s linear;
}

<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
<div class="item html">
<h2>0</h2>
<svg width="160" height="160" xmlns="http://www.w3.org/2000/svg">
<g>
<title>Layer 1</title>
<circle id="circle" class="circle_animation" r="70" cy="81" cx="81" stroke-width="8" stroke="#6fdb6f" fill="none"/>
</g>
</svg>
</div>

JSFiddle version

answered Apr 15, 2015 at 12:18
Turnip

Comments:
Toniq, Mar 27, 2020: How did you get 440?
Turnip, Mar 28, 2020: @Toniq The radius(r) of the circle is ~70 which creates a circumference of 440.

Answer 2 (score -3):

you should look at my jquery plugin Knob https://github.com/aterrien/jQuery-Knob, generated canvas circular input, and set timer behavior like :

var time = 0,
maxTime = 60;
$('#dial').knob({
readOnly : true,
thickness : 0.1,
max : maxTime
});

setInterval(function() {
if(time>maxTime) time = 0;
time++;
$('#dial')
.val(time)
.trigger('change');
}, 1000);

I made a codepen here : http://codepen.io/pik_at/pen/azeYRg

answered Apr 15, 2015 at 12:26
Pik_at
