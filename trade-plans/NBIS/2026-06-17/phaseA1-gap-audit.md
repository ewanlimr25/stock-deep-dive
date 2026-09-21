# Phase A1 — Critical-Information Gap Audit — NBIS 2026-06-17

## Checklist (against rubrics/gap-rubric.md)

| # | Input | Status | Where |
|---|-------|--------|-------|
| A1 | Options flow / sweeps | HAVE | phase-1: sweeps 5/5, $722.4M |
| A2 | Dark pool / blocks | HAVE | phase-2: mega-tier 93.6% sell |
| A3 | OI / positioning (walls, pins) | HAVE | deep-dive levels: pin 267.5, call wall 300 |
| A4 | Dealer structure (GEX/DEX/ZGL) | PARTIAL | DEX +$2.88bn HAVE; **gamma_flip 34.64 is a bad value** |
| A5 | Historical signal win-rate (Kelly p) | HAVE | phase-5: bullish_flow 0.375 (n=8) |
| B1 | OHLCV history | HAVE | chart.json, yfinance, 372 sessions |
| B2 | Support/resistance + pivots | HAVE | chart.json support_resistance + recent_pivots |
| B3 | Trend / structure | HAVE | uptrend HH-HL; bullish MA stack |
| B4 | Chart patterns | HAVE | double_bottom (low); Elliott discarded |
| B5 | Fibonacci / measured moves | HAVE | up-swing retracements |
| B6 | ATR / volatility | HAVE | ATR 24.29 |
| C1 | Macro regime + rotation | HAVE | tech inflow 0.8; hawkish FOMC |
| C2 | Event calendar | HAVE | OPEX 6/18, NDX 6/22, CPI 7/15, ER 8/6 |
| C3 | Fundamentals veto | HAVE | MSPR -100 (CAUTION) |
| C4 | Sentiment / crowd / SI | HAVE | CROWDED_LONG; easy borrow |
| C5 | Implied / expected move | HAVE | 4.86% / $13.66 |
| C6 | Earnings date | HAVE | 8/6 (beyond horizon) |

**Completeness:** 17/18 fully present → **94%** (A4 partial counts as 0.5 → reported 92%).

## Missing / how to source

| Item | Severity | How to source |
|------|----------|---------------|
| `gamma_flip` 34.64 implausible (scale/data artifact) | important | `uw options-structure gex --symbol NBIS --dte-max 45 --json` → real ZGL |
| Live intraday tape for 6/22 timing | nice_to_have | `uw options-flow sweeps --symbol NBIS` + intraday yfinance on the day |
| Live borrow/HTB | nice_to_have | `fz quote NBIS --agent` + broker borrow fee |

## Verdict

**SUFFICIENT.** Every `critical` input (flow+DP, dealer DEX, price history, win-rate, expected move) is present. The lone `important` gap is a data-quality flag on one reused level — handled by setting `gamma_flip = null` and not using it as a trigger (the plan triggers off the chart swing-high and OI pin instead). Full plan may be written; sizing follows the (already conservative) deep-dive numbers.
