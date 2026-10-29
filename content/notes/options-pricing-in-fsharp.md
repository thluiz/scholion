---
title: "Options pricing in F#"
date: '2015-11-09T18:41:40-03:00'
category: webclip
summary: 'The post explains option pricing in F# through stock-price modeling, then focuses on the binomial model, delta hedging, dividend adjustment, and both imperative and functional implementations.'
tags: ["fsharp", "options-pricing", "binomial-pricing", "delta-hedging"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Options pricing in F#"
    url: "http://www.hoonzis.com/fsharp-options-pricing/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-11/hoonzis-com--options-pricing-in-fsharp.md"
    kind: repo
---

The post explains two common option-pricing methods, Black-Scholes and binomial pricing, then focuses on the binomial model. It first models share-price movement with a generalized Wiener process and the assumption that log returns are normally distributed and independent, then uses that setup to derive a tree-based pricing method.

## Reading notes

- The page presents option pricing in F# and mentions two methods: Black Scholes formula and binomial pricing.
- Black Scholes is described as a closed-form formula for European options.
- Binomial pricing is presented as an algorithmic method that can price diverse financial products.
- The model assumes the stock price has a long-term direction and short-term random oscillation.
- Stock movement is written as a generalized Wiener process: dS = alpha*S*dt + sigma*S*dW.
- The text says daily returns under this process have a log-normal distribution.
- If daily returns are independent, their logarithms are normally distributed.
- The binomial model assumes the share can move up or down in the same way at each step.
- A stock tree and a derivative tree are built to represent the possible paths to maturity.
- The option price is tied to the underlying stock price, so changes in the stock change the option value.
- The post describes a hedged portfolio with shares and a short derivative position that can be made immune to stock-price changes.
- This process of continuously adapting the share position is called delta hedging.
- In a no-arbitrage world without taxes, the hedged portfolio should earn the neutral interest rate.
- The text derives delta from the condition that the portfolio value stays the same and from the growth of the portfolio at the neutral rate.
- Option price P is then expressed as a function of Pu and Pd, the option prices after an up or down move.
- A technical probability p is introduced to simplify that pricing equation.
- If the dividend yield is q, the stock tree changes and p also includes the dividend.
- The Cox, Ross, and Rubinstein model determines the up and down factors from volatility.
- The implementation section presents two F# versions: one imperative and one functional.
- The algorithm first determines the stock and derivative prices at the end nodes.
- It then walks backward through the tree to compute the derivative price at each earlier node.
- For American options, each node also checks whether early exercise is better than holding the option.
- End-node option value is computed with max(S-X,0) for calls and max(X-S,0) for puts.
- The imperative version iterates over and mutates two arrays, one for stock prices and one for option prices.
- The functional version reduces a list of node values step by step with Seq.pairwise.
- The functional rewrite can keep track of both stock price and option price in tuples.
- The last-node prices are generated with a helper that uses unfold to build the sequence.
