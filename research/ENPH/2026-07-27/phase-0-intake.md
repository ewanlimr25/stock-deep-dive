# Phase 0 — Intake

**Ticker:** ENPH
**As-of date:** 2026-07-27
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/ENPH/2026-07-27
**Version:** v1
**Generated:** 2026-07-27T20:08:00-04:00
**Upstream phases cited:** — (root phase)

## Summary

Ticker ENPH (Enphase Energy Inc, Technology / Solar) validated. Output directory
created fresh — no prior `phase-*.md` in `research/ENPH/2026-07-27/`, so this run
is **v1**. The `uw` CLI is reachable and the local snapshot carries all five
datasets through **2026-07-27**, i.e. the as-of date is fully covered with no
stale-date substitution needed. ENPH has live options activity. `fz` is
reachable but its `quote` payload is **degraded** (14 of 84 fundamental fields);
float/short-interest were recovered via `fz screen --view ownership` instead —
and the recovered **Short Float = 17.94%** is a headline number that phase-7c
must gate on.

## UW availability

- `uw historical available-dates --json`: **ok** (exit 0, valid JSON)
- Datasets present: `darkpool`, `hotchains`, `oi`, `options`, `screener` — n=74 dates each
- Latest available **options** date: **2026-07-27** ✅ (= as-of)
- Latest available **darkpool** date: **2026-07-27** ✅ (= as-of)
- Latest available **oi** / **hotchains** / **screener** date: **2026-07-27** ✅

As-of date is the newest date in the snapshot. All `--date 2026-07-27` calls
downstream will hit real data, not a fallback.

## Ticker sanity

- Options activity (`uw options-flow unusual-volume --symbol ENPH --top-n 1 --date 2026-07-27`): **non-empty**
  - `ENPH 2026-08-07 P35.5` — `total_volume=216`, `open_interest=2`, `vol_oi_ratio=108`,
    `total_premium=$50,753`, `trade_count=97`, `avg_iv=1.196`
- Source parquet: `~/Documents/Stocks/All Options/bot-eod-report-2026-07-27.parquet`
- Note for phase 1: the single most vol/OI-extreme line on the tape is a **near-dated
  put** at a strike ~7% below the fz print price of $38.01, on essentially zero prior OI.
  Do not read one line as the tape — phase 1 must aggregate.

## Local data (escape hatch / gap-awareness)

- `local_data_available`: **yes** · `duckdb_available`: **yes**
- `STOCKS_DIR`: `/Users/ewan/Documents/Stocks`
- Available local dates (n=74): `2026-03-13 … 2026-03-27`, then `2026-04-27 … 2026-07-27`
- **Gap flagged: yes** — a one-month hole between **2026-03-27 and 2026-04-27**
  (no trading dates in April 1–24). Phase-5 lookbacks longer than ~62 sessions
  and any phase-0.5 self-history percentile must treat `dates_used` as the real N,
  not the nominal window.
- Contiguous recent run: **2026-04-27 → 2026-07-27 = 62 sessions**, clean. Any
  lookback ≤62 sessions is gap-free.
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: **yes** (`fz doctor --agent` exit 0)
- `fz quote ENPH --agent`: **degraded** — returned only **14** of the documented 84
  `.fundamentals` fields. `Shs Float`, `Shs Outstand`, `Short Float`, `Price`,
  `RSI (14)`, SMAs, `Target Price`, `P/E` were all **absent (null)**.
  Fields that did return: `Market Cap 5.01B`, `Enterprise Value 4.69B`,
  `Sales 1.40B`, `Income 135.00M`, `Book/sh 8.36`, `Cash/sh 7.06`,
  `Employees 2872`, `Payout 0.00%`, `Dividend TTM "-"`, `IPO Mar 30, 2012`.
- **Recovery path used:** `fz screen --view ownership --tickers ENPH --agent`
  returned the ownership block intact:

| Field | Value |
|---|---|
| **Shs Float** | **127.77M** |
| Shs Outstanding | 131.78M |
| **Short Float** | **17.94%** |
| Short Ratio | 3.04 |
| Inst Own | 100.56% |
| Insider Own | 3.06% |
| Insider Trans | −3.09% |
| Inst Trans | +2.13% |
| Price | 38.01 |
| Change | +3.57% |
| Avg Volume | 7.54M |
| Volume | 3,732,274 |
| Market Cap | 5.01B |

  Cross-check: `Market Cap 5.01B` is **identical** in both the degraded `quote`
  and the ownership screen, confirming the ownership row is ENPH despite the
  `Ticker` string rendering as `"EENPH"` (a display artifact in the screen output,
  see Tool errors).
- **`Shs Float` carried forward: 127.77M** — phase-2 and phase-3 use this to express
  dark-pool block size and OI walls as % of float.
- **Flag for phase-7c:** `Short Float = 17.94%` on a 127.77M float with a
  `Short Ratio` of only 3.04 days is a heavily-shorted, liquid-to-cover name.
  This is a *positioning gate* input, not a bull thesis — 7c must decide whether
  it caps size or enables a squeeze read.
