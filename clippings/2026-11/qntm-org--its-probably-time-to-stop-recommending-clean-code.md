---
url: "https://qntm.org/clean"
captured_at: "2026-11-16T03:32:41+00:00"
title: "It's probably time to stop recommending Clean Code"
domain: "qntm-org"
---

It may not be possible for us to ever reach empirical definitions of "good code" or "clean code", which means that any one person's opinions about another person's opinions about "clean code" are necessarily highly subjective. I cannot review Robert C. Martin's 2008 book [_Clean Code_](https://learning.oreilly.com/library/view/clean-code/9780136083238/) from your perspective, only mine.

That said, the major problem I have with _Clean Code_ is that a lot of the example code in the book is _just dreadful_.

#### \*

In chapter 3, "Functions", Martin gives a variety of advice for writing functions well. Probably the strongest single piece of advice in this chapter is that **functions should not mix levels of abstraction**; they should not perform both high-level and low-level tasks, because this is confusing and muddles the function's responsibility. There's other valid stuff in this chapter: Martin says that function names should be descriptive, and consistent, and should be verb phrases, and should be chosen carefully. He says that functions should do exactly one thing, and do it well, which I agree with... provided that we aren't too dogmatic about how we define "one thing", and we understand that in plenty of cases this can be highly impractical. He says that functions should not have side effects (and he provides a really great example), and that output arguments are to be avoided in favour of return values. He says that functions should generally either be commands, which _do_ something, or queries, which _answer_ something, but not both. This is all reasonable entry-level advice.

But mixed into the chapter there are more questionable assertions. Martin says that Boolean flag arguments are bad practice, which I agree with, because an unadorned `true` or `false` in source code is opaque and unclear _versus_ an explicit `IS_SUITE` or `IS_NOT_SUITE`... but Martin's reasoning is rather that a Boolean argument means that a function does more than one thing, which it shouldn't.

Martin says that it should be possible to read a single source file from top to bottom as narrative, with the level of abstraction in each function descending as we read on, each function calling out to others further down. This is far from universally relevant. Many source files, I would even say most source files, cannot be neatly hierarchised in this way. And even for the ones which can, an IDE lets us trivially jump from function call to function implementation and back, the same way that we browse websites.

