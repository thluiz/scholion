---
url: "https://blog.appsignal.com/2024/06/25/leverage-concurrency-efficiently-when-managing-multiple-tasks-in-elixir.html?utm_source=elixir-alchemy&utm_medium=email&utm_campaign=2024-07-03"
captured_at: "2026-09-23T18:37:23+01:00"
title: "Leverage Concurrency Efficiently When Managing Multiple Tasks in Elixir | AppSignal Blog"
domain: "blog.appsignal.com"
---

Elixir

Leverage Concurrency Efficiently When Managing Multiple Tasks in Elixir

Tracey Onim

When working on multiple tasks, it's important to consider performing them concurrently. However, when using concurrency, we need to be careful not to overload our system resources.

In this article, we will cover the following:

What is concurrency?
How can we use concurrency in Elixir?
Common issues when working with a series of tasks concurrently.
How to efficiently manage a series of tasks using the Task module.

Let's get going!

What is Concurrency?

Concurrency is the ability to execute multiple tasks at the same time.

Concurrency and parallelism are crucial features in modern programming. The operating systems installed on our computers are designed to incorporate these features. Both concurrency and parallelism involve executing multiple tasks simultaneously. However, concurrency focuses on managing multiple tasks within one resource. This can be achieved through techniques like multitasking and asynchronous programming. In an operating system, concurrency can be achieved by opening multiple applications to perform different tasks at the same time, also referred to as multitasking.

On the other hand, parallelism involves executing multiple tasks simultaneously across multiple processing units (such as multiple CPU cores or distributed computing resources), thus improving system speed.

How Can We Use Concurrency in Elixir?

To achieve concurrency in Elixir, you need to initiate a process and execute the function or code responsible for performing a specific task within that process.

Here's an example of some basic Elixir code that we can take a look at.

ELIXIR
def send_message(phone_number) do
  # Simulate some processing time
  Process.sleep(3000)
  IO.puts("Sending message to #{phone_number}")
  {:ok, "sent"}
end

In this example, we've added a 3-second sleep to simulate the fact that sending a message to an external phone number can sometimes cause some latency.

When send_message/1 is invoked, this function will delay processing for 3 seconds before printing a message. It will also return an {:ok, "sent"} tuple to indicate that the message was successfully sent to the given phone number.

When executing synchronous Elixir code like the code above, we must wait for it to complete before receiving the output. If we need to send messages to multiple phone numbers, each with a delay of 3 seconds, it could take a significant amount of time to receive a notification that all messages have been successfully sent.

Taking It One Step Further

Now, let's take it a step further and write some code that sends a message to multiple phone numbers.

ELIXIR
def send_to_all(phone_numbers) do
  Enum.each(phone_numbers, &send_message/1)
end

The send_to_all/1 function takes a list of phone numbers as an argument and uses the Enum.each/2 function to iterate over the list, sending a message to each phone number using the send_message function.

If you run this function in iex, you will notice two things:

It takes longer to receive the final output, which is an atom :ok. Enum.each/2 returns :ok when invoked.
Printing happens one at a time, with each print taking 3 seconds. Depending on the number of phone numbers provided, send_message/1 is called 5 times in our case, taking about 15 seconds to complete.

This means that when sending a message to a given phone number, each phone number has to wait for the preceding phone number to execute before moving on to the next one. The execution is synchronous, also known as blocking code.

Elixir provides the ability to run code concurrently or asynchronously. Asynchronous code allows you to execute multiple tasks simultaneously. This type of code is also referred to as non-blocking code because it does not hinder the primary execution of a program.

Let's improve the send_to_all/1 function by running the task of sending messages to each phone number asynchronously. We need to start a process for each task.

A process is a separate entity where code execution occurs. These processes are lightweight, run concurrently, and are isolated from each other. The code we write runs inside processes. The IEx (interactive shell) is an example of an Elixir process.

ELIXIR
def send_to_all(phone_numbers) do
  Enum.each(phone_numbers, fn phone_number ->
    Task.start(fn -> send_message(phone_number) end)
  end)
end

Here, we've used Task.start/1 (which we'll go over in more detail later) to start a process for each task. After we recompile and run this function again in our IEx, you will notice two things:

It runs faster than before because it's now running asynchronously. The final output — :ok — is immediately returned even before we see the printed success messages.
It instantly prints the success message at once for all tasks, which means that all the messages are being sent at the same time.
Running Tasks Concurrently using the Task Module

