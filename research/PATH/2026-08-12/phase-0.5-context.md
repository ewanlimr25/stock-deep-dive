# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** PATH
**As-of date:** 2026-08-12
**Generated:** 2026-08-13T01:20:00Z
**Upstream phases cited:** phase-0-intake.md

## Summary

PATH is **not** among today's directional leaders on either side of the tape —
it ranks outside the top-50 on net bullish premium, net bearish premium,
volume-vs-average, and IV-rank-high. Its exact universe percentile (via the
DuckDB escape hatch, 4,539-name optionable universe) puts it at the **92.5th
percentile on raw total premium** but only the **14.0th percentile on net
directional premium** — i.e. PATH is a consistently liquid options name (lots
of gross premium changes hands every day) but today's net skew is mild and
tilts slightly bearish, not something that stands out among 4,539 names.
Critically, **self-history says today is completely ordinary for PATH itself**
(47.1st/49.4th percentile vs its own 86-session window) and today's volume is
actually *below* its 30-day average (0.735×). Verdict: **BUSY_NAME_NORMAL_DAY**
— phases 1–2 confluence should be capped at `+`, not `++`, per
`rubrics/confluence-scoring.md`.

## Universe ranking

- Net bullish premium (`uw screener bullish-bearish --direction bullish --top-n 50`):
  PATH not present → outside top-50. Leaders: SPX ($3.86B), SPXW ($192M), SPCX
  ($87M), NBIS ($59M), NVDA ($47M), CRWV ($41M), SMCI ($35M), SNDK ($28M).
- Net bearish premium (same, `--direction bearish`): PATH not present → outside
  top-50. Leaders: SPY (-$110M), META (-$71M), MU (-$68M), AMD (-$42M), AMZN
  (-$29M), AAPL (-$25M), PANW (-$23M), TSLA (-$22M), PLTR (-$21M).
- Volume-vs-average (`--min-volume-ratio 2 --top-n 50`): PATH not present →
  outside top-50 (consistent with the DuckDB read below showing PATH's own
  vol/avg ratio at 0.735×, i.e. *below* its 30-day average today).
- IV-rank-high (`--mode high --top-n 50`): PATH not present → outside top-50
  (PATH's raw `iv_rank=63.16` is elevated for itself but not extreme enough to
  crack the universe's top 50 on a day when many names carry high IV rank).

## Sector read

PATH's `sector` field is `Technology` (read from the local screener parquet —
the `uw screener` API's `sector` field is null/broken per the known UW issue,
`[CTX:sector DUCKDB]`); Finviz corroborates `Software - Infrastructure` as the
industry (phase-0 `fz quote`).

Technology is the single most *active* sector on today's tape on **both**
sides — not a clean "leading" or "lagging" read:
- Bullish top-15: 6 of 15 are Technology (NVDA, CRWV, SMCI, SNDK, SKHY, DDOG) —
  concentrated in AI/datacenter infra and semis.
- Bearish top-15: 8 of 15 are Technology (MU, AMD, AAPL, PANW, PLTR, TSM, MSFT,
  STX) — concentrated in semis (MU/AMD/TSM), mega-cap hardware (AAPL), and
  enterprise software/security (PANW, PLTR).

PATH's own sub-industry neighbors (PANW, PLTR — enterprise software/security)
sit on the **bearish** side of today's split; the semis/AI-infra names driving
the bullish side are not PATH's peer set. This is a mild yellow flag for
phase-6 to resolve, not a strong directional read either way — Technology is
internally bifurcated today, not uniformly "in favour."

## Self-history

(DuckDB escape hatch — local screener parquet present for 2026-08-12,
86 sessions in the available local window per `lib/duckdb-cuts.md §C`; the
window spans the known non-contiguous gap 2026-03-28→04-24, so 86 is the true
session count, not a calendar count.)

| Metric | Value | Self-percentile (86 sessions) |
|---|---|---|
| Net directional premium (`net_call_premium − net_put_premium`) | −$44,378 | 47.1 |
| Total premium (`call_premium + put_premium`) | $3,329,081 | 49.4 |

Both land almost exactly at the median of PATH's own recent trading history —
today is not unusual for PATH by its own standards.

## Universe percentile (DuckDB, full 4,539-name optionable universe)

| Metric | PATH percentile |
|---|---|
| Total premium | 92.5 |
| Net directional premium | 14.0 |
| IV rank | 90.7 |
| Volume vs. 30-day average | 56.5 |