He says code duplication "may be the root of all evil in software" and fiercely advocates [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself). At the time, this was quite standard advice. In more recent times, however, we generally understand that [a little duplication isn't the worst thing in the world](https://overreacted.io/goodbye-clean-code/); it can be clearer, and it can be [cheaper than the wrong abstraction](https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction).

And then it gets weird. Martin says that functions should not be large enough to hold _nested_ control structures (conditionals and loops); equivalently, they should not be indented to more than two levels. He says blocks should be one line long, consisting probably of a single function call. He says that an ideal function has _zero arguments_ (but still no side effects?), and that a function with just three arguments is confusing and difficult to test. Most bizarrely, Martin asserts that an ideal function is _two to four lines of code long_. This piece of advice is actually placed at the start of the chapter. It's the first and most important rule:

> The first rule of functions is that they should be small. The second rule of functions is that _they should be smaller than that_. This is not an assertion that I can justify. I can’t provide any references to research that shows that very small functions are better. What I can tell you is that for nearly four decades I have written functions of all different sizes. I’ve written several nasty 3,000-line abominations. I’ve written scads of functions in the 100 to 300 line range. And I’ve written functions that were 20 to 30 lines long. What this experience has taught me, through long trial and error, is that functions should be very small.
> 
> \[...\]
> 
> When Kent \[Beck\] showed me the code, I was struck by how small all the functions were. I was used to functions in Swing programs that took up miles of vertical space. Every function in _this_ program was just two, or three, or four lines long. Each was transparently obvious. Each told a story. And each led you to the next in a compelling order. _That’s_ how short your functions should be!

All of this sounds like hyperbole. A case for short functions instead of long ones can certainly be made, but we assume that Martin doesn't _literally_ mean that every function in our entire application _must_ be four lines long or less.

But the book is being absolutely serious about this. All of this advice culminates in the following source code listing at the end of chapter 3. This example code is **Martin's preferred refactoring** of [a pair of Java methods](https://github.com/unclebob/fitnesse/blob/3bec390e6f8e9e341149b7d060551a92b93d3154/src/fitnesse/html/HtmlUtil.java#L279-L331) originating in an open-source testing tool, [FitNesse](http://www.fitnesse.org/).

package fitnesse.html;

import fitnesse.responders.run.SuiteResponder;
import fitnesse.wiki.\*;

public class SetupTeardownIncluder {
  private PageData pageData;
  private boolean isSuite;
  private WikiPage testPage;
  private StringBuffer newPageContent;
  private PageCrawler pageCrawler;


  public static String render(PageData pageData) throws Exception {
    return render(pageData, false);
  }

  public static String render(PageData pageData, boolean isSuite)
    throws Exception {
    return new SetupTeardownIncluder(pageData).render(isSuite);
  }

  private SetupTeardownIncluder(PageData pageData) {
    this.pageData = pageData;
    testPage = pageData.getWikiPage();
    pageCrawler = testPage.getPageCrawler();
    newPageContent = new StringBuffer();
  }

  private String render(boolean isSuite) throws Exception {
     this.isSuite = isSuite;
    if (isTestPage())
      includeSetupAndTeardownPages();
    return pageData.getHtml();
  }

  private boolean isTestPage() throws Exception {
    return pageData.hasAttribute("Test");
  }

  private void includeSetupAndTeardownPages() throws Exception {
    includeSetupPages();
    includePageContent();
    includeTeardownPages();
    updatePageContent();
  }


  private void includeSetupPages() throws Exception {
    if (isSuite)
      includeSuiteSetupPage();
    includeSetupPage();
  }

  private void includeSuiteSetupPage() throws Exception {
    include(SuiteResponder.SUITE\_SETUP\_NAME, "-setup");
  }

  private void includeSetupPage() throws Exception {
    include("SetUp", "-setup");
  }

  private void includePageContent() throws Exception {
    newPageContent.append(pageData.getContent());
  }

  private void includeTeardownPages() throws Exception {
    includeTeardownPage();
    if (isSuite)
      includeSuiteTeardownPage();
  }

  private void includeTeardownPage() throws Exception {
    include("TearDown", "-teardown");
  }

  private void includeSuiteTeardownPage() throws Exception {
    include(SuiteResponder.SUITE\_TEARDOWN\_NAME, "-teardown");
  }

  private void updatePageContent() throws Exception {
    pageData.setContent(newPageContent.toString());
  }

  private void include(String pageName, String arg) throws Exception {
    WikiPage inheritedPage = findInheritedPage(pageName);
    if (inheritedPage != null) {
      String pagePathName = getPathNameForPage(inheritedPage);
      buildIncludeDirective(pagePathName, arg);
    }
  }

  private WikiPage findInheritedPage(String pageName) throws Exception {
    return PageCrawlerImpl.getInheritedPage(pageName, testPage);
  }

  private String getPathNameForPage(WikiPage page) throws Exception {
    WikiPagePath pagePath = pageCrawler.getFullPath(page);
    return PathParser.render(pagePath);
  }

  private void buildIncludeDirective(String pagePathName, String arg) {
    newPageContent
      .append("\\n!include ")
      .append(arg)
      .append(" .")
      .append(pagePathName)
      .append("\\n");
  }
}

I'll say again: this is Martin's own code, written to his personal standards. This is the ideal, presented to us as a learning example.

I will confess at this stage that my Java skills are dated and rusty, almost as dated and rusty as this book, which is from 2008. But surely, even in 2008, this code was illegible trash?

Let's ignore the wildcard `import`.

First, the class name, `SetupTeardownIncluder`, is dreadful. It _is_, at least, a noun phrase, as all class names should be. But it's a nouned verb phrase, the strangled kind of class name you invariably get when you're working in strictly object-oriented code, where everything has to be a class, but sometimes the thing you really need is just one simple gosh-danged _function_.

Inside the class, we have:

*   two public, static methods, as before, plus
*   one new private constructor and
*   **fifteen** new private methods.

Of the fifteen private methods, fully thirteen of them either have side effects (such as `buildIncludeDirective`, which has side effects on `newPageContent`) or call out to other methods which have side effects (such as `include`, which calls `buildIncludeDirective`). Only `isTestPage` and `findInheritedPage` look to be side-effect-free. They still make use of variables which aren't passed into them (`pageData` and `testPage` respectively) but they _appear_ to do so in side-effect-free ways.

At this point you might reason that maybe Martin's definition of "side effect" doesn't include member variables of the object whose method we just called. If we take this definition, then the five member variables, `pageData`, `isSuite`, `testPage`, `newPageContent` and `pageCrawler`, are implicitly passed to _every_ private method call, and they are considered fair game; any private method is free to do anything it likes to any of these variables.

But Martin's own definition contradicts this. This is from earlier in this exact chapter, with emphasis added:

> Side effects are lies. Your function promises to do one thing, but it also does other hidden things. **Sometimes it will make unexpected changes to the variables of its own class.** \[...\] \[T\]hey are devious and damaging mistruths that often result in strange temporal couplings and order dependencies.

I like this definition of "side effect". I agree with this definition. It's a useful definition, because avoiding side effects enables us to reason about what a function does, with some degree of confidence, by referring only to its inputs and output. I agree that it's bad for a function to make _unexpected_ changes to the variables of its own class.

So why does Martin's own code, "clean" code, do _nothing but this_? Rather than have a method pass arguments to another method, Martin makes a distressing habit of having the first method set a member variable which the second method, or some other method, then reads back. This makes it incredibly hard to figure out what any of this code does, because all of these incredibly tiny methods do almost nothing and work exclusively through side effects.

Let's just look at one private method.

private String render(boolean isSuite) throws Exception {
   this.isSuite = isSuite;
  if (isTestPage())
    includeSetupAndTeardownPages();
  return pageData.getHtml();
}

So... imagine that someone enters a kitchen, because they want to show you how to make a cup of coffee. As you watch carefully, they flick a switch on the wall. The switch looks like a light switch, but none of the lights in the kitchen turn on or off. Next, they open a cabinet and take down a mug, set it on the worktop, and then tap it twice with a teaspoon. They wait for thirty seconds, and finally they reach behind the refrigerator, where you can't see, and pull out a _different_ mug, this one full of fresh coffee.

...What just happened? What was flicking the switch for? Was tapping the empty mug part of the procedure? Where did the coffee come from?

That's what this code is like. Why does `render` have a side effect of setting the value of `this.isSuite`? When is `this.isSuite` read back, in `isTestPage`, in `includeSetupAndTeardownPages`, in both, in neither? If it does get read back, why not just pass `isSuite` in as a Boolean? Or perhaps the caller reads it back?

Why do we return `pageData.getHtml()` when we never touched `pageData`? How did the HTML get there? Was it already there? We might make an educated guess that `includeSetupAndTeardownPages` has side effects on `pageData`, but then, what? We can't know either way until we look. And what other side effects does that have on other member variables? The uncertainty becomes so great that we suddenly have to wonder if calling `isTestPage()` could have side effects too.

How would you unit-test this method? Well, you can't. It's not a unit. It can't be separated from the side-effects it has on other parts of the code. (And what's up with the indentation? And where are the danged braces?)

Martin states, in this very chapter, that it makes sense to break a function down into smaller functions "if you can extract another function from it with a name that is not merely a restatement of its implementation". But then he gives us:

private boolean isTestPage() throws Exception {
  return pageData.hasAttribute("Test");
}

and:

private WikiPage findInheritedPage(String pageName) throws Exception {
  return PageCrawlerImpl.getInheritedPage(pageName, testPage);
}

and half a dozen others, none of which are even called from more than one location.

