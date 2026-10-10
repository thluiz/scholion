---
url: "http://pressupinc.com/blog/2014/09/mistakes-made-first-ember-project/?utm_source=javascriptweekly&utm_medium=email"
captured_at: "2014-09-26T18:19:46-03:00"
title: "Mistakes I Made in My First Ember Project - Press Up"
domain: "pressupinc-com"
---

# Mistakes I Made in My First Ember Project

![6bc2f0dc7816c31a1a05db54af71fdd6.png](pressupinc-com--mistakes-i-made-in-my-first-ember-project/6bc2f0dc7816c31a1a05db54af71fdd6.png)

I recently was presented with a completely [greenfield project](http://en.wikipedia.org/wiki/Greenfield_project). We were making a not-uncommon CRUD (create-read-update-delete) app for a business that was looking to move beyond the constraints of their Microsoft Excel-based data-tracking system. We also had a limited but important numbers of use cases where data from all over (what was Excel sheets) would need to be coordinated through the system to accomplish some currently-impossible business goals.

Because the project was pretty simple CRUD, and I’d been curious to make a single-page Javascript application for a while, I decided I’d dive into the project using the Ember framework. I’d been curious about it, for a while but had never used. And I saw a few places that it would be necessary to have a rich Javascript-driven experience, and saw ways that some of Ember’s best traits would shine there. So I dove in.

And what I had was a bit of a long and painful learning process because of some limitations of Ember, my understanding of it, and how those things worked together. I hope my exploration of that experience can help old-hats at Ember get more clarity about where beginners struggle, Ember newbies learn a thing or two, and people totally inexperienced with Ember get a better sense of the framework’s strengths and weaknesses.

## I Dove into Ember Too Deep Too Fast

> Because I didn’t *need* to take the time to learn up front about some of the more core features, values, and conventions of Ember, I experienced a lot of painful times metaphorically bashing my head against simple problems that were just one layer deeper than what I was currently understanding of the auto-wiring.

One of the great things about more “magic” or “it just works” or “convention over configuration” frameworks like Ember is that you can get a lot done in very little code. One of the worst things about them is that you can also quickly lose track of what’s going on and become quite unsure about where you should put this new thing you’re trying to do that’s not quite exactly in line with the plumbing of the magic. A quick example: because Ember will auto-create your View layer, when you finally realize you need to change one where you never made one before, you suddenly have to learn a number of things — where to put them, what they can do, what they shouldn’t do, etc. The topic of “magic” in programming frameworks is clearly too big in scope for this piece, but it was one of primary struggles as I started to roll on the Ember parts of this project.

Because I didn’t *need* to take the time to learn up front about some of the more core features, values, and conventions of Ember, I experienced a lot of painful times metaphorically bashing my head against simple problems that were just one layer deeper than what I was currently understanding of the auto-wiring. That next level down I needed to reach wasn’t just a few different keystrokes from where I was, but required me to master a whole other way of thinking about what was going on. There were painful learnings involved.

### I Didn’t Take Advantage of All the Ember Conventions, like `.get()` and `.set()`

One of the core things that differentiates Ember from most other Javascript frameworks is that you’re never really supposed to access or change a property in the traditional Javascript ways. For the unfamiliar, calls like:

```
thisvalue  
 thisvalue   
// do thing
```

Should actually be done in Ember-land with:

```
this'value' 
 this'value'   
// do thing
```

There’s a lot of under-the-surface benefit to this wrapping of a core Javascript behavior. For one it makes [computed properties](http://emberjs.com/guides/object-model/computed-properties/), one my core reasons for picking Ember for this application, work seamlessly like more pedestrian properties on your objects. And I do really enjoy that I can access computed properties exactly like any other throughout Ember.

But it took more than a few cycles of confusion and insisting on fighting the Ember object model before I realized the power of this “universal access”-enabling feature. What this comes down to is that because Ember is an avowedly convention-over-configuration structure, you’ve got to both take the time upfront to learn about the conventions, and to take the time to really understand what they mean and imply before you go off and start coding. The Ember documentation is reasonably good and explaining all this stuff, but I didn’t read it deeply-enough upfront. And then when I had a problem, the upfront parts I’d skipped over were just more stuff I didn’t get.

If the Ember docs were to be improved to save people these kind of headaches, I think they could benefit from more clearly defining the difference between Ember and what an average Javascript programmer would expect, and regularly refer to those definitions when concepts that build up from them are discussed.

## I Didn’t Fully Understand the Power and Possibility of Ember Data

[![3e38f8e226f1f264e452872c114f439d.jpg](pressupinc-com--mistakes-i-made-in-my-first-ember-project/3e38f8e226f1f264e452872c114f439d.jpg)](http://pressupinc.com/wp-content/uploads/2014/09/star-trek-figurine-data.jpg)

I used Ember Data on this project. On the whole, I’m very glad I did. Its ability to wrap and abstract away the server-side API from my Javascript made everything simpler. I rarely had to think about it at all, and that was a huge boon to my ability to focus on interface elements and user flows rather than sweating modestly different problems around data-storage and persistence.

The issue I had was this: I was using a server-side framework that could easily serve up JSON responses, but I didn’t know what the default Ember Data serialization format was, nor how I would make that make my server output it. But I knew that my database column names matched that of Rails, and in my eagerness to get started decided that I’d use the ActiveModel serializer and munge the data in my server-side app. And it did (and still does) work this way. But it’s far from optimal, because much of default serialization of my server doesn’t look all the much like an ActiveModel serialization.

What I have, then, is a set of unnecessarily brittle data handlers on both ends masquerading as something neither of them is, because that was how I thought, in my early ignorance, it would work best. In reality, that I haven’t (and may never) refactor the app’s Ember Data serializer into one that uses the default server formatting so I can drop all the pretense of using the ActiveModel format is an indictment of my handling of the project as much as it is of Ember, Ember Data, or any part of the models involved. But clearly I wish I’d known sooner and understood more deeply how simple and much more effective it would have been to modify the Ember Data serializer to match my server’s default rendering.

## I Fought Against “the Ember Way” Because I didn’t Understand It

[![54240f4097a59c20c384807ff5012302.jpg](pressupinc-com--mistakes-i-made-in-my-first-ember-project/54240f4097a59c20c384807ff5012302.jpg)](http://pressupinc.com/wp-content/uploads/2014/09/tomster.jpg)

If you’ve not noticed yet, the core mistake I made in my Ember project was starting before I really understood all the Ember-y-ness of Ember and what the implications of that were. I think this is a recurring theme because you really can and should think of Ember as more than a set of libraries that let you do specific things, but as a holistic vision of how you should and can program you project. Where (something like) Backbone is a set of tools, Ember is a full and powerful philosophy of work that you need to bite off completely and chew thoroughly before you reach flow with it. If you don’t, you’re likely to bang your head against it, as I did.

I had a few other notable struggles because of places where I opted out of the Ember way, which are worth highlighting quickly:

- **Browser, jQuery, and Ember DOM state conflicts** — I was using [Ember Table,](http://addepar.github.io/ember-table/) a pretty rich little library to display large data tables from Ember with reasonable performance. But when I mixed jQuery and non-Ember state into those tables, weird and troubling things happened. Checkboxes were randomly checked that shouldn’t have been, only some of the actually selected checkboxes were captured by my script, etc. Basically, because Ember and Ember Table were drawing the DOM, jQuery would get lost and weird states would manifest. The solution: leaving Ember in charge of ALL the state. No more weirdness.
- **Using Javascript native methods like `.push()` instead of Ember’s `.pushObject()`** — It works, basically, but not quite. As I’ve mentioned computed properties are awesome, but in order for Ember to re-compute for you, you have to submit to Ember-specific methods. I had, in the course of the project, more than a few issues where I wrote a native-Javascript function that didn’t behave as I wanted because the interactions with Ember weren’t as expected. After some experience with this, I learned to spot the symptoms and make the necessary changes, but it was a painful and regular mistake.

There are probably a few other notable snags and mistakes made over the course of the project, but I don’t recall them all. On reflection, I’m very glad I tried Ember out. I think it’s a powerful system, and as good a place I could hope to start from for building rich “multi-page” single-page Javascript applications. But if I could do it all again, I’d spend more time learning the hows and whys of all the Ember conventions before I started. Without really understanding them deeply, you can quickly and accidentally find yourself in a marathon debugging session with a problem you don’t quite understand. But take Ember on with that understanding, and I recommend it highly.

*Image Credits: [jdhancock](http://www.flickr.com/photos/jdhancock/8031897271/)*
