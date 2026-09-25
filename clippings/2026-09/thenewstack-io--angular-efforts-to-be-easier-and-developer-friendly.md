---
url: "https://thenewstack.io/angulars-efforts-to-be-easier-and-developer-friendly/?ref=dailydev"
captured_at: "2026-09-25T21:23:00+01:00"
title: "Angular’s Efforts To Be Easier and Developer Friendly"
domain: "thenewstack-io"
---

Developers who tried Angular years ago should revisit the framework because it’s simpler, more performant and more developer-friendly now, an Angular representative told audiences at a Saturday teleconference.

Mark Thompson, a senior developer relations engineer at [](https://cloud.google.com/?utm_content=inline+mention)Google, spoke as part of Medium Day, a conference hosted by the online content platform. [Angular maintains a blog](https://blog.angular.dev/) on Medium. He shared how Angular has improved and discussed plans for its future, which includes partial hydration.

“We had a interesting reputation,” he said. “One of our reputation points was that Angular was hard to learn, and it’s for good reason.”

Thompson outlined what Angular has done to change that reputation, starting with the code for a Hello World application. He showed the volume of code required to create a “Hello World.”

[![](https://cdn.thenewstack.io/media/2024/08/16e71921-helloworldangularcode.jpg)

Zoom



](https://cdn.thenewstack.io/media/2024/08/16e71921-helloworldangularcode.jpg)

Screenshot via Mark Thompson’s presentation.

“This is the full function of hello world, which feels like a lot. It was hard to process for people, so we heard the feedback, and then we did better for a better developer experience,” he said. “Now here’s that same application, but much more focused, and you’re able to have a better experience, a lot less code.”

[![A shorter block of text of revised Angular code for Hello World.](https://cdn.thenewstack.io/media/2024/08/af8b8b4a-hellowordlesscodeangular.jpg)

Zoom



](https://cdn.thenewstack.io/media/2024/08/af8b8b4a-hellowordlesscodeangular.jpg)

Screenshot via Mark Thompson’s presentation

Today, the Angular team is focused on three pillars, which he added would apply to any framework or [next generation of “supercharged” web applications](https://thenewstack.io/whats-next-in-building-better-generative-ai-applications/):

*   Performance
*   Developer Experience
*   AI Smarts

## Improving Angular Developer Experience

One of the areas where Angular thought it could [improve developer experience](https://thenewstack.io/improving-developer-experience-drives-profitability/) was in how it handled syntax when working in templates, he said. He showed a block of code and began walking through the details.

TRENDING STORIES

1.  [A New JavaScript Framework? In this Economy?](https://thenewstack.io/a-new-javascript-framework-in-this-economy/)
2.  [Trends That Defined JavaScript in 2025](https://thenewstack.io/trends-that-defined-javascript-in-2025/)
3.  [Why Developers Are Ditching Frameworks for Vanilla JavaScript](https://thenewstack.io/why-developers-are-ditching-frameworks-for-vanilla-javascript/)
4.  [The Pros and Cons of Using React Today](https://thenewstack.io/the-pros-and-cons-of-using-react-today/)
5.  [Recreating Shopify’s BFCM Globe Using react-globe.gl](https://thenewstack.io/recreating-shopifys-bfcm-globe-using-react-globe-gl/)

“Even trying to explain this to you, I could understand, if you’ve never seen Angular, how this can feel like it’s not as intuitive, and that makes sense,” he said.

Then he shared the revised code, which was notably clearer.

“Now we’re using our new built-in syntax for conditional rendering,” he said. “Now I think anybody who has some programming experience could read this … Even if you don’t write Angular, this becomes a better experience, because you can read this and get a pretty strong idea about what’s happening.”

## Modern Reactivity in Angular: Signals

In frontend development, reactivity is the automatic updating of the UI when the underlying data changes.

“Reactivity is all the rage right now. People are thinking about reactivity in \[the\] form of how do you update your UI based on the changes to your data?” Thompson said.

Angular decided to “solve” the reactivity with automatic reactivity, which removed the reactivity problem from the developer. But that created a different problem, he said: It didn’t work at scale.

“Extracting the reactivity layer so much meant that when people built scalable apps, they ran into problems because they needed more fine-grained control,” he said. “That led us to building what we call Angular Signals.”

[Angular Signals](https://thenewstack.io/dev-news-wordpress-6-5-angular-signals-and-net-components/) is based on three components, he explained:

*   Signal
*   Computed
*   Effect

### Angular’s Signal Component

An Angular signal is a value that can tell Angular when it changes and is capable of notifying the context of future changes in its value.

“Overall, it’s this idea that there’s a container, a box that holds a value, just like a variable,” he said. “But here’s where things get really dope: That variable, when the value internally changes, it can signal out to anyone who’s been listening, so anyone in the context who cares about that value, it can send a signal — you see what we did there? I know I’m sorry, dad jokes — it can send the signal out and let you know that the data has changed.”

This opens up new possibilities for fine-grained interactions and reactivity in Angular.

Before Signals, if developers wanted to keep track of when a first or last name changed, the developer would have to write code to make it critical, declarative and reactive. Now, if a developer wants to use this in a template that gets written to the user, the developer can just use the name of the signal and then use the parentheses, which show exactly how to intone it to get the value inside, he said.

### Angular’s Computed Component

Computed derives a new value when one of the dependent signals change, he said.

“A computed is just a signal, where if you have more than one signal that you’re referencing, or even the signal that you’re referencing and you’re deriving the value, meaning the value of the computed is based on the internal signals, you can get an update,” he said. “Now that seems a little complex.”

He shared what the code for computed might look like if the full name of a user or customer needed to update.

[![Computed Component code sample](https://cdn.thenewstack.io/media/2024/08/3984b5f5-component-one.jpg)

Zoom



](https://cdn.thenewstack.io/media/2024/08/3984b5f5-component-one.jpg)

Screenshot via Mark Thompsons’ presentation

[![Computed component code sample continued](https://cdn.thenewstack.io/media/2024/08/3db809d7-computed-two.jpg)

Zoom



](https://cdn.thenewstack.io/media/2024/08/3db809d7-computed-two.jpg)

Screenshot via Mark Thompson’s presentation

“If the first and last name update, we want the full name to update, so that’s where computed can really help you, and in the template, we use the same syntax,” he added.

### Angular’s Effect Component

An effect is a side-effectful operation that reads the value of zero or more signals, so it’s another part of the Signals story, Thompson explained.

“What this does is \[it\] lets you say, ‘I want to keep track of these signals, and if one of these changes I want to perform the action, maybe I want to make an API call, maybe I want to `console.log` some value, but I want to perform an action,” he said. That’s what we’re doing here. So inside this effect, function as highlighted.”

[![Angular effect component code sample](https://cdn.thenewstack.io/media/2024/08/97adf30f-effectangular.jpg)

Zoom



](https://cdn.thenewstack.io/media/2024/08/97adf30f-effectangular.jpg)

Screenshot via Mark Thompson’s presentation

## Better Lazy Loading

When it comes to performance, Angular added lazy loading at the template. For example, in an app with a recommended movie section component that has to make some data calls, the developer doesn’t want the component to call unless the user clicks a load button.

“We want to interact with this button and then trigger the loading of that component. Well, here’s how you can do it, with our first syntax. Now, this is not at the router level. This is at the template level,” he said, showing an example of that code.

When the button is clicked, the app will load the recommended movies.

“This means the JavaScript will be sent from the server to the client only at this time. But what about when you’re waiting? Fine, here’s what you should render,” he said. “What about if something goes wrong? This is what you should render, and then what about if I want a placeholder before I start loading just to let people know that something could go here? All right, then you got a placeholder. Now this is at the template level, and we think this is a good idea that’s going to help developers build things.”

He added that developers will probably find more frameworks implementing this fine-grained lazy loading, but Angular wanted to “take this to your wildest dreams,” so developers can do custom triggers that define what happens based on the data.

Bill.com was able to reduce their bundle size by 50% because they were able to defer parts of the application that were not needed, which made the performance much faster for the users, he said.

## Coming Soon: Partial Hydration

Hydration is what makes it possible for users to get an impression of a web page immediately, rendering images and texts before the interactions arrive, he said. To simplify hydration, Angular has made it a one-line piece of code to include hydration in an application, he added.

[![One line hydration code in Angular](https://cdn.thenewstack.io/media/2024/08/4355dee6-onelinehydrationangulr.jpg)

Zoom



](https://cdn.thenewstack.io/media/2024/08/4355dee6-onelinehydrationangulr.jpg)

Screenshot via Mark Thompson’s presentation

Hybrid rendering means using things like hydration to support the render process, he continued.

“We saw one Angular customer \[who\] saw a 72% reduction in the LCP, which is the largest contentful paint, after switching to hybrid rendering,” he said.

He also revealed that Angular is working on partial hydration. [Partial Hydration lets developers selectively add interactivity to a static](https://thenewstack.io/astro-revs-up-static-sites-with-partial-hydration/) app, improving frontend performance while keeping the benefits of client-side apps. Angular is solving this with Event Replay, a feature of its [internal Wiz framework](https://thenewstack.io/google-angular-lead-sees-convergence-in-javascript-frameworks/).

“What this means that when you click on this button, we’re caching those events, and then we’re going to replay them as soon as the interactivity is available,” he said. “This is really nice integration, and we think it’s going to really make things special for people.”

## AI Apps

Angular is also exploring adding AI to applications in meaningful ways as a means to serve developers, not replace them, he said. Specifically, the team sees a use for AI for tasks that are beyond a human’s scale, simplifying coding elements and generating dynamic applications based on data.

He attempted to demo an app that could be used to help practice a language in any [language by leveraging Gemini](https://thenewstack.io/exploring-the-api-of-googles-gemini-language-model/), but something went wrong with the demo. The [code is available on GitHub](https://github.com/google-gemini/angular-language-learning-sample), however.

“With Gemini, we’re doing structured output so that you can not only set the [MIME type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types), but you can also do things like set a schema,” he said. “I can actually define a schema, kind of like Zod with TypeScript, and provide the schema and let it know, hey, this is what it should look like.”

[Zod](https://github.com/colinhacks/zod) is a TypeScript-first schema declaration and validation library.

Group Created with Sketch.
