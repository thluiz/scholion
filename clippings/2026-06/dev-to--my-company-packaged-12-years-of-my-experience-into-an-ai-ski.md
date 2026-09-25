---
url: "https://dev.to/xulingfeng/my-company-packaged-12-years-of-my-experience-into-an-ai-skill-then-laid-me-off-when-it-crashed-4b3e?context=digest"
captured_at: "2026-06-11T19:19:19+01:00"
title: "My company packaged 12 years of my experience into an AI Skill, then laid me off. When it crashed, the CTO called at 5x my salary. - DEV Community"
domain: "dev-to"
---

---
> A story about knowledge extraction, Kafka consumer rebalance, and what happens when a company discovers their AI Skill knows the past — but not the present.  
> Based on a submission from a community member. If you have a similar story or something you need to get off your chest — reach out. The next one could be yours.

___

**Has your company ever extracted your experience into a system — then decided the system was good enough without you?**

**Have you watched an AI Skill handle 312 scenarios correctly, and wondered whether you'd be around when number 313 finally showed up?**

**This is that story.**

___

## [](https://dev.to/xulingfeng/my-company-packaged-12-years-of-my-experience-into-an-ai-skill-then-laid-me-off-when-it-crashed-4b3e?context=digest#act-1-knowledge-extraction)Act 1 · Knowledge Extraction

The conference room had no windows. Three months.

Every Monday through Thursday I sat in that plastic chair — a voice recorder, a laptop, a mug on the table. Across from me sat an engineer named Caleb. His job was to ask me questions.

"Why PostgreSQL over MongoDB?"

"Why is the retry interval 450 milliseconds?"

"How did you calculate that alert threshold?"

I answered. He wrote it down. The red light on the recorder stayed on.

They called it a **"Knowledge Transfer Initiative."** The CTO's all-hands email was polished: _We're preserving decades of institutional knowledge for the next generation of engineers._

**In plain English: your experience is too expensive. We're packaging it into a Skill.**

I didn't take it seriously at first. Every company has knowledge management. Then month three rolled around. Caleb stopped asking questions. He started validating.

He pulled up an incident I'd debugged the year before — a production outage. He asked me to reproduce the diagnosis. Then he let the system do it.

The system said: _Message broker latency spike detected. Retry logic at 450ms interval will amplify under queue backpressure. Recommend adaptive backoff._

I read it three times. It was right. It was my chain of reasoning — but it said it faster than I could.

The CTO stood next to me, smiling. I've seen that smile too many times in Silicon Valley. It's not happiness. It's sign-off.

## [](https://dev.to/xulingfeng/my-company-packaged-12-years-of-my-experience-into-an-ai-skill-then-laid-me-off-when-it-crashed-4b3e?context=digest#act-2-968-accuracy)Act 2 · "96.8% Accuracy"

The moment I knew something was wrong was the day the validation report came out.

A full row of people sat across the table — CTO, HRBP, VP of Engineering, and a woman I didn't recognize with a consulting firm logo on her blazer.

The projector displayed one number: **Knowledge Retention Rate: 96.8%**

Caleb delivered his findings. "After three rounds of validation, the AI Skill achieved 96.8% diagnostic accuracy across 312 historical failure scenarios. The remaining 3.2% deviation is suboptimal recommendations due to insufficient context — correctable with guidance."

Applause. The CEO turned to me and said something I'll never forget.

**"Mark, you created your own replacement."**

Everyone laughed. I laughed too. What else was there to do?

After the meeting I sat in the parking lot for a long time. My coffee had gone cold. Outside the window, that unchanging California blue — the same one it's always been. My phone buzzed. A text from my wife: _What time are you coming home?_

I typed: "Soon." Then I deleted it.

I didn't know how to tell her I'd spent three months turning myself into a manual. **And once you write the manual, you don't need the original.**

