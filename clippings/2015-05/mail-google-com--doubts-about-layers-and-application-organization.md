---
url: "https://mail.google.com/mail/u/0/?pli=1#label/Listas%2F05+-+Principais/14d6c234c32cf644"
captured_at: "2015-05-25T09:11:24-03:00"
title: "[elixir-talk:8520] Doubts about layers and application's organization - th.luiz@gmail.com - Gmail"
domain: "mail-google-com"
---

[elixir-talk:8520] Doubts about layers and application's organization

Participantes: ivan.inmm@gmail.com, elixir-lang-talk@googlegroups.com, jose.valim@plataformatec.com.br, catenacci@gmail.com

[Abrir conversação no Gmail](https://mail.google.com/mail/u/0/?pli=1#label/Listas%2F05+-+Principais/14d6c234c32cf644)

Ivan MirandaTue, May 19, 2015 at 9:25 AM

Hello guys,

Making a little analogy with Java, How to make a good distribution of layers in Elixir using Phoenix and Ecto?

What you guys are doing with the repo code and the business rules to make the application more organized?

Thanks

Ivan MirandaTue, May 19, 2015 at 11:10 PM

well, I talked to a teacher and based on the conversation i prepared something like this for my application:

web  
| - controllers

| - models

| - user.ex

| - post.ex

| - comment.ex

| - repo

| - user\_repo.ex

| - post\_repo.ex

| - comment\_repo.ex

\*\* The name of the modules are for example only

Thus, the data structure and all logic associated with the user are in the User module as well to calculate the age based on date of birth, while all queries would be in their "repo"

I know that may seem stupid, but I'm afraid that when I have a big application with thousands of queries scattered in controllers the maintenance cost become too high.

What you guys think about it?

Em terça-feira, 19 de maio de 2015 09:25:58 UTC-3, Ivan Miranda escreveu:
> Hello guys,
>
> Making a little analogy with Java, How to make a good distribution of layers in Elixir using Phoenix and Ecto?
>
> What you guys are doing with the repo code and the business rules to make the application more organized?
>
> Thanks

--   
You received this message because you are subscribed to the Google Groups "elixir-lang-talk" group.  
To unsubscribe from this group and stop receiving emails from it, send an email to [elixir-lang-talk+unsubscribe@googlegroups.com](mailto:elixir-lang-talk+unsubscribe@googlegroups.com).  
To view this discussion on the web visit [https://groups.google.com/d/msgid/elixir-lang-talk/5ab12501-2f6b-4e62-8905-09865bd3f6c2%40googlegroups.com](https://groups.google.com/d/msgid/elixir-lang-talk/5ab12501-2f6b-4e62-8905-09865bd3f6c2%40googlegroups.com?utm_medium=email&utm_source=footer).

José ValimWed, May 20, 2015 at 4:40 AM

Well, I would say that you should first develop your application and, when it starts to become complex, you can think about better ways to organize your code. At this point, you are assuming queries are going to play a good part of the complexity problem but you may be wrong. It is hard to come up with a plan without real "data".

In any case, I wouldn't call those "repo". The repository is the abstraction around the database, with update, delete and other ops. In your case, you just want a place to put the queries. Maybe you can call it user\_query if you want to be explicit?

/web

/queries

/user\_query.ex

**José Valim**

[www.plataformatec.com.br](http://www.plataformatec.com.br/)

Skype: jv.ptec

Founder and Lead Developer

To view this discussion on the web visit [https://groups.google.com/d/msgid/elixir-lang-talk/CAGnRm4KBw1o7x1tR5s0y8uLeOs\_OP1SCXFb7qS7WnaiM4W5UwA%40mail.gmail.com](https://groups.google.com/d/msgid/elixir-lang-talk/CAGnRm4KBw1o7x1tR5s0y8uLeOs_OP1SCXFb7qS7WnaiM4W5UwA%40mail.gmail.com?utm_medium=email&utm_source=footer).

Ivan MirandaWed, May 20, 2015 at 8:19 AM

Cool, user\_query is a nice name for me!

Talking about my real situation, I'm doing the adaptation of part of a browser game for Elixir, had written him earlier in PHP and am now using websockets to make the disputes between players more interactive .

It is a turn-based game so no high processing to worry, I consider every action of the players as a simple request, I make the logic behind the movement and notify those involved with the board changes.

In this context, the consultations are very frequent, since I still have code in PHP that need to know the state of the battle.

I could then do something like:

defmodule Player do

schema "player" do

...

end

def avoidance(p) do

...

end

def critical(p) do

...

end

end

defmodule PlayerQuery do

def get\_skills(p) do

# make a query to get the skills of Player in the Repo

end

end

Initially it seems like a good way of organizing for me :D

  
Em quarta-feira, 20 de maio de 2015 04:40:51 UTC-3, José Valim escreveu:
> Well, I would say that you should first develop your application and, when it starts to become complex, you can think about better ways to organize your code. At this point, you are assuming queries are going to play a good part of the complexity problem but you may be wrong. It is hard to come up with a plan without real "data".
>
> In any case, I wouldn't call those "repo". The repository is the abstraction around the database, with update, delete and other ops. In your case, you just want a place to put the queries. Maybe you can call it user\_query if you want to be explicit?
>
> /web
>
> /queries
>
> /user\_query.ex
>
> **José Valim**
>
> [www.plataformatec.com.br](http://www.plataformatec.com.br/)
>
> Skype: jv.ptec
>
> Founder and Lead Developer
>
>   
>
> On Wed, May 20, 2015 at 4:10 AM, Ivan Miranda <ivan...@gmail.com> wrote:  
> > well, I talked to a teacher and based on the conversation i prepared something like this for my application:
> >
> > web  
> > | - controllers
> >
> > | - models
> >
> > | - user.ex
> >
> > | - post.ex
> >
> > | - comment.ex
> >
> > | - repo
> >
> > | - user\_repo.ex
> >
> > | - post\_repo.ex
> >
> > | - comment\_repo.ex
> >
> > \*\* The name of the modules are for example only
> >
> > Thus, the data structure and all logic associated with the user are in the User module as well to calculate the age based on date of birth, while all queries would be in their "repo"
> >
> > I know that may seem stupid, but I'm afraid that when I have a big application with thousands of queries scattered in controllers the maintenance cost become too high.
> >
> > What you guys think about it?
> >
> > Em terça-feira, 19 de maio de 2015 09:25:58 UTC-3, Ivan Miranda escreveu:
> > > Hello guys,
> > >
> > > Making a little analogy with Java, How to make a good distribution of layers in Elixir using Phoenix and Ecto?
> > >
> > > What you guys are doing with the repo code and the business rules to make the application more organized?
> > >
> > > Thanks
> >
> > --   
> > You received this message because you are subscribed to the Google Groups "elixir-lang-talk" group.  
> > To unsubscribe from this group and stop receiving emails from it, send an email to elixir-lang-ta...@googlegroups.com.  
> > To view this discussion on the web visit [https://groups.google.com/d/msgid/elixir-lang-talk/5ab12501-2f6b-4e62-8905-09865bd3f6c2%40googlegroups.com](https://groups.google.com/d/msgid/elixir-lang-talk/5ab12501-2f6b-4e62-8905-09865bd3f6c2%40googlegroups.com?utm_medium=email&utm_source=footer).  
> > For more options, visit <https://groups.google.com/d/optout>.

--   
You received this message because you are subscribed to the Google Groups "elixir-lang-talk" group.  
To unsubscribe from this group and stop receiving emails from it, send an email to [elixir-lang-talk+unsubscribe@googlegroups.com](mailto:elixir-lang-talk+unsubscribe@googlegroups.com).  
To view this discussion on the web visit [https://groups.google.com/d/msgid/elixir-lang-talk/22b62a96-7fd1-43b2-8f16-84fa857bfca0%40googlegroups.com](https://groups.google.com/d/msgid/elixir-lang-talk/22b62a96-7fd1-43b2-8f16-84fa857bfca0%40googlegroups.com?utm_medium=email&utm_source=footer).

Onorio CatenacciWed, May 20, 2015 at 10:42 AM

On Tuesday, May 19, 2015 at 10:10:36 PM UTC-4, Ivan Miranda wrote:
> well, I talked to a teacher and based on the conversation i prepared something like this for my application:
>
> web  
> | - controllers
>
> | - models
>
> | - user.ex
>
> | - post.ex
>
> | - comment.ex
>
> | - repo
>
> | - user\_repo.ex
>
> | - post\_repo.ex
>
> | - comment\_repo.ex
>
> \*\* The name of the modules are for example only
>
> Thus, the data structure and all logic associated with the user are in the User module as well to calculate the age based on date of birth, while all queries would be in their "repo"
>
> I know that may seem stupid, but I'm afraid that when I have a big application with thousands of queries scattered in controllers the maintenance cost become too high.
>
> What you guys think about it?

Hi Ivan,

While it's good to plan things before coding I agree with José on this one.  Trying to decide where the complexity will be before you've even written a line of code seems like a textbook definition of premature optimization to me.  Yes, by all means plan your application architecture but don't spend a lot of time agonizing about it.  More important than a lot of upfront planning is building in some flexibility so that when things change (and they will change) you're not totally sunk.  I can't guarantee anyone where the complexity will be in a given application but I can guarantee that things will change before you finish the app.

Just my humble opinion.

--

Onorio

--   
You received this message because you are subscribed to the Google Groups "elixir-lang-talk" group.  
To unsubscribe from this group and stop receiving emails from it, send an email to [elixir-lang-talk+unsubscribe@googlegroups.com](mailto:elixir-lang-talk+unsubscribe@googlegroups.com).  
To view this discussion on the web visit [https://groups.google.com/d/msgid/elixir-lang-talk/97d57427-0d54-4780-bb3a-c66abea41d78%40googlegroups.com](https://groups.google.com/d/msgid/elixir-lang-talk/97d57427-0d54-4780-bb3a-c66abea41d78%40googlegroups.com?utm_medium=email&utm_source=footer).

Ivan MirandaWed, May 20, 2015 at 1:15 PM

Thank you Onorio, its reallygood for me hear from people with more experience.

Then a start to write some code and I think dont even got the hang of it yet...

ex:

defmodule Character do

schema "character" do

.. ## some fields

has\_many :char\_skils, SkillRef

has\_many :skills, through: [:char\_skils, :skill]

end

end

defmodule SkillRef do

schema "character\_skill" do

belongs\_to :character, Character

belongs\_to :skill, Skill

end

end

defmodule Skill do

scheme "skill" do

... ## some fields

end

end

In a situation, the player send an ID of chosen Character, an ID of chosen Skill and a coordinate {x,y} of the board, then i validate the ID's and the coordinate, calculate the damage on the cordinate and reply the update message,

Here i need to rescue the character and the Skill.

I see 2 ways to do it:

- Def a func in the CharacterQuery module that rescue to me the character and the Skill

- Def a func in the Character module called something like 'get\_skill( character, skillID )' that rescue for me the choisen skill for the character

In the first way i can isolate all about the query in a exclusive module, but reduces the practicality since it is necessary knows about the operation of Character and CharacterQuery modules

In the second way i have more readability, but beginning to mix database logic with business rules...

As a beginner in the Elixir universe I ask:

What do you suggest me?

Thank you! :)

To view this discussion on the web visit [https://groups.google.com/d/msgid/elixir-lang-talk/7a3d9e8f-f3f9-429c-b724-befd38887552%40googlegroups.com](https://groups.google.com/d/msgid/elixir-lang-talk/7a3d9e8f-f3f9-429c-b724-befd38887552%40googlegroups.com?utm_medium=email&utm_source=footer).

Ivan MirandaThu, May 21, 2015 at 9:26 PM

Ok, Just to complete, I wrote a lot of code and did the following:

models

| - character.ex

| - skill.ex  

| - character

| - query.ex

| - builder.ex

| - skill

| - query.ex

the modules:

defmodule Character do

...

end

defmodule Character.Query do

...

end

defmodule Character.Builder do

...

end

with it i can do things like:

char = Character

|> Character.Builder.with\_skills

|> Character.Builder.with\_id(150)

|> Character.Builder.build

and things like:

skils\_count = Character.Query.count\_atack\_skills(150)

Using the Character.Builder and Character.Query reduced the amount of aliased modules, improved readability for me, organize and encapsulate all logic and even allows me to build optimized queries as needed...

well, I go forward in the application and'm getting satisfied with the results

if someone want to see the elixir at work in my humble little game, you can access:

[www.sugoigame.com.br](http://www.sugoigame.com.br/)

is a brasilian game in construction, only the fight system is in Elixir, to see, create a team e click in "Treino", enter in the queue and await for a opponent.

Thank you for the patience :)

greetings

Em terça-feira, 19 de maio de 2015 09:25:58 UTC-3, Ivan Miranda escreveu:
> Hello guys,
>
> Making a little analogy with Java, How to make a good distribution of layers in Elixir using Phoenix and Ecto?
>
> What you guys are doing with the repo code and the business rules to make the application more organized?
>
> Thanks

--   
You received this message because you are subscribed to the Google Groups "elixir-lang-talk" group.  
To unsubscribe from this group and stop receiving emails from it, send an email to [elixir-lang-talk+unsubscribe@googlegroups.com](mailto:elixir-lang-talk+unsubscribe@googlegroups.com).  
To view this discussion on the web visit [https://groups.google.com/d/msgid/elixir-lang-talk/5f314182-9638-42d9-83ac-fbbc67353233%40googlegroups.com](https://groups.google.com/d/msgid/elixir-lang-talk/5f314182-9638-42d9-83ac-fbbc67353233%40googlegroups.com?utm_medium=email&utm_source=footer).