- **Flag for phase-7b:** `Inst Own 100.56%` (>100%) is a Finviz artifact of shares
  lent into the short base, not a data error — it corroborates the heavy short.
- On `fz_available=yes` but partial, phase-7b still prefers Finnhub statements;
  phase-7c uses the ownership-screen SI above rather than WebSearch.

## Prior versions

None in `research/ENPH/2026-07-27/`.

**Earlier ENPH deep dives exist on other dates** (not versions of this run, but
the phase-0.5 self-history pass should read them for prior-thesis continuity):

- `research/ENPH/2026-05-19/`
- `research/ENPH/2026-05-22/`

`fz quote-drift` was not run: the prior runs predate the `fz` quote snapshot
convention and the current `fz quote` payload is degraded anyway, so there is no
usable baseline to diff. Drift will be assessed qualitatively in phase-0.5 by
reading the two prior runs' artifacts.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw historical available-dates --json` | options/darkpool/oi/hotchains/screener latest = `2026-07-27`, n=74 each ← `to_entries[] \| .value\|sort\|last` | all 5 datasets |
| `uw options-flow unusual-volume --symbol ENPH --top-n 1 --date 2026-07-27 --json` | `vol_oi_ratio=108`, `total_volume=216`, `total_premium=50753`, `strike=35.5`, `option_type=put`, `expiry=2026-08-07` ← `.results[0]` | top-1 |
| `ls "$STOCKS_DIR/Stock Screener/"` + `python3 -c "import duckdb"` | 74 local dates, gap 2026-03-27→2026-04-27; `DUCKDB=yes` | dir listing |
| `fz quote ENPH --agent` | 14 fields only; `Market Cap=5.01B` ← `.fundamentals."Market Cap"`; float/SI = **null** | 1 |
| `fz screen --view ownership --tickers ENPH --agent` | `Float=127.77M`, `Short Float=17.94%`, `Short Ratio=3.04`, `Price=38.01` ← `.[0].Float` / `.[0]."Short Float"` / `.[0]."Short Ratio"` / `.[0].Price` | 1 |

## Tool errors

No hard errors (all commands exit 0, all output round-tripped through `jq`). Two
degradations recorded rather than errors:

1. **`fz quote ENPH --agent` — partial payload.** Returned 14 `.fundamentals`
   keys instead of the ~84 documented in `lib/uw-json-paths.md §fz`. Re-run once;
   identical 14-key result, so it is deterministic for this ticker/session, not a
   transient truncation. Missing: `Shs Float`, `Shs Outstand`, `Short Float`,
   `Short Ratio`, `Price`, `RSI (14)`, `SMA20/50/200`, `Perf YTD`, `52W High/Low`,
   `Recom`, `Target Price`, `P/E`, `Forward P/E`.
   **Mitigation:** ownership screen used for float/SI (above). Phases needing
   `RSI (14)` / SMAs / `Target Price` / `Recom` must source them elsewhere
   (phase-5 price context, phase-7b analyst cross-source) or mark them `n/a`.
2. **`fz screen --view ownership` — `Ticker` field renders as `"EENPH"`.** Cosmetic
   string artifact in the screen output. Confirmed to be ENPH by the exact
   `Market Cap = 5.01B` match against `fz quote ENPH`. No numeric impact; do not
   propagate the malformed string into any downstream citation.

## DATA NOTE / CORRECTION

First read stood for every value written above. The only re-read was the
deliberate `fz quote` retry (item 1 in Tool errors), which reproduced the same
14-key payload and therefore changed no number.

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake sets no bias)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. **`Shs Float = 127.77M`, `Short Float = 17.94%`, `Short Ratio = 3.04`.**
     Float normalizes phase-2 blocks and phase-3 walls; the ~18% short interest is
     a phase-7c gate input and a two-sided risk (squeeze fuel *and* a crowded-bear
     signal). Market cap is only **$5.01B** — a small-cap, so absolute premium and
     block sizes will look small versus mega-caps; judge everything in % -of-float
     and % -of-ADV (`Avg Volume 7.54M`) terms, never in raw dollars.
  2. **The local snapshot has a real one-month hole (2026-03-27 → 2026-04-27).**
     Any lookback ≤62 sessions is clean; anything longer silently spans the gap.
     Phase-5 must report `dates_used`, not the nominal window.
  3. **Two prior ENPH deep dives exist (2026-05-19, 2026-05-22), ~9–10 weeks stale.**
     Phase-0.5 must read them and state explicitly whether today's setup confirms,
     contradicts, or is unrelated to the prior thesis — a repeat call on the same
     name is worth less than an independent one.
- **Open questions:**
  - Is today's tape genuinely unusual for ENPH, or is a 108× vol/OI put line just
    a normal day in a $5B name with 7.54M ADV? → **phase-0.5**
  - Does the near-dated downside line (Aug-07 $35.5 put) represent directional
    positioning or hedging against the short base? → **phase-1 / phase-3**
  - `fz quote` is degraded — can `RSI (14)`, SMAs, `Target Price` and `Recom` be
    recovered from another `fz` view or must phase-7b mark them `n/a`? → **phase-7b**
