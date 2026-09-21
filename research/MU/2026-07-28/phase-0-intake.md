# Phase 0 — Intake

**Ticker:** MU
**As-of date:** 2026-07-28
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/MU/2026-07-28
**Version:** v1 (first run in this dated directory)
**Generated:** 2026-07-28T21:10:00-04:00
**Upstream phases cited:** none (entry phase)

## Summary

Ticker MU validated (US-listed equity, NDX + S&P 500 member). Output directory created and
empty — this is **v1** for 2026-07-28. The `uw` CLI is reachable and every one of the five
local datasets (options, darkpool, oi, hotchains, screener) carries an **as-of date of
2026-07-28**, so no staleness fallback is required. MU is anything but thin: the top
unusual-volume contract alone printed **$26.59M premium on 11,401 contracts against 12 OI
(vol/OI 950×)**. Note for every downstream phase: MU closed **-8.85% at $820.53** on
**61.0M shares vs 52.22M avg** — this is a large single-day drawdown day, not a quiet tape,
and phases 1–5 must be read in that light.

## UW availability

- `uw historical available-dates`: **ok** (JSON parsed, 5 dataset keys)
- Latest available options date: **2026-07-28**
- Latest available darkpool date: **2026-07-28**
- Latest available oi / hotchains / screener date: **2026-07-28** (all)
- Coverage: 75 dates per dataset, 2026-03-13 → 2026-07-28

## Ticker sanity

- Options activity (`unusual-volume` top 1): **MU 820C exp 2026-07-29** —
  `total_premium=26,588,476`, `total_volume=11,401`, `open_interest=12`,
  `vol_oi_ratio=950.08`, `avg_iv=1.4362` (143.6% IV).
- Verdict: **very heavy** options activity. Deep-ATM weekly (strike 820 vs spot 820.53)
  with a 1-day expiry and 143.6% IV — consistent with an event-day tape. Proceed.

## Local data (escape hatch / gap-awareness)

- `local_data_available`: **yes** · `duckdb_available`: **yes**
- `STOCKS_DIR`: `/Users/ewan/Documents/Stocks`
- Available local dates: **75 files**, 2026-03-13 → 2026-07-28.
  Recent run: 2026-07-15, 07-16, 07-17, 07-20, 07-21, 07-22, 07-23, 07-24, 07-27, 07-28.
