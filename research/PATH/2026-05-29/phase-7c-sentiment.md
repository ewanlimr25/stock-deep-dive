# Phase 7c — Sentiment, Positioning & Short Interest

**Ticker:** PATH · **As-of:** 2026-05-29 · **Generated:** 2026-05-29
**Upstream:** phase-7b (CONFIRM, profitable laggard) · phase-7 (weak-bullish) ·
phase-2 (DP accumulation) · phase-0 (short float 31.15%)

## ⚠️ Material reframe — earnings were 2026-05-28, NOT 2026-09-03

The 14-day news pull reveals **UiPath reported Q1 FY2027 earnings after the close
on 2026-05-28.** UW's `next_earnings_date = 2026-09-03` (cited in phases 0.5/1/6)
was **stale/incorrect.** This changes the *context* of the entire run (the raw
flow/DP/OI/GEX data remain valid, but their interpretation shifts):

- **This run's 2026-05-29 tape is the POST-EARNINGS reaction day**, not a quiet
  pre-catalyst session. The 97th-pctile volume (phase-0.5), the call buildup
  (phase-1/3), and the DP accumulation off the $10.4 intraday low (phase-2) are
  all the **day-after-earnings repositioning**.
- **The print (per news):** EPS ~$0.15 *missed* ~$0.163 (−8%), but **revenue
  beat**, **FY2027 guidance RAISED** ($1.776–1.781B vs $1.754–1.759B prior),
  **first-ever GAAP profitability**, ARR > $1.9B, "improving demand, AI a bigger
  part of deals." Stock dipped after-hours on the EPS miss, then **recovered**
  intraday 5/29 ($10.4 → $11.72).
- This reconciles phase-7b's dropped "look-ahead" row (period 2026-06-30, EPS
  0.15 miss −7.9%) — that *was* this just-reported quarter (fiscal-calendar
  labeling), so the **latest earnings was a slight EPS miss offset by a guidance
  raise**, not a clean beat. (Phase-10 must log the UW earnings-date error.)

## Summary

Sentiment is **mixed-but-constructive into a heavily-shorted, low-expectations
name** — a contrarian-bullish setup that *confirms* (does not fade) the weak
bullish flow lean. The post-earnings news is genuinely two-sided: bears got the
EPS miss, bulls got the **guidance raise + first GAAP profit + improving AI
demand**, and the stock's recovery off the lows says the market leaned bullish on
balance. The Street is **lukewarm and hold-heavy** (17 holds of 28 analysts; PTs
post-print clustered $12–$15; fz Recom 2.65) — i.e. *low expectations*, which is
the friendly backdrop for an upside surprise. The dominant positioning fact is
**31.15% of float short** (128.4M shares, days-to-cover 3.9) — but **borrow is
EASY and cheap (0.29% fee, ~10M shares available)**, so the squeeze is **latent,
not lit**: shorts are not trapped and need a catalyst to force covering. Net: a
**crowded-short, cheap, profitable laggard that just raised guidance** — the
shorts are fuel, not a wall, and the bullish lean faces no crowded-long fade
risk. `tier_adjustment = CONFIRM` (squeeze is a noted tailwind, *not* added to
size — gate is downside-only).

## Key signals

- **Earnings 2026-05-28: EPS miss, revenue beat, GUIDANCE RAISED, first GAAP
  profit** `[SENT:news Finnhub]` — the catalyst that drove today's tape; net
  constructive despite the headline "miss."
- **31.15% float short, 128.4M shares, days-to-cover 3.90** `[SENT:short_float fz
  semi-monthly]` — extreme short positioning = squeeze fuel for a long / hazard
  for a short.
- **BUT borrow EASY: 0.29% fee, ~10M available** `[SENT:borrow WebSearch:fintel.io]`
  — shorts are *not* under cover pressure; squeeze is latent, needs a catalyst.
- **Street lukewarm / hold-heavy** — 2 strongBuy / 8 buy / 17 hold / 1 sell;
  post-print PTs $12 (DA Davidson), $13 (BofA), $15 (MS, Needham); Recom 2.65
  `[SENT:recom fz]`. Low expectations = contrarian-friendly.
- **Mild positive revision drift** — buy count 6→7→8 and holds 19→18→17 over
  Feb→May `[SENT:recommendation Finnhub]`. Slowly warming, not deteriorating.

## Detailed findings

### News flow (14d tone)
Volume is entirely earnings-clustered on 5/28–5/29. Tone **mixed → constructive**:
headlines split between "weak earnings / EPS miss / slips after-hours" and
"guidance beats, ARR tops $1.9B, first-time GAAP profitability, improving AI
demand, doubles down on agentic AI." Price **led bullishly** (recovered off the
post-print low), suggesting the market weighted the guidance raise over the EPS
miss. No pre-earnings news (quiet into the print).

