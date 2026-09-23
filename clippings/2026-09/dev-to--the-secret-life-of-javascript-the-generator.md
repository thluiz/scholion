---
url: "https://dev.to/aaron_rose_0787cc8b4775a0/the-secret-life-of-javascript-the-generator-1fi5?context=digest"
captured_at: "2026-09-23T14:22:04+01:00"
title: "The Secret Life of JavaScript: The Generator - DEV Community"
domain: "dev.to"
---

Aaron Rose

Posted on Feb 1

28
2
4
2
2
The Secret Life of JavaScript: The Generator
#
javascript
#
coding
#
programming
#
softwaredevelopment

How to pause, resume, and control the flow of execution.

Timothy was staring at a frozen screen. He forced a reload, but he looked defeated.


function createIds() {
    let i = 0;
    while (true) {
        return i++; // This doesn't work like I want...
    }
}
// He wanted a new ID every time he called it.
// Instead, he got "0" every time.



"I'm trying to create a system that generates unique IDs forever," Timothy explained. "But if I use a loop, it hangs the browser. If I don't use a loop, the variable resets every time I call the function."

Margaret pulled up a chair. "You are running into the Run-to-Completion rule," she said.

"Normal functions are like a sprint," she continued. "Once they start, they cannot stop until they finish. You need a function that can pause."

The Asterisk

Margaret wrote a new symbol on the board.


function* createIds() { ... }



"This is a Generator Function," she said. "Notice the asterisk (*). This tells the engine that this function behaves differently. It doesn't run straight through. It yields control back to you."

The yield Keyword

She rewrote Timothy's code using the new syntax.


function* createIds() {
    let i = 0;
    while (true) {
        yield i++;
    }
}



"Wait," Timothy said. "You still have while(true). Won't that crash the browser with an infinite loop?"

"No," Margaret smiled. "Because of yield. When the engine hits yield, it pauses the function completely. It saves the variable i, steps out of the function, and gives the value to you. The loop effectively freezes in time."

The Packet: { value, done }

Timothy looked at the code. "So how do I un-freeze it?"

"A Generator doesn't return a value directly," Margaret explained. "It returns a Generator Object. You control that object using .next()."

She wrote the usage code, but this time she showed the full output.


const idGenerator = createIds(); // The function is "ready", but hasn't started.

console.log(idGenerator.next()); 
// Output: { value: 0, done: false }
// The function ran, hit 'yield 0', and paused.

console.log(idGenerator.next()); 
// Output: { value: 1, done: false }
// It woke up, incremented 'i', and paused again.



"It returns a packet," Margaret said. "Value is what you asked for. Done tells you if the function has finished running. Since we are in an infinite loop, done will always be false."

The Iterator Protocol (for...of)

"Do I always have to drive it manually?" Timothy asked.

"Not at all," Margaret said. "Because Generators follow the standard Iterator Protocol, you can drop them right into a for...of loop."


for (const id of createIds()) {
    console.log(id);
    if (id > 5) break; // We stop the infinite loop externally!
}



"This is Lazy Evaluation," she added. "We aren't creating a million IDs in memory. We are creating them one by one, only when the loop asks for them."

Two-Way Communication

"It gets even more interesting," Margaret added. "You can also pass data back into the function when you resume it."

She modified the example to accept a reset command.


function* createIds() {
    let i = 0;
    while (true) {
        const reset = yield i++; // We receive data here
        if (reset) {
            i = 0;
        }
    }
}

const gen = createIds();
console.log(gen.next().value); // 0
console.log(gen.next().value); // 1
console.log(gen.next(true).value); // 0 (We sent "true" back in!)



Timothy watched the output. "So I'm having a conversation with the function. I ask for a value, it gives one and waits. I ask again, it continues."

The Conclusion

Timothy looked at his infinite loop. It was no longer a browser-killer; it was a useful tool.

"I always thought functions were strict," Timothy said. "Start, run, finish."