There is at least one questionable aspect of this code which isn't Martin's fault: the fact that `pageData`'s content gets destroyed. Unlike the member variables (`isSuite`, `testPage`, `newPageContent` and `pageCrawler`), `pageData` is not actually ours to modify. It is originally passed in to the top-level public `render` methods by an external caller. The `render` method does a lot of work and ultimately returns a `String` of HTML. However, during this work, as a side effect, `pageData` is destructively modified (see `updatePageContent`). Surely it would be preferable to create a brand new `PageData` object with our desired modifications, and leave the original untouched? If the caller tries to use `pageData` for something else afterwards, they might be very surprised about what's happened to its content. But this is [how the original code behaved](https://github.com/unclebob/fitnesse/blob/3bec390e6f8e9e341149b7d060551a92b93d3154/src/fitnesse/html/HtmlUtil.java#L329) prior to the refactoring, and the behaviour could be intentional. Martin has preserved the behaviour, though he has buried it very effectively.

Some other mild puzzles: why do we use `pageData.hasAttribute("Test")` to figure out whether this is a test page, but we have to consult a separate Boolean to figure out whether or not this is a test _suite_ page? And what exactly is the separation of concerns between `PageCrawler` and `PageCrawlerImpl`, both of which are in use here?

#### \*

Is the whole book like this?

Pretty much, yeah. _Clean Code_ mixes together a disarming combination of strong, timeless advice and advice which is highly questionable or dated or both.

Much of the book is no longer of much use. There are multiple chapters of what are basically filler, focusing on laborious worked examples of refactoring Java code; there is a whole chapter examining the internals of JUnit. This book is from 2008, so you can imagine how relevant that is now. There's a whole chapter on formatting, which these days reduces to a single sentence: "Pick a sensible standard formatting, configure automated tools to enforce it, and then never think about this topic again."

The content focuses almost exclusively on object-oriented code, to the exclusion of other programming paradigms. Object-oriented programming was very fashionable at the time of publication. Martin is a huge proponent of OO, having invented three of the five principles which make up [SOLID](https://en.wikipedia.org/wiki/SOLID), and having popularised the term. But the total absence of functional programming techniques or even simple procedural code was regrettable even then, and has only grown more obvious in the years since.

The book focuses on Java code, to the exclusion of other programming languages, even other object-oriented programming languages. Java was popular at the time, and if you're writing a book like this, it makes sense to pick a single well-known language and stick with it, and Java is still very popular and may still be a strong choice for this purpose. But the book's overall use of Java is very dated.

This kind of thing is unavoidable — programming books date legendarily poorly. That's part of the reason why _Clean Code_ was a recommended read at one time, and I now think that the pendulum is swinging back in the opposite direction.

But even for the time, even for 2008-era Java, much of the provided code is _bad_.

There's a chapter on unit testing. There's a lot of good, basic, stuff in this chapter, about how unit tests should be fast, independent and repeatable, about how unit tests enable more confident refactoring of source code, about how unit tests should be about as voluminous as the code under test, but strictly simpler to read and comprehend. But then he shows us a unit test with what he says is too much detail:

@Test
  public void turnOnLoTempAlarmAtThreashold() throws Exception {
    hw.setTemp(WAY\_TOO\_COLD);
    controller.tic();
    assertTrue(hw.heaterState());
    assertTrue(hw.blowerState());
    assertFalse(hw.coolerState());
    assertFalse(hw.hiTempAlarm());
    assertTrue(hw.loTempAlarm());
  }

and he proudly refactors it to:

@Test
  public void turnOnLoTempAlarmAtThreshold() throws Exception {
    wayTooCold();
    assertEquals(“HBchL”, hw.getState());
  }

This is done as part of an overall lesson in the virtue of _inventing a new domain-specific testing language for your tests_. I was left so confused by this suggestion. I would use exactly the same code to demonstrate exactly the opposite lesson. Don't do this!

Which is to say nothing of the method named `wayTooCold`. This is an adjective phrase. It's entirely unclear what this method does. Does it _set_ the world's state to be way too cold? Does it _react_ to the world's state _becoming_ way too cold? Or is it an _assertion_ that the world's state currently must _be_ way too cold?

Methods should have verb or verb phrase names like `postPayment`, `deletePage`, or `save`. That's not me saying that. That's a direct quote from this book. Chapter 2, "Meaningful Names":

> Methods should have verb or verb phrase names like `postPayment`, `deletePage`, or `save`.

This is perfectly sound advice. And `hw.setTemp(WAY_TOO_COLD);` was a perfectly unambiguous line of code. What gives?

And even if you guess correctly that calling `wayTooCold()` _sets_ the temperature to be way too cold... there's no way that you could guess that it also calls `controller.tic()` internally. Earlier, we were advised to avoid code having side effects. This, also, was sound advice. And it is, again, being ignored in the actual written code example.

(And since we're here, this, the original unrefactored code, is a fine demonstration of the drawbacks of unadorned Booleans. What does it mean when, say, `coolerState` returns `true`? Does it mean that the cooler's current state is good, _i.e._ cold enough, _i.e._ switched off? Or does it mean that it is powered on, and actively cooling? An `enum` with a few values, `ON` and `OFF`, could be less ambiguous.)

#### \*

The book presents us with the [TDD](https://en.wikipedia.org/wiki/Test-driven_development) loop:

> **First Law** You may not write production code until you have written a failing unit test.
> 
> **Second Law** You may not write more of a unit test than is sufficient to fail, and not compiling is failing.
> 
> **Third Law** You may not write more production code than is sufficient to pass the currently failing test.
> 
> These three laws lock you into a cycle that is perhaps thirty seconds long. The tests and the production code are written together, with the tests just a few seconds ahead of the production code.

But the book doesn't acknowledge the missing zeroth step in the process: figuring out how to break down the programming task in front of you, so that you can take a minuscule thirty-second bite out of it. _That_, in many cases, is exceedingly time-consuming, and frequently obviously useless, and frequently impossible.

#### \*

There's a whole chapter on "Objects and Data Structures". In it, we're provided with this example of a data structure:

public class Point {
  public double x;
  public double y;
}

and this example of an object (well, the interface for one):

public interface Point {
  double getX();
  double getY();
  void setCartesian(double x, double y);
  double getR();
  double getTheta();
  void setPolar(double r, double theta);
}

Martin writes:

> These two examples show the difference between objects and data structures. Objects hide their data behind abstractions and expose functions that operate on that data. Data structure expose their data and have no meaningful functions. Go back and read that again. Notice the complimentary nature of the two definitions. They are virtual opposites. This difference may seem trivial, but it has far-reaching implications.

And... that's it?

Yes, you're understanding this correctly. Martin's definition of "data structure" disagrees with the definition everybody else uses. This is a very strange choice of definition, though Martin does at least define his term clearly. Drawing a clear distinction between objects as dumb data and objects as sophisticated abstractions with methods is legitimate, and useful. But it's quite glaring that there is no content in the book _at all_ about clean coding using [what most of us consider to be real data structures](https://en.wikipedia.org/wiki/List_of_data_structures): arrays, linked lists, hash maps, binary trees, graphs, stacks, queues and so on. This chapter is _much_ shorter than I expected, and contains very little information of value.

#### \*

I'm not going to rehash all the rest of my notes. I took a lot of them, and calling out everything I perceive to be wrong with this book would be counterproductive. I'll stop with one more egregious piece of example code. This is from chapter 8, a prime number generator:

package literatePrimes;

import java.util.ArrayList;

public class PrimeGenerator {
  private static int\[\] primes;
  private static ArrayList<Integer> multiplesOfPrimeFactors;

  protected static int\[\] generate(int n) {
    primes = new int\[n\];
    multiplesOfPrimeFactors = new ArrayList<Integer>();
    set2AsFirstPrime();
    checkOddNumbersForSubsequentPrimes();
    return primes;
  }

  private static void set2AsFirstPrime() {
    primes\[0\] = 2;
    multiplesOfPrimeFactors.add(2);
  }

  private static void checkOddNumbersForSubsequentPrimes() {
    int primeIndex = 1;
    for (int candidate = 3;
         primeIndex < primes.length;
         candidate += 2) {
      if (isPrime(candidate))
        primes\[primeIndex++\] = candidate;
    }
  }

  private static boolean isPrime(int candidate) {
    if (isLeastRelevantMultipleOfNextLargerPrimeFactor(candidate)) {
      multiplesOfPrimeFactors.add(candidate);
      return false;
    }
    return isNotMultipleOfAnyPreviousPrimeFactor(candidate);
  }

  private static boolean
  isLeastRelevantMultipleOfNextLargerPrimeFactor(int candidate) {
    int nextLargerPrimeFactor = primes\[multiplesOfPrimeFactors.size()\];
    int leastRelevantMultiple = nextLargerPrimeFactor \* nextLargerPrimeFactor;
    return candidate == leastRelevantMultiple;
  }

  private static boolean
  isNotMultipleOfAnyPreviousPrimeFactor(int candidate) {
    for (int n = 1; n < multiplesOfPrimeFactors.size(); n++) {
      if (isMultipleOfNthPrimeFactor(candidate, n))
        return false;
    }
    return true;
  }

  private static boolean
  isMultipleOfNthPrimeFactor(int candidate, int n) {
   return
     candidate == smallestOddNthMultipleNotLessThanCandidate(candidate, n);
  }

  private static int
  smallestOddNthMultipleNotLessThanCandidate(int candidate, int n) {
    int multiple = multiplesOfPrimeFactors.get(n);
    while (multiple < candidate)
      multiple += 2 \* primes\[n\];
    multiplesOfPrimeFactors.set(n, multiple);
    return multiple;
  }
}

What the heck is this code? What is this algorithm? What are these _method names_? `set2AsFirstPrime`? `smallestOddNthMultipleNotLessThanCandidate`? Why does the code break with an out-of-bounds exception if we replace the `int[]` with a second `ArrayList<Integer>`? Earlier, we were advised that a method should be a command, which _does_ something, or a query, which _answers_ something, but not both. This was good advice, so why do nearly all of these methods ignore it? And what of thread safety?

Is this meant to be clean code? Is this meant to be a legible, intelligent way to search for prime numbers? Are we supposed to write code like this? And if not, why is this example in the book? And where is the "real" answer?

If this is the quality of code which this programmer produces — at his own leisure, under ideal circumstances, with none of the pressures of real production software development, _as a teaching example_ — then why should you pay any attention at all to the rest of his book? Or to his other books?

#### \*

I wrote this essay because I keep seeing people recommend _Clean Code_. I felt the need to offer an anti-recommendation.

I originally read _Clean Code_ as part of a reading group which had been organised at work. We read about a chapter a week for thirteen weeks. (The book has seventeen chapters, we skipped some for reasons already mentioned.)

Now, you don't want a reading group to get to the end of each session with nothing but unanimous agreement. You want the book to draw out some kind of reaction from the readers, something additional to say in response. And I guess, to a certain extent, that means that the book has to either say something you disagree with, or not say everything you think it should say. On that basis, _Clean Code_ was _okay_. We had good discussions. We were able to use the individual chapters as launching points for deeper discussions of _actual_ modern practices. We talked about a great deal which was not covered in the book. We disagreed with a lot in the book.

Would I recommend this book? **No.** Would I recommend it as a beginner's text, with all the caveats above? No. Would I recommend it as a historical artifact, an educational snapshot of what programming best practices used to look like, way back in 2008? No, I would not.

#### \*

So the killer question is, what book(s) would I recommend instead? I don't know. Suggestions in the comments, unless I've closed them.

### Update, 2020-12-19

After suggestions from comments below, I read _A Philosophy of Software Design_ (2018) by John Ousterhout and found it to be a much more positive experience. I would be happy to recommend it over _Clean Code_.

_A Philosophy of Software Design_ is not a drop-in replacement for _Clean Code_. As the title suggests, it focuses more on the practice of software design at a higher level than it does on the writing or critiquing of actual individual lines of code. (As such, it contains relatively few code examples.) Because it's aimed at this higher level, I think it's possibly not a suitable read for absolute beginner programmers. A lot of this high-level theory is difficult to comprehend or put into practice until you have some real experience to compare it with. I think there actually is something of a gap in the market for an entry-level introductory programming text right now.

Having said that, I found _A Philosophy of Software Design_ to be informative, cogent, concise and _much_ more up-to-date. I found that I agreed with nearly all of Ousterhout's assertions and suggestions for good software design, many of which are diametrically opposed to those found in _Clean Code_. By virtue of providing relatively high-level advice, I feel that the book is likely to age rather better too.

Of course, software development is still moving forwards as I write this. Who knows what a good programming book will look like in ten more years?

### Afterword, 2022-03-21

Probably the most common defence of _Clean Code_ that I've seen coming from readers of this essay is that the book _is_ still worth recommending, despite the objections above, because the advice in the book shouldn't be taken entirely literally, or applied dogmatically. The burden is on the reader to think critically, draw their own conclusions, and selectively ignore the book's advice when that advice is bad. Even the book itself says:

> \[M\]any of the recommendations in this book are controversial. You will probably not agree with all of them. You might violently disagree with some of them. That's fine. We can't claim final authority.

I don't think this is a particularly convincing defence of the book containing bad advice and bad example code in the first place.

It's true that we should always engage critically with material instead of passively letting it wash over us. This is universally understood; this is what reading _is_; this is what the essay above is. This doesn't need to be stated, and it's redundant for the book itself to mention the point at all. This isn't something which can be used to shield a book from criticism.

What's more important is what the book actually says. And, especially in an instructional text like this, _how carefully_ the book has to be read in order to get a positive experience out of it, and what happens if the book isn't read sufficiently critically.

Experienced programmers will get almost nothing out of reading _Clean Code_. They'll be able to weigh the advice given against their own experiences and make an informed decision — and the book will tell them almost nothing that they didn't learn years ago.

Inexperienced programmers, meanwhile — and _Clean Code_ is an entry-level programming text, so this is the target audience, whose experiences are most important — won't be able to distinguish the good advice from the bad, and won't be able to see that the example code is bad and shouldn't be imitated. Inexperienced programmers will take those lessons at face value, and it might be years before they figure out how badly they were misled.

### Discussion (145)

#### [2020-06-29 10:21:12](#komment5ef9a4789921e) by TZ:

I reread your breakdown of the FitNesse code example a few times and I felt less and less generous about the analysis each time. Here's two and half questions: 1) If private fields are NOT to be considered implicit arguments to every private method, what exactly are they for? (And if they should not be modified, why would they be anything other than 'final'?) 2) Why do you consider Martin's definition of side-effect, which speaks of 'global state' and 'unexpected changes' to include changes to private members of the class in functions that document those changes via their signature? You could answer those uncharitably and make Uncle Bob look bad, or you could answer them charitably and then his code makes sense. I also have to say I don't understand how 'illegible trash' is remotely an appropriate description. This is as good as just about anything I've seen in actual production work in 10 years. It's extremely readable and quite testable. There are nits to pick (and you've done an excellent job of that), but for some part of those at least I feel like they're to be picked with 2008 Java API and coding standards rather than the author. I can't see that reading this book would be a net negative for 95% of people writing OO code. If you also don't know of a better book either, I'm stumped as to why you'd stop recommending it. Finally, it looks to me like there's people out to get Uncle Bob cancelled for not being on-board with a certain political invasion of software that's going around at the moment (you can already see a comment calling him 'a terrible human'), so I'm somewhat suspicious of ulterior motives here. If that's not your intent, my apologies. I did like this article in general and found it to be plenty insightful, so I'd love to read more from you.

#### [2020-06-29 11:53:14](#komment5ef9ba0a5d411) by Sander Vermeer:

I think the idea of clean code is ridiculous. Code should simply be straightforward. A common pitfall is over-engineering, where the code is made more complicated than needs to be. But I see this in every aspect of programming, where people spend hours in creating a build file (Cmake etc.), creating UML diagrams, pre-defining API's, but also create unnecessary functions and classes ('I might need that later on') etc. etc. Which honestly is just a waste of time. Since programming is an inherent iterative process, code should be written as such. The general idea is simple; create a quick and dirty solution for the problem at hand. Than, refine the code so it's more reusable, more readable, more testable. More often than not, the API and data structures needed to solve that problem naturally emerge. Also, because the code was developed bottom up, any oversights or over-complications are easily avoided. Oh and what most people lost over time is the ability to think about programming as the transformation of data. In game development for instance, every game is essentially 1) handle user input, 2) generate images and sound. Of course there are thousands of steps in between (you need to simulate some system/world, load assets from disk, populate the world, calculate animations, create a rendering pipeline), but every step is still the manipulation of data into a desired result. And I think that way of reasoning about your code is lost when OOP became the defacto paradigm.

