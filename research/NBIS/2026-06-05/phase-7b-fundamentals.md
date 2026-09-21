# Phase 7b — Deep Fundamentals & Quality Veto (FINNHUB)

**Ticker:** NBIS
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T21:35:00-0400
**Upstream phases cited:** phase-0-intake.md, phase-6-macro.md, phase-7-insights.md

## Summary

The fundamental trend **contradicts the bearish flow bias on 2 of 3 veto axes**
→ `tier_adjustment = VETO` on a *directional short*. The business is improving
fast: 4/4 quarterly EPS beats with narrowing losses (−0.38 → −0.32, surprise
+20% → +59%), Q1-26 revenue $399M beat consensus ($389M), AI-cloud ARR +54%
QoQ to $1.92B, FY26 guide $3–3.4bn revenue at ~40% adj-EBITDA margin, TTM
revenue growth +528%. Only the insider axis confirms the bears: **7 distinct
insiders sold 1,197,934 shares across 23 transactions in 6 months with zero
open-market buys**. The bear case that *survives* the veto is not about the
business trend — it is valuation + funding: P/S ~65, a PE built on
non-operating gains (net margin +93.1% against **operating margin −70.6%**),
and **$16–20bn planned capex against $3–3.4bn revenue** — an external-funding
dependence that phase-6's hawkish rates repricing directly threatens. Analyst
consensus is Buy (Recom 1.94; avg target $238.86, +4.9% vs spot) — no
analyst-vs-flow divergence panic, but BofA's raised target ($205, May-11) sits
*below* Friday's close.

## Key signals

- Earnings-surprise history: **4/4 beats**, surprisePercent +20.2 → +26.0 →
  +39.9 → **+59.1** (improving cadence) `[FUND:earnings_surprises]`
- Growth: revenueGrowthTTMYoy **+527.97%**; Q1-26 ARR $1.92B (+54% QoQ); FY26
  guide $3–3.4bn / ~40% adj EBITDA `[FUND:metric]`
  `[FUND:guidance WebSearch:stockanalysis.com/quartr.com]`
- Quality flag: netProfitMarginTTM **+93.09%** vs operatingMarginTTM
  **−70.55%** — profits are revaluation/one-off-driven, not operational;
  peTTM 70.15 is not an operating multiple `[FUND:metric]`
- Insiders: code **S ×23, −1,197,934 shares, 7 distinct sellers**; code M ×4
  (exercises); **zero P (open-market buys)** in 6 months to as-of
  `[FUND:insider_transactions]`; no 30-day cluster either side
  `[FUND:insider_cluster fz]`
- Funding intensity: FY26 **capex $16–20bn vs revenue $3–3.4bn**; LT-D/E 1.16
  with current ratio 8.33 (cash-rich today, structurally capital-hungry)
  `[FUND:metric]` `[FUND:capex WebSearch:northwiseproject.com]`

## Detailed findings

### Valuation

| Metric | NBIS | Note |
|---|---|---|
| peTTM | 70.15 | contaminated by one-off gains (see margins) |
| peNormalizedAnnual | 694.89 | the "real" operating multiple is meaningless-high |
| P/S TTM | **65.30** | extreme even for the cohort |
| P/B | 7.92 | |
| Forward P/E | "−" (negative fwd EPS) `[FUND:recom fz]` | still loss-making on consensus |
| Market cap | $57.3bn | |

Cross-source analyst read: fz Recom **1.94** (buy), target **$252.43** (+10.8%)
`[FUND:recom fz]`; S&P Global consensus (16 analysts) **Buy, avg target
$238.86** (+4.9%); BofA raise May-11: $175 → **$205** — below spot
`[FUND:analyst WebSearch:stockanalysis.com/thestreet.com]`. No flow-vs-analyst
divergence (both lukewarm-positive), resolving phase-7's empty analyst leg.

### Growth profile

