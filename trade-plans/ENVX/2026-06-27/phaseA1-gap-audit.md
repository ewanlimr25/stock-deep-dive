# Phase A1 — Critical-Information Gap Audit — ENVX (2026-06-27)

Grades available evidence against `rubrics/gap-rubric.md`. Substrate = fresh deep dive `research/ENVX/2026-06-26/` (age 1 day, full phase set) + live `chart_engine.py` (yfinance, 373 sessions).

## Checklist

### A. Directional evidence (the "why")
| # | Input | Status | Source / where |
|---|-------|--------|----------------|
| A1 | Options flow / sweeps | **HAVE** | `phase-1-flow.md` — $6-Oct call ask-sweep **$871,964 / 6,738 ct / 84.2% ask** [FLOW:sweeps] |
| A2 | Dark-pool / block accumulation | **HAVE** | `phase-2-dark-pool.md` — DP value area $5.95; supply shelf $6.28–6.33 [DP:price_levels] |
| A3 | OI / positioning (walls, pins) | **HAVE** | `phase-3-positioning.md` — $6-Oct build, $8 call-OI wall, $6 max-pain [OI] |
| A4 | Dealer structure (GEX/DEX/ZGL) | **HAVE** | `phase-4-structure.md` — **long-gamma 30/30 sessions**, max-pain $6.00, gamma-flip $5.50 [STRUCT:max_pain] |
| A5 | Historical signal win-rate (Kelly p) | **HAVE** | `phase-5-historical.md` — bullish_flow backtest **p=0.20, n=5**, avg move −0.05% (negative edge, thin N — but the input is present) [HIST] |

### B. Price structure (the "where")
| # | Input | Status | Source / where |
|---|-------|--------|----------------|
| B1 | OHLCV history (≥150 sessions) | **HAVE** | `chart_engine.py` yfinance — 373 daily sessions, `available: true` |
| B2 | Support/resistance + swing pivots | **HAVE** | derived B1 → `chart.json` (A2); corroborated by DP/gamma levels |
| B3 | Trend / market structure | **HAVE** | `chart.json` ma_stack **mixed/bearish** (spot < all SMAs), MACD bearish |
| B4 | Chart patterns | **HAVE (capped medium)** | derived B1 → `chart.json patterns` (A2) |
| B5 | Fibonacci / measured-move | **HAVE** | derived B1 → `chart.json fibonacci` (A2) |
| B6 | ATR / volatility for stops | **HAVE** | `chart.json indicators.atr14` = 0.56 (**10.49%**) |

### C. Context (the "when / what breaks it")
| # | Input | Status | Source / where |
|---|-------|--------|----------------|
| C1 | Macro regime + sector rotation | **HAVE** | `phase-6-macro.md` — TRANSITIONAL/CHOPPY (breadth 38%), Industrials net −$61.6M (adverse), beta 2.31, 10y 4.40% [MACRO] |
| C2 | Event calendar | **HAVE** | July OPEX Jul-17 ($6 magnet); earnings ~Aug-12; late-July FOMC (date soft — see C6) |
| C3 | Fundamentals quality veto | **HAVE** | `phase-7b-fundamentals.md` — **CONFIRM** (0/3 axes contradict); 4/4 beats, but cash-burning, EPS next-Y −1.36% [FUND] |
| C4 | Sentiment / crowd / short interest | **HAVE** | `phase-7c-sentiment.md` — **CROWDED_SHORT**, SI 26.00%, 49.12M sh, DTC 7.45, HTB [SENT:short_float] |
| C5 | Implied / expected move | **HAVE** | front-expiry ±2.42% / ±$0.14; **VRP −0.17 → PREMIUM_BUYING** (cheap vol) [CTX:implied_move] |
| C6 | Earnings date (expiry selection) | **PARTIAL** | **~Aug-12 by IR cadence; UW shows 07-30, flagged likely stale & unconfirmed** (phase-6 L141–142). Two candidate dates resolved by cadence, not a clean source match. |

## Completeness
- HAVE = 16 / 17, PARTIAL = 1 (C6), MISSING = 0 → **completeness = 94%**.

## Missing / gaps
| Item | Severity | how_to_source |
|------|----------|---------------|
| Confirmed Q2 earnings date (UW 07-30 vs IR-cadence ~Aug-12) | **important** | `fz quote ENVX` / `finnhub_enrich.py --ticker ENVX --date 2026-06-27` / ENVX IR page — re-confirm before placing; if it is 07-30 the squeeze catalyst arrives 2 weeks sooner (less theta carry) |
| Live intraday tape / next-day OI confirmation of the $6-Oct build | nice_to_have | `uw oi biggest-increases --symbol ENVX --json` + `uw options-flow sweeps --symbol ENVX --json` morning-of — confirms the sweep was real accumulation, not a one-off [OI:biggest_increases] |

**Why C6 is not critical here:** both candidate earnings dates (07-30 and ~Aug-12) fall **inside the sanctioned Oct-16 expiry**, so expiry selection is robust regardless. The date only shifts *carry duration / theta budget* and squeeze timing — hence `important`, not `critical`.

## Verdict: **SUFFICIENT**
All `critical` inputs present (A1+A2+A4 flow/positioning, B1 price history, A5+C5 edge & priced move) and completeness 94% ≥ 75%. → A4 may publish a **full plan, sizing per rubric** — no gap-driven size cut.

**Important distinction:** SUFFICIENT = the evidence is complete enough to decide well. It does **not** imply an edge — here the empirical edge is **negative** (backtest 20%, raw Kelly −0.143) and the read is **DIVERGENT** (bullish lone-sweep vs bearish downtrend). Those are conviction constraints resolved in A3/A4, not information gaps; expect the plan to remain RANGE / defined-risk / size-0.

## Sourcing plan (ordered)
1. `fz quote ENVX` → confirm next earnings date (resolve 07-30 vs Aug-12) before any pre-earnings sizing.
2. `uw oi biggest-increases --symbol ENVX --json` → verify tomorrow's OI confirms the $6-Oct call build (one-off vs campaign).
3. `uw options-structure gex --symbol ENVX --dte-max 120 --json` + `uw options-flow sweeps --symbol ENVX --json` → re-confirm the long-gamma $6 pin and any follow-on flow morning-of.
