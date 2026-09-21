# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** FSLR · **As-of:** 2026-07-20 · **Version:** v1 · **Generated:** 2026-07-20
**Cites:** phase-0-intake.md (as-of, local parquet present → DuckDB percentiles used)

## Summary

FSLR is a **busy, high-attention name having a directionally mild, vol-driven
day** — not a genuine size breakout. Total option premium ($29.8M) sits in the
**98.7th universe percentile** (6,275 names), confirming it is one of the most
actively traded single names on the tape. But the "unusual" is almost entirely
an **earnings-driven IV ramp** (IV rank **99.1**, 97.2nd universe pctile;
earnings **2026-07-30**, 10 sessions out), *not* directional conviction:
today's option volume is **below FSLR's own 30-day average** (vol-vs-avg
**0.69×**, fails the ≥2× unusual-volume bar) and total premium is only the
**63.8th self-percentile**. Net directional flow is **−$3.80M (net bearish)** —
the 15.5th self-percentile (a more-bearish-than-usual day for FSLR) and the
0.7th universe percentile on signed net-direction, though the magnitude is
modest next to index/mega-cap hedging. Compounding the caution: FSLR's sector
(**Technology**) is the **single most net-bearish sector on the tape today**
(−$133.9M), so the name is leaning bearish *inside* the most-sold sector — a
yellow flag for phase-6 to resolve, not a clean directional signal.

## Universe ranking (as-of 2026-07-20)

- **Net-bearish premium rank: #45** (net −$3.80M) — inside the bearish top-60 but
  far below the leaders. **Outside** the bullish top-60. **Outside** the
  vol-vs-avg top-80 (≥2×).
- **Total-premium universe percentile: 98.7** (very active name).
- **Net-direction universe percentile: 0.7** (signed; near the bearish extreme,
  modest magnitude).
- **IV-rank universe percentile: 97.2** (earnings-vol driven).
- Net-bearish single-name leaders today: TSLA (−$45.9M), NVDA (−$45.1M),
  AAPL (−$30.9M), INTC (−$28.6M), META (−$19.7M) — index ETFs (SPY −$125M,
  QQQ −$47M) set aside. Bullish tape led by index/semis complex: SPX, SPXW,
  **SMH (+$63.3M)**, MRVL (+$34.0M), MSFT (+$15.7M).

## Sector read

FSLR sector = **Technology**, which is **LAGGING hard** — the most net-bearish
sector today at **−$133.9M** (n=568). Bid sectors are defensives/cyclical-value:
Utilities (+$9.5M), Energy (+$5.8M), Consumer Defensive (+$2.5M). This is a
risk-off / de-grossing tape in tech. FSLR bearish-leaning *within* a sold sector
= confirmation of the caution, **not** a contrarian long setup yet. (Note the
split: SMH/semis were bought even as the broad Tech aggregate was sold — solar
is not semis; phase-6 to reconcile.)

## Self-history (post-gap block, 58 sessions 2026-04-27 → 2026-07-20)

| Metric | Today | Self-pctile | Read |
|--------|-------|-------------|------|
| Net-directional prem | −$3.80M | **15.5** | more bearish than usual for FSLR |
| Total premium | $29.8M | 63.8 | moderately elevated, not extreme |
| IV rank | 99.1 | **91.4** | near its own recent top (earnings run-up) |
| Put/call (prem-wt) | 0.418 | 22.4 | call-heavy vs its own history |
| Vol-vs-avg | 0.69× | 41.4 | below-average tape |

Trend: net-direction has drifted steadily negative over the last four sessions
(−1.74 → −2.01 → −1.29 → **−3.80M**) while IV rank ramped (83 → 99) — a bearish
directional drift layered on an earnings-vol bid.

## Source

CLI (`uw screener` × 3, `uw insights deep-dive`) **+ DuckDB** (`lib/duckdb-cuts.md`
§C-style exact universe + 58-session self-history percentiles from the local
`stock-screener-2026-07-20.parquet`). "Outside top-N" recorded on bullish-net and
vol-vs-avg. Sector field is null in CLI screener rows (known-broken) → sector taken
from the parquet's `sector` column.

## Verdict for downstream

```
[CTX:]
universe_pctile_total_prem:  98.7
universe_rank_net_dir:       #45 net-bearish (outside bullish top-60; outside vva top-80)
sector_leadership:           Technology is LAGGING (most net-bearish sector, -$133.9M)
iv_rank:                     99.1
implied_move_pct:            5.31%
self_pctile_net_dir:         15.5   (bearish tilt vs own history)
self_pctile_total_prem:      63.8
unusual_verdict:             BUSY_NAME_NORMAL_DAY
```

**Downstream instruction:** per `rubrics/confluence-scoring.md`, because the
verdict is BUSY_NAME_NORMAL_DAY, **phases 1–2 flow/DP confluence is capped at `+`
(not `++`).** The genuinely elevated axis is **IV rank into earnings**, not size or
directional conviction — treat this as a **pre-earnings vol + mild-bearish-drift**
context, and let phases 1–8 (plus the 7c positioning gate and 8b debate) set the
actual bias. Sector-vs-name tension (bearish name in the most-sold sector, yet
semis bid) is handed to phase-6.
