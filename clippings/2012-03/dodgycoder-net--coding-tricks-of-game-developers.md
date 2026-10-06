---
url: "http://www.dodgycoder.net/2012/02/coding-tricks-of-game-developers.html"
captured_at: "2012-03-17T03:36:50-03:00"
title: "Dodgy Coder: Coding tricks of game developers"
domain: "dodgycoder-net"
---

### Coding tricks of game developers

If you've got any real world programming experience then no doubt at some point you've had to resort to some quick and dirty fix to get a problem solved or a feature implemented while a deadline loomed large. Game developers often experience a horrific "crunch" (also known as a "death march"), which happens in the last few months of a project leading up to the game's release date. Failing to meet the deadline can often mean the project gets cancelled or even worse, you lose your job. So what sort of tricks do they use while they're under the pump, doing 12+ hour per day for weeks on end?  
  
Below are some classic anecdotes and tips - many thanks to [Brandon Sheffield](http://www.gamasutra.com/view/authors/543/Brandon_Sheffield.php) who originally put together [this article](http://www.gamasutra.com/view/feature/4111/dirty_coding_tricks.php) on Gamasutra. I have reposted a few of his stories and also added some more from newer sources. I have also linked on each story to the author's home page or blog wherever possible.  
  
1. The programming antihero - [Noel Llopis](http://gamesfromwithin.com/)  
  
I was fresh out of college, still wet behind the ears, and about to enter the beta phase of my first professional game project -- a late-90s PC title. It had been an exciting rollercoaster ride, as projects often are. All the content was in and the game was looking good. There was one problem though: We were way over our memory budget.  
  
Since most memory was taken up by models and textures, we worked with the artists to reduce the memory footprint of the game as much as possible. We scaled down images, decimated models, and compressed textures. Sometimes we did this with the support of the artists, and sometimes over their dead bodies.  
  
We cut megabyte after megabyte, and after a few days of frantic activity, we reached a point where we felt there was nothing else we could do. Unless we cut some major content, there was no way we could free up any more memory. Exhausted, we evaluated our current memory usage. We were still 1.5 MB over the memory limit!  
  
At this point one of the most experienced programmers in the team, one who had survived many years of development in the "good old days," decided to take matters into his own hands. He called me into his office, and we set out upon what I imagined would be another exhausting session of freeing up memory.  
  
Instead, he brought up a source file and pointed to this line:  
  
static char buffer[1024\*1024\*2];  
  
"See this?" he said. And then deleted it with a single keystroke. Done!  
  
He probably saw the horror in my eyes, so he explained to me that he had put aside those two megabytes of memory early in the development cycle. He knew from experience that it was always impossible to cut content down to memory budgets, and that many projects had come close to failing because of it. So now, as a regular practice, he always put aside a nice block of memory to free up when it's really needed.  
  
He walked out of the office and announced he had reduced the memory footprint to within budget constraints -- he was toasted as the hero of the project.  
  
As horrified as I was back then about such a "barbaric" practice, I have to admit that I'm warming up to it. I haven't gotten into the frame of mind where I can put it to use yet, but I can see how sometimes, when you're up against the wall, having a bit of memory tucked away for a rainy day can really make a difference. Funny how time and experience changes everything.  
  
2. Cache it up - [Andrew Russell](http://gamedev.stackexchange.com/users/288/andrew-russell)  
  
To improve performance when you are processing things in a tight loop, you want to make the data for each iteration as small as possible, and as close together as possible in memory. That means the ideal is an array or vector of objects (not pointers) that contain only the data necessary for the calculation.  
  
This way, when the CPU fetches the data for the first iteration of your loop, the next several iterations worth of data will get loaded into the cache with it.  
  
There's not really much you can do with using fewer and faster instructions because the CPU is as fast as its going to get, and the compiler can't be improved. Cache coherence is where it's at - [this article](http://supercomputingblog.com/optimization/taking-advantage-of-cache-coherence-in-your-programs/)  contains a good example of getting cache coherency for an algorithm that doesn't simply run through data linearly.  
  
3. Plan your distractions - [Jay Barnson](http://rampantgames.com/blog/?p=3881)  
  
The Internet is one of the greatest tools ever invented for both improving and destroying productivity. Twitter and forums and blogs and instructional websites can be extremely motivational and educational, but they can also be a distraction that completely destroys all hope of ever getting anything done. One thing I’ve done in the past which has proven pretty successful is to stick to a plan for when I can spend some minutes checking email and Twitter, or play a quick game or something. Either at the completion of a task, or after a period of time (say one five-minute break every hour). Otherwise, the browser’s only use is for reading reference manual pages, if necessary. That way I turn a potential distraction into a motivating tool.  
  
4. Collateral damage - Jim Van Verth ([@cthulhim](https://twitter.com/#%21/cthulhim))  
  
Don't know how many remember Force 21, but it was an early 3D RTS which used a follow cam to observe your current platoon. Towards the end of the project we had a strange bug where the camera would stop following the platoon -- it would just stay where it was while your platoon moved on and nothing would budge it. The apparent cause was random because we couldn't find a decent repro case. Until, finally, one of the testers noticed that it happened more often when an air strike occurred near your vehicles. Using that info I was able to track it down.  
  
Because the camera was using velocity and acceleration and was collidable, I derived it from our PhysicalObject class, which had those characteristics. It also had another characteristic: PhysicalObjects could take damage. The air strikes did enough damage in a large enough radius that they were quite literally "killing" the camera.  
  
I did fix the bug by ensuring that cameras couldn't take damage, but just to be sure, I boosted their armor and hit points to ridiculous levels. I believe I can safely say we had the toughest camera in any game.  
  
5. The blind leading the blind - [Maurício Gomes](http://blog.agfgames.com/)  
  
At university there was a team that made a FPS flash game. For some bizarre reason, the programmer, instead of checking if the character was colliding with the wall and stop you going there, he did the inverse, he checked if there was a wall, and only allowed you to move parallel to it!  
  
This sparked a bizarre bug: in crossings or T junctions in the level, you could not actually cross, only turn to the passage on your left or right. The deadline was closing, and they had no idea on how to fix it.  
  
Then the team writer fixed the issue; he told the artist to add an animation of hands touching the walls, and then he added in the background story that the main character was blind and needed to constantly touch the walls to know where he was going.  
  
6. You wouldn't like me when I'm angry - [Nick Waanders](http://www.nickwaanders.com/)  
  
I once worked at THQ studio Relic Entertainment on The Outfit, which some may remember as one of the earlier games for the Xbox 360. We started with a PC engine (single-threaded), and we had to convert it to a complete game on a next-gen multi-core console in about 18 months. About three months before shipping, we were still running at about 5 FPS on the 360. Obviously this game needed some severe optimization.  
  
When I did some performance measurements, it became clear that as much as the code was slow and very "PC," there were also lots of problems on the content side as well. Some models were too detailed, some shaders were too expensive, and some missions simply had too many guys running around.  
  
It's hard to convince a team of 100 people that the programmers can't simply "fix" the performance of the engine, and that some of the ways people had gotten used to working to needed to be changed. People needed to understand that the performance of the game was everybody's problem, and I figured the best way to do this is with a bit of humor that had a bit of hidden truth behind it.  
  
The solution took maybe an hour. A fellow programmer took four pictures of my face -- one really happy, one normal, one a bit angry, and one where I am pulling my hair out. I put this image in the corner of the screen, and it was linked to the frame rate. If the game ran at over 30fps, I was really happy, if it ran below 20, I was angry.  
  
After this change, the whole FPS issue transformed from, "Ah, the programmers will fix it." to, "Hmm, if I put this model in, Nick is going to be angry! I'd better optimize this a little first." People could instantly see if a change they made had an impact on the frame rate, and we ended up shipping the game at 30fps.  
  
7. Its not a bug, its a feature! - [Philip Tan](http://gamedev.stackexchange.com/users/305/philip-tan)  
  
I worked on an RPG in which we were trying to get the NPCs (Non-player Characters) to spot when you were in range, walk up to you, and strike up a conversation with you by activating the dialog system.  
  
We forgot to add code to distinguish NPCs from PCs (Player Characters), so we'd walk into town and all the NPCs would be talking with each other. Because all NPC AI code used the same dialog template, they actually got a few sentences in before the conversations became nonsensical. And because character dialog was broadcast, you could read everything they said if you were in range.  
  
We decided to turn that bug into a major feature.  
  
8. Dirty deeds - Tim Randall (Developer @ [Encore](http://www.encore.com/) )  
  
The engine team at Gremlin Interactive used to keep a single glove in their office. When someone asked why it was there, they were told it was only used when someone was about to type some really dirty code. It wasn't so much a case of not wanting to leave fingerprints but rather not wanting to actually touch the dirtiest fixes!  
  
9. Explicit conditional hinting - [ZorbaTHut](http://www.mandible.net/)  
  
A very, very low-level tip, but one that can come in handy... most compilers support some form of explicit conditional hinting. GCC has a function called \_\_builtin\_expect which lets you inform the compiler what the value of a result probably is. GCC can use that data to optimize conditionals to perform as quickly as possible in the expected case, with slightly slower execution in the unexpected case.  
  
if(\_\_builtin\_expect(entity->extremely\_unlikely\_flag, 0)) {  
  // code that is rarely run  
}  
  
I've seen a 10-20% speedup with proper use of this.  
  
10. Object-ive oriented programming - Anonymous  
  
Back at a game studio, I think it was near the end of the project, we had an object in one of the levels that needed to be hidden. We didn't want to re-export the level and we did not use checksum names. So right smack in the middle of the engine code we had something like the following:  
  
if( level == 10 && object == 56 )  
{  
    HideObject();  
}  
  
The game shipped with this in.  
  
Maybe a year later, an artist using our engine came to us very frustrated about why an object in their level was not showing up after exporting. The level they had a problem with resolved to level 10. I wonder why?  
  
11. Stack vs Heap - [Torbjörn Gyllebring](http://stackoverflow.com/users/21182/torbjorn-gyllebring)  
  
Stack allocation is much faster than heap allocation since all it really does is move the stack pointer. Using memory pools, you can get comparable performance out of heap allocation, but that comes with a slight added complexity and its own headaches.  
  
Also, stack vs heap is not only a performance consideration; it also tells you a lot about the expected lifetime of objects. The stack is always hot, the memory you get is much more likely to be in cache than any far heap allocated memory.  
  
Downside of the stack is that it is actually a stack. You can't free a chunk of memory used by the stack unless it is on top of it. There's no management, you push or pop things on it. On the other hand, the heap memory is managed: it asks the kernel for memory chunks, maybe splits them, merges thems, reuses them and frees them. The stack is really meant for fast and short allocations.  
  
12. I'm a programmer, not an artist - [Damian Connolly](http://divillysausages.com/)  
  
For indie / solo developers who are working on an iPhone or Android game on their own, while you're looking for an artist etc, you should be developing your game at the same time. Use programmer art, stand-ins, free sprites anything. Most of the time, before even thinking about final assets, I just want something up and running quickly to see if it's fun. Prototype the crap out of it and find the game. Then, when the gameplay's locked down, you can start putting in the proper art. Doing it the other way around leads to lost money, and work that needs to be redone multiple times, which aside from harming your project, sucks your motivation to finish it (and if you're making a game to get a job, showing that you can finish a project is a good thing). Another tip if you're lacking upfront finance is to find a freelance game artist who will accept a revenue sharing deal, e.g. typically something like 30% of game revenue, payable once it gets published to the AppStore.  
  
13. Remove unnecessary branches - [tenpn](http://gamedev.stackexchange.com/users/259/tenpn)  
  
On some platforms and with some compilers, branches can throw away your whole pipeline, so even insignificant if() blocks can be expensive.  
  
The PowerPC architecture (PS3/x360) offers the floating-point select instruction, fsel. This can be used in the place of a branch if the blocks are simple assignments:  
  
float result = 0;  
if (foo > bar) { result = 2.0f; }  
else { result = 1.0f; }  
  
Becomes:  
  
float result = fsel(foo-bar, 2.0f, 1.0f);  
  
When the first parameter is greater than or equal to 0, the second parameter is returned, else the third. The price of losing the branch is that both the if{} and the else{} block will be executed, so if one is an expensive operation or dereferences a NULL pointer this optimisation is not suitable. Sometimes your compiler has already done this work, so check your assembly first.  
  
14. Hack the stack - [Steve DeFrisco](http://stevedefrisco.com/)  
  
I was one of a few interns at IMAGIC in 1982-83. We were all doing Intellivision carts. One of the programmers had to leave to go back to school, and I was chosen to fix the random crash bug in his game. It turned out to be a stack overflow in the timer interrupt handler. Since the only reason for the handler was to update the \*display\* of the on-screen timer, I added some code to test the depth of the stack at the beginning of the interrupt routine. If we were in danger of overflowing the stack, return without doing anything. Since the handler was called multiple times per second, the player never noticed, and the crash was fixed.  
  
15. Meet my dog, "Patches" - [Mick West](http://www.gamasutra.com/view/authors/1181/Mick_West.php)  
  
There's an old joke that goes something like this:  
  
Patient: "Doctor, it hurts when I do this."  
Doctor: "Then stop doing it."  
  
Funny, but are these also wise words when applied to fixing bugs? Consider the load of pain I found myself in when working on the port of a 3D third person shooter from the PC to the original PlayStation.  
  
Now, the PS1 has no support for floating point numbers, so we were doing the conversion by basically recompiling the PC code and overloading all floats with fixed point. That actually worked fairly well, but where it fell apart was during collision detection.  
  
The level geometry that was supplied to us worked reasonably well in the PC version of the game, but when converted to fixed point, all kinds of seams, T-Junctions and other problems were nudged into existence by the microscopic differences in values between fixed and floats. This problem would manifest itself in one case with the main character touching a particular type of door in a particular level in a particular location; rather than fix the root cause of the problem, I simply made it so that if he ever touched the door, then I'd move him away, and pretend it never happened. Problem solved.  
  
Looking back I find this code quite horrifying. It was patching bugs and not fixing them. Unfortunately the real fix would have been to go and rework the entire game's geometry and collision system specifically with the PS1 fixed point limitations in mind. The schedule was initially aggressive, and since we always seemed close to finishing, the quick patch option won over against a comprehensive (but expensive) fix.  
  
But it did not go well. Hundreds of patches were needed, and then the patches themselves started causing problems, so more patches were added to turn off the patches in hyper-specific circumstances. The bugs kept coming, and I kept beating them back with patches. Eventually I won, but at a cost of shipping several months behind schedule, and working 14 hour days for all of those several months.  
  
That experience soured me against "the patch." Now I always try to dig right down to the root cause of a bug, even if a simple, and seemingly safe, patch is available. I want my code to be healthy. If you go to the doctor and tell him "it hurts when I do this," then you expect him to find out why it hurts, and to fix that. Your pain and your code's bugs might be symptoms of something far more serious. The moral: Treat your code like you would want a doctor to treat you; fix the cause, not the symptoms.  
  
16. Identity crisis - [Noel Llopis](http://gamesfromwithin.com/)  
  
This scene is familiar to all game developers: It's the day we're sending out the gold candidate for our Xbox 1 game. The whole team is playtesting the game all day long, making sure everything looks good. It's fun, it's solid, it's definitely a go in our minds.  
  
In the afternoon, we make the last build with the last few game-balancing tweaks, and do one last playthrough session when disaster strikes: The game crashes hard! We all run to our workstations, fire up the debugger, and try to figure out what's going on. It's not something trivial, like an assert, or even something moderately hard to track down, like a divide by zero. It looks like memory is garbage in a few places, but the memory reporting comes out clean. What's going on?  
  
One dinner and many hours later, our dreams of getting out on time shattered, we manage to track it down to one data file being loaded in with the wrong data. The wrong data? How's that possible? Our resource system boiled down every asset to a 64-bit identifier made out of the CRC32 of the full filename and the CRC32 of all the data contents. That was also our way of collapsing identical resource files into a single one in the game. With tens of thousands of files, and two years of development, we never had a conflict. Never.  
  
Until now, that is.  
  
It turns out that one of the innocent tweaks the designers had checked in that afternoon made it so a text file had the exact same filename and data CRC as another resource file, even though they were completely different!  
  
Our hearts sank to our feet when we recognized the problem. There's no way we could change the resource indexing system in such a short period of time. Even if we pulled an all-nighter, there was no way to know for sure that everything would be stable in the morning.  
  
Then, as quickly as despair swept over us, we realized how we could fix this on time for the gold candidate release. We opened up the text file responsible for the conflict, added a space at the end, and saved it. We looked at each other with huge grins on our faces and said:  
  
"Ship it!"  
  
The extra space meant the CRC32 checksum of the text file was altered and therefore no longer conflicted with the other resource.  
  
17. HexEdit to the rescue - [Ken Demarest](http://ken.demarest.com/bio/bio.html)  
  
Back on Wing Commander 1 we were getting an exception from our EMM386 memory manager when we exited the game. We'd clear the screen and a single line would print out, something like "EMM386 Memory manager error. Blah blah blah." We had to ship ASAP. So I hex edited the error in the memory manager itself to read "Thank you for playing Wing Commander."  
  
18. 8-bit audio stomper - [Toonse](http://news.ycombinator.com/user?id=toonse)  
  
For a launch product of a certain console I had a nasty bug report from QA that took 20+ hours to reproduce. Finally (with 24 hours left to go to hit console launch) tracked it down to some audio drivers in the firmware that were erroneously writing 1 random byte "somewhere" at random times where the "somewhere" was always in executable code space. I finally figured out that any given run of the game that "somewhere" was always the same place, luckily. 1st party said sorry, can't fix it in time as we don't know why it's being caused! So I shipped that game with stub code at the very start of main that immediately saved off the 1 byte from the freshly loaded executable in the place I knew it would overwrite for that particular version of the exe. There was then code that would run each frame after audio had run and restore that byte back to what it should be just in case it had been stomped that frame. Good times! We hit launch.  
  
To this day I still feel very very dirty about this hack, but it was needed to achieve the objectives and harmed no-one :)  
  
19. Rainy day server pool - [Potatolicious](http://news.ycombinator.com/user?id=potatolicious)  
  
I used to work for a company that had a horrific hardware requisition policy. If your team needed a server, it had to go through a lengthy and annoying approvals process - and even then, it took months before Infrastructure would actually provide said servers.  
  
In other words, when a project gets handed down from above to launch in, say, 3 months, there's no way in hell you can get the servers requisitioned, approved, and installed in that time. It became standard practice for each team to slightly over-request server capacity with each project and throwing the excess hosts into a rainy day pool, immediately available and repurposeable as required.  
  
New servers will still get requested for these projects, but since they took so long to approve, odds are they'd go right into the pool whenever they actually arrived, which sometimes took up to a year.  
  
Of course, it was horrifyingly inefficient. Just on my team alone I think we had easily 50 boxes sitting around doing nothing (and powered on to boot) waiting to pick up the slack of a horrendously broken bureaucracy.  
  
20. Bit shifting magic - [Steven Pigeon](http://hbfs.wordpress.com/)  
  
In order to avoid stalls in the processor pipeline due to branching, one can often use a branchless equivalent, that is, code transformed to remove the if-then-elses and therefore jump prediction uncertainties. E.g. a straightforward implementation of abs( ) in C might be  
  
inline int abs(int x)  
{  
    return (x<0) ? -x : x;  
}  
  
Which is simple enough but contains an inline if-then-else. As the argument, x, isn’t all that likely to follow a pattern that the branch prediction unit can detect, this simple function becomes potentially costly as the jump will be mispredicted quite often.  
  
How can we remove the if-then-else, then? One solution is to use the right shift operator (>>) and the bitwise XOR operator (^) as following:  
  
inline int abs\_no\_branch(int x)  
{  
  int m = (x >> (8 \* sizeof(int)-1));  
  return ((x ^ m) - m);  
}  
  
Where the expression (8 \* sizeof(int) - 1) evaluates to 15, 31, or 63 depending on the size of integers on the target computer.  
  
*Further detailed reading about this technique here: [Branchless Equivalents of Simple Functions](http://hbfs.wordpress.com/2008/08/05/branchless-equivalents-of-simple-functions/) .*  
  
[Follow @dodgy\_coder](http://twitter.com/dodgy_coder)  
  
[Subscribe to posts via RSS](http://www.dodgycoder.net/feeds/posts/default)
