---
name: growth-funnel
description: "Diagnose growth bottlenecks and prioritize what to fix using the AARRR framework (Acquisition, Activation, Retention, Referral, Revenue — 'pirate metrics'). Use when the user asks which stage of the funnel is broken, wants a growth framework applied to their product, or mentions AARRR, pirate metrics, or the customer lifecycle."
---

# Growth Funnel (AARRR)

## Goal

Find the one stage of the customer lifecycle that's actually capping growth, and recommend fixing that stage before any other. AARRR (Dave McClure's "pirate metrics") splits the lifecycle into five stages so bottlenecks are diagnosable instead of vibes-based. This skill is a diagnostic lens, not a content generator — most of the value is in correctly naming which stage is weak and refusing to spread effort across all five at once.

## The five stages

| Stage | The question it answers | Signal it's broken |
|---|---|---|
| **Acquisition** | How do people find this? | Low or expensive traffic; no repeatable channel |
| **Activation** | Do new users reach real value fast? | High signup-to-first-value drop-off; users never come back after day 1 |
| **Retention** | Do they come back? | Users return once then vanish; usage decays fast after the first week |
| **Referral** | Do they tell anyone? | Zero organic word-of-mouth; no one shares or refers unprompted |
| **Revenue** | Do they pay, and how much? | Free users never convert; paying users have low lifetime value relative to cost to acquire |

Define each stage with a real behavioral event specific to the product — "activated" means something concrete (uploaded a file, sent a first message, completed setup), not "visited the dashboard." Vague event definitions produce a diagnosis that's just as vague.

## Step 1 — Find where the biggest drop-off actually is

Before recommending any tactic, get (or estimate from what's available) the conversion rate between each adjacent stage. The stage with the steepest relative drop is the bottleneck — not necessarily the stage the user is most anxious about or has heard the most advice on. A product with strong acquisition and activation but near-zero retention doesn't need more ad spend; it needs the product itself fixed, and more acquisition spend on a leaky retention curve is money funding churn.

If real numbers aren't available, say so plainly and reason from what evidence exists (support tickets, user interviews, analytics if any exist) rather than presenting a guess as measured data.

## Step 2 — Diagnose by cohort, not in aggregate

An aggregate "30% retention" number hides whether that's stable, improving, or actively decaying — always compare cohorts against each other (this month's signups vs. last month's) rather than reading one blended number. A channel or feature change that looks neutral in aggregate is often a clear win or loss once cohorts are split out.

Quality over volume: a channel bringing fewer but better-activated users is usually the better acquisition channel even if its raw signup count is smaller. Don't let a vanity top-of-funnel number override a weak down-funnel outcome from the same channel.

## Step 3 — Recommend ONE stage to fix, not a rebalance across all five

The temptation is to hand back a list of five improvements, one per stage. Resist it. Name the single stage with the worst relative performance, explain the evidence, and scope the recommendation to that stage only. If a second stage is close behind, say so explicitly and note it as next-in-line rather than folding it into the same push.

## Per-stage actions (once a stage is identified as the bottleneck)

- **Acquisition** — audit which channels are actually repeatable and profitable vs. one-off spikes; check channel-fit against where the actual target user spends time before adding a new channel.
- **Activation** — walk the real first-session path as a new user would; find the exact step where people stall (a setup step, a missing example, an unclear next action) rather than redesigning onboarding wholesale.
- **Retention** — separate "never came back" churn from "used it, moved on" churn; they have different fixes (the first is often an activation problem in disguise; the second usually needs a reason to return — a trigger, a habit loop, or genuine ongoing value).
- **Referral** — check whether the product is actually worth telling someone about yet before building referral mechanics on top of it; a referral program bolted onto weak retention just accelerates churn of the referred users too.
- **Revenue** — compare cost to acquire against lifetime value by cohort and channel, not blended; a channel with cheap signups but low-value customers can be net-negative even while acquisition metrics look great.

## Guardrails

- Don't recommend fixing all five stages in parallel — that's the default failure mode this framework exists to prevent.
- Don't treat vanity totals (total signups, total pageviews) as stage health; use conversion rate between adjacent stages instead.
- If retention is the actual bottleneck, don't let acquisition or paid-ads work get proposed as the fix — that just grows the leak.
- Ground the diagnosis in real numbers or direct observation (support tickets, session recordings, actual analytics) wherever they exist; label anything reasoned from partial evidence as an estimate, not a measured fact.

## Output format

- **Stage-by-stage read**: current state of each stage, with the evidence behind it (or "no data available" where that's the truth).
- **The bottleneck**: one stage, named plainly, with the reasoning.
- **The one recommendation**: what to do about that stage this cycle — concrete, not a tactics list spanning all five stages.
- **What's next**: the stage likely to become the bottleneck once this one is fixed, so the user isn't surprised by it later.
