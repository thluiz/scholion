---
url: "https://dockyard.com/blog/2020/04/01/refactoring-a-function-in-elixir"
captured_at: "2026-11-16T03:09:54+00:00"
title: "Refactoring a Function in Elixir - DockYard"
domain: "dockyard-com"
---

![White markee light shaped like a question mark](https://assets.dockyard.com/images/White%20markee%20light%20shaped%20like%20a%20question%20mark-large.webp)

![Zach Liss](https://s3.amazonaws.com/dockyard-com-production/images/team-monster-09.png)

Over the past year, I have been using my DockYard Days (time dedicated to professional development and passion projects) and some free time to pick up Elixir. I've read a few textbooks, worked through this year's [Advent of Code](https://adventofcode.com/) programming puzzles, and participated in DockYard's Mentor/Mentee Program. Throughout this learning process, I've also been working towards building a small quiz game to practice implementing various concepts as I come across them.

Recently, I've wrapped up Part 1 of _[Designing Elixir Systems with OTP](https://pragprog.com/book/jgotp/designing-elixir-systems-with-otp)_ and felt this was a great opportunity to revisit and **refactor some of the old code I've written with core programming principles** demonstrated in the book.

## Core programming principles

*   Build functions at a single level of abstraction
*   Make decisions in function heads where possible
*   Name concepts with functions
*   Shape functions for composition
*   Build single-purpose functions

Let's step through applying these core principles to an `answer_question` function from the quiz game application. `answer_question` lives inside of a `Game` module and handles the logic around what should happen when a user with a `user_name` attempts to answer a `question` with a `guess`.

```
# game.ex

def answer_question(%Game{current_question: current_question} = game, guess, user_name) do
 case(current_question.mascot == guess) do
 true ->
 game =
 game
 |> increase_score_for_user(user_name)
 |> check_for_winning_user(user_name)
 |> Map.put(:current_question, get_random_question())

 {:ok, game}

 _ ->
 {:error, :incorrect}
 end
 end
```

## Functions should be at single layer of abstraction

Our `answer_question` function currently has three different layers of abstraction.

*   `case(current_question.mascot == guess) do` - We're making a decision at the `guess` level to determine if the response from a user is correct
*   `game = game |> increase_score_for_user(user_name) |> check_for_winning_user(user_name)` - Game level operations occur as we a advance our `game` token.
*   `|> Map.put(:current_question, get_random_question())` - Elixir datatypes level abstraction

The first thing we can do is rework the pipeline. The `|> Map.put(:current_question, get_random_question())` can be pulled into a single purpose and composable function.

```
# game.ex

def answer_question(%Game{current_question: current_question} = game, guess, user_name) do
 case(current_question.mascot == guess) do
 true ->
 game =
 game
 |> increase_score_for_user(user_name)
 |> check_for_winning_user(user_name)
 |> select_question() # add select_question() to the pipeline

 {:ok, game}

 _ ->
 {:error, :incorrect}
 end
end

defp select_question(game) do
 Map.put(game, :current_question, get_random_question())
end
```

With the above change, we've also touched on three more core principles:

*   Name concepts with functions
*   Shape functions for composition
*   Build single-purpose functions

`select_question` was created to name the `Game` level concept of selecting a question. The only purpose of the function is to wrap an Elixir datatype operation. We shaped it for composition in our pipeline by accepting the `%Game{}` as the first argument and also returning it.

Next we can create a new `Response` module to abstract away determining the "correctness" of a `guess`. In `answer_question`, we create a new response and use `response.correct` in our case statement.

```
# response.ex

defmodule Response do
 defstruct ~w[guess game user_name correct]a

 def new(game, guess, user_name) do
 %__MODULE__{
 guess: guess,
 user_name: user_name,
 game: game,
 correct: correct?(game, guess)
 }
 end

 defp correct?(%Game{current_question: current_question} = game, guess) do
 current_question.mascot == guess
 end
end
```

```
# game.ex

def answer_question(%Game{current_question: current_question} = game, guess, user_name) do
 response = Response.new(game, guess, user_name)
 case(response.correct) do
 true ->
 game =
 game
 |> increase_score_for_user(user_name)
 |> check_for_winning_user(user_name)
 |> select_question() # add select_question() to the pipeline

 {:ok, game}

 _ ->
 {:error, :incorrect}
 end
end
```

This is a good start. The overall intention of this function is easier to understand now that we've updated it to only use one level of abstraction. We can do better and continue to break it up further.

## Make decisions in function heads where possible

Now that `response.correct` is stored in a struct, we can remove the `case` statement in favor of some additional clauses for the `answer_question` function.

```
# game.ex

def answer_question(%Game{current_question: current_question} = game, guess, user_name)
 when is_binary(guess) do
 response = Response.new(game, guess, user_name)
 answer_question(game, response, user_name)
end

def answer_question(game, %Response{correct: true} = response, user_name) do
 game =
 game
 |> increase_score_for_user(user_name)
 |> check_for_winning_user(user_name)
 |> select_question()

 {:ok, game}
end

def answer_question(_game, %Response{correct: false} = response, _user_name) do
 {:error, :incorrect}
end
```

By adding several new `answer_question` clauses which pattern match on `%Response{correct: true}` and `%Response{correct: false}` we've pulled the decision from the previous `case` statement and reduced each function to a single purpose.

## Wrap Up

So far `Designing Elixir Systems with OTP` has provided some handy tools. I feel that these programming principles will continue to help me write code that has clearer intentions, is testable, and remains maintainable over time. I'm looking forward to seeing what's next in Part 2!

_[DockYard](https://dockyard.com/) is a digital product agency offering custom software, mobile, and web application development consulting. We provide exceptional professional services in strategy, user experience, design, and full stack engineering using Ember.js, React.js, Ruby, and Elixir. With a nationwide staff, we've got consultants in key markets across the United States, including San Francisco, Los Angeles, Denver, Chicago, Austin, New York, and Boston._

### Stay in the Know

Get the latest news and insights on Elixir, Phoenix, machine learning, product strategy, and more—delivered straight to your inbox.

![Narwin holding a press release sheet while opening the DockYard brand kit box](https://assets.dockyard.com/images/narwin-press-release-og-v2.svg)
