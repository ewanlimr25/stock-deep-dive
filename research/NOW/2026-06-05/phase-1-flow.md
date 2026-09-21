# Phase 1 — Options Flow

**Ticker:** NOW
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T12:05:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

NOW's options tape on a hard down day (underlying printed 118.89 at 13:35 UTC
→ 111.70 by 19:20 UTC; close 112.45, see phase-0.5-context.md §Universe) was
**high-premium, two-way, and premium-seller-dominated, with a bearish
undertow**: a 5-session bearish sweep campaign (consistency 1.0, $377.9M
cumulative sweep premium) [FLOW:sweep_persistence], fresh ask-side put buying
in Aug 110P ($7.25M, 306 trades), but the day's single largest print — $20.7M
of deep-ITM Jul-17 135P — hit the **bid** (put selling/closing). Per
phase-0.5's `[CTX:] unusual_verdict = BUSY_NAME_NORMAL_DAY`, this phase's
confluence contribution is **capped at `+`**.

## Key signals

- **5-day bearish sweep campaign**: `dominant_direction="bearish"`,
  `sessions_in_top=5`, `consistency_score=1.0`, `total_sweep_premium`
  $377,864,816 [FLOW:sweep_persistence] — the strongest directional fact on
  the tape.
- **$20.69M bid-side sweep block in 135P 2026-07-17** (8,492 contracts, 455
  trades; largest single print $9.8M / 4,000 lots @ 15:50:50 UTC, delta
  −0.74) [FLOW:sweeps side=bid] — deep-ITM put SOLD/closed into the selloff;
  reads as hedge monetization or opening put-write, not fresh bearishness.
- **Fresh OTM put buying**: 110P 2026-08-21 $7,252,905 ask-side across 306
  trades / 6,125 contracts [FLOW:sweeps side=ask] — sustained, not a single
  block; plus new 109P 6/12 (vol 2,910 vs OI 77, r=38) and 110P 10/16 (vol
  491 vs OI 82) [FLOW:unusual_volume].
- **Whole tape net ≈ flat but seller-dominated ex-0DTE**: calls $22.14M ask
  vs $37.72M bid; puts $20.12M ask vs $37.54M bid
  [FLOW:aggressor_ex0dte DUCKDB] — both wings net sold; net delta-notional
  ≈ −$0.01bn (flat).
- **LEAP tape is call-heavy**: $33.86M LEAP call premium vs $9.20M LEAP puts
  [FLOW:dte_bucket DUCKDB] — long-dated interest concentrated in calls
  (100–200 strikes, 2027–2028 expiries).

## Detailed findings

### Whole-tape aggregate (read top-N against this)

From `insights deep-dive .uw_screener` (executed in phase-0.5-context.md
§Universe, same `--date 2026-06-05`):
- call_premium **$74,064,700** vs put_premium **$77,595,932**
- bullish_premium **$62,496,824** vs bearish_premium **$60,713,788** →
  derived `net_flow` = **+$1,783,036** (no `net_flow` key in this block —
  `lib/uw-json-paths.md`)
- call_volume **126,878** vs put_volume **101,468**; `put_call_ratio` **0.80**
- iv_rank **79.23**, iv30d **0.6693**

A near-flat classified tape on ~$152M total premium — the top prints below
are read against this, not as the tape itself. The put-premium skew
phase-0.5 flagged (universe net call−put pctile 1.3) is **mostly explained by
the single $20.7M ITM put block**, not by broad put accumulation.

### Sweeps (ask vs bid)

Top-25 sweeps ≥$100k per side [FLOW:sweeps]:

| Side | Call prem | Put prem | Read |
|---|---|---|---|
| ask (lifted) | $6,272,484 (7,994 ctr) | $12,498,396 (10,027 ctr) | put buyers 2:1 over call buyers |
| bid (hit) | $12,295,740 (9,771 ctr) | $27,148,658 (14,287 ctr) | heavy selling both wings; puts dominated by 135P block |

Notable ask-side (bought): 110P 8/21 $7.25M (306 trades — campaign-like);
135P 7/17 $2.10M; 200C 6/17/27 $639k; 123C 6/18 $414k (900 lots @ 13:35:49
UTC when underlying was 118.89 — morning call buy that is deeply underwater
by the close).
Notable bid-side (sold): **135P 7/17 $20.69M**; 105P 6/17/27 $2.15M (LEAP put
write, 4 prints ~$536k each at 18:15 UTC); 110P 8/21 $1.38M; 109P 6/12 $529k
(2,520 ctr).

### New positioning (unusual volume, vol/OI ≥3)

