---
title: "Pseudo Random Number Generation in Elixir"
date: '2015-02-03T07:25:35-03:00'
category: webclip
summary: 'The post explains why Elixir relies on Erlang for pseudo-random numbers, how deterministic seeds affect :random.uniform, and why :crypto can provide better seeds than timestamps or :erlang.now.'
tags: ["elixir", "erlang", "random-number-generation", "genetic-algorithms"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Pseudo Random Number Generation in Elixir - Neo | Ideas"
    url: "http://www.neo.com/2014/02/24/pseudo-random-number-generation-in-elixir"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-02/neo-com--pseudo-random-number-generation-in-elixir.md"
    kind: repo
---

The post starts from a genetic algorithm in Elixir and uses it to explain why random numbers matter in software. It distinguishes true random number generators from pseudo random number generators, then turns to Erlang’s approach, where the seed must be set explicitly.

## Reading notes

- Genetic algorithms depend on random numbers to create initial populations, generate child solutions, and mutate solutions.
- True random number generators use natural phenomena, are non-deterministic, and are non-periodic, but are slower and less efficient.
- Pseudo random number generators are deterministic and periodic, but produce numbers that are random enough for many tasks.
- Elixir uses Erlang’s random number generation instead of implementing its own.
- Erlang does not seed the PRNG automatically.
- Without changing the seed, :random.uniform returns the same sequence after restarting the Beam VM.
- Calling :random.seed with the default seed keeps producing the same pattern.
- Using :os.timestamp as the seed changes the sequence, and reseeding resets the PRNG without restarting iex.
- :os.timestamp can fail as a unique seed in concurrent code because calls may happen within the same clock tick.
- :erlang.now provides a unique timestamp, but can move the Beam VM clock ahead of the system clock and cause clock skew.
- :crypto.rand_bytes can be pattern matched into three integers and passed to :random.seed.
- Seeding from :crypto avoids clock skew and gives unique values.
- The post notes that :random.uniform has a short period and that a Mersenne Twister implementation would be better for genetic algorithms.
- The conclusion recommends setting a seed before generating pseudo-random numbers and considering :crypto for seeding.
- The conclusion also advises caution with :erlang.now and suggests :os.timestamp when it fits better.