## [](https://dev.to/xulingfeng/my-company-packaged-12-years-of-my-experience-into-an-ai-skill-then-laid-me-off-when-it-crashed-4b3e?context=digest#act-3-the-severance)Act 3 · The Severance

The Monday after, the CTO closed the door for our one-on-one.

"Mark, I won't sugarcoat it. Your position's been eliminated as part of the restructuring."

He slid an envelope across the table.

N+3. Three months of severance. The standard Silicon Valley _we're not firing you, we're helping you transition_ treatment.

I signed without stopping. Not because I didn't care — because I'd already played out how this ended before I walked in.

My last day was a Friday. It took me under forty minutes to clear my desk. One backpack. One monitor stand. Three pen caps — I still don't know how three pen caps ended up in my drawer.

I sat in the car and searched three things on my phone:

-   LLC registration (California, single-member, $70, 15 minutes)
-   Professional liability insurance (industry standard for consultants, ~$1,200/year)
-   Rate benchmarking for senior infrastructure consultants (median: $215/hour)

That night I registered a company. Mark Johnson Consulting LLC. No office, no employees, no VC pitch deck. One clause, written clear: project-based only. No AI in the delivery chain.

## [](https://dev.to/xulingfeng/my-company-packaged-12-years-of-my-experience-into-an-ai-skill-then-laid-me-off-when-it-crashed-4b3e?context=digest#act-4-ai-skill-goes-live)Act 4 · AI Skill Goes Live

The first full quarter was a showpiece.

The AI Skill absorbed 70% of tier-2 operations tickets. New engineers went from six months to three weeks to reach productivity. The CEO used a slick slide at the all-hands:

_Before: 12 years of Mark's experience locked in his head.  
After: 12 years of Mark's experience available as a prompt._

Nobody mentioned Mark himself. They didn't need to. He was already packaged.

My wife noticed before I did. The weekend after I left, she looked at me across the kitchen and said something I wasn't expecting.

"You seem different."

"Different how?"

"When you sit at your computer and don't talk — that tension's gone. You used to be waiting for things to break. Now you're waiting for clients."

She was right. I was waiting.

I saw on LinkedIn they'd hired a new Platform Lead. First thing he did was rebuild the monitoring stack. The Skill? Nobody re-ran validation after they migrated to Kafka. Why would they? The person who built it wasn't there anymore.

## [](https://dev.to/xulingfeng/my-company-packaged-12-years-of-my-experience-into-an-ai-skill-then-laid-me-off-when-it-crashed-4b3e?context=digest#act-5-crash)Act 5 · Crash

It happened at 3:47 AM on a Wednesday.

The distributed tracing system lit up. P99 latency on the core payment chain went from 80 milliseconds to 12 seconds. Three minutes in, the first transaction timed out and rolled back. At ten minutes, the payment queue started backing up. At twenty-three minutes, the rollbacks triggered a cascade — two downstream services began refusing requests.

The on-call engineer pulled up the AI Skill. It scanned the logs, identified the pattern, and returned a diagnosis.

**Detected message broker latency. Applying known mitigation: activate retry queue with 450ms backoff.**

That diagnosis had been correct 312 times out of 312 historical scenarios.

This was number 313.

The 450ms retry window was a compatibility shim I'd written five years earlier for RabbitMQ. The number wasn't random — I'd spent two weeks load-testing on a RabbitMQ cluster to find the exact gap that cleared its Erlang VM GC cycle.

But that was RabbitMQ. Retired for three years. They were running Kafka now.

Kafka's consumer groups use a poll-based protocol — every consumer has to keep polling the coordinator at a configured interval, or the coordinator marks it dead and triggers a rebalance. My retry worker was synchronous — process one message, pull the next. At 450ms a round, a queue of a few dozen messages stretched the poll window by multiple factors.  