#### [2020-06-29 18:29:54](#komment5efa1702e1f83) by Elf M. Sternberg:

The thing that drives me absolutely crazy about Martin's approach is his almost religious insistence that one not "choose a database" before writing code. The relational algebra is one of the most important algorithms of the 20th century, and yet Martin wants you to write and manage your own relationships in the code you write yourself. To me, writing your own relational management code when you have a perfectly solid enforcement mechanism already present is programmatic malpractice. The other thing that I find infuriating is that I'll run into people who insist "no frameworks!" Martin says that your code shouldn't be about Javabeans or Django, it should be about what it's about: if you're writing a payroll app, the app's repository should say "payroll!" Which is great advice. But every time I've looked over an application written to "clean code" standards, I see folders labeled "domain," "services," "use\_cases," "gateways," "adapters." I call this "Writing to the Clean Code Framework," because that's exactly what it is.

#### [2020-06-29 19:58:30](#komment5efa2bc6c7130) by Hamled:

One thing I remember from watching the old SICP lecture videos was this idea that you should look at your code as defining a new language, and factor your code with functions which are the most useful terms in that language. Pretty basic advice I suppose, but it feels relevant to what Martin is talking about in this book. If you factor your code into functions that are minimal but necessary, you can provide clarity through both the structure and explicit naming of meaningful concepts/actions. However, based on these examples it seems like Martin has perverted that idea quite a bit. He's taken this core of a good idea and morphing it into an odd approach to self-documenting code: instead of writing a comment next to every few lines, you put it into a function named the same as what that comment would have been. Of course, the commenting style is noisy but broadly innocuous. Doing the same with factoring instead ends up implying many things about the code that are orthogonal to the original goal of documentation. Basically zero of these tiny functions he's created in these examples are called in multiple places, for example. And of course it's throwing away the point of abstraction if you use a naming convention that seeks to encompass every detail of the unit being named. I think his prime number generator example contains another great example of these problems, not mentioned in the post. His code for checking whether a candidate is "a multiple of any previous prime factor" actually has side-effects despite being named like a "query" function in his terminology. Not only that, the side-effect is modifying an array while that array is being iterated. This is probably just how a prime sieve works (IDK), but it's far from obvious that is what's going on because the mutative function is multiple calls away from the function with the loop. I wonder how much Martin has been subject to code reviews throughout his career.

