# Phase A1 — Critical-Information Gap Audit — INTC (2026-06-27)

Grades available evidence against `rubrics/gap-rubric.md`. Substrate = fresh deep dive `research/INTC/2026-06-26/` (age 1 day) + live `chart_engine.py` (yfinance, 373 sessions).

## Checklist

### A. Directional evidence (the "why")
| # | Input | Status | Source / where |
|---|-------|--------|----------------|
| A1 | Options flow / sweeps | **HAVE** | `phase-1-flow.md` — 5/5-session bearish sweep campaign, $925.2M, consistency 1.0 [FLOW:sweep_persistence] |
| A2 | Dark-pool / block accumulation | **HAVE** | `phase-2-dark-pool.md` — DP shelf ~$128.32, supply band $132–133 / $140.94 [DP:price_levels] |
| A3 | OI / positioning (walls, pins) | **HAVE** | `phase-3-positioning.md` — Jul-17 $130 put +11,442 OI (ratio 4.11), ~73% bearish new OI; pins $120/$125/$130 [OI:biggest_increases] |
| A4 | Dealer structure (GEX/DEX/ZGL) | **HAVE** | `phase-4-structure.md` — ZGL $27.26, long-gamma pins +5.34M@120 / +4.16M@130, $128 neg-gamma notch [STRUCT:gex] |
| A5 | Historical signal win-rate (Kelly p) | **HAVE** | `phase-5-historical.md` — backtest p=0.667, n=9, payoff_b 1.77 [HIST] |

### B. Price structure (the "where")
| # | Input | Status | Source / where |
|---|-------|--------|----------------|
| B1 | OHLCV history (≥150 sessions) | **HAVE** | `chart_engine.py` yfinance — 373 daily sessions, `available: true` |
| B2 | Support/resistance + swing pivots | **HAVE** | derived B1 → `chart.json` (detailed in A2); corroborated by DP/OI levels |
| B3 | Trend / market structure | **HAVE** | `chart.json` ma_stack `bullish_stack` (spot>sma20>sma50>sma200) |
| B4 | Chart patterns | **HAVE (capped medium)** | derived B1 → `chart.json patterns` (A2); engine caps confidence at medium |
| B5 | Fibonacci / measured-move | **HAVE** | derived B1 → `chart.json fibonacci` (A2) |
| B6 | ATR / volatility for stops | **HAVE** | `chart.json indicators.atr14` = 9.97 (8.42%) |

### C. Context (the "when / what breaks it")
| # | Input | Status | Source / where |
|---|-------|--------|----------------|
| C1 | Macro regime + sector rotation | **HAVE** | `phase-6-macro.md` — hawkish Fed, Tech #1 outflow −$637.8M, $1.3T June semis selloff [MACRO] |
| C2 | Event calendar | **HAVE** | June CPI ~Jul-15 · OPEX Jul-17 · **earnings Jul-23 AMC** · FOMC Jul-29 |
| C3 | Fundamentals quality veto | **HAVE** | `phase-7b-fundamentals.md` — 4/4 EPS beats, +45.76% fwd EPS, insiders buying → **VETO** [FUND] |
| C4 | Sentiment / crowd / short interest | **HAVE** | `phase-7c-sentiment.md` — CROWDED_LONG, SI only 3.39% (no trapped shorts) [SENT] |
| C5 | Implied / expected move | **HAVE** | expected_move ±22% / ±$28.2 to Jul-17 (94% ATM IV); VRP +5.95 [CTX:implied_move] |
| C6 | Earnings date (expiry selection) | **HAVE (dual-confirmed)** | **Jul-23** confirmed by **UW screener AND fz** (phase-6 L164 "all match UW/fz"); resolves the stale-date risk |

## Completeness
- HAVE = 17 / 17 → **completeness = 100%**. PARTIAL = 0, MISSING = 0.

## Missing / gaps
- **None critical, important, or nice-to-have.** All directional, price-structure, and context inputs are present and fresh.
- **Watch-item (not a gap):** intraday/today's live tape is from a 1-day-old deep dive, not re-pulled at this hour. Sourcing if desired: `uw options-flow sweeps --symbol INTC --json` and `uw options-structure gex --symbol INTC --dte-max 45`. Classified `nice_to_have` — the day-old read is well within freshness and price is unchanged ($128.30→$128.32).

## Verdict: **SUFFICIENT**
All `critical` inputs present (A1+A2+A4 flow/positioning, B1 price history, A5+C5 edge & priced move) and completeness 100% ≥ 75%. → A4 may publish a **full plan, sizing per rubric**, no gap-driven size cut.

**Important distinction:** SUFFICIENT means the *evidence is complete enough to decide well* — it does **not** imply a high-conviction directional trade exists. The deep dive's own risk gates (fundamentals **VETO**, price-vs-flow **DIVERGENCE**, **long-gamma pin**, hard **Jul-23 earnings stop**) are conviction/sizing constraints resolved in A3/A4 — not information gaps. Expect the plan to remain defined-risk / small despite SUFFICIENT data.

## Sourcing plan
- No gaps to close. Optional pre-trade freshness refresh (run morning-of): `uw options-flow sweeps --symbol INTC --json`, `uw options-structure gex --symbol INTC --dte-max 45 --json`, `uw oi oi-by-strike --symbol INTC --json` — confirm the 5/5 sweep campaign and $120/$130 pins still hold before placing any spread.
