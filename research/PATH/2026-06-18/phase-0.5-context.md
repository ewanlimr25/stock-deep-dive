# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** PATH (UiPath Inc.)
**As-of date:** 2026-06-18
**Generated:** 2026-06-20T12:57:40Z
**Upstream phases cited:** phase-0-intake.md

## Summary

PATH's options tape on 2026-06-18 is **a busy name having a normal day**, not a
genuinely unusual event. Cross-sectionally it is an active options name — top-decile
on total premium (89.4th universe pctile) and ~80th pctile on net-directional
premium — but it is **outside the top-50 leaders** on every screener metric
(bullish, bearish, vol-vs-avg, IV-rank-high), and on its **own 49-session history**
this is a *below-median* total-premium day (33.3rd self-pctile) with only mid
net-direction (60.4th self-pctile) and option volume just 66.5th pctile vs its own
average (i.e. < 2× — it failed the min-ratio-2 screen). Net directional premium is
essentially flat (bullish $1.00M vs bearish $0.98M = +$17.8k). Verdict:
**BUSY_NAME_NORMAL_DAY** → phases 1–2 confluence capped at `+` (not `++`).

## Universe ranking (single names, ETFs set aside)

- **Net bullish premium:** PATH **outside top-50**. Leaders: MU (+$522M), NDX,
  SNDK (+$110M), IBIT, SMH, INTC (+$92M), MRVL, SPY — the bullish tape is led by
  **semiconductors**. [CTX:screener_bullish_bearish]
- **Net bearish premium:** PATH **outside top-50**. [CTX:screener_bullish_bearish]
- **Volume-vs-average (min ratio 2×):** PATH **outside top-50** → today's option
  volume is < 2× its 30-day average. [CTX:screener_volume_vs_average]
- **IV-rank (high):** PATH **outside top-50** → not an elevated-IV name today.
  [CTX:screener_iv_rank]

## Sector read

Technology dominates today's bullish tape (24 of 50 single names), **but the
leadership is semiconductors / hardware** (MU, SNDK, INTC, MRVL, SMH). PATH sits in
the broad Technology bucket as an **AI-automation / software** name and is **not
participating** in the semis-led move. Net for PATH: broad sector in favour, but
PATH's software subsegment is mid-pack/lagging. Hands phase-6 a head start: the
risk-on bid is in semis, not enterprise software.

## Self-history (DuckDB §C — local snapshot present, N = 49 sessions, gap-aware)

| Metric | Today's self-pctile |
|--------|---------------------|
| net-directional premium (net_call − net_put) | 60.4 [CTX:self_pctile DUCKDB] |
| bullish − bearish premium | 60.4 [CTX:self_pctile DUCKDB] |
| **total premium (call+put)** | **33.3** (below own median) [CTX:self_pctile DUCKDB] |

N=49 available sessions (window spans the 2026-03-30→04-24 data hole — not a
contiguous calendar window; see phase-0 gap flag).

## Exact universe percentiles (DuckDB §C, ~optionable universe today)

| Metric | Universe pctile |
|--------|-----------------|
| total premium | 89.4 [CTX:universe_pctile DUCKDB] |
| net-directional premium | 80.7 [CTX:universe_pctile DUCKDB] |
| bullish − bearish premium | 80.7 [CTX:universe_pctile DUCKDB] |
| IV rank | 47.0 [CTX:universe_pctile DUCKDB] |
| volume vs average | 66.5 [CTX:universe_pctile DUCKDB] |

## Source

CLI (`uw screener` ×4 + `uw insights deep-dive`) **+ DuckDB §C** (exact universe &
self-history percentiles; local snapshot present for 2026-06-18). "Outside top-50"
recorded on all four screener metrics.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq`/SQL path | Rows used |
|------------------|------------------------------|-----------|
| `uw screener bullish-bearish --direction bullish --top-n 50 --date 2026-06-18` | PATH not in results → outside top-50; leaders MU $522M ← `.results[].net_flow` | top-50 |
| `uw screener bullish-bearish --direction bearish --top-n 50 --date 2026-06-18` | PATH outside top-50 | top-50 |
| `uw screener volume-vs-average --min-volume-ratio 2 --top-n 50 --date 2026-06-18` | PATH outside top-50 (< 2×) | top-50 |
| `uw screener iv-rank --mode high --top-n 50 --date 2026-06-18` | PATH outside top-50 | top-50 |
| `uw insights deep-dive --symbol PATH --date 2026-06-18` | bull=$1,002,311 bear=$984,512 call_prem=$1.87M put_prem=$0.67M pcr=0.335 iv_rank=34.55 implied_move_perc=0.0206 ← `.uw_screener` | 1 |
| DuckDB §C universe + self-history percentile | see tables above | universe + 49 self-sessions |

## Tool errors

_none_

## DATA NOTE / CORRECTION

_none — first reads stood._

## Verdict for downstream — `[CTX:]` block

```
universe_pctile_total_prem:  89.4
universe_rank_net_dir:       outside top-50 (universe pctile 80.7)
sector_leadership:           TECHNOLOGY leading BUT via semis; PATH (software) lagging/mid-pack
iv_rank:                     34.55
implied_move_pct:            2.06%
self_pctile_net_dir:         60.4
unusual_verdict:             BUSY_NAME_NORMAL_DAY
```

- **Bias from this phase:** neutral (context only — sets no directional bias)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. **BUSY_NAME_NORMAL_DAY** — cap phases 1–2 confluence at `+`. Net directional
     flow is flat (+$17.8k); don't read big absolute call premium as a directional signal.
  2. PATH is **not** in today's directional leaders; the risk-on bid is in
     semiconductors, not enterprise software — phase-6 should weigh sector rotation.
  3. On its own history this is a **below-median total-premium day** (33rd self-pctile)
     — tradeability/conviction should stay modest absent a strong single-print case.
- **Open questions:** With short float 31.78% (phase-0) and flat net flow, is anyone
  positioning for a squeeze or a breakdown? Resolve in phases 1–4 + the 7c gate.