Reconciling the apparent tension: PATH is a genuinely high-*gross*-premium name
(top-decile total premium — a structurally active options market, unrelated to
today specifically) but its *directional* skew today (14th pctile net-dir) is
mild in absolute dollars and only stands out as "low" because most other
optionable names skew more net-bullish today. This is not evidence of unusual
institutional accumulation or distribution in PATH specifically.

## Raw datapoints (source)

- `uw insights deep-dive --symbol PATH --date 2026-08-12`: `bullish_premium=
  $1,440,177`, `bearish_premium=$1,484,555`, `call_premium=$2,254,097`,
  `put_premium=$1,074,984`, `put_call_ratio=0.4748`, `iv_rank=63.16`,
  `iv30d=0.8212`, `implied_move=$0.50`, `implied_move_perc=3.29%`,
  `next_earnings_date=2026-09-03` (postmarket per DuckDB `er_time`) — **flag
  for phase-7c cross-check**: this field has been stale before on PATH runs
  (memory: 2026-05-29 run), verify against Finnhub `company-news`/`stock/earnings`.
- DuckDB screener row (`Stock Screener/stock-screener-2026-08-12.parquet`):
  `close=$15.26`, `prev_close=$15.72` (**-2.93%** on the day, matches phase-0's
  `fz screen` read), `marketcap=$7.128B`, `sector=Technology`,
  `total_volume=59,551,421`, `avg30_volume=81,004,700` (vol_x=0.735×).

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw screener bullish-bearish --direction bullish --top-n 50 --date 2026-08-12 --json` | PATH absent from `.results[]` | top-50 |
| `uw screener bullish-bearish --direction bearish --top-n 50 --date 2026-08-12 --json` | PATH absent from `.results[]` | top-50 |
| `uw screener volume-vs-average --min-volume-ratio 2 --top-n 50 --date 2026-08-12 --json` | PATH absent from `.results[]` | top-50 |
| `uw screener iv-rank --mode high --top-n 50 --date 2026-08-12 --json` | PATH absent from `.results[]` | top-50 |
| `uw insights deep-dive --symbol PATH --date 2026-08-12 --json` | `.uw_screener` block above | whole name |
| DuckDB `stock-screener-2026-08-12.parquet` §C percentile query | `pctile_total_prem=92.5, pctile_net_dir=14.0, pctile_iv_rank=90.7, pctile_vol_vs_avg=56.5` | 4,539-name universe (`call_volume+put_volume>0`) |
| DuckDB `stock-screener-*.parquet` (all local dates) §C self-history query | `self_pctile_net_dir=47.1, self_pctile_total=49.4, sessions_in_window=86` | PATH's own local history |

## Tool errors

<none>

## DATA NOTE / CORRECTION

<none — first read stood>

## Verdict for downstream phases

- **Bias from this phase:** neutral (context-setting only, per skill design —
  this phase sets no directional bias)
- **Conviction:** n/a (context phase)
- **`[CTX:]` block:**
  ```
  universe_pctile_total_prem:  92.5
  universe_rank_net_dir:       outside top-50 (pctile 14.0, mild bearish tilt)
  sector_leadership:           Technology most-active but bifurcated (bullish in AI/semis-infra, bearish in enterprise software/security — PATH's own peer set) today
  iv_rank:                     63.16
  implied_move_pct:            3.29%
  self_pctile_net_dir:         47.1
  unusual_verdict:             BUSY_NAME_NORMAL_DAY
  ```
- **Three things later phases should remember:**
  1. Today's flow is NOT cross-sectionally or self-historically unusual for
     PATH — cap phases 1–2 confluence at `+`, not `++`.
  2. `next_earnings_date=2026-09-03` is unverified against a second source —
     phase-7c must cross-check (this exact field has been stale before on a
     prior PATH run).
  3. PATH's software/security peer neighborhood (PANW, PLTR) is on the
     bearish side of today's tape, not the bullish semis/AI-infra side driving
     Technology's bullish leaders — mild yellow flag for phase-6.
- **Open questions:** whether the mild net-bearish tilt (14th pctile) reflects
  anything PATH-specific or is simply broad Tech's split character today;
  phase-1's flow read should determine whether the −$44K net skew concentrates
  in any single strike/expiry or is noise-level dispersion.
