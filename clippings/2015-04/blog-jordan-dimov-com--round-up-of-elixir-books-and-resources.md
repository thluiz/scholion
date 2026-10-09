---
url: "http://blog.jordan-dimov.com/round-up-of-elixir-books-and-resources/"
captured_at: "2015-04-10T11:05:56-03:00"
title: "Round-up of Elixir Books and Resources"
domain: "blog-jordan-dimov-com"
---

# Round-up of Elixir Books and Resources

19 March 2015

If you are ready to dive into Elixir, or have already taken the plunge and want to increase your knowledge, here is a list of books and resources that I have compiled for you. My collection is, of course, subjective - I have picked only those books and resources which have been useful to me, and I have tried to present them here in a somewhat logical order. Hopefully, they will also be useful to you on your quest to becoming an expert Elixir programmer. You can thank me by sharing this post with anyone new to Elixir.

## Introductory Elixir Books

- Dave Thomas, [Programming Elixir: Functional |> Concurrent |> Pragmatic |> Fun](https://pragprog.com/book/elixir/programming-elixir) (November, 2014) - This is, in my opinion, the best available published book for learing Elixir. It can be a bit fast-paced at times, as it assumes you already have some programming experience in other languages. However, the main reason I like and recommend the book is that it doesn't just cover the basics - it also does a great job of introducing you to various aspects of the philosophy of Elixir (and functional programming in general), which really does help in making the best of your subsequent studies and practice. Make sure you do the exercises - they are great, although, in my opinion, there's not enough of them.
- Simon St. Laurent, J. David Eisenberg, [Introducing Elixir: Getting Started in Functional Programming](http://shop.oreilly.com/product/0636920030584.do) (September, 2014) - I found this book to be somewhat lighter reading than the one by Dave Thomas. What worked best for me is reading these two in parallel, as they cover pretty much the same ground. This one also makes for a pretty good reference.
- Paulo A Pereira, [Elixir Cookbook](https://www.packtpub.com/application-development/elixir-cookbook) (February, 2015) - I feel the title of this book is a bit misleading. Usually, when I pick up a programming "cookbook", I expect to read in it about ways to do things which are commonly needed, but not well documented elsewhere. Instead, this book takes the approach of summarizing the standard introductory Elixir topics in the format of "recipes". Which actually makes it a great introductory book, to supplement your reading of the above two. I did learn a few new concepts and tricks that I didn't get from the other books and it generally helped cement my knowledge of the "foundations".
- J. David Eisenberg, [Études for Elixir](http://chimera.labs.oreilly.com/books/1234000001642) - This is a great resource, available [on-line free of charge](http://chimera.labs.oreilly.com/books/1234000001642/index.html). All the other books I've mentioned suffer from not enough exercises. This one is the opposite - it ONLY contains exercises, which is exactly what I needed. Use it!

## Books on Intermediate and Advanced Elixir Topics

- Saša Jurić, [Elixir in Action](http://www.manning.com/juric/) (expected in May, 2015) - Once you have the foundations, there is no substitute for actually building your own projects in Elixir. This book will give you just what you need and the author does demonstrate exceptionally deep understanding of the language. While the books is not yet published at the time of writing this post, you can pre-order it from the publisher's website and get access to almost all of the content right away.
- Chris McCord, [Metaprogramming Elixir: Write Less Code, Get More Done (and Have Fun!)](https://pragprog.com/book/cmelixir/metaprogramming-elixir) (February, 2015) - This book, by the creator of the [Phoenix web framework](http://phoenixframework.org/) guides you on a delightful tour of one of the most powerful features of Elixir - the ability to write code, which writes code (aka. metaprogramming). Once you have a good grasp of this topic, I think you will deserve your "Elixir master" badge.

## Books on Erlang and OTP

Elixir is built on top of Erlang and the Open Telecom Platform (OTP), so if you want to be great with Elixir, you have to also be great with these gems. Here are some good books:

- Joe Armstrong, [Programming Erlang: Software for a Concurrent World](https://pragprog.com/book/jaerlang2/programming-erlang) (2nd edition, October 2013) - THE book on Erlang, from the original author of the language.
- Martin Logan, Eric Merritt, Richard Carlsson - [Erlang and OTP in Action](http://www.manning.com/logan/) (December, 2010) - This book will help you master the concepts of OTP. A solid familiarity with OTP is crucial to achieving a deep understanding the practical aspects of Erlang and Elixir programming.
- Fred Hebert, [Learn You Some Erlang for Great Good!: A Beginner's Guide](http://learnyousomeerlang.com/) (January, 2013) - an alternative good introduction to Erlang.

## Recommended Non-Elixir books

The books below are not directly about Elixir or even Erlang, but they will help you a lot. They cover in-depth the foundations of functional programming, recursion, and good software design. Most of them use dialects of Lisp to get the point across.

- Harold Abelson, [Structure and Interpretation of Computer Programs](https://mitpress.mit.edu/sicp/full-text/book/book.html) (2nd edition, August 1996) - **Read this book**, it will make you a better programmer, no matter what language you use. Be prepared, though - this is NOT an easy read and working through it will take time, so treat it like a project. The language used in the book is Scheme.
- **UPDATE (06 April 2015)** Thomas VanDrunen, [Discrete Mathematics and Functional Programming](http://cs.wheaton.edu/~tvandrun/dmfp/) (March, 2013) - I thoroughly enjoyed this book as a refresher on discrete math and introduction to many advanced topics. The book uses Standard ML as the functional programming language to complement the mathematical exposition, but it is great for Elixir programmers as well.
- Daniel P Friedman, [The Little Schemer](http://mitpress.mit.edu/books/little-schemer) (4th edition, February 1996) - "[This book is] mind expanding if you haven't read a lot about lisp / recursion / functional programming" ([Drew Olson](http://blog.drewolson.org/))
- Paul Chiusano and Rúnar Bjarnason, [Functional Programming in Scala](http://manning.com/bjarnason/) (August, 2014)
- Michael Fogus, [The Joy of Clojure](http://www.joyofclojure.com/) (June, 2014)
- Joe Armstrong's PhD theses: [Making reliable distributed systems in the presence of software errors](http://www.erlang.org/download/armstrong_thesis_2003.pdf)

## Other useful resources for Elixir

- [Elixir Radar](http://plataformatec.com.br/elixir-radar) - the official Elixir newsletter from Platformatec. Delivered weekly by e-mail, with high quality curated content. Subscribe on the website.
- [Functional Elixir newsletter](http://newsletter.elixir-devs.com/) - a weekly, auto-generated Paper.li newsletter, set up by [Yours Truly](http://twitter.com/jdimov). Contains summaries and links to popular Elixir resources and discussions over the week. View on-line or subscribe by e-mail.
- [Exercism.io](http://exercism.io/) - this is the most awesome thing ever. Just follow the instructions and do the Elixir exercises, you will learn SO much!
- [Elixir projects on GitHub](https://github.com/search?q=elixir) - about 2500 projects at the time of writing (March 2015)
- [Elixir Q&A on StackOverflow](http://stackoverflow.com/questions/tagged/elixir)
- [Elixir on reddit](http://www.reddit.com/r/elixir)
- [The Elixir Community on Google+](https://plus.google.com/u/0/communities/115770991058707869622)
- [The Elixir Group on LinkedIn](https://www.linkedin.com/groups?home=&gid=6530248)

Of course, the best way to get started is to ignore all of the above and just get your hands dirty. Here's how to [install Elixir](http://elixir-lang.org/install.html) on your platform.

Finally, if you are itching to learn from the best, make your way to [Elixir Conf 2015](http://www.elixirconf.eu/) in Kraków, Poland (22 - 24 April, 2015).

**P.S.** Obviously, there is a lot more on the Internet than the resources I have chosen to present in this post. If you are the author of, or know about a great resource which I have missed, let me know. If you have a blog related to Elixir, consider adding it to the [Planet Elixir](http://planet.elixircentral.com/) aggregator, administered by [Jonathan Harrington](http://blog.jonharrington.org/).

**P.S.S.** I didn't even mention one of *the best* resources for learning Elixir - the official [Getting Started with Elixir](http://elixir-lang.org/getting-started/introduction.html) tutorial.
