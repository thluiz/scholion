---
url: "https://saadh393.github.io/blog/adapter-port-architecture-two-cases"
captured_at: "2026-06-04T17:12:19+01:00"
title: "Ports and Adapters (Hexagonal Architecture), Explained with Two Real Codebases — Saad Hasan"
domain: "saadh393-github-io"
---

---
Imagine you're in a standup and finance says the email bill is too high. The plan is to move to a cheaper provider by the end of the month. Easy enough, you think. Then you search the codebase for the old email SDK and find twenty-eight files using it. Order confirmations sit in the order service. Password resets are in auth. Refund notices live in the admin panel. Weekly digests run in a cron job nobody has opened in a year. Every one of them calls the email SDK directly, in its own way, with its own retry logic and its own template quirks.

Now the small task isn't small. Twenty-eight files to read, twenty-eight to change, and twenty-eight chances to quietly break a real email flow because the new provider reports errors in a slightly different shape.

If that feeling is familiar, this post is for you. So is the moment you look at a payment integration and tell yourself "we'll never swap this," while knowing the company will probably ask for a second provider in six months. Or the time a frontend team sat blocked for weeks because the backend wasn't ready. These look like three different problems, but they're the same one underneath. There's a simple pattern that solves all three.

We'll start with the idea itself, then walk through two real projects that used it. One backend, one frontend.

## Why this pattern exists

Most code that talks to the outside world slowly gets tangled with whatever it's talking to. You import the Stripe SDK, and before long Stripe-specific words show up in checkout, in refunds, in the webhook handlers. You import the SendGrid SDK, and the same thing spreads to every spot that sends mail.

For a while none of this hurts. There's one provider, the code works, you move on. Then something shifts. A cheaper option shows up. A new region needs a local provider. A vendor raises prices, or goes down, or changes their API without much warning. The moment you have to react, the cost of reacting is tied to one number: how many files mention that vendor by name.

So the real problem isn't the vendor. It's coupling. When your business logic knows the exact shape of an outside thing, every change to that outside thing leaks back into your business logic.

◆ Insight

The pain isn't writing the integration. It's everywhere the integration leaks. A clean integration in one file is fine. The same integration sprinkled across thirty files is what hurts.

## How the pattern works

The fix is one move. Put an interface between your business logic and the outside world, and let the business logic depend only on that interface, never on the provider directly.

Think of a wall socket. Your charger doesn't care which power company is behind the wall. It plugs into a standard socket and pulls power. The power company can change, but your charger keeps working because it only ever talked to the socket.

That's the whole pattern. Business logic is the charger. The provider is the power company. The socket is the piece we add in the middle, and it has three parts.

The **port** is the socket. It's an interface that says what our code wants to do in our own words. "Send an email." "Charge a card." "Get the standings." No Stripe, no SendGrid, no HTTP. Just a contract.

An **adapter** is the plug that fits the socket. Each one wraps a single provider and translates between our words and theirs. The Stripe adapter knows Stripe. The bKash adapter knows bKash. The business logic knows neither.

The **registry** is the switch that decides which plug is in the socket at runtime. It's the one file that knows the wiring, usually a registry or a factory.

Port

Interface in our domain language. No SDK names. No HTTP. Pure contract.

→

Adapter

Concrete implementation. Wraps one provider. Translates to and from the port shape.

→

Registry

The only file that knows which adapter is active. Business logic never imports adapters directly.

→

It helps to play with it. The hexagon below is our business logic. The six dots on its edges are ports. Click any of the adapter buttons on the right to wire a different one into a port. Watch the registry at the bottom update.

Ports and adapters, wired liveclick an adapter to wire it

// registry.ts — runtime wiring

export const registry \= {

payments: "bKash",

mailer : "Resend",

sms : "Twilio",

storage : "S3",

search : "Meilisearch",

queue : "SQS",

};

Notice what changes in the registry and what doesn't. Swapping a payment provider only changes one line of wiring. The hexagon, which is everything calling those ports, never moves.

