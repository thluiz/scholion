---
url: "https://dev.to/awwsmm/super-simple-markdown-bae"
captured_at: "2026-11-16T01:33:34+00:00"
title: "Super Simple Markdown"
domain: "dev-to"
---

[![Cover image for Super Simple Markdown](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Flsoicwn1t7vjox6j2vdi.jpg)](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Flsoicwn1t7vjox6j2vdi.jpg)

[![Andrew (he/him)](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F101393%2F56bf0c89-b8ca-4157-9c3b-79031045a21f.png)](https://dev.to/awwsmm)

[Markdown](https://en.wikipedia.org/wiki/Markdown) is the language of DEV posts, and is a super-lightweight way to add some _pizzazz_ to your plaintext. It consists of a few easy-to-remember (and easy-to-type) shortcuts. If you're learning Markdown for the first time (or just have trouble remembering what does what) bookmark this cheat sheet and come back to it as necessary.

* * *

## [](#common-formatting)Common Formatting

* * *

To make text _italic_  

```
...use _single underscores_ or *single asterisks*
```

Enter fullscreen mode Exit fullscreen mode

* * *

To make text **bold**  

```
...use __double underscores__ or **double asterisks**
```

Enter fullscreen mode Exit fullscreen mode

* * *

To make text **_bold and italic_**  

```
...use __*asterisks in double underscores*__,
       **_underscores in double asterisks_**,
       _**double asterisks in underscores**_, or
       *__double underscores in asterisks__*
```

Enter fullscreen mode Exit fullscreen mode

* * *

To add `inline code`  

```
...use `single backticks`
```

Enter fullscreen mode Exit fullscreen mode

* * *

To add  

```
a code
block
```

Enter fullscreen mode Exit fullscreen mode

use  

````
```
triple
backticks
```
````

Enter fullscreen mode Exit fullscreen mode

or  

```
    indent
    four
    spaces
1234
```

Enter fullscreen mode Exit fullscreen mode

* * *

To add

## [](#headings)Headings

## [](#of-various)of various

### [](#sizes)sizes

use  

```
# one
## or more
### octothorpes
```

Enter fullscreen mode Exit fullscreen mode

* * *

To add horizontal rules (like the one above), write three or more hyphens in a row:  

```
---
```

Enter fullscreen mode Exit fullscreen mode

* * *

1.  To create
2.  ordered lists
3.  of items

```
1. simply write
1. "1. " before
1. each item
```

Enter fullscreen mode Exit fullscreen mode

* * *

*   To create
*   unordered lists
*   of items

```
- simply write
- "- " before
- each item
```

Enter fullscreen mode Exit fullscreen mode

* * *

1.  Create sublists
    *   by indenting
        1.  four spaces
            *   for each level

```
1. Create sublists
    - by indenting
        1. four spaces
            - for each level
```

Enter fullscreen mode Exit fullscreen mode

* * *

To create a [hyperlink](https://timecube.2enp.com/)  

```
put the [link text in square braces](https://timecube.2enp.com/)
(followed by the URL in parentheses)
```

Enter fullscreen mode Exit fullscreen mode

* * *

> To create a blockquote  

```
> begin the quote with "> "
```

Enter fullscreen mode Exit fullscreen mode

* * *

To strikethrough text  

```
use ~~double~~ tildes
```

Enter fullscreen mode Exit fullscreen mode

* * *

To add an inline image

[![Trogdor, the Burninator](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fsguw2x61byhenjclhmmj.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fsguw2x61byhenjclhmmj.png)  

```
Use the same syntax as for a hyperlink, but prepend a '!':

![Trogdor, the Burninator](https://dev-to-uploads.s3.amazonaws.com/i/sguw2x61byhenjclhmmj.png)
```

Enter fullscreen mode Exit fullscreen mode

* * *

pssst hey kid, want some

## [](#super-secret-markdown-tips-they-dont-want-you-to-know-about)Super Secret Markdown Tips (_They_\* don't want you to know about!)

* * *

### [](#need-to-write-a-literal-etc-character)Need to write a literal \*, \_, etc. character?

Escape them by preceding them with backslashes: `\*`, `\_`

* * *

### [](#need-to-put-backticks-inside-inline-code)Need to put backticks inside inline code?

``Use double-backticks `with backticks` inside``  

```
``Use double-backticks `with backticks` inside``
```

Enter fullscreen mode Exit fullscreen mode

* * *

### [](#need-to-put-triplebackticks-inside-a-code-block)Need to put triple-backticks inside a code block?

````
```
indent four spaces
and then add the backticks
```
````

Enter fullscreen mode Exit fullscreen mode

    \`\`\`
    indent four spaces
    and then add the backticks
    \`\`\`

* * *

### [](#need-to-put-a-code-block-in-a-list)Need to put a code block in a list?

1.  Just make sure
2.  To indent  
    
    ```
    four
    spaces
    ```
    
3.  to keep the numbering contiguous
    

    1. Just make sure
    1. To indent


        \`\`\`
        four
        spaces
        \`\`\`


    1. to keep the numbering contiguous

* * *

### [](#need-to-put-a-block-of-code-in-a-blockquote)Need to put a block of code in a blockquote?

> You might want to do something like
> 
> ```
> small bug on DEV.to -- first line is indented one space
> val x = 42
> val y = 42 * 19
> ```
> 
> ...just make sure you start each line with "> "

\> You might want to do something like
> 
>     small bug on DEV.to -- first line is indented one space
>     val x = 42
>     val y = 42 \* 19
> 
> ...just make sure you start each line with "> "

* * *

### [](#need-fancy-syntax-highlighting-to-impress-your-friends-and-frighten-your-enemies)Need fancy syntax highlighting to impress your friends and frighten your enemies?

```
def foo (val bar: Int, baz: Double): String = { ... }
```

Enter fullscreen mode Exit fullscreen mode

Just put the name of the programming language after the initial \`\`\`:  

````
```scala
def foo (val bar: Int, baz: Double): String = { ... }
```
````

Enter fullscreen mode Exit fullscreen mode

* * *

Got any tough Markdown problems you need help solving? Got any tips or tricks for those new to the (plaintext formatting syntax) game? Let me know in the comments below!

\* The Markdown Illuminati, not to be confused with the [Marky Mark Illuminati](https://www.youtube.com/watch?v=AO9909uexu8)
