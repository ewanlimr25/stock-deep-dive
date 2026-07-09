# Gap Rubric — what a good trade plan needs (goal #1 / #2)

Phase A1 grades the available evidence against this checklist, then writes a
`gap_audit` block: what we **have**, what is **missing**, the **severity** of
each gap, and **how to source it**. A plan is only as good as its weakest
critical input — surface the gaps, don't paper over them.

## The required-input checklist

Score each line `HAVE` / `PARTIAL` / `MISSING`. `completeness = HAVE/total * 100`.

### A. Directional evidence (the "why")
| # | Input | Primary source | If missing, how to source |
|---|-------|----------------|---------------------------|
| A1 | Options flow / sweeps (today's tape) | `phase-1-flow.md` · `uw options-flow sweeps` | run `/stock-deep-dive` or live `uw options-flow` |
| A2 | Dark-pool / block accumulation | `phase-2-dark-pool.md` · `uw dark-pool` | `uw dark-pool largest / block-stratified` |
| A3 | OI / positioning (walls, pins) | `phase-3-positioning.md` · `uw oi oi-by-strike` | `uw oi oi-by-strike / pin-risk` |
| A4 | Dealer structure (GEX/DEX/ZGL) | `phase-4-structure.md` · `uw options-structure gex/dex` | `uw options-structure gex --dte-max 45` |
| A5 | Historical signal win-rate (the Kelly p) | `phase-5-historical.md` · `uw historical signal-backtest` | `uw historical signal-backtest` for the firing class |

### B. Price structure (the "where") — the NEW layer
| # | Input | Primary source | If missing, how to source |
|---|-------|----------------|---------------------------|
| B1 | OHLCV history (≥150 sessions ideal) | `chart_engine.py` (yfinance) | `lib/chart_engine.py`; fallback UW screener parquet |
| B2 | Support/resistance + swing pivots | `chart.json` `support_resistance` | derived from B1 |
| B3 | Trend / market structure (HH-HL etc.) | `chart.json` `trend` | derived from B1 |
| B4 | Chart patterns (flag/H&S/triangle/…) | `chart.json` `patterns` | derived from B1 (low-confidence → analyst confirm) |
| B5 | Fibonacci / measured-move targets | `chart.json` `fibonacci` | derived from B1 |
| B6 | ATR / volatility for stop placement | `chart.json` `indicators.atr14` | derived from B1 |

### C. Context (the "when / what could break it")
| # | Input | Primary source | If missing, how to source |
|---|-------|----------------|---------------------------|
| C1 | Macro regime + sector rotation | `phase-6-macro.md` · `uw risk market-regime` | `fred_macro.py`, `uw risk market-regime` |
| C2 | Event calendar (earnings/FOMC/CPI/OPEX) | `phase-6` + `finnhub_enrich.py` | `finnhub_enrich.py`, WebSearch, `uw oi opex-concentration` |
| C3 | Fundamentals quality veto | `phase-7b-fundamentals.md` | `finnhub_enrich.py --ticker T --date D` |
| C4 | Sentiment / crowd / short interest | `phase-7c-sentiment.md` · `fz quote` | `fz_enrich.py`, `fz quote` |
| C5 | Implied / expected move (for option width) | `phase-0.5`/`phase-7` `uw_screener.implied_move` | screener parquet `implied_move_perc` |
| C6 | Earnings date (for expiry selection) | `finnhub_enrich.py` / screener `next_earnings_date` | screener parquet `next_earnings_date` |

## Severity rules

- **critical** — a directional plan cannot be responsibly written without it.
  Default-critical: **A1+A2 or A4** (some flow/positioning read), **B1** (price
  history for levels), **A5 or C5** (a calibrated edge or at least the priced move).
- **important** — materially changes sizing or structure: **C1, C2, C3, C6**.
- **nice_to_have** — sharpens but doesn't gate: **B4, B5, C4**, intraday tape.

## Verdict

| Verdict | Condition | What phase A4 may publish |
|---------|-----------|---------------------------|
| `SUFFICIENT` | all `critical` present, completeness ≥ 75% | full plan, sizing per rubric |
| `USABLE_WITH_GAPS` | all `critical` present, 50–75% | plan with **explicit caveats**; cap size one step |
| `INSUFFICIENT` | any `critical` missing | **watch-only**; list exactly what to source first, size 0% |

The gap audit is itself a deliverable (goal #1). When a gap is `critical` and
unsourced, A4 must NOT fabricate the missing input — it sizes to 0 and names the
exact command/feed that would unblock the plan (goal #2).
