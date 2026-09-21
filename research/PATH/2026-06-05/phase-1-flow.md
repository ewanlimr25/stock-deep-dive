# Phase 1 — Options Flow

**Ticker:** PATH
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T10:15:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

PATH's options tape is **mildly bullish under a structurally noisy surface**:
whole-tape bullish vs bearish premium is essentially flat (+$55,591 net on
$4.72M traded), but stripping the 0–1DTE deep-ITM call-spread arb reveals a
modest ask-side call accumulation (+$343k call ask−bid premium, +$1.30M net
delta-notional) concentrated in the **Sep-18 tenor ($10C and $15C)**. PATH has
been in the top sweep names **5 of 5 sessions ($20.63M cumulative sweep
premium) but with `dominant_direction: "mixed"`** — a two-way battle, not a
campaign. Phase-0.5's `BUSY_NAME_NORMAL_DAY` verdict caps this phase at `+`.

## Key signals

- Sep-18 **$10C ask-side sweeps: $472,648** across 64 trades, incl. a 582-lot
  $147,246 single print at 14:28:31Z (10:28 ET) — delta 0.69 ITM
  stock-replacement buying [FLOW:sweeps ask][FLOW:top_premium_trades]
- Sep-18 **$15C ask-side: $253,238** across 188 trades (delta ~0.32 OTM upside
  bet, same tenor) [FLOW:sweeps ask]
- Aug-21 **$10P ask-side: $178,444** across 77 trades — put *buying*, the
  counterweight/hedge [FLOW:sweeps ask]
- **5/5-session sweep persistence, $20,628,866 total premium, direction
  `mixed`** — persistent attention, no directional winner
  [FLOW:sweep_persistence]
- Whole tape near-flat: bullish $2,131,707 vs bearish $2,076,116 (derived
  net_flow **+$55,591**); P/C volume ratio 0.39 [FLOW:insights_deep_dive]

## Detailed findings

### Whole-tape aggregate (read top-N against this)

| Field (`.uw_screener`) | Value |
|---|---|
| call_premium / put_premium | $3,816,349 / $899,432 |
| bullish_premium / bearish_premium | $2,131,707 / $2,076,116 |
| **derived net_flow (bullish−bearish)** | **+$55,591** |
| call_volume / put_volume | 45,372 / 17,735 |
| put_call_ratio | 0.39 |
| iv_rank / implied_move_perc | 40.03 / 2.238% |

The headline P/C 0.39 *looks* call-heavy, but bullish-vs-bearish premium is a
coin flip — much "call volume" is non-directional structure (below). Per
phase-0.5 (`[CTX:] BUSY_NAME_NORMAL_DAY`, self-pctile 64), magnitude is
discounted and this phase's confluence contribution is capped at `+`.

### Sweeps (ask vs bid)

Ask-side ≥$100k (4): Sep-18 $10C $472,648 (64 tr); Sep-18 $15C $253,238
(188 tr); 0DTE 06/05 $5.5C $228,026 (70 tr); Aug-21 $10P $178,444 (77 tr).
Bid-side ≥$100k (2): 0DTE 06/05 $6C $265,468 (8 tr); 0DTE $5.5C $131,730 (15 tr).

**The 0DTE legs pair off**: top-premium-trades shows same-second pairs —
14:29:34Z 240-lot 5.5C **ask** $143,040 + 240-lot 6C **bid** $131,280; then
80-lot 5.5C/6C pairs at 16:37:32Z, 16:56:21Z, 16:56:32Z. That is a deep-ITM
$5.5/$6 call spread traded repeatedly (both strikes ~50% ITM vs spot ~$11.24,
deltas 0.94–0.98 [FLOW:greek_screener]) — **exercise/borrow-related structure,
not directional intent**. With short float at 31.15% (phase-0-intake.md
§Finviz), deep-ITM calls are a classic hard-to-borrow workaround; phase 2/3
should look for the matching stock prints.

### New positioning (vol ≫ OI)

| Contract | vol | OI | vol/OI | premium |
|---|---|---|---|---|
| 06/12 $5.5C | 213 | 2 | 106.5 | $132,028 |
| 06/12 $5C | 212 | 6 | 35.3 | $141,166 |
| 06/05 $6C | 496 | 20 | 24.8 | $265,468 |
| 07/02 $18C | 133 | 14 | 9.5 | $1,485 |
| **06/12 $13C** | **7,161** | **1,272** | **5.6** | **$56,233** |

The 06/12 deep-ITM $5/$5.5C are fresh opens of the same HTB-structure family.
The standout retail-flavoured line: **7,161 lots of the 06/12 $13C for only
$56,233** (≈$0.08/share, +15.7% OTM weekly) — cheap upside teenies, lottery
profile [FLOW:unusual_volume].

### Largest premium prints

Top genuine directional print: 14:28:31Z Sep-18 $10C **ask** 582 lots
$147,246, with same-second adds of 144/132/121/89 lots (≈$270k in one second)
and 94 more at 16:01:08Z [FLOW:top_premium_trades]. Late-day smaller bid-side
prints in Jul $12C / Jun $11C/P and 2027 LEAPs ($15C/$20C, bid, <$19k each) —
minor profit-taking/selling at the edges.

### IV outliers + Greeks

IV-outlier list is entirely the deep-ITM weeklies (06/12 $5C iv 5.70, $5.5C iv
5.43 — quote-width artifacts on ~zero-vega lines, vega ≤0.006
[FLOW:greek_screener]; not a vol signal). Sep $10C delta 0.693 / vega 0.0213,
Sep $15C delta ~0.32 — the real vol-carrying directional lines.