Elixir has a standard library Task module commonly used for running code concurrently. This allows you to perform tasks asynchronously, which can lead to improved performance and responsiveness in your applications.

Let's go back to our send_to_all/1 function. At first, we used this function to send messages to multiple phone numbers sequentially.

ELIXIR
# Sequential version of send_to_all/1
def send_to_all(phone_numbers) do
  Enum.each(phone_numbers, fn phone_number ->
    Task.start(fn -> send_message(phone_number) end)
  end)
end

In the sequential version, send_message/1 was called for each message in the list, one after the other.

Later on, we converted the sequential code into concurrent code using Task.start/1.

ELIXIR
# Asynchronous version using Task.start/1
def send_to_all(phone_numbers) do
  Enum.each(phone_numbers, fn phone_number ->
    Task.start(fn -> send_message(phone_number) end)
  end)
end

In the asynchronous version, Task.start/1 creates a separate task for each message, allowing the tasks to execute concurrently.

The Task module has several useful functions to run code concurrently. Let's now look at a few of these functions.

Task.start/1

Task.start/1 is used to start a new process/task. It takes in an anonymous function with zero arity as an argument, where the intended work is performed. Usually, it doesn't return the result of the executed function. Instead, it returns an {:ok, PID} tuple, where :ok means the process was started successfully, and PID stands for process identifier: a number that uniquely identifies an Elixir process.

Let's try it out in IEx:

SHELL
iex > {:ok, pid} = Task.start(fn ->  IO.puts("converting to asyncronous code") end)
         converting to asyncronous code
          {:ok, #PID<0.153.0>}

The message is printed instantly and the result is {:ok, #PID<0.153.0>}. This means that the process was started successfully. pid represents the process started by Task.start/1.

However, it's hard to know if all the messages were sent successfully using Task.start/1, since it will still return {:ok, PID}, which stands for a process that's started successfully.

It is useful in cases where you don't have interest in the returned result or whether it completes successfully.

A good example is working on a background job processing system, such as sending messages to registered users every midnight. You can use Task.start/1 to asynchronously handle each task that sends messages to users. In this context, you're not particularly interested in the return value of Task.start/1, because your main concern is to handle the tasks asynchronously, and you have a mechanism to track the status of each task. This mechanism can involve saving the status in the database, ensuring that any pending tasks are retried in subsequent runs.

In case something goes wrong when sending messages to users, the status of the message will still be pending in the database. You can guarantee that the worker will run again at midnight and retry for pending messages.

Task.async/1

Like Task.start/1, Task.async/1 is also used to start a process. The difference between Task.async/ and Task.start/ is that with Task.async/1, you can retrieve the function result executed within the process. It takes in an anonymous function with zero arity which starts a process and then returns a %Task{} struct.

Let's try it out in IEx:

SHELL
iex > Task.async(fn -> IO.puts("converting to asyncronous code using async") end)
    converting to asyncronous code using async
      %Task{
        mfa: {:erlang, :apply, 2},
        owner: #PID<0.109.0>,
        pid: #PID<0.110.0>,
        ref: #Reference<0.0.13955.2933390707.3162308609.257437>
      }

The message is printed immediately and returns a %Task{} struct as the output. The returned Task struct includes useful information about the process that's started:

owner represents the Process Identifier (PID) of the process that started the Task. In our example, the owner is IEx since we are running code within the shell. If we run self(), the function that returns the PID of the current process, then the PID returned by self() will indeed match the PID of the owner of the task started.
pid: The process identifier of the process started by the task. You can use this PID to monitor the process further if needed.
ref: This is a process monitor reference that can be used in cases where you want to be notified about how and where a process exits.

To retrieve a result from the returned task, use either Task.await/2 or Task.yield/2. They both accept a %Task{} struct as an argument and handle process timeout. However, they handle the timeout differently.

Task.await/2 and Task.yield/2 have a default timeout of 5000ms or 5 seconds to ensure that processes don't get stuck waiting for a result forever. Task.await/2 will cause an exception and crash the process if there is a slower task taking more than 5000ms to complete, while Task.yield/2 returns nil.

Let's modify send_to_all/1 to use Task.async/1, then retrieve its result using Task.await/2. Later, use Task.yield/2:

ELIXIR
def send_to_all(phone_numbers) do
  phone_numbers
  |> Enum.map(fn phone_number ->
    Task.async(fn -> send_message(phone_number) end)
  end)
  |> IO.inspect(label: "started tasks++++")
  |> Enum.map(fn task -> Task.await(task) end)
end

send_to_all/1 iterates over a given list of phone numbers using Enum.map/2 instead of Enum.each/2 to retrieve the result of each task, and spawns a task for each using Task.async/1. Then we use Task.await/2 to retrieve the result of each task. It waits for the task to complete and then returns a result.

Run the send_to_all/1 function in IEx:

SHELL
iex > send_to_all(1..10)
started tasks++++[
  %Task{
    mfa: {:erlang, :apply, 2},
    owner: #PID<0.150.0>,
    pid: #PID<0.151.0>,
    ref: #Reference<0.0.19203.3913757788.1002242054.113465>
  },
  %Task{
    mfa: {:erlang, :apply, 2},
    owner: #PID<0.150.0>,
    pid: #PID<0.152.0>,
    ref: #Reference<0.0.19203.3913757788.1002242054.113469>
  },..
]
 
sending message  to 1
sending message  to 2
sending message  to 3
sending message  to 4
sending message  to 5
sending message  to 6
sending message  to 7
sending message  to 8
sending message  to 9
sending message  to 10
 
[
  {:ok, "sent"},
  {:ok, "sent"},
...
]

Looking at the inspected result, each task represents a spawned process. They all have a different pid with a similar owner pid meaning that the caller process (IEx) is one. Once each task is completed, the messages are printed at the same time and the result returned. The final result returned is a list of output expected from send_message/1.

Now, let's retrieve the result from each spawned task using Task.yield/2:

ELIXIR
def send_to_all(phone_numbers) do
  phone_numbers
  |> Enum.map(fn phone_number ->
    Task.async(fn -> send_message(phone_number) end)
  end)
  |> IO.inspect(label: "started tasks++++")
  |> Enum.map(fn task -> Task.yield(task) end)
end
SHELL
iex > send_to_all(1..10)
started tasks++++[
  %Task{
    mfa: {:erlang, :apply, 2},
    owner: #PID<0.150.0>,
    pid: #PID<0.151.0>,
    ref: #Reference<0.0.19203.3913757788.1002242054.113465>
  },
  %Task{
    mfa: {:erlang, :apply, 2},
    owner: #PID<0.150.0>,
    pid: #PID<0.152.0>,
    ref: #Reference<0.0.19203.3913757788.1002242054.113469>
  },..
]
 
sending message  to 1
sending message  to 2
sending message  to 3
sending message  to 4
sending message  to 5
sending message  to 6
sending message  to 7
sending message  to 8
sending message  to 9
sending message  to 10
 
[
  :ok, {:ok, "sent"},
  :ok, {:ok, "sent"},
...
]

The result is similar. However, Task.yield/2 returns an {:ok, term()} tuple, where term represents the result returned by the function executed within the process. That's why our output is a list of the {:ok, {:ok, "sent"}} tuple where {:ok, "sent"} is the expected result from send_message/1.

In our send_to_all/1 function, we used Task.start/2 and Task.async/2 to start each task of sending a message to a given phone number in the background, allowing them to run concurrently. Starting a separate process for each task when sending a message ensures its isolation. Therefore, if one task encounters an error or fails for any reason, it won't affect the execution of other tasks.

An Example with an Error

For example, let's assume we have introduced an error in one of the tasks.

ELIXIR
def send_message(3) do
  # Simulate some processing time
  Process.sleep(3000)
  IO.puts("Sending message to #{3 + "a"}")
  {:ok, "sent"}
end
 
def send_message(phone_number) do
  # Simulate some processing time
  Process.sleep(3000)
  IO.puts("Sending message to #{phone_number}")
  {:ok, "sent"}
end
 
# Asynchronous version using Task.start/1
def send_to_all(phone_numbers) do
  Enum.each(phone_numbers, fn phone_number ->
    Task.start(fn -> send_message(phone_number) end)
  end)
end

Here, the send_message/1 function has two function heads. The first function head pattern matches on 3 and deliberately raises an arithmetic error by adding the number 3 to a string "a". The second function head handles other phone numbers values and simulates sending messages as before.

SHELL
iex > send_to_all(1..5)
06:19:17.562 [error] Task #PID<0.294.0> started from #PID<0.291.0> terminating
** (ArithmeticError) bad argument in arithmetic expression
    :erlang.+(3, "a")
 
[
  ok: #PID<0.292.0>,
  ok: #PID<0.293.0>,
  ok: #PID<0.294.0>,
  ok: #PID<0.295.0>,
  ok: #PID<0.296.0>
]
sending message  to 1
sending message  to 2
sending message  to 4
sending message  to 5

If you pass a list of phone numbers to send_to_all/1 and one of them is 3, the corresponding task will raise an arithmetic error, but other tasks will continue to run. From the results, we can see that we are notified of an arithmetic error in one of the started processes (#PID<0.294.0>). We also receive printed messages indicating that the messages were sent successfully to numbers 1, 2, 4, and 5. That means that the task started for number 3 encountered an error, but didn't prevent other processes from performing their tasks.

This approach enhances concurrency by allowing tasks to run concurrently, while also ensuring that they are isolated processes. This helps to create a more robust system.

A Problem: Working with a Series of Tasks

We've seen how we have been able to send messages to the given phone numbers concurrently using Task.async/1 and Task.start/1. In the examples provided, send_to_all/1 spawned a process for each task when sending a message. Even though our aim is to leverage concurrency and build a fault-tolerant and robust application, we should also take into consideration that processes don't share memory.

The more we increase phone numbers, the more we start a high number of concurrent tasks, each one occupying their own memory. Therefore, increasing the number of concurrent tasks can lead to an application consuming a significant amount of memory. That, in turn, can cause slow application performance and a spike in system usage, degrading system performance and maybe even making other services unresponsive.

Let's make send_to_all/1 send messages to 1 million phone numbers. But first, we'll modify it by renaming send_to_all/1 to differentiate the send_to_all/1 using Task.async/1 from the one using Task.start/1.

ELIXIR
defmodule Sender do
  def send_message(phone_number) do
    # Simulate some processing time
    Process.sleep(3000)
    IO.puts("Sending message to #{phone_number}")
    {:ok, "sent"}
  end
 
  # Asynchronous version using Task.start/1
  def send_to_all_start(phone_numbers) do
    Enum.each(phone_numbers, fn phone_number ->
      Task.start(fn -> send_message(phone_number) end)
    end)
  end
 
  # Asynchronous version using Task.async/1
  def send_to_all_async(phone_numbers) do
    phone_numbers
    |> Enum.map(fn phone_number ->
      Task.async(fn -> send_message(phone_number) end)
    end)
  end
end

In this modification, send_to_all_async/1 and send_to_all_start/1 functions have been defined to differentiate the behavior of Task.async/1 and Task.start/1 when attempting to run a million processes.

Now, open IEx (or recompile it using the recompile() command if it was already running) and call send_to_all_start/1 with a million phone numbers. We're not using a real phone number, therefore we simply pass a 1..1_000_000 range of numbers.

SHELL
iex > Sender.send_to_all_start(1..1_000_000)
SHELL
06:12:14.067 [error] Too many processes
** (SystemLimitError) a system limit has been reached
    :erlang.spawn(Task.Supervised, :noreply, [{:nonode@nohost, #PID<0.150.0>, #PID<0.150.0>}, [#PID<0.150.0>, #PID<0.142.0>], [#PID<0.150.0>], {:erlang, :apply, [#Function<7.61290973/0 in Sender.send_to_all_start/1>, []]}])
    (elixir 1.15.5) lib/task/supervised.ex:6: Task.Supervised.start/3
    (elixir 1.15.5) lib/enum.ex:4356: Enum.map_range/4
    (elixir 1.15.5) lib/enum.ex:4356: Enum.map_range/4
    (elixir 1.15.5) lib/enum.ex:4356: Enum.map/2
    iex:2: (file)

The first thing we can see is an error message notifying us that too many processes have been started, exceeding the system limit. This is happening as soon as Task.start/1 is invoked for each phone number in the range from 1 to 1,000,000. Success messages have been printed, but they are not showing for all of the phone numbers. The highest number of messages that I can see in the output is 262073. Since the numbers are not sorted, it is easy to miss the highest number. However, the total number of messages sent is around 262000.

What's Going On Here and How Do We Fix It?

We are having issues with starting a million processes because the number of tasks spawned by Task.start/1 exceeds the default limit of processes (262144, for performance and memory-saving reasons) that can be started in BEAM. However, we can override this limit using +P NUM. This means we can increase the limit by running the command iex --erl '+P 1000000'.

To apply this change, close IEx and restart it by running the command iex --erl '+P 1000000' -S mix. Then, you can call send_to_all_start/1 again, with a range of phone numbers from 1 to 1000000.

SHELL
sender tracey$ iex --erl '+P 1000000' -S mix
iex > Sender.send_to_all_start(1..1_000_000)
 :ok

This time, the function Enum.each/2 has returned the final output :ok. Additionally, success messages have been printed for all of the one million phone numbers. It is good that we can override the default system limit, but we must be cautious when increasing the limit, as it can cause the VM to use more memory, potentially leading to performance issues.

To monitor memory usage before and after a system limit increase, use the :observer.start command in IEx to open the Observer tool. The Observer shows a spike in memory usage when the system limit is increased.

Before the system limit increase:

After the system limit increase:

Sending Messages To the Phone Numbers with Task.async/1

Next, we will use the send_to_all_async/1 function to send messages to a million phone numbers. This function uses Task.async/1 to start a process for each task.

SHELL
iex > Sender.send_to_all_async(1..1_000_000)

With Task.async/1, you can send a message to all the phone numbers. However, this capability may not be available on all machines, so keep that in mind.

The Observer shows a spike in memory usage when using Task.async/1.

Running these tasks synchronously works out better in terms of memory usage compared to running them asynchronously when using a combination of Enum with either Task.async/1 or Task.start/1.

When using Task.start/ or Task.async/1 to start a process for each task, you're essentially creating a separate process for each message you want to send. While this can be an efficient way to handle concurrency, it can also lead to increased memory usage, especially when dealing with a large number of tasks simultaneously.

The spike in memory usage we're seeing in the Observer is likely due to the fact that each process created by Task.async/1 and Task.start/1 consumes memory. With a million phone numbers, you're creating a million processes, which can quickly exhaust available memory, especially if each process is doing significant work or holding onto a large amount of data.

The Solution: Use Task.async_stream/3

When utilizing Task processes, the goal is to achieve concurrency to efficiently send messages to designated phone numbers. However, it is important to be mindful of system resources and avoid sudden increases in pressure.

Fortunately, the Task module provides a useful feature known as Task.async_stream/3. It works similarly to Enum.map/2 and Task.async/2 combined, as it creates task processes from a given list of items.

With Task.async_stream/3, you can perform the task for each item in the list concurrently, by starting a process. The only difference is that you can set a limit on the number of processes running at the same time with this function.

For instance, suppose the message application needs to send messages to 100 phone numbers using Task.async_stream/3. In this case, we can set the concurrency limit to 5, which means that, at most, only 5 processes will start to send messages to the given phone numbers at the same time.

Task.async_stream/3 takes in three arguments:

Enumerable: This argument represents the collection of items that you want to process concurrently. It can be an Enum or a Stream.
Anonymous function: This must take a single argument that represents an element of the enumerable. The function is applied to each enumerable element. It defines the task to be executed concurrently for each item.
Options, used to control the level of concurrency, the time tasks are allowed to run, ordering of the results and the action to take when a task times out.

Task.async_stream/3 returns a stream, which is a lazy enumerable. Therefore, transformations or computations on the stream are not performed as soon as the stream is created. Instead, they are performed until the stream is explicitly consumed or operated upon.

An Example Using Task.async_stream/3

Here's an example of using Task.async_stream/3 in IEx:

SHELL
iex > Task.async_stream(1..5, fn phone_number -> send_message(phone_number) end)
#Function<3.112246596/2 in Task.build_stream/3>

The result that's returned is a stream. To run this stream, we can use Stream.run/1, which returns :ok and isn't useful when we're not interested in the final result. Another alternative is to use the Enum functions. This is useful when you intend to perform other tasks with the expected result.

SHELL
iex > 1..5 |> Task.async_stream(fn phone_number -> send_message(phone_number) end) |> Stream.run()
sending message  to 1
sending message  to 2
sending message  to 3
sending message  to 4
sending message  to 5
:ok

Stream.run/1 is used to run the stream without collecting the result. The messages are sent to the given phone numbers and once all tasks are completed, :ok is returned.

SHELL
iex > 1..5 |> Task.async_stream(fn phone_number -> send_message(phone_number) end) |> Enum.to_list
sending message  to 1
sending message  to 2
sending message  to 3
sending message  to 4
sending message  to 5
 
[
:ok, {:ok, "sent"},
:ok, {:ok, "sent"},
:ok, {:ok, "sent"},
:ok, {:ok, "sent"},
:ok, {:ok, "sent"}
]

Enum.to_list/1 runs the stream and collects the results into a list.

Task.async_stream/3 accepts a list of options. When not explicitly passed, the options default to their default values. Let's dive further into the options passed to Task.async_stream/3.

:max_concurrency

:max_concurrency is responsible for setting a limit on the number of processes running at the same time. Its value defaults to the number of logical cores available in a system.

When running Task.async_stream/3 in IEx with a 1..20 range of phone numbers:

SHELL
iex >  Task.async_stream(1..20, fn phone_number -> send_message(phone_number) end) |> Stream.run()

I noticed that the number of items processed at the same time was in a batch of 10 until completion. This number can differ depending on the machine used, so don't be surprised if you're seeing a batch of 20 or even 5 items processed simultaneously in your machine. This is because of the logical cores available in different machines. To confirm the number of logical cores available, use System.schedulers_online/0. For machines whose CPU has less than 4 logical cores, Task.async_stream/3 will appear to be slower.

We can emulate the slow performance by setting :max_concurrency to a value less than 4.

SHELL
iex >  Task.async_stream(1..20, fn phone_number -> send_message(phone_number) end, max_concurrency: 2) |> Stream.run()

When the concurrency limit is set to 2, it takes more time to complete compared to using the default value set, 10. This is due to the fact that with a lower concurrency limit, fewer tasks are processed concurrently.

When setting max_concurrency, consider your system resources. Verify that the system has enough resources to handle the specified concurrency limit effectively and also bear in mind the need for performance. Depending on what works for your use case, you can decrease or increase the concurrency limit.

Our application aims to send messages to a million phone numbers. At present, the max_concurrency setting on my machine is set to 10 and is working satisfactorily. However, it is taking a long time to process all the messages. After 17 minutes, only about 3,000 messages have been sent. To improve the processing speed, we need to increase the concurrency limit. I shall set it to 100, allowing more items to be processed concurrently, while also ensuring we do not overload the system.

SHELL
iex > 1..20
    > |> Task.async_stream( fn phone_number -> send_message(phone_number) end, max_concurrency: 100)
    > |> Stream.run()

After increasing the max_concurrency to 100:

In 4 minutes, about 6,000 messages were sent.
There is no spike in memory allocation when we open the observer.

Here's the observer memory allocation when max_concurrency is set to 10:

And here it is when max_concurrency is set to 100:

:ordered

When we execute this code in IEx, you will notice that the results are returned in the same order as the input data:

SHELL
iex > 1..5
    > |> Task.async_stream( fn phone_number -> send_message(phone_number) end, max_concurrency: 100)
    > |> Enum.to_list
 
sending message  to 1
sending message  to 2
sending message  to 3
sending message  to 4
sending message  to 5
 
[
:ok, {:ok, "sent"},
:ok, {:ok, "sent"},
:ok, {:ok, "sent"},
:ok, {:ok, "sent"},
:ok, {:ok, "sent"}
]

This is because we have the :ordered option set to true by default in the Task.async_stream/3 function.

However, setting :ordered to true can result in slower processing if a task takes longer to complete. This is because Task.async_stream/3 will wait for a slow task to finish before moving on to the next one. Therefore, it is important to consider the trade-off between ordered results and processing speed when using this function.

To improve processing speed, you can disable ordering by setting the :ordered option to false. This way, Task.async_stream/3 won't wait for a slow task to complete processing before moving on to the next task.

Let's introduce a slow process in our Sender application.

ELIXIR
defmodule Sender do
  def send_message(3) do
    # Simulate slow processing time
    Process.sleep(4000)
    IO.puts("Sending message to 3")
 
    {:ok, "sent", 3}
  end
 
  def send_message(phone_number) do
    # Simulate some processing time
    Process.sleep(3000)
    IO.puts("Sending message to #{phone_number}")
    {:ok, "sent", phone_number}
  end
 
  # Asynchronous version using Task.async_stream/3
  def send_to_all(phone_numbers) do
    phone_numbers
    |> Task.async_stream(fn phone_number -> send_message(phone_number) end)
    |> Enum.to_list()
  end
end

The send_message/1 function accepts one argument, a phone number. If the phone number is 3, the function simulates a slow process by sleeping for 4 seconds. Otherwise, it simulates a regular process by sleeping for 3 seconds. The output result includes the phone number that's being processed, which allows us to check the order of the returned result.

SHELL
iex > Sender.send_to_all(1..5)
 
sending message  to 1
sending message  to 2
sending message  to 4
sending message  to 5
sending message  to 3
 
[
{:ok, {:ok, "sent"}, 1},
{:ok, {:ok, "sent"}, 2},
{:ok, {:ok, "sent"}, 3},
{:ok, {:ok, "sent"}, 4},
{:ok, {:ok, "sent"}, 5}
]

The print message of number 3 is displayed last, indicating that it took longer to process before sending. However, the collected list is returned in the same order as the given input. This means that, while number 3 took longer to complete, numbers 4 and 5 had to wait before being operated on.

In our case, we want to check whether the status of the messages sent to the given phone numbers was successful or not. To speed up things, let's disable the :ordered option by setting it to false, since we don't care about the order.

ELIXIR
defmodule Sender do
  def send_message(3) do
    # Simulate slow processing time
    Process.sleep(4000)
    IO.puts("Sending message to 3")
 
    {:ok, "sent", 3}
  end
 
  def send_message(phone_number) do
    # Simulate some processing time
    Process.sleep(3000)
    IO.puts("Sending message to #{phone_number}")
    {:ok, "sent", phone_number}
  end
 
  # Asynchronous version using Task.async_stream/3
  def send_to_all(phone_numbers) do
    phone_numbers
    |> Task.async_stream(fn phone_number -> send_message(phone_number) end, ordered: false)
    |> Enum.to_list()
  end
end
SHELL
iex > Sender.send_to_all(1..5)
 
sending message  to 1
sending message  to 2
sending message  to 4
sending message  to 5
sending message  to 3
 
[
{:ok, {:ok, "sent"}, 1},
{:ok, {:ok, "sent"}, 2},
{:ok, {:ok, "sent"}, 4},
{:ok, {:ok, "sent"}, 5},
{:ok, {:ok, "sent"}, 3},
]

The number 3 is collected last in the returned result. This way, we can be sure that Task.async_stream/3 won't be idle waiting for the processing of number 3 to complete, before moving to the next.

:timeout

The Task.async_stream/3 function has a :timeout option which sets a limit on how long each task can run. By default, the timeout is set to 5000 milliseconds or 5 seconds. You can specify the time limit in milliseconds or set it to :infinity if you want to allow the task to run indefinitely. If a task takes longer than the specified timeout, it will raise an exception and terminate the current process.

ELIXIR
defmodule Sender do
  def send_message(3) do
    # Simulate slow processing time
    Process.sleep(7000)
    IO.puts("Sending message to 3")
 
    {:ok, "sent", 3}
  end
 
  def send_message(phone_number) do
    # Simulate some processing time
    Process.sleep(3000)
    IO.puts("Sending message to #{phone_number}")
    {:ok, "sent", phone_number}
  end
 
  # Asynchronous version using Task.async_stream/3
  def send_to_all(phone_numbers) do
    phone_numbers
    |> Task.async_stream(fn phone_number -> send_message(phone_number) end, ordered: false)
    |> Enum.to_list()
  end
end

Here, the processing time of the slow process/task is increased to 7000ms, which exceeds the default timeout in Task.async_stream/3.

SHELL
iex > Sender.send_to_all(1..5)
 
sending message  to 1
sending message  to 2
sending message  to 4
sending message  to 5
 
** (exit) exited in: Task.Supervised.stream(5000)
    ** (EXIT) time out
    (elixir 1.15.5) lib/task/supervised.ex:314: Task.Supervised.stream_reduce/7
    (elixir 1.15.5) lib/enum.ex:4387: Enum.reverse/1
    (elixir 1.15.5) lib/enum.ex:3704: Enum.to_list/1
    iex:3: (file)

When we execute the Sender.send_to_all(1..5) function in IEx, an exception is raised, which stops the stream and crashes the current process. This is because the slow task takes more than 5000ms to complete, while Task.async_stream/3 has a timeout limit of 5000ms.

:on_timeout

It's difficult to predict the duration of a task, as several factors can contribute to its slow processing. For instance, processing a large amount of data can be time-consuming, as can waiting for a slow third-party API to respond.

Instead of allowing Task.async_stream/3 to raise an exception that stops the stream, we can use the :on_timeout option by setting it to :kill_task. This option determines the action to take when the task times out. Setting it to :kill_task will cause Task.async_stream/3 to ignore the process that exits with a timeout and continue with other tasks.

By default, it's set to :exit. This results in the task exceeding the timeout to stop the stream and crash the current process, as seen with the :timeout option.

ELIXIR
defmodule Sender do
  def send_message(3) do
    # Simulate slow processing time
    Process.sleep(7000)
    IO.puts("Sending message to #{3}")
    {:ok, "sent", 3}
  end
 
  def send_message(phone_number) do
    # Simulate some processing time
    Process.sleep(3000)
    IO.puts("Sending message to #{phone_number}")
    {:ok, "sent", phone_number}
  end
 
  # Asynchronous version using Task.async_stream/3
  def send_to_all(phone_numbers) do
    phone_numbers
    |> Task.async_stream(fn phone_number -> send_message(phone_number) end,
      ordered: false,
      on_timeout: :kill_task
    )
    |> Enum.to_list()
  end
end

Add the :on_timeout option and set it to :kill_task in Task.async_stream/3. Then, execute Sender.send_to_all(1..5) in IEx. We can observe that the other tasks are processed completely, while the slow process is ignored, and returns {:exit, :timeout} instead of crashing.

SHELL
iex > Sender.send_to_all(1..5)
 
sending message  to 1
sending message  to 2
sending message  to 4
sending message  to 5
 
[
{:ok, {:ok, "sent"}, 1},
{:ok, {:ok, "sent"}, 2},
{:ok, {:ok, "sent"}, 4},
{:ok, {:ok, "sent"}, 5},
exit: :timeout
]

Before we wrap up, let's take a very quick look at monitoring memory using Observer.

Monitor Memory with Erlang Observer

Let's use Erlang Observer to monitor memory allocation. We can compare memory usage when defining the send_to_all/1 function using Task.async_stream/3 and using a combination of Enum.map/2 and Task.async/1.

ELIXIR
defmodule Sender do
  def send_message(3) do
    # Simulate slow processing time
    Process.sleep(7000)
    IO.puts("Sending message to #{3}")
    {:ok, "sent", 3}
  end
 
  def send_message(phone_number) do
    # Simulate some processing time
    Process.sleep(3000)
    IO.puts("Sending message to #{phone_number}")
    {:ok, "sent", phone_number}
  end
 
  # Asynchronous version using Task.async_stream/3
  def send_to_all(phone_numbers) do
    phone_numbers
    |> Task.async_stream(fn phone_number -> send_message(phone_number) end,
      max_concurrency: 100,
      ordered: false,
      on_timeout: :kill_task
    )
    |> Stream.run()
  end
end
ELIXIR
defmodule Sender do
  def send_message(3) do
    # Simulate slow processing time
    Process.sleep(7000)
    IO.puts("Sending message to #{3}")
    {:ok, "sent", 3}
  end
 
  def send_message(phone_number) do
    # Simulate some processing time
    Process.sleep(3000)
    IO.puts("Sending message to #{phone_number}")
    {:ok, "sent"}
  end
 
  # Asynchronous version using Task.async/1
  def send_to_all(phone_numbers) do
    phone_numbers
    |> Enum.map(fn phone_number ->
      Task.async(fn -> send_message(phone_number) end)
    end)
  end
end

The combination of Task.async/1 and Enum.map/2 can significantly impact memory consumption compared to using Task.async_stream/3.

Task.async_stream/3 is a powerful tool for effectively utilizing concurrency without overloading system resources when working with a series of tasks.

Here are a couple of benefits of using Task.async_stream/3:

It prevents sudden spikes in system usage: By setting the concurrency limit option, you can control the number of concurrent tasks being executed at any given time. This helps prevent the system from becoming overwhelmed with too many tasks running simultaneously, which could lead to spikes in resource usage, such as memory or CPU.
It handles back pressure: Back pressure occurs when there's resistance to the progress of turning input to output. By setting the concurrency limit, Task.async_stream/3 ensures that tasks are processed at a manageable rate, preventing resource exhaustion.

And that's it!

Wrapping Up

Elixir has several tools that are useful when it comes to leveraging concurrency, and Task processes is one of them.

In this post, we explored the concept of concurrency and some of the issues we might face when dealing with a series of tasks while using concurrency.

We then explored the use of Task.async_stream/3, a Task module function that is effective in handling a large number of tasks, as it provides both concurrency and performance.

Happy coding!

P.S. If you'd like to read Elixir Alchemy posts as soon as they get off the press, subscribe to our Elixir Alchemy newsletter and never miss a single post!

Published Jun 25, 2024
