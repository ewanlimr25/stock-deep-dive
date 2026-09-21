# Phase 7c — Sentiment, Positioning & Short Interest

**Ticker:** RKT
**As-of date:** 2026-07-17
**Generated:** 2026-07-19T20:16:00-04:00
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-5-historical.md, phase-7b-fundamentals.md

## Summary

The crowd **confirms the constructive base case and contradicts the bearish-flow
lane** — it is not crowded against the thesis. On the as-of date, **Morgan Stanley
upgraded RKT to Overweight and raised its PT to $19**, and the Finnhub analyst
recommendation trend has been **steadily improving** (buy-side count 8 → 9 → 11 → 11
across Apr–Jul, **zero sell ratings throughout**), partially offset by a Rosenblatt
Buy→Neutral downgrade (07-14) and JPM/Barclays PT trims to $15.5/$17 — a **mixed-to-
constructive** tape with targets spanning **$15.5–$19**. Positioning is **BALANCED**:
short float **10.83%** (moderate, DTC 3.70), institutional ownership only **29.77%**
(retail-heavy float), and dark-pool institutions were *accumulating* (phase-2) — so
the bearish options tape sits against improving analysts and institutional buying.
No sentiment extreme (P/C z +0.38, IV-rank 51.7). Net: sentiment **CONFIRMS**, and
the 10.8% SI + 4/4 beat habit + fresh $19 upgrade make an upside squeeze the more
dangerous tail — **further disqualifying a directional short** (reinforces 7b).

## Key signals

- **Morgan Stanley → Overweight, PT $19 (2026-07-17)** — fresh bullish catalyst on the as-of date `[SENT:news finnhub]`
- **Analyst revisions improving: buy-count 8→9→11→11 (Apr→Jul), 0 sells** → constructive momentum `[SENT:recommendation finnhub]`
- **Short float 10.83%, DTC 3.70** (fz, semi-monthly) → moderate SI = squeeze fuel, not a crowded short `[SENT:short_float fz]`
- **Inst own 29.77%** (Gilbert Class-D holds rest) → retail-heavy float; institutions were the dark-pool buyers `[SENT:retail_vs_inst]`
- **Targets span $15.5–$19** (Rosenblatt cut, JPM $15.5, Barclays $17, MS $19) → wide dispersion, no consensus `[SENT:news finnhub]`

## Detailed findings

### News flow (14d tone; lead/lag) `[SENT:company-news finnhub]`

9 items over 2026-07-03 → 07-17. Tone **mixed, tilting constructive late**:

| Date | Item | Tone |
|---|---|---|
| 2026-07-17 | **Morgan Stanley upgrades RKT to Overweight, PT → $19** | **Bullish** |
| 2026-07-17 | RKT on CNBC 'Final Trades' | Neutral (attention) |
| 2026-07-14 | Rosenblatt downgrades Buy → Neutral | Bearish |
| 2026-07-13 | JP Morgan maintains Neutral, PT → $15.5 | Mild bearish |
| 2026-07-09 | Financials higher as Treasury yields decline | Bullish (sector) |
| 2026-07-07 | Barclays maintains Overweight, PT → $17 | Mixed (OW, trim) |

Price **lagged** the constructive news — RKT still closed −2.4% on 07-17 despite the
MS upgrade → the upgrade is not yet chased; sets up a possible catch-up on a 07-30
beat, or fade if the tape stays heavy. The bearish *options* tape (phase-1) is more
bearish than the *news/analyst* tone.

### Analyst-revision momentum `[SENT:recommendation finnhub]`

| Period | strongBuy | buy | hold | sell | strongSell | Buy-side total |
|---|---:|---:|---:|---:|---:|---:|
| 2026-07-01 | 5 | 6 | 11 | 0 | 0 | **11** |
| 2026-06-01 | 6 | 5 | 10 | 0 | 0 | 11 |
| 2026-05-01 | 4 | 5 | 10 | 0 | 0 | 9 |
| 2026-04-01 | 4 | 4 | 11 | 0 | 0 | 8 |

**Improving trend, 0 sell ratings across the window** — constructive, corroborates
7b's earnings-beat habit. Fresh MS upgrade (07-17) extends it. **`fz` Recom/target
cross-check unavailable** (reduced RKT payload) → no vendor-divergence check possible.

### Retail vs institutional `[SENT:retail_vs_inst]`

- **Inst own 29.77%** (low; Class-D held by Gilbert) → the tradeable float is
  retail-tilted.
