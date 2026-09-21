# Phase 0 — Intake

**Ticker:** FSLR
**As-of date:** 2026-07-31
**Output dir:** `/Users/ewan/Development/stock-deep-dive/research/FSLR/2026-07-31`
**Version:** v1 (new date directory)
**Generated:** 2026-07-31

## Summary

FSLR (First Solar Inc, Technology / Solar, S&P 500) validated as a US-listed
optionable equity. Output directory created fresh — this is **v1** for
2026-07-31. The `uw` CLI is reachable and **all five datasets carry a
2026-07-31 snapshot**, so the as-of date is fully covered with no
latest-date substitution needed. Options activity confirmed live.
DuckDB escape hatch available. `fz` reachable but its `quote` command is
**degraded to a 14-field subset** — float/short-interest/price were sourced
instead from `fz screen --view ownership`, which works.

## UW availability

- `uw historical available-dates --json`: **ok** (5 datasets, 78 dates each)
- Latest available options date: **2026-07-31** ✓ matches as-of
- Latest available darkpool date: **2026-07-31** ✓ matches as-of
- Latest available oi date: **2026-07-31** ✓
- Latest available hotchains date: **2026-07-31** ✓
- Latest available screener date: **2026-07-31** ✓

## Ticker sanity

- Options activity (`uw options-flow unusual-volume --symbol FSLR --top-n 1`):
  **non-empty** — `FSLR 2026-08-07 C237.5`, `total_volume=152`,
  `open_interest=8`, `vol_oi_ratio=19`, `total_premium=$24,143`,
  `avg_iv=0.7606`. Source parquet:
  `~/Documents/Stocks/All Options/bot-eod-report-2026-07-31.parquet`.
- Note the ~76% avg IV on the front-week OTM call — carry to phase-4/5 for the
  IV-percentile read.

## Local data (escape hatch / gap-awareness)

- `local_data_available`: **yes** · `duckdb_available`: **yes**
- `STOCKS_DIR`: `/Users/ewan/Documents/Stocks`
- Dataset dirs present: `All Options`, `Dark pool`, `Hot Option Chains`,
  `OI changes`, `Stock Screener` (78 files each)
- Available local dates (options, sorted): 2026-03-13 … 2026-03-27, then
  2026-04-27 … 2026-07-31.
- **Gap flagged: YES** — no data between **2026-03-27 and 2026-04-27**
  (~1 month). Phase-5 historical lookbacks must not assume contiguity across
  that boundary; a "60 trading day" window in file-count terms spans a longer
  calendar period than it appears.
- Contiguous run since the gap: 2026-04-27 → 2026-07-31 = **63 sessions**,
  which is the usable clean self-history window.
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: **yes (partial)** — `fz doctor` reports
  `api: reachable`, `config: ok`, cache `sync_state is empty`.
- **`fz quote FSLR` is degraded**: returns only **14** fundamental fields
  (Book/sh, Cash/sh, Dividend*, Employees, Enterprise Value, IPO, Income,
  Index, Market Cap, Payout, Sales) instead of the documented 84. `Price`,
  `Shs Float`, `Short Float`, `Earnings`, P/E and analyst-target fields are
  **absent** on this path — confirmed identical under `--json` (no `--compact`)
  and under `--data-source live`.
- **Working substitute:** `fz screen --tickers FSLR --view ownership --json`
  returns the needed fields. Values as-of this run:

  | Field | Value |
  |-------|-------|
  | Price | **211.03** |
  | Change | **+2.44%** |
  | Volume | 3,426,122 |
  | Avg Volume | 2.42M |
  | **Shs Float** | **101.48M** |
  | Outstanding | 107.47M |
  | **Short Float** | **9.75%** |
  | Short Ratio | **4.09** |
  | Inst Own | 92.82% |
  | Inst Trans | −5.03% |
  | Insider Own | 5.55% |
  | Insider Trans | −2.02% |
  | Market Cap | 22.68B |

- **`Shs Float` = 101.48M** — carried forward to phase-2/3 for
  % -of-float normalization of dark-pool blocks and OI walls.
