---
url: "http://simpleprogrammer.com/2015/04/13/why-comments-are-stupid-a-real-example/"
captured_at: "2015-04-14T12:27:43-03:00"
title: "Making the Complex Simple"
domain: "simpleprogrammer-com"
---

# Why Comments Are Stupid, a Real Example

![stupid.png](simpleprogrammer-com--why-comments-are-stupid-a-real-example/e60f74fc6707b33448de1c61b2805ec5.png)

Nothing seems to stir up **religious debate** more so than when I [write a post](http://simpleprogrammer.com/2015/03/16/11-rules-all-programmers-should-live-by/) or do a [YouTube video](https://www.youtube.com/watch?v=ErW6fEvulAc) that mentions how most of the time comments are not necessary and are actually more harmful than helpful.

I first switched sides in this debate when I read the second edition of [Code Complete](http://www.amazon.com/gp/product/0735619670/ref=as_li_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=0735619670&linkCode=as2&tag=makithecompsi-20&linkId=XRVP7LFMXGGPFZPK).

In that book, Steve McConnell, made it abundantly clear to me that the reasons I was putting so many comments in my code was that:

- **I wasn’t naming things** in a way that would make explanatory comments unnecessary
- My methods and functions were far **too large** and thus needed extra explaining

The way I wrote code drastically changed.

**I had believed I was doing a good job, and being a dutiful programmer by writing comments to explain my code and make it easier for the next developer to understand them.**

But, when I started applying what I learned in [Code Complete](http://www.amazon.com/gp/product/0735619670/ref=as_li_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=0735619670&linkCode=as2&tag=makithecompsi-20&linkId=XRVP7LFMXGGPFZPK), and started writing code that was often more clear than the comments I was previously writing, I realized that I was doing a **greater favor** to any developers who would inherit my code than simply writing comments. **I was making my code even more clear.**

When I read Uncle Bob’s book, [Clean Code](http://www.amazon.com/gp/product/0132350882/ref=as_li_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=0132350882&linkCode=as2&tag=makithecompsi-20&linkId=OE6W2DLW3J5Z2TNZ), my position further strengthened.

Not only did Uncle Bob say we should avoid comments, he said—and showed—how comments, more often than not, indicated **a failure to express intention in code.**

Bob made me realize that I was still leaning too heavily on comments and that I needed to further improve my naming and strive to have my code communicate its intention without the need of outside aid.

## Showing a real comment-removing example

Now, this was my own personal progression—and I don’t expect everyone to have the same experience I did, or even to see things the same way—but, I do feel **there is still a large amount of ignorance that seems to spew forth whenever I mention that comments should generally be avoided** in favor of more communicative code.

## LEARN HOW TO CREATE A BLOG

## In Less Than 5 Minutes!

6 Lessons, Delivered Right to Your Inbox

It couldn't be easier!​

For a while now, I’ve felt the burden of needing to back up what I am saying.

It is one thing for me to extol the value of clear, communicative code, but it is another thing for me to show how clear—or as Uncle Bob would put it “clean”—code is far more understandable and maintainable than equally “good” code that is heavily commented.

At first I was going to make up some code example to show you how this is the case.

I was going to write some code that was not named very well and full of comments, and then show you how I could refactor that code to get rid of the comments and actually increase the clarity.

But, I know from experience that is a trap.

Too many people will cry foul and claim I have setup a “straw man” that didn’t represent real world code.

Fortunately, I realized an excellent opportunity that is now open to me.

## Refactoring some real code from the .NET framework

Since Microsoft decided to open source the entire .NET code base, I decided I would instead pick a real example of real code that is not bad, but just could be refactored to eliminate comments and still make the code just as clear—and in my opinion clearer.

The piece of code I decided to “pick on” [is located here](https://github.com/dotnet/corefx/blob/master/src/System.IO.FileSystem/src/System/IO/PathHelpers.cs).

I’ve just pulled out one method in this code, *SplitDirectoryFile,*to illustrate my point.

I don’t know who wrote this code, and I don’t even consider this code bad. I’m just using it as an example, so keep that in mind.

I picked a fairly small method, so that it could be easily understood and fit into this blog post, but my general approach could be applied to much larger swatches of code.

Let’s take a look at what the code looked like before I refactored it:

|  |  |
| --- | --- |
|  | ```  internal static  SplitDirectoryFile(string path, out string directory, out string file)  directory = ;  file = ;  // assumes a validated full path  (path != )  length = path.Length;  rootLength = GetRootLength(path);  // ignore a trailing slash  (length > rootLength && EndsInDirectorySeparator(path))  length--;  // find the pivot index between end of string and root  ( pivot = length - ; pivot >= rootLength; pivot--)  (IsDirectorySeparator(path[pivot]))  directory = path.Substring(, pivot);  file = path.Substring(pivot + , length - pivot - );  return;  // no pivot, return just the trimmed directory  directory = path.Substring(, length);  return; ``` |

Like I said before, this code isn’t bad.

It’s pretty clear what it is doing.

The comments even make sense.

But, could we eliminate all of these comments and actually make the code more understandable?

Let’s start with the first comment. It seems innocent enough.

> // assumes a validated full path

Is there was way we can communicate this in the code?

## Replacing a comment with a better parameter name

What if we change the name of the variable from path to validatedFullPath?

|  |  |
| --- | --- |
|  | ```  internal static  SplitDirectoryFile(string validatedFullPath, out string directory, out string file)  directory = ;  file = ;  (validatedFullPath != )  length = validatedFullPath.Length;  rootLength = GetRootLength(validatedFullPath);  // ignore a trailing slash  (length > rootLength && EndsInDirectorySeparator(validatedFullPath))  length--;  // find the pivot index between end of string and root  ( pivot = length - ; pivot >= rootLength; pivot--)  (IsDirectorySeparator(validatedFullPath[pivot]))  directory = validatedFullPath.Substring(, pivot);  file = validatedFullPath.Substring(pivot + , length - pivot - );  return;  // no pivot, return just the trimmed directory  directory = validatedFullPath.Substring(, length);  return; ``` |

Not a huge difference—almost trivial—but, not only have we eliminated a comment, we’ve made it so someone calling this method can tell from the variable name that they are not just supposed to pass in a path, but a validated full path.

Again, seems like a rather small change, but, I do believe it has made the code more clear.

## A bit of a bigger change…

Moving on, we can take a look at the next comment:

> // ignore a trailing slash

Now, there are a few ways we can handle this one.

We can simply replace the comment with a method, so we have:

> if (ShouldIgnoreTrailingSlash(length, rootLength, validatedFullPath)
>
> length–;

We could also create a simple boolean variable to replace the comment:

> bool ShouldIgnoreTrailingSlash = length > rootLength && EndsInDirectorySeparator(validatedFullPath);
>
> if(ShouldIgnoreTrailingSlash)
>
> length–;

Another, perhaps better possibility, would be to do something like this:

> length = LengthWithoutTrailingSlash(length, rootLength, validatedFullPath);

But, I see an opportunity here to improve the overall readability and structure of the code and get rid of a comment.

How about this refactor?

|  |  |
| --- | --- |
|  | ```  public class DirectoryFileSplitter  private readonly string validatedFullPath;  private  length;  private  rootLength;  public DirectoryFileSplitter(string validatedFullPath)  .validatedFullPath = validatedFullPath;  public  Split( string directory,  string )  directory = ;  file = ;  (validatedFullPath != )  length = validatedFullPath.Length;  rootLength = GetRootLength(validatedFullPath);  IgnoreTrailingSlash();  // find the pivot index between end of string and root  ( pivot = length - ; pivot >= rootLength; pivot--)  (IsDirectorySeparator(validatedFullPath[pivot]))  directory = validatedFullPath.Substring(, pivot);  file = validatedFullPath.Substring(pivot + , length - pivot - );  return;  // no pivot, return just the trimmed directory  directory = validatedFullPath.Substring(, length);  return;  private  IgnoreTrailingSlash()  (length > rootLength && EndsInDirectorySeparator(validatedFullPath))  length--; ``` |

It might seem like overkill here, but I think it makes a lot of sense to make this static method into an actual class.

We can then very clearly communicate what the class is supposed to do and utilize the state of the class to simplify the code.

Trying to cleanly remove comments led me to this refactoring of the method itself, because I found that the clearest way to express the intent was to encapsulate it.

Now, you might not agree with this particular refactoring—and that is fine—but I’m sure you can still see how we can easily eliminate comments by expressing the intent in the code more clearly.

## Now it gets easy

From here, it is trivial to get rid of the next comment:

> // find the pivot index between end of string and root

All we have to do is change this into a method that says exactly what it does.

|  |  |
| --- | --- |
|  | ```  public class DirectoryFileSplitter  private readonly string validatedFullPath;  private  length;  private  rootLength;  private  pivotFound;  public string Directory { ; ; }  public string  { ; ; }  public DirectoryFileSplitter(string validatedFullPath)  .validatedFullPath = validatedFullPath;  length = validatedFullPath.Length;  rootLength = GetRootLength(validatedFullPath);  public  Split()  (validatedFullPath != )  IgnoreTrailingSlash();  FindPivotIndexBetweenEndOfStringAndRoot();  // no pivot, return just the trimmed directory  (!pivotFound)  Directory = validatedFullPath.Substring(, length);  return;  private  FindPivotIndexBetweenEndOfStringAndRoot()  ( pivot = length - ; pivot >= rootLength; pivot--)  (IsDirectorySeparator(validatedFullPath[pivot]))  Directory = validatedFullPath.Substring(, pivot);  File = validatedFullPath.Substring(pivot + , length - pivot - );  pivotFound = ;  private  IgnoreTrailingSlash()  (length > rootLength && EndsInDirectorySeparator(validatedFullPath))  length--; ``` |

Again, I couldn’t resist changing the structure a bit as well.

I moved the *Directory* and *File* to properties on the class instead of out parameters on the method.

But, that isn’t as important as removing the comment and replacing it with a method that says the same thing while providing an abstraction on top of the logic.

I also pulled out the idea of finding the pivot into a variable, so we could use that state, explicitly rather than counting on an early return. (Which wasn’t even explained by a comment.)

Now the intent is much more clear. If we didn’t find a pivot we just want to return the trimmed directory.

## The final refactor

That brings us to our final refactor:

|  |  |
| --- | --- |
|  | ```  public class DirectoryFileSplitter  private readonly string validatedFullPath;  private  length;  private  rootLength;  private  pivotFound;  public string Directory { ; ; }  public string  { ; ; }  public DirectoryFileSplitter(string validatedFullPath)  .validatedFullPath = validatedFullPath;  length = validatedFullPath.Length;  rootLength = GetRootLength(validatedFullPath);  public  Split()  (validatedFullPath != )  IgnoreTrailingSlash();  FindPivotIndexBetweenEndOfStringAndRoot();  (!pivotFound)  TrimDirectory();  private  TrimDirectory()  Directory = validatedFullPath.Substring(, length);  private  FindPivotIndexBetweenEndOfStringAndRoot()  ( pivot = length - ; pivot >= rootLength; pivot--)  (IsDirectorySeparator(validatedFullPath[pivot]))  Directory = validatedFullPath.Substring(, pivot);  File = validatedFullPath.Substring(pivot + , length - pivot - );  pivotFound = ;  private  IgnoreTrailingSlash()  (length > rootLength && EndsInDirectorySeparator(validatedFullPath))  length--; ``` |

We’ve simply extracted the trimming of the directory into a method that says exactly what it does.

Now, in my opinion, **this code is much more clear, yet it has zero comments.**

I can quickly look at this code and understand exactly what it is doing.

The structure and naming of the variables and methods communicates in a much more precise and clear way what was being communicated in the comments of the original code.

## Compare and contrast

Take a look at the original code versus this refactored code and see which one you think is easier to understand and maintain.

Specifically compare the main method doing the work in each case:

|  |  |
| --- | --- |
|  | ```  internal static  SplitDirectoryFile(string path, out string directory, out string file)  directory = ;  file = ;  // assumes a validated full path  (path != )  length = path.Length;  rootLength = GetRootLength(path);  // ignore a trailing slash  (length > rootLength && EndsInDirectorySeparator(path))  length--;  // find the pivot index between end of string and root  ( pivot = length - ; pivot >= rootLength; pivot--)  (IsDirectorySeparator(path[pivot]))  directory = path.Substring(, pivot);  file = path.Substring(pivot + , length - pivot - );  return;  // no pivot, return just the trimmed directory  directory = path.Substring(, length);  return; ``` |

|  |  |
| --- | --- |
|  | ```  public  Split()  (validatedFullPath != )  IgnoreTrailingSlash();  FindPivotIndexBetweenEndOfStringAndRoot();  (!pivotFound)  TrimDirectory(); ``` |

Yes, I have changed the structure of the code to make it a class and I’ve replaced the out parameters with properties, but I could have achieved a similar result just getting rid of comments and replacing them with code and variable names that were more expressive. (Although, in this particular case, I’ll admit the out parameters makes things a bit more difficult.)

## Code without comments is easier to maintain

Nevertheless, I’d make the argument that trying to write code in a way that the code expresses the intent rather than relying on comments causes you to structure code in a better way which results in more cohesive classes and a better overall structure.

Whether you think I’ve made things better or not, one thing you can perhaps agree on is that I certainly haven’t made things worse.

And if you can refactor from comments to no comments without losing clarity, it’s a net win in my book, because code gets updated, comments do not. (At least they often do not.)

And remember, **this was an example with some already decent code**, where the comments weren’t very extraneous.

**Most commented code I see doesn’t look like this at all.**

In the code, the variables already had pretty good names and the comments talked about what the logic did, not how it did it.

Most of the commented code I see uses comments as a crutch for code that is not very clear at all.

So, in a sense, I picked a bad example.

I didn’t cherry-pick some crappy code with bad comments and make it better by removing them—that would have been easy.

Anyway, I await the barrage of angry commentators (no pun intended.)

**What do you think?**

Have I convinced you at all?

Can you at least see why writing code without comments isn’t lazy, but could actually be beneficial—or at the very least a matter of taste?

## GET INSTANT ACCESS

## to my FREE blogging course

Get 2 lessons via email every week and learn how to create a blog that will BOOST your career!
