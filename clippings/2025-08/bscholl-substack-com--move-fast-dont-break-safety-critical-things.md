---
url: "https://bscholl.substack.com/p/move-fast-and-dont-break-safety-critical?utm_source=tldrnewsletter"
captured_at: "2025-08-13T09:31:35+01:00"
title: "Move fast and don't break (safety critical) things"
domain: "bscholl-substack-com"
---

---
_First in a series on lessons learned at Boom on how to develop hardware quickly and efficiently_

[

![](https://substackcdn.com/image/fetch/$s_!Q_Nf!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffed7d397-b45d-4061-841a-672abeb2b23d_6636x4424.jpeg)

](https://substackcdn.com/image/fetch/$s_!Q_Nf!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffed7d397-b45d-4061-841a-672abeb2b23d_6636x4424.jpeg)

XB-1 is the world’s first independently-developed supersonic jet, breaking the sound barrier for the first time in January, 2025. It was designed, built, and flown successfully by a team of just 50 people—compared to the hundreds or even thousands that would have been employed by a traditional big aerospace company. And we did this with roughly a tenth of the budget that would traditionally be required.  People have marveled at how our small team of just 50 people at Boom designed, built, and successfully flew the XB-1, the world’s first independently developed supersonic jet. And we did this with about a tenth the capital as any other supersonic program.

Yet, reflecting on our journey, we realized if we’d known from day one what we know now, we probably could have built XB-1 three times faster for a third of the budget. We're carefully harvesting these development lessons learned for the Overture airliner and the Symphony engine—and our goal is to make both the most efficient large aircraft and engine developments ever.

How? Of course, foundational elements like assembling a small, exceptional team were key—but there are some non-obvious lessons learned. Beneath each of these is an underlying design philosophy that values _iteration_—and seeks to reduce the cost of iteration, allowing us to get to hardware faster and improve our designs quickly.

In this initial post, we'll dive deep into the first critical lesson: how we build our own engineering software, deploying software engineers into hardware engineering teams.

Most aerospace design tools and practices are stuck in the 1990s—with lots of custom engineering trapped in Excel spreadsheets and laborious handoffs from engineer to engineer. If something changes, re-running analyses becomes expensive and time-consuming, severely limiting the ability to iterate rapidly.

At Boom, every engineer is expected to code and to leverage AI. We've taken the unconventional approach of embedding software engineers—typically with high curiosity but little or no aerospace experience—directly within our hardware teams.

The culture of these teams is critical, based around a philosophy we call "invent together." The software engineers are expected to learn the hardware discipline they're supporting and build tools that automate design workflows. Similarly, the hardware engineers are expected to learn to code and contribute engineering code within software frameworks. The central goal is to reduce cost of each engineering iteration and make engineering analysis easily repeatable. Additionally, we build software engineering best practices—like automated unit testing and continuous integration—into our hardware development workflows.

This close approach gave rise to mkBoom, our proprietary airplane design software. Initially created in a simpler form for XB-1, mkBoom has evolved significantly and is now pivotal to designing our Overture airliner.

[

![](https://substackcdn.com/image/fetch/$s_!ZYVR!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8186e271-c7cd-4fab-8f9d-3574ca7ffeb7_2214x1202.png)

](https://substackcdn.com/image/fetch/$s_!ZYVR!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8186e271-c7cd-4fab-8f9d-3574ca7ffeb7_2214x1202.png)

mkBoom fully automates whole aircraft level design analysis, including weights, propulsion, and aerodynamics. We can literally define an airplane parametrically in a configuration file and press a button. In a matter of minutes we have a complete quick-and-dirty analysis of how the whole aircraft performs—as mkBoom flies the aircraft through a full simulated mission (takeoff, climbout, acceleration, cruise, descent, landing). Overnight, mkBoom can run higher-fidelity simulations for a more exact understanding of performance. As our engineering code gets more sophisticated, better engineering analysis methods are integrated into mkBoom. 

This approach dramatically speeds engineering, allowing small teams to accomplish quickly what previously would have taken large teams and radically more time. 

But the real magic isn't the time savings—it's sort of a Jevon's Law of engineering: when engineering iteration is quick and cheap, many more designs can be evaluated and a much better design can be discovered. mkBoom doesn't just allow us to design faster—it allows us to explore designs we otherwise couldn’t afford to, resulting in a dramatically better Overture.

In fact, the passenger experience onboard Overture will be wildly better because of mkBoom. 

About 18 months ago, industrial designers working on Overture's passenger experience had a breakthrough. For the first time, they had figured out how to put a remarkable seating concept (still a closely held secret) into a skinny, narrowbody supersonic jet. But there was a catch: it required a subtle fuselage re-shaping to add a few inches of space in critical places... and our estimates these changes would cost a catastrophic 1,000 miles of range. Overture needed 4,000+ miles of range to service key routes, and we couldn’t afford to lose 1,000 miles. It looked like it might not work out.

But as passengers ourselves, we all yearned for the better cabin. So we challenged ourselves to find a way. We needed to recover the 1,000 miles in lost range.

By this time, our in-house Symphony engine efforts were in full swing, and we'd developed the ability to jointly simulate both Overture and Symphony inside mkBoom.

A supersonic airplane and supersonic engine are both made of countless design choices. Should the engine fan be bigger or smaller? Should the core be bigger or smaller? Should the wing have more sweep or less? Each of these design choices has ramifications throughout the flight profile. For example, a larger fan will be quieter at takeoff but less fuel efficient at cruise. A larger core will have more powerful transonic thrust—meaning the airplane will spend less time punching through the sound barrier, where drag is the highest—but this comes at the expense of increased weight. It's essentially impossible to tell which design choices lead to the best overall airplane without testing many combinations.

Traditionally, airplanes and engines are made by different companies... making extensive airplane/engine joint design iteration practically impossible. But since Boom designs both airplane and engine, we went for it. 

[

![](https://substackcdn.com/image/fetch/$s_!gAAY!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d1fa0f5-15e5-440a-9c73-7192ee678e15_2260x674.png)

](https://substackcdn.com/image/fetch/$s_!gAAY!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d1fa0f5-15e5-440a-9c73-7192ee678e15_2260x674.png)

Last year, we evaluated multiple subtle engine variations—adjusting fan sizes, core dimensions, etc.—and with mkBoom digitally flew each variant through a complete "mission:" takeoff, transonic acceleration, supersonic cruise, descent, and landing. Remarkably, within just two weeks, we'd found a counterintuitive but much better design, which significantly improved overall efficiency. Symphony's fan shrank modestly while its core increased in size, while we were able to maintain enough acoustic margin for quiet takeoff and landing. Together with a few other optimizations, these tweaks yielded over 1,000mi in increased range—enough that we could now afford a remarkable passenger cabin without sacrificing fuel efficiency or range.

It turns out these same design optimizations are the ones that unlock [Boomless Cruise](http://boomsupersonic.com/boomless-cruise) on Overture—the smaller fan and larger core perform better transonically, allowing Overture to break the sound barrier at a high enough altitude to enable boomless flights.

The magic of software has compounding effects within our engineering team. Great tools reduce rote engineering work, making jobs more enjoyable. Because we don’t need a ton of people, we can be much more selective in our hiring—building small but mighty teams that are fun to be part of. 

If you're a software engineer who would love to build an airplane, we're hiring. [Apply here](https://job-boards.greenhouse.io/boomsupersonic/jobs/5537577004).
