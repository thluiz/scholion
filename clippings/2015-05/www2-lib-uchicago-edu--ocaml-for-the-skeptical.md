---
url: "http://www2.lib.uchicago.edu/keith/ocaml-class/home.html"
captured_at: "2015-05-31T13:51:30-03:00"
title: "OCaml for the Skeptical"
domain: "www2-lib-uchicago-edu"
---

## OCaml for the Skeptical

[Course Materials](http://www2.lib.uchicago.edu/keith/ocaml-class/class-01.html)

## Some History

### Which ML?

OCaml is a dialect of ML (for *Meta Language*), which started out as a language for
mathematical theorem proving in the [LCF project](http://en.wikipedia.org/wiki/LCF_theorem_prover) at the University
of Edinburgh[1](http://www2.lib.uchicago.edu/keith/ocaml-class/home.html#note1) and which is descended from Algol and Lisp
via P.J. Landin's never-implemented language ISWIM ("If you See What I Mean" -- which was
very influential due to several important journal articles in the late 1960's)[2](http://www2.lib.uchicago.edu/keith/ocaml-class/home.html#note2).

Development of ML proceeded at Edinburgh, Stanford and AT&T Bell Labs; at the [Institut National de Recherche en Informatique et en Automatique
(INRIA)](http://www.inria.fr/) in France as Caml (for *Categorical Abstract Machine Language*, after
the underlying compilation technique); and at Chalmers in Sweden (as Lazy ML). The
original line eventually became Standard ML, which has several notable implementations
([Standard ML of New Jersey](http://www.smlnj.org/), [MLton](http://www.mlton.org/) , [Moscow ML](http://www.dina.kvl.dk/~sestoft/mosml.html) [3](http://www2.lib.uchicago.edu/keith/ocaml-class/home.html#note3), etc). Lazy ML strongly influenced Haskell and is no longer actively developed. Caml development continues at INRIA.

A [Brief History of
Caml](http://www.pps.jussieu.fr/~cousinea/Caml/caml_history.html) by Guy Cousineau, the original developer, provides some insights.

### Which Caml?

There are three "Caml" languages (at least: the excellent Caml compilers are very popular
with researchers all over the world as a basis for experimental languages):

- *Caml*: the original French implementation; no longer developed.
- *Caml Light* (and later *Caml Special Light*): the precursors to OCaml; practically
  the same as OCaml except for the object system that gives OCaml its "O"; still
  available, quite stable and still supported I think (latest release was in 2002), but I
  don't know why you would choose it over OCaml.
- *Objective Caml* or *OCaml*: the latest and greatest version of the language,
  introduced the first strongly-typed object system with type inference.

In summary, make sure you install and use OCaml and don't bother with the earlier Camls!

Standard ML and OCaml have minor syntactic differences. If you know OCaml, you can
switch to ML very easily. The most important differences are in the libraries of the
languages and in two significant OCaml advances: the object system (Standard ML has
none) and the module system (very similar in basic use, though).

## Getting OCaml

OCaml is installed on merlot.lib and you can use it there. It's in the FreeBSD ports,
the NetBSD packages, and Linux rpms are available (Debian, Mandrake and RedHat
reportedly install OCaml). Binaries for Windows and Linux are available from INRIA and,
of course, OCaml is free software so you can always download and install from source; it
compiles and runs on most every version of Unix (MacOS X included). For more
information see [Installing OCaml](http://www2.lib.uchicago.edu/keith/ocaml-class/installing.html).

## Third Party Software

The best one-stop-shopping site for third party OCaml libraries is [The Caml Humps](http://caml.inria.fr/humps/index.html) (newbies should go
directly to the [Caml Light / OCaml
Hump](http://caml.inria.fr/humps/caml_latest.html)).

## OCaml Documentation

### Official Documentation

[OCaml User's Manual](http://caml.inria.fr/pub/docs/manual-ocaml/), incorporating:

- [an introduction](http://caml.inria.fr/pub/docs/manual-ocaml/manual003.html)
- [the language proper](http://caml.inria.fr/pub/docs/manual-ocaml/manual008.html)
- [the core library](http://caml.inria.fr/pub/docs/manual-ocaml/manual033.html)
- [the standard library](http://caml.inria.fr/pub/docs/manual-ocaml/manual034.html)
  (mostly data structures)

and much more.

### OCaml Books

Besides these books in English, there are eleven in French, and one each in German and
Italian.

- [**Developing
  Applications With Objective Caml**](http://caml.inria.fr/oreilly-book/), Emmanuel Chailloux,
  Pascal Manoury and Bruno Pagano, preliminary translation of
  the book  [*Développement d'applications avec Objective
  Caml*](http://caml.inria.fr/books-eng.html#ocaml-oreilly).

  > This book is very good and typically O'Reillian; I highly recommend it.
- [*The Functional Approach to Programming*](http://caml.inria.fr/books-eng.html#cousineau-mauny), Guy Cousineau and
  Michel Mauny, Cambridge University Press, Cambridge, 1998, ISBN
  0-521-57183-9 (hardcover), 0-521-57681-4 (paperback)

  > This book is a little more formal; most would probably consider it rather dry. Note
  > that it covers the earlier language Caml rather than OCaml and so has no coverage of
  > OCaml's object system nor the module system. But all the stuff about functional
  > programming and types and syntax is applicable to OCaml.
- [*The
  Little MLer*](http://mitpress.mit.edu/catalog/item/default.asp?ttype=2&tid=4787), Matthias Felleisen and Daniel P. Friedman, The MIT
  Press, Cambridge MA, 1997, ISBN 0-262-56114-X

  > Like the other *Little* books by the same authors (*Lisper*, *Schemer*,
  > *Java*), this is not a conventional introduction to ML. It's a programmed text
  > with a sense of humor that will either enlighten you or infuriate you. It assumes
  > no previous familiarity with ML but covers very advanced topics very quickly. It is
  > almost completely concerned with types. (N.B. while this is a book about Standard
  > ML, it works fine for OCaml and the authors provide a one-page cheat sheet that
  > explains how to translate the book's ML code into OCaml.)

Finally it should be mentioned that there are many books on Standard ML and all of these
are quite usable by OCaml programmers, once you've gone through any of the books above
(you *do* want to initially learn OCaml from an OCaml book, I think, but after that
you can branch out into the literature of Standard ML).

### OCaml Tutorials

I suggest doing these tutorials in this order, except for Kitt's, which,
being so terse, is good to look at simultaneously with all of these.

- [A Concise Introduction to Objective Caml](http://www.csc.villanova.edu/~dmatusze/resources/ocaml/ocaml.html) by David Matuszek.

  > A long single web page; worth reading.
- Jason Hickey's  [Introduction to Objective Caml](http://www.cs.caltech.edu/courses/cs134/cs134b/book.pdf) as used in his  [compiler design course at Caltech](http://www.cs.caltech.edu/courses/cs134/cs134b/).

  > 110-page well-hyperlinked PDF, very well done.
- [Learning OCaml, for C, C++, Perl and Java programmers](http://www.ocaml-tutorial.org/) by Richard
  W.M. Jones.

  > Substantial group of web pages; gets into some fairly advanced stuff
  > quickly; covers some stuff that most tutorials don't (keyword and
  > optional parameters, OCaml's Gtk bindings (Gtk is the popular,
  > modern GUI toolkit used by the Gimp and the Gnome project), garbage
  > collection, a great discussion of weak pointers, speed, etc); and
  > frequently explains what's going on internally in the compiler and
  > interpreter.
- [Kitt's OCaml
  Webpage](http://www.cs.ait.ac.th/~kitt/caml/). A nice 10-page introduction.

  > Kind of like a very long reference card.

### OCaml Mailing Lists and Newsgroups

The official  [OCaml mailing list](http://www2.lib.uchicago.edu/keith/ocaml-class/home.htmlmailto:%63%61%6d%6c%2d%6c%69%73%74%2d%72%65%71%75%65%73%74%40%69%6e%72%69%61%2e%66%72) ([archives](http://caml.inria.fr/pub/ml-archives/caml-list/))
can also be [read with your favorite news reader](http://www2.lib.uchicago.edu/keith/ocaml-class/home.htmlnews:news.gmane.org) (which
I highly recommend) thanks to [the amazing gmane](http://www.gmane.org/) or
directly [via
your browser](http://news.gmane.org/gmane.comp.lang.caml.inria/).

There's also a list [specifically
for beginners](http://groups.yahoo.com/group/ocaml_beginners/) (also available [via gmane](http://news.gmane.org/gmane.comp.lang.ocaml.beginners/)).

OCaml is also discussed on Usenet in [comp.lang.ml](http://www2.lib.uchicago.edu/keith/ocaml-class/home.htmlnews:comp.lang.ml) (which
also covers Standard ML) and [comp.lang.functional](http://www2.lib.uchicago.edu/keith/ocaml-class/home.htmlnews:comp.lang.functional)
(which covers all functional languages).

## Footnotes

1. Michael J. C. Gordon; Robin Milner; Christopher
   P. Wadsworth. *Edinburgh LCF: A Mechanized Logic for Computation.*
   New York: Springer Verlag, 1979.
2. P. J. Landin. "The Next 700 Programming Languages" in
   *Communications of the ACM*. 9:3. March 1966. Pages 157-66.
3. Moscow ML is actually implemented using the Caml Light compiler!

This page was last updated on 17 June 2006.
