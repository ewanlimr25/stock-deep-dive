# Phase 7c — Sentiment, Positioning & Short Interest

**Ticker:** RKT
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T18:15:00-04:00
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-5-historical.md, phase-6-macro.md, phase-7-insights.md, phase-7b-fundamentals.md

## Summary

The crowd is **not crowded** — and the loudest contrary axis is the sell side:
**analyst-revision momentum is improving into the decline** (strongBuy 4 → 6
between May and June, holds 11 → 10, zero sells; fz Recom 1.94 / target $20.27
agrees — no vendor divergence) while retail small-lot flow leans bearish
short-dated and the 14-day news tone is mixed. Short interest is moderate
(**7.48% of float, days-to-cover 2.86** [fz, semi-monthly]) with no
hard-to-borrow evidence — squeeze fuel exists but isn't extreme. No positioning
extreme triggers (P/C z +0.017 NORMAL; IV %ile 15.4 low). Against the weak-bear
flow baseline this gates to **CAUTION** (one contrary axis: improving
revisions; plus retail already leaning the thesis's way without squeeze
asymmetry) — cut one size step on any bearish expression.

## Key signals

- Analyst revisions (Finnhub monthly): 2026-03 → 06: strongBuy 5→4→4→**6**,
  buy 3→4→5→**5**, hold 11→11→10→**10**, sell 0 throughout — **improving into
  the sell-off** [SENT:recommendation]
- fz cross-source agrees: `Recom` 1.94, `Target Price` $20.27 (+60.2% vs
  $12.65) — no Finnhub-vs-fz divergence [SENT:recom fz]
- Short interest **7.48% of float**, days-to-cover **2.86**, float 960.91M
  [SENT:short_float fz semi-monthly]; borrow fee: no figure/HTB flag found
  (WebSearch) — recorded n/a, not inferred
- News tone 14d: mixed — bearish "3 Reasons to Avoid RKT" (05-23) vs bullish
  "Strongest Q1 Results from the Thrifts & Mortgage Finance Group" (05-22);
  **no headline matches the −10.8% week — the tape led the news**
  [SENT:company_news]
- Retail-vs-institutional split: retail small-lot **put buying** (Jun-18 $14P:
  797 contracts over 701 trades; Jun-26 $15P: 321 trades — phase-1) vs
  institutional covered-call signature + LEAP call buys (phases 1/7) — crowd
  leaning bearish near-dated while institutions sell that fear
  [SENT:retail_vs_inst; phase-1-flow.md §Sweeps]

## Detailed findings

### News flow (14d window 2026-05-22 → 06-05, look-ahead filtered; 9 items)

| Date | Headline (source) | Tone |
|---|---|---|
| 06-04 | Tracking Leon Cooperman's Omega Advisors Portfolio Q1 (SeekingAlpha) | neutral |
| 06-03 | "Housing M&A Boom Isn't A Recovery Signal — It's A Long-Term Bet On Next Cycle" (Benzinga) | cautious |
| 05-26 | Redfin: income needed to afford a home declined 7th straight month (Yahoo) | mild + |
| 05-26 | Luxury home prices rise (Yahoo) | neutral |
| 05-23 | **"3 Reasons to Avoid RKT and 1 Stock to Buy Instead"** (Yahoo) | bearish |
| 05-23 | Redfin Savings Program "Tests Rocket Companies Valuation Gap" (Yahoo) | cautious |
| 05-22 | **"Strongest Q1 Results from the Thrifts & Mortgage Finance Group"** (Yahoo) | bullish |
| 05-12 / 04-23 | tangential (Wise listing; sector-wide Tehran risk-off) | n/a |

Net tone: **mixed**. Lead/lag: price fell 10.8% in the window's final week with
no proportionate headline — the move was mechanical (rates + L-1 unlock,
phase-6-macro.md §Sector overlay), i.e. **tape led, narrative lagging**.

### Analyst-revision momentum

| Period | strongBuy | buy | hold | sell |
|---|---|---|---|---|
| 2026-06-01 | **6** | 5 | 10 | 0 |
| 2026-05-01 | 4 | 5 | 10 | 0 |
| 2026-04-01 | 4 | 4 | 11 | 0 |
| 2026-03-01 | 5 | 3 | 11 | 0 |

Direction: **up** (SB+B 8 → 11 over four months; the June bump landed as the
stock broke down). Cross-source: fz Recom 1.94 / target $20.27 — consistent
(both vendors bullish); divergence flag: none. For a bearish thesis this is the
"flow front-running a downgrade cycle" heuristic **inverted** — the flow is
bearish while revisions improve; pair with 7b's 4/4 beats (same direction:
fundamentals/street vs tape).

