# Phase A1 — Critical-Information Gap Audit — ELF (2026-06-30)

Grades available evidence against `rubrics/gap-rubric.md`. Substrate = fresh deep dive `research/ELF/2026-06-30/` (age 0 days, full phase set) + live `chart_engine.py` (yfinance, 373 sessions).

## Checklist

### A. Directional evidence (the "why")
| # | Input | Status | Source / where |
|---|-------|--------|----------------|
| A1 | Options flow / sweeps | **HAVE** | `phase-1-flow.md` — $45 Jan-2028 **delta-0.85 LEAP**, bullish sweeps [FLOW:sweeps] |
| A2 | Dark-pool / block accumulation | **HAVE** | `phase-2-dark-pool.md` — DP clusters + 5-day institutional shelf $64–65 [DP:price_levels] |
| A3 | OI / positioning (walls, pins) | **HAVE** | `phase-3-positioning.md` — **25 consecutive OI-build days +127,955**; gamma walls $70 (+1.03M) / $75 (+681k) [HIST:oi-trend][OI] |
| A4 | Dealer structure (GEX/DEX/ZGL) | **HAVE** | `phase-4-structure.md` — POSITIVE/long-gamma, **ZGL $59.97**, max-pain $59–63 below spot [STRUCT:gex] |
| A5 | Historical signal win-rate (Kelly p) | **HAVE** | `phase-5-historical.md` — bullish_flow backtest **p=0.625, n=8**; but 90d net premium −$9.5M [HIST] |

### B. Price structure (the "where")
| # | Input | Status | Source / where |
|---|-------|--------|----------------|
| B1 | OHLCV history (≥150 sessions) | **HAVE** | `chart_engine.py` yfinance — 373 daily sessions, `available: true` |
| B2 | Support/resistance + swing pivots | **HAVE** | derived B1 → `chart.json` (A2); corroborated by DP/gamma levels |
| B3 | Trend / market structure | **HAVE** | `chart.json` ma_stack **mixed** (spot > sma20/50, < sma200 84.05); RSI 72.7 overbought |
| B4 | Chart patterns | **HAVE (capped medium)** | derived B1 → `chart.json patterns` (A2) |
| B5 | Fibonacci / measured-move | **HAVE** | derived B1 → `chart.json fibonacci` (A2) |
| B6 | ATR / volatility for stops | **HAVE** | `chart.json indicators.atr14` = 3.85 (5.49%) |

### C. Context (the "when / what breaks it")
| # | Input | Status | Source / where |
|---|-------|--------|----------------|
| C1 | Macro regime + sector rotation | **HAVE** | `phase-6-macro.md` — **TRANSITIONAL** (half-size), Consumer Defensive persistent INFLOW, hawkish Fed dots 3.8% [MACRO] |
| C2 | Event calendar | **HAVE** | June ISM/jobs (early Jul), June CPI (mid-Jul), haircare rollout (soft +), earnings ~Aug-5 [MACRO] |
| C3 | Fundamentals quality veto | **HAVE** | `phase-7b-fundamentals.md` — **CONFIRM** (0/3 axes contradict); P/E ~166x trough, net margin 1.6%, gross 70.7%, current ratio 2.35 [FUND] |
| C4 | Sentiment / crowd / short interest | **HAVE** | `phase-7c-sentiment.md` — **BALANCED**; SI 15.9%→12.7% (short-covering fuel, partly non-recurring) [SENT:short_float] |
| C5 | Implied / expected move | **HAVE** | ±3.52% / ±$2.61 to Jul-31; **VRP +0.081 → mild PREMIUM_SELLING**; IV rank 46.8 [CTX:implied_move] |
| C6 | Earnings date (expiry selection) | **HAVE (exact date soft)** | **~Aug-5** (UW screener, phase-0.5/6) + ELF's early-August Q1 fiscal cadence. `fz quote ELF` does **not** expose the earnings field; exact day (Aug-5 vs 6/7) is soft — but the **trade-relevant fact holds robustly: earnings is AFTER the Jul-31 expiry**, so the "expire pre-earnings" logic is safe. |

## Completeness
- HAVE = 17 / 17 → **completeness = 100%**. PARTIAL/MISSING = 0.

## Missing / gaps (none critical/important)
| Item | Severity | how_to_source |
|------|----------|---------------|
| Exact Q1 FY2027 earnings day (Aug-5 vs 6/7) | nice_to_have | ELF IR / earnings calendar; `finnhub_enrich.py --ticker ELF --date 2026-06-30` — confirm before placing; any early-Aug date is safely after the Jul-31 expiry |
| Leverage detail (debt/equity) + cash-flow statements | nice_to_have | paid-tier Finnhub `financials-reported`; proxied HAVE (current ratio 2.35, gross margin 70.7% intact) — no red flag |
| Live intraday tape / same-day dip-buy trigger timing | nice_to_have | `uw options-flow sweeps --symbol ELF --json` + `uw options-structure gex --symbol ELF --dte-max 45 --json` morning-of |

## Verdict: **SUFFICIENT**
All `critical` inputs present (A1+A2+A4 flow/positioning, B1 price history, A5+C5 edge & priced move) and completeness 100% ≥ 75%. → A4 may publish a **full plan, sizing per rubric**. No gap-driven size cut.

**Distinction:** unlike the prior two tickers, ELF's constraints are **not** a veto/negative-edge — the edge is real (positive Kelly, CONFIRM fundamentals, CONFLUENT bullish flow+chart). The constraints are **entry quality** (extended +34.9%/30d, overbought, into a long-gamma $75 cap) and **regime** (TRANSITIONAL → half-size). Those shape a **small dip-buy**, resolved in A3/A4, not an information gap.

## Sourcing plan (optional, pre-trade)
1. Confirm the exact earnings date via ELF IR (`~Aug-5`) — ensures Jul-31 structures stay pre-earnings.
2. `uw options-structure gex --symbol ELF --dte-max 45 --json` — re-confirm ZGL $59.97 and the $70/$75 gamma walls hold before buying a dip.
3. `uw options-flow sweeps --symbol ELF --json` — confirm the OI-build/LEAP thesis is still accreting (not flipping to distribution) morning-of.