revenueGrowthTTMYoy +527.97%; Sales Q/Q +621.52% `[FUND:metric]` `[FUND: fz]`;
grossMarginTTM 72.06%; operatingMarginTTM −70.55% (heavy DC build-out opex/D&A);
EPS losses narrowing 4 straight quarters. EPS next Y +36.75% (improvement rate,
still negative level) `[FUND: fz]`. Trajectory: unambiguously improving on
revenue/ARR; profitability still structurally distant.

### Earnings-surprise history (4 quarters available — listed FY2025; beat-rate 4/4)

| Period | Actual EPS | Estimate | Surprise | Surprise % |
|--------|-----------:|---------:|---------:|-----------:|
| 2026-03-31 | −0.32 | −0.7831 | +0.4631 | **+59.14%** |
| 2025-12-31 | −0.70 | −1.1648 | +0.4648 | +39.90% |
| 2025-09-30 | −0.40 | −0.5406 | +0.1406 | +26.01% |
| 2025-06-30 | −0.38 | −0.4760 | +0.0960 | +20.17% |

All rows ≤ as-of (look-ahead filter applied; only 4 quarters exist on the free
tier for this recently-relisted name).

### Forward consensus

Finnhub `eps-estimate` / `revenue-estimate`: **paid, skipped** (verbatim:
`{"error":"You don't have access to this resource."}`). WebSearch fallback:
FY26 revenue guide **$3–3.4bn**; ARR target **$7–9bn** by YE-26; Q1 pre-print
consensus was $389M (actual $399M — beat); consensus direction: **rising**
(guide reaffirmed/raised at Q1, BofA target raised pre-earnings)
`[FUND:consensus WebSearch:stockanalysis.com/quartr.com/thestreet.com]`.

### Balance-sheet health

`financials-reported` not pulled (free-tier statements unreliable; metric
proxies used per phase guidance): currentRatioQuarterly **8.33** (large cash
position post-raises), ltDebtEquityQuarterly **1.16** (convertibles +
DC financing already material). The $16–20bn capex plan implies continuous
debt/equity issuance — **rate-sensitive** (phase-6: DGS2 +17bp/30d, hike
pricing).

### Cash-flow quality

Proxy read: gross margin 72% but operating margin −70.6% and capex 5–6× revenue
→ deeply FCF-negative by construction during build-out. The +93.1% net margin
is non-cash/one-off (stake revaluations), not quality earnings.

### Insider signal

MSPR: `insider-sentiment` returned `[]` (known-empty on this key). Fallback —
`insider-transactions` (2025-12-05 → 2026-06-05), grouped by code
`[FUND:insider_transactions]`:

| Code | Transactions | Net shares | Distinct names |
|---|---|---|---|
| S (sale) | 23 | **−1,197,934** | **7** |
| M (option exercise) | 4 | 0 | 1 |
| P (open-market buy) | 0 | — | 0 |

`fz insider-clusters --days 30` (buy and sell): **no NBIS rows** — the selling
is persistent-distributed, not a 30-day cluster `[FUND:insider_cluster fz]`.
Insider axis = bearish (sustained distribution into the rally).

### Peers — relative value (hand-picked neocloud cohort; Finnhub `peers` returned only `["NBIS"]`)

| Ticker | P/E | Fwd P/E | EPS next Y | Short Float | Float | Perf YTD | Mcap |
|--------|----:|--------:|-----------:|------------:|------:|---------:|-----:|
| **NBIS** | 76.01* | − | +36.75% | **22.43%** | 201.04M | +172.2% | $57.3bn |
| CRWV | − | − | +73.37% | 15.26% | 337.14M | +40.2% | $54.8bn |
| IREN | 187.2 | 133.1 | +185.5% | 15.71% | 324.15M | +43.9% | $19.4bn |
| APLD | − | − | −10.77% | 30.43% | 258.69M | +61.6% | $11.3bn |

(*one-off-gain-contaminated; sources `[FUND:peer_pe fz]`, phase-0 float
snapshot.) NBIS is the group's YTD leader by 3–4× with the second-highest short
float — the most squeeze-prone *and* the most de-rate-exposed of the cohort.
Cohort-wide: nobody has a clean P/E; the whole group trades on ARR ramp.

