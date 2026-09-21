# Phase 7c — Sentiment, Positioning & Short Interest (second filter)

**Ticker:** OKLO
**As-of date:** 2026-07-17
**Generated:** 2026-07-18T00:00:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-5-historical.md, phase-7b-fundamentals.md

## Summary

The crowd is a **material caution on the bearish thesis, not a confirmation**. OKLO is a
**crowded short — 19.29% of float short (27.2M shares, $1.65B) as of 2026-06-15**, though
**days-to-cover is only ~2.6** (very liquid → squeeze mechanics are *moderate*, not
explosive). Short interest ran up Jan→May (10.9% → 24.9%) then **eased to 19.3% in June** —
some covering already happened. Meanwhile **sell-side analysts remain net-bullish by level**
(20 buy/strong-buy vs 1 sell; Truist just *initiated at Hold with a $55 target*, above the
$41 spot) even as the stock collapses — a standing squeeze/re-rate risk — while the *revision
momentum* is quietly deteriorating (hold count 6→9 over four months). OKLO-specific **news
tone is bearish** ("What's Wrong With Oklo's Stock?", "Tumbling") but the nuclear **theme**
carries bullish headlines that keep favoring *other* names (ARK doubling into X-Energy; NJ's
$24B nuclear plan tilting to Cameco/Brookfield) — OKLO lagging its theme yet again. Net gate:
**CAUTION** (cut one size step); express any bearish view **defined-risk only**, and respect
the 08-10 earnings squeeze window.

## Key signals

- **Crowded short: 19.29% of float** (27.2M sh, $1.65B), DTC ~2.6, as-of 2026-06-15
  [SENT:short_float WebSearch:marketbeat semi-monthly]
- **SI eased off the May peak**: 10.9% (Jan) → 20.3% (Apr) → 24.9% (May) → **19.3% (Jun)** —
  partial covering already [SENT:short_float WebSearch]
- **Analysts still net-bullish (20 buy / 1 sell)**, Truist initiates **Hold, PT $55** (>spot)
  — contrary to the short [SENT:recom finnhub]
- **Revision momentum softening**: hold count 6→6→8→9 (Apr→Jul) while buys flat — slow tilt
  toward the thesis [SENT:recom finnhub]
- **OKLO-specific news bearish; theme bullish for peers**: "What's Wrong With Oklo",
  "Tumbling" vs ARK→X-Energy, NJ nuclear→Cameco [SENT:news finnhub]

## Detailed findings

### News flow (14d tone, 29 items; ≤ as-of) — [SENT:news finnhub]

OKLO-specific tone **bearish/questioning**: 07-16 "Oklo Stock is Tumbling Today" (Benzinga),
07-14 "What's Wrong With Oklo's Stock?" (Yahoo), 07-14/07-15 "Truist Initiates … **Hold**,
PT $55". Theme-level tone **bullish but pointed elsewhere**: 07-14 "Cathie Wood's ARK Doubles
Down on Nuclear" (favorite = **X-Energy**, not OKLO), 07-14 "NJ $24B Nuclear — **Cameco**,
Brookfield best positioned", 07-17 generic SMR-future piece. **The tape LED the news** (price
had already fallen ~37% before the "what's wrong" coverage). Read: OKLO is the *laggard*
inside a still-loved theme — consistent with phase-0.5 (CCJ/GEV/BE lead the flow).

### Analyst-revision momentum — [SENT:recom finnhub]

| Period | strongBuy | Buy | Hold | Sell | strongSell |
|---|---:|---:|---:|---:|---:|
| 2026-07-01 | 5 | 15 | **9** | 1 | 0 |
| 2026-06-01 | 5 | 15 | 8 | 1 | 0 |
| 2026-05-01 | 5 | 16 | 6 | 1 | 0 |
| 2026-04-01 | 5 | 14 | 6 | 1 | 0 |

Level is **strongly bullish** (20 buy-side vs 1 sell) — a **contrary axis** to the short and a
squeeze/re-rate risk. But the **direction** is softening (holds 6→9, buys flat) — analysts are
slowly capitulating toward the price, not against it. Truist's fresh **Hold/$55** is the newest
mark: cautious, but the $55 target still implies ~34% *upside* from spot. `fz` Recom/target
**null** (degraded quote) — no cross-source check this run.

### Retail vs institutional — [SENT: phases 1–2]

