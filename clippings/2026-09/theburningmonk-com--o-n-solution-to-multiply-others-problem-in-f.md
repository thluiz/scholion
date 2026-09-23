---
url: "http://theburningmonk.com/2016/12/o-n-solution-to-multiply-others-problem-in-f/?utm_content=42278278&utm_medium=social&utm_source=twitter"
captured_at: "2026-09-23T17:09:38+01:00"
title: "O(n) solution to Multiply Others problem in F# | theburningmonk.com"
domain: "theburningmonk.com"
---

O(n) solution to Multiply Others problem in F#
F#, Programming

Yan Cui

I help clients go faster for less using serverless technologies.

Another tasty challenge that I ran into during my preparation for technical interviews is this seemingly simple problem from Facebook.

input [2,3,1,4]
output [12,8,24,6]

Multiply all fields except it's own position.

Restrictions:
1. no use of division
2. complexity in O(n)

The main challenge is in making the algorithm run in O(n) time.

One solution I saw (and thought it was quite clever) is to maintain two temporary arrays, calculated by multiplying the elements of the input array from front-to-back, and back-to-front.

ie. input is [ 2, 3, 1, 4 ]

The front array starts with [ 1, 0, 0, 0 ], and starting from position 1, we can say front[i] = front[i-1] * input[i-1] and end up with [ 1, 2, 6, 6 ] (which is the product of all the input elements before that position.

The rear array starts with [ 0, 0, 0, 1 ] and starting from position 2 (ie, second to last), we can say rear[i] = rear[i+1] * input[i+1] and end up with [ 12, 4, 4, 1 ].

And finally we can work out the output array by multiplying the corresponding elements in the front and rear arrays, and that runs in O(n) of time and space.

Here's the implementation in F#.

	let multiplyOthers (input : int[]) = 
	  let front = Array.zeroCreate input.Length
	  let rear  = Array.zeroCreate input.Length
	  front.[0] <- 1
	  rear.[input.Length-1] <- 1
	

	  for i = 1 to input.Length-1 do
	    front.[i] <- front.[i-1] * input.[i-1]
	

	  // start from second to last element
	  for i in input.Length-2 .. -1 .. 0 do
	    rear.[i] <- rear.[i+1] * input.[i+1]
	

	  Seq.zip front rear 
	  |> Seq.map (fun (f, r) -> f * r)
	  |> Seq.toArray
	

	multiplyOthers [| 2;3;1;4|]
view raw
multiply_others.fsx hosted with  by GitHub

 

Try it Yourself

Links
Interview question on CareerCup
DotNetFiddle snippet
All my Project Euler solutions in F#
All my Advent of Code solutions in F#

Whenever you're ready, here are 3 ways I can help you:

Production-Ready Serverless: Join 20+ AWS Heroes & Community Builders and 1000+ other students in levelling up your serverless game. This is your one-stop shop for quickly levelling up your serverless skills.
I help clients launch product ideas, improve their development processes and upskill their teams. If you'd like to work together, then let's get in touch.
Join my community on Discord, ask questions, and join the discussion on all things AWS and Serverless.