### Aggressor split EX 0–1DTE `[FLOW:aggressor_ex0dte DUCKDB]`

| type | side | trades | contracts | prem $M | Δ-notional $M |
|---|---|---|---|---|---|
| call | ask | 1,723 | 18,851 | 1.498 | +6.37 |
| call | bid | 2,154 | 14,471 | 1.155 | +5.07 |
| call | mid | 642 | 5,114 | 0.367 | +1.75 |
| put | ask | 1,183 | 5,791 | 0.421 | −2.07 |
| put | bid | 1,026 | 6,613 | 0.268 | −2.15 |
| put | mid | 227 | 1,063 | 0.084 | −0.40 |

Ex-0DTE: calls net **+$343k at ask** (+$1.30M delta-notional); puts also net
bought at ask (+$153k — bearish counterweight). DTE buckets
`[FLOW:delta_notional DUCKDB]`: 46–180DTE calls **$1.296M** is the largest
bucket (the Sep cluster), LEAP calls $0.909M, 0–1DTE calls $0.797M (the arb),
puts concentrated 8–45DTE ($0.261M) + 46–180DTE ($0.319M).

### Smart-money / sweep-ratio (market-wide)

No PATH rows in `smart-money-flow` top-10 either direction, nor in
`sweep-ratio` top-15 — **no smart-money flow detected on this date** (per
composition guidance, thresholds not loosened). Day's bullish leaders were
GLD/STM/IWM chains.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw options-flow sweeps --symbol PATH --side ask --min-premium 100000 --top-n 25 --date 2026-06-05 --json` | Sep $10C $472,648 ← `.results[].total_premium` | 4 rows |
| `… sweeps --side bid …` | 0DTE $6C $265,468 ← same | 2 rows |
| `uw options-flow unusual-volume --symbol PATH --min-vol-oi-ratio 3 --top-n 25 --date 2026-06-05 --json` | 06/12 $13C vol 7,161 / OI 1,272 ← `.results[]{total_volume,open_interest}` | 5 rows |
| `uw options-flow top-premium-trades --symbol PATH --top-n 25 --date 2026-06-05 --json` | 582-lot $10C ask $147,246 @14:28:31Z ← `.results[]{premium,size,side}` | 25 rows |
| `uw options-flow iv-outliers --symbol PATH --top-n 15 --date 2026-06-05 --json` | 06/12 $5C iv 5.70 ← `.results[].avg_iv` | 12 rows |
| `uw options-flow greek-screener --symbol PATH --top-n 15 --sort-by premium --date 2026-06-05 --json` | Sep $10C delta 0.693 ← `.results[].avg_delta` | 15 rows |
| `uw hot-chains smart-money-flow --direction bullish/bearish --top-n 10 --min-volume 500 --date 2026-06-05 --json` | no PATH rows ← `select(.option_symbol\|startswith("PATH"))` | top-10 ×2 |
| `uw hot-chains sweep-persistence --days 5 --top-n 20 --symbol PATH --json` (no `--date`, see errors) | sessions_in_top 5, $20,628,866, direction mixed ← `.results[0]` | 1 row |
| `uw hot-chains sweep-ratio --top-n 15 --min-volume 500 --min-sweep-ratio 0.3 --date 2026-06-05 --json` | no PATH rows ← same prefix filter | top-15 |
| `uw insights deep-dive --symbol PATH --date 2026-06-05 --json` | net_flow +$55,591 ← `.uw_screener.bullish_premium - .bearish_premium` (derived) | whole-tape |
| DuckDB §A ex-0DTE aggressor + DTE buckets | call ask−bid +$343k; 46–180DTE calls $1.296M | whole PATH tape |

## Tool errors

- `uw hot-chains sweep-persistence --days 5 --top-n 20 --symbol PATH --date 2026-06-05 --json` →
  `Error: unknown flag: --date` (verbatim). Trailing tool; re-ran without
  `--date`. Safe here: latest available date = 2026-06-05 = as-of
  (phase-0-intake.md §UW availability), so the 5-day trailing window anchors
  correctly. Not as-of-reproducible on future re-runs — noted for calibration.

## DATA NOTE / CORRECTION

- First-pass jq filters for `smart-money-flow`/`sweep-ratio` used
  `.underlying_symbol // .ticker` (returned all-null) — rows actually key on
  `option_symbol`. Re-ran with `select(.option_symbol|startswith("PATH"))`
  before concluding "no PATH rows". No numbers from the bad pass were used.

## Verdict for downstream phases

- **Bias from this phase:** mildly bullish (ex-0DTE ask-side call skew, Sep
  tenor), explicitly two-way — confluence contribution capped at `+` per
  phase-0.5 `BUSY_NAME_NORMAL_DAY`
- **Conviction:** 2/5
- **Three things later phases should remember:**
  1. The only institutional-quality directional print is the **Sep-18 $10C
     ask-side cluster ($472,648, delta 0.69)** + $15C ($253,238); tenor =
     post-Q2-earnings (next earnings 2026-09-03 per phase-0.5) — it spans the
     event.
  2. **Deep-ITM 0DTE/weekly call structure (≈$0.8M premium) is HTB/arb
     mechanics, not direction** — with 31.15% short float, phases 2/3 should
     check borrow-driven distortion in OI and dark-pool prints.
  3. Aug-21 $10P ask-side $178,444 put buying sits against the call case;
     5-day sweep direction is `mixed` — nobody has won this tape yet.
- **Open questions:** Is dark pool confirming the Sep call accumulation with
  block buying (phase 2)? Did the Sep $10C/$15C volume convert to new OI
  (phase 3)?