Lit tape: retail-ish front-week ATM call activity ($41.5c) but **being sold on the bid**
(phase-1) — not euphoric retail buying. Dark pool: mild large-tier dip-buy (0.611, phase-2)
but no mega conviction. **No clean retail-euphoria-vs-institutional-distribution divergence** —
both sides are muted/mixed. Not a fade-the-crowd trigger on this axis.

### Short interest & borrow — [SENT:short_float WebSearch]

| As-of (semi-monthly) | % float short | Shares | Days-to-cover |
|---|---:|---:|---:|
| 2026-01-21 | 10.9% | 17.0M | 2.0 |
| 2026-04-15 | 20.3% | 28.6M | 3.0 |
| 2026-05-15 | 24.9% | 35.1M | 2.6 |
| **2026-06-15** | **19.3%** | **27.2M** | **2.6** |

**Crowded short (19.3% of float)** but **liquid (DTC ~2.6)** → the squeeze can unwind in <3
sessions of average volume, so mechanics are *moderate*, not the explosive DTC>5 profile.
Borrow-fee / HTB tag **not found** in search (no explicit borrow-rate data surfaced) — record
n/a; the low DTC suggests borrow is likely available rather than hard-to-borrow. **This is the
central hazard for a fresh short.** SI is ~1 month lagged (semi-monthly settlement).

### Positioning extremes — [SENT: phases 0.5, 5]

P/C z-score **0.171 (NORMAL)** (phase-5), IV-rank **32.7** (mid, phase-0.5). **No sentiment
extreme** — no contrarian mean-reversion trigger on the options-positioning axis.

## Divergences

- **Analysts net-bullish (20 buy/1 sell, $55 PT) vs −79%-from-high price collapse** — Wall
  Street has not capitulated; re-rate/squeeze risk to the short.
- **Nuclear-theme bullish headlines favor peers (X-Energy, Cameco) not OKLO** — OKLO
  under-owned by the theme's fresh money; confirms relative weakness but also means a
  theme-rotation *back* to OKLO would squeeze.
- **Crowded short (19% float) vs a fresh short thesis** — you'd be joining a crowded trade.

## Source calls (audit)

| Source | Result |
|---|---|
| `company-news` (finnhub, 14d) | ok — 29 items, OKLO-bearish / theme-mixed |
| `stock/recommendation` (finnhub) | ok — 20 buy / 1 sell, holds rising |
| `fz quote` short_float/float/Recom | **null (degraded fz)** — SI via WebSearch |
| WebSearch short interest | ok — 19.3% float, DTC 2.6 (6/15) |
| WebSearch borrow/HTB | not found — borrow tag n/a |

## Source errors

`fz` short-float/float/Recom fields null (degraded quote, consistent across phases 0/5/7b) →
short interest sourced from WebSearch (MarketBeat/Fintel/X aggregations of exchange
semi-monthly data). Borrow-fee not located. No abort.

## Verdict for downstream

```
sentiment_signal:  BEARISH        # OKLO-specific news + softening revision momentum
crowd_state:       CROWDED_SHORT  # 19.29% of float short (2026-06-15, semi-monthly)
short_interest:    19.29% float [WebSearch, semi-monthly 2026-06-15] ; days_to_cover: 2.6 ; borrow: n/a (likely EASY given low DTC) [WebSearch]
tier_adjustment:   CAUTION        # crowded-short + still-bullish analysts = one+ contrary axis → cut one size step; near the VETO line for a NAKED short
divergences:       [ "analysts 20-buy/1-sell + $55 PT vs -79%-from-high price",
                     "nuclear theme bullish for peers (ARK->X-Energy, NJ->Cameco), OKLO lags",
                     "crowded 19% short into a fresh short thesis" ]
key_risks:         [ "Crowded short (19% float) + 2026-08-10 earnings = squeeze window",
                     "Cash-rich (7b) + 52-week-low level = downside floor / bounce risk",
                     "Bullish analyst base ($55 targets) could re-rate on any milestone win" ]
```

- **Conviction:** 3 / 5. The crowd read does **not** support piling into the short; it caps
  it. Phase-9: **defined-risk expression only** (put debit spread over naked short/puts),
  modest size, and treat 08-10 earnings as a hard squeeze catalyst to be out of or hedged
  around.
- **Open questions:** Does the phase-8 desk + phase-8b debate judge the squeeze risk as
  dominating the downtrend edge (→ VETO/stand-aside) or as a manageable, defined-risk
  continuation short? Is there a bearish structure that profits from further downside while
  capping the squeeze loss and the earnings gap?
