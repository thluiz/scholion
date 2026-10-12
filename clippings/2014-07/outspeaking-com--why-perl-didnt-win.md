---
url: "http://outspeaking.com/words-of-technology/why-perl-didnt-win.html"
captured_at: "2014-07-07T14:18:22-03:00"
title: "Why Perl Didn't Win | Outspeaking"
domain: "outspeaking-com"
---

# Why Perl Didn't Win

The early days of the (public) Internet felt like living in the science
fiction world of a Bruce Sterling or William Gibson, whether finally being able
to download a web browser with image support (Slipknot?) or realizing that you
were logged into a machine in Australia from the middle of farm country USA and
it was responding to your FTP commands.

To everyone who'd learned how to type on an old PS/1 computer running
WordPerfect for DOS—with the little plastic keyboard overlay giving you
formatting hints—and for whom Alt-F3 "Reveal Codes" made word processing
make sense, HTML was the easiest thing in the world to learn (even if the best
your design sensibilities could do was center things with tables).

Your author remembers the first time he came across a web page which
*changed* when you reloaded it. Some university student had set up the
official homepage for a band and every new page view displayed a different
snippet of lyrics. These web pages weren't simple documents. They were
*programs*. This was science fiction. This was living in the future.

Then came forms and server side processing and your author left college and
learned Java and scrounged together spare parts at work to build his own Linux
machine and learned that the Internet wasn't magic science fiction. It was all
programs and protocols, and the greatest magic protocol of them all at that
time was HTTP, especially when combined with the new HTML extensions for form
submissions and the Common Gateway Interface that let a web server launch
programs to process form parameters and produce a fresh batch of HTML.

CGI programs could be anything. You could write them in a shell script on an
HP-UX or Irix box. You could write them in C. Netscape tried to make money
selling server software where you could write them in JavaScript (and oh how
everyone laughed).

Like almost everyone in the late '90s during the Internet boom, your author
learned Perl.

## Why Perl Won

Perl was already everywhere, at least on the serious machines you wanted
connected to the Internet. (Microsoft was still struggling to understand why
you'd want to connect to the Internet. Then again, in the 2010s, Microsoft
started to wonder why you would want a computer which *didn't* behave
exactly like a tablet. Legions of gamers cringe as they consider a Halo 5 where
you must tap your TV screen to fight off the Covenant and Prometheans.) Perl
was everywhere because it was a good language for system administration,
bridging the gap between C and shell. Shell was a terrible language, mostly
because it didn't run the same way everywhere and it didn't handle things like
variables or functions very well.

Perl was everywhere, at least in the Unix world. It was good at manipulating
strings. Back in those days, HTTP and HTML were all stringy protocols. You get
a string, you parse it, and you emit a string. It was a mess, but it was a
simple mess and it was a small mess, so you could get away with it—more
importantly, you could get your work done before you figured out where you'd
gone wrong with string handling in C.

Perl was on version 5 of the language, as exemplified by the second edition
of a book called *Programming Perl*. You could walk into a room full of
techie cubicles and find that book on at least one desk, all dog-eared and full
of Post-its, because in any group of a couple of dozen
engineers/programmers/techies in those days, one of them was running a little
webserver on a Linux box under his or her desk and odds are he or she was using
Perl.

The code wasn't great. A lot of it was copied and pasted and modified and
downloaded and modified again from the kind of technical support forms that
StackOverflow has mostly thankfully (and almost entirely humorlessly)
supplanted.

But it worked.

Perl *did* have the advantage of momentum and ubiquity and efficacy
in those days. But it lost. Why?

## Perl Wasn't and Isn't Perfect

