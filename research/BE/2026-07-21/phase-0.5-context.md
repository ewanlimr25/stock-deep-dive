# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** BE
**As-of date:** 2026-07-21
**Generated:** 2026-07-22T08:00:00Z
**Upstream phases cited:** phase-0-intake.md

## Summary

BE's flow today is **genuinely unusual on the directional axis, not on raw
turnover.** Net-directional premium sits in the **top 0.2% of the whole
optionable universe** (99.8th pctile) and, more strikingly, is the **single most
bullish net-directional day in BE's own 70-session history** (100th self-pctile).
Total premium is also 99.6th-pctile universe-wide (#11 net-bullish name on the
tape, ~#6 among single names, ahead of ORCL/ASML/FSLR). The one caveat: option
*volume* is only ~1.2× the 30-day average (75th pctile) — this is a
record-conviction *lean*, not a volume explosion. Context is set by an imminent
earnings print (**2026-07-28, 5 trading days out**) with IV rank **98.8** and a
~**10.6% implied move**. A loud divergence to resolve downstream: put/call
**volume** ratio is 2.05 (puts 2× calls) yet net *premium* is firmly bullish
(+$25.5M) — puts are being sold / calls bought into rich IV, not accumulated.

## Universe ranking (as-of 2026-07-21)

| Metric | BE value | Universe pctile / rank |
|--------|----------|------------------------|
| Net-directional premium (`net_flow`) | **+$25,457,620** | **99.8** pctile · rank **#11** overall (~#6 single-name) `[CTX:universe_pctile DUCKDB]` |
| Total option premium | $249.6M (call 127.2M + put 122.4M) | **99.6** pctile |
| IV rank | **98.78** | **96.3** pctile |
| Volume vs 30-day avg | **1.2×** | 75.1 pctile — **outside** the vol-vs-avg ≥2 top-60 |

Bullish-tape leaders today (ETFs aside): **MU $289.9M, SNDK $198.2M, NBIS
$55.5M, AMD $40.3M, TSM $28.4M, NVDA $26.0M**, then **BE $25.5M**, ORCL $25.1M.
`[CTX:screener_bullish_bearish]`

## Sector read

Today's directional tape is **semiconductor/AI-infrastructure led** (MU, SNDK,
AMD, TSM, NVDA, ASML, AMAT, LRCX all in the top 15). BE's own sector is
**Industrials** (fuel-cell / distributed-power) — *not* the leading sector, but
BE trades as the **AI-datacenter-power** proxy and sits in the flow cluster right
next to **FSLR #18 (solar)**. Read: BE is riding the AI-power-demand narrative
that is pulling the semi tape, rather than an Industrials-sector bid. Phase-6
should check whether the power/energy-infra sub-theme is confirming or whether BE
is a lone straggler on a semis day (mild yellow flag — name strong, home sector
not leading).

## Self-history (parquet present — 70 sessions, gap-adjusted)

- `self_pctile_net_dir`: **100.0** — today is BE's most bullish net-directional
  day across all 70 available sessions `[CTX:self_pctile DUCKDB]`
- `self_pctile_total`: **78.3** — total premium high but not a record for the name
- `sessions_in_window`: **70** (spans the 2026-03-27→04-27 data gap; N is
  available sessions, not a contiguous calendar window — per phase-0)

Reconciliation: record directional lean (100th) on merely-78th total premium and
75th volume ⇒ the *same-ish* dollars as other busy days but pointed far more
one-sidedly bullish than BE has ever leaned. That is the signal.

## Source

CLI (`uw screener bullish-bearish` ×2, `uw screener volume-vs-average`, `uw
insights deep-dive`) **+ DuckDB §C** for exact universe & self-history
percentiles (snapshot present for 2026-07-21). BE was outside the
volume-vs-average ≥2 top-60 (recorded, not an error).

## Verdict for downstream

```
[CTX:]
universe_pctile_total_prem:  99.6
universe_rank_net_dir:       11        # ~#6 among single names (ETFs aside)
sector_leadership:           INDUSTRIALS lagging (semis/AI-infra lead); BE trades as AI-power proxy
iv_rank:                     98.78
implied_move_pct:            10.6%      # earnings 2026-07-28, 5 trading days out
self_pctile_net_dir:         100.0
unusual_verdict:             GENUINELY_UNUSUAL
```

**Rationale for GENUINELY_UNUSUAL (not the strict all-three test):** net-dir is
99.8 universe + 100 self (both maxed), which dominates. The lone failing leg is
vol-vs-avg (1.2× < 2×), so the unusualness lives in the *directional conviction*,
not the raw volume. Downstream note: because turnover is only mildly elevated,
phases 1–2 should verify the directional premium is real institutional
positioning (sweeps, block, dark-pool confirmation) and not a handful of large
prints inflating a thin tape — if it fails that check, treat as BUSY_NAME and cap
phase-1/2 confluence at `+`.

## Verdict for downstream phases

- **Bias from this phase:** context only — no directional bias set (but flags a
  record-bullish directional lean into earnings for phases 1/5/9 to weigh)
- **Conviction:** n/a (context)
- **Three things later phases should remember:**
  1. **Earnings 2026-07-28 (5 trading days out)** dominates everything — IV rank
     98.8, ~10.6% implied move. Any plan is an earnings-window plan.
  2. Record net-bullish directional lean (100th self-pctile, 99.8 universe) on
     only 1.2× volume — conviction is in the *lean*, verify it's institutional.
  3. **Put/call volume 2.05 vs net premium bullish** — reconcile in phase 1
     (puts sold vs bought?) and phase 3 (put-wall OI). LEAP 310C OI build
     (+4,790) hints at directional bullish call accumulation.
- **Open questions:** Is the bullish net premium call-buying or put-selling? Is
  the heavy near-dated put volume (110P/165P/170P) directional bearish or
  IV-selling/hedging? Resolved in phases 1–4.
