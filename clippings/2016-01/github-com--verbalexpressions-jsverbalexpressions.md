---
url: "https://github.com/VerbalExpressions/JSVerbalExpressions"
captured_at: "2016-01-05T13:05:56-03:00"
title: "VerbalExpressions/JSVerbalExpressions"
domain: "github-com"
---

# VerbalExpressions v0.1.2

## JavaScript Regular Expressions made easy

VerbalExpressions is a JavaScript library that helps to construct difficult regular expressions.

## Other Implementations

You can see an up to date list of all ports on [VerbalExpressions.github.io](http://verbalexpressions.github.io/).

If you would like to contribute another port (which would be awesome!), please open an issue specifying the language. A repo in the [VerbalExpressions organization](https://github.com/VerbalExpressions) will be created for it. Please don't open PRs for other languages against this repo.

## How to get started

### In the browser

```
<script =text/javascript =VerbalExpressions.js></script>
```

### On the server (node.js)

Install:

```
npm install verbal-expressions
```

Require:

```
 VerEx  require(verbal-expressions);
```

## Running tests

```
$ grunt
(or)
$ grunt test
```

## Creating a minified version

This will generate a minified version of VerbalExpressions.js (aptly named VerbalExpressions.min.js) in a *dist* folder.

```
$ grunt build
```

A source map will also be created in the same folder, so you can use the original unminified source file (copied to *dist* as well) for debugging purposes.

## Examples

Here's a couple of simple examples to give an idea of how VerbalExpressions works:

### Testing if we have a valid URL

```
// Create an example of how to test for correctly formed URLs
 tester  VerEx()
            .startOfLine()
            .(  )
            .maybe(  )
            .(  )
            .maybe(  )
            .anythingBut(  )
            .endOfLine();

// Create an example URL
 testMe  https://www.google.com;

// Use RegExp object's native test() function
( tester.( testMe ) ) alert( We have a correct URL ); // This output will fire
 alert( The URL is incorrect );

console.( tester ); // Outputs the actual expression used: /^(http)(s)?(\:\/\/)(www\.)?([^\ ]*)$/
```

### Replacing strings

```
// Create a test string
 replaceMe  Replace bird with a duck;

// Create an expression that seeks for word "bird"
 expression  VerEx().(  );

// Execute the expression like a normal RegExp object
 result  expression.replace( replaceMe,  );

alert( result ); // Outputs "Replace duck with a duck"
```

### Shorthand for string replace:

```
 result  VerEx().(  ).replace( We have a red house,  );
alert( result ); // Outputs "We have a blue house"
```

## API documentation

You can find the API documentation at the [wiki pages](https://github.com/VerbalExpressions/JSVerbalExpressions/wiki).

## A little word for a big help

I'd like to promote a special thank-you to [Ben Nadel](http://www.bennadel.com/) for his [great article about extending native JS objects](http://www.bennadel.com/blog/2292-extending-javascript-arrays-while-keeping-native-bracket-notation-functionality.htm)

## Contributions

Clone the repo and fork:
`git clone https://github.com/jehna/VerbalExpressions.git`.

Pull requests are warmly welcome!

Check out these slide decks for handy Github & git tips:
