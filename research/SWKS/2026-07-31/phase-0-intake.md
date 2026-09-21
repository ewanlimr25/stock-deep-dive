# Phase 0 — Intake

**Ticker:** SWKS
**As-of date:** 2026-07-31
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/SWKS/2026-07-31
**Version:** v1
**Generated:** 2026-08-02

## Summary

Ticker SWKS (Skyworks Solutions Inc, Technology / Semiconductors, USA) validated.
Output directory created empty — this is a v1 run. `uw` CLI reachable and the
as-of date 2026-07-31 is the **latest** available date across all five local
datasets (darkpool, hotchains, oi, options, screener), so nothing is stale.
Options activity confirmed present (top-premium trades return rows) although the
narrower `unusual-volume` screen (vol >> OI) returns **empty** for SWKS on this
date — a first hint that flow is positional rather than fresh-opening. `fz` is
reachable but **degraded** (14 of 84 fundamental fields parse; `Shs Float`,
`Short Float`, `Price` all absent), so the float-normalization and short-interest
lanes must fall back. Proceeding to phase 0.5.

## UW availability

- `uw historical available-dates --json`: **ok** (exit 0, valid JSON, 5 dataset keys)
- Datasets present: `darkpool`, `hotchains`, `oi`, `options`, `screener` — **78 dates each**
- Latest available options date: **2026-07-31**
- Latest available darkpool date: **2026-07-31**
- Latest available oi date: **2026-07-31**
- Latest available hotchains date: **2026-07-31**
- Latest available screener date: **2026-07-31**
- ⇒ As-of 2026-07-31 == latest snapshot. No forward-looking leakage risk, no
  staleness gap. (Arrays sorted explicitly with `sort | .[-1]` — the raw arrays
  are unsorted.)

## Ticker sanity

- `uw options-flow unusual-volume --symbol SWKS --top-n 3 --date 2026-07-31`:
  **empty** (`.results == []`). Not an error — the symbol resolves, the screen
  simply has no vol-far-exceeds-OI contracts for SWKS on this date.
  → Flagged as **thin *new-position* options activity**; carry to phase 1/3.
- `uw options-flow top-premium-trades --symbol SWKS --top-n 5 --date 2026-07-31`:
  **5 rows returned**. Largest print: **put, strike 52.5, expiry 2026-08-21,
  premium $173,030, size 2,662, side `bid`, IV 0.634, delta −0.130, underlying
  $61.48 @ 14:06:26Z**.
  → Options market is live and tradeable; the ticker is valid for the full workup.
- Company metadata (`fz quote`): Skyworks Solutions Inc · Technology ·
  Semiconductors · USA · S&P 500 · Market Cap **$9.37B** · Enterprise Value
  **$9.25B** · Sales **$4.01B** · Income **$290.10M** · Payout **91.35%** ·
  Dividend TTM **2.84 (4.56%)**.

## Local data (escape hatch / gap-awareness)

- `local_data_available`: **yes** · `duckdb_available`: **yes** (`import duckdb` ok)
- `STOCKS_DIR`: `/Users/ewan/Documents/Stocks`
- Available local dates (78): 2026-03-13 … 2026-03-27, **[GAP]**, 2026-04-27 … 2026-07-31
- **Gap flagged: YES** — one contiguous block 2026-03-13→2026-03-27 (11 sessions),
  then a hole covering 2026-03-30 → 2026-04-24 (~4 weeks missing), then a dense
  contiguous block 2026-04-27 → 2026-07-31 (67 sessions).
  → Phase 5 (historical) must treat any lookback longer than ~67 sessions as
  **non-contiguous** and must not compute a continuous return path across the
  March/April boundary. Self-history percentiles in phase 0.5 should be scoped to
  the post-2026-04-27 block unless explicitly noting the gap.
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: **yes, DEGRADED**
  - `fz --version` → `finviz-pp-cli 1.0.0`; `fz doctor` → `api: reachable`,
    `auth: not required`, `config: ok`.
  - `fz doctor` cache hint: *"sync_state is empty; run 'finviz-pp-cli sync' to
    hydrate"* — local store unhydrated, so reads are live-scrape only.
  - `fz quote SWKS --json` parses only **14 of the expected 84** fundamental
    fields. Missing: `Shs Float`, `Shs Outstand`, `Short Float`, `Short Ratio`,
    `Price`, and all the valuation/margin/performance grid.
  - `fz screen --tickers SWKS` returns a row but with a **mangled ticker field**
    (`"Ticker": "SSWKS"`) and no float/SI columns.
