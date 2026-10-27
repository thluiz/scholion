---
url: "http://blog.8thlight.com/micah-martin/2013/05/28/performing-code-katas.html"
captured_at: "2013-05-30T21:01:12-03:00"
title: "Performing Code Katas | 8th Light"
domain: "blog-8thlight-com"
---

# **P**erforming Code Katas

*Coauthored by [Kelly Steensma](http://telladifferentstory.tumblr.com/)*

Wikipedia defines a kata as a detailed choreographed pattern of movement**.** Based on the Japanese word meaning "form", katas were originally used to preserve, perfect and pass down fighting techniques to martial artists of younger generations**.**

From a software development perspective, we use katas to build muscle memory, practice logical thought and teach ourselves familiar ideas but from a different perspective**.** Katas can stretch our abilities and, similar to how a kata would teach a martial artist to become comfortable with the uncomfortable, they help us write code we may not normally write**.**

Here at 8th Light, we consider katas to be an integral discipline of a craftsman**.** Mike Ebert, an 8th Light craftsman, often uses katas to warm up before starting his work for the day and will occasionally use them to take a step back and gain clarity when working through a complex problem**.**

Although katas are typically practiced in a private setting, at 8th Light we often perform katas, once perfected, live in front of an audience of peers**.** The goal of the kata performance, in this instance, is not to be considered a rite of passage or to demonstrate mastery of the material**.** Instead, as its name implies, it is simply a performance meant to entertain**.**

## Guidelines for Performing Katas

While there are no hard and fast rules as to what dictates a kata performance, here are some guidelines to consider:

1. Kata performances should last between five and ten minutes**.** Five minutes is an ambitiously small amount of time to get functional code that conveys a theme**.** If you can do it, great**!** Nevertheless, 7+ minutes may be a more realistic estimate**.** If your kata goes much over ten minutes, your audience may find it hard to resist the urge to write code themselves**.**
2. Your performance should include an introduction and conclusion**.** Before you begin your performance, stand up and announce your name and your kata (e**.**g., "I’m Micah Martin and I’m presenting Langton's Ant in Ruby**.**"). This is important**.** Your audience needs to know what to expect. To conclude the performance, repeat your introduction with a convincing salutation - "Thank you my fellow craftsmen**.** I’m Micah Martin and this was Langton's Ant in Ruby**.**" It is important to close with this information since, after ten minutes of mind-blowing code, your viewer may have forgotten your introduction**.** In addition to your introduction and conclusion, in the martial arts realm, you would accompany each event with a bow**.** Although people in the software realm find this unusual, I still do it**.**
3. Make sure your font is large enough for everyone in the audience to see, but avoid scrolling if at all possible**.** While seemingly an innocuous detail, font size can easily ruin the most adept performance**.** This can be easily remedied by allowing yourself time to perform a "mic check" beforehand with the projector or monitor you will be using**.**
4. In my experience, the best color combination for a live performance is a white background with black text**.** Avoid a black background if at all possible. Many text editors and terminal applications have preset and customizable themes**.** Consider creating a customized "presentation" theme that you can use at the time of your performance**.** This will not only save you time, but give you one less thing to worry about**.**
5. Type fast in order to maintain your audience's attention**.** It is painful to w-a-t-c-h s-o-m-e-o-n-e t-y-p-e s-l-o-w-l-y**.** Spare your audience the aggravation. Software craftsmen should be able to type fast**.** Use the kata performance as an opportunity to improve your typing speed**.**
6. Strive for perfection. A perfect kata performance would have no typographical errors**.** That said, during your performance, know that a viewer will generally overlook the occasional mistyped letter**.** Find a good typing pace; rushing to get through a performance may only increase your rate of typing errors**.**
7. While copy and paste are shortcuts we use in our everyday work, avoid using this functionality during your performance**.** Autocomplete is acceptable as well as tools like templates and macros, but only if you build the templates and macros during your live performance**.**
8. Avoid using a mouse or trackpad**.** The mouse will almost always slow you down and the time it takes you to move your hand from the keyboard to the mouse is enough time to lose your viewers' attention**.** Learn the keyboard shortcuts for everything including changing application focus and drop-down menu commands**.** Reserve the mouse for dramatic effect only.
9. Each kata should contain a theme - a bite-sized lesson the viewer can take away from the performance**.** There are a plethora of themes to choose from and can be anything from a demonstration of pattern matching in Elixir to [adding functional composition to an HTTP sever written in Clojure](https://vimeo.com/61701111) **.** Keep it simple and limit yourself to only one theme and, remember, it is not so much about the solution to the problem, but about the process and steps you take to get to the solution**.**
10. While there are a number of very popular katas scattered across the Internet, know that anything can be the subject of a kata**.** Joshua Cheek, another 8th Light craftsman, performed a [StringScanner kata](https://vimeo.com/29823879)  during his resident apprenticeship demonstrating the strscan method in Ruby and then crafted his own method emulating the existing functionality**.** Although Joshua's intended theme of beginning from acceptance tests was interesting, an equally noteworthy theme emerged - his advanced use of TextMate**.**
11. During the performance, the code, tests and test executions (i**.**e., the terminal window) should be visible on the screen at all times**.** Although you have probably seen your code and test failures countless times, your viewer has not**.** Switching back and forth between applications may confuse viewers**.**
12. Katas can be built in their entirety from scratch or may leverage an existing codebase**.** Starting a kata performance from a blank slate, although impressive, may not always be an option depending on your theme**.**
13. Decide whether you are going to speak or play music during the performance**.** If you intend to speak, avoid explaining every line of code**.** Talking should be used as a tool to grab the viewer's attention and highlight a significant action related to the kata's theme**.** Avoid phrases like "So, now that my loop is in place..**.**" and instead express yourself through assertive phrases like, "Now you will see me do this**.**"

    Alternatively, you may play music but avoid using it as just background noise**.** Instead, you should use the music to emphasize the kata's theme and complement the flow of the performance**.** Music should be considered an advanced tool. If you've timed your performance to coordinate with the music, making a mistake could disrupt the entire presentation**.**

    Silence is a third option and can set an interesting tone**.** However, it can be challenging to pull off. At times, silence can convey a sense of calm if the speaker has a strong demeanor, but it can also communicate insecurity**.** Silence can be risky, so talking may be preferred for inexperienced performers**.**
14. Above all, your technique should be flawless**.** If you plan to use test-driven design, it should be model test-driven design**.** If you're demonstrating a new programming language, you should use the conventional techniques of that language**.**

Throughout my career, I have performed katas as a means to sharpen my skills and push myself to think in different ways**.** Typically, I do not have a theme in mind when starting a new kata**.** The theme will often emerge just simply through the act of solving the problem**.** I often practice my kata dozens of times before performing it**.** However, I am not atypical and sometimes find it difficult to fit time into my schedule to practice**.** Scheduling a live kata performance gives me the extra push I need to practice more**.**

## An Example

I want to share a kata that was recently performed at 8th Light by Sandro Padin, one of our resident apprentices**.** The kata is Fizzbuzz in Clojure and highlights many of the points I have detailed above**.** The theme for Sandro's kata was top-down design.

Sandro's clever display of the theme was what I found most appealing about his performance**.** Based on the reaction of the audience, I have a hunch that the initial two tests grabbed viewers' attention and left them feeling confused but, yet, intrigued**.**

The music was an excellent choice and complemented the flow of the kata perfectly**.** While setting up his environment and the initial two tests, the music was mellow and had a continuous, steady beat**.** Just as his first real test passed (at the 3:05 mark), the tempo of the music picked up and the entire beat changed**.** It was as if to say, "Now, he's on to something!"

This coupling of music and theme continued for the remainder of the performance**.** At the 4:05 mark, Sandro was just beginning to refactor his test suite when the music's mood changes**.** This happened again at the 5:55 mark when he retries the original two tests with success**.** And, as if it were the finale of the performance, at the 6:30 mark the music's tempo changed in effect highlighting the success of the final test**.**

As the music dies down one final time, he runs the newly completed program, exits the text editor and deletes the code as if it were just another practice session**.** To close the performance, the terminal screen is cleared and the music fades for dramatic effect**.**

While I found Sandro's kata to be a compelling performance, one thing that did detract from it was the lull from the 4:00 to 5:00 minute mark when he refactored his test suite**.** The refactoring of the tests was unrelated to the theme and could have been omitted**.** The second test could have also been omitted as I found it to be a bit redundant**.**

## In Closing

It occurred to me the other day that music, in some aspects, can be likened to that of a kata performance**.** Most songs have similar features**.** They typically last three to five minutes; they often include a bridge and a chorus**.** Yet, the impact of songs varies immensely**.** While some songs are released to little fanfare, others will receive wide acclaim and be remembered, enjoyed and recognized for a lifetime**.**

Similar to this notion, I have seen kata performances that inspire and motivate me and I will remember them for a lifetime**.** Notwithstanding, I have seen many others that do none of those things**.** My goal in writing this blog post is to create a common set of standards that, not only raise the bar for kata performances in general, but also inspire us to give performances that we will reflect on for a lifetime**.**

![a146b5b836216c379de1b337d5af26fb.jpg](blog-8thlight-com--performing-code-katas/a146b5b836216c379de1b337d5af26fb.jpg)

[Micah Martin](http://www.8thlight.com/our-team/micah-martin) 
is co-founder of 8th Light and is known for his open source work such as
FitNesse, Limelight, Joodo, and Speclj**.**

[↑ Back to top](#blog)