#### [2020-06-30 17:38:27](#komment5efb5c737a8fc) by Sam J M:

Back when I was a young coder many moons ago I tried my damnedest to study and practice what uncle Bob was preaching. All my colleagues were raving about uncle Bob's masterpieces. I thought I was deficient for not being able to come to terms with and accept the folksy uncle's gospel truth. Working in a company designing and producing embedded systems and controllers drilled into my psyche the importance of clear requirements, and most of the errors we encountered were a result of imprecise requirements. This is something uncle Bob doesn't bother about, instead, he goes on about craftsmanship and professionalism. Later when I moved to larger software projects, the best ones were those that were readable, unassuming, well commented, and didn't go crazy over some religious doctrine of code styles. Uncle Bob also conveniently ignores the engineering aspect of large projects with multiple distributed teams working across different timezones and cultures and the multitude of challenges they bring. Most code is not written by 'craftsmen' who follow a codestyle religion. A lot of requirements reviews, design reviews, and so on... I recently heard him talk about some software project he had worked for some sort of content management, where he went on to say the database was an afterthought and unimportant. I lost all respect for the guy after that.

#### [2020-07-03 00:28:46](#komment5efe5f9e6e790) by kpreid:

The test code you criticize. { assertEquals(“HBchL”, hw.getState()); } does have one practical advantage over the set of assertFalse and assertTrue it is replacing: it lets you see the entire set of outputs of the controller in the test failure output, whereas the other version gives you only one of the outputs, unless you either run it under a debugger or change the order of the asserts to make another one fail first. That said, if I were spending time on engineering the tests, what I'd do is write test helper methods for the assertions so that when \*any\* of those boolean assertions fail, \*all\* of the state is printed (which can then be less cryptic than “HBchL”). Or, use a test framework that doesn't abort execution as soon as a single assertion fails, but presents a list of all of the failures. Another common example of unhelpful test failure I have seen is { assertEquals(2, list.size()); assert something about list.get(0); assert something about list.get(1); } where if the list is not the expected size, you have no information about what it actually contained. I have found that in complex code, test failures that explain what went wrong in detail are very helpful because if you broke something \*that you didn't expect to break\* — that might be a distant dependent of the thing you changed — then the test having a good description of the problem means you can proceed like "oh, I didn't realize I need to handle that case—there, done". instead of having to fire up the debugger or reading lots of code that you weren't intending to be working on.