You can make the argument (and you're correct to do so) that people didn't
learn Perl for the sake of learning Perl. You can also make the argument that
people didn't really learn Perl at all—they learned enough to modify
programs that almost worked right to work a little bit righter. You can argue
that, but you're missing the important point: that's what people
*always* do. It looks different on the web now these days with bigger
frameworks and more choices and Google and StackOverflow, but it's not
materially different now than it was then.

Perl as a language had its quirks and flaws. It still have some of those
flaws and it definitely has those quirks. Perl's ease of using external
binaries within programs made it great for gluing things together, but there
were multiple documented cases of security holes and unintentional bugs from
people using backticks in [scalar
or list context](http://modernperlbooks.com/books/modern_perl_2014/01-perl-philosophy.html#Y29udGV4dF9waGlsb3NvcGh5) and not knowing the difference and exposing sensitive
information. People writing code by copy and paste and modify didn't learn the
nuance of the Perl philosophy which makes context important in part because
people writing code in that fashion don't learn the philosophy of *any*
language and in part because no Perl tutorial really explained the philosophy
of the language in an accessible fashion until 2010's [Modern
Perl](http://www.amazon.com/gp/product/0985451947?ie=UTF8&tag=outspeaking-20).

## Ease of Beginning is Better than Eventual Perfection

The execution model of CGI programs was simple and awful in its simplicity:
the web server would launch a new separate program and provide all of the data
received by the web browser to that program. It would listen for data produced
by that program and send it to the web browser. That doesn't sound awful, but
if you're reading this, you've probably replaced a couple of smartphones with
many times more memory and processor power than the web servers back in those
days had.

Launching a new program for every page requested was a little bit expensive
once your site became a little bit popular.

Even though that model of operation is conceptually straightforward to
understand (just launch a program), configuring your web server to execute
these programs (written in any language by any user) wasn't as easy as it
sounds. If you had a good system administrator, he or she would have set up the
web server to give every user a specific directory in which to put these CGI
programs where they'd run but not expose the world to security holes. If you
had a Linux box under your desk and you were your own system administrator, you
had to learn about directory structures and permissions and paths and the
details of how your web server was compiled and configured. Again, it was
relatively straightforward, but there was a lot to learn and there were a lot
of ways things could go wrong.

None of this was Perl's fault. It was a consequence of the Unix model
meeting the Internet and a lot of intelligent people figuring out the simplest
way to get something working quickly without necessarily thinking about the
*best* way to build something which would have to last for 20 years and
counting. (See also DNS, SMTP, FTP, NNTP, IMAP, IMAPS, SSL, TLS, et
cetera.)

Web programs were easier to write in Perl than they were in C because Perl,
as a language, made them easier, but the dominant execution model of Perl
programs was slow and expensive and difficult to configure.

A web server is just a program, however. If you modified the program, you
could make it do anything—including connecting it with a different
programming language. In fact, you could put Perl in the web server so that you
could simplify the configuration of these programs *and* not pay the
price of loading every program anew for every request.

This is what mod\_perl did. Of course, mod\_perl was part of making the Apache
httpd web server more configurable by giving it a plugin architecture where you
could write extensions to the web server to customize every part of the web
server request and response cycle, so mod\_perl became less a way to make
writing and deploying Perl programs simpler and faster and cheaper and more a
way to write your own extensions to Apache httpd in Perl instead of C (because,
again, Perl was a better language for web programming than C).

This was great, until it wasn't. It addressed part of the problem but it
didn't address other parts of the problem. Installing and configuring mod\_perl
wasn't trivially easy. It was downright difficult in some cases. You
*could* get a speed boost from using it, by trading some memory up front
for less memory used later, but every program attached to mod\_perl could
potentially access the memory space of every other program attached to
mod\_perl, even if both programs belonged to *different* users.

mod\_php solved this problem. PHP was a terrible language back then, good
mostly for making very simple templates which represented web pages. PHP's
memory model fit mod\_php better, though. PHP's deployment model was a lot
simpler, too. No one wanted to write Apache httpd extensions in PHP because it
was a template language, so there was no pressure to make mod\_php anything
other than a very simple template processor which happened to be easy to
deploy.

In fact, it was so easy to deploy that people *used* it. System
administrators set it up because it was so easy to do they couldn't
*not* do it. People began to answer questions about "How do I make a
dynamic web page?" with PHP answers because they didn't mostly have to answer
the question "How do I configure my web server to deploy this CGI program I
wrote in PHP?" and because they never had to answer the question "How do I
bribe my system administrator to enable CGI execution on our web server?"

mod\_php may not be the best way to deploy programs in 2014, but it was the
*easiest* way for non-programmers to deploy programs in 1999 or 2000 and
it's still difficult to beat. (Some people may argue that a Git-based hosting
service such as Heroku is even easier in 2014, but people in 1999 or 2000
didn't have to learn *CVS*, let alone API keys, software as a service,
dependency manifests, or branch management in distributed version control
systems to deploy simple applications to use FTP to drop a *.php* file
in a shared folder.)

PHP didn't get much respect because it wasn't a *real* programming language—and why would you want to use software deliberately simple, only able to implement a templating language, when you could use software that let you write your own plugins to customize the entirety of Apache httpd's request and response cycle? Not that you would, but you *could*?

## Library Dominance is Not a Historical Inevitability

Perl 5 also had a distinct advantage in the [CPAN](http://cpan.org/), a massive library of free software you can
download, use, modify, and deploy in your own programs. Perl had this right for
a long time. Perl advocates long argued (and some presumably still do) that the
large library of CPAN is *the* reason to use Perl.

This may have been true at one point, but it's an argument that gets weaker
over time.

A module ecosystem is an advantage when it contains what you need to get
your job done. If you need a library and it doesn't exists, you have a few
choices. You can do without. You can switch to another language or toolkit
which has that library. You can build your own. If a language community has
enough skilled people with the time and desire and inclination and permission
to write their own libraries, the module ecosystem will grow. When there aren't
enough people (the ecosystem is too new or the ecosystem is in decline), those
libraries won't get written.

In the olden days, you could expect to find a Perl module for most anything
you wanted to do: scrape Google, buy or sell things on eBay, check your Amazon
rank, whatever. You could also find Perl modules to format text, work with
ancient mainframe data specifications, manipulate images in weird formats,
whatever. You could find these, because there were enough people using Perl by
the numbers that the small percentage of users capable of and interested in
producing these modules would do so.

You need large absolute numbers of users to grow a library. That's why
library ecosystems like that of Python, Ruby, and Node.js have grown large in
recent years. They may have started with fewer modules than existed on the CPAN
at the time, but given enough users in absolute numbers, you'll eventually get
the libraries you need.

Keep in mind one other piece of nuance: the modules that written in 2014
aren't necessarily the modules written in 1999. It's less useful to have a
module which understands the Gopher or Archie protocols in 2014 than it was 15
years ago, whereas it's unlikely that anyone in 1999 would have been prescient
enough to produce a Perl module which understands Stripe's JSON over REST API.
In other words, you tend to get in any year the modules that people need now.
Just because CPAN was dominant in 1999 or 2004 doesn't mean that it has what
people want in 2014.

## Maintenance and Greenfield Concerns are Very Different

The concern gets more subtle as you consider the lifecycle of products begun
at different times. A new project started in 2014 is likely to use different
components (and protocols and design patterns) than a project begun in 1999.
For example, the ORMs available in 1999 were... rare. The web frameworks
available in 1999 were... rare. The user management or credit card payment
systems available in 1999 were... well, they weren't Mozilla's Persona or
Stripe.

The modules used by a project first begun in 1999 and maintained until this
day will probably not reflect the modules used by a project first begun
tomorrow. (It's *possible* to continue to refactor the design and
implementation of an existing project such that it evolves through the years to
take advantage of new techniques and new opportunities, but ask yourself how
often that *really* happens and how much work you're willing to put in
to convince business interests *and* developers to do so instead of
eventually scrapping things in favor of a fresh rewrite in a new language or at
least a new architecture.)

The implication for a programming language are difficult to prove
conclusively, but simple to explain: an ecosystem focused more on maintaining
existing projects than creating new projects will be less attractive for new
projects. This is even more true socially than it is technically: an ecosystem
with buzz ("Should you write your next project in Node.js? How about Swift?
Go?" on the cover of your favorite IT rag) is more attractive than one you
first heart about 15 years ago ("Yep, still using C++ at Google.")

## It Takes a Lot of Work to be Lazy

New developers—dabblers and dilettants, even—don't necessarily
care about the same things experienced developers do. An experienced developer
ought to think about safety, about simplicity, and about the long term
maintenance costs of design decisions. Dabblers want to get things done now, as
easily as possible, without having to learn more than they need to. A week
spent figuring out how to configure a web server is a week wasted, when they
could be on to the next thing without their boss breathing down their
necks.

Ease of getting started is big. Ease of finding modules or plugins or
whatever kind of code you can download and modify is really important. The Perl
community did a good job of this early on (and CPAN still has advantages in [testing](http://testers.cpan.org/) and documentation standards that
aren't easily replicated), but Perl lost when it switched to maintenance
mode.

Laziness isn't a virtue when trying to curate a community. It's a vice.
Laziness is something a community has to cultivate on behalf of community
members. Releasing a module for a community as free software is a lot of work,
but it enables a greater laziness among other people. So does reporting or
fixing a bug or writing documentation. Enabling the laziness of others is an
act of love.

Open source proponents want to believe that enlightened self interest will
eventually somehow fill in the gaps such that your laziness can be enabled by
my hard work and vice versa. (One can point to superluminary projects such as
the Linux kernel as an example, but one can just as easily point to tens of
thousands of less successful projects as examples that making this work is
very, very difficult. Yes, Usain Bolt is fast, but 100% of people in the world
aren't as fast as Usain Bolt, to a great degree of accuracy in decimal
placement.)

Enlightened self interest—especially if that self interest depends on
mundane concerns such as "I have a day job" and "I need this for my day job"
and "I need my day job to pay my mortgage and buy food for my
children"—focuses on specific concerns related to what you're doing right
now. If you're creating new things, your concerns might be modules for new
technologies and techniques that other people want right now. If you're
maintaining existing code, then your concerns might be refining existing things
that other people might have wanted when you started your project those many
years ago.

In other words, an ecosystem will slowly become less attractive as a base of
new projects unless it has a continual focus on developing new projects. (This
doesn't even take into account [the difficulty of
hiring good developers](http://outspeaking.com/words-of-technology/the-lemon-market-of-programming-language-adoption.html)—without an attractive ecosystem for a
language, how can you hire junior developers?)

## Why Wouldn't People Create New Things in Perl, Starting in, Oh, Let's Say July 2000?

Some people make the argument that Perl was always a stopgap technology
because of syntax and semantics. You can ignore that argument. Consider the
dominance of PHP and especially JavaScript. Neither language is an example of
careful language design, nor does either language demonstrate modern research
into modern programming languages. (One might joke that both languages are
stuck in the computer science of 1972 at best.) Yet in both cases, [technical quality is a secondary
consideration to product market fit](http://outspeaking.com/words-of-technology/why-javascript-and-php-won-the-web.html). Both languages succeeded because
they're everywhere and both languages continue to be everywhere because they
are everywhere.

Perl dominated Unix by 1998 because it had a better product market fit than
anything else, the same way that the first thing you did when you booted your
shiny new Sun workstation was to install the GNU tools, because they were just
better. (Sorry, BSD fans. Even something as simple as `sort -h` is
the kind of usability improvement that made it worth avoiding the builtin SunOS
stuff, even if Sun Studio weren't both more expensive and less useful than
GCC.)

All that changed when Perl forked itself in July 2000.

It's easy to criticize Perl 6 in 2014, as the project approaches its 14th
anniversary without anything productive to show for it. It's more important to
discuss why the failures of Perl 6 doomed Perl, at least so that other
languages can attempt to make new and interesting failures.

The problem wasn't apparent in 2000. The solution seemed obvious: rather
than let Perl stagnate, start a new project with a lot of excitement and
harness the community's energy to make improvements which would allow Perl to
be a better platform for further new development. A new VM! Better defaults!
Performance improvements! Simplicities! Better library support! These are
exciting things.

Put yourself in the shoes of someone trying to choose a language for a new
project.

It's August 2000. You've heard that Perl 6 will have a beta out in mid-2001.
Cool! Maybe you'll start in Perl 5 and port to Perl 6 when the benefits of the
latter are obvious. After all, they plan to have a compatibility layer, so you
won't have to throw your code away.

It's mid-2001. There's no beta, but that's fine. You've heard that they plan to have something by the end of the year. It's a little disappointing, but it's okay. They're going to merge Perl 5.12 and Perl 6, so you're okay sticking with Perl 5 for now.

It's 2002. There's no beta. There's no delivery date for a beta. In fact,
there's no delivery date for the specification. There's a Perl 5.8 on the way.
Maybe that'll be worth playing with. Everyone knows that Perl 6 is the future
of Perl, but no one can tell you what the migration strategy is from new code
you write today in Perl 5 to use Perl 6.

It's 2006. Six months after the project fizzled out, [the
Perl 5 to Perl 6 bridge is finally announced as abandoned](http://www.nntp.perl.org/group/perl.ponie.dev/2006/08/msg487.html).

It's 2007. Maybe there'll be a 5.10 this year. Will Perl 6 ever replace Perl
5? No one can tell you, and you're getting a little suspicious that it's been
18 months away since July 2000.

It's 2009. Maybe they'll fix some of the bugs in 5.10 this year.

It's 2014. Are you still paying attention?

With every year that passed, as Perl 6 produced more press releases than
actual code, the attractiveness of Perl as a platform declined. Sure, it still
had users. Sure, it still had people starting new projects. (The Modern Perl
movement was a decent attempt to bring wider enthusiasm back into the ecosystem
by dispelling some of the worst myths of the language. It modeled itself after
[JavaScript:
The Good Parts](http://www.amazon.com/gp/product/0596517742?ie=UTF8&tag=outspeaking-20) without realizing that Perl lacked JavaScript's
insurmountable advantage of ubiquity. Who could have predicted that Objective-C
would be interesting again a year before the iPhone came out?)

What it didn't have was a clearly defined future, let alone an articulated
one.

(The argument that [Perl
6 has no practical guiding theme](http://outspeaking.com/words-of-technology/theme-pragmatics-and-purpose-in-programming-language-implementation.html) is subtler, but not difficult to make. In
specific, the current design principle of Perl 6 is to explore ways to modify
the grammar of a programming language such that the language designers can make
backwards incompatible changes in subsequent versions without making programs
written in those languages incompatible while also allowing users to make local
slangs, and all of this without adopting S-expressions.)

Defining the future of a language across the chasm of a version split is
difficult and dangerous. Python has done an adequate job, and it'll have taken
them 20 years from the initial announcements of Python 3000 in 2000 to the
point at which (currently) the maintainers believe that the sun will have set
on Python 2.x for any serious *maintenance* work in 2020. All this, and
Python 3 has existed in a broadly usable form for several years.

"But wait," some Perl advocates protest. "The marketing message of Perl 6
has long been that Perl 5 and Perl 6 are *sister* languages, where Perl
6 has no intent to supplant Perl 5 in toto and Perl 5 has no plan to cease to
exist!"

The problem with *that* line of reasoning—besides being at
least a decade too late to matter—is that it *continues* to split
the potential adopter base. The stated technical reasons for the existence of
Perl 6 still have not been addressed in Perl 5 and may never be addressed, so
even if those flaws were not material to the concerns of potential adopters,
they're now direct and obvious concerns that take up mental space and present
themselves as risks. Worse yet, the question still arises as to what the Perl
community as a whole would look like if Perl 6 were ever to be released in a
generally usable form. Would there be a compatibility layer, such as a revived
Ponie project? Would Perl 6 have the library support people have come to expect
from Perl 5? Would there be documentation, example code, tools, and
knowledgeable support channels as a modern language needs in 2014? Where will
new users of Perl 6 come from and where will existing Perl 5 developers go?

No one can answer these questions. There's just not enough information.
(It's not even possible to speculate responsibly about whether the answers
would have been useful a decade ago.)

None of this is to say that it's *impossible* for Perl to reinvent
itself again and start to gain users. It's *possible* that one of the
Perl 6 works-in-progress will reach a point of usability and gain stability and
maturity as a useful product, with documentation, libraries, support, and
uptake.

Yet with every passing year, it's less likely, and the alternatives grow in
number and desirability (for goodness's sake, at the time of this writing, the
[Swift](https://developer.apple.com/swift/) programming language has
been public for less than a week and already has more users than Perl 6, and
Swift is entirely built on technologies which have been invented since the Perl
6 announcement).

How does a language win? By being compelling enough to be used for
*new* things. It's not solely a technical concern; it's a concern of the
language community and ecosystem.