[FLOW:unusual_volume] — 25 contracts. Highlights (vol vs OI):
- 109P 6/12: $622,451 prem, vol 2,910, OI 77 (r=38) — new weekly put line,
  mostly bid-side per sweeps (sold).
- 110P 10/16: $702,759, vol 491, OI 82 (r=6) — new Oct put, bid-side $686k
  (sold).
- 112/115/116P 7/02: ~$960k combined, ask-side per sweeps (bought) — fresh
  early-July put protection.
- 116C/117C 6/05 (0DTE, expired worthless or scalped): $413k combined,
  vol 6,888 — pin noise, discounted.
- 65P 6/12: vol 17,030 vs OI 22 (r=774!) but only $68,150 premium — 42%-OTM
  weekly lottery/disaster hedges at avg_iv 1.63; size noise, premium trivial.
- 216P 6/18: $2,437,380, vol 236 vs OI 45 — deep-ITM (≈2× spot), see below.

### Largest premium prints

[FLOW:top_premium_trades] top rows (times UTC; underlying price at print
shows the intraday slide 118.89 → 111.70):

| Time | Contract | Side | Premium | Size | Δ | IV |
|---|---|---|---|---|---|---|
| 15:50:50 | 135P 7/17 | **bid** | $9,800,000 | 4,000 | −0.74 | 0.66 |
| 17:43:55 | 120P 9/18 | no_side | $2,865,000 | 1,500 | −0.49 | 0.64 |
| 17:43:55 | 120C 9/18 | no_side | $2,145,000 | 1,500 | +0.52 | 0.69 |
| 19:20:38 | 220P 6/18 | no_side | $1,255,520 | 118 | −0.97 | 1.77 |
| 19:20:38 | 216P 6/18 | no_side | $1,208,320 | 118 | −0.96 | 1.80 |
| 14:54:48 | 110P 10/16 | bid | $686,400 | 480 | −0.37 | 0.63 |
| 18:23:23 | 110P 8/21 | bid | $596,000 | 500 | −0.41 | 0.65 |
| 18:15:24× 4 | 105P 6/17/27 | bid | ~$2.15M tot | ~997 | −0.33 | 0.59 |
| 13:35:49 | 123C 6/18 | ask | $405,000 | 900 | +0.42 | 0.70 |

Structural/non-directional prints to NOT read as bets: the 120P+120C 9/18
pair (same second, same size — a 1,500-lot straddle/combo, no_side); the
216/220P 6/18 deep-ITM prints (|Δ|≈0.96–0.97, IV 1.8 — synthetic
stock/crossing mechanics, $4.4M+ combined premium but near-zero optionality).

### IV outliers + Greeks

[FLOW:iv_outliers] concentrated in (a) the deep-ITM 216/220P 6/18 (avg_iv
1.80–1.82 — artifact of ITM quoting), (b) 42%-OTM 65P 6/12 (1.63), (c)
160/165P 6/18 (~1.26–1.29, $460k+$261k real premium — tail hedges).
[FLOW:greek_screener] top-premium rows mirror the table above; the 135P
block carries vega 0.13/contract — its sale is also a short-vol expression
at iv_rank 79.

### Aggressor split ex-0/1DTE + DTE buckets (escape hatch)

Run because top-N and aggregate disagreed (`lib/duckdb-cuts.md §A`):

| type | ask | bid | mid | net (ask−bid) |
|---|---|---|---|---|
| call | $22.14M | $37.72M | $9.56M | **−$15.58M (net sold)** |
| put | $20.12M | $37.54M | $6.44M | **−$17.42M (net sold)** |

[FLOW:aggressor_ex0dte DUCKDB] Both wings net SOLD — consistent with
harvesting iv_rank 79 premium. Ex the single 135P block (~$20.7M bid), puts
flip to net BOUGHT ≈ +$3.3M — the block is the whole put-skew story.
Delta-notional: call +0.35bn gross vs put −0.28bn gross; netting ask−bid by
side ≈ **−$0.01bn → directionally flat tape in delta terms**.

| DTE bucket | call prem | put prem |
|---|---|---|
| 0-1DTE | $2.51M | $5.67M |
| 2-7DTE | $3.92M | $4.41M |
| 8-45DTE | $17.49M | **$38.77M** (≈$23M = the 135P line) |
| 46-180DTE | $16.29M | $19.55M |
| LEAP | **$33.86M** | $9.20M |

[FLOW:dte_bucket DUCKDB] Tradeable-window (8–45DTE) put dominance is
block-driven; LEAP activity is 3.7:1 call-heavy.

### Smart-money / sweep-ratio (market-wide)

