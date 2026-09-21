# Phase A1 — Critical-Information Gap Audit

Evidence graded against `rubrics/gap-rubric.md`. Substrate = same-day deep dive
`research/PATH/2026-07-13/` (age 0 trading days) + chart engine (yfinance, 373 sessions).

## Checklist

### A. Directional evidence (the "why")

| # | Input | Status | Source / where |
|---|-------|--------|----------------|
| A1 | Options flow / sweeps | **HAVE** | `research/PATH/2026-07-13/phase-1-flow.md` (118 ln); decision.json [FLOW] citations |
| A2 | Dark-pool / block accumulation | **HAVE** | `phase-2-dark-pool.md`; 07-09 mega block 54.6M sh/$644M buy_ratio 1.000 [DP:block_stratified]; $678.8M shelf @ $11.80 [DP:price_levels] |
| A3 | OI / positioning (walls, pins) | **HAVE** | `phase-3-positioning.md`; largest pin $11.00, put wall $10, call wall/cap $13 |
| A4 | Dealer structure (GEX/DEX/ZGL) | **HAVE** | `phase-4-structure.md`; gamma wall $13, ZGL $5.70, book long-gamma [STRUCT:gex] |
| A5 | Historical signal win-rate (Kelly p) | **PARTIAL** | `phase-5-historical.md`: `signal-backtest --signal-type dark_pool_accumulation` returned `total_signals: 0` on both mandated runs → `win_rate_source = null`, `win_rate_n = 0`. Sizing falls back to conviction bin (0.55). IV %ile 44.4 and VRP +0.084 ARE present. |

### B. Price structure (the "where")

| # | Input | Status | Source / where |
|---|-------|--------|----------------|
| B1 | OHLCV history (≥150 sessions) | **HAVE** | chart engine `available: true`, yfinance, **373 sessions** |
| B2 | Support/resistance + pivots | **HAVE** | probe JSON `support_resistance` (8 levels) + `recent_pivots` |
| B3 | Trend / market structure | **HAVE** | probe JSON `trend` |
| B4 | Chart patterns | **HAVE** | probe JSON `patterns` (all 6 detectors ran; result: none detected — the analysis exists, the null result is itself information) |
| B5 | Fibonacci / measured moves | **HAVE** | probe JSON `fibonacci` |
| B6 | ATR for stop placement | **HAVE** | probe JSON `indicators.atr14 = 0.65` |

### C. Context (the "when / what breaks it")

| # | Input | Status | Source / where |
|---|-------|--------|----------------|
| C1 | Macro regime + sector rotation | **HAVE** | `phase-6-macro.md`; TRANSITIONAL regime, breadth 33.8%, tech net-inflow score 1, Fed easing DFF 3.62% |
| C2 | Event calendar | **HAVE** | decision.json catalysts: CPI ~2026-07-15, FOMC ~2026-07-29, earnings 2026-09-03. (July monthly OPEX 2026-07-17 derivable from calendar — A3 adds it.) |
| C3 | Fundamentals quality veto | **HAVE** | `phase-7b-fundamentals.md`; gate **CAUTION**, insiders net sellers (MSPR −100 Jul-2026; −9.6M sh Mar-2026) |
| C4 | Sentiment / crowd / short interest | **HAVE** | `phase-7c-sentiment.md`; SI 28–32% float, ~5 DTC, crowd_state **CROWDED_SHORT**, consensus HOLD / UBS PT $12 |
| C5 | Implied / expected move | **HAVE** | decision.json `expected_move` front-expiry ±5.3% ($0.63) [CTX:implied_move]; IV rank 40.4 |
| C6 | Earnings date | **HAVE** | 2026-09-03 (outside 1–4w horizon; Aug-21 structures avoid it) |

## Completeness

**HAVE 16 / 17 = 94%** (A5 PARTIAL). All default-critical inputs present:
A1+A2 ✓, A4 ✓, B1 ✓, and the A5-or-C5 pair is satisfied via C5.

## missing[]

| Item | Severity | how_to_source |
|------|----------|---------------|
| A5 empirical win-rate for the firing signal class (dark-pool accumulation) | **important** | `uw historical signal-backtest --signal-type dark_pool_accumulation --lookback-days 5` — returned 0 signals twice on 2026-07-13; no history exists for this class yet. Until it accrues, size from the conviction bin (already done upstream: p=0.55, quarter-Kelly) and do NOT size above starter. Re-run at next deep dive. |
| 07-09 block attribution (offering / index cross / 13D vs fresh accumulation) | **nice_to_have** (but it is the thesis's #1 named risk) | SEC EDGAR check for 13D/13G/S-3/424B filings on UiPath after 2026-07-09 (WebSearch "UiPath 13D OR offering July 2026"); `uw dark-pool block-stratified` daily to confirm large-tier buy_ratio holds > 0.55 |
| Intraday tape freshness at execution time | nice_to_have | `uw options-flow sweeps --symbol PATH` + `uw dark-pool largest --symbol PATH` on the morning of entry |

## Verdict

**`SUFFICIENT`** — every critical input present, completeness 94% ≥ 75%. Full plan
permitted; sizing per rubric. One honesty note carried to A3/A4: the Kelly p is a
conviction-bin fallback (no empirical base rate), so conviction must not be
promoted above upstream's 0.55 on flow evidence alone.
