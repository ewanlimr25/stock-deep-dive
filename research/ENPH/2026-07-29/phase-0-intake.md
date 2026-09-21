# Phase 0 — Intake

**Ticker:** ENPH
**As-of date:** 2026-07-29
**Output dir:** `/Users/ewan/Development/stock-deep-dive/research/ENPH/2026-07-29`
**Version:** v1 (first run for this date; three prior *dated* runs exist — see Prior versions)
**Generated:** 2026-07-30T00:54:31Z

## Summary

Ticker validated (ENPH — Enphase Energy, Technology / Solar, US-listed, optionable).
Output directory created empty; this is **v1 for 2026-07-29**. The `uw` CLI is reachable
and every dataset (options, darkpool, oi, hotchains, screener) carries data **through
2026-07-29**, so the as-of date requires no back-off. Local parquet snapshot is present
with DuckDB available.

**The single most important intake fact:** ENPH reported **Q2 2026 earnings postmarket
2026-07-28**, one day before this as-of date. The prior complete run
(`research/ENPH/2026-07-27/`) was an explicitly *pre-event, no-position* blueprint
(bias NEUTRAL, confluence 29, `final_size_pct` 0.0, spot_reference 38.01). Today's spot
is **35.07** (`fz` ownership view), i.e. **−7.74% from the 07-27 reference** and
**−3.44% on the session**. This run is therefore a *post-catalyst re-underwrite*, not a
continuation — every phase must treat pre-08-28 flow/OI/GEX as a different regime and
must not inherit the pre-event thesis. Proceeding to phase 0.5.

## UW availability

- `uw historical available-dates --json`: **ok** (exit 0, valid JSON)
- Latest available options date: **2026-07-29**
- Latest available darkpool date: **2026-07-29**
- Latest available oi date: **2026-07-29**
- Latest available hotchains date: **2026-07-29**
- Latest available screener date: **2026-07-29**

> Note: per `memory/uw-available-dates-unsorted.md`, the per-dataset arrays are
> **unsorted**; every latest-date read above used `sort | last`, never `.[-1]`.

## Ticker sanity

- Options activity (`uw options-flow unusual-volume --symbol ENPH --top-n 1 --date 2026-07-29`):
  **non-empty** — `ENPH 2026-08-14 C36`, `total_volume` 111 vs `open_interest` 4
  (`vol_oi_ratio` 27.75), `total_premium` $28,231, `avg_iv` 0.8735, `trade_count` 14.
- Interpretation: options tape is live and the very first row is a fresh-OI
  out-of-the-money call two weeks out at 87% IV — consistent with a post-earnings
  surface. Not thin.
- Source parquet confirmed: `~/Documents/Stocks/All Options/bot-eod-report-2026-07-29.parquet`.

## Local data (escape hatch / gap-awareness)

- `local_data_available`: **yes** · `duckdb_available`: **yes**
- `STOCKS_DIR`: `/Users/ewan/Documents/Stocks`
- Available local dates (76 sessions): 2026-03-13 → 2026-03-27, then 2026-04-27 → 2026-07-29.
  - `2026-03-13, 03-16, 03-17, 03-18, 03-19, 03-20, 03-23, 03-24, 03-25, 03-26, 03-27,`
    `04-27, 04-28, 04-29, 04-30, 05-01, 05-04, 05-05, 05-06, 05-07, 05-08, 05-11, 05-12,`
    `05-13, 05-14, 05-15, 05-18, 05-19, 05-20, 05-21, 05-22, 05-26, 05-27, 05-28, 05-29,`
    `06-01, 06-02, 06-03, 06-04, 06-05, 06-08, 06-09, 06-10, 06-11, 06-12, 06-15, 06-16,`
    `06-17, 06-18, 06-22, 06-23, 06-24, 06-25, 06-26, 06-29, 06-30, 07-01, 07-02, 07-06,`
    `07-07, 07-08, 07-09, 07-10, 07-13, 07-14, 07-15, 07-16, 07-17, 07-20, 07-21, 07-22,`
    `07-23, 07-24, 07-27, 07-28, 07-29`
