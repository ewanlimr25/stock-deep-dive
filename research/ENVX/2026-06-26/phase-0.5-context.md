# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** ENVX
**As-of date:** 2026-06-26
**Generated:** 2026-06-27T14:47:39Z
**Upstream phases cited:** phase-0-intake.md

## Summary

ENVX's options tape today is **genuinely unusual in *direction* but not in *volume*.**
By absolute dollars it sits outside the day's top-50 (that list is mega-cap/ETF
dominated — the #50 cutoff is +$3.06M net, ENVX is only +$442K net). But on an
*exact* universe percentile it is **95.8th on net-directional premium, 89.5th on
total premium, and 89.2nd on options-intensity-vs-stock-liquidity** — and **94.3rd
vs its own 54-session history** on net-directional premium. The catch: ENVX's option
volume today (18,437 contracts) is **0.94× its own 30-day average** — a normal-volume
day, not a surge. So the signal here is a sharp *call skew* (PCR 0.198, call premium
$1.82M vs put $0.34M) layered on ordinary participation, on a $5.95 name that is
**down -20.67% over the past month** and carries a **26% short float** (phase-0). Read
this as a real but *small-scale, counter-trend* directional tilt — calibrate
conviction to the skew, not to a breakout, and keep size modest.

## Universe ranking (vs ~4,589 optionable names today)

| Metric | CLI top-50 rank | Exact universe %ile `[DUCKDB]` |
|--------|-----------------|-------------------------------|
| Net-directional premium | **outside top-50** (cutoff +$3.06M; ENVX +$442K) | **95.8** |
| Total premium | outside top-50 | **89.5** |
| Options vol vs stock liquidity | outside top-50 | **89.2** |
| IV rank | outside top-50 | 54.7 (mid; iv_rank 42.5) |

Today's single-name directional leaders (ETFs set aside): TSLA +$70.3M, LULU +$68.0M,
LLY +$37.5M, NOW +$25.0M, META +$20.0M, ASTS +$15.1M, UBER +$11.4M. Leading ETF/index
flow: SPXW +$120M, **SMH +$77.9M (semis), IGV +$76.1M (software)**, QQQ +$33.5M.

## Sector read

Today's tape is led by **semiconductors (SMH) and software (IGV)** on the ETF side and
mega-cap tech/discretionary (TSLA, LULU, LLY, NOW, META) on the single-name side.
ENVX (silicon-anode **EV-battery / clean-tech**) is **not in a leadership cluster** —
its group is out-of-favour and the name itself is -20.67% on the month / -18.60% YTD.
A bullish-skewed tape on a lagging, falling name is a **counter-trend / contrarian
yellow flag** for phase-6 (macro) and phase-8b (debate) to resolve: is smart money
fading the decline, or is this short-dated call buying / hedging noise?

## Self-history (local screener parquet present; 54 sessions, gap-aware)

- `self_pctile_net_dir`: **94.3** `[CTX:self_pctile DUCKDB]` — today's net-directional
  premium is in the top ~6% of ENVX's own ≤54 available sessions.
- `self_pctile_net_bull` (bullish−bearish): **94.3**
- `self_pctile_total`: 84.9
- `sessions_in_window`: **54** (spans the 2026-03-27→04-27 gap — these are *available*
  sessions, not a contiguous calendar window; per phase-0 + duckdb-cuts §gap).
- Caveat: option volume 0.94× its 30-day average — the high percentile is a
  *directional* extreme, not a participation surge.

## Source

CLI screener ranks (`uw screener bullish-bearish / volume-vs-average / iv-rank`,
`uw insights deep-dive`) **+ DuckDB escape hatch §C** for exact universe & self-history
percentiles (local parquet `stock-screener-2026-06-26.parquet` present). "Outside
top-50" recorded on all four CLI metrics — not an error, just below the mega-cap-led
absolute cutoff. Percentiles tagged `[DUCKDB]`.

## Verdict for downstream — `[CTX:]` block

```
universe_pctile_total_prem:  89.5            # DUCKDB exact
universe_rank_net_dir:       outside top-50 by $ ; 95.8th percentile (DUCKDB)
sector_leadership:           BATTERY/CLEAN-TECH lagging (semis+software led the tape)
iv_rank:                     42.5            # insights_deep_dive
implied_move_pct:            2.42            # implied_move_perc 0.0242 → feeds phase-9 N4
self_pctile_net_dir:         94.3            # DUCKDB; N=54 sessions
unusual_verdict:             GENUINELY_UNUSUAL (direction) — VOLUME CAVEAT: opt vol 0.94x 30d avg, not a surge; small absolute scale
```

## Verdict for downstream phases

- **Bias from this phase:** context only — no directional bias set here.
- **Conviction:** n/a (context phase)
- **Three things later phases should remember:**
  1. The unusualness is a **call skew** (95.8th %ile net-direction, 94.3rd self-history,
     PCR 0.198), **not a volume surge** (0.94× 30d avg) — phase-1/2 confluence should
     credit direction, not breakout scale. Absolute net flow is small (+$442K).
  2. ENVX is **counter-trend**: -20.67% past month, lagging sector, 26% short float.
     Bullish flow into that = either contrarian accumulation OR short-dated hedging /
     squeeze positioning. Phase-8b must adjudicate.
  3. IV rank mid (42.5), implied move ~2.42% — modest expected move; feeds phase-9 (N4).
- **Open questions:** Is the call skew genuine accumulation (sweeps/repeat strikes, dark
  pool support — phases 1–2) or short-dated/0DTE noise (phase-0 flagged a 0DTE $2.5 call)?
  Does the 26% short float make this a squeeze setup rather than a fundamental call?