This is what the books call [hexagonal architecture](https://en.wikipedia.org/wiki/Hexagonal_architecture_%28software%29), or ports and adapters, or onion architecture. The names point at the same idea drawn slightly differently. Stuff inside doesn't know about stuff outside.

## The shape on disk

Three folders. That's most of what we need to remember.

A real backend project skeleton

app▾

checkout.ts← business logic, imports ports only

webhooks.ts← business logic

refunds.ts← business logic

lib▾

payments.ts← PaymentGateway

adapters▾← one file per provider

registry.ts← runtime wiring

The rule that holds it together is simple. Files inside `app/` can import from `lib/ports`. They cannot import from `lib/adapters`. If we keep that one rule, the rest works.

Arrows always point inward, toward the port. Business logic doesn't reach out to adapters. Adapters fit into a shape the business logic already defined. This inversion is the whole trick. It's why books call it "dependency inversion" when they want to sound formal.

The best way to feel that inversion is to run a request through it. Below is a small order. A customer has just clicked Pay Now on a $42 charge. The business logic needs to do two things — charge the card, then send a receipt. For each step, pick which adapter the registry should hand back. Watch the call travel from business logic, through the port, into the adapter, out to the provider, and back. Then change the adapter and run it again. The business logic above doesn't move.

Same business logic, swappable adapterssame business logic, different adapters

scenarioOrder #1042 — $42.00 — customer@example.com

step 1 of 3Charge the card

Business logic calls gateway.createCharge(). The registry decides which provider answers.

pick adapter for PaymentGateway

Business Logicgateway.createCharge({ amount: 4200, currency: "USD" })

Port: PaymentGatewayinterface contract

Stripetranslates the call

stripe.comreal service

the call leaves business logic, passes through the port, hits the adapter, then the provider

// runtime log

waiting for the first call…

Run it once with Stripe and Resend. Then reset and run it with bKash and SES. The call lines, the business logic, every word above the registry stays identical. Only the registry resolves a different adapter on each run. That's the whole pitch in motion.

## Adding Stripe to a codebase that only knew bKash

We were running a Node.js backend for a marketplace in Bangladesh. bKash was the primary payment provider. Six months in, the product team wanted Stripe for international cards, with SSLCommerz as a fallback. When we joined, every checkout route, every webhook handler, every refund script imported the bKash SDK directly.

The first thing we did was sketch the port. No code yet, just the interface. What does our business logic want to do with a payment provider? Four things.

Open the editor below. The sidebar shows the whole shape of the project. `ports/payments.ts` is the contract, `checkout.ts` is the only business logic file the rest of the app cares about, and the three adapters in `adapters/` each wrap one SDK behind that same contract. Click any tab to read the file. Notice how the port has no provider names in it, and the business logic has no SDK imports.

lws-marketplace · payment refactorapp/checkout.ts

app›checkout.ts

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

```
<span><span>import</span><span> { getPaymentGateway } </span><span>from</span><span> "@/lib/registry"</span><span>;</span></span>
<span><span>import</span><span> { markOrderFailed } </span><span>from</span><span> "@/lib/orders"</span><span>;</span></span>
<span><span>import</span><span> type</span><span> { Order } </span><span>from</span><span> "@/lib/types"</span><span>;</span></span>
<span></span>
<span><span>export</span><span> async</span><span> function</span><span> checkout</span><span>(</span><span>order</span><span>:</span><span> Order</span><span>) {</span></span>
<span><span>  // business logic</span></span>
<span><span>  const</span><span> gateway</span><span> =</span><span> getPaymentGateway</span><span>(order.region);</span></span>
<span></span>
<span><span>  const</span><span> charge</span><span> =</span><span> await</span><span> gateway.</span><span>createCharge</span><span>({</span></span>
<span><span>    amount: order.total,</span></span>
<span><span>    currency: order.currency,</span></span>
<span><span>    reference: order.id,</span></span>
<span><span>    customerEmail: order.email,</span></span>
<span><span>  });</span></span>
<span></span>
<span><span>  // business logic continues</span></span>
<span><span>  if</span><span> (charge.status </span><span>===</span><span> "failed"</span><span>) {</span></span>
<span><span>    await</span><span> markOrderFailed</span><span>(order.id);</span></span>
<span><span>    return</span><span> null</span><span>;</span></span>
<span><span>  }</span></span>
<span><span>  return</span><span> charge.id;</span></span>
<span><span>}</span></span>
<span></span>
```

● maintypescriptUTF-8LFSpaces: 223 lines · 6 files

Notice what's missing from the port. No bKash, no Stripe, no `paymentID`, no `statusCode`. Just our words. The adapters carry the SDK weight. The business logic file stays the same whether bKash, Stripe, or SSLCommerz is on the other end.

The payoff lives in what we didn't have to write. When Stripe finally landed in production, the change was one new file in `adapters/` plus one line in `registry.ts`. Checkout didn't move. Webhook handlers didn't move. The refund flow didn't move. We shipped it on a Tuesday afternoon and went home.

✓ Result

Adding Stripe took about a day, including writing the adapter, mapping its error codes, and adding a feature flag in the registry. The original bKash integration had taken roughly a week. The difference is everything that didn't need to move.

A few months later bKash changed one field in their response shape during a minor SDK update. The fix was four lines, all of them in `adapters/bkash.ts`. The rest of the codebase didn't notice.

This is where the pattern actually pays back. Not in the first integration, where it costs a bit more than a direct SDK call. In the second integration, the third, and every silent SDK change after that.

## Forty places that sent emails, all written differently

Same codebase, different mess. About forty places sent emails. Order confirmations, password resets, refund notices, two-factor codes, weekly digests, admin alerts. Each one called the email SDK its own way. Some passed raw HTML. Some used template IDs. The signup flow had a retry loop. The refund flow had no retry at all. The audit log was inconsistent at best.

When the company wanted to switch providers for cost reasons, engineering quietly avoided the topic for three weeks. Nobody wanted to read forty files and change forty things.

The fix was the same shape. A `Mailer` port with two methods. Adapters for the old provider and the new one. A registry to switch between them.

```
<span data-line=""><span>// app/lib/ports/mailer.ts</span></span>
<span data-line=""><span>export</span><span> interface</span><span> Mailer</span><span> {</span></span>
<span data-line=""><span>  send</span><span>(</span><span>to</span><span>:</span><span> string</span><span>, </span><span>subject</span><span>:</span><span> string</span><span>, </span><span>body</span><span>:</span><span> string</span><span>)</span><span>:</span><span> Promise</span><span>&lt;</span><span>void</span><span>&gt;;</span></span>
<span data-line=""><span>  sendTemplate</span><span>(</span></span>
<span data-line=""><span>    to</span><span>:</span><span> string</span><span>,</span></span>
<span data-line=""><span>    templateId</span><span>:</span><span> string</span><span>,</span></span>
<span data-line=""><span>    vars</span><span>:</span><span> Record</span><span>&lt;</span><span>string</span><span>, </span><span>unknown</span><span>&gt;</span></span>
<span data-line=""><span>  )</span><span>:</span><span> Promise</span><span>&lt;</span><span>void</span><span>&gt;;</span></span>
<span data-line=""><span>}</span></span>
```

The interesting part was the migration path. We didn't rip everything out at once. We added the port and an adapter for the existing provider, then migrated calling sites one at a time over a couple of weeks. Each PR replaced one direct SDK call with `mailer.send(...)`. Small, boring, easy to review. When the last calling site was migrated, switching the provider was a one-line change.

Week 1

Port and first adapter

Defined Mailer interface. Wrote adapter for current provider. Added registry. Zero calling sites migrated yet.

Weeks 2-3

Migrate calling sites

One PR per file. Replaced direct SDK calls with mailer.send. Added retry and audit log behind the port for free.

Week 4

Second adapter

Wrote adapter for the new provider against the same port. Tested in staging.

Week 4

Flip the registry

One-line change. Production traffic moved to the new provider. No calling site touched.

The bigger win turned out to be the retry and audit log added behind the port. Once there was one place to do those things, doing them consistently was free. Before the migration, only some emails had retries. After, every email did. Nobody wrote any retry code in calling sites. It just happened inside the adapter.

## Three weeks of frontend work with no backend

Different project, different pain. We were building a sports tracking dashboard. Standings, player ranks, live matches, upcoming fixtures. Designs were approved. The frontend team had three weeks to ship before launch. The backend team had six weeks of work ahead of them.

The reflex move would have been mocking. Stub fetch with hardcoded data, ship the UI, swap to real APIs later. That works fine for one or two endpoints. We had a couple dozen and they were going to land at different times over six weeks. We needed something more disciplined than mocks.

So we did adapter port on the frontend. Components called functions like `getStandingsRepo().listGroups()`. Whether that came back from an in-memory array or a real fetch was the registry's problem, not the component's.

app/lib in the frontend project

app▾

standings.ts← StandingsRepo, GroupStandings

player-ranks.ts← PlayerRanksRepo

matches.ts← MatchesRepo (getCurrent, listPast)

fixtures.ts← FixturesRepo (listUpcoming)

static▾← in-memory adapter

registry.ts← per-resource toggle

The key move was that the static adapters returned the exact shape the real APIs would later return. We sat with the backend team for two afternoons before any code got written and agreed on response shapes. The frontend team built against those shapes using hardcoded data. The backend team built the real endpoints to match.

When backend shipped the standings endpoint first, we flipped one toggle in the registry. The standings page started running on real data. No component changed. Player ranks shipped two weeks later. Same flip. Fixtures shipped last. By launch every page was on real data and not a single component file got touched during the migration.

◆ Insight

Mocking is for temporary stubs. Adapter port is for when "temporary" lasts six weeks and the swap will happen one endpoint at a time.

There was a side effect we didn't plan. The static adapters stayed in the repo, kept around for tests and storybook. Anyone running a component test gets predictable data without spinning up an API. That came for free.

Know a frontend engineer who's about to spend three weeks waiting on a backend that isn't ready? Send them this story before they start mocking.

## What we actually gain

The headline benefit is the obvious one. We can swap implementations without touching calling code. The pattern delivers on that, repeatedly.

The less obvious benefits are usually bigger.

2Files changed when adding the second payment provider

1Files changed when switching email providers

0Component files touched during frontend API migration

4Lines changed to fix a bKash response shape regression

Tests get simpler. We hand the test a fake adapter that implements the port. No `jest.mock()`, no module patching, no clever spies. The test just gets a different implementation.

Parallel work unblocks. Frontend builds against a static adapter while backend designs the real API. Backend ships endpoints in any order. Neither side blocks the other.

The calling code gets cleaner whether we ever swap or not. When the only way to talk to a provider is through a port, provider-specific weirdness stops leaking everywhere. The codebase reads better even before the first swap.

## What it costs us

It's more files. A direct SDK call lives in one file. The same thing through a port lives in three. On small projects that overhead is real and not worth it.

The port has to be designed well. A bad port leaks the provider into the interface and gives us none of the benefit. If our port has a method called `createBkashPayment`, we didn't write a port. We wrote a wrapper. A real port speaks in our domain language. This is the part beginners get wrong most often, and the part worth slowing down on.

There's a small tax on debugging. When we read `mailer.send(...)` in a stack trace, we have to jump to the registry to see which adapter is active. IDE jump-to-definition handles this, but it's an extra hop.

The first port we design will probably be wrong. We'll learn the right shape by writing the second adapter and feeling where the first one's assumptions break. Plan for one refactor of the port after the second adapter exists.

## When to reach for it

Reach for this when the dependency is one we expect to swap or extend, and the calling code is spread across many files. Payments, email, SMS, search, file storage, queues, third-party APIs, anything billed per call, anything regulated, anything where a vendor change is a realistic six-month possibility.

Also reach for it when we can't yet build the real thing but need to start building against it. Frontend with no backend. A new feature that depends on a service that doesn't exist yet. A migration where the old and new systems both need to run for a while.

## When to skip it

Most of the time. Most code doesn't have this problem. If we're calling a library that's stable, that won't be replaced, that lives in one or two files, we should just call the library. Premature ports cost more than premature optimization because the cost gets paid on every read, not just on the day they're written.

A rule of thumb that's served us well is the rule of two. One implementation and no real plan for a second, don't build the port. Two implementations or a real conversation about adding one, build it. Three, it should already exist.

⇄ Trade-off

Cost of a port is paid on day one and every read after. Benefit is paid the day we swap or extend. No swap, no extension, no benefit. The math is harsh on speculative abstractions.

## What we'd do differently

Two things stand out across all three projects.

First, design the port before writing the first adapter. Both backend times we wrote the bKash code first and the port second, and the port came out shaped like bKash. That's backwards. The port should be shaped like what business logic wants to say, not like what the first provider happens to expose. Writing the port first forces us to think in our own words instead of the vendor's.

Second, keep the fake adapter alive after the real one ships. On the frontend project we almost deleted the static adapters once the real APIs landed. We didn't, and that turned out to be one of the better decisions in the project. Deterministic test data without spinning up an API is too useful to throw away.

Past that, the pattern earns its keep. Two backends and one frontend, three boring migrations that would have been ugly without it, and a team that never had to wait on another team for data. That's the case for it. Nothing more dramatic to add.