No NOW rows in `smart-money-flow` top-10 bullish (GLD/STM/IWM lead) or
bearish (GLD/EEM/IWM puts lead), nor in `sweep-ratio` top-15
(OKLO/CVNA/TSLA) [FLOW:smart_money_flow, FLOW:sweep_ratio] — no
smart-money flow detected on this date; NOW's aggression is persistent
rather than top-of-tape today.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw options-flow sweeps --symbol NOW --side ask --min-premium 100000 --top-n 25 --date 2026-06-05 --json` | call $6,272,484 / put $12,498,396 ← `.results \| group_by(.option_type) \| map(map(.total_premium)\|add)` | top-25 |
| `uw options-flow sweeps --side bid …` | call $12,295,740 / put $27,148,658; 135P 7/17 $20,691,153 ← same + `.results[0]` | top-25 |
| `uw options-flow unusual-volume --symbol NOW --min-vol-oi-ratio 3 --top-n 25 --date 2026-06-05 --json` | 109P 6/12 vol 2,910/OI 77 ← `.results[]` | top-25 |
| `uw options-flow top-premium-trades --symbol NOW --top-n 25 --date 2026-06-05 --json` | 135P $9.8M bid @15:50:50 ← `.results[0]` | top-25 |
| `uw options-flow iv-outliers --symbol NOW --top-n 15 --date 2026-06-05 --json` | 220P 6/18 avg_iv 1.82 ← `.results[0]` | top-15 |
| `uw options-flow greek-screener --symbol NOW --top-n 15 --sort-by premium --date 2026-06-05 --json` | 135P vega 0.13 ← `.results[0].vega` | top-15 |
| `uw hot-chains smart-money-flow --direction bullish/bearish --top-n 10 --min-volume 500 --date 2026-06-05 --json` | NOW absent ← `select(.option_symbol \| test("^NOW[0-9]"))` → [] | top-10 ×2 |
| `uw hot-chains sweep-persistence --days 5 --top-n 20 --symbol NOW --json` (no `--date` — see Tool errors) | bearish / 5 sessions / 1.0 / $377,864,816 ← `.results[0]` | 1 row |
| `uw hot-chains sweep-ratio --top-n 15 --min-volume 500 --min-sweep-ratio 0.3 --date 2026-06-05 --json` | NOW absent ← option_symbol filter → [] | top-15 |
| DuckDB §A (`lib/duckdb-cuts.md`) | aggressor ex-0DTE + DTE buckets (tables above) | whole NOW tape |
| (reused) `uw insights deep-dive --symbol NOW --date 2026-06-05` | aggregate block — executed in phase-0.5, values quoted verbatim | per-name |

## Tool errors

- `uw hot-chains sweep-persistence --days 5 --top-n 20 --symbol NOW --date 2026-06-05 --json` →
  `Error: unknown flag: --date`. Trailing tool, latest-anchored (memory:
  trailing tools take no `--date`). Re-run without the flag; **latest
  available date = 2026-06-05 = as-of** (phase-0-intake.md §UW availability),
  so the 5-day window ends exactly at as-of — output is as-of-correct.

## DATA NOTE / CORRECTION

First `jq` filter for hot-chains used `underlying_symbol//ticker//symbol`,
which don't exist in those results (rows key on `option_symbol`); re-filtered
with `test("^NOW[0-9]")` on the saved JSON — same empty result for NOW,
verified against `keys0`. No numeric value changed.

## Verdict for downstream phases

- **Bias from this phase:** mixed, bearish-leaning (persistent bearish
  sweeps + fresh Aug put buys + −6% intraday tape, against block-driven put
  selling and flat net delta)
- **Conviction:** 2 / 5 (capped at `+` by `[CTX:] BUSY_NAME_NORMAL_DAY`,
  phase-0.5-context.md §Verdict)
- **Three datapoints later phases must remember:**
  1. `sweep_persistence`: bearish 5/5 sessions, $377.9M — does dark pool
     (phase 2) and OI build (phase 3) confirm a campaign?
  2. The $20.7M bid-side 135P 7/17 block — phase 3 must check whether 135P
     OI *fell* (closing → hedge monetization, contrarian-bullish) or *rose*
     (opening put-write).
  3. Both wings net-sold ex-0DTE at iv_rank 79 [FLOW:aggressor_ex0dte
     DUCKDB] — vol is being supplied; phase 4/5 should read GEX/VRP in that
     light.
- **Open questions:** Is dark pool confirming distribution on the −6% day?
  Did 110P 8/21 OI rise (fresh hedging) — and at which strikes are the put
  walls (phase 3)?