- `Shs Float`: **n/a** (not returned) — phase-2/3 order-size-as-%-of-float
  normalization must fall back to a WebSearch/Finnhub share-count or be marked
  unavailable.
- `Short Float` / `Short Ratio`: **n/a** — phase-7c short-interest gate falls back
  to **WebSearch** per orchestration rule 1c.
- **Timing caveat:** every `fz` read is a **live** scrape (executed 2026-08-02),
  not an as-of-2026-07-31 read. `fz screen` shows Price **62.28**, Change
  **−0.32%**, Volume **6,203,824** — these are *live* values and must be tagged
  advisory-only, never mixed into as-of computations or the Kelly `p`.
- `fz quote-drift`: not run — no prior run for SWKS, so no prior snapshot exists.

## Prior versions

None. This is v1 — `research/SWKS/2026-07-31/` was empty before this run.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `uw historical available-dates --json` | 5 keys ← `keys`; latest=2026-07-31 ← `.[$k] \| sort \| .[-1]`; 78 dates each ← `to_entries[] \| .value\|length` | whole |
| `uw options-flow unusual-volume --symbol SWKS --top-n 3 --date 2026-07-31 --json` | `[]` ← `.results` | top-3 (empty) |
| `uw options-flow top-premium-trades --symbol SWKS --top-n 5 --date 2026-07-31 --json` | n=5 ← `.results\|length`; premium=173030 ← `.results[0].premium`; strike=52.5 ← `.results[0].strike`; side=`bid` ← `.results[0].side`; underlying=61.48 ← `.results[0].underlying_price` | top-5 |
| `ls "$STOCKS_DIR/Stock Screener/"` + `python3 -c "import duckdb"` | DUCKDB=yes; 78 local screener dates; gap 2026-03-30→2026-04-24 | whole dir |
| `fz doctor --json` | api=`reachable`; cache.status=`unknown`; cache.hint=`sync_state is empty` | whole |
| `fz quote SWKS --json` | 14 ← `.fundamentals\|length`; float=null ← `.fundamentals."Shs Float"`; Market Cap=9.37B ← `.fundamentals."Market Cap"` | whole |
| `fz screen --tickers SWKS --json` | Price=62.28, Ticker=`SSWKS` (mangled) ← `.[0]` | 1 row |

## Tool errors

- `fz screener …` → `Error: unknown command "screener" for "finviz-pp-cli"`
  (operator error; correct leaf is `fz screen`). Re-run with `screen` succeeded.
- No `uw` errors. No aborting conditions.

**Non-fatal degradations recorded (not errors):**
- `uw options-flow unusual-volume` empty for SWKS — valid empty result, not a failure.
- `fz quote` field-parse shortfall (14/84) — degrades the `fz` lane to advisory
  metadata only; SI/float lanes fall back per rule 1c.

## DATA NOTE / CORRECTION

- First `fz quote SWKS --agent` call returned nulls for float/short-float. The
  `--agent` flag implies `--compact`, so the shortfall was initially suspected to
  be compaction. Re-read with plain `fz quote SWKS --json --no-color --no-input`
  returned the **same 14 fields** — confirming the shortfall is a real upstream
  parse degradation, not a compaction artifact. `Shs Float` is genuinely
  unavailable, not merely suppressed.

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only — no directional read taken)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. **As-of == latest.** 2026-07-31 is the newest date in all five datasets, so
     every `--date 2026-07-31` read is a full, non-stale snapshot. Trailing/"latest"
     tools that anchor to the newest date will coincidentally agree with the as-of
     date on this run — but still pass `--date` explicitly where the flag exists.
  2. **The local history has a 4-week hole** (2026-03-30 → 2026-04-24). Phase 5
     and any DuckDB self-history percentile must scope to the contiguous
     2026-04-27 → 2026-07-31 block (67 sessions) or explicitly annotate the break.
  3. **`fz` is degraded and live-only.** No float, no short float, no as-of price
     from `fz`. Phase 7c's short-interest gate needs WebSearch; phase 2/3 cannot
     express print size as % of float from `fz`. Any `fz` number quoted downstream
     is a 2026-08-02 live value, tagged advisory, and never enters the Kelly `p`.
- **Open questions:**
  - Why does `unusual-volume` return empty while `top-premium-trades` returns
    $173k puts? Phase 1 must resolve whether SWKS flow is *closing/rolling*
    existing OI rather than opening new positions.
  - The single largest premium print is a **put bought on the bid** (side=`bid`
    ⇒ seller-initiated) at a strike ~15% below spot — phase 1 must grade whether
    that is put *selling* (bullish) or a bearish hedge lifted down, since the
    Signal Quality Hierarchy treats opening-put prints differently by side.
