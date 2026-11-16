---
url: "https://dev.to/youroff/a-case-study-for-property-based-testing-in-elixir-44c6"
captured_at: "2026-11-16T02:02:51+00:00"
title: "A case study for property based testing in Elixir"
domain: "dev-to"
---

It's been a while since I learned about property based testing, yet I never had a chance to apply it in my work. Property based testing is a stochastic process, in which your code is being bombarded with multiple combinations of examples, and output is checked for compliance to some condition that is supposed to hold on all inputs. The idea of describing and checking higher level properties of some code is just as beautiful as impractical in many areas of programming. In particular, in web development, where logic is usually intertwined with the database layer. Running hundreds of instances of the same test would introduce prohibitive overhead. This explains why I have not even attempted to adopt it before.

Let's take for example this little function:  

```
def add(a, b) do
  a + b
end
```

Suppose I meant it to be used with positive integers and I want to make sure that the result is always equal or greater than either operand. Kinda silly, but this is just an example. Let's describe this assumption then:  

```
property "result of addition always >= of each operand" do
  check all a <- integer(),
            b <- integer()
  do
    s = add(a, b)
    assert s >= a && s >= b
  end
end
```

This fails (expectedly):  

```
Failed with generated values (after 1 successful run):

  * Clause:    a <- integer()
    Generated: -1

  * Clause:    b <- integer()
    Generated: 0
```

Right! We forgot about negative ints. In order to make fix comprehensive, we need to both add a guard to the function itself and bound the input stream. Whenever we do `var <- integer()`, it means instantiation of a particular value out of the stream of integers. Since we don't want just _any_ integer, we should be able to apply a filter somehow. Even though the library provides specified `positive_integer()` generator, it does not suit our needs, because it filters out zeroes as well. Instead we apply filter to the stream:  

```
def add(a, b) when a >= 0 and b >= 0 do
  a + b
end

property "result of addition always >= of each operand" do
  check all a <- filter(integer(), &(&1 >= 0)),
            b <- filter(integer(), &(&1 >= 0))
  do
    s = add(a, b)
    assert s >= a && s >= b
  end
end
```

Now test passes. We could go on with improvements by creating a custom generator, but instead I wanted to move to the first useful and successful use of property based testing in my practice. Meanwhile feel free to dig deeper into [StreamData docs](https://hexdocs.pm/stream_data/ExUnitProperties.html#content) to learn more about API of the library that was almost included into Elixir itself.

## [](#real-life-example)Real life example

Recently, while working on a `poll` feature for a social app, I ran into the issue of distributing percents. There are multiple options with the poll, each option has an integral number of votes greater or equal than zero, there is a total number of votes as well. What I needed is to hide the absolute numbers of voters and convert these numbers into percents, while making sure they add up to 100% or 0% if there were no votes whatsoever. The main issue I expected was rounding errors. Simple example:  

```
4.5 + 5.5 == 10.0
round(4.5) + round(5.5) == 11
```

With different distributions of votes, rounding can introduce overflows as well as underflows.

[![Russian miracle: vote percentages sum up to 146%](https://res.cloudinary.com/practicaldev/image/fetch/s--2blpsbHM--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/x8hmeuf8khkv776tb21k.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--2blpsbHM--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/x8hmeuf8khkv776tb21k.png)

While 146% of votes might be okay for Russian politics, I wanted to avoid that. And the original approach was to maintain some accumulator initialized at 100 and return it at the last option.  

```
@doc """
Computing percent for all options using total_votes
and option_votes in Poll and Option respectively.
This function makes sure that integral percents
sum up properly to 100%.
"""
@spec distrib_votes(%Poll{}, [%Option{}]) :: [%Option{}]
def distrib_votes(poll, options, acc \\ 100)

def distrib_votes(%Poll{total_votes: 0}, options, _) do
  options
end

def distrib_votes(_, options, percent)
  when options == [] or percent <= 0
do
  options
end

def distrib_votes(_, [option], percent) do
  [%{option | percent: percent}]
end

def distrib_votes(poll, [option | options], percent) do
  p = round(100 * option.option_votes / poll.total_votes)
  option = %{option | percent: min(p, percent)}
  [option | distrib_votes(poll, options, percent - p)]
end
```

When I tried to come up with meaningful and comprehensive test cases, I realized that it slips out of my control and I recalled property based testing. Really, this little function does not need the database, and the assertion is extremely easy to formulate: the sum of the percents should either equal to 100% or 0% if there is no votes:  

```
property "distrib_votes always sums to either 100 or 0" do
  check all votes <- list_of(filter(integer(), & &1 >= 0)) do
    options = Enum.map(votes, & %Option{option_votes: &1})
    total_votes = Enum.sum(votes)
    poll = %Poll{total_votes: total_votes}
    total_percents = Feed.distrib_votes(poll, options)
    |> Enum.map(&(&1.percent))
    |> Enum.sum()
    assert total_votes > 0  && total_percents == 100
        || total_votes == 0 && total_percents == 0
  end
end
```

These were the final versions of the test and function definition. Initially I failed to define correct assertion by setting a naive condition `total_percents == 100 || total_percents == 0` and of course it would allow for a buggy behavior, where no votes poll would show 100% at the last option. Using implicative form (precondition) fixed that and proved that the test is just as good or as bad, as the logic behind it.
