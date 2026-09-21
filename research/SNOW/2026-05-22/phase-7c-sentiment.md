# Phase 7c — Sentiment, Positioning & Short Interest

**Ticker:** SNOW
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T16:58:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-5-historical.md, phase-7-insights.md, phase-7b-fundamentals.md

> **Look-ahead guard:** news filtered to `≤ 2026-05-22`; analyst-recommendation
> periods `≤ 2026-05-22`. Nothing post-as-of (and real "today" 5/26 is pre-earnings).

## Summary

The crowd is **heavily, one-sidedly long into the print — and the smart money is not
confirming it.** Sell-side consensus is **~86% buy-or-better** (50 of 58:
strongBuy 17 / buy 33 / hold 7 / sell 1), stable-to-improving [SENT:revision_trend];
14-day news tone is **bullish** (GSA OneGov data deal, "AI trade is back," Citizens
Market Outperform $325 PT) with one dissent (5/15 downgrade to Hold)
[SENT:company_news]; the stock is **+32% into the event**. Yet the lit options tape is
**dominated by retail small-lots net-buying calls** ($14.2M in ≤5-lot trades, the
largest bucket, ask-leaning) while **institutional block flow is tiny and balanced**
($3.0M / 11 trades) [SENT:retail_vs_inst DUCKDB] — and the dark pool is balanced
(phase-2), insiders are only selling (phase-7b). This is a textbook **CROWDED_LONG
without smart-money confirmation**. It is not an extreme (P/C z −0.65 NORMAL, no
|z|>2) and the DP is balanced not distributing, so it **CAUTIONS, not VETOES** — but
it is a clear fade-risk on anyone chasing the long into the binary. Short interest
unavailable (blind spot).

## Key signals

- **Analyst consensus ~86% bullish, stable** (sB17/B33/H7/S1, strongBuy 16→17 over 4
  months) [SENT:revision_trend] — crowded long, revisions not deteriorating.
- **News tone bullish, momentum-confirming** (GSA OneGov deal 5/21, software-ETF/AI
  revival, $325 PT) [SENT:company_news] — narrative fueled the +32% run.
- **Retail dominates the lit tape, net-buying calls:** ≤5-lot bucket $14.2M (ask
  $7.83M / bid $6.33M); >100-lot institutional only $3.0M, balanced
  [SENT:retail_vs_inst DUCKDB] — euphoria without institutional confirmation.
- **No smart-money confirmation:** DP balanced (phase-2 0.486), insiders only selling
  (phase-7b 38M sold / 0 bought), price-vs-flow divergence (phase-7).
- **Not an extreme:** P/C z −0.65 NORMAL [SENT:pc_zscore], IV rank 86.8 (96th universe
  pctile but 57th self) [CTX:iv_rank] — crowded, but no contrarian-trigger extreme.

## Detailed findings

### News flow (14d tone; lead/lag) [SENT:company_news]

20 items 2026-05-08→05-22, net **bullish/constructive**. Drivers: **GSA OneGov
agreement** to accelerate government data adoption (5/21, Benzinga); SNOW leading the
**Open Semantic Interchange (OSI)** AI-data standard with Zeta (5/14, 5/20);
"Forgotten AI Trade Is Back — software ETFs outpace QQQ" (5/19); **Citizens reiterates
Market Outperform, $325 PT** (5/19); SeekingAlpha "Risk/Reward Finally Favors The
Bulls" (5/15) and "A Great Time To Buy" (5/22). Dissent: SeekingAlpha downgrade to
**Hold** on "market concerns" (5/15); "Why SNOW Is Falling Wednesday" (5/20). **The
news LED the rally** (AI-standard narrative + GSA deal) — sentiment is rich and
already in the tape.

### Analyst-revision momentum [SENT:revision_trend]

| Period | strongBuy | buy | hold | sell | strongSell |
|--------|-----------|-----|------|------|------------|
| 2026-05-01 | 17 | 33 | 7 | 1 | 0 |
| 2026-04-01 | 17 | 33 | 7 | 1 | 0 |
| 2026-03-01 | 17 | 31 | 8 | 1 | 0 |
| 2026-02-01 | 16 | 33 | 7 | 1 | 0 |

~86% buy-or-better, **stable-to-slightly-improving** (strongBuy 16→17, hold 8→7). No
downgrade cycle. Wall Street is crowded long and not turning — which, for a contrarian
read into a richly-priced print, is a *yellow* flag (less room for upgrades, lots of
room for disappointment).

