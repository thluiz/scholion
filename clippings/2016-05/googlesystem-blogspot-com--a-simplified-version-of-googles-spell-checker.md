---
url: "http://googlesystem.blogspot.com/2007/04/simplified-version-of-googles-spell.html"
captured_at: "2016-05-13T14:55:25-03:00"
title: "A Simplified Version of Google's Spell Checker"
domain: "googlesystem-blogspot-com"
---

# A Simplified Version of Google's Spell Checker

Peter Norvig (from Google) [explains in a detailed article](http://www.norvig.com/spell-correct.html) how to write in 20 lines of [Python](http://www.python.org/) code a spell checker almost as good as the one used by Google to show the famous "[did you mean](http://www.google.com/search?q=did+yu+men&hl=en)" corrections. Well, at least for one-word corrections.
> We will read a text file, holmes.txt (that I happened to have on my laptop) which is a collection of Sherlock Holmes stories (from Project Gutenberg) consisting of about 100,000 words. We then extract the individual words from the file (using the function words, which converts everything to lowercase, so that "the" and "The" will be the same). Next we train a probability model, which is a fancy way of saying we count how many times each word occurs. (...)  
>   
> Now let's look at the problem of enumerating the possible corrections c of a given word w. It is common to talk of the edit distance between two words: the number of edits it would take to turn one into the other. An edit can be a deletion (remove one letter), a transposition (swap adjacent letters), an alteration (change one letter to another) or an insertion (add a letter). (...)  
>   
> The literature on spelling correction claims that 80 to 95% of spelling errors are an edit distance of 1 from the target.

A simple way to define the error model was to say that "all known words of edit distance 1 are infinitely more probable than known words of edit distance 2, and infinitely less probable than a known word of edit distance 0". From all the candidates for the correction, you can choose the most frequent word.  
  
In Peter Norvig's tests, this simple algorithm returned correct answers in more than 80% of the cases. Of course that Google has more data than the holmes.txt file (it crawls the web, right?) and has access to a huge list of queries and refinements that could improve the algorithm, but this is an example of a simple yet powerful program.