#### [2020-07-03 03:16:57](#komment5efe87097adb7) by Mike Bridge:

You've made several mistakes here. Briefly: - A boolean flag argument is usually a bad idea whether you give it a label or not. The point---which you seem to acknowledge and then ignore---is that a boolean flag \*may\* indicate that you have two paths through your code. Similarly, two boolean flags \*may\* mean that you have four. This has nothing to do with the naming of the boolean argument or having to do extra work to navigate the code. - Martin is \*not\* saying FitNesse example is "ideal" code. His goal in chapter 3---still early in the book---is to give the high-level view of the technique for making garbage code into humanly-understandable and maintainable code by refactoring, with the help of some rules-of-thumb. Really, this is an introduction to the whole point of the book. Sure it's not perfect, but he's not claiming it is. - It sounds to me like you're missing the big picture when you say there's a "missing fourth step" in TDD. He \*doesn't\* say that you break down the problem into abstractions first, then write code, then test it---he's saying it's the opposite: you write tests, then write code, then refactor it, then keep repeating the process until you have a good abstraction. Your first iteration may well be a mess, but he's saying that that doesn't matter---you can work on finding better abstractions once the code works. In other words, it's much harder to write good code if you try to figure it all out in your head out a-priori. - I'm not sure how you define "Data Structures", despite the link to WikiPedia. How is this different from Martin's definition? - And \*yes\*, set2AsFirstPrime and smallestOddNthMultipleNotLessThanCandidate make perfect sense to me. Do you have a better suggestion? "What the heck?" doesn't give me any insight. - And there are perfectly good arguments for using wildcard imports.

#### [2020-07-09 00:34:03](#komment5f0649db74196) by qntm:

A few people have recommended Code Complete as a replacement for Clean Code. I think it's a better book, but I'd still be hesitant to recommend it. I don't have anywhere near as much to say about Code Complete because I haven't read it cover to cover, because it's a monster. I have the first edition, which is 850 pages long. That in itself is well worth considering. But the main thing about Code Complete is that even if all the information in it was complete and correct at the time of going to press, it's really quite dated right now. Even the second edition is from 2004, \*predating\* Clean Code. As I say, this is just a standing problem which almost all programming books have. Fifteen years is a \*long\* time in software development. There are some other strong recommendations in this thread, but these are books which sadly I have not read (I spend far too much time writing and not enough time reading). That means I can't recommend them myself. For what it's worth, on the basis of what people have said here and elsewhere, these are the programming books which I'm most likely to read next: \* John Ousterhout, A Philosophy Of Software Design (2018) \* Michael Feathers, Working Effectively With Legacy Code (2004, oof)

#### [2020-07-24 09:16:14](#komment5f1a8abe86f61) by FeepingCreature:

FP and OOP are totally compatible. This is approximately how we do it where I work: FP for everything small. Pure data is pure, and manipulated by pure methods. Immutable data structures, return instead of ref, recreation rather than modification. No OOP here. Then, the application code has separated areas of responsibility. These are classes that may hold state, and mutate it by business-level methods. But each set of data is only stored and mutated in one class. Anything that can be mutated is private, and no mutable references to it are handed out. Then, OOP is used lightly, mostly just to separate interfaces and implementations between different areas of the codebase, and for bits of dependency injection to avoid dependency cycles. So code reuse is mostly achieved by composition rather than inheritance. The FP routines manipulating data basically never see any OOP themselves. Also, the example unittest would compare a state struct with cleanly labeled flags. Thanks to a diff routine, the mismatching flag would be highlighted in red/green. :) That is to say: none of the examples in this post would pass code review.

#### [2020-09-15 02:01:55](#komment5f60128347231) by Ray:

Frank, I would argue that if the examples are bad enough, you're better off with no examples at all, and that the prime number generator, in particular, falls into that category. But since you want an alternative, I've thrown together an implementation of the same function. I've replaced each tab with ". . " in hopes of preserving the formatting. We'll see how well that works. As a side note, the below code uses the simplest prime number sieve, and takes about 45 seconds to find the first 20 million primes. The Clean Code version takes \*22 minutes\*. Based on the prime number generator alone, it is \*entirely\* reasonable to conclude that the author knows almost nothing about writing good code. ======== import std.stdio, std.algorithm, std.range; // generates all primes in \[start,end) and returns all primes in \[0,end). // primes array must contain all primes < start uint\[\] grow\_sieve(uint\[\] primes, uint start, uint end) { . . assert(end >= start && start > 1); . . bool\[\] composite; . . composite.length = end - start; . . // mask multiples of existing primes over the expanded range . . foreach (p; primes) { . . . . // start at first multiple of p in \[start,end) . . . . for (uint j = p \* (((start - 1) / p) + 1); j < end; j += p) { . . . . . . composite\[j - start\] = 1; . . . . } . . } . . // locate primes inside the expanded range . . foreach (i; start..end) { . . . . if (composite\[i - start\]) continue; . . . . for (uint j = i \* 2; j < end; j += i) { . . . . . . composite\[j - start\] = 1; . . . . } . . } . . // concatenate all numbers in \[start, end) that aren't marked composite . . return primes ~ iota(start,end).filter!(a => !composite\[a - start\]).array; } // Generate first n primes by successive applications of the // Sieve of Eratosthenes uint\[\] generate\_primes(uint n) { . . const STEP\_SIZE = 10\_000\_000; . . uint\[\] primes = \[ \]; . . uint start = 2; . . for (uint end = STEP\_SIZE; primes.length < n; end += STEP\_SIZE) { . . . . primes = grow\_sieve(primes, start, end); . . . . start = end; . . } . . return primes\[0..n\]; } ========== (n.b. I started to translate this into Java for easier comparison with the original, but then I remembered that no one had a gun to my head, so I stopped.)

