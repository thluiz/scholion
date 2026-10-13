---
url: "http://www.xml.com/lpt/a/2004/12/01/restful-web.html"
captured_at: "2013-02-20T10:11:05-03:00"
title: "XML.com: How to Create a REST Protocol"
domain: "xml-com"
---

# **H**ow to Create a REST Protocol

  
 Published on **[XML.com](http://xml.com/)**  <http://www.xml.com/pub/a/2004/12/01/restful-web.html>  
[See this](http://www.xml.com/pub/a/admin/printhelp.html)  if you're having trouble printing code examples
  
  
**How to Create a REST Protocol**  
**By** Joe Gregorio  
December 01, 2004

*Note: In this inaugural article of Joe Gregorio's new column,
The Restful Web, he explains how to use the REST architectural style
to create an application protocol with web-like properties**.** Future
columns will offer additional REST-based applications and
analyses**.** — Editor*

If you follow web services, then you may have heard
of REST**.** REST is an architectural style that can be
used to guide the construction of web
services**.** Recently, there have been attempts to create
such services that have met with mixed success**.** This
article outlines a series of steps you can follow in
creating your protocol--guidance that will help you
get all the benefits that REST has to offer, while
avoiding common pitfalls**.**

### What Is REST?

What is REST anyway**?** It is an architectural style.
An architectural style is a named, coordinated set of
architectural constraints**.**

> A software architecture is defined by a
> configuration of architectural
> elements--components, connectors, and
> data--constrained in their relationships in
> order to achieve a desired set of
> architectural properties**.** [[Roy
> Fielding](http://www.ics.uci.edu/%7Efielding/pubs/dissertation/software_arch.htm#sec_1_2)]

### Why Follow REST**?**

The whys of REST are covered on the [REST
Wiki](http://rest.blueoxen.net/cgi-bin/wiki.pl?FrontPage) **.** There are advantages to be had, from
scalability, to simplifying implementation, to
increasing the ability for your service to be reused**.**
Jon Udell has two great articles, [The Beauty of REST](http://www.xml.com/pub/a/2004/03/17/udell.html)  and [Tangled in Threads: The power of the URL-line](http://udell.roninhouse.com/bytecols/2001-08-15.html) , that
cover the benefits of a 'composable' system**.**

Look at it this way: if you're using the
infrastructure of the web to move your data around,
shouldn't you follow the best practices that will help
your data move more smoothly through the system**?** It's
better to go with the flow than to try to swim up
stream**.**

### How to Create a RESTful Interface

Now we get to the meat of the matter**.** Instead of
covering this from an architectural view, I'll
approach it from a recipe perspective, a
series of steps you take and questions you
can answer, that will hopefully guide you to
creating a great REST interface**.**

To create a REST service, you need to answer the following
questions, and you should answer them in this order:

1. What are the URIs**?**
2. What's the format?
3. What methods are supported at each URI**?**
4. What status codes could be returned**?**

In laying out these questions, I didn't use the
proper naming conventions; instead, I used the common
names for things that most developers are familiar
with**.** As we answer each question, I'll also introduce
the proper nomenclature**.**

### Question 1: What Are the URIs?

The proper nomenclature would be "What are the
resources**?**" The things identified by URIs are
"resources." That is the terminology used in Roy
Fielding's thesis and also the same terminology used
in [Architecture of the World Wide Web, First
Edition](http://www.w3.org/TR/webarch/#information-resource)**.** Resources are identified by URIs.

You might be creating a RPC protocol, or worse, if
you only have a single URI that everything goes
through**.** Many years ago, one of the first intranet
services I put together was a web interface to an ECO
(Engineering Change Order) system**.** Every time a part
was changed, an ECO was filed and had to flow through
this system**.** I created a single script that handled
the whole system, a single script that took all it's
parameters via POST**.** That meant there was no way to
bookmark a page in the system; each page had the same
URI: `/cgi-bin/eco.cgi`**.** Employees wanted
to bookmark certain ECOs or send shortcuts via email,
but they couldn't because the URI in the address bar
never changed**.** It was always the
same, `/cgi-bin/eco.cgi`, unchanging, like
the blinking 12:00 on an unprogrammed VCR**.** The
employees didn't know about REST, but what they did
know implicitly is that each resource, in this case, an
ECO, should have its own URI**.**

Break your problem down into the types of resources
you want to manipulate**.** The thing to remember is that
each resource should have its own URI**.** Try to list all
the resources you could possibly need at this
step**.** Two places to consider when looking for
potential resources are collections and search
interfaces**.** A "collection of resources" may, in itself,
be a whole new resource**.**

A search interface is another source of
resources**.** You enter criteria for the resources you
want to find, and a list of matching resources are
returned**.** You may notice, though, that the results of a
search are just a collection of resources, ones that
match a particular criteria, and as such, this is
really just a narrower version of the first case of a
resource collection**.**

Consider a very simple example of a system for
maintaining an employee contact list**.** For our example,
it will contain each employees name, title, and
contact information**.** In such a system, each user should
have their own URI with an appropriate
representation**.** That representation should contain the
name, title, and contact information for that
employee**.**

There is also a collection of resources that is, in
itself, another resource**.** The collection of all
employees is another resource in our system**.** So we
have identified two kinds of resources in this tiny
system, and so there will be two types of URIs:

1. Employee (One URI per employee)
2. All Employees

After you've identified the resources via their
URIs, it's time to consider the next question**.**

### Question 2: What's the Format?

The proper terminology here is "representation**.**"
You can't actually reach out and touch the resources
behind the URIs you identified in Step 1**.** What you
*can*  do is exchange representations of those
resources**.** When I do a GET on an "employee" resource,
I need to get something back which conveys information
about that employee**.** These days HTML, XML, images,
sound, and movies are all potential formats that could
be used**.** For now, we'll restrict ourselves to using
XML: it's a pretty popular format, lots of tools are
available to process it, and there is an expectation
that when you say "web services," you are referring
primarily to the exchange of XML documents**.** And, yeah,
this is being published on XML.com**!**

For each of the resources you listed in Step 1, you
need to decide what the representations are going to
look like**.** If possible, reuse existing formats if they
are applicable**.** This can increase the chances that
your system can be composed with other systems.

In our example employee contact list above, we could
have the following representations:

Employee Format
:   For the sake of exposition, I will make up
    a new XML format for this information**.** [Exposition](http://dictionary.reference.com/search?q=exposition) --"A statement or rhetorical discourse intended
    to give information about or an explanation of
    difficult material"--which just means that I
    get to cheat as long as you learn something in
    the process**.**
:   ```
    <employee xmlns='http://example.org/my-example-ns/'>
        <name>Full name goes here.</name>
        <title>Persons title goes here.</title>
        <phone-number>Phone number goes here.</phone-number>
    </employee>
    ```

Employee List Format
:   Since each employee will have his or her own
    URI with all the details there, our list will only
    include that URI**.**
:   ```
    <employee-list xmlns='http://example.org/my-example-ns/'>
        <employee-ref href="URI of the first employee"/>
    	 Full name of the first employee goes here.</employee>
        <employee-ref href="URI of employee #2"/>Full name</employee>
        .
        .
        <employee-ref href="URI of employee #N"/>Full name</employee>
    </employee-list>
    ```

Note that we haven't mapped the representations to
resources just yet**.** To do that, we need to consider
the methods.

### Question 3: What Methods Are Supported at Each URI**?**

In the proper nomenclature, how do the URIs we
defined in Step 1 get *dereferenced***?**

> Agents may use a URI to access the
> referenced resource; this is
> called dereferencing the
> URI**.** Access may take many forms,
> including retrieving a representation of the
> resource (for instance, by using HTTP GET or
> HEAD), adding or modifying a representation of
> the resource (for instance, by using HTTP POST
> or PUT, which in some cases may change the
> actual state of the resource if the submitted
> representations are interpreted as
> instructions to that end), and deleting some
> or all representations of the resource (for
> instance, by using HTTP DELETE, which in some
> cases may result in the deletion of the
> resource itself)**.** [[Architecture
> of the World Wide Web, First Edition](http://www.w3.org/TR/webarch/#dereference-uri)]

We'll restrict the discussion to accessing
resources using one the four basic HTTP methods that
can be applied to a URI: GET, POST, PUT, and DELETE**.** HEAD
is really a GET without a response body, and there are
also others defined by RFC 2616 like OPTIONS**.** In
addition, specs like WebDAV introduce even more
methods**.** That's nice, but you should be able to go
very far with just the four basic methods, which align
nicely with CRUD, an acronym from the database world
which stands for [Create,
Retrieve, Update, and Delete](http://en.wikipedia.org/wiki/CRUD.) **.**

| HTTP Method | CRUD Action | Description |
| --- | --- | --- |
| POST | CREATE | Create a new resource |
| GET | RETRIEVE | Retrieve a representation of a resource |
| PUT | UPDATE | Update a resource |
| DELETE | DELETE | Delete a resource |

I hesitated to include this table**.** By presenting it,
I wanted to point out the overlap in the four basic
methods of HTTP**.** What I **don't** want to
happen is that you start thinking of web resources as
SQL tables**.** Don't do that.

Make sure your GETs are side-effect free**.** This is a
biggie, the one where many services get it wrong**.** GETs
must be both [safe](http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html#sec9.1.1) and
[idempotent](http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html#sec9.1.2)**.** In turn, [anything which does not have side effects
should use GET](http://www.w3.org/DesignIssues/Axioms.html#state)**.**

So if you want to create a new resource, use
POST**.** Want to retrieve a representation of a resource?
Use GET. To update a current resource, use
PUT**.** Finally, to delete a resource, use DELETE.

Once you have decided on the URIs (Step 1), picked
representations (Step 2), and decided on methods (Step
3), you need to match them all up**.** At the very least,
you'll need to pick a representation for the response
of every GET and a representation to place in the
request for PUT and POST**.** Optionally, you may want to
consider the representation, if any is returned from
a POST**.**

Let's go back to our employee contact list, and now
we can match up the resources, the representations,
and the methods**.**

| Resource | Method | Representation |
| --- | --- | --- |
| Employee | GET | Employee Format |
| Employee | PUT | Employee Format |
| Employee | DELETE | N/A |
| All Employees | GET | Employee List Format |
| All Employees | POST | Employee Format |

### Question 4: What Status Codes Could Be Returned**?**

Not only do you need to know what type of
representation is returned, you also need to enumerate
the typical HTTP status codes that could be
returned**.** In a perfect world, this step wouldn't be
necessary since a good implementation would handle
every status code correctly**.** In practice, you should
list all the status codes you expect to return**.** This
will provide good guidance for implementers on the
conditions they should be testing for**.**

We'll update our table for our employee contact
list to include the expected status codes

| Resource | Method | Representation | Status Codes |
| --- | --- | --- | --- |
| Employee | GET | Employee Format | 200, 301, 410 |
| Employee | PUT | Employee Format | 200, 301, 400, 410 |
| Employee | DELETE | N/A | 200, 204 |
| All Employees | GET | Employee List Format | 200, 301 |
| All Employees | POST | Employee Format | 201, 400 |

### Warning Signs

Even following these steps, you could still make
some mistakes**.** Paul Prescod has created a list of [Common
REST Mistakes](http://www.prescod.net/rest/mistakes/)  that is worth reviewing as you work
on your protocol**.**

### Review

Let's review**.** To build a good REST service you need
to answer the following questions:

1. What are the URIs**?**
2. What's the format?
3. What methods are supported at each URI**?**
4. What status codes could be returned**?**

And that's all there is to it**.** You don't believe
me? Good, because it's not true**.** There's lots more to
discuss, like compression, etags, caching,
extensibility, idioms, and implementations**.** See you
next month.

**XML.com** Copyright © 1998-2006 O'Reilly Media, Inc**.**
