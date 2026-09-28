---
url: "https://dev.to/aman894/what-the-hell-is-doctype-html-32om"
captured_at: "2022-07-08T15:54:00-03:00"
title: "What the hell is <!DOCTYPE html>? - DEV Community"
domain: "dev-to"
---

# What the hell is <!DOCTYPE html>?

```
<!DOCTYPE html> <!-- What the hell is this?? -->>
<html lang="en">
<head>
    <title>Document</title>
</head>
<body>
</body>
</html
```

When creating a new HTML file, you might have wondered, “Why do I need to add this statement to the first line of my HTML file? Doesn’t the .html file extension suffice in telling the browser that this is an HTML file?”. While this is true, there’s still more to it. Before we understand the above statement, let’s try to understand what a DTD is.

## Document Type Definition (DTD)

A Document Type Definition (or DTD in short) describes the document structure of an XML document along with a list of the legal elements the document can have.

Prior to HTML5 (for e.g. in HTML 4.01), all HTML documents would have to contain a “Doctype” declaration on its first line along with a reference to its type definition. This would look something like:

```
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" 
"http://www.w3.org/TR/html4/strict.dtd">
```

This declaration served two purposes:

- Provide the list of valid elements the document can contain.
- Define the flavour of the DTD which could be strict, transitional or frameset. More on this [here](https://www.htmlhelp.com/reference/html40/html/doctype.html).

So why don’t you see these long DTD references in the latest HTML files you've encountered?

## Enter HTML5!

See, earlier versions of HTML (prior to HTML5) were SGML (Standard Generalized Markup Language) based, and therefore required a reference to DTDs. HTML5 onwards, this reference was no longer needed since this version of HTML is not SGML based.

So now, this “Doctype” declaration serves another purpose. It allows browser to run the HTML file in a *“Standard mode”*. Now it’s logical to ask, “What on earth is this standard mode now??” To understand this, let’s go back in time.

## Back in time

Back when tech enthusiasts realised the power of what would be known as the internet, two popular browsers came into existence - the Netscape Navigator & following its success, (drumrolls) Microsoft’s Internet explorer. This was even before the W3C standards came into picture which would eventually standardise how code would run across different browsers. Hence, you can imagine that, given the popularity of these browsers, websites were written in two versions - one for the Navigator, and the other one for IE, which might sound a little redundant now, but was the norm back then. However, after the W3C standards were created and browsers started adhering to them, developers encountered a new problem.

The problem now was that the legacy code started to break. Hence, a possible solution to this was that the sites were now made in two versions - a *Standard version* (the one which we mentioned earlier) which was W3C standards compliant and hence would run across different browsers and a *Quirks version* which supported the legacy code.

Now how do browsers identify which mode it needs to use? Well, just add a valid DOCTYPE declaration in the first line of the HTML file, to instruct the browser to run the code in *Standard mode*. Anything other than that will trigger the *Quirks mode* in IE9 or older. This is exactly what `<!DOCTYPE html>` does HTML5 onwards. If you fail to add this line to your HTML file, the browser would interpret this as an instruction to run your code in *Quirks mode*, and you could end up getting inconsistent results across different browsers.

## Conclusion

With this little background in mind, I hope you now understand the importance of the <!DOCTYPE html> statement. If you’d like to read a little more on this, please go through the links I have provided as a reference below.

### References

<https://www.freecodecamp.org/news/what-is-the-doctype-declaration-in-html/>  
<https://developer.mozilla.org/en-US/docs/Web/HTML/Quirks_Mode_and_Standards_Mode>  
<https://hsivonen.fi/doctype/>
