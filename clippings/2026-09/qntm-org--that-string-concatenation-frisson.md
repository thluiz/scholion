---
url: "https://qntm.org/concat"
captured_at: "2026-09-25T20:21:19+01:00"
title: "That string concatenation frisson"
domain: "qntm-org"
---

If I see code along the lines of:

const ref = application + ':' + endpoint

then I'm going to request that you provide a rigorous proof that neither of the strings `application` or `endpoint` can ever contain a colon. In accordance with my belief that [code should be obviously correct](https://qntm.org/devphilo), not provably correct, your proof will look something like this:

if (application.includes(':') || endpoint.includes(':')) {
  throw Error()
}

This is because **I have been down this road too many times.**

There are two major scenarios where concatenating strings together in this way is dangerous. The first is if we intend to use `ref` as some kind of unique identifier. A key in a hash table, maybe. In this case, we are at risk of collisions, _e.g._ `application = 'a:b'; endpoint = 'c'` collides with `application = 'a'; endpoint = 'b:c'` as both result in `ref = 'a:b:c'`.

The second is if we are trying to send two strings through some kind of field which nominally only allows a single string to be passed, with the intention of splitting the single string to recover the two original strings at the other end. In this case, we risk not being able to recover the original strings, _e.g._ `'a:b:c'` could resolve to either `application = 'a:b'; endpoint = 'c'` or `application = 'a'; endpoint = 'b:c'`, or even:

const \[application, endpoint\] = ref.split(':')
// application = 'a', endpoint = 'b'

This is particularly amusing if instead of `application` and `endpoint` we have, say, `username` and `role`. It's all fun and games until someone figures out how to inject `username = 'horse:admin'`. Yes, I have seen this.

If it is unavoidable that `application` and/or `endpoint` must allow colons, then see if you can just send them separately. Otherwise, you need a rigorous procedure for properly escaping the delimiter prior to concatenation. And in the second case, unescaping them and recovering the originals.

### Discussion (10)

#### [2025-02-04 00:08:09](#komment67a15a693f9ab) by tyler:

\> rigorous proof that neither of the strings application or endpoint can ever contain a colon. That example definitely counts as a "code smell", but the requested proof isn't good enough, and the problem is much more general. Okay, nothing contains a colon. So what? That only means so much when the broader context is not well defined. Maybe the resulting single-colon string will be used in a URL, in which case a slash or a percent sign could be just as bad as a colon. Moreover, should colons be fully banned, or should they be encoded in some way? Maybe encoded in the first part and left alone in the second? For example, if you're putting file names into a hash table, prefixed by the Unix owner name and a colon, restricting colons might cause me grief: I've got files with colons in their names. But, also, this gets us into the larger problem of encodings. My file names are all valid UTF-8, as far as I know, but they don't have to be. What are the actual and expected low-level encodings of the input and output strings? What if it's invalid UTF-8, or is UTF-16 with a surrogate pair mismatch? Can the input contain NUL characters, are they properly handled by the language, and will the consumer properly handle them? What about stuff outside ASCII? The way I see it, "strings" are often meant for specific purposes such as human-readable text, and abused to store other things. Those proposed colon-checks would just worry me further; they look too ad-hoc, and are not explained. Depending on the language and purpose, perhaps those should be passed as a tuple of strings, or an object with two length-and-binary-data members.
