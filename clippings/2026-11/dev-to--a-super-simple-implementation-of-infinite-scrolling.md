---
url: "https://dev.to/sakun/a-super-simple-implementation-of-infinite-scrolling-3pnd"
captured_at: "2026-11-16T00:54:29+00:00"
title: "A super simple implementation of Infinite Scrolling"
domain: "dev-to"
---

[![Cover image for A super simple implementation of Infinite Scrolling](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fthepracticaldev.s3.amazonaws.com%2Fi%2Fbnzlkv3hnnge2kpglf7r.jpg)](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fthepracticaldev.s3.amazonaws.com%2Fi%2Fbnzlkv3hnnge2kpglf7r.jpg)

[![sakun](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F222763%2F2f019d5f-2068-4305-b55a-bb82926e70b3.jpg)](https://dev.to/sakun)

[sakun](https://dev.to/sakun)

Posted on Dec 23, 2019 Edited on Dec 23, 2019

I thought I’d share our approach to implementing infinite scrolling using jQuery on [https://sideprojects.net](https://sideprojects.net/) and how it could be applied to other sites.

In our case, our pagination is in a “load more” format where you have to click the “load next days” button every time you reached the bottom of the page in order to show content from the previous 4 days.

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fmiro.medium.com%2Fmax%2F1200%2F1%2A18xm60QQiI5WMMmz5nNu_A.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fmiro.medium.com%2Fmax%2F1200%2F1%2A18xm60QQiI5WMMmz5nNu_A.gif)

What we wanted to do was display the next few days as soon as you scrolled to the bottom of the page and that’s what this tutorial will cover.

## [](#setup)Setup

### [](#prerequisites)Prerequisites

*   A website with some sort of pagination.
*   Add jQuery to your website if you haven’t already.

```


<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js">


```

Enter fullscreen mode Exit fullscreen mode

*   Add a class to the button the controls your site’s pagination if you don’t have one already.

#### [](#1-create-a-window-scroll-event)1) Create a window scroll event

```


//Infinite scroll
$(window).on("scroll", function() {

});


```

Enter fullscreen mode Exit fullscreen mode

#### [](#2-create-a-variable-for-the-height-of-the-entire-document-as-well-as-a-variable-to-determine-your-scroll-position)2) Create a variable for the height of the entire document as well as a variable to determine your scroll position

Inside the scroll event, create 2 variables. We’re going to call them scrollHeight and scrollPos.

```


var scrollHeight = $(document).height();
var scrollPos = $(window).height() + $(window).scrollTop();


```

Enter fullscreen mode Exit fullscreen mode

#### [](#3-lets-do-some-math)3) Let's do some math!

Remember: we want the event to fire every time the user scrolls to the bottom of the page.

We can check if you’ve reached the bottom of a page with the following conditional statement:

```


if ((scrollHeight - scrollPos) / scrollHeight == 0) {


```

Enter fullscreen mode Exit fullscreen mode

We want the event to be triggered if the conditional statement is met.

In our case, the class name for our button is .load-more-days-button. That button will be clicked upon reaching the end of a page.

```


if ((scrollHeight - scrollPos) / scrollHeight == 0) {             
   $('.load-more-days-button').click();
}


```

Enter fullscreen mode Exit fullscreen mode

So putting it all together, we get:

```


//Infinite scroll
$(window).on("scroll", function() {
  var scrollHeight = $(document).height();
  var scrollPos = $(window).height() + $(window).scrollTop();
  if ((scrollHeight - scrollPos) / scrollHeight == 0) {
    $('.load-more-days-button').click();
    console.log("bottom!");
  }
});


```

Enter fullscreen mode Exit fullscreen mode

That’s all? Are we done?!? Well — yes, but no.

It works.

But it’s not great. Why?

1.  It requires you to scroll all the way down so that your scrollbar touches the end before it fires the event.
2.  It works poorly on mobile. I’ve noticed that it doesn’t always trigger on mobile and pick up the fact that you’ve reached the bottom of the page — even when you’ve scroll all the way down.

So let's fix it:

Let’s substitute this line:

```


if ((scrollHeight - scrollPos) / scrollHeight == 0) {


```

Enter fullscreen mode Exit fullscreen mode

with this instead:

```


if(((scrollHeight - 300) >= scrollPos) / scrollHeight == 0) {


```

Enter fullscreen mode Exit fullscreen mode

This line of code causes the scroll event to trigger when it is 300 (or less) pixels above the bottom of the page. (You can configure the 300 to something else if you’d like)

This works great on desktop and mobile!

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fmiro.medium.com%2Fmax%2F1280%2F1%2AyAGJC5O3pLZoO5H75n2XXw.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fmiro.medium.com%2Fmax%2F1280%2F1%2AyAGJC5O3pLZoO5H75n2XXw.gif)

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fmiro.medium.com%2Fmax%2F640%2F1%2ADX91Gh4_34ptN2Rw36nbvQ.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fmiro.medium.com%2Fmax%2F640%2F1%2ADX91Gh4_34ptN2Rw36nbvQ.gif)

## [](#wrapping-things-up)Wrapping things up

Putting everything together, your code will probably end up looking something like this:

```


//Infinite Scroll
$(window).on("scroll", function() {
 //page height
 var scrollHeight = $(document).height();
 //scroll position
 var scrollPos = $(window).height() + $(window).scrollTop();
 // fire if the scroll position is 300 pixels above the bottom of the page
 if(((scrollHeight - 300) >= scrollPos) / scrollHeight == 0){
   $('.load-more-days-button').click();
  }
});


```

Enter fullscreen mode Exit fullscreen mode

You can view a live example [here](https://sideprojects.net/).