- **Institutions were BUYING** in the dark pool (phase-2 large-tier buy_ratio 0.651;
  phase-7 buy/sell 1.46), while the lit options tape leaned bearish (overwrite/hedge).
- **No retail-euphoria-into-distribution signature** — price is in the *lower third*
  of its 52w range (not a euphoric high), and the smart-money (dark pool) is on the
  buy side. This is the *opposite* of the fade-the-crowd setup.

### Short interest & borrow `[SENT:short_float fz semi-monthly]`

- **Short float 10.83%**, days-to-cover **3.70**, float 960.68M (fz, exchange
  semi-monthly settlement, ~2-week lag).
- **Borrow: likely EASY** (inferred — 960M float, DTC 3.7, moderate SI; a $14.6B-float
  large-cap is not typically HTB). Dedicated WebSearch borrow-fee not run (low
  materiality for this float size) → marked inferred, not confirmed.
- Read: **moderate SI = meaningful squeeze fuel on a 07-30 beat**, but not a crowded/
  hard short. Hazard for any bear thesis; supportive-but-not-sized tailwind for a long.

### Positioning extremes `[SENT:positioning]`

- P/C z-score **+0.38** (not extreme), IV-rank **51.7** (mid). **No contrarian
  trigger** — positioning is unremarkable, neither euphoric nor panicked.

## Divergences

1. **Bearish options tape (phase-1) vs improving analysts + MS $19 upgrade (07-17)** —
   the options desk is more bearish than the sell-side/news.
2. **Retail-heavy float (inst 29.77%) but institutions accumulating in dark pool** —
   smart money buying a retail-held name; not a distribution setup.
3. Price lagged the constructive news (closed −2.4% into a same-day upgrade) —
   catch-up-or-fade tension into 07-30.

## Source calls (audit)

| Source | Result |
|---|---|
| `company-news` (07-03→07-17) | ok — 9 items, MS upgrade 07-17 |
| `stock/recommendation` | ok — improving trend, 0 sells |
| `fz` SI/float (via 7b ownership screen) | ok — SF 10.83%, DTC 3.70, inst 29.77% |
| `fz quote` recom/target | null (reduced payload) |
| WebSearch borrow-fee | not run (inferred EASY, low materiality) |

## Source errors

None. `fz` Recom/target null (reduced payload) and borrow-fee not separately searched
— recorded as gaps, not vetoes. Look-ahead guard applied: all news/revisions filtered
to `<= 2026-07-17` (the 07-17 MS upgrade is on-date and valid).

## Verdict for downstream — positioning gate

```
sentiment_signal:  BULLISH        # improving revisions, 0 sells, fresh MS OW/$19 upgrade
crowd_state:       BALANCED       # SF 10.83% moderate; inst 29.77% low; no euphoria/panic
short_interest:    10.83% [fz, semi-monthly] ; days_to_cover: 3.70 ; borrow: EASY (inferred) [not WebSearch-confirmed]
tier_adjustment:   CONFIRM        # crowd confirms constructive base; not crowded against thesis.
                                   #   Reinforces 7b: a directional SHORT is squeeze-exposed (10.8% SI + beat habit + $19 upgrade)
divergences:       [
  "bearish options tape vs improving analysts + MS $19 upgrade",
  "retail-heavy float (inst 29.77%) but institutions accumulating in dark pool",
  "price lagged same-day MS upgrade (closed -2.4%) — catch-up-or-fade into 07-30"
]
key_risks:         [
  "SF 10.83% + beta 2.21 = two-way squeeze/flush risk into FOMC 07-29 / earnings 07-30",
  "analyst targets span $15.5-$19 — wide dispersion, no fair-value consensus",
  "MS upgrade may be partly priced; a 07-30 miss + rate spike = sharp downside on a retail-held name"
]
```

**Interpretation for phase-9:** sentiment is a **CONFIRM** for the constructive/range
base and **compounds 7b's veto of a directional short** (squeeze fuel + improving
revisions). It does not (and cannot) *raise* long conviction — it removes the bear
case and flags upside squeeze potential on a beat as a tailwind to *weigh*, not size
up. Carry the two-way event-vol and target-dispersion risks into structure selection.

- **Open questions for phase-8/8b:** with the short (7b) and long-fade (7c) both
  off the table, is the cleanest expression **non-directional / long-vol into the
  07-30 event** (matching the phase-1 straddle) or a **constructive defined-risk long**
  leaning on the improving fundamentals + squeeze fuel? The desk agents should adjudicate.