- **Gap flagged: yes** — a single non-contiguous gap **2026-03-27 → 2026-04-27 (31 days)**.
  Phase-5 historical percentiles and phase-0.5 self-history must treat the pre-gap block
  (2026-03-13…03-27, 11 dates) as a separate regime sample, not a continuous series.
  Post-gap continuous sample = **2026-04-27 → 2026-07-28 (64 dates)**.
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't express
  (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: **yes** (`fz doctor` green)
- **`fz quote MU --agent` returned a DEGRADED payload — 14 of 84 fundamental fields.**
  Present: Book/sh 89.22, Cash/sh 23.06, Market Cap 926.70B, Enterprise Value 907.03B,
  Sales 90.27B, Income 50.47B, Employees 53,000, Index "NDX, S&P 500", Payout 6.06%,
  Dividend TTM 0.53 (0.06%), Dividend Ex-Date Jul 06 2026, IPO Jun 01 1984.
  **Absent:** `Shs Float`, `Shs Outstand`, `Short Float`, `Price`, all Perf/SMA/margin/
  analyst fields. Re-run reproduced the same 14 fields (not transient).
- **Float recovered via fallback** (`fz screen --tickers MU --view ownership --agent`,
  `lib/fz-recipes.md §2b`):

  | Field | Value |
  |---|---|
  | `Price` | **820.53** |
  | `Change` | **-8.85%** |
  | `Float` | **1.12B** |
  | `Outstanding` | **1.13B** |
  | `Short Float` | **3.22%** (semi-monthly settlement, ~2-week lag) |
  | `Short Ratio` | **0.69** days to cover |
  | `Inst Own` / `Inst Trans` | **78.11%** / **-1.85%** |
  | `Insider Own` / `Insider Trans` | **0.44%** / **-6.05%** |
  | `Avg Volume` / `Volume` | **52.22M** / **61,039,321** |

- **Carried forward to phase-2/3:** `Shs Float = 1.12B`. A 1% -of-float block = **11.2M sh**;
  at $820.53 that is **~$9.19B notional**. Dark-pool prints will be normalized against this.
- Carried to 7b/7c as *advisory only*: Short Float 3.22% / Short Ratio 0.69 (low SI, no
  squeeze fuel), Inst Own 78.11% with **negative** institutional and insider transaction
  trend.
- Note: `fz` supplements SI/float/peer/breadth only (`lib/fz-recipes.md`) and is
  downside-only/advisory — it never enters the Kelly `p`.

## Prior versions

None in `research/MU/2026-07-28/`. **Prior MU runs exist on other dates:**
`research/MU/2026-06-23/` and `research/MU/2026-06-25/`. Those are separate as-of runs,
not versions of this one — phase-0.5 will read them as self-history for the
"what did we say last time / what changed" context leg.
`fz quote-drift` was not run: the degraded `fz quote` payload (14 fields) makes a field-level
drift diff unreliable, and no prior `fz` snapshot is recorded for MU.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `uw historical available-dates --json` | latest=2026-07-28 (×5 datasets), n=75 ← `to_entries[] \| .value \| sort \| last` | all 5 datasets |
| `uw options-flow unusual-volume --symbol MU --top-n 1 --date 2026-07-28 --json` | premium=26,588,476; vol=11,401; oi=12; vol_oi=950.08; iv=1.4362 ← `.results[0]` | top-1 |
| `ls "$STOCKS_DIR/Stock Screener/"` + python gap scan | 75 files; gap 2026-03-27→2026-04-27 (31d) | full list |
| `python3 -c "import duckdb"` | duckdb_available=yes | — |
| `fz doctor --agent` | fz_available=yes | — |
| `fz quote MU --agent` | 14 fields ← `.fundamentals \| keys \| length`; MktCap=926.70B, EV=907.03B, Sales=90.27B, Income=50.47B | degraded |
| `fz screen --tickers MU --view ownership --agent` | Float=1.12B; Price=820.53; Change=-8.85%; Short Float=3.22%; Short Ratio=0.69; Inst Own=78.11% ← `.[0]` | 1 row |

## Tool errors

No hard errors — every command exited 0 and every payload round-tripped through `jq`.
Two **degradations** recorded instead of errors:

1. `fz quote MU --agent` → returns **14 of the documented 84** fundamental fields.
   `.fundamentals."Shs Float"`, `."Short Float"`, `."Shs Outstand"`, `.Price` all resolve
   to `null`. Reproduced on a second call, so this is a persistent upstream/parse
   degradation, not a transient miss. **Mitigation:** float/SI/price sourced from
   `fz screen --view ownership` instead (values above). Phase-7c must NOT read SI from
   `fz quote` this run.
2. `fz screen --tickers MU --view ownership --agent` returns `"Ticker":"MMU"` — a mangled
   ticker string (leading char duplicated). Every other field on the row matches MU's
   `fz quote` Market Cap (926.70B) exactly, so the row is MU's; the `Ticker` field itself
   is not trustworthy this run. Do not key any downstream join on it.

## DATA NOTE / CORRECTION

First read stood for all `uw` values. The `fz` float snapshot was **re-sourced** after the
primary path failed: `Shs Float` was initially `null` via `fz quote MU --agent`
(`.fundamentals."Shs Float"`), and was re-verified as **1.12B** via
`fz screen --tickers MU --view ownership --agent` (`.[0].Float`). No number in this file was
transcribed from an unparsed buffer.

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake sets no bias)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. **MU closed -8.85% at $820.53 on 61.0M shares (1.17× avg).** Every flow, dark-pool and
     OI read for 2026-07-28 is an *event-day* read. Do not interpret elevated premium or
     print size as "unusual accumulation" without first netting it against the fact that the
     tape was down hard.
  2. **Float = 1.12B shares; 1% of float = 11.2M sh ≈ $9.19B.** Use this to normalize every
     dark-pool block in phase-2 and every OI wall in phase-3 — at an $820 handle, raw notional
     numbers will look enormous and mean less than they appear.
  3. **Data has one 31-day hole (2026-03-27 → 2026-04-27).** Phase-5 percentile and
     lookback windows must be computed on the 64-date post-gap block, or explicitly declared
     as spanning the gap. `fz quote` is degraded to 14 fields — phase-7b/7c must use the
     `fz screen` views, not `fz quote`, for SI/float/analyst data.
- **Open questions:**
  - What caused the -8.85% day — earnings, guidance, a sector/memory-cycle event, or a
    broad-market risk-off session? Phase-6 (regime) and phase-7c (news) must answer this;
    the intake data cannot.
  - Is the 820C/7-29 $26.6M print (vol/OI 950×) a directional bet on a bounce, an event
    hedge, or dealer-facing flow? Phase-1 must classify side/aggressor, not just size.
  - Both prior MU runs (2026-06-23, 2026-06-25) predate the drawdown — phase-0.5 must check
    whether their thesis has already been invalidated.