## Red flags

1. **Capex $16–20bn vs revenue $3–3.4bn** — funding gap must be raised in
   markets that just repriced hawkish (phase-6).
2. **Earnings quality**: net margin +93% / operating margin −70.6% — reported
   profits are revaluations; operating losses persist.
3. **Persistent insider selling**: 7 sellers, −1.2M shares, 0 buys in 6 months.
4. P/S 65 into a sector derating event (phase-6 AVGO guide-down).

## Tool / source calls

| Source | Status | Key values |
|---|---|---|
| Finnhub `/stock/metric` | ok | PE 70.15, P/S 65.30, rev growth +527.97%, opM −70.55%, CR 8.33, D/E 1.16 ← `.metric.*` |
| Finnhub `/stock/earnings` | ok (4 rows) | table above ← `[.[] \| select(.period <= "2026-06-05")]` |
| Finnhub `/stock/eps-estimate` | **paid, skipped** | error verbatim below |
| Finnhub `/stock/revenue-estimate` | **paid, skipped** | error verbatim below |
| Finnhub `/stock/peers` | degenerate (self only) | `["NBIS"]` → fz cohort substituted |
| Finnhub `/stock/insider-sentiment` | empty `[]` | → insider-transactions fallback |
| Finnhub `/stock/insider-transactions` | ok | S×23 −1,197,934 sh / 7 names ← group_by(.transactionCode) |
| `fz insider-clusters` (buy+sell, 30d) | ok | no NBIS rows |
| `fz quote` NBIS/CRWV/IREN/APLD | ok | Recom 1.94, target 252.43; peer table |
| WebSearch (consensus/guidance) | ok | FY26 $3–3.4bn, ARR $7–9bn, capex $16–20bn, consensus $238.86 |

## Tool / source errors

- `eps-estimate` / `revenue-estimate`: `{"error":"You don't have access to this
  resource."}` — paid tier; WebSearch fallback used (per established workaround).
- `insider-sentiment`: `[]` (empty data array) — insider-transactions-by-code
  fallback used.
- `peers`: returned `["NBIS"]` (self only) — hand-picked neocloud cohort
  (CRWV/IREN/APLD) substituted via `fz quote`; flagged as judgment-based.
- Finnhub `/stock/metric` is TTM-current (captured 2026-06-06), not strictly
  point-in-time for the as-of date; price-linked ratios (PE/PS) reflect the
  227.81 close — consistent here, but flagged per pitfalls.

## Verdict for downstream phases — the quality gate

```
fundamental_signal:  BULLISH        # trend axes: beats accelerating, ARR +54% QoQ, guide intact
                                    # (qualified: valuation extreme, earnings quality poor)
tier_adjustment:     VETO           # vs the phase-1→7 BEARISH flow bias:
                                    #   earnings_trend  = improving  → contradicts bear bias
                                    #   growth/margins  = improving  → contradicts bear bias
                                    #   insider         = selling    → confirms bear bias
                                    # contradictions = 2 ≥ 2 → VETO the directional SHORT
contradiction_count: 2
insider_cluster:     {present: n, distinct_buyers: n/a, side: n/a}   # but 7 sellers/−1.2M sh over 6mo, 0 buys
key_risks:
  - "Capex $16–20bn vs revenue $3–3.4bn: external-funding dependence into a hawkish rates repricing (DGS2 4.05%)"
  - "P/S ~65 with non-operational earnings (opM −70.6%): maximal multiple-compression exposure in an AI-capex derating"
  - "7 insiders sold 1.2M shares in 6 months, zero buys — distribution into the rally"
```

**Phase-9 effect (rubric):** a *directional short* on flow alone is
**watch-only / 0%**; carry-only defined-risk structures remain allowed. Note
the gate is downside-only: it cuts the short thesis; it does NOT mint a long
thesis — the long side carries its own red flags (valuation, funding, insiders)
and phase-7c/8b must weigh the 22.43% short float separately.
