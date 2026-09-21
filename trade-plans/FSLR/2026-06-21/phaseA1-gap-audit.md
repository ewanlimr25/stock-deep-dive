# Phase A1 — Critical-Information Gap Audit

**Ticker:** FSLR **As-of:** 2026-06-21 **Verdict:** **USABLE_WITH_GAPS**

> *For research and educational use only. Not financial advice.*

## How this was graded

Substrate = the **stale** deep dive `research/FSLR/2026-05-18/` (anchor 2026-05-15,
~23 trading days old) **plus targeted live refreshes** I pulled at intake to cure
the most time-sensitive, decision-changing gaps (price has moved **+10%** since the
dive, so the gamma map and IV had to be re-read). Live refreshes are saved under
`trade-plans/FSLR/2026-06-21/_live/` (anchor **2026-06-18** EOD parquet):
`gex.json`, `dex.json`, `maxpain.json`, `ivterm.json`, plus two WebSearches
(Section 232 status; analyst PTs / earnings).

## Required-input checklist

### A. Directional evidence (the "why")
| # | Input | Status | Source / where |
|---|-------|--------|----------------|
| A1 | Options flow / today's sweep tape | **PARTIAL** | Reused 5/15 sweep campaign (two-tenor $280C, Mar-27 280C $1.39M vol/OI 10×) [FLOW]; **no live TODAY sweep prints**. Persistent call-heavy OI corroborates (below). |
| A2 | Dark-pool / block accumulation | **PARTIAL** | Reused 5/15 only (large-tier buy_ratio 0.535, $231.62 cluster $17.5M) [DP]; **not refreshed** — narrative is stale. |
| A3 | OI / positioning (walls, pins) | **HAVE** | **Fresh 6/18:** max-pain $260 cluster, P/C OI 5.06→19.1 (very call-heavy), per-strike map below [`_live/maxpain.json`]. |
| A4 | Dealer structure (GEX/DEX/ZGL) | **HAVE** | **Fresh 6/18:** GEX regime POSITIVE, ZGL $70.31, total +$10.7M; DEX +$666M (dealers BUY) [`_live/gex.json`,`dex.json`]. |
| A5 | Historical signal win-rate (Kelly p) | **PARTIAL** | Reused 5/15 `bullish_flow` backtest 26.3% win / −1.26% avg-20d, n=19 [HIST]; regime stat, semi-durable but stale. |

### B. Price structure (the "where")
| # | Input | Status | Source / where |
|---|-------|--------|----------------|
| B1 | OHLCV history (≥150 sessions) | **HAVE** | chart_engine.py, 371 yfinance sessions, `available:true`. |
| B2 | Support/resistance + pivots | **HAVE** | chart.json (computed in A2). |
| B3 | Trend / market structure | **HAVE** | chart.json; smoke read = pullback within uptrend (>sma50/200, <ema9/21). |
| B4 | Chart patterns | **HAVE** (engine-capped med) | chart.json (A2); manual confirm for any `high`. |
| B5 | Fibonacci / measured move | **HAVE** | chart.json (A2). |
| B6 | ATR / volatility for stops | **HAVE** | atr14 = **16.34** (atr% 6.77) — wide stops required. |

### C. Context (the "when / what breaks it")
| # | Input | Status | Source / where |
|---|-------|--------|----------------|
| C1 | Macro regime + sector rotation | **PARTIAL** | Reused 5/15 TRANSITIONAL / Tech −$151M [MACRO]; **not refreshed**. |
| C2 | Event calendar (earnings/FOMC/CPI/Sec232) | **PARTIAL** | **Sec 232 polysilicon STILL PENDING** ("clarified by end of month" — within ~9 days) [WebSearch:pv-tech.org]; June FOMC 6/16–17 **passed**; earnings ~7/30. |
| C3 | Fundamentals quality veto | **HAVE** | Reused: Q1-2026 GM 46.6% (vs 40.8% YoY), 45X tailwind, **no veto** [FUND]; quarterly → still valid. |
| C4 | Sentiment / crowd / short interest | **PARTIAL** | **Fresh PTs:** UBS $290→$330 (6/1), Mizuho $243→$300 (6/11), **Bernstein initiated Underperform (6/16)** [WebSearch:marketbeat]; short interest not pulled. |
| C5 | Implied / expected move (option width) | **HAVE** | **Fresh 6/18 IV term:** front 6/26 = **82.7%** → implied ±$30 (±11.6%); 7/17 ±$62. Elevated binary-event vol. |
| C6 | Earnings date (expiry selection) | **HAVE** | ~**2026-07-30** (deep dive), corroborated by **7/31 expiry IV bump 76.9%** vs 72.2% neighbors. |

