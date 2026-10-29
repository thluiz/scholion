---
url: "http://www.levibotelho.com/development/c-remove-diacritics-accents-from-a-string/"
captured_at: "2015-10-08T19:11:01-03:00"
title: "[C#] Remove diacritics (accents) from a string"
domain: "levibotelho-com"
---

# [C#] Remove diacritics (accents) from a string

June 19, 2014
 [Permalink](http://www.levibotelho.com/development/c-remove-diacritics-accents-from-a-string/ "[C#] Remove diacritics (accents) from a string")

 [Tweet](https://twitter.com/intent/tweet?hashtags=development&text=[C#] Remove diacritics (accents) from a string&url=http://www.levibotelho.com/development/c-remove-diacritics-accents-from-a-string/&via=LeviBotelho "Share on Twitter")

Removing diacritics from a string is a common task that doesn’t have a built-in method in the .NET framework. Luckily, it’s really easy to write an extension method which will do the trick. Here is how it’s done.

```
public static string RemoveDiacritics string 

     stringIsNullOrWhiteSpace
        return 

      NormalizeNormalizationFormFormD
     chars  Where => CharUnicodeInfoGetUnicodeCategory  UnicodeCategoryNonSpacingMarkToArray
    return  stringcharsNormalizeNormalizationFormFormC
```

## How it works

*If your Unicode knowledge is a bit rusty, check out [my post from two weeks ago which covers the essentials](http://www.levibotelho.com/development/unicode-and-utf-what-you-need-to-know/) before going on.*

Many characters in Unicode have multiple numerical representations. For example, “ô” can be represented both by the code point `U+00F4` (“Latin small letter o with circumflex”), or by the pair of code points `U+006F 0+0302` (“Latin small letter o” and “combining circumflex accent”). Unicode works this way in order to improve compatibility with other character sets.

However while this system provides flexibility, it poses a problem when comparing strings for equality. As we just saw, two syntactically-equivalent strings can have different numerical representations. To solve this problem, Unicode defines four “normalization forms”, which are essentially sets of rules which specify one single way to represent each character in the Unicode standard. When syntactically-equivalent strings are normalized, their binary representations are guaranteed to be identical.

While in our case we don’t really care about string equality, we make use of normalization in order to pick out the accents from our input string. Specifically, normalization form “D” works by taking precomposed characters (such as `U+00F4`) and converting them to their decomposed equivalents (`U+006F 0+0302`). Once our input string is normalized according to this standard, we are able to run through each code point one by one and remove all diacritics (classified in Unicode as “non spacing marks”).

With this complete, all that is left to do is rebuild the string and normalize it once again, this time using normalization form “C”, which recomposes any decomposed characters remaining in the text. We then take the result, return it to the caller, and we’re done!
