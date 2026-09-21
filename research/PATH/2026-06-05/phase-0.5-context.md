# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** PATH
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T10:05:00-04:00
**Upstream phases cited:** phase-0-intake.md

## Summary

PATH's 2026-06-05 options tape is **active in absolute terms but directionally
flat and not unusual for the name**. The name sits at the **91.9th universe
percentile on total premium** ($4.72M) and 91.2th on net-directional premium —
but that net direction is only **+$55,591 bullish on $4.72M traded (1.2% net)**,
i.e. a coin-flip tape, and the name is **outside the top-50** on every screener
ranking (bullish, bearish, volume-vs-average ≥2×, IV-rank). Against its own
40-session history today is just the **64th percentile** — a mildly busy, fully
two-way day. Sector context is hostile: **Technology was the most-sold sector
on the day (−$890.3M net directional premium)**. This is four days after the
2026-06-01 earnings-pop run (price 13.10 → 11.24 since, phase-0 drift).

## Universe ranking

- Net **bullish** premium rank: **outside top-50** [CTX: `screener bullish-bearish --direction bullish`]. Day's leaders: SPX +$2.40B, NDXP +$73.8M, IWM +$55.2M, **STM +$53.4M**, NDX +$43.5M (index-dominated; STM the lead single name).
- Net **bearish** premium rank: **outside top-50**. Leaders: SPXW −$2.09B, QQQ −$116.9M, SNDK −$114.3M, SOXL −$85.6M, NVDA −$81.4M — **semis/tech being sold hard**.
- Volume-vs-average (≥2×): **outside top-50** (leaders are micro-caps: FCPT 5309×, IMCR 732×). PATH equity rel-volume 1.03 (phase-0 drift) — option volume similarly unexceptional.
- IV-rank high: outside top-50 (MU/AIS/MRVL pinned at 100).
- Exact universe percentiles `[CTX:universe_pctile DUCKDB]`: total_prem **91.9**, net_dir **91.2**, iv_rank **41.6**, vol_vs_avg **79.8** (of ~6k optionable names; 92nd pctile ≈ rank ~500 — busy, not a leader).

## Sector read

- PATH sector: **Technology** (screener parquet, `sector` column).
- Sector net-directional tape 2026-06-05 `[CTX: DUCKDB]`: Technology **−$890.3M**
  (worst of all sectors, on $19.6B total premium); Communication Services −$137.0M,
  Consumer Cyclical −$114.5M. Only Consumer Defensive green (+$13.3M).
- **PATH's sector is decisively out of favour today** — a name-vs-sector yellow
  flag is *not* present (PATH itself is flat, not strong), but phase 6 should
  treat the tech tape as a headwind.

## Self-history (40 sessions, gap-aware)

- `self_pctile_net_dir` = **64.1**, `self_pctile_total` = **64.1**, N = **40
  sessions** `[CTX:self_pctile DUCKDB]` (window includes the 2026-03-28→04-24
  hole; percentile is over available sessions only, per phase-0 gap flag).
- Today is a 64th-percentile day for PATH — above median, nowhere near its own
  extremes (its extremes were the 2026-06-01 earnings session: 67.7M shares,
  rel-vol 2.02 per phase-0 drift).

## PATH's own screener block (`uw insights deep-dive .uw_screener`)

| Field | Value |
|---|---|
| bullish_premium | $2,131,707 |
| bearish_premium | $2,076,116 |
| net direction (derived bullish−bearish) | **+$55,591** |
| call_premium / put_premium | $3,816,349 / $899,432 |
| call_volume / put_volume | 45,372 / 17,735 |
| put_call_ratio | **0.39** |
| iv30d | 64.74% |
| iv_rank | **40.03** |
| implied_move / implied_move_perc | $0.2521 / **2.238%** |
| total_open_interest | 815,535 |
| next_earnings_date | 2026-09-03 (no near-term event) |

## Source

CLI (`uw screener` ×4, `uw insights deep-dive`) **+ DuckDB §C** (exact universe
percentile, self-history percentile, sector aggregate). PATH outside top-50 on
all four screener rankings — recorded as information, not error.

## Verdict for downstream

```
universe_pctile_total_prem:  91.9          [CTX:universe_pctile DUCKDB]
universe_rank_net_dir:       outside top-50
sector_leadership:           Technology is lagging today (worst sector, −$890.3M net dir)
iv_rank:                     40.03
implied_move_pct:            2.238
self_pctile_net_dir:         64.1          [CTX:self_pctile DUCKDB] (N=40)
unusual_verdict:  BUSY_NAME_NORMAL_DAY
```

**`BUSY_NAME_NORMAL_DAY`** — high absolute premium (92nd universe pctile) but:
volume-vs-average < 2× (79.8 pctile, rel-vol 1.03), self-history only 64th
pctile, net direction a flat +1.2%, outside top-50 everywhere.
**Per `rubrics/confluence-scoring.md`, phases 1–2 confluence is capped at `+`
(not `++`).**

- **Bias from this phase:** neutral (context-only; no directional bias by design)
- **Conviction:** n/a (context phase)
- **Three things later phases should remember:**
  1. Flow is two-way and flat (+$55.6k net on $4.7M) — any single bullish print
     phase 1 finds must be weighed against near-equal bearish premium.
  2. Tech is the day's most-sold sector (−$890M) — sector headwind for longs.
  3. P/C 0.39 with IV rank 40 four days post-earnings-pop-and-fade; phase 3
     must check whether the call OI is opening or post-earnings unwind.
- **Open questions:** is the flat net flow a genuine equilibrium or a large
  bullish position being distributed into strength faded? (phases 1–3)

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw screener bullish-bearish --direction bullish --top-n 50 --date 2026-06-05 --json` | PATH outside top-50; leaders ← `.results[:5][]{ticker,net_flow}` | top-50 |
| `uw screener bullish-bearish --direction bearish --top-n 50 --date 2026-06-05 --json` | PATH outside top-50; SPXW −$2.09B ← `.results[:5]` | top-50 |
| `uw screener volume-vs-average --min-volume-ratio 2 --top-n 50 --date 2026-06-05 --json` | PATH outside top-50 ← rank scan on `.results[].ticker` | top-50 |
| `uw screener iv-rank --mode high --top-n 50 --date 2026-06-05 --json` | PATH outside top-50; MU/AIS/MRVL ivr=100 ← `.results[:3]` | top-50 |
| `uw insights deep-dive --symbol PATH --date 2026-06-05 --json` | bullish 2,131,707; bearish 2,076,116; P/C 0.39; iv_rank 40.03; implied_move_perc 0.02238 ← `.uw_screener.*` | whole-tape |
| DuckDB §C universe pctile (screener parquet 2026-06-05) | 91.9 / 91.2 / 41.6 / 79.8 | full universe |
| DuckDB §C self-history (40 screener parquets) | self_pctile_net_dir 64.1, N=40 | 40 sessions |
| DuckDB sector aggregate (screener parquet) | Technology −$890.3M net dir | full universe |

## Tool errors

One DuckDB informational query referenced a non-existent `industry` column
(`Binder Error: Referenced column "industry" not found`); re-run with `sector`
only — succeeded. No `uw`/`fz` errors; all JSON parsed through jq.

## DATA NOTE / CORRECTION

None — first reads stood.
