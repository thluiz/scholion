---
url: "http://www.marcnewlin.me/2015/06/write-beautiful-code.html"
captured_at: "2015-06-02T14:17:11-03:00"
title: "Making software is way fun.: Write beautiful code"
domain: "marcnewlin-me"
---

# Write beautiful code

Writing code is much more than an engineering discipline; it is a true art form. Each line of code you write reflects your understanding of the language, your ability to communicate ideas to other engineers, and the lessons lessons from previous projects.

There is no "correct" code style, just as there is no "correct" solution to any given engineering task. The internet is littered with style guides written in absolutes, and these can be useful, but often forget that the context of a project is as important as the code itself. Mocking up a proof of concept for a hobby project is very different than implementing a base class to be used by your entire team.

When you write code, your first priority is to satisfy functional and performance requirements. This is universally requisite, but as engineers, we often forget the importance of ensuring that our code be easy to understand by other programmers (including your future self). Remember that time you looked at a project from six months ago and had no idea how it worked? It doesn't have to be that way.

Let's dispel some myths about writing beautiful code.

Myth #1 - Verbose comments make you a bad programmer

Many engineers profess that comments are unnecessary, and that a good engineer should be able to read code completely devoid of comments. This sounds cool, and conjures up an image of a badass motherfucking sorcerer-hacker wizard-god reading the matrix on 16 goddamn monitors at once. The thing is, as mere mortals, we are better at processing natural language than code. Certainly we need to be able to read and understand code quickly, but it is usually easier to parse a few sentences in your native language than to truly understand the code in an unfamiliar function.

Myth #2 - White space is bad

A common school of thought is that less code is better, and less white space is better. Surely if we remove all blank lines and keep our code as tiny as possible, everybody wins, right? I mean, classic Greek and Latin was written in all caps and without spaces, so we should apply that to our code, right?

Let's consider the following function, with and without comments and line breaks.

No comments, no line breaks

vectorcomplexdouble>>plcp\_dataencode(Raterate,vectorunsignedpayload,unsignedshortservice)

RateParams rate\_params RateParams(rate); num\_symbols ceil(double (payload.size() double(rate\_params.dbps)); num\_data\_bits num\_symbols rate\_params.dbps; num\_data\_bytes num\_data\_bits num\_pad\_bits num\_data\_bits (payload.size() vectorunsigned data(num\_data\_bytes

memcpy(data[service,    memcpy(data[], payload.data(), payload.size());

boostcrc\_32\_type crc;    crc.process\_bytes(data[ payload.size());unsigned calculated\_crc crc.checksum();    memcpy(data[ payload.size()], calculated\_crc,

vectorunsigned scrambled(num\_data\_bytes state , feedback num\_data\_bytes; x       feedback (state (state       scrambled[x] feedback data[x];       state ((state << feedback;    data.swap(scrambled);

vectorunsigned data\_encoded(num\_data\_bits    viterbi v;    v.conv\_encode(data[], data\_encoded.data(), num\_data\_bitsvectorunsigned data\_punctured puncturerpuncture(data\_encoded, rate\_params);

interleaver inter;vectorunsigned data\_interleaved inter.interleave(data\_punctured);vectorcomplexdouble>> data\_modulated modulatormodulate(data\_interleaved, rate);

return data\_modulated;

Verbose comments, liberal line breaks

// Encode the data portion of a PLCP frame given a rate, payload, and service fieldvectorcomplexdouble>> plcp\_dataencode(Rate rate, stdvectorunsigned payload, unsignedshort service)// Get the parameters associated with the given rate    RateParams rate\_params RateParams(rate);// Calculate the number of symbols num\_symbols ceil(double/\* service \*/ (payload.size() /\* CRC \*//\* tail \*/double(rate\_params.dbps));// Calculate the number of data bits/bytes (including padding bits) num\_data\_bits num\_symbols rate\_params.dbps; num\_data\_bytes num\_data\_bits // Calculate the number of padding bits (past the 6 tail bits) num\_pad\_bits num\_data\_bits /\* service \*/ (payload.size() /\* CRC \*//\* tail \*/// Concatenate the service and payloadvectorunsigned data(num\_data\_bytes    memcpy(data[service,    memcpy(data[], payload.data(), payload.size());// Calcualate and append the CRC    boostcrc\_32\_type crc;    crc.process\_bytes(data[ payload.size());unsigned calculated\_crc crc.checksum();    memcpy(data[ payload.size()], calculated\_crc, // Scramble (whiten) the datavectorunsigned scrambled(num\_data\_bytes state , feedback num\_data\_bytes; x       feedback (state (state       scrambled[x] feedback data[x];       state ((state << feedback;    data.swap(scrambled);// Convolutionally encode the datavectorunsigned data\_encoded(num\_data\_bits    viterbi v;    v.conv\_encode(data[], data\_encoded.data(), num\_data\_bits// Puncture the datavectorunsigned data\_punctured puncturerpuncture(data\_encoded, rate\_params);// Interleave the data    interleaver inter;vectorunsigned data\_interleaved inter.interleave(data\_punctured);// Modulate the datavectorcomplexdouble>> data\_modulated modulatormodulate(data\_interleaved, rate);

return data\_modulated;

A good engineer can parse either function and figure out what's going on, and that makes sense, it's kinda what we do. The thing is, it takes at least an order of magnitude longer to parse and understand the uncommented version.

Programmers often argue that comments are redundant, but as projects grow in size and complexity, comments are like the notes you use to cram before a big exam. In a profession that values efficiency, it makes sense to comment early and often.

Difficult to decipher code might look cool, and obfuscated programming competitions reveal some pretty fucking rad language features. Unfortunately, we live in the real world, and in the real world we need to cater to every engineer who might look at your code in the future. Don't be a dick. Comment your code.

Myth #3 - Naming conventions matter

This is really a half-myth. In the ever raging battle between **PascalCase****camelCase****underscore\_case****I\_LOVE\_LAMP\_CASE** and the like, there will never be a winner. It is a pointless war. Everybody has a preference on naming conventions, and some languages overwhelmingly prefer one style over the other. The only thing that matters is consistency.

- If you are working on an existing project, for the love of science, follow the conventions already in place.
- If you are starting a new project, figure out what naming conventions you want to use, and stick with them.
- If you are writing a project in a language with a style guide, it is good to follow the naming conventions defined in it. It might not matter in the scope of your project, but six months from now, your company is going to hire a C# veteran. This veteran is going to use camelCase and fuck up the underscore\_case you lobbied so hard for. You are going to get sad, and it is better to be happy. Be happy.

Myth #4 - Using third party libraries is bad Engineers like building things and can be hesitant to use others' code. I love the sense of accomplishment of implementing a complex algorithm in an efficient way. It feels great, and I think, "golly gee, I must be a good engineer, I implemented this complex mathsomethingorotherfunction(...) in only two days! Go me! I can do hard things!"The thing is, most of the time, had I Googled around a bit, I would have found an MIT/BSD licensed library to do exactly what I needed and more.  If somebody else has already written the code you need, and it satisfies the licensing requirements of your current project, use it. As much fun as it is to have complete ownership over your code, you could have spent those two days building something new and original instead. Get to the point already...

I could spend all day ranting about what not to do, but you would probably just get bored and go back to Reddit or Hacker News or Slashdot or whatever it is that you do at work, so it is about time to get to the point. If you take away one thing from this blog post, it is this: Write your code so a freshman computer science student can read it. Keep it simple and don't over-complicate things. The enlightened programmer will leave his or her ego at the door, write as little, well commented code as possible, and be more productive for it. Write beautiful code.
