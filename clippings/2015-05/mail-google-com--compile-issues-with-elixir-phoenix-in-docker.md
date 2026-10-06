---
url: "https://mail.google.com/mail/u/0/?pli=1#label/Listas%2F05+-+Principais/14d87057983dd727"
captured_at: "2015-05-25T08:53:56-03:00"
title: "[elixir-talk:8586] Compile issues with Elixir/Phoenix in a Docker container - th.luiz@gmail.com - Gmail"
domain: "mail-google-com"
---

[elixir-talk:8586] Compile issues with Elixir/Phoenix in a Docker container

Participantes: sasa.juric@gmail.com, elixir-lang-talk@googlegroups.com, jose.valim@plataformatec.com.br

[Abrir conversação no Gmail](https://mail.google.com/mail/u/0/?pli=1#label/Listas%2F05+-+Principais/14d87057983dd727)

Saša JurićSun, May 24, 2015 at 2:43 PM

I have been playing a bit with dockerizing Elixir/Phoenix dev env, and have run into a strange issue with compiling.

I’m able to setup a Docker container where I can create, compile, and run a Phoenix server. However, when I restart the container, I can’t build the project anymore.

The project folder is mounted as a volume, so all the files are preserved after the container is restarted. However, some of the compiled dependencies (under \_build/dev/lib) are deleted as soon as I start the compilation in the restarted container.

I have a feeling it happens because I’m not persisting everything that needs to be persisted (maybe some local hex cache?), but I’m not sure where exactly the problem lies, so I’m looking for some pointers.

Here’s an outline on reproducing the issue (assuming Docker (and boot2docker, if needed) is installed):

1. mkdir -p ~/test\_docker && cd ~/test\_docker

Note: (I work under the home folder because it works out of the box on OS X + boot2docker)

2.

cat > Dockerfile <<EOF

FROM trenpixster/elixir:1.0.4  
   
RUN curl -sL <https://deb.nodesource.com/setup_0.12> | sudo bash - && apt-get -y install nodejs inotify-tools  
RUN mix local.hex --force && mix archive.install <https://github.com/phoenixframework/phoenix/releases/download/v0.13.1/phoenix_new-0.13.1.ez> —force

ENV LANG en\_US.UTF-8  
EOF

3. Build the image and start the container:

docker build -t sasa/phoenix:0.13.1 .

docker run --rm -it -v $(pwd):/test\_docker -w /test\_docker -p 4000:4000 sasa/phoenix:0.13.1 /bin/bash

4. mix phoenix.new hello\_phoenix

(answer Y to "Fetch and install dependencies?”)

5. cd hello\_phoenix && mix compile

This compiles and it even works (though you don’t need to run it). The problem appears if I stop the container, then start it again, and try to compile the project again:

# stop the container

exit

# start another container

docker run --rm -it -v $(pwd):/test\_docker -w /test\_docker -p 4000:4000 sasa/phoenix:0.13.1 /bin/bash

# try to compile again

cd hello\_phoenix && mix compile

\*\* (MatchError) no match of right hand side value: {:error, {:plug, {'no such file or directory', 'plug.app'}}}  
    (phoenix) lib/mix/tasks/compile.phoenix.ex:11: Mix.Tasks.Compile.Phoenix.run/1  
    (elixir) lib/enum.ex:977: anonymous fn/3 in Enum.map/2  
    (elixir) lib/enum.ex:1261: Enum."-reduce/3-lists^foldl/2-0-"/3  
    (elixir) lib/enum.ex:977: Enum.map/2  
    (mix) lib/mix/tasks/compile.all.ex:15: Mix.Tasks.Compile.All.run/1  
    (mix) lib/mix/tasks/compile.ex:64: Mix.Tasks.Compile.run/1  
    (mix) lib/mix/cli.ex:55: Mix.CLI.run\_task/2

Somehow some of the built deps (such as plug) are deleted from the build folder after I started mix compile:

ls \_build/dev/lib/  
cowboy  hello\_phoenix  phoenix  phoenix\_ecto  phoenix\_html  phoenix\_live\_reload  postgrex

Attempting to fetch the deps doesn’t fetch anything (since everything is there from the initial fetching), but it makes compiling work again:

mix deps.get  
Running dependency resolution  
Dependency resolution completed successfully  
All dependencies up to date

mix compile

(now it works, though it recompiles lost deps builds)

Any idea what happens here?

José ValimSun, May 24, 2015 at 3:05 PM

The only reason it would happen is if plug is no longer seen as a dependency. Then its build directory is automatically removed and cleaned up. And the only reason plug cannot be seen as a dependency is if hex is not available or has a faulty registry (assuming plug is appearing as a dependency of a hex dependency).

You can investigate this further in a couple ways. You can try for example running Phoenix with --no-compile or --no-deps-check.

**José Valim**

[www.plataformatec.com.br](http://www.plataformatec.com.br/)

Skype: jv.ptec

Founder and Lead Developer

To view this discussion on the web visit [https://groups.google.com/d/msgid/elixir-lang-talk/CAGnRm4JoRRySkzk5Bk9%2B64j\_xVLDvOV7PqnFtmjBQ1Ym7ZuZjA%40mail.gmail.com](https://groups.google.com/d/msgid/elixir-lang-talk/CAGnRm4JoRRySkzk5Bk9%2B64j_xVLDvOV7PqnFtmjBQ1Ym7ZuZjA%40mail.gmail.com?utm_medium=email&utm_source=footer).

Saša JurićSun, May 24, 2015 at 3:42 PM

On Sunday, May 24, 2015 at 8:05:25 PM UTC+2, José Valim wrote:
> The only reason it would happen is if plug is no longer seen as a dependency. Then its build directory is automatically removed and cleaned up. And the only reason plug cannot be seen as a dependency is if hex is not available or has a faulty registry (assuming plug is appearing as a dependency of a hex dependency).

The faulty registry was the reason. Or rather the fact that ~/.hex wasn't preserved between containers, which means that after a restart there was no registry. Mounting that folder as a volume resolved the problem:

docker run --rm -it -v $(pwd):/test\_docker **-v $(pwd)/.hex:/root/.hex** -w /test\_docker -p 4000:4000 sasa/phoenix:0.13.1 /bin/bash

Thanks for the help!

--   
You received this message because you are subscribed to the Google Groups "elixir-lang-talk" group.  
To unsubscribe from this group and stop receiving emails from it, send an email to [elixir-lang-talk+unsubscribe@googlegroups.com](mailto:elixir-lang-talk+unsubscribe@googlegroups.com).  
To view this discussion on the web visit [https://groups.google.com/d/msgid/elixir-lang-talk/15dc126d-945b-4477-886e-d5ed92d089e9%40googlegroups.com](https://groups.google.com/d/msgid/elixir-lang-talk/15dc126d-945b-4477-886e-d5ed92d089e9%40googlegroups.com?utm_medium=email&utm_source=footer).