### Retail vs institutional

- **Retail (lit small-lot):** put-heavy — the two most trade-fragmented prints
  of the day are ITM put buys (~1.1 contracts/trade; phase-1). Retail is
  *bearish* the front month.
- **Institutional:** covered-call signature (conviction-matrix COVERED_CALL,
  phase-7), block-tier DP selling 0.883 intraday but LEAP/Sep call accumulation
  (phases 2/3).
- Same-side? **No** — retail bearish short-dated; institutions harvesting that
  premium while keeping long-dated upside. Mild fade-the-crowd flag *against*
  the short thesis.

### Short interest & borrow

- `Short Float` **7.48%**, `Short Ratio` (days-to-cover) **2.86**, float
  960.91M [SENT:short_float fz semi-monthly — exchange settlement, ~2-week
  lag; may not reflect post-06-03 short build]
- Peer context (phase-7b table): mid-pack (UWMC 13.14%, LDI 15.82%, BETR
  30.82%, PFSI 5.89%) — elevated but not squeeze-critical.
- Borrow fee / HTB: WebSearch surfaced trackers (Fintel/ShortableStocks) but
  **no current fee figure or HTB flag** — recorded **n/a** (not inferred;
  large-float names are typically GC, but absence of data is a blind spot, not
  a datapoint).

### Positioning extremes

- P/C ratio z-score **+0.017** (`extreme: "NORMAL"`, phase-5) — no extreme.
- IV rank 29.96 / IV percentile 15.38 (phases 0.5/5) — low-vol regime, no
  panic pricing; **no contrarian trigger fires**.

## Divergences (crowd vs flow)

1. **Improving analyst revisions (SB 4→6 into June) vs bearish flow + −18.9%
   30d price** — street and tape pointed opposite ways at the as-of.
2. **Retail small-lot put-buying vs institutional call-overwriting** — the
   crowd pays for downside while institutions sell upside calls and buy
   LEAPs; both sides can't be right on the path.
3. **Tape led news** — the −10.8% week has no narrative-severity match; the
   move is mechanical (rates + unlock), which mean-reverts faster than
   narrative-driven breaks when the mechanics clear (post-06-30).

## Source calls

| Source | Status |
|---|---|
| Finnhub `/company-news` (05-22 → 06-05, look-ahead filtered) | ok — 9 items |
| Finnhub `/stock/recommendation` | ok — 4 monthly rows |
| `fz quote RKT` (Short Float / Short Ratio / Recom / Target) | ok |
| WebSearch borrow-fee / HTB | ran — no fee figure found → n/a |
| Positioning extremes | reused phase-5 PCR-z + phase-0.5 IV rank (no new call) |

## Source errors

None fatal. Borrow-fee data unavailable from free sources — recorded as a
blind spot (n/a), per "absence of data is not a datapoint."

## DATA NOTE / CORRECTION

None — first reads stood.

## Verdict for downstream — positioning gate

Flow bias being gated (plurality of phases 1–7): **weak-bear / capped-upside**.

```
sentiment_signal:  NEUTRAL      # mixed news; improving analyst revisions (bullish)
                                # vs bearish retail tape — nets out
crowd_state:       BALANCED     # no P/C or IV extreme; retail mildly bearish
                                # near-dated, institutions opposite — not crowded
short_interest:    7.48% [fz, semi-monthly] ; days_to_cover: 2.86 ; borrow: n/a [WebSearch — no figure found]
tier_adjustment:   CAUTION      # one contrary axis vs the bear thesis:
                                # improving revision momentum (+ retail already
                                # leaning bearish without squeeze asymmetry)
                                # → cut one size step on bearish expressions
divergences:
  - improving analyst revisions (SB 4→6) vs bearish flow and falling price
  - retail small-lot put euphoria vs institutional call-overwrite/LEAP-buy
  - tape led news — mechanical (rates/unlock) not narrative break
key_risks:
  - 7.48% SI + 2.86 DTC + improving revisions = bounce/squeeze risk on any rate
    relief (the phase-4 vanna trigger) — hazard for shorts into 06-30
  - SI figure is semi-monthly (~2wk lag); post-06-03 short build may be larger,
    raising squeeze sensitivity further
  - Street target +60% above spot: upgrade-driven counter-trend rallies can
    exceed the ±1.2% front-expiry implied move
```

Downside-only note: this CAUTION cuts bearish sizing one step; it does not add
to any long case (the gate never raises conviction).