```
<span># What the Skill did (the 450ms retry window)
</span><span>def</span> <span>handle_queue</span><span>():</span>
    <span>while</span> <span>queue_not_empty</span><span>():</span>
        <span>msg</span> <span>=</span> <span>fetch_one_message</span><span>()</span>          <span># one at a time
</span>        <span>retry_with_backoff</span><span>(</span><span>450</span><span>ms</span><span>)</span>          <span># ⏱ 450ms per message
</span>        <span>process</span><span>(</span><span>msg</span><span>)</span>                       
        <span>poll_consumer</span><span>()</span>                    <span># "still alive?" → into debt
</span>
<span># What happened with 60 queued messages
</span><span>poll_timeout</span> <span>=</span> <span>5000</span>                        <span># 5s before coordinator marks dead
</span><span>time_per_round</span> <span>=</span> <span>60</span> <span>*</span> <span>450</span>                  <span># 60 messages × 450ms = 27,000ms
# 27,000ms &gt; 5,000ms → poll timeout missed → rebalance triggered
</span>
```

Once the rebalance kicked in, the whole group started oscillating. New consumers claimed partitions. Old messages got redelivered. Latency climbed again. A sticky problem turned into a snowball.

The AI executed a strategy that was 100% correct on the old architecture. **On the current one, it was pouring gasoline on the fire.**

**The AI didn't fail because it was wrong. It failed because it was right about yesterday — and yesterday wasn't running anymore.**

## [](https://dev.to/xulingfeng/my-company-packaged-12-years-of-my-experience-into-an-ai-skill-then-laid-me-off-when-it-crashed-4b3e?context=digest#act-6-the-call)Act 6 · The Call

My phone rang at 4:12 AM.

A name I hadn't called in months — my former CTO.

His voice was calm. Too calm. When an engineer calls at 4 AM and sounds that steady, something's on fire.

"Mark. I need to ask you something."

"Ask."

He laid out the incident in three sentences. I thought he'd ask about rollback strategy. Damage containment. He didn't.

"You left a note in the RabbitMQ migration docs. At the time, nobody understood it. We thought it was a stale config comment. I think I understand it now."

I leaned back against the headboard. The only light in the room was the phone screen. My wife stirred beside me. Didn't wake up.

The note said: _450ms matches RabbitMQ GC window. Do not reuse outside this context._

Silence on the other end. About four seconds.

"I know," he said. "I'm out of time, Mark. Come back."

"I'm not asking if you'll come back." His voice shifted. "I'm asking you to. I'll pause everything for the rest of the month. You call the shots. Name your price."

## [](https://dev.to/xulingfeng/my-company-packaged-12-years-of-my-experience-into-an-ai-skill-then-laid-me-off-when-it-crashed-4b3e?context=digest#act-7-the-price)Act 7 · The Price

"Five times my old salary."

I heard his breath catch.

"… Deal. But I need you on-site for two weeks. Contract. Bring your own equipment. No AI touches your delivery chain."

"Done. Send the contract to my lawyer."

I didn't have a lawyer. What I meant was: this runs at my pace.

After I hung up, I scrolled to a name I hadn't called in nearly a year — Mike, college roommate, law school grad. Sent one message.

_Got a contract. Mind glancing at it?_

He didn't reply. At 4 AM, who's awake except people in IT?

I waited. Then I typed five more words. I sent them to him, but they were really for me.

**This time I set the price.**

___

**You've been through this before? Your knowledge extracted, packaged into a Skill, turned into the reason you weren't needed anymore. And when the Skill hit something it didn't understand, they came back. Is there a better answer than "no"?**

___

**The Skill knew every past scenario. It just couldn't see that the infrastructure had changed.**

**The company saved six figures on headcount. They just forgot validation only works when the person who wrote it is still there to re-run it.**

**When the system went down — who did they call?**

___

_Follow for more stories about AI extraction, implicit knowledge, and what happens when companies discover their Skill only remembers the past._

___

I couldn't teach the AI Skill to understand context. But the stories stay open. [buy me a coffee](https://ko-fi.com/xulingfeng) ☕
