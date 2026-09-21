# Phase 1 — Options Flow

**Ticker:** RKT
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T17:00:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

RKT's 2026-06-05 options tape is **mixed with a near-term bearish tilt and a
long-dated bullish undertow**. The whole-tape aggregate nets slightly bearish
(derived net_flow **−$209,751** on $3.24M total premium) despite call-heavy volume
(P/C 0.46), and the ex-0DTE aggressor split confirms it: calls were net-sold and
puts net-bought. Against that, the single cleanest institutional print is a
$257,910 ask-side sweep campaign in the Jan-2027 $9.2 deep-ITM calls
(stock-replacement), while the day's largest single print is an opening **sale**
of 3,459 Jul-10 $14.5 calls. Sweep activity is persistent (5/5 sessions) but
directionally mixed — no campaign. Per phase-0.5-context.md `[CTX:]`
`unusual_verdict = BUSY_NAME_NORMAL_DAY`, this phase's confluence contribution is
capped at `+`.

## Key signals

- Whole-tape: bullish_premium 1,256,315 vs bearish_premium 1,466,066 → derived
  net_flow **−$209,751**; call_volume 32,206 vs put_volume 14,951, put_call_ratio
  0.46 [FLOW:insights_deep_dive]
- Largest print of the day is a **sale**: Jul-10 $14.5C, 3,459 contracts @ $0.32
  = $110,688 at the **bid**, 2 trades, vol/OI 1,153 (OI=3 → opening) — someone
  capping upside above $14.5 into mid-July [FLOW:top_premium_trades +
  unusual_volume]
- Cleanest bullish print: Jan-2027 $9.2C swept at **ask** — total_premium
  $257,910, 543 contracts, 15 trades, avg_price 4.748, delta 0.816 — deep-ITM
  LEAP stock-replacement buying [FLOW:sweeps --side ask]
- Jun-18 $14P bought at ask $108,377 — but 797 contracts across **701 trades**
  (~1.1/trade): small-lot, retail-quality bearish flow [FLOW:sweeps --side ask]
- Ex-0-1DTE aggressor: calls 8,042 ask vs **12,773 bid** contracts ($0.74M vs
  $0.77M); puts **7,706 ask** vs 3,119 bid ($0.58M vs $0.38M) → customer-signed
  net ≈ −$0.23M, both legs lean bearish [FLOW:aggressor_ex0dte DUCKDB]
- Sweep persistence: `sessions_in_top` 5/5, `dominant_direction` **"mixed"**,
  total_sweep_premium $2,646,472 [FLOW:sweep_persistence]

## Detailed findings

### Whole-tape aggregate (read top-N against this)

| Field (`.uw_screener`) | Value |
|---|---|
| call_premium / put_premium | 1,912,369 / 1,332,438 |
| bullish_premium / bearish_premium | 1,256,315 / 1,466,066 |
| **derived net_flow** (bullish − bearish; no `net_flow` key in block) | **−209,751** |
| call_volume / put_volume | 32,206 / 14,951 |
| put_call_ratio | 0.46 |
| iv_rank / implied_move_perc | 29.9622 / 0.0119843 |

Volume skews 2.2:1 to calls but premium-aggressor nets bearish → much of the call
volume is selling or low-priced short-dated tape, resolved by the DuckDB cut below.
Underlying drifted **down all session**: prints show underlying_price ≈12.98 in the
morning → 12.505 by 19:11Z (15:11 ET); screener close $12.65
(phase-0.5-context.md §Sector read).

### Sweeps (ask vs bid)