"Most are," Margaret agreed. "But Generators give you control over Time. You decide when the code moves forward."

"And if you think pausing sync code is cool," she whispered, "wait until you see Async Generators handling network requests. But that is a story for another day."

Aaron Rose is a software engineer and technology writer at tech-reader.blog and the author of Think Like a Genius.

DEV Community

Work through these 3 parts to earn the exclusive Google AI Studio Builder badge!

This track will guide you through Google AI Studio's new "Build apps with Gemini" feature, where you can turn a simple text prompt into a fully functional, deployed web application in minutes.

Read more →

Read More
Top comments (13)
Subscribe
Submit
Preview
 
 
Charan Koppuravuri
•
Feb 1

🔥 Spot-on teaching. Generators = controlled execution suspension.

Real production use (from building LLM frameworks):


js
function* createRecoveryPointIds() {
  let timestamp = Date.now();
  let sequence = 0;
  while (true) {
    yield `rpe_${timestamp}_${sequence++}`;
    if (sequence > 999) {
      timestamp = Date.now();
      sequence = 0;
    }
  }
}

// Usage in ETL pipeline
const idGen = createRecoveryPointIds();
for (const record of recoveryPoints) {
  record.id = idGen.next().value; // Non-blocking ID stream
}

4
 likes
Like
Reply
 
 
Aaron Rose 
•
Feb 1

✨💯❤️

2
 likes
Like
Reply
 
 
Bhavin Sheth
•
Feb 1

Really enjoyed this — the way you explain generators as "pausing time" makes a tricky concept feel simple and practical. The ID example is super relatable and the two-way communication part clicked instantly for me.

2
 likes
Like
Reply
 
 
Aaron Rose 
•
Feb 1

❤🙏

2
 likes
Like
Reply
 
 
PEACEBINFLOW
•
Feb 1

This was a really enjoyable read.

I like how you framed generators as a shift in how time works rather than just another JS feature. That "run-to-completion vs pause and resume" distinction is one of those things that quietly changes how you think about programs once it clicks.

The ID example is perfect too — it's simple, but it exposes a real mental model gap. A lot of people try to solve problems like this by reaching for more state or globals, when the real issue is that normal functions just don't give you control over execution flow.

The "conversation with the function" line is especially good. That's exactly how generators feel once you get comfortable with them — not just yielding values, but passing intent back in. It makes things like lazy iteration and controlled infinite sequences feel way less magical and way more deliberate.

Also appreciate that you showed for...of and the iterator protocol instead of leaving generators in the "weird syntax corner." That's usually the moment where people realize this isn't a niche trick, it's a core language concept.

Solid explanation overall. Definitely one of those posts that makes a feature stick instead of just explaining it.

2
 likes
Like
Reply
 
 
Aaron Rose 
•
Feb 1

❤️🙏

1
 like
Like
Reply
 
 
Muhammad Ahmad
•
Feb 3

In the start you mentioned to create a system to creat unique IDs forever but this system will not always generate unique IDs. It will initialize from start once the server restarts or program is being executed again.

2
 likes
Like
Reply
 
 
Martí Serra Molina
•
Feb 1

Really liked this article! I knew about the iterator pattern but not using this approach! I will keep this in mind in case I ever need to create an iterator.

2
 likes
Like
Reply
 
 
Aaron Rose 
•
Feb 1

❤🙏✨

2
 likes
Like
Reply
 
 
Arc
•
Feb 1

I've written JS for 9 years, wrote sync generator only less than 5 times.

2
 likes
Like
Reply
 
 
Benjamin Nguyen
•
Feb 1

Great explaining, Aaron! I enjoy you and other people article. They are so easy to follow and understand.

2
 likes
Like
Reply
 
 
Aaron Rose 
•
Feb 1

🙏❤️✨

2
 likes
Like
Reply
View full discussion (13 comments)
Code of Conduct • Report abuse
