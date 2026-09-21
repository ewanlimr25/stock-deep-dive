# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** CRM
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T15:52:00-04:00
**Upstream:** phase-0-intake.md (as-of validated; local parquet present for 2026-06-05)

## Summary

CRM's options tape on 2026-06-05 is **big in absolute terms but unremarkable in
every relative sense**. The name sits at the 98.0th universe percentile on total
premium — it is always one of the busiest tickers — yet it is **outside the
top-50 on net bullish AND net bearish premium**, outside the top-50 on
volume-vs-average (≥2x screen), and in neither IV-rank tail. Its own-name net
direction is barely positive (bullish $23.02M vs bearish $21.74M → derived net
+$1.28M), while the exact universe percentile on net call−put premium is just
**15.4** — mildly bearish-skewed cross-sectionally. Self-history says today is a
*below-median* day for CRM: total premium at the **33.3rd** self-percentile and
net direction at the 61.5th (N=40 sessions). Verdict: **BUSY_NAME_NORMAL_DAY** —
phases 1–2 confluence is capped at `+` per `rubrics/confluence-scoring.md`.

## Universe ranking

- **Net bullish premium (top-50):** CRM absent. Leaders: SPX (+$2.398B), NDXP
  (+$73.8M), IWM (+$55.2M), STM (+$53.4M), NDX (+$43.5M) — index-dominated;
  STM is the lead single name. `[CTX: screener bullish-bearish .results[]]`
- **Net bearish premium (top-50):** CRM absent. Leaders: SPXW (−$2.090B), QQQ
  (−$116.9M), SNDK (−$114.3M), SOXL (−$85.6M), NVDA (−$81.4M) — semis are the
  sold sector (SNDK/SOXL/NVDA all top-5 bearish).
- **Volume vs 30-day average (≥2x, top-50):** CRM absent (leaders are small-caps:
  FCPT, IMCR, QVCAQ…). Exact percentile below says 91.6 — elevated but < 2x.
- **IV-rank screens:** CRM in neither high (MU/AIS/MRVL lead) nor low tail.

## Sector read

Technology is **two-sided but net-bearish-skewed** today: 13 of the top-25
bearish-flow names are Technology vs 7 of the top-25 bullish (nulls = index/ETF
products). The day's clearest single-name story is semis distribution
(SNDK/SOXL/NVDA top-5 bearish) with STM the lone semi bought. CRM's sector is
**mid-pack-to-lagging** — no sector tailwind for a long, no panic either.
Hands phase-6 a head start: directional tape is index-dominated and
tech-internals are soft.

## Self-history (DuckDB §C, N=40 sessions, gap-aware)

`[CTX:universe_pctile DUCKDB]` exact cuts on stock-screener-2026-06-05.parquet:

| Metric | Universe pctile | Self pctile (N=40) |
|---|---|---|
| Total premium | **98.0** | **33.3** |
| Net directional (net_call−net_put prem) | **15.4** | **61.5** |
| IV rank | 73.5 | — |
| Volume vs 30d avg | 91.6 | — |

Today is a below-median-activity, direction-flat day *for CRM itself*. Note the
self-history window spans the 2026-03-28→04-26 local gap; N=40 available
sessions, not a contiguous calendar window. `[CTX:self_pctile DUCKDB]`

## Source

CLI (`uw screener` ×4, `uw insights deep-dive .uw_screener`) **+ DuckDB §C**
(exact universe + self percentiles). Outside-top-N metrics: net bullish, net
bearish, volume-vs-average (≥2x), iv-rank high, iv-rank low — all recorded above.
`net_flow` for CRM derived as `bullish_premium − bearish_premium` from the
deep-dive `uw_screener` block (deep-dive has no `net_flow` field).

## Verdict for downstream

```
universe_pctile_total_prem:  98.0            # DUCKDB exact
universe_rank_net_dir:       outside top-50 (both directions); exact pctile 15.4 [DUCKDB]
sector_leadership:           Technology is lagging today (13/25 of bearish leaders vs 7/25 bullish; semis sold)
iv_rank:                     60.0            # insights deep-dive .uw_screener.iv_rank = 59.9885
implied_move_pct:            0.56%           # .uw_screener.implied_move_perc = 0.00560 ($1.04 on $185.66)
self_pctile_net_dir:         61.5            # DUCKDB, N=40 sessions (gap-aware)
unusual_verdict:  BUSY_NAME_NORMAL_DAY
```

**Downstream instruction:** phases 1–2 confluence contributions are capped at
`+` (not `++`). Big prints on CRM must clear a higher bar — the name always
prints big numbers. Next earnings 2026-09-02 (far; no event-vol crutch).

## Tool calls

| Command | jq path | Status |
|---|---|---|
| `uw screener bullish-bearish --direction bullish --top-n 50 --date 2026-06-05 --json` | `.results[] .ticker/.net_flow` | ok |
| `uw screener bullish-bearish --direction bearish --top-n 50 --date 2026-06-05 --json` | `.results[] .ticker/.net_flow` | ok |
| `uw screener volume-vs-average --min-volume-ratio 2 --top-n 50 --date 2026-06-05 --json` | `.results[]` | ok (CRM absent) |
| `uw screener iv-rank --mode high/low --top-n 50 --date 2026-06-05 --json` | `.results[]` | ok (CRM absent both) |
| `uw insights deep-dive --symbol CRM --date 2026-06-05 --json` | `.uw_screener` | ok |
| DuckDB §C universe + self-history percentiles | (queries in `lib/duckdb-cuts.md §C`) | ok |
| `uw screener bullish-bearish … --top-n 25` ×2 (sector mix) | `.results[].sector` group_by | ok |

## Tool errors

None.
