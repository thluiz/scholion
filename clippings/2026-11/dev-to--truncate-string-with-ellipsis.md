---
url: "https://dev.to/ip127001/truncate-string-with-ellipsis-26l5"
captured_at: "2026-11-16T01:55:23+00:00"
title: "Truncate string with ellipsis"
domain: "dev-to"
---

[![Cover image for Truncate string with ellipsis](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Flnz4sza6s0qr1s90plul.png)](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Flnz4sza6s0qr1s90plul.png)

[![Rohit Kumawat](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F362984%2F54ffd551-e81f-4ffe-8f2c-bd2e1b310440.jpeg)](https://dev.to/ip127001)

Sometimes we required to adjust long strings in one line and show ellipsis(...) at the end of the string as a symbol that this text is long.

Then we can use the `title` attribute to show the full string on the hover of text.

## [](#to-truncate-long-strings-we-will-use-the-following-css-properties)**To truncate long strings we will use the following CSS properties:**

1.  `text-overflow`: describes how hidden content should be shown to the user.
2.  `white-space`: sets how white space inside an element is handled.
3.  `overflow`: property specifies whether to clip the content or to add scrollbars when the content of an element is too big to fit in the specified area.
4.  `width`: width of the content.

```
div {
  width: 100%;
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
}
```

Enter fullscreen mode Exit fullscreen mode

> text-overflow property is used with white-space and overflow to show this ellipsis signal if the content is clipped.

*   `white-space: nowrap`: text will not be wrapped.
*   `overflow: hidden`: hide/clip the content in fix width.
*   Finally`text-overflow: ellipsis`: will show the sign (...) stating that this text is clipped.

### [](#inform-user-about-fulltext-content)**Inform user about full-text content:**

*   For that use the `title` attribute.
*   If used, the long string will be shown to the user if hovered on `div` like the example below.

```
const longText = Hey everyone, This code shows how we can truncate long strings so that they can show as an ellipsis. we can use 100% width to adjust the text in one line.

<div title={longText}>{longText}</div>
```

Enter fullscreen mode Exit fullscreen mode

### [](#both-examples-in-codepen)Both examples in codepen

## [](#ellipsis-in-input-element)Ellipsis in input element:

Just use `text-overflow: ellipsis` directly.  

```
input {
  text-overflow: ellipsis;
}
```

Enter fullscreen mode Exit fullscreen mode

Happy coding!

Thanks for reading!