### Retail vs institutional (lit small-lot vs block) [SENT:retail_vs_inst DUCKDB]

Ex-0DTE lit premium by trade size:

| lot bucket | ask $M | bid $M | read |
|------------|--------|--------|------|
| ≤5 (retail) | **7.83** | 6.33 | net call-buying; LARGEST bucket ($14.2M) |
| 6–20 | 4.56 | 3.96 | slight buy |
| 21–100 | 3.55 | 4.02 | slight sell |
| >100 (institutional) | 1.69 | 1.35 | balanced, tiny ($3.0M, 11 trades) |

**Retail is the marginal buyer; institutions are barely present and balanced.**
Combined with balanced dark pool (phase-2) and insider selling (phase-7b), the bullish
lit-call activity is **retail-driven, not smart-money-confirmed**.

### Short interest & borrow

**Unavailable** — Finnhub `/stock/metric` short fields returned null; WebSearch
deliberately not used (look-ahead control). Qualitatively, SNOW is a large, liquid
$57B name → borrow almost certainly **EASY**, not a squeeze candidate, but **%float
short is a blind spot** (`n/a`). Do not infer a squeeze tailwind or hazard either way.

### Positioning extremes [SENT:pc_zscore][CTX:iv_rank]

P/C z-score **−0.65 = NORMAL** (phase-5); today is call-heavier than its 20d norm but
not a |z|>2 extreme. IV rank 86.8 = 96th universe pctile but only 57th self-pctile
(phase-0.5) → rich vs market, normal for SNOW. **No contrarian-trigger extreme** — the
crowding is directional/positioning, not a vol/sentiment blow-off.

## Divergences

1. **Retail call-buying + institutions absent/DP balanced + insiders selling** — the
   bullish lit bid has no smart-money confirmation [SENT:retail_vs_inst DUCKDB].
2. **86% analyst-buy + bullish news + +32% price** vs **net-bearish options flow**
   (phase-7 divergence) — the crowd is long, the flow isn't.
3. **Narrative bullish (AI-data standard, GSA deal)** vs **dealer/positioning says
   capped & event-binary** (phase-3/4) — story richer than the structure.

## Source calls (audit trail)

| Source | Status | Result |
|--------|--------|--------|
| `/company-news` (14d, ≤as-of) | ok | 20 items, net bullish, news led the rally |
| `/stock/recommendation` (≤as-of) | ok | ~86% buy, stable-improving |
| `/stock/metric` short fields | null | short interest unavailable |
| DuckDB §A lot-size split | ok | retail $14.2M dominant; institutional $3.0M balanced |
| WebSearch (SI/news) | not used | look-ahead control (as-of run, pre-earnings) |

## Source errors

(none fatal. Short-interest %float a blind spot — Finnhub null, WebSearch withheld.)

## Verdict for downstream

```
sentiment_signal:  NEUTRAL    # crowd is bullish (a contrarian yellow flag), but no extreme; net neither confirms nor reverses
crowd_state:       CROWDED_LONG   # ~86% analyst buy + retail net call-buying + +32% run + bullish news
short_interest:    n/a (Finnhub null) ; borrow: EASY (inferred, large-cap) — not a squeeze factor
tier_adjustment:   CAUTION    # one contrary axis: crowded long WITHOUT smart-money confirmation into the binary → cut one size step
divergences:       [ "retail call-buying vs institutions absent/DP balanced/insiders selling",
                     "86% analyst-buy + +32% price vs net-bearish options flow",
                     "bullish AI-data narrative vs capped, event-binary dealer structure" ]
key_risks:         [ "crowded long: one-sided bullish positioning into a ±13% binary unwinds violently on disappointment",
                     "no smart-money confirmation of the retail/analyst bid (DP balanced, insiders selling)",
                     "short interest a blind spot — squeeze fuel can't be assessed either way" ]
```

**Reconciliation:** sentiment does **not** flip the thesis — it sharpens it. The
CROWDED_LONG read + lack of smart-money confirmation is the *positioning-side* twin of
phase-7b's *valuation-side* "priced for perfection." Both are downside-only CAUTIONs
that argue for **defined-risk, reduced size, and skepticism toward chasing the long**
— coherent with phase-6 (TRANSITIONAL, half-size) and phase-7 (divergence), not a new
direction.
