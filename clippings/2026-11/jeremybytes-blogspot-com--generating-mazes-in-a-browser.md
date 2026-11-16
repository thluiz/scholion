---
url: "https://jeremybytes.blogspot.com/2020/01/generating-mazes-in-browser.html"
captured_at: "2026-11-16T02:27:44+00:00"
title: "Generating Mazes in a Browser"
domain: "jeremybytes-blogspot-com"
---

When the serious coding stuff gets too serious, I take a break and do something fun. This time, it's going back to my Mazes for Programmers project -- GitHub: [https://github.com/jeremybytes/mazes-for-programmers](https://github.com/jeremybytes/mazes-for-programmers).

This is a project based on code from the book _Mazes for Programmers_ by Jamis Buck ([Amazon link](https://www.amazon.com/Mazes-Programmers-Twisty-Little-Passages/dp/1680500554/)). I took the samples from the book (which are in Ruby) and made a C# project. You can see the articles listed on the [README.md](https://github.com/jeremybytes/mazes-for-programmers/blob/master/README.md) for the GitHub project.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEha8ODFA465i2ylClzNF7_uZOb99g0W_ZCKzARIGRrEFgsOL54rnYNsBdf4_edt_Z02aAcgtOeEFTk9WR7f8aaY_bXPofC_Jz-UxJaYeqFOPjVmMLyBF7Y_67wJ3AMMSC3myPxL8RIXquQ/s320/maze.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEha8ODFA465i2ylClzNF7_uZOb99g0W_ZCKzARIGRrEFgsOL54rnYNsBdf4_edt_Z02aAcgtOeEFTk9WR7f8aaY_bXPofC_Jz-UxJaYeqFOPjVmMLyBF7Y_67wJ3AMMSC3myPxL8RIXquQ/s1600/maze.png)

_Update: This article is about running the application. If you want to see how I built it, check out this article: [Building a Web Front-End to Show Mazes in ASP.NET Core MVC](https://jeremybytes.blogspot.com/2020/01/building-web-front-end-to-show-mazes-in.html)._

**Moving to .NET Core**  
The last time I wrote about this, I was working on converting the project to .NET Core (read about a bit of that here: [Converting .NET Framework to .NET Core -- UseShellExecute has a Different Default Value](https://jeremybytes.blogspot.com/2019/08/converting-net-framework-to-net-core.html)).

I managed to get the code working, but I wasn't happy with the solution. The application is a console application, but it uses a shell execute to display the bitmap version of the maze when it is done. In the prior article, I mention how this is fine for Windows, but there is not really a good cross-platform solution to this.

When I picked up the code this time, I decided to make a browser-based version. This should be friendly to macOS and Linux systems as well.

**Showing a Maze in a Browser**  
I won't go into the code here (I'm planning a more detailed article to walk through that part), I just want to show what's new in the GitHub repo [(jeremybytes/mazes-for-programmers)](https://github.com/jeremybytes/mazes-for-programmers) in case you want to take a look at the projects yourself.

_Preview of the code: The bitmaps are generated in memory and streamed to the browser. I know it's not groundbreaking, but it's something I had never done before._

Running the "MazeWeb" project gives us a parameter page:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhXP9RQGJ2JTias7o8jSZUjoAjHcmyBsRFrGyQeyAzn82LqvkeYFY_ksps6T3lKXq1C2OGaqrIow7l1hIBxv7-wVlnxxWoF99o4QUyvbDjo41Mm038Y49tHSAhyphenhyphen6yOGpt9X4FH0PnNGvlc/s640/00-Selection1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhXP9RQGJ2JTias7o8jSZUjoAjHcmyBsRFrGyQeyAzn82LqvkeYFY_ksps6T3lKXq1C2OGaqrIow7l1hIBxv7-wVlnxxWoF99o4QUyvbDjo41Mm038Y49tHSAhyphenhyphen6yOGpt9X4FH0PnNGvlc/s1600/00-Selection1.png)

This gives options for selecting the size of the maze (the value of "50" will give a 50 by 50 grid). In addition, there are drop-downs to select the color and maze algorithm.

I particularly like these options because it makes it easier to generate mazes to see the differences in the algorithms (and the colors are fun, too).

Here's the output for the selected parameters: 50, Purple, Recursive Backtracker:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEif1TNuYX5U6kqR9HOHNe4kDHF1tNDyg5xIG8tPqnoPc0NoLyXp9_q8RkAP1NgWvlJWDLw56ZLwHyol_GwEoT1ilOaaJJdcD75_OV6OjmpCAk612e6wMvdYMvvsaprzToLcN-mDyTXfQQs/s640/01-Output1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEif1TNuYX5U6kqR9HOHNe4kDHF1tNDyg5xIG8tPqnoPc0NoLyXp9_q8RkAP1NgWvlJWDLw56ZLwHyol_GwEoT1ilOaaJJdcD75_OV6OjmpCAk612e6wMvdYMvvsaprzToLcN-mDyTXfQQs/s1600/01-Output1.png)

And another sample:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhp3NfMW1vczglWuQ5lgB62_Sla90vUgfl_W7HnvpzKuWdHA0vylIVCBXFsyYpKmAVo_cLXLSJyjg1k8d6v4oYxAOVAI_yJFhnQnYImbnCPTlR-SKKKJynsedjhO1qSXsSJwKGE-AdjFgA/s640/02-Selection2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhp3NfMW1vczglWuQ5lgB62_Sla90vUgfl_W7HnvpzKuWdHA0vylIVCBXFsyYpKmAVo_cLXLSJyjg1k8d6v4oYxAOVAI_yJFhnQnYImbnCPTlR-SKKKJynsedjhO1qSXsSJwKGE-AdjFgA/s1600/02-Selection2.png)

This uses the values 150, Mustard, and Aldous-Broder. (You can look at the [prior articles](https://github.com/jeremybytes/mazes-for-programmers/blob/master/README.md) to see the differences in the algorithms.)

As a warning, the larger values take longer to generate. If you go over 200, then you may be waiting several minutes for it to complete. I've done some benchmarking, and the delay seems to be in the creation of the bitmap image, not in the generation of the maze itself.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhdHHwQdEnkIM2EYJVgJ8HXRXcafxCpLivbCsoY22iAkgebEJ0niHqWpnFevigi2cJwqtc1HQQiB7Uzc-c8apv7soHK5NjPGt9BHWuS0Of5PyY-pJBYW0B0Kw4G96R6ylcyrsaQFZuac_I/s640/03-Output2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhdHHwQdEnkIM2EYJVgJ8HXRXcafxCpLivbCsoY22iAkgebEJ0niHqWpnFevigi2cJwqtc1HQQiB7Uzc-c8apv7soHK5NjPGt9BHWuS0Of5PyY-pJBYW0B0Kw4G96R6ylcyrsaQFZuac_I/s1600/03-Output2.png)

Also, the bitmaps can be a bit large. Notice in the browser tab that the image is 4500x4500. When I saved off this particular file, it was about 2 MB. Here's the full image that you can zoom in on to see the detail:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgKEymQyLaptdsVuwxNLlPtUsZ7is-cjn40bnKi2yd4cyh9dGi7QcYD2uBaBTgkTn5kC8nmOgikxRD8UpSKLHxULHRZ30Cxj_RhNJCWqJG_fAP40kSgH15kM75TPx2lXHtKX2OQXAci40I/s640/maze.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgKEymQyLaptdsVuwxNLlPtUsZ7is-cjn40bnKi2yd4cyh9dGi7QcYD2uBaBTgkTn5kC8nmOgikxRD8UpSKLHxULHRZ30Cxj_RhNJCWqJG_fAP40kSgH15kM75TPx2lXHtKX2OQXAci40I/s1600/maze.jpg)

**Running the Project**  
This project uses .NET Core 3.1, so you'll need that version of .NET installed. You can run the web application through the command line or with Visual Studio 2019.

**Running from Visual Studio**  
If you open the project in Visual Studio 2019, you'll want to change the drop-down on the "Start Debugging" button so that it runs the right way.

First, make sure that "MazeWeb" is set as the startup project. Then in the toolbar, click the drop-down for the "Start Debugging" button (the green triangle) -- it's a bit hard to see; I didn't know it was there for a long time.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhh5HZXeGjFPpgjf2uEDIZ5Ng5EN1yELrT1FOPCWzlTIM53cnHGttZuBDEN_3Pc_0l0neryn-ymKmcTOBp1amn-Dp2wnmJzBtpbWUG9X0Ibne1ARYQm2yaKRfrCju6XMjO9HjXxifos2x4/s400/04-Debug.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhh5HZXeGjFPpgjf2uEDIZ5Ng5EN1yELrT1FOPCWzlTIM53cnHGttZuBDEN_3Pc_0l0neryn-ymKmcTOBp1amn-Dp2wnmJzBtpbWUG9X0Ibne1ARYQm2yaKRfrCju6XMjO9HjXxifos2x4/s1600/04-Debug.png)

Make sure that "MazeWeb" is selected. If "IIS Express" is selected (which is the default), then Visual Studio will try to run the web application under IIS Express, and this won't work. If you select "MazeWeb", then Visual Studio will use the self-hosted Kestrel environment (the same one you get running from the command line).

With this setting changed, you can click the button (or hit F5), and the debugger will start, the website will be started from the command line, and the browser will navigate to the parameter page.

You may be prompted to install / trust a developer certificate. This is so that you can use HTTPS against the "localhost" environment.

**Running from the Command Line**  
You can also run the website from the command line. Open a PowerShell (or cmd) window and navigate to the "MazeWeb" project folder:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg3r3gI-KZ4ciBeVVeaFCEDdfdOiE8AMi1k4FW6qmln8YokEZNp5ZZ3hSP14jK04kTQsmw2W4XoJOeFIiM5Xjt5enO-t13qz65VcvjsLRKRj_SilFNt21lxGSl8vf9p3zx-xUaddq8nA0M/s640/05-dotnetrun.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg3r3gI-KZ4ciBeVVeaFCEDdfdOiE8AMi1k4FW6qmln8YokEZNp5ZZ3hSP14jK04kTQsmw2W4XoJOeFIiM5Xjt5enO-t13qz65VcvjsLRKRj_SilFNt21lxGSl8vf9p3zx-xUaddq8nA0M/s1600/05-dotnetrun.png)

Once you're at the "MazeWeb" folder, type "dotnet run" to start the website.

Notice that it says "Now listening on: https://localhost:5001". If you navigate your browser to that address, you'll find the parameter page. You may be prompted to install / trust a certificate for HTTPS. This is normal for the development environment.

**More to Come**  
There's still a little more work to be done on this project. I'm currently unsuccessful in getting default values into the parameter page, and I think there are some inefficiencies with the bitmap generation.

I haven't been active in web programming for a while, so there was a bit of fumbling through the process of getting this running. I'll be putting down those thoughts soon.

Find some joy and frivolity from time to time. It's too easy to get bogged down in frustrations.

I might spend the rest of the day generating mazes in different colors.

Happy Coding!
