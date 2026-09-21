# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** HOOD
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T14:03:50Z
**Upstream phases cited:** phase-0-intake.md

## Summary

HOOD is one of the most *liquid* option names in the universe (98.5th percentile
by total option premium, ~top 1.5% of ~6,171 names) — but as-of 2026-05-27 it is
having a **below-average, modestly-bullish, low-vol day for itself**. Its own
options volume is 0.67× its 30-day average, total option premium ($54.3M) sits at
only the 21.9th percentile of its own last 33 sessions, IV rank is low (23.2), and
net directional premium is a trivial **+$1.07M** (bullish $24.1M vs bearish $23.0M,
near-balanced). Technology broadly leads today's directional tape, but HOOD is not
among the leaders — it ranks 114th on net bullish flow behind index/ETFs and the
real leaders (META +$61.7M, TSLA +$54.8M, ASTS +$32.5M, IREN +$30.8M, APP +$29.1M).
**Verdict: BUSY_NAME_NORMAL_DAY** — big absolute liquidity, ordinary day. Phases 1–2
confluence is therefore capped at `+` (not `++`) per the scoring rubric.

## Key signals

- Total option premium $54.3M → **98.5th universe percentile** but **21.9th self
  percentile** [CTX:universe_pctile DUCKDB] — liquid name, light day for itself.
- Net directional premium **+$1.07M** (P/C 0.36), CLI rank **114th** on net bullish
  flow [CTX:universe_rank_net_dir]; 97.6th universe pctile is an artifact of the long
  zero/negative tail — the absolute figure is tiny vs leaders.
- Options volume **0.67× its own 30-day average** (199,180 vs 297,776) [CTX:vol_vs_avg]
  — a quiet tape day, not an unusual-volume event.
- IV rank **23.2** (23.0th universe pctile) [CTX:iv_rank] — low realized-vs-range; no
  vol premium being paid up. Implied move **3.29%** [CTX:implied_move_pct].
- Self-history net direction **62.5th percentile** of last 33 sessions
  [CTX:self_pctile DUCKDB] — modestly bullish for HOOD, nowhere near extreme.

## Detailed findings

### Universe ranking (cross-sectional, ~6,171 optionable names, 2026-05-27)

| Metric | HOOD value | Universe percentile | Read |
|--------|-----------|--------------------|------|
| Total option premium | $54.30M | 98.5 | Top 1.5% — very liquid |
| Net directional premium | +$1.07M | 97.6 | Misleading; absolute trivial |
| IV rank | 23.2 | 23.0 | Low — cheap vol |
| Options vol vs own 30d avg | 0.67× | n/a (CLI rank 2019) | Below average |

CLI net-bullish leaderboard (single names, ETFs noted): SPXW/SPY/SOXL/RUT/XSP
(index/ETF — set aside), then **META +$61.7M, TSLA +$54.8M, ASTS +$32.5M,
IREN +$30.8M, APP +$29.1M, AXTI +$25.3M, AAPL +$17.4M**. HOOD at +$1.07M is rank
**114th** — clearly outside the day's directional leaders.

> Note: the DuckDB §C recipe's `pctile_vol_vs_avg` returned 94.6, but it divides
> options *contracts* by average *stock-share* volume (avg30_volume = 25.1M shares) —
> a malformed cross-metric. The correct options-volume-vs-own-average is **0.67×**
> (CLI `volume-vs-average` and the self-history table both confirm). Disregard the
> 94.6 figure.

### Sector read

UW classifies HOOD as **Technology**, though it is functionally a fintech/brokerage.
Technology is well represented among today's bullish leaders (APP, AXTI, AAPL, ORCL,
AVGO, FSLR, POET, ADBE, COHR, DELL, KLAC, SMTC), so the **sector tape is in favour** —
but HOOD itself is *lagging within a leading sector*. That is a mild yellow flag:
the name is not riding its sector's bid. Phase-6 should resolve whether fintech /
brokerage names specifically (vs semis/AI within "Technology") are participating.

### Self-history (33 local sessions; non-contiguous — gap 2026-03-30→04-24)

Last 14 sessions show HOOD's net direction chops around zero (range −$10.0M on
2026-05-22 to +$14.9M on 2026-05-14); today's +$1.07M is unremarkable. Total premium
today ($54.3M) is below the recent median (May 14 ran $112M, May 11 $78.6M). Options
volume has been sub-1.0× its average on 12 of the last 14 sessions — HOOD's options
tape has been broadly quiet lately. Price has drifted **80.78 (2026-05-11) → 76.23
(2026-05-27)**, a ~6% fade over the window, on falling IV rank.

## Source

CLI (`uw screener` ×3, `uw insights deep-dive`) + DuckDB escape hatch (`lib/duckdb-cuts.md §C`)
for exact universe + self-history percentiles. Local snapshot present for 2026-05-27;
self-history N=33 sessions across a non-contiguous window (one ~21-session hole).
"Outside top-N" metrics: HOOD is outside the net-bullish top-50, outside the
volume-vs-average top-300 (ratio<1), and outside the high-IV-rank top-500.

## Tool calls (audit trail)

| Command | Result summary |
|---------|----------------|
| `uw insights deep-dive --symbol HOOD --date 2026-05-27 --json` | net_dir +$1.07M, P/C 0.36, IV rank 23.2, implied_move 3.29%, total prem $54.3M, DP $273.7M |
| `uw screener bullish-bearish --direction bullish --top-n 200 --date 2026-05-27 --json` | HOOD rank 114, net_flow +1,069,371 |
| `uw screener bullish-bearish --direction bearish --top-n 300 ...` | HOOD absent (net positive) |
| `uw screener volume-vs-average --min-volume-ratio 0 --top-n 8000 ...` | HOOD rank 2019, volume_ratio 0.67 |
| `uw screener iv-rank --mode high --top-n 500 ...` | HOOD absent (low IV rank) |
| DuckDB §C universe + self-history pctiles | total 98.5/self 21.9; net_dir 97.6/self 62.5; iv 23.0; N=33 |

## Tool errors

DuckDB recent-history query first failed on `close` (reserved word); re-run with
`"close"` quoted succeeded. No other errors.

## Verdict for downstream (the `[CTX:]` block — phases 1, 5, 9 read verbatim)

```
universe_pctile_total_prem:  98.5
universe_rank_net_dir:       114 (CLI, incl. ETFs); 97.6 universe pctile (artifact of zero-tail — absolute +$1.07M is trivial)
sector_leadership:           Technology is LEADING the tape, but HOOD is LAGGING within it (yellow flag for phase-6)
iv_rank:                     23.2
implied_move_pct:            3.29
self_pctile_net_dir:         62.5
self_pctile_total_prem:      21.9
unusual_verdict:             BUSY_NAME_NORMAL_DAY
```

- **Bias from this phase:** neutral (context only — no directional bias set here)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. **BUSY_NAME_NORMAL_DAY** — cap phases 1–2 confluence at `+` not `++`; do not
     mistake HOOD's top-1.5% absolute premium for an unusual signal.
  2. Net direction is **near-balanced and trivial** (+$1.07M); any directional thesis
     must come from *structure/positioning/dark-pool*, not from headline net flow.
  3. **Low IV rank (23) + below-average volume (0.67×)** — cheap optionality and a
     quiet tape; favors patience and defined-risk structures over chasing.
- **Open questions:** Is fintech/brokerage specifically participating in the
  Technology bid, or only semis/AI? (phase-6). Why is total premium light while
  dark-pool premium ($273.7M) is large? (phase-2).
