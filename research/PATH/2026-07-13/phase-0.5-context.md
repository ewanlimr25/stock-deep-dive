# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** PATH
**As-of date:** 2026-07-13
**Generated:** 2026-07-13T20:14:00-04:00
**Upstream phases cited:** phase-0-intake.md

## Summary

PATH's **options** tape is not genuinely unusual today. It sits in the top decile
of the optionable universe on *absolute* total premium (89.4th pctile) — a
normally well-traded name — but that premium is **quiet for PATH itself**
(17.5th self-percentile of total premium over its own last 64 sessions). Net
directional premium is mildly **bearish** both cross-sectionally (8.4th pctile of
net_dir) and for the name (36.5th self-pctile), and volume-vs-average is only
moderately elevated (68.6th pctile). PATH does **not** appear in the top-60 of
either the bullish or bearish net-premium leaderboards. Read: **BUSY_NAME_NORMAL_DAY
with a quiet-options lean** — the options market is not the story here. The
flagged 2026-07-09 afterhours darkpool print (phase 2) is the genuine anomaly,
and phases 1–2 confluence is therefore capped at `+` (not `++`) per the scoring rubric.

## Universe ranking (as-of 2026-07-13)

- **Net bullish premium:** PATH **outside top-60**. Leaders (single names, ETFs
  aside): AMZN (net +$20.8M), SLS (+$19.7M), DRAM (+$18.0M), GEV (+$15.2M). Index
  ETFs SPX/NDX/RUT dominate the raw list.
- **Net bearish premium:** PATH **outside top-60** — its net-directional magnitude
  (bullish $771k − bearish $938k = **−$167k**) is tiny in absolute terms.
- **Volume-vs-average (≥2×):** PATH **outside top-80**.
- **Exact universe percentiles [CTX:universe_pctile DUCKDB]:** total_prem **89.4**,
  net_dir **8.4** (net-bearish tilt), iv_rank **38.5**, vol_vs_avg **68.6**.

## Sector read

PATH = application software (enterprise automation / RPA / agentic-AI). Today's
directional tape is led by mega-cap tech (AMZN), power/utilities (GEV), and a few
small-cap movers (SLS, DRAM) — **not a broad software-led session**. Software is
**mid-pack, not in favour**. A name showing a net-bearish options tilt while its
sector is not leading is a mild yellow flag for phase 6 to resolve, but the
magnitudes are too small to weight heavily.

## Self-history (64 sessions, gap-aware) [CTX:self_pctile DUCKDB]

- **self_pctile_net_dir: 36.5** — today is modestly more bearish than PATH's median session.
- **self_pctile_total: 17.5** — total option premium is **low** for PATH; a quiet options day.
- **sessions_in_window: 64** (spans the known 2026-03-28→04-24 gap; N is available sessions, not calendar days).

## Source

CLI screener rankings (`uw screener bullish-bearish` / `volume-vs-average`) +
`uw insights deep-dive` **+ DuckDB §C** exact percentiles (local snapshot present
for 2026-07-13). "Outside top-N" recorded for all three leaderboards.

## Verdict for downstream

```
universe_pctile_total_prem:  89.4
universe_rank_net_dir:       outside top-60 both lists (net_dir pctile 8.4, net-bearish tilt)
sector_leadership:           SOFTWARE lagging / mid-pack today
iv_rank:                     40.4
implied_move_pct:            5.3
self_pctile_net_dir:         36.5
unusual_verdict:  BUSY_NAME_NORMAL_DAY   # quiet-options lean; darkpool is the real anomaly
```

**Three things later phases should remember:**
1. Options flow is *not* the driver today — it's quiet for the name and net-bearish-tilted; don't let raw premium be mistaken for a signal (confluence cap `+`).
2. The darkpool print (2026-07-09 AH, flagged #4-largest-ever) is the anomaly to characterize — phase 2 carries the burden of proof.
3. IV rank ~40 / implied move 5.3% — mid vol, next earnings 2026-09-03 (well outside a near-dated horizon).

**Open questions:** Is the net-bearish options tilt hedging, or genuine directional
selling? (phase 1). Was the 07-09 darkpool print accumulation or distribution? (phase 2).