- **Early flags for the gates:** Short Float 9.75% is elevated (phase-7c
  positioning gate); Inst Trans −5.03% and Insider Trans −2.02% are both
  net-selling (phase-7b / 7c). These are *recorded, not scored* here.
- From `fz quote` (the 14 fields that did return): Market Cap 22.68B,
  Enterprise Value 21.14B, Sales 5.38B, Income 1.75B, Book/sh 96.03,
  Cash/sh 16.07, Employees 7,900, no dividend, S&P 500 member.
- On the degraded `quote` path, phase-7b's fundamental-ratio pulls should lean
  on Finnhub, with `fz screen` views as the structured fallback.

## Prior versions

None in this directory (v1). Prior FSLR deep dives exist under other dates and
may be referenced as self-history, not as versions of this run:

- `research/FSLR/2026-05-18/`
- `research/FSLR/2026-07-20/`

`fz quote-drift` was not run: the degraded `quote` path above returns no
snapshotable fundamental surface, and no prior `fz` snapshot exists in this
directory.

## Tool errors

No hard errors — all commands exited 0. Two degradations recorded, neither
blocking:

1. `fz quote FSLR --agent` / `--json` / `--data-source live` — exit 0 but
   returns 14 of 84 fundamental fields; `Price`, `Shs Float`, `Short Float`,
   `Earnings` all absent. **Worked around** via
   `fz screen --tickers FSLR --view ownership --json`.
2. `fz screen --tickers FSLR --view ownership --json` returns
   `"Ticker": "FFSLR"` — a duplicated-leading-character rendering artifact in
   the Ticker field only. All accompanying values match First Solar
   (Market Cap 22.68B agrees with `fz quote`), so the row is trusted; do not
   key any downstream join on that literal string.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `uw historical available-dates --json` | options latest=2026-07-31 ← `.options[] \| sort \| last`; count=78 ← `.options\|length` | all 5 datasets |
| `uw options-flow unusual-volume --symbol FSLR --top-n 1 --json` | vol_oi_ratio=19 ← `.results[0].vol_oi_ratio`; total_premium=24143 ← `.results[0].total_premium`; avg_iv=0.7606 ← `.results[0].avg_iv` | top-1 |
| `ls "$STOCKS_DIR/Stock Screener/" \| wc -l` | 78 files; DUCKDB=yes | dir listing |
| `fz doctor --agent` | api=reachable ← `.api`; cache hint="sync_state is empty" ← `.cache.hint` | 1 |
| `fz quote FSLR --json` | fundamentals field count=14 ← `.fundamentals\|length` (expected 84) | 1 |
| `fz screen --tickers FSLR --view ownership --json` | Float=101.48M ← `.[0].Float`; Short Float=9.75% ← `.[0]."Short Float"`; Price=211.03 ← `.[0].Price` | 1 |

## DATA NOTE / CORRECTION

Initial `fz quote FSLR --agent` was read as returning nulls for
`Price` / `Shs Float` / `Short Float`. First hypothesis — that `--agent`
implies `--compact` and truncated the payload — was tested and **rejected**:
re-running with plain `--json` and with `--data-source live` returned the same
14 fields. The degradation is in the `quote` endpoint itself, not the flags.
Corrected source for those three fields is
`fz screen --tickers FSLR --view ownership --json`, verified above.

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake sets no bias)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. **`Shs Float` = 101.48M** (Outstanding 107.47M) — use for all
     % -of-float normalization in phase-2 (dark-pool block size) and phase-3
     (OI walls).
  2. **Local data gap 2026-03-27 → 2026-04-27.** Phase-5 self-history and any
     DuckDB percentile cut must use the clean **2026-04-27 → 2026-07-31
     (63-session)** window, or explicitly handle the discontinuity.
  3. **`fz quote` is degraded to 14 fields** — phase-7b/7c must route
     float/SI/price through `fz screen --view ownership` and lean on Finnhub
     for ratios. Pre-recorded for the gates: **Short Float 9.75%**,
     **Short Ratio 4.09**, **Inst Trans −5.03%**, **Insider Trans −2.02%**.
- **Open questions:** Is the 9.75% short float a squeeze fuel or a
  well-founded bearish position? Is the −5.03% institutional-transaction
  reading distribution or rebalancing? Both deferred to phase-7c.