### Analyst-revision momentum
Finnhub recommendation trend is **stable and hold-dominated** (17/28 hold) with a
**mild positive drift** in buys. Post-earnings PT actions (all 5/29): DA Davidson
Neutral→$12 (cut), BofA Underperform→$13 (raised), MS Equal-Weight→$15 (cut),
Needham Buy→$15 (maintained). **No Finnhub-vs-fz divergence** — both read a
mild-buy/hold consensus (~2.65). The Street is firmly on the fence: a "show me"
name post-guidance-raise.

### Retail vs institutional
Aligned, both mildly long: phase-1 lit tape = 0DTE retail lottery calls + LEAP
institutional calls; phase-2 DP = institutional **block-tier buying** the
$11.65–$11.80 recovery shelf. **No retail-euphoria-vs-institutional-distribution
divergence** — the classic fade signature is absent.

### Short interest & borrow
- **% float short: 31.15%** (fz/Finviz semi-monthly, ~2-wk lag); short interest
  128.43M sh; **days-to-cover 3.90**; float 412.34M; inst own 60.8%, insider 20.8%.
- **Borrow: EASY** — fee 0.29%, ~10M shares available (Fintel, ~current). NOT
  hard-to-borrow. (Note: sources disagree on the SI level — FINRA Nov-2025 showed
  ~7.9%; fz's 31% is the more recent semi-monthly settlement. The *easy borrow*
  is the operative tell: whatever the exact %, shorts are not squeezed yet.)
- Read: heavy short positioning + a guidance-raise catalyst = **squeeze fuel
  loaded**, but easy borrow + moderate days-to-cover = **not lit**; a break of
  the $13 wall (phase-4) would be the igniter.

### Positioning extremes
P/C z-score −0.26 (not extreme, phase-5); IV rank 43 / post-event IV crush
(8.8th pctile 1y, phase-5). No options-sentiment extreme. The *short interest* is
the positioning extreme, not the options crowd.

## Divergences
- **Crowd (shorts) vs flow lean:** shorts are 31% bearish-positioned while the
  flow/DP lean mildly bullish — this is a *constructive* divergence for a long
  (shorts = fuel), not a fade.
- **EPS miss vs guidance raise:** the print itself is internally split; resolved
  bullishly by the price recovery.
- **High SI headline vs easy borrow:** tempers the squeeze thesis.

## Source calls
| Source | Call | Result |
|---|---|---|
| Finnhub | `company-news` 14d | earnings-clustered, mixed-constructive |
| Finnhub | `recommendation` | hold-heavy, mild positive drift |
| fz | `quote` SI/float/recom | 31.15% short, dtc 3.9, Recom 2.65, tgt $13.47 |
| WebSearch | borrow/HTB | EASY, 0.29% fee, ~10M available (fintel.io) |

## Source errors
(none — note the cross-source SI-level disagreement above; borrow read is the
tiebreaker.)

## Verdict for downstream

```
sentiment_signal:  NEUTRAL  (constructive-contrarian undertone)
crowd_state:       CROWDED_SHORT
short_interest:    31.15% float [fz, semi-monthly] ; days_to_cover: 3.90 ; borrow: EASY (0.29%) [WebSearch:fintel.io]
tier_adjustment:   CONFIRM
divergences:       ["shorts 31% vs mildly-bullish flow = fuel not fade",
                    "EPS miss vs FY guidance raise (resolved bullish by price)",
                    "31% SI headline vs easy/cheap borrow = squeeze latent not lit"]
key_risks:         ["easy borrow → no forced-cover pressure; squeeze needs a >$13 catalyst",
                    "hold-heavy Street + cut PTs (DA Davidson $12, MS $15) cap re-rating",
                    "post-earnings IV crush removes cheap-vol tailwind for long premium"]
```

- **CONFIRM (no-op on size).** The crowd is short, not long, so the bullish lean
  has **no fade risk**; the 31% SI is a **latent squeeze tailwind** for phase-9 to
  *weigh qualitatively* — but per the downside-only rule it does **not** add size.
- **Reframe phase-9 must carry:** this is a **post-earnings, guidance-raise,
  heavily-shorted recovery**, not a pre-catalyst quiet name. The thesis is
  "cheap profitable laggard mean-reverts toward $13 (consensus target + gamma
  wall), with short-covering as upside convexity if $13 breaks." The near-term
  catalyst already fired (mixed); the next is the **post-IV-crush drift**.
- **Open question for phase-8b:** does the bear case (EPS miss, decel growth,
  easy borrow = no squeeze) outweigh the bull case (guidance raise, first GAAP
  profit, 31% SI, cheap fwd 13x), or is this genuinely range-bound $11–$13?
