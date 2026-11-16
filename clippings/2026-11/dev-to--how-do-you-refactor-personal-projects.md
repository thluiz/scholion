---
url: "https://dev.to/scrabill/how-do-you-refactor-personal-projects-39ho"
captured_at: "2026-11-16T19:22:37+00:00"
title: "How do you refactor personal projects?"
domain: "dev-to"
---

[![Shannon Crabill](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F15567%2F93b40a7b-1493-4995-9487-ff6ba2966e5d.jpg)](https://dev.to/scrabill)

Perhaps a better question is _do you_ refactor personal projects?

I can see both sides of this.

Refactoring a personal project to incorporate new functionality is a good way to show off new skills. On the flip side, _learning_ new skills may be a better use of your time.

Do you ever go back and rework old projects? What do you look for when refactoring?

## Top comments (16)

Subscribe

Collapse Expand

[![ravavyr profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F203941%2F8b2cd853-f5c0-4476-ab98-0b1f4a91f57b.png)](https://dev.to/ravavyr)

[Ravavyr](https://dev.to/ravavyr)

Web Dev full-stack \[LAMP\] since 2005, but much heavier on the JS stuff these days. Jack of all Stacks, Master of some. Always looking to learn new things. Always glad to help out, just ask.

*   Location
    
    Atlanta, GA
    
*   Education
    
    B.S. in Biochemistry 2004, M.S. in Computer Information Systems 2007
    
*   Pronouns
    
    Stormageddon Dark Lord of All
    
*   Work
    
    Senior Web Consultant at Applied Imagination LLC
    
*   Joined
    
    Jul 30, 2019
    

• [Dec 27 '19](https://dev.to/scrabill/how-do-you-refactor-personal-projects-39ho#comment-jd55)

*   [Copy link](https://dev.to/scrabill/how-do-you-refactor-personal-projects-39ho#comment-jd55)

*   [Report abuse](https://dev.to/report-abuse?url=https://dev.to/ravavyr/comment/jd55)

I mostly refactor things if i decide to go back and add a new feature or fix a bug i found. It usually goes something like "who wrote that crap? oh, right, me...i need to fix that" and then i spend two days cleaning stuff up and then finally adding the new feature :)

Collapse Expand

[![scrabill profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F15567%2F93b40a7b-1493-4995-9487-ff6ba2966e5d.jpg)](https://dev.to/scrabill)

Lol, I can relate to "who wrote this crap?"

Collapse Expand

[![eranelbaz profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F277401%2F51218fc1-c843-4c09-829e-06299e43421a.png)](https://dev.to/eranelbaz)

I do refactor my project,  
most the refactor I do is when I need to add new features and I see the code that integrate with my new feature and I understand that my "now" knowledge is better than what I had so I do a little refactor,  
What that helps my do all my refactor is thick layer of integration tests that tells me if I broke something

And I'm writing a new blog post about a half year refactor I did in one of my team products

Collapse Expand

[![tiso profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F37821%2F0d0443f8-4739-42c5-b3d5-192e6a0404a9.jpeg)](https://dev.to/tiso)

I do, for one of two reasons:

1.  I want to upgrade code to my new/better skills.
2.  I want to add some new feature (move project forward). You know, I have lot of projects in "it does something i want, but i have lot of features in mind to add there" state. Some of them i didn't touched for years. Now i have some time to move them forward - something like End of Year Resolution.

Collapse Expand

[![\_\_orderandchaos profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F177328%2Fa897be73-7149-4424-9d90-166c94421176.png)](https://dev.to/__orderandchaos)

Refactoring a project is learning a new skill.

Collapse Expand

[![scrabill profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F15567%2F93b40a7b-1493-4995-9487-ff6ba2966e5d.jpg)](https://dev.to/scrabill)

Refactoring a project is a skill in its self? Or to refactor means you've learned new skills?

Collapse Expand

[![\_\_orderandchaos profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F177328%2Fa897be73-7149-4424-9d90-166c94421176.png)](https://dev.to/__orderandchaos)

Well, both of course.

I get tired of the argument that "you ain't gonna need it".

It's important that we always refactor our code. Even if we never touch it again, the process itself is the most important part.

The skills we pick up as we refactor our code makes us more efficient at spotting opportunities to refactor and at quicker at implementing the changes.

Once you start refactoring everything you start to notice the consistencies in your codebase then you can decide whether or not it's worth abstracting them away.

Sure sometimes you can take an abstraction too far but you'll never know whether it's worth it or not without a lot of practice and experience.

The only way to get that is to refactor everything all the time.

Collapse Expand

[![zakwillis profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F192515%2F312d3b1a-97c0-4ad7-8af6-16bd17ea86ef.jpg)](https://dev.to/zakwillis)

[zakwillis](https://dev.to/zakwillis)

Hi, I normally contract in MSBI, SQL, Data Arcitecture, Oracle, .Net/.Net Core, API development, React, focusing on www.cryptostatto.com at the moment. Reach out if you see any synergy.

*   Location
    
    London
    
*   Education
    
    Degree - Grad 1998
    
*   Work
    
    CEO at London/Virtual
    
*   Joined
    
    Jul 9, 2019
    

• [Dec 28 '19](https://dev.to/scrabill/how-do-you-refactor-personal-projects-39ho#comment-jdca)

*   [Copy link](https://dev.to/scrabill/how-do-you-refactor-personal-projects-39ho#comment-jdca)

*   [Report abuse](https://dev.to/report-abuse?url=https://dev.to/zakwillis/comment/jdca)

Yes and no.  
I only refractor when;

*   something I did before needs enhancing and it becomes obvious it has become too complicated to extend/understand.
*   I find myself repeating the same code. Some code will move to a utilities library or generic.

Often, it is more that if something wasn't developed fully, it is new code, so little refactoring occurs.

It is definitely the case there are some awful parts to my code, but typically they are fire and forget.

Collapse Expand

[![sylwiavargas profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F283021%2F487202dc-33a7-402d-9e81-e57602edd620.jpeg)](https://dev.to/sylwiavargas)

[Sylwia Vargas](https://dev.to/sylwiavargas)

I'm a tech writer and educator advocating for code newbies ✨ I'm also a Developer Relations Lead + front-end dev at @inngest

*   Location
    
    New York
    
*   Pronouns
    
    she/her
    
*   Joined
    
    Nov 30, 2019
    

• [Dec 28 '19](https://dev.to/scrabill/how-do-you-refactor-personal-projects-39ho#comment-jdho)

*   [Copy link](https://dev.to/scrabill/how-do-you-refactor-personal-projects-39ho#comment-jdho)

*   [Report abuse](https://dev.to/report-abuse?url=https://dev.to/sylwiavargas/comment/jdho)

I decided to refactor my side project from April from bootcamp. It was the first time I did anything with Rails and CSS and it shows - CSS is a mess. I genuinely like the project so decided to give it a new life. I wrote a plan for myself and wrote about it here:  
[dev.to/sylwiavargas/refactoring-my...](https://dev.to/sylwiavargas/refactoring-my-rails-project-32h3)

I’ve been coding 10-75 minutes a day this holiday break. I see I’m learning a lot, also because I give myself space to go down the rabbit hole of docs and stack overflow threads :)

Collapse Expand

[![aolivier profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F36461%2F5ce0bb30-53b4-4a39-b350-8c1985534d8e.png)](https://dev.to/aolivier)

I do refactor my projects, principally because if you learn something new every day, some new framework or some new pattern and refactor your personal project is, I think, a great way to improve your understanding on those.

Collapse Expand

[![scrabill profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F15567%2F93b40a7b-1493-4995-9487-ff6ba2966e5d.jpg)](https://dev.to/scrabill)

Agreed!

Collapse Expand

[![larswww profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F285413%2Feb67af22-11da-45c9-9db7-403d736fd40d.jpeg)](https://dev.to/larswww)

When I want to add something new to my project, I take a close look at _everything_ on display to the user, and focus on making sure what’s already there is working as well as it could.

I usually find that there’s stuff I’ve already done, which I haven’t done as well as I could :)

Collapse Expand

[![get\_hariharan profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F172952%2F310ca08a-c4f8-4f43-a06d-b8d8d16a1736.jpg)](https://dev.to/get_hariharan)

When I initially wrote my library to access StackExchange Api's, it was just working and the code was super trash. I again refactored it in a much better way. Have a look here

[github.com/gethari/StackExchange.NET](https://github.com/gethari/StackExchange.NET)

Collapse Expand

[![dominicduffin1 profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F25371%2F771bb67f-ca43-427f-8dcf-fef075204046.png)](https://dev.to/dominicduffin1)

I haven't yet, although there are a few things I _would_ go back and refactor if I was going to work on them again.
