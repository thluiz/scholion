---
url: "http://blog.rodneyrehm.de/archives/14-Sorting-Were-Doing-It-Wrong.html"
captured_at: "2012-05-30T10:56:55-03:00"
title: "Sorting - We're Doing It Wrong | Rodney Rehm"
domain: "blog-rodneyrehm-de"
---

# We're Doing It Wrong

---

I usually write about `Array.sort` rather than `Array#sort`. Simply because I never know when to use which. But no worries, [@mathias](https://twitter.com/mathias)  is here to set us straight! ☺

---

## Sorting - the basics

[Array#sort()](https://developer.mozilla.org/en/JavaScript/Reference/Global_Objects/Array/sort)  is a handy little function that sorts arrays for us. It's handy, because we don't have to implement one of the various sorting algorithms like BubbleSort, MergeSort or HeapSort. *(If you studied computer science, you've probably implemented a couple of these yourself. Quite annoying, right?)* ECMAScript, the specification behind Javascript, doesn't regulate which algorithm a Javascript engine vendor should use. According to this [question on StackOverflow](http://stackoverflow.com/questions/234683/javascript-array-sort-implementation)  apparently Mozilla implemented [MergeSort](http://en.wikipedia.org/wiki/MergeSort) , Safari did some [SelectionSort](http://en.wikipedia.org/wiki/Selection_sort)  and Chrome's V8 uses [QuickSort](http://en.wikipedia.org/wiki/QuickSort) .

---

For kicks and laughs, here's what sorting algorithms sound like:

---

So the actual sorting is done for you, as long as you pass in a callback function that compares two elements according to how you want them sorted. Said function must accept two arguments (`a, b`) and is supposed to return an integer. `0` if `a === b`, `-1` if `a < b` and `1` if `a > b`. Since `a` is already positioned before `b`, returning `0` and `-1` yield the same result, which usually allows to remove the extra equality comparison and end up with `a > b ? 1 : -1`.

### Stable vs. Unstable Sorting

While ECMascript doesn't dictate the algorithm to be used for sorting, it very well says it should be a stable one. [Stable sorting algorithms](http://en.wikipedia.org/wiki/Category:Stable_sorts)  maintain the relative order of elements that appear to be "the same". To `Array#sort` two items appear the same when the comparison function returns `0`. While InsertionSort and BubbleSort (Apple and Mozilla) are stable, QuickSort (Google Chrome) is **not**.

[@millermedeiros](https://twitter.com/millermedeiros)  wrote a little [test-case](http://jsbin.com/eqanux/edit#javascript,live) to point that out. *(Thanks!)*

So Safari and Firefox will sort `["sed", "dolor", "ipsum", "foo", "bar", "cat", "sit", "man", "lorem", "amet", "maecennas"]` (by character length) in a way that `"sed"` will retain first position, while Chrome will roll the dice and possibly prefer `"cat"` to take the pole position. *The Chrome developers obviously like Kittens…*

[@millermedeiros](https://twitter.com/millermedeiros)  suggests implementing a stable algorithm, such as [MergeSort](http://en.wikipedia.org/wiki/MergeSort)  yourself, if you find yourself in need. Or, if you're as lazy as me, you might be happy with [his implementation](http://millermedeiros.github.com/amd-utils/array.html#sort) he made available with [AMD-Utils](http://millermedeiros.github.com/amd-utils/) .

### Sorting Different Types

Let's see what happens when different types are sorted ([fiddle](http://jsfiddle.net/rodneyrehm/HXRNW/) ):

var list = [Infinity, -Infinity, NaN, 0, -0, 1, -1, {}, [3], [4,5], [6], "1", "-1", "a", NaN, "z"]  
  
// sort with internal default comparison function  
list.sort();  
  
// sort with custom comparison function  
list.sort(function(a, b) {  
  return a > b ? 1 : -1;  
});

The results are rather interesting:

=== internal default comparison (Firefox and Chrome) ===  
-1 | -1 | -Infinity | 0 | 0 | 1 | 1 | 3 | 4,5 | 6 | Infinity | NaN | NaN | [object Object] | a | z  
  
  
=== custom comparison (Firefox) ===  
-Infinity | -1 | -1 | 1 | 3 | Infinity | NaN | 0 | 0 | 1 | 4,5 | 6 | [object Object] | a | NaN | z  
=== custom comparison (Chrome) ===  
-Infinity | -1 | -1 | 0 | 0 | 1 | NaN | 1 | 3 | 4,5 | 6 | [object Object] | a | NaN | Infinity | z

- `a > b ? 1 : -1` is the most rudimentary comparison function, mentioned in pratically every single example illustrating the Array#sort() function. Yet it doesn't yield the same result as the internal default comparison function. Let's ignore the internal default comparison function for now, we're most likely not going to use it.
- See how `NaN` pretty much stayed in their original spots? Comparing something to `NaN` seems to be a bad Idea.
- Chrome and Firefox seem to apply different rules to casting strings and arrays to numeric values.
- Note how Firefox and Chrome treat `Infinity` differently (both don't make sense, imho).

Removing everything that is not immeditely numeric (including `NaN`) we get the following result (across browsers):

-Infinity | -1 | 0 | 0 | 1 | Infinity

Now, that finally makes sense.

In short: sorting different types seems like a bad idea because the results will vary across browsers. We must take measures to feed the comparison function reliable data. Beware of `NaN`! Replace them with an `Infinity` if you can.

### Sorting Strings

MDN suggests string comparison to be done like `"a" < "b"`. While this works for English just fine, it fails pretty much every other language there is. According to the rules, the German Umlauts (ä, ö, ü) should come right after their respective vowels: `a, ä, b, o, ö`. But here's where we're facing a problem, because `"ä" > "b"`. You see, the unicode of `b` is 0x62 and `ä` is 0xE4 and `0x62 < 0xE4`. See for yourself:

var list = "ä ba bb bä bz a e è é aa ae b ss sz sa st ß".split(" ");  
list.sort(function(a, b) {  
  return a > b ? 1 : -1;  
});

yields

a, aa, ae, b, ba, bb, bz, bä, e, sa, ss, st, sz, ß, ä, è, é

which is not quite what we (Germans, French, …) want.

Sadly MDN's [Array#sort()](https://developer.mozilla.org/en/JavaScript/Reference/Global_Objects/Array/sort)  doesn't mention the very handy function [String#localeCompare](https://developer.mozilla.org/en/JavaScript/Reference/Global_Objects/String/localeCompare) . *(I edited MDN to now link to that handy utility…)*

For comparing strings you can simply replace `a > b ? 1 : -1` by `a.localeCompare(b)` and your language is back in the game:

var list = "ä ba bb bä bz a e è é aa ae b ss sz sa st ß".split(" ");  
list.sort(function(a, b) {  
  return a.localeCompare(b);  
});

yields

a, ä, aa, ae, b, ba, bä, bb, bz, e, é, è, sa, ss, ß, st, sz

which is just fine!

`String#localeCompare` has been around since Javascript 1.2 - pretty much every browser out there knows it - So use it!

Let it be known that `localeCompare` uses the operating system's locale. Which means that if you're running an English (or Scandinavian) System, you won't be seeing the characters sorted according to German (or French, or whatever) rules.

> [@**rodneyrehm**](https://twitter.com/rodneyrehm "Rodney Rehm")  [@**mathias**](https://twitter.com/mathias "⚞ Mathias Bynens ⚟")  Worth noting that localeCompare is based on the user's OS locale and also that Scandinavians put äöü etc at the end :)

## Sorting DOMElements

A trivial function to sort the children of a DOMElement looks like:

$.fn.sortChildren = function(compare) {  
  var $children = this.children();  
  $children.sort(compare);  
  this.append($children);  
  return this;  
};

and would be invoked with

$('ul').sortChildren(function(a, b) {  
  return $(a).text().toLowerCase() > $(b).text().toLowerCase() ? 1 : -1;  
});

While this method works, it's wasting about 70% performance across the board.

## Boosting Performance - jQuery

jQuery itself is a wonderful thing. It makes things really simple. But losing a bit of performance is often the toll for said simplicity. Let's ditch `jQuery#append` and improve performance by 20% - 30%:

$.fn.sortChildren = function(compare) {  
  return this.each(function(){  
    var $children = $(this).children();  
    $children.sort(compare);  
    for (var i=0, l=$children.length; i < l ; i++) {  
      this.appendChild($children[i]);  
    }  
  });  
};

less jQuery, more performance…

## Comparing Elements

MDN (and most other resources I came across) illustrate sorting with an example like the following:

var list = ["Delta", "alpha", "CHARLIE", "bravo"];  
list.sort(function(a, b) {  
  return a.toLowerCase() > b.toLowerCase() ? 1 : -1;  
});

The docs usually fail to inform the reader of the fact that this comparison function is executed multiple times for each element in the array. *(I edited MDN to now reflect that fact)* Let's take a closer look at what's happening behind the scenes using the comparison function from before:

$('ul').sortChildren(function(a, b) {  
  var an = $(a).text().toLowerCase(),  
    bn = $(b).text().toLowerCase();  
  
console.log(an, bn);  
  return an > bn ? 1 : -1;  
});

A list of five elements:

<ul>  
  <li>delta</li>  
  <li>bravo</li>  
  <li>alpha</li>  
  <li>charlie</li>  
  <li>echo</li>  
</ul>

And Firefox gives us the following output:

delta bravo  
delta alpha  
bravo alpha  
charlie echo  
delta charlie  
alpha charlie  
bravo charlie  
delta charlie  
delta echo

You can easily see how `charlie` is evaluated 5 times. That means `$(a).text().toLowerCase()` is executed 5 times for charlie alone. The sorting algorithm used 9 iterations leading to 18 »get text of node and convert to lower case« operations. eighteen, instead of the 5 you'd actually need. Depending on what your comparison function actually does, this can be a tremendous overhead.

## Mapping Before Comparing

We cannot reduce the number of times our comparison function is executed. But we can reduce the work it actually does to a bare minimum. Instead of evaluating each element on every comparison, we do those evaluations once. For this we create a second array containing the values to sort

var list = ["Delta", "alpha", "CHARLIE", "bravo"],  
  map = [],  
  result = [];  
  
for (var i=0, length = list.length; i < length; i++) {  
  map.push({  
    index: i, // remember the index within the original array  
    value: list[i].toLowerCase() // evaluate the element  
  });  
}  
  
// sorting the map containing the reduced values  
map.sort(function(a, b) {  
  return a.value > b.value ? 1 : -1;  
});  
  
// copy values in right order  
for (var i=0, length = map.length; i < length; i++) {  
  result.push(list[map[i].index]);  
}  
  
// print sorted list  
print(result);

Using this technique, we can improve the performance of our little sorting plugin as much as 70% over the original.

Note: I don't know of any (reasonable) way to change to sorting of an array in-place. While `Array#sort` will modify the original array (as well as return itself), the mapped sorting approach described here will create a new array.

## Working On Detached DOM

Discussing the issue with [@derSchepp](https://twitter.com/derSchepp)  a couple of weeks ago, he threw in the Idea of detaching the nodes we want to sort from the DOM, so we could reduce the number of reflows (which happen when you alter the position of elements within the DOM) to a bare minimum of 2. A simple helper function (for lack of a better name) called `phase()` will help:

$.fn.phase = function() {  
  return this.each(function() {  
    var $this = $(this),  
      placeholder = $this.data('redetach');  
  
if (placeholder) {  
      placeholder.parentNode.replaceChild(this, placeholder);  
      $this.removeData('redetach');  
    } else {  
      placeholder = document.createTextNode(''),  
      this.parentNode.replaceChild(placeholder, this);  
      $this.data('redetach', placeholder);  
    }  
  });  
};

now we throw that into our little sorting function and get:

$.fn.sortChildren = function(map) {  
  return this.each(function() {  
    var $this = $(this).phase(),  
      $children = $this.children(),  
      \_map = [],  
      length = $children.length,  
      i;  
  
for (i = 0; i < length ; i++) {  
      \_map.push({  
        index: i,   
        value: map($children[i])  
      });  
    }  
  
\_map.sort(compare);  
  
for (i = 0; i < length ; i++) {  
      this.appendChild($children[\_map[i].index]);  
    }  
  
$this.phase();  
  });  
};

Note: the `.phase()` function here is just a quick hack without much thought put into it. [@cowboy](http://twitter.com/cowboy)  came up with a [better solution](https://gist.github.com/978520) !

## Benchmarking

You can't optimize what you can't quantify. Let's throw some tests at jsPerf and see how our optimizations panned out:

Surprise: the DOM-detaching thing only benefits Chrome. Firefox and Safari seem to do internal optimizations to prevent reflows on every single DOM mutation. Benefits in Chrome are far less than the losses in Firefox and Safari, so we'll just skip this step. Sorry Schepp :(

## Final Sorting Plugin

[In a Gist](https://gist.github.com/2818576) . Enjoy :)

## Sorting Numbers Within Strings

This [Fiddle](http://jsfiddle.net/rodneyrehm/5pLLG/)  has some ideas about how to "properly" sort numbers within strings.

### Update

- Modified mapped sorting examples according to [@cowboy](https://twitter.com/cowboy) 's suggestion
- Added a section about stable and unstable sorting algorithms