**HAVE = 11 / 17 → completeness ≈ 65%** (PARTIAL counted strict-zero; 6 PARTIAL, 0 MISSING).

## Current gamma & pin map (fresh 6/18 — supersedes the stale 5/15 map for levels)

| Role | Strike | net_gex (6/18) | Note |
|------|--------|----------------|------|
| Upside magnet | **$270** | +$2.31M | next pull above $260 |
| Upside magnet / pin | **$260** | +$3.38M | max-pain cluster (7/02,7/17,7/31); 6/26 max-pain $265 |
| Local short-gamma chop | $252.5–$257.5 | −$0.33M to **−$1.04M** | spot $257 sits ON the $257.5 neg-gamma strike → moves amplified locally |
| Support magnet | **$250** | **+$4.33M** | largest single magnet; now BELOW spot → pin/support |
| Neg-gamma shelf | $245 | −$0.42M | below support magnet |
| Old put wall | $230 | −$0.40M | aligns with stale invalidation line |
| LEAP ceiling | $280 | +$1.13M | old two-tenor target |

**Read:** spot $257 is **pinned in a $250–$265 magnet box** with negative-gamma chop in
the middle. Bullish positioning (call-heavy OI, dealers buying, ZGL far below) is
**still intact 23 days on** — the flow thesis de-stales materially even though the
narrative phases (DP, agents, macro) were not re-pulled.

## Gaps — severity + how_to_source

| Gap | Severity | Why it matters | how_to_source |
|-----|----------|----------------|---------------|
| **Section 232 resolution unknown (binary, imminent)** | **important** | The single dominant catalyst; deep dive made "NO-TARIFF = same-day exit" an invalidation. Direction & event-vega both hinge on it. | Monitor `regulations.gov` / BIS / Commerce / pv-tech.org daily; WebSearch "Section 232 polysilicon determination" each session through end-June. |
| **Today's live sweep tape (A1)** | **important** | Tells whether NEW money is adding vs taking profit into the +10% run — distinguishes fresh LONG from finished move. | `uw options-flow sweeps --symbol FSLR`; `uw insights deep-dive --symbol FSLR`. |
| **Dark-pool refresh (A2)** | nice_to_have | Confirm accumulation vs distribution after the run. | `uw dark-pool largest/block-stratified --symbol FSLR`. |
| **Macro regime refresh (C1)** | important | TRANSITIONAL→? changes the sizing ceiling. | `uw risk market-regime`; `fred_macro.py`. |
| **Historical backtest refresh (A5)** | nice_to_have | The Kelly p; 26.3% bullish_flow hit-rate is the sizing brake. | `uw historical signal-backtest`. |
| **Short interest / borrow (C4)** | nice_to_have | Squeeze fuel in a call-heavy name. | `fz quote FSLR`; `fz_enrich.py`. |
| **Exact earnings date (C6)** | nice_to_have | Already strongly inferred (7/30); confirm to pick expiry that avoids crush. | `finnhub_enrich.py --ticker FSLR`; screener `next_earnings_date`. |

## Verdict

**USABLE_WITH_GAPS** — every **critical** input is present (dealer structure A4 +
price history B1 + implied move C5 are all **freshly** sourced; A1/A2 flow exists
via the reused dive and is corroborated current by persistent call-heavy OI), but
completeness is ~65% and three things temper conviction: **(1)** the dominant
catalyst (Sec 232) is **unresolved and binary**; **(2)** the directional *tape*
(today's sweeps) and the dark-pool/macro/agent narrative are **stale**; **(3)**
front-end IV is **very elevated (82.7%)**, so any long-premium structure fights vol
crush. → A3 cuts one conviction step (already mandated by stale-flow lesson L-0003);
**A4 caps size one step** and must prefer vega-aware structures.

### Sourcing plan (ordered) to lift toward SUFFICIENT
```
1. WebSearch "Section 232 polysilicon tariff determination June 2026"   # catalyst resolution (daily)
2. uw options-flow sweeps   --symbol FSLR --json --quiet                 # today's directional tape
3. uw insights deep-dive    --symbol FSLR --json --quiet                 # conviction matrix / accumulation refresh
4. uw risk market-regime    --json --quiet                              # is regime still TRANSITIONAL?
5. uw dark-pool block-stratified --symbol FSLR --json --quiet           # accumulation vs distribution post-run
6. uw historical signal-backtest --json --quiet                        # refresh the Kelly p
   # — or simply run /stock-deep-dive FSLR for a full fresh substrate before sizing up.
```
