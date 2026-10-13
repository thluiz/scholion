---
url: "http://blogs.msdn.com/b/tomholl/archive/2009/05/21/protecting-against-xml-entity-expansion-attacks.aspx"
captured_at: "2013-12-05T11:01:05-03:00"
title: "Protecting against XML Entity Expansion attacks - Tom Hollander's blog - Site Home - MSDN Blogs"
domain: "blogs-msdn-com"
---

# **P**rotecting against XML Entity Expansion attacks

21 May 2009 5:25 AM

- [4](#comments)

One of the critical responsibilities of every developer and architect is to understand, and know how to prevent, as many kinds of security attacks as possible**.** While there are many types of attacks and many weapons at our disposal to thwart them, the most basic defence we have is input validation**.** The rule of thumb really needs to be to assume all input from uncontrolled sources is malicious, unless you can prove otherwise**.** This includes input from end users, as well as input from other systems.

Recently I worked on an application that received XML files from that most untrustworthy of sources, the Internet**.** Knowing the kind of people who lurk there, we took what seemed like a responsibly paranoid approach involving validating each parsed document against an XML schema, checking a digital signature to ensure it came from a known sender, and cherry-picking the values we needed out of the document**.**

So I was quite surprised to learn that there were was a class of attack which we had not mitigated**.** It turns out that you should *never* load untrusted XML content into a .NET **XmlDocument** class as a first step, even if you plan to do all sorts of checks on it afterwards**.** This is because there is a class of attack which can bring your server to meltdown just by getting it to parse some XML**.**

Consider this piece of XML:

```
<!DOCTYPE foo [ 
  
<!ENTITY a "1234567890" > 
  
<!ENTITY b "&a;&a;&a;&a;&a;&a;&a;&a;" > 
  
<!ENTITY c "&b;&b;&b;&b;&b;&b;&b;&b;" > 
  
<!ENTITY d "&c;&c;&c;&c;&c;&c;&c;&c;" > 
  
<!ENTITY e "&d;&d;&d;&d;&d;&d;&d;&d;" > 
  
<!ENTITY f "&e;&e;&e;&e;&e;&e;&e;&e;" > 
  
<!ENTITY g "&f;&f;&f;&f;&f;&f;&f;&f;" > 
  
<!ENTITY h "&g;&g;&g;&g;&g;&g;&g;&g;" > 
  
<!ENTITY i "&h;&h;&h;&h;&h;&h;&h;&h;" > 
  
<!ENTITY j "&i;&i;&i;&i;&i;&i;&i;&i;" > 
  
<!ENTITY k "&j;&j;&j;&j;&j;&j;&j;&j;" > 
  
<!ENTITY l "&k;&k;&k;&k;&k;&k;&k;&k;" > 
  
<!ENTITY m "&l;&l;&l;&l;&l;&l;&l;&l;" > 
  
]> 
  
<foo>&m;</foo>
```

This certainly looks like an odd bit of XML, but at first glance it doesn’t appear overly scary**.** It’s compact, well-formed and actually only contains one element: <foo>**.** But what’s in that element? It’s a single custom-defined entity, &m;**.** And how is that defined? Well, it’s 8 other custom &l; entities**.** So what’s an &l; then? Hmm, it’s 8 &k;s**.** You can see where this is going. The document will end up with 812 &a;s, where each &a; has 10 characters, so that innocent looking &m; will blow out to 10x812 or 687,194,767,360 characters**.** And on my reasonably well spec’ed developer machine, expanding that number of characters consumed all of my CPU for longer than I was prepared to put up with**.** A bad guy armed with this attack isn’t going to steal any data, but they could still cause a lot of damage through denial of service**.**

The good news is that it’s actually very easy to stop this entity expansion in its tracks**.** The key is to use an **XmlReader** before parsing the document into an **XmlDocument** (or instead of, if you can live without a fully-parsed document)**.** It’s possible to validate against an XSD or other schema type using an **XmlReader** too, but here’s a minimalist example showing how you can check that a document is well-formed, contains no DTDs (and hence no entity definitions) and is less than 10K in size:

```
// Prepare text reader and settings for Xml Validation
StringReader textReader = new StringReader(unparsedXml);
XmlReaderSettings settings = new XmlReaderSettings();
settings.XmlResolver = null;
settings.MaxCharactersInDocument = 10000;

// Successfully parse the file, otherwise an XmlException is to be thrown
XmlReader reader = XmlReader.Create(textReader, settings);
while (reader.Read()) ;
```

If you get to this point without an **XmlException** being thrown, the document should be safe to parse**.** Of course, there could be all sorts of evil things lurking within the elements of the document, so you need to continue to use appropriate validation and encoding as you would for any untrusted input**.**

- [4 Comments](http://blogs.msdn.com/b/tomholl/archive/2009/05/21/protecting-against-xml-entity-expansion-attacks.aspx#comments)

[Security](http://blogs.msdn.com/b/tomholl/archive/tags/Security/)
