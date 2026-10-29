---
url: "https://dev.firmafon.dk/blog/making-the-best-of-private-methods/"
captured_at: "2015-07-24T08:44:58-03:00"
title: "Making the best of private methods - Firmafon Developers Blog"
domain: "dev-firmafon-dk"
---

# Making the best of private methods

Jul 21 2015

The other day my team and I had a discussion about why we use (or don’t use) private methods. I had a hard time trying to explain my reasons why. So I’ve tried to write them in case they’re of use to others.
It’s an assorted take on why I like to split my objects into a public section for other objects to use, while keeping a private section that’s just for the class I’m writing.

### Whenever, Wherever

It’s a distinct trait of cowboy coding to have everything able to send anything to whomever they want whenever they feel like.
That uncertainty inherent in the show all approach spooks me whenever I scan the code. At least if you’ve added private methods, I know you’ve thought about how your class should collaborate - and where it shouldn’t.

### Public interfaces as debt

Ostensibly adding public methods carries a hint of future coding. You’re saying: collaborator classes should have a use for this in the future. But if they don’t have a clear use for it now, why add it? That might not lead to a stable system. To have stability, you must plead a degree of stableness. You intend to keep that method working in the future. Otherwise you’d have an always changing public method. I wouldn’t feel comfortable having my code depend on unstable things. Instability has a way of spreading, potentially without end.

Sometimes you can’t avoid that shaky footing. After all your code is bound to change. It’s written to be rewritten. Though needless rewrites carries no sense and the best way to counteract those is slimming down what your class will commit to keeping stable. It means keeping more methods to yourself, free from others’ grubby hands. This way you’re also less likely to underdeliver because the promise is much smaller. The rest of your app also becomes more stable, because code pieces have shorter reach.

### Hide how, focus on what.

Usually we’re very concerned about how to do something. We’re problem solvers with recipes in our toolbelt. But I’ve found that leaves me blind to what my code is trying to tell me. Whenever I’ve succumbed to expose how my objects do something the code has been more brittle. How something is done is usually a series of steps, and those are bound to change. Now what those steps achieve together are probably less likely to change. Let’s say you have a workout routine. The individual exercises could change, but the ”what” stays. It’s still a workout.

When you force yourself to think about ”what”, your system becomes more stable and easier to reason about. Private methods help you by making it easier to hide the how, and focus on the what.

### Keywords don’t have to be the delimiter

I’ve been using private throughout, which in a language like Ruby, is a keyword that change a method’s visibility. Though you don’t have to use keywords to fence off the public. Rails, for example, has methods that are for internal use but they’re in the public namespace. Now how do people know not to use them? Those methods are marked as `:nodoc:`, which means they won’t show up in the public section of the generated documentation. This way there’s a clear split between what you can rely on and what we in the Rails team use to implement the framework.

### Private as a proving ground

I start methods as private and promote them to public only if there’s frequent need for them outside of the class. What level of frequent tips the scale will be different for every case. In our Rails app, we had a case where a `before_save` callback was private, but the code was useful in the console. We didn’t want to have to `send` it, and instead chose to make it public. This way we were more explicit about what our class handled while still being flexible.

I think it’s fine to promote a method that’s shown use to public. You still get the benefit of starting with your cards close. If some methods seem useful outside of the class you’ve found a real need. Adding a missing piece is a better direction than making it harder to refactor your code.
There’s also the chance that there are other private methods closely related to the one you’re thinking about making public. What should happen to those? I’d say leave them in the dark, there’s no reason to shine light where none has been needed.

This could be unnecessary busywork. Bureaucracy seeping into our world of code. But I see it as a profoundly humane effort. We’re writing code for humans to make sense of it. We need our objects to have boundaries, we need them to be as stable as possible, while keeping them free to change.

### Privacy and flexibility

For me that freedom is what private methods really bring. The flexibility to allow you to change your mind without worrying about disturbing other pieces of your code. Starting a method out as private also allows you to try out an abstraction and see if you’ve found the right fit. Sometimes methods do too much and become a rats nest of configuration, other times, the method is short lived and better off being inlined. This is design emerging from the bottom up. Your code evolves from actual needs. As I see it, private methods are the seeds which help unearth those sprouts. This way you get to keep your sanity because the code sprouts in a clear and controlled way.

In real world architecture the foundations never change. But the facade is continually renovated. It’s in code we keep a stone face while underneath our bedrock is crumbling.

[How do you track down an obtuse error in your Rails app?](https://dev.firmafon.dk/blog/how-do-you-track-down-an-obtuse-error-in-your-rails-app/)