#### [2020-10-18 09:21:53](#komment5f8bfb213199f) by dmyp:

If you ask me, I'd say that you understand the book too literally. For example, when you write about side effects and short methods with zero arguments, I would say that side effects is not about changing the private fields but about doing something that is not related to what's stated in the name of the method. Say, includeSetupPages() must not touch anything that has impact on how includePageContent() works (the example is of course artificial, but I hope the idea is clear). If you ask me about the book in general, I would definitely recommend it to newbies, but I would warn them that the book is aimed only to give you a \*feeling\* of how clean code should look like, it's not a set of strict rules that must be followed. E.g., I hope everyone would agree that 2 to 4 lines of code per method is almost impossible to achieve in modern projects, and may even be harmful from performance perspective (say, in C++ function calls are not free). In my opinion, reading this book when you are a beginner in programming will plant a seed in your head and give you a basic feeling of what should feel wrong. For experienced developers, however, most likely there is nothing new there.

#### [2021-01-21 21:31:19](#komment6009f2a78a6a5) by Veysel Ozdemir:

Thank you for writing this post. I recommended a chapter from this book to a friend today and just wanted to skim through the chapters again, and just within 1 hour I felt so uneasy and found myself googling "critisism of clean code" (of course google corrected my spelling to "criticism" :) In retrospect, as I read through the chapters, I now realise how the language of the book the language of a "know it all" or a "brilliant jerk". How a disagreeable mind it is the writer, sure of himself talking from the ethical high ground but unable to demonstrate his ability to apply them, let alone applicability of that high ground by at least demonstrating examples from others applying them. Those who talking about political views of Martin etc, I am not in the US and I don't care a bit about the politics there. But I care when some holy evangelist warrior endlessly argues on a piece of code in the name of "clean principles" to make it a less and less readable, understandable, deeply nested layered maze. Kudos to Carlos Saltos, in the comments, for recommending The Wet Codebase. Heard it here for the first time, really liked it. Such a great talk. I want to repeat the link: https://www.deconstructconf.com/2019/dan-abramov-the-wet-codebase

#### [2021-02-06 08:22:27](#komment601e51c38e2ec) by Jacob Nordfalk:

I really HATE clean architecture!... A simple rename of a field in a recent project involved changing 32 (thirty-two!!) files, all over the place. CLEAN makes people forget a much more important principle, namely KISS, and tempts some developers solve simple things in the most complicated manner, adding unit test and integration tests all over the place for their complicated converters and no-op code, and makes further development crawl to a halt.... CLEAN+Coroutines+Flow+whatever-is-cool-at-the-moment+heavy use of Dagger DI and 2-3 more annotation based frameworks... costs weeks for new developers to understand the code. I am currently taking over a one-man project on a codebase with 1200 classes where 300 classes would have sufficed, as its really just a wrapper on a REST interface with no offline logic. It is sooo CLEAN, with so many layers and modules and packages that the code is a mess for newcomers - debugging the simplest thing involves switching threads and package at least a dozen times, which the coroutines helps to obfuscate the call stack completely. The app regularly crashes, at many places, but its hard to see why.... I am looking forward to the day CLEAN is declared dead for 1-2 man projects like e.g. apps, and we can get back to KISS and getting things done

#### [2021-07-02 16:11:30](#komment60df2ca2c21d2) by Paul:

I would have to agree with this post re the code examples (as given here: I haven't read 'Clean Code'). However... I do have to wonder if some of the people dissing 'Clean Architecture' haven't really understood much of it. I found it to be probably the most insightful book on creating clean and maintainable systems I've read - and I've read quite a few. Most other books are heavy on the management aspects, or pushing a particular metholology (usually the authors, unsurprisingly), or bound up with a particular technology (and that's just \*wrong\*). In contrast, in 'Clean Architecture' Martin makes the - perhaps surprising, to some, but entirely reasonable - observation that tools, frameworks, ORMs, and the like - have \*nothing\* to do with architecture. (This in itself was good to read. I don't remember any other text making this point quite so forcefully.) 'Clean Architecture' actually expounds some quite fundamental, if often misunderstood, or half understood, ideas. In particular around dependencies, DIP and where to place boundaries in a system (and what, exactly, is meant by 'a boundary'). It also provides some fairly unique (in my experience) insights. To give just one example from the first part of the book: there's a rather well thought-out summary of the three main paradigms: structured, OO and functional. It also provides good reason to believe that these may be the \*only\* three paradigms that will exist (because each, although we don't usually think if it this way, actually takes something \*away\* from the programmer). There's much in this book about how to apply SRP, LSP, OCP and the like. But there's also a refrain that runs though the text: protect your 'business logic' (which is to say, your USP - the reason you are building something in the first place) from extraneous details. To which it can be added, as the book shows, that there's a lot more that falls under 'extraneous' than is often accounted for. There's also no attempt in 'Clean Architecture' follow any of the latest trends, management fads, or the like. Rather it tries to get at what is fundamental about good software architecture, across development platforms, application domains, or - for that matter - the last 50 or so years. It doesn't reject what has been learnt for the latest shiny tool, but rather engages, throughout, with what can be learnt from the history of our field. In general, I found that nearly all parts of the book left me with new ways of looking at old problems, and something new to think about. That said, this is not an easy book to read: it takes some time and reflection to map these ideas into your own work and past-experience. It's the sort of book that rewards a second reading. It isn't, and I don't think it was meant to be, an Architecture 101. (Aside, and on a practical note, it lead me to re-architect an existing system I had started on - with much better results.)