- **Gap flagged: yes** — one structural gap, **2026-03-27 → 2026-04-27** (~1 month, 21
  missing sessions). Phase 5 must not compute a continuous lookback across that boundary;
  self-history percentiles should be windowed to 2026-04-27→2026-07-29 (**64 sessions**)
  unless a longer window is explicitly gap-annotated. The remaining discontinuities are
  ordinary market holidays (05-25 Memorial Day, 06-19 Juneteenth, 07-03 observed
  Independence Day) and are **not** data gaps.
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't express
  (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: **yes** (v1.0.0, `doctor` → api reachable, auth not required, config ok)
- `Shs Float`: **127.77M** (carried to phase-2/3 for %-of-float normalization)
- Also snapshotted for downstream gates: `Outstanding` 132.13M · `Price` 35.07 ·
  `Change` −3.44% · `Short Float` **17.94%** · `Short Ratio` 3.05 ·
  `Inst Own` 101.05% · `Inst Trans` +2.13% · `Insider Own` 3.06% · `Insider Trans` −3.09% ·
  `Avg Volume` 7.51M · `Volume` 9,508,592 · `Market Cap` 4.62B
- Internal consistency check passed: 4.62B ÷ 132.13M = **$34.97 ≈ Price 35.07** ✔
- **Short Float 17.94% is UP from 17.55% at the 07-27 run** — the short base did not
  cover into the print. Phase 7c owns this; tag `[SENT:short_float fz semi-monthly]`
  (settlement figure, ~2-week lag, so it may not yet reflect 07-28/07-29 activity).
- Note: `fz` supplements SI/float/peer/breadth only (`lib/fz-recipes.md`); every `fz`
  datapoint is downside-only or advisory and never enters the Kelly `p`.

### ⚠ `fz` harness degradation discovered this run (workaround applied)

- `fz quote <T>` is **degraded**: it returns only **14 of the documented 84** fundamentals
  fields (`Book/sh, Cash/sh, Dividend Est., Dividend Ex-Date, Dividend Gr. 3/5Y,
  Dividend TTM, Employees, Enterprise Value, IPO, Income, Index, Market Cap, Payout,
  Sales`). `Shs Float`, `Short Float`, `Price`, `RSI (14)`, `SMA50/200`, `Target Price`,
  `Recom`, `Earnings`, `52W High/Low` all return **null**. Confirmed **not**
  ticker-specific — a control `fz quote AAPL` also returns 14 keys — and not a cache
  artifact (`--no-cache` identical). The `--select 'fundamentals.Short Float'` projection
  path documented in `lib/fz-recipes.md §Field-projection` is therefore also dead this run.
- **Workaround used (validated):** `fz screen --tickers <T> --view ownership --agent`
  serves float / short-float / short-ratio / price / inst-own / insider-own correctly.
  Control-checked across AAPL / ENPH / FSLR — values are distinct per ticker and
  internally consistent (market-cap ÷ shares reproduces price for all three).
- **Second, cosmetic `fz` bug:** the `Ticker` field in the ownership view duplicates its
  first character (`EENPH`, `AAAPL`, `FFSLR`). Values are correctly aligned to the
  requested ticker; only the label is malformed. Do **not** key joins on that field.
- Downstream impact: phase-7b loses the `fz` analyst `Recom`/`Target Price`
  cross-source leg and phase-5/9 lose the `fz` RSI/SMA advisory color unless another
  `fz` view supplies them; both are advisory-only, so no gate is blocked. Phase-7c's SI
  leg is **fully preserved** via the workaround.
- `quote-drift` against the 07-27 run was **not** attempted — with `fz quote` returning
  only 14 fields, any drift diff would be structurally empty and misleading.

## Prior versions

No prior `phase-*.md` exists in `research/ENPH/2026-07-29/` → this run is **v1** and
writes unsuffixed filenames.

Three prior **dated** runs exist for ENPH and are available to phase 0.5 as self-history:

| Run | Completeness | Stance |
|---|---|---|
| `research/ENPH/2026-05-19/` | 11 files, **no** `decision.json`, no 0.5/7b/7c/8b | legacy schema — per `memory/deep-dive-no-decision-json.md`, resolve via phase-9 + phase-10 MD only |
| `research/ENPH/2026-05-22/` | 16 files incl. `decision.json` | full modern chain |
| `research/ENPH/2026-07-27/` | 16 files incl. `decision.json` | full modern chain — **2 sessions ago** |

**Carry-forward from `2026-07-27/decision.json` (context only — must be re-derived, not inherited):**

- `bias` NEUTRAL · `conviction` 0.55 · `confluence_score` **29** · `horizon` 1-4w
- `spot_reference` **38.01** · `recommended_bin` 0.55
- `sizing.final_size_pct` **0.0** — deliberately no directional position into the print
  (`p` 0.556 on `win_rate_n` 9, `payoff_b` 1.49, `raw_kelly` 0.258, then gated to zero)
- `gates`: fundamentals **VETO**, sentiment **VETO**, `crowd_state` CROWDED_SHORT,
  `sector_rotation` adverse, `debate_disconfirmed` **true** — all five downside gates fired
- `levels`: support 35.00 · resistance 42.50 · `gamma_flip` null · `largest_pin` 41.00
- `context`: `unusual_verdict` BUSY_NAME_NORMAL_DAY · `iv_rank` 69.81 · `self_pctile_net_dir` 37.0
- `expected_move.front_expiry_pct` **12.25%** (±$4.65) for the 07-31 expiry

**Catalyst calendar carried from that run — this is the regime break:**

| Date | Event | Status as of 2026-07-29 |
|---|---|---|
| 2026-07-28 | **Q2 2026 earnings postmarket** — consensus $292.2M (−19.6% YoY) / $0.46 (−33.3% YoY); guide $280–310M incl. ~$85M safe-harbor; ~3pp tariff GM hit | **OCCURRED** — outcome must be established in phase 7b, not assumed |
| 2026-07-29 | FOMC statement 14:00 ET (no dot plot) | **TODAY** — the earnings gap trades into the Fed |
| 2026-07-31 | Front-week expiry; positive-gamma island expires, IV crush 170% → ~90% | 2 sessions out |
| 2026-08-21 | Monthly OPEX — 18.64% of total OI; $40 put wall (7,888) / $35 put wall (3,734) | pending; **spot 35.07 now sits ON the $35 put wall** |

**Mandatory instruction to all downstream phases:** the 07-27 blueprint's directional
read is **void**. Spot moved 38.01 → 35.07 through a binary event; open interest, GEX,
skew and the entire dealer surface reset on 07-29. Cite the prior run only for
(a) the pre-event baseline when measuring change, and (b) whether the pre-event
CROWDED_SHORT / rising-SI setup resolved by squeeze or by breakdown. Phase 5 must
additionally note that the post-earnings session makes 07-29 a **statistical outlier
day** — signal win-rates drawn from ordinary sessions transfer with reduced confidence.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw historical available-dates --json` | options/darkpool/oi/hotchains/screener latest = 2026-07-29 ← `to_entries[] .value \| sort \| last` | all 5 datasets |
| `uw options-flow unusual-volume --symbol ENPH --top-n 1 --date 2026-07-29 --json` | `vol_oi_ratio`=27.75, `total_premium`=28231, `avg_iv`=0.8735 ← `.results[0]` | top-1 |
| `ls "$STOCKS_DIR/Stock Screener/" \| sed \| sort` | 76 local dates, gap 2026-03-27→2026-04-27 | dir listing |
| `python3 -c "import duckdb"` | exit 0 → `duckdb_available=yes` | — |
| `fz doctor --agent` | `api`=reachable, `auth`=not required, `config`=ok ← `.api/.auth/.config` | — |
| `fz quote ENPH --agent` | **degraded** — `.fundamentals \| keys \| length` = 14 (expected 84); `."Shs Float"`=null | 1 |
| `fz quote AAPL --agent` (control) | also 14 keys → degradation is global, not ticker-specific | 1 |
| `fz screen --tickers ENPH --view ownership --agent` | `Float`=127.77M, `Short Float`=17.94%, `Short Ratio`=3.05, `Price`=35.07, `Change`=−3.44% ← `.[0]` | 1 |
| `fz screen --tickers AAPL,ENPH,FSLR --view ownership --agent` (control) | distinct, cap÷shares≈price for all 3 → view validated | 3 |
| `jq … research/ENPH/2026-07-27/decision.json` | `confluence_score`=29, `spot_reference`=38.01, `sizing.final_size_pct`=0.0 | 1 |

Every value above round-tripped through `jq` on validated JSON per the JSON-validity gate.

## Tool errors

1. **`fz quote <TICKER>` — silent partial parse (exit 0, valid JSON, missing data).**
   Returns 14/84 `.fundamentals` keys; all short-interest, float, price, technical and
   analyst fields are `null`. Reproduced on ENPH and on an AAPL control, with and without
   `--no-cache`. Exit code is **0**, so this fails *silently* — the documented
   graceful-skip trigger (non-zero exit) does **not** fire. Mitigated via
   `fz screen --view ownership`; no phase is blocked. Recommend a `lib/fz-recipes.md`
   patch (propose-only, per the audit convention).
2. **`fz` ownership-view `Ticker` field first-character duplication** (`EENPH`).
   Cosmetic; values correctly aligned. Do not join on that field.

No `uw` errors. No aborts.

## DATA NOTE / CORRECTION

First read stood for every `uw` value. One correction path inside the `fz` lane:
`Shs Float` and `Short Float` were **initially read as `null`** from
`fz quote ENPH --agent` (`.fundamentals."Shs Float"`). That null was **not** transcribed
as a datapoint — it was diagnosed as harness degradation (confirmed by the AAPL control)
and re-sourced from `fz screen --tickers ENPH --view ownership --agent`, verified against
`jq '.[0].Float'` → **127.77M** and `jq '.[0]."Short Float"'` → **17.94%**, then
cross-checked by the market-cap ÷ shares ≈ price identity.

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake sets no bias by construction)
- **Conviction:** n/a (phase 0 is procedural)
- **Three things later phases should remember:**
  1. **2026-07-29 is D+1 after a binary earnings event (Q2 print postmarket 07-28), and
     FOMC lands 14:00 ET the same day.** Spot 38.01 → **35.07** (−7.74%). All pre-08-28
     positioning data describes a dead regime. Do not inherit the 07-27 NEUTRAL/29
     blueprint — re-derive. Establish the *actual* Q2 outcome vs the $292.2M / $0.46
     consensus in phase 7b before any fundamental judgment.
  2. **Float 127.77M and Short Float 17.94% (up from 17.55% pre-print).** Normalize every
     block/sweep/OI figure as % of the 127.77M float. The pre-event CROWDED_SHORT
     configuration survived the print — phase 7c must determine whether that is now a
     fuel tank or a confirmed-right consensus. Spot 35.07 sits **on** the 08-21 $35 put
     wall (3,734 contracts) and **at** the prior run's stated 35.00 support.
  3. **Two harness constraints.** (a) `fz quote` is degraded to 14/84 fields *with a zero
     exit code* — use `fz screen --view ownership` for float/SI and treat any `fz quote`
     null as suspect, not as data. (b) Local parquet has a **2026-03-27 → 2026-04-27
     gap**; window self-history to the 64 contiguous sessions 2026-04-27→2026-07-29.
- **Open questions phase 0 cannot answer:**
  - Did ENPH beat, miss, or guide down on 07-28, and is the −7.74% move the *whole*
    reaction or a partial one still unwinding? (→ 7b, 5)
  - Is today's tape a genuine post-event repositioning or forced expiry-week noise ahead
    of the 07-31 gamma-island expiry? (→ 1, 3, 4)
  - Did the 17.94% short base add, hold, or begin covering into the gap? (→ 1, 2, 7c)
  - Does 35.07-on-the-$35-put-wall behave as dealer-supported support or as a shelf that
    breaks once 07-31 gamma rolls off? (→ 3, 4)
