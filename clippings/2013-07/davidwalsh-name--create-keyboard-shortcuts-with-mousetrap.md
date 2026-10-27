---
url: "http://davidwalsh.name/keyboard-shortcuts?utm_source=javascriptweekly&utm_medium=email"
captured_at: "2013-07-12T10:24:07-03:00"
title: "Create Keyboard Shortcuts with Mousetrap"
domain: "davidwalsh-name"
---

# Create Keyboard Shortcuts with Mousetrap

Written by [David Walsh](http://davidwalsh.name/) on July 9, 2013 · ** [4 Comments](http://davidwalsh.name/keyboard-shortcuts?utm_source=javascriptweekly&utm_medium=email#comments)

[Tweet](https://twitter.com/intent/tweet?original_referer=http%3A%2F%2Fdavidwalsh.name%2Fkeyboard-shortcuts%3Futm_source%3Djavascriptweekly%26utm_medium%3Demail&text=Create%20Keyboard%20Shortcuts%20with%C2%A0Mousetrap%20by%20%40davidwalshblog&tw_p=tweetbutton&url=http%3A%2F%2Fdavidwalsh.name%2Fkeyboard-shortcuts)

[52](http://twitter.com/search?q=http%3A%2F%2Fdavidwalsh.name%2Fkeyboard-shortcuts "This page has been shared 52 times. View these Tweets.")

[anexo ausente][anexo ausente]

This page has been shared 52 times. View these Tweets.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |  |  |  | | --- | --- | --- | |  | 18 |  | |

|  |  |
| --- | --- |
| Like | 22 |

Some of the finest parts of web apps are hidden in the little things.  These "small details" can often add up to big, big gains.  One of those small gains can be found in keyboard shortcuts.  Awesome web apps like Gmail and GitHub use loads of keyboard shortcuts and they make navigating exponentially faster.  After evaluating a few keyboard microlibraries, I've found Mousetrap to be the best!

[View Demo >](http://davidwalsh.name/demo/keyboard-shortcuts.php) 
[Get Mousetrap >](http://craig.is/killing/mice)

## Using Mousetrap

Mousetrap's bind method is the key to the madness, accepting the key(s) to listen to, the callback method, and a specific event to use (if present):

```
Mousetrap.bind("s", function(e) {
	// Focus on the search field, do whatever
});
```

What's immediately nice to see is that you can reference keys by key name and not need to look up key code numbers.  You can listen for multiple keys by adding a + between them:

```
Mousetrap.bind("shift+k", function() {
	// Create a link
});
```

You can also listen for key sequences by separating keys with spaces:

```
Mousetrap.bind("d a v i d", function() {
	// Alert "FTW"
});

// konami code!
Mousetrap.bind('up up down down left right left right b a enter', function() {
    highlight([21, 22, 23]);
});
```

In the case of listening for likewise events, you can pass Moustrap an array:

```
Mousetrap.bind(["command+s", "ctrl+s"], function() {
	// Save the form
});
```

Modifier keys like `SHIFT` and `CONTROL` may also be used:

```
Mousetrap.bind("shift+k", function() {
	// Yay for extra key control
});
```

You can also use keys which require `SHIFT` without needing to cite the key:

```
Mousetrap.bind("* _ $", function() {
	// Yay for extra key control
});
```

Removing event listeners can be done with a simple unbind call, passing the key(s) to which unbind:

```
Mousetrap.unbind("s");
```

You can ever trigger an event if you'd like:

```
Mousetrap.trigger("s");
```

Essentially you get maximum control over key events.  Mousetrap even provides a more advanced functionality if you need it, so check out the [official documentation](http://craig.is/killing/mice) to learn more.

[View Demo >](http://davidwalsh.name/demo/keyboard-shortcuts.php)

Mousetrap is an awesome utility:  simple, useful, and tiny.  You can probably get away with avoid this micro-library if you only have a few keys to listen for, but if you're looking to do advanced keyboard handling and navigation, Mousetrap is perfect.