#### [2021-07-25 06:14:02](#komment60fcf31ae2da5) by jCalculette:

I would say that even today Clean Code is worth reading. As are the 2nd editions of Fowler's Refactoring and The Pragmatic Programmer. Now while the later is mostly a philosophical book about software engineering then others are essentially full blown textbooks. For example, Fowler's book has first 100 pages dedicated to the overall idea of refactoring (how, why, what) and the next 300 pages serve essentially as a reference guide. Not to mention that Fowler' himself mentions that while he has mostly only included one mechanism to achieve the refactoring, it is not the one and only one. With the Clean Code we first have to take account that it is somewhat of an "older book" and software engineering has advanced a lot since then. However, it does give the general ideas that one should strive for and as always, one should make up ones own damn mind about the recommendations that the book gives. An easy example, Uncle Bob recommends using wildcard imports, I do not for various reasons. And as we read opinions on the Net we can come upon those who do agree with it, and those that don't (Google's official Java guide for example). In addition, if SonarQube analyzes your project and starts saying, that one should fix this and that - do you blindly follow suit or take it with a grain of salt and make your own opinion about it? So overall... I think one should read Clean Code but one should read Refactoring and Pragmatic Programmer and Clean Architecture and so on. As the authors of The Pragmatic Programmer suggest that if possible, you should read at least one technical book per month while not forgetting about the non-technical books. In the end, they all expand your understanding and it is left as an excercise to the reader to weed out the do's and don't's from each of them.

#### [2021-09-15 22:59:15](#komment61426cb35a782) by Ray:

In response to Michael's, "But 45 seconds is also a bit too slow": That was due to a mix of running on an old machine, missing a couple of obvious optimizations (starting the masking at each iteration at k\*k instead of k+2, stopping grow\_sieve early once we have enough primes), both of which your version has, and printing \*all\* the generated primes, not just the last 10. With the optimizations, and all run on the same cheap laptop, C takes 25 seconds, D 26, Rust 34 (your code, but printing all 20M primes), and Java 164 (with the sane algorithm, not the Clean Code one).

#### [2021-12-24 06:32:25](#komment61c56979b047e) by Ryan:

The comment section here is honestly atrocious. It feels weird after reading this book and having to stop and ask myself the intentions of the writer in certain areas to truly understand what he wanted to teach me. <br/> I bought this book a while ago after doing some research on books that could enhance my knowledge and skills. I didn't really read too much at the time, as I fell headlong into a new position, but I just broke it out again to read through the unit testing portion to refresh for an interview. Chapter 9 is only 12 pages but I feel like I've been cheated of about 8 pages worth of useful material. <br/> I don't want to harp too much on what you have written here already, but I want to add something after I've gone over my notes. For a chapter in the book "Clean Code", the framework for the chapter is non-existent. The chapter feels less like an instruction and more of a stream of consciousness, where random bits of knowledge fling at me in no particular order. <br/> The chapter starts with an anecdote, introduces The Three Laws of Test Driven Development, goes to another anecdote about him consulting a development team that honestly doesn't feel like a real experience which could have been cut to get to the one sentence point, which has nothing to do with the Three Laws, as the issue at hand were poor tests(he doesn't outline what made the tests poor, or "dirty" as he puts it) and it keeps spiraling. <br/> There are little tiny grains of knowledge in paragraphs. "If you fail to maintain good tests, you'll accumulate code debt", "Good tests allows for code to change easily", "Tests should be easy to read and understand". And then you get hit with the "BUILD-OPERATE-CHECK" pattern, bringing in test data out of the blue, but never in any detail or with a good example. <br/> The main issue here is this is not instructive. Ignoring cleanliness, most of this advice is general to the point where its almost too general for unit testing in and of itself, except for the 3 testing structures he adds at random. If I had never touched JUnit before, I would be absolutely lost. Unit Testing isn't the sexiest thing in the world, but his pen jumps as if the concept itself is more important than what goes in production. And he never even establishes what a unit test \*is\* or should BE. Also he brings in a code example in this chapter, 9-8, to show how one would unit test a concept at a time, instead of just individual single tests as their own unconnected code, and then doesn't refactor the example to show how it \*should\* be done.

#### [2022-01-28 14:32:04](#komment61f3fe64530e9) by alban:

I have been into clean code architecture since 4 years now. The principles, of this book / videos are very good compared to the caos of the industry where you do not have any architecture. Since ever I applied clean code, I have notice that my projects are scalable, extendable, durable, easy to pick over again... it totally changed the quality of the projects. I picked up a project I started 2 years ago with no issue, extending it. Now said that, is this the best architecture? of course no. do we have a better one? Nope Software developers today are like monkey coders, they write any type of code just to make things work, but never think in term of architecture: what happen if I have to add a new feature? would it be easy? how is going my unit test change?.... and what is worst is that this kind of developers tend to argue with air with no data and no base I work for the biggest cloud company, and the main issue I see here is creating of tech debt, done by bad coding/no architecture... we spend most of our dev time in figuring out and re-factoring continuously our code even for simple changes like adding a new column to a table....

#### [2022-06-28 13:35:32](#komment62baf5941a528) by Sinity:

I always thought that advice to aggressively break functions down into ridiculously small ones is weird and doesn't actually simplify the code. There's a nice text by Carmack: number-none.com/blow/blog/programming/2014/09/26/carmack-on-inlined-code.html - which recommends not artificially breaking functions into smaller ones if these would be only called once "If everything is just run out in a 2000 line function, it is obvious which part happens first, and you can be quite sure that the later section will get executed before the frame is rendered." "The function that is least likely to cause a problem is one that doesn’t exist, which is the benefit of inlining it. If a function is only called in a single place, the decision is fairly simple." "Using large comment blocks inside the major function to delimit the minor functions is a good idea for quick scanning, and often enclosing it in a bare braced section to scope the local variables and allow editor collapsing of the section is useful. I know there are some rules of thumb about not making functions larger than a page or two, but I specifically disagree with that now – if a lot of operations are supposed to happen in a sequential fashion, their code should follow sequentially." "If a function is only called from a single place, consider inlining it. "If a function is called from multiple places, see if it is possible to arrange for the work to be done in a single place, perhaps with flags, and inline that." "If there are multiple versions of a function, consider making a single function with more, possibly defaulted, parameters." "Minimize control flow complexity and “area under ifs”, favoring consistent execution paths and times over “optimally” avoiding unnecessary work."
