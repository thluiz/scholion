---
url: "https://michaelscodingspot.com/what-i-learned-about-c-from-job-interviews/"
captured_at: "2021-02-24T08:13:46-03:00"
title: "What I Learned About C# From Job Interviews - Michael's Coding Spot"
domain: "michaelscodingspot-com"
---

# What I Learned About C# From Job Interviews

[C#](https://michaelscodingspot.com/category/csharp/) /  February 1, 2021

![learned-about-c-from-job-interviews.jpg](michaelscodingspot-com--what-i-learned-about-c-from-job-interviews/7a9ff25cbf0d260b587534cb44adff62.jpg)

I recently went through a series of job interviews for some of the biggest companies in tech. Without giving any names, I interviewed for 3 out of the top 5 tech firms in the world. You know who I’m talking about.

The interview processes in these companies were quite different from each other, but they also had a lot of things in common, including a big emphasis on coding problems. Those problems might be to sort something, to print all possible combinations, or to find your way out of a maze. I’m not sure how solving these is related to actual software development, but these companies certainly seem to think so. I don’t remember ever having to implement a sorting algorithm in my day job. Or to reverse a linked list. Or to use DFS on a graph. Still, you can make the case that a developer that’s able to solve these is going to be better in real-life problems.

But this post is not about the motivation for those questions. This post is about what I learned about C# from job interviews. Specifically, from the coding problems. I’ve been programming professionally in C# for more than 10 years, but developing software is quite different than going through interviews, as I found out.

###### By the way, all major companies allow candidates to solve problems in any programming language. So even if the position is for JavaScript, for example, you’ll still be able to write C# code.

## Multidimensional arrays are a thing

I don’t think I ever used a multidimensional array in my job. Sure, I sometimes used a list of lists `List<List<T>>` and maybe a list of arrays `List<int[]>`, and the occasional list of dictionaries of arrays `List<Dictionary<int, string[]>>` (this one not so often). Not so much multidimensional arrays. But I found out they are very useful in coding exercises.

Multidimensional arrays are not the same as arrays of arrays, like `int[][] arr` (Jagged arrays). The latter is a group of arrays where each array can be of a different length. Whereas a multidimensional array is more fitted for common problems, like representing a 2D maze or a 3D cube. If you’re going to a job interview any time soon, freshen up on the syntax of these. This includes the initializer, the dimension length, and the column/row respective indexes.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12 | int[,]arr=newint[3,2]{  {1,2},  {3,4},  {5,6}  };  intfirstDimensionLength=arr.GetLength(0);//3  intsecondDimensionLength=arr.GetLength(1);//2  varp00=arr[0,0];//1  varp01=arr[0,1];//2  varp10=arr[1,0];//3 |

Here’s an example of a question where multidimensional arrays come in handy: *Given a 2D space of MxN square cells, where each cell is either a free space or a wall, find the largest connected area of free spaces and return its number of cells.*

## Use Tuples, not Classes

I’ve been programming in C# for a while now, and it’s pretty rare for me to be using Tuples. Probably because I’m not used to the nicer new syntax of `ValueTuple`. My default choice is usually a class. There are some good things to be said for classes: They make the code more structured and arguably more readable. But tuples actually have a very nice syntax. Maybe, more importantly, they have a more *compact* syntax. There’s just less to write. And if you want to change something, there’s less to change. These things are really important in a coding interview. You want to spend the least amount of time typing code so as to leave more time to think. And possibly answer more questions.

Here’s an example. Let’s say I have a method that returns a point in a 3D array, when using a class I would write:

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9 | classPoint3D  {  publicintX{get;set;}  publicintY{get;set;}  publicintZ{get;set;}  }  privatePoint3D Calc(){...} |

Whereas with a tuple it’s:

|  |  |
| --- | --- |
| 1  2 | private(intX,intY,intZ)Calc(){...} |

Keep in mind that in a coding interview, you’ll be writing in a kind of online notepad-like environment, where you don’t have snippets, auto-complete, and all the other goodness you’re used to from Visual Studio.

## Binary operations are also a thing

How often are you using `<<`, `>>`, `&`, and `|` operators in your libraries and applications? I’m guessing not that much. Me neither, but they can be useful in coding problems. Here’s a small reminder:

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15 | inta=15;  Console.WriteLine(Convert.ToString(a,toBase:2));//1111  a=a>>2;//shift right twice (same as divide by 4)  Console.WriteLine(Convert.ToString(a,toBase:2));//11  a=a<<3;//shift left 3 times (same as multiply by 8)  Console.WriteLine(Convert.ToString(a,toBase:2));//11000  a=a&0b\_11111;// stays same  Console.WriteLine(Convert.ToString(a,toBase:2));//11000  a=a&0b\_1111;// remains 1000 because leftmost digit is nullified  Console.WriteLine(Convert.ToString(a,toBase:2));//1000  a=a|0b\_1;// becomes 1001  Console.WriteLine(Convert.ToString(a,toBase:2));//1001  a=a|0b\_110;// becomes 1111  Console.WriteLine(Convert.ToString(a,toBase:2));//1111 |

One of the things about binary is that iterating in base 2 can be helpful in permutation problems. For example, consider the following problem: *Given an array of items, print out all possible combinations of those items where each item might be included or not. The order doesn’t matter.*

So for the input [“a”,”b”,”c”], the output will be:

|  |  |
| --- | --- |
| 1  2 | [empty array],a,b,c,ab,ac,bc,abc |

Now consider iterating in binary from 0 to 2^3. If each digit describes an item of the array being included or not in the result, then that’s one way to print out all possible iterations. The above result can be described as:

|  |  |
| --- | --- |
| 1  2 | 000,001,010,100,110,101,011,111 |

Don’t rely just on binary operators though. Another way to solve this permutation problem is with simple recursion.

## Useful stuff with strings and arrays

Most of the methods used in coding problems are the same methods used in real-life coding. For strings it’s your `.Substring`, `.Contains`, `.Replace`, `string.Equals()`, `.ToLower()`, `.ToUpper()`, etc. One method I found very useful in these problems, but not so much in my job, is `string.Join`. It will join a collection of strings with a delimiter in between each couple. For example:

|  |  |
| --- | --- |
| 1  2 | varjoined=string.Join(",",new[]{"a","b","c"});// "a,b,c" |

For arrays, I discovered a couple of useful methods as well. One of them is `Array.Sort`, which can accept a `Comparison<T>` delegate to sort however you want. Let’s say you want to sort a bunch of strings according to their last letter. It’s as easy as:

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10 | varwords=new[]{"cat","job","zebra","row"};  Array.Sort(words,(w1,w2)=>  {  varlastLetter1=w1[w1.Length-1];  varlastLetter2=w2[w2.Length-1];  returnlastLetter1<lastLetter2?-1:1;// or: return lastLetter1.CompareTo(lastLetter2);  });  varjoined=string.Join(',',words);// zebra,job,cat,row |

Another useful method I never really used before is `Array.Copy`. Among other things, it can copy slices of an array to a new array. For example:

|  |  |
| --- | --- |
| 1  2  3  4  5 | varwords=new[]{"cat","job","zebra","row"};  string[]dest=newstring[2];  Array.Copy(words,sourceIndex:1,dest,destinationIndex:0,length:2);  Console.WriteLine(string.Join(',',dest));// job, zebra |

There are other ways to copy an array slice. One of those is with LINQ: `words.Skip(1).Take(2).ToArray()`. But I’m not sure I would flash my ninja C# skills in an interview with a Java programmer for example.

## Everything is shorter in Python

There’s a lot of good things to be said about C#, but it’s probably not the best language for algorithms. By that, I mean that the same solution in Python is going to be shorter and I daresay *cleaner*. If you doubt it, go to [leetcode.com](https://leetcode.com/) or any other similar site, and browse for solutions. Try comparing solutions to the same problem in C# and Python. Don’t the Python ones seem more… beautiful? Then again, maybe it’s a case of the grass is always geener on the other side of the fence.

## Stuff I learned unrelated to C#

You get to learn so much from job interviews. Both as the interviewer and as the interviewee. The most important things I learned in this entire process are not related to C# or any other language. Since this post is about coding challenges, I’ll stick to the things I learned about those. Here are some tips and tricks I picked up to help me pass coding problems:

### Practice makes perfect

Preparation for interviews is what makes all the difference. Yes, it takes a lot of time, but considering the stakes, it is very much worth it. Looking from a strictly financial point of view, getting a job in a well paying firm, with a high seniority level, is one of the most significant financial improvements you’re going to make in your life. It is definitely worth spending a few days or weeks preparing for them.

For coding problems, I used [leetcode.com](https://leetcode.com/), which is one of the best sites for those kinds of questions. I recommend starting with the Easy problems, spending the most time in Medium, and trying some of the Hard ones as well. One of the best features of this site is that you can see other submissions in the *discussion* part of each question. The site is extremely popular, so there are always submissions in all languages. I recommend trying to solve a problem yourself first, and then looking at other submissions (even if you succeeded). I certainly learned a lot from this.

### Most questions are simple

If you go browsing sites like [leetcode.com](https://leetcode.com/), you might think top firms like Facebook or Apple are going to ask you the really hard questions. That’s not true from my experience. Most questions are somewhere in the *medium* difficulty range. Not too easy, but also not tricky, and definitely not hard. Many questions are a classic implementation of a recursive DFS or BFS. Or a variation of the [Bin packing problem](https://en.wikipedia.org/wiki/Bin_packing_problem). Sometimes you’ll need to traverse a binary tree. In rare cases, you might need to use a heap.

But you can fail terribly at the easy and medium questions as well. Believe me, I know. Interviews are stressful. You have to come up with a solution very quickly. Sometimes the interviewer is going to lead you in the wrong direction (whether on purpose or not). Other times, you might remember something or become distracted, which will stray you from the correct (and easy) solution.

I learned to always keep in mind that the question is probably not tricky, but rather easy. It’s mostly true and thinking that alleviates some pressure.

### Think before writing

Before actually writing the solution, think just a bit more. Is it most optimal? Can you reach a better time complexity? Is the code going to be short and easy to understand? Ask yourself whether you can improve the solution.

Often, the interviewer will ask you to describe your solution before actually writing it. This is great for you. Even if they don’t ask, I suggest explaining it yourself. After explaining, writing the code is easier. Moreover, you will often find some issues with the solution right there. It’s also a great opportunity to bond with the interviewer. You get to show them your thought process, demonstrating you’re a smart person who’s going to be easy to work with.

### Use short names

In software development, we’re very much used to descriptive names. So I’ll have a method `GetAddress` and `CalculateFastestRoute` instead of `Get` and `Calc`. In coding problems, the exact opposite is the way to go. At least this is what worked for me. Stick with short names for both variable names and methods. If you feel your interviewer is a stickler, you can rename them after your solution works or just mention that you’re using short names for this interview, not as a rule.

I’m not saying to name your methods `A` and `B`. But I am saying that if your problem is to iterate through a maze, and you’re using a Depth First Search algorithm, feel free to name the method `DFS` instead of `FindAWayInAMaze`.

## Finishing up

Interviewing for a big enterprise is a fascinating experience. It’s completely different than being interviewed for a start-up or even for a large-sized tech company. The interviews are very different between companies, and you can get some sense of the company culture.

I talked here about coding problems, but that’s just one part of the interviews. Most companies also have some kind of “system design” interview where you have to architect a big (usually distributed) system. Another part of the interview process is about your conduct, attitude, and behavior in an organization. Are you a team player? Are you always thinking about the customer? Can you work independently? These are probably as important as the technical questions.

As for the results of my own interviews, I’m happy to say that I’m starting a new position at Microsoft! I’ll tell more on [Twitter](https://twitter.com/MichaelShpilt) and [LinkedIn](https://www.linkedin.com/in/michael-shpilt-1a144a67) for whoever’s interested.

Share:

Want to become an expert problem solver? Check out a chapter from my book Practical Debugging for .NET Developers
