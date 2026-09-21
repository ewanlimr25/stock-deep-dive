# Phase 7c — Sentiment, Positioning & Short Interest

**Ticker:** MU
**As-of date:** 2026-06-23
**Generated:** 2026-06-23
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-5-historical.md, phase-7-insights.md, phase-7b-fundamentals.md

## Summary

The crowd read is a **divergence, not a one-sided extreme** — and it is **not crowded enough
to veto anything**. Today's news tape is overwhelmingly bearish ("Micron Shares Getting
Obliterated," "Worst Day in More Than a Year Ahead of Earnings," a "South Korea-led memory
selloff," broad "AI spending concerns") — event-driven fear into the binary, *not* a
fundamental-deterioration story (phase-7b: EPS +412%, 100% beat rate). Against that, **Wall
Street is strong-buy and getting *more* bullish**: Finnhub recommendation trend strongBuy
17→17→17→**18**, 51 of 55 analysts buy/strong-buy, only 1 sell — matching `fz` **Recom 1.35**
(no vendor divergence). Positioning is **clean/balanced**: short interest **3.35% of float**,
**0.74 days-to-cover** (no squeeze fuel either way), 79.3% institutional ownership, P/C
z-score 0.78 (not extreme). Institutions (phase-2 mega-tier 85.9% buy) were *buying the dip*
while the broad tape hedged — no retail-euphoria-into-distribution setup. Net `crowd_state =
BALANCED`, `sentiment_signal = NEUTRAL` (bearish tape vs bullish analysts cancel), and the gate
is **CAUTION** — the active −12% selloff + bearish news into a binary is a knife-catching/gap
risk on any *fresh* directional entry, but nothing here is crowded enough to VETO.

## Key signals

- News tape **bearish today** (memory selloff + AI-capex fear) — 249 articles/14d, today's all-red `[SENT:company_news]`
- Analyst revisions **improving & bullish**: strongBuy 17→18, 51/55 buy, 1 sell; `fz` Recom **1.35** (agree) `[SENT:recommendation]` `[SENT:recom fz]`
- **Short interest 3.35% / 0.74 days-to-cover** — clean, no squeeze fuel either direction `[SENT:short_float fz semi-monthly]`
- **Institutions bought the dip** (mega DP 85.9%) vs broad-tape hedging — no retail-euphoria distribution `[SENT:retail_vs_inst]`
- Positioning **not extreme**: P/C z 0.78 (|z|<2), IV rank 100 (event, not sentiment) `[SENT:positioning]`

## Detailed findings

### News flow (14d tone; lead/lag) — `[SENT:company_news]`

249 items 2026-06-09→06-23; today's (06-23) headlines uniformly bearish: "Why Micron Shares
Are Getting Obliterated Today," "A Bad Omen for Micron? Worst Day in More Than a Year Ahead of
Earnings," "Micron Falls as South Korea-Led Memory Selloff Raises Earnings Stakes," "Wall
Street ends lower as AI spending concerns mount," "Hard Sell-Off in Chipmakers." The **price
led** (−12% today) on a *macro/sector* narrative (memory-sector selloff + AI-capex doubt), not
MU-specific bad news. Reads as **event-driven washout/fear**, consistent with phase-6 (semis
−3.94%) — the print is the resolution.

### Analyst-revision momentum — `[SENT:recommendation]` `[SENT:recom fz]`

| Period | strongBuy | buy | hold | sell | strongSell |
|---|---:|---:|---:|---:|---:|
| 2026-06-01 | **18** | 33 | 3 | 1 | 0 |
| 2026-05-01 | 17 | 32 | 3 | 1 | 0 |
| 2026-04-01 | 17 | 31 | 3 | 1 | 0 |
| 2026-03-01 | 17 | 32 | 3 | 2 | 0 |

Trend **improving** (strongBuy +1, buy +1, sell steady at 1) — 51 of 55 buy/strong-buy.
`fz` Recom **1.35** (strong-buy), target **$1123.28** (+6.8%). **No Finnhub-vs-`fz` divergence.**
Wall Street is firmly bullish into the print — directly opposite the bearish news tape.

### Retail vs institutional — `[SENT:retail_vs_inst]`

- Institutional: phase-2 mega-tier DP **85.9% buy** + the $553M above-ask block → buying the dip;
  79.3% institutional ownership.
- Lit tape: phase-1 top-sweeps leaned bullish (call buying) but whole-tape ask/bid had calls
  net *sold* (phase-7 conviction-matrix) + put hedging.
- **No retail-euphoria-into-distribution signature** — if anything, smart money (mega DP) is the
  *buyer* and the broad tape is the hedger. Not a fade-the-crowd long.

### Short interest & borrow — `[SENT:short_float fz semi-monthly]`

`short_float` **3.35%**, `days_to_cover` **0.74**, float 1.12B, inst_own 79.3%, insider_own 0.48%.
SI is **low** and days-to-cover **trivial** → **no squeeze fuel** (doesn't threaten a short, doesn't
fuel a long). Borrow: not separately retrieved, but 3.35% SI / 0.74 DTC implies **EASY to borrow**
(no HTB) `[SENT:borrow WebSearch — inferred EASY from low SI]`. Note: Finviz SI is the exchange
semi-monthly settlement (~2-week lag).

### Positioning extremes — `[SENT:positioning]`

P/C z-score **0.782** (|z|<2 — *not* a sentiment extreme; no contrarian P/C trigger). PCR 1.013
(balanced). IV rank **100** — extreme, but that is the *earnings event*, not crowd sentiment.

## Divergences

1. **Wall Street strong-buy & improving revisions** vs **−12% price drop + all-bearish news tape** — the cleanest divergence; resolves on the print.
2. **Institutions (mega DP 85.9% buy) buying the dip** vs **broad options tape hedging/net-bearish** — smart money and the crowd on opposite sides (mildly contra a bearish thesis).
3. **Stellar fundamentals (7b)** vs **bearish near-term sentiment** — fear ≠ deterioration.

## Source calls (audit trail)

| Source | Status | Key value |
|---|---|---|
| Finnhub `/company-news` (14d) | ok | 249 items, today all-bearish (memory/AI-capex) |
| Finnhub `/stock/recommendation` | ok | strongBuy 17→18, 51/55 buy, 1 sell (improving) |
| `fz quote` Recom/target | ok | 1.35 strong-buy, target $1123.28 |
| `fz quote` SI/float/own | ok | SI 3.35%, DTC 0.74, inst 79.3% |
| phase-5 P/C z-score | reused | 0.78 (not extreme) |

## Source errors

(none. Borrow-fee/HTB not directly fetched — inferred EASY from 3.35% SI / 0.74 DTC; flagged.)

## DATA NOTE / CORRECTION

(none — news filtered to ≤ as-of; recommendation rows filtered to ≤ as-of; all values
round-tripped through `jq`.)

## Verdict for downstream — the positioning gate

```
sentiment_signal:  NEUTRAL          # bearish news tape vs bullish/improving analysts → net neutral, near-term tape bearish
crowd_state:       BALANCED         # SI 3.35% / DTC 0.74, P/C z 0.78, no retail euphoria, no squeeze fuel
short_interest:    3.35% of float [fz, semi-monthly] ; days_to_cover: 0.74 ; borrow: EASY [inferred]
tier_adjustment:   CAUTION          # active -12% selloff + bearish news into a binary = knife-catch/gap risk on any fresh entry; not crowded enough to VETO
divergences:       ["Wall St strong-buy/improving vs -12% drop + all-bearish news tape",
                    "institutions buying the dip (mega DP) vs broad-tape hedging",
                    "exploding fundamentals (7b) vs near-term fear/sentiment"]
key_risks:         ["memory-selloff / AI-capex narrative could persist regardless of MU's number",
                    "-12% pre-earnings drop → knife-catch risk on a long; two-sided gap risk",
                    "sentiment is event-driven fear, not a tradeable directional crowd extreme"]
```

**Phase-9 application (downside-only):** the gate is **CAUTION → cut one size step** on any
*fresh directional* entry, reflecting the live washout + binary uncertainty. It does **not**
veto: positioning is balanced and clean (low SI, no squeeze, no retail-distribution). It
reinforces phase-7b's steer — **don't short** (improving revisions + institutions buying +
clean SI all oppose a short), and **don't chase a naked long into the knife** — favor
defined-risk vol structure into the print.
