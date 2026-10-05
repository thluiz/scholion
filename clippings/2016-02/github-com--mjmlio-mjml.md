---
url: "https://github.com/mjmlio/mjml"
captured_at: "2016-02-07T22:07:41-03:00"
title: "mjmlio/mjml"
domain: "github-com"
---

# Introduction

MJML is a markup language designed to reduce the pain of coding a responsive email. Its semantic syntax makes it easy and straightforward while its rich standard components library fastens your development time and lightens your email codebase. MJML’s open-source engine takes care of translating the MJML you wrote into responsive HTML.

[![ee034178-bf85-11e5-9dda-98d0c8f9f8d6.png](github-com--mjmlio-mjml/2767d71f3bec00eb103b51f6cad3e729.png)](http://mjml.io/)

# Installation

```
npm install -g mjml
```

[**Via... click:**](https://github.com/mjmlio/mjml/releases)

# Show me the code!

### Command line

> Compile the file and output the result in `a.html`

```
$ mjml -r input.mjml
```

> Redirect the result to a file

```
$ mjml -r input.mjml -o output.html
```

> Watch a file and compile every time the file changes

```
$ mjml -w input.mjml -o output.html
```

### Inside NodeJs

```
import   

  Compile an mjml string

const htmlOutput  .mjml2html(<mj-body>
  <mj-section>
    <mj-column>
      <mj-text>
        Hello World!
      </mj-text>
    </mj-column>
  </mj-section>
</mj-body>
)

  Print the responsive HTML generated

console.(htmlOutput);
```

### Create your component

> Issue the following in your terminal

```
$ mjml --init-component name of your component

# If your component cannot contain anything else than text:
$ mjml --init-component name of you component -e

# It means nothing inside it will be parsed by the mjml engine.
```

It will create a basic component template in a `.js` file. Follow the instructions provided in the file
and read more about custom components in the documentation

# Try it live

Get your hands dirty by trying the MJML online editor! Write awesome code on the left side and preview your email on the right. You can also get the rendered HTML directly from the online editor.

[![58a40618-b5f7-11e5-9ed3-80463874ab14.png](github-com--mjmlio-mjml/519835f55055c96636f6b73d2dcb4ee0.png)](http://mjml.io/try-it-live)

# Contributors

# Contribute

- Fork the repository
- Code an awesome feature (we are confident about that)
- Make your pull request
- Add your github profile here