| Side | Chain | total_premium | size | trades | Read |
|---|---|---|---|---|---|
| ask | **2027-01-15 $9.2C** | $257,910 | 543 | 15 | deep-ITM LEAP buy campaign — bullish, institutional, slow |
| ask | 2026-06-18 $14P | $108,377 | 797 | 701 | ITM put buying, ~1.1 contracts/trade → small-lot/retail quality |
| bid | **2026-07-10 $14.5C** | $110,720 | 3,460 | 2 | block call **sale** (matches unusual-volume #1) — bearish/cap |

### New positioning (unusual volume, vol/OI ≥ 3 — 11 chains)

| Chain | vol | OI | vol/OI | prem | Note |
|---|---|---|---|---|---|
| Jul-10 $14.5C | 3,460 | 3 | **1,153** | $110,720 | the bid-side sale — opening short call |
| Jul-24 $13C | 234 | 1 | 234 | $24,368 | |
| Jun-12 $12C | 435 | 2 | 217.5 | $39,160 | |
| Jun-12 $12.5C | 947 | 35 | 27.1 | $47,204 | |
| Jun-12 $13C | 2,046 | 155 | 13.2 | $83,379 | weekly call activity above spot |
| Jun-5 $13C (0DTE) | 6,496 | 1,148 | 5.7 | $37,490 | 0DTE pin noise — discounted |
| Jun-18 $12.5C | 1,106 | 260 | 4.3 | $66,897 | |
| Jul-17 $10P | 985 | 235 | 4.2 | $17,729 | cheap OTM put lotto/hedge |
| Jun-26 $15P | 340 | 102 | 3.3 | $86,578 | ITM put, 321 trades — small-lot |
| Jun-18 $12.5P | 1,157 | 383 | 3.0 | $64,761 | |

Fresh positioning is two-sided: weekly 12–13 calls opening against ITM put buys
and the big 14.5C short.

### Largest premium prints (top-premium-trades, top 10 of 25)

| Time (UTC) | Chain | Side | Size | Premium | Delta |
|---|---|---|---|---|---|
| 19:11:01 | Jul-10 $14.5C | **bid** | 3,459 | $110,688 | +0.25 |
| 15:51:28 | Jan-27 $9.2C | ask | 200 | $95,000 | +0.82 |
| 15:51:28 | Jan-27 $9.2C | ask | 200 | $95,000 | +0.82 (two same-second prints; sweeps tool aggregates chain to $257,910) |
| 15:45:36 | Aug-21 $14C | **bid** | 500 | $57,000 | +0.45 |
| 15:46:12 | Aug-21 $14C | mid | 500 | $56,500 | +0.45 |
| 16:10:46 | Aug-21 $15C | ask | 500 | $42,500 | +0.37 |
| 16:09:43 | Aug-21 $15C | mid | 500 | $42,500 | +0.37 |
| 17:33:13 | Jun-18 $16P | mid | 100 | $33,500 | −0.95 (deep-ITM, likely close/roll) |
| 13:58:25 | Jan-28 $15C | bid | 84 | $30,324 | +0.60 |
| 16:32:26 | Jan-27 $12.2C | mid | 100 | $29,500 | +0.64 |

The Aug-21 500×500 pairs (sell $14C bid / buy $15C ask, ~25 min apart) read like a
**roll up** or call-spread adjustment — premium-neutral-ish, mildly bullish term
but reduces nearer-the-money upside exposure.

### IV outliers + Greeks

All 13 IV-outlier rows are **0DTE (2026-06-05 expiry)** with avg_iv 1.3–7.3 —
expiry-day noise, tagged and discounted per pitfall guidance. Greek-screener
(sort-by premium) replicates the top-premium table; notable: Jul-10 $14.5C gamma
0.133 / theta −0.011 — short-gamma supply at $14.5; Jun-12 $13P/$13C 500×500 at
15:30:49 both at **ask** (long straddle-ish weekly vol buy, $44k combined).

### DuckDB §A — aggressor ex-0-1DTE + DTE buckets [FLOW:… DUCKDB]

| type | side | trades | contracts | prem $M | δ-notional $bn |
|---|---|---|---|---|---|
| call | ask | 652 | 8,042 | 0.74 | 0.004 |
| call | **bid** | 924 | **12,773** | 0.77 | 0.005 |
| call | mid | 229 | 3,002 | 0.30 | 0.002 |
| put | **ask** | 1,976 | **7,706** | 0.58 | −0.005 |
| put | bid | 1,996 | 3,119 | 0.38 | −0.003 |
| put | mid | 540 | 1,253 | 0.15 | −0.001 |

Customer-signed net ≈ (0.74−0.77) + (0.38−0.58) = **−$0.23M** — confirms the
aggregate's bearish tilt is real, not 0DTE artifact.

| DTE bucket | call prem $M | put prem $M |
|---|---|---|
| 0-1DTE | 0.08 | 0.20 |
| 2-7DTE | 0.20 | 0.37 |
| 8-45DTE | 0.41 | **0.61** |
| 46-180DTE | **0.54** | 0.04 |
| LEAP | **0.69** | 0.11 |

Tenor structure: **short-dated tape is put-heavy; 46+ DTE is overwhelmingly
call-side** ($1.23M vs $0.15M). Bearish now, bullish later.

### Smart money / sweep-ratio boards

- `smart-money-flow` top-10 bullish and bearish (market-wide): **no RKT chains**
  — no smart-money flow detected on this date (thresholds not loosened per
  composition guidance).
- `sweep-ratio` top-15: no RKT.
- `sweep-persistence --days 5`: ticker RKT, `sessions_in_top` **5**,
  `dominant_direction` **"mixed"**, `consistency_score` 1, total_sweep_premium
  **$2,646,472** — persistently active, directionally incoherent.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw options-flow sweeps --symbol RKT --side ask --min-premium 100000 --top-n 25 --date 2026-06-05 --json` | 9.2C $257,910; 14P $108,377 ← `.results[]` | 2 |
| `uw options-flow sweeps --symbol RKT --side bid …` | 14.5C $110,720 ← `.results[0]` | 1 |
| `uw options-flow unusual-volume --symbol RKT --min-vol-oi-ratio 3 --top-n 25 --date 2026-06-05 --json` | 11 chains ← `.results[]` | 11 |
| `uw options-flow top-premium-trades --symbol RKT --top-n 25 --date 2026-06-05 --json` | top prints ← `.results[]` | 25 |
| `uw options-flow iv-outliers --symbol RKT --top-n 15 --date 2026-06-05 --json` | all 0DTE ← `.results[].expiry` | 13 |
| `uw options-flow greek-screener --symbol RKT --top-n 15 --sort-by premium --date 2026-06-05 --json` | gamma/theta ← `.results[]` | 15 |
| `uw hot-chains smart-money-flow --direction bullish/bearish --top-n 10 --min-volume 500 --date 2026-06-05 --json` | no RKT ← `.results[] \| select(.option_symbol \| test("^RKT[0-9]"))` | 0 |
| `uw hot-chains sweep-persistence --days 5 --top-n 20 --symbol RKT --json` (no `--date`; latest-anchored = 2026-06-05) | mixed, $2,646,472 ← `.results[0]` | 1 |
| `uw hot-chains sweep-ratio --top-n 15 --min-volume 500 --min-sweep-ratio 0.3 --date 2026-06-05 --json` | no RKT ← same filter | 0 |
| `uw insights deep-dive --symbol RKT --date 2026-06-05 --json` | aggregate ← `.uw_screener.*`, net derived | whole-tape |
| DuckDB §A (`lib/duckdb-cuts.md`) on `bot-eod-report-2026-06-05.parquet` | aggressor ex-0DTE, DTE buckets | whole-tape |

## Tool errors

- `uw hot-chains sweep-persistence --days 5 --top-n 20 --symbol RKT --date 2026-06-05 --json` →
  `Error: unknown flag: --date` / `error: unknown flag: --date`.
  Re-ran without `--date` (tool is latest-anchored; latest dataset date =
  2026-06-05 = as-of per phase-0-intake.md, so the 5-day window ends on the as-of
  date and the read is valid).
- First-pass `jq` filter on `smart-money-flow`/`sweep-ratio` used a `ticker` field
  that doesn't exist (keys are `option_symbol`-based); re-ran with
  `test("^RKT[0-9]")`. No data was transcribed from the bad filter.

## DATA NOTE / CORRECTION

None — values above are from the corrected re-runs; nothing was written from the
failed first-pass filters.

## Verdict for downstream phases

- **Bias from this phase:** mixed — near-term bearish tilt (net −$210k, calls
  net-sold/puts net-bought ex-0DTE, biggest print an opening call sale), long-term
  bullish undertow (LEAP/46-180DTE call buying $1.23M incl. the $9.2C
  stock-replacement sweep)
- **Conviction:** 2/5 (magnitudes modest; `[CTX:]` BUSY_NAME_NORMAL_DAY caps
  phases 1–2 at `+` regardless — phase-0.5-context.md)
- **Three datapoints later phases must remember:**
  1. Jul-10 $14.5C opening **short** 3,459× ($110,688 at bid, vol/OI 1,153) —
     watch whether OI confirms tomorrow; defines a $14.5 upside cap [FLOW].
  2. Jan-2027 $9.2C ask-side sweep $257,910 (delta 0.82) — institutional
     stock-replacement; bullish on a 6-12 month tenor, not tradeable
     short-term [FLOW].
  3. Tenor split: ≤45DTE premium is put-dominant ($1.18M put vs $0.69M call),
     46DTE+ is call-dominant ($1.23M vs $0.15M) [FLOW:DUCKDB].
- **Open questions:** Is dark pool confirming the bearish near-term tilt
  (phase 2)? Does OI at $14.5/$12.5 corroborate the new positioning (phase 3)?
  Was the intraday slide (12.98→12.51) flow-led or market-led
  (phase-0.5 risk-off tape)?
