# Phase 1 — Options Flow

**Ticker:** NBIS
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T19:55:00-0400
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

NBIS printed a 99.6th-percentile-of-universe premium day ($460M gross — see
phase-0.5-context.md `[CTX:]`) that is **structurally two-way, not directional**:
derived whole-tape net_flow is only **−$9.6M** (bullish_premium $195.1M −
bearish_premium $204.7M) and the ex-0DTE customer delta-notional nets to
**≈ $0.0bn**. The tape is dominated by deep-ITM put calendars/rolls (a 2,000×2,000
285P Jun-05→Jun-26 roll, ~$26M both legs at 15:10 ET) and deep-ITM Jan-27 50C
stock-replacement blocks (~$34M two-way) — financing mechanics, not bets. The
genuinely directional residue is **bearish**: `sweep-persistence` has NBIS as a
top sweep name **5/5 consecutive sessions, dominant_direction "bearish",
consistency_score 1.0, $643.6M cumulative sweep premium**, and the stock fell
intraday from $240.29 (10:52 ET) to ~$217.40 (14:49 ET) on the day while OTM
June puts (215P/200P/190P) were bought at ask.

## Key signals

- **5-day bearish sweep campaign**: sessions_in_top=5, dominant_direction=bearish,
  consistency_score=1.0, total_sweep_premium=$643,611,015 `[FLOW:sweep_persistence]`
- Whole-tape derived net_flow = 195,086,472 − 204,689,185 = **−$9,602,713** on
  $460.1M gross; P/C 0.97 — near-balanced `[FLOW:insights_deep_dive]`
- **Jun-26 285P fresh open**: 7,006 vol on OI 6 (vol/OI 1167.7×), $49.3M premium —
  but net **sold**: $31.0M at bid vs $7.1M at ask → deep-ITM put *writing*
  (synthetic-long / financing leg), not crash protection `[FLOW:unusual_volume]`,
  `[FLOW:sweeps]`
- **Ex-0/1DTE aggressor split**: calls net SOLD (ask $78.1M vs bid $107.5M),
  puts net SOLD (ask $47.7M vs bid $86.2M); customer delta-notional ≈ +0.265
  −0.365 −0.195 +0.295 = **+0.000bn — flat** `[FLOW:aggressor_ex0dte DUCKDB]`,
  `[FLOW:delta_notional DUCKDB]`
- One clean institutional outlier: **Jan-27 310C, 1,550× $9.84M at mid
  (no_side), IV 1.137, delta 0.564** printed 10:52 ET with stock at $240.29 —
  a long-vega upside structure put on *before* the intraday slide
  `[FLOW:top_premium_trades]`
- Intraday underlying path off the prints: $240.29 (14:52Z) → $219.89 (18:21Z) →
  $217.39 (18:49Z) → $222.58 (19:10Z); screener close $227.81 — a violent
  down-then-recover session `[FLOW:greek_screener]`

## Detailed findings

### Whole-tape aggregate (read the top-N against this)

`[FLOW:insights_deep_dive]` — `.uw_screener`:

| Field | Value |
|---|---|
| call_premium / put_premium | $223,213,183 / $236,887,376 |
| bullish_premium / bearish_premium | $195,086,472 / $204,689,185 |
| **derived net_flow** | **−$9,602,713** (= bullish − bearish; no `net_flow` key in this block) |
| call_volume / put_volume | 138,427 / 134,702 |
| put_call_ratio | 0.97 |
| iv_rank / iv30d | 89.97 / 1.117 |
| total_open_interest | 1,117,357 |

`[CTX:]` carry: unusual_verdict = GENUINELY_UNUSUAL (bearish-tilted; net ~2.6% of
gross). No BUSY_NAME_NORMAL_DAY cap applies, but the gross-vs-net gap itself
caps directional conviction from magnitude alone.

### Sweeps (ask vs bid)

Top ask-side (aggressive buys), min $100k `[FLOW:sweeps side=ask]`:

| Contract | Premium | Size | Trades | Read |
|---|---|---|---|---|
| Jun-05 285P (0DTE, deep ITM) | $20,439,318 | 3,223 | 56 | roll leg (see below) |
| Jan-27 50C (deep ITM, Δ≈0.98) | $15,106,310 | 878 | 41 | stock-replacement two-way |
| Jun-05 272.5P (0DTE) | $7,761,588 | 1,529 | 20 | ITM put roll/exercise mech. |
| Jun-26 285P | $7,134,604 | 1,006 | 45 | smaller ask leg of the line |
| **Jun-12 215P (OTM)** | **$3,621,942** | 3,236 | 134 | genuine downside buying |
| Jun-12 200P (OTM) | $815,791 | 1,410 | 379 | genuine downside buying |

Top bid-side (aggressive sells) `[FLOW:sweeps side=bid]`:

| Contract | Premium | Size | Trades | Read |
|---|---|---|---|---|
| **Jun-26 285P** | **$31,049,050** | 4,431 | 56 | deep-ITM put WRITE (synthetic long / financing) |
| Jan-27 50C | $19,062,700 | 1,115 | 24 | deep-ITM call unwind |
| Jun-05 285P (0DTE) | $16,657,352 | 2,515 | 51 | roll counter-leg |
| Jun-26 270P | $8,488,280 | 1,501 | 16 | ITM put write |
| Jul-17 300C / 320C | $4.81M / $2.99M | 3,099 / 2,449 | 319/193 | OTM call overwriting |

**The 285P roll (15:10:33 ET, 2,000 × 2,000):** bought Jun-05 285P at ask
($62.94, Δ −0.956) and sold Jun-26 285P at bid ($68.41, Δ −0.793) in the same
second, spot $222.58 `[FLOW:top_premium_trades]` `[FLOW:greek_screener]`. Net
position delta ≈ −0.16 × 2,000 — modest. Extrinsic collected on the Jun-26 leg
≈ $6/contract (~$1.2M). This is calendar/financing mechanics (consistent with
maintaining a synthetic-long or conversion book), **not** outright bearish intent —
even though premium classifiers will count both legs in put premium.

### New positioning (vol ≫ OI) `[FLOW:unusual_volume]`

- Jun-26 285P: 7,006 vol / 6 OI = **1167.7×** — fresh line, net sold (above).
  Phase 3 must confirm Monday's OI print.
- Jun-05 0DTE calls 222.5–250 strikes: 4 of the top-10 vol/OI lines (e.g. 232.5C
  67.1×, 6,306 vol; 240C 11.3×, 9,940 vol) — intraday scalp tape, discounted.
- Jun-12 215P: 5,062 vol / 429 OI = 11.8×, $5.66M total — **fresh OTM put
  opening**, the cleanest new bearish line.
- Jun-12 240C: 2,346 vol / 191 OI = 12.3×, $2.49M — dip-buying calls also opening.

### Largest premium prints `[FLOW:top_premium_trades]`

| Time (UTC) | Contract | Prem | Size | Side | Spot | Read |
|---|---|---|---|---|---|---|
| 19:10:33 | Jun-26 285P | $13.68M | 2,000 | bid | 222.58 | roll: write 21-DTE leg |
| 19:10:33 | Jun-05 285P | $12.59M | 2,000 | ask | 222.58 | roll: buy 0DTE leg |
| 14:52:15 | **Jan-27 310C** | **$9.84M** | 1,550 | no_side | **240.29** | long-vega upside, pre-slide |
| 18:39:39–41 | Jun-26/Jun-05 285P pairs | ~$3.5–3.9M ×6 | 286–546 | bid/mid | ~219 | same roll, earlier clips |
| 18:21:06 | Jun-26 265P / Jun-05 265P | $3.26M bid / $2.75M ask | 600 | — | 219.89 | same structure, 265 line |
| 18:51:17 | Jun-18 190P | $3.16M | 3,700 | no_side | 217.50 | OTM put block at the lows |
| 18:49 | Jan-27 50C ×4 clips | $2.4–3.0M | 143–176 | bid | ~217.4 | deep-ITM call selling |

### IV outliers + Greeks

- IV outliers are concentrated in **deep-OTM far puts** (Jun-18 33P–50P at
  315–441% IV) but with trivial premium ($0.4–2.3k) `[FLOW:iv_outliers]`.
  Notable volume in cheap crash strikes: Jun-12 125P traded 3,238 contracts
  ($40.7k) and Jun-18 100P 1,295 contracts ($27.0k) — lottery-sized tail hedges,
  wide participation but no capital conviction.
- Greeks confirm the structural reads: Jan-27 50C Δ 0.973–0.976 (pure stock
  proxy); Jun-26 285P Δ −0.79; the Jan-27 310C carries vega 0.74/contract —
  the largest clean vega-buy on the tape `[FLOW:greek_screener]`.

### Aggressor split ex-0/1DTE `[FLOW:aggressor_ex0dte DUCKDB]`

| Type | Side | Trades | Contracts | Prem $M | Δ-notional $bn |
|---|---|---|---|---|---|
| call | ask | 7,518 | 29,833 | 78.08 | +0.265 |
| call | bid | 10,859 | 40,134 | 107.45 | −0.365 (customer sells) |
| put | ask | 8,125 | 35,808 | 47.71 | −0.195 |
| put | bid | 6,695 | 40,963 | 86.21 | +0.295 (customer sells) |

Net customer delta ≈ **0.000bn** — flat. Calls net sold (−$29.4M at-ask-minus-
at-bid), puts net sold (−$38.5M) — premium harvesting on a 90 IV-rank name from
both sides.

DTE buckets (premium $M): 0-1DTE puts **80.0** (roll legs + pin), 8-45DTE puts
**102.2** (the 285/270/265 complex + 215P), LEAP calls **102.5** (50C two-way +
310C), 8-45DTE calls 64.1 `[FLOW: DUCKDB]`.

### Smart-money / sweep-ratio screens

- `smart-money-flow` top-10 (bullish and bearish): **no NBIS rows** on this date
  (leaders: GLD, STM, IWM / GLD, EEM, IWM, NVDA). No smart-money ask/bid
  imbalance detected at screen thresholds. `[FLOW:smart_money_flow]`
- `sweep-ratio` top-15 (≥0.3, vol ≥500): no NBIS contracts. `[FLOW:sweep_ratio]`

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw options-flow sweeps --symbol NBIS --side ask --min-premium 100000 --top-n 25 --date 2026-06-05 --json` | top line Jun-05 285P $20,439,318 ← `.results[0].total_premium` | top-25 |
| `uw options-flow sweeps --symbol NBIS --side bid …` | top line Jun-26 285P $31,049,050 ← `.results[0].total_premium` | top-25 |
| `uw options-flow unusual-volume --symbol NBIS --min-vol-oi-ratio 3 --top-n 25 --date 2026-06-05 --json` | Jun-26 285P vol_oi_ratio 1167.67 ← `.results[0].vol_oi_ratio` | top-25 |
| `uw options-flow top-premium-trades --symbol NBIS --top-n 25 --date 2026-06-05 --json` | 285P roll pair 19:10:33Z; Jan-27 310C $9,842,500 no_side ← `.results[].premium/.side/.executed_at` | top-25 |
| `uw options-flow iv-outliers --symbol NBIS --top-n 15 --date 2026-06-05 --json` | Jun-18 33P avg_iv 3.907 ← `.results[0].avg_iv` | top-15 |
| `uw options-flow greek-screener --symbol NBIS --top-n 15 --sort-by premium --date 2026-06-05 --json` | underlying_price 240.29→217.39; Jan-27 310C delta 0.564, vega 0.741 ← `.results[].underlying_price/.delta/.vega` | top-15 |
| `uw hot-chains smart-money-flow --direction bullish\|bearish --top-n 10 --min-volume 500 --date 2026-06-05 --json` | no NBIS rows ← `.results[] \| select(.option_symbol \| test("^NBIS[0-9]"))` | top-10 ×2 |
| `uw hot-chains sweep-persistence --days 5 --top-n 20 --symbol NBIS --json` (no `--date`; anchors to latest = 2026-06-05) | sessions_in_top 5, dominant_direction "bearish", consistency 1.0, $643,611,015 ← `.results[0]` | 1 row |
| `uw hot-chains sweep-ratio --top-n 15 --min-volume 500 --min-sweep-ratio 0.3 --date 2026-06-05 --json` | no NBIS rows ← same option_symbol filter | top-15 |
| `uw insights deep-dive --symbol NBIS --date 2026-06-05 --json` | aggregate table above ← `.uw_screener.*` | whole-tape |
| DuckDB §A (`lib/duckdb-cuts.md`) | aggressor ex-0/1DTE + DTE×type tables | whole-tape |

## Tool errors

- `uw hot-chains sweep-persistence --days 5 --top-n 20 --symbol NBIS --date 2026-06-05 --json` →
  `Error: unknown flag: --date`. Re-ran without `--date`; tool anchors to the
  latest available date, which IS the as-of date (2026-06-05, per
  phase-0-intake.md), so the result is as-of-correct.
- First-pass jq filters on `smart-money-flow`/`sweep-ratio` guessed phantom
  fields (`.underlying_symbol`); schema inspected and re-filtered on
  `.option_symbol`. No numbers were transcribed from the bad reads.

## DATA NOTE / CORRECTION

- Screener close ($227.81, phase-0.5) sits above the last print-anchored spot
  observed at 19:10Z ($222.58) — late-session rally implied; phase-5 OHLC must
  confirm the close and day range.
- Premium classifiers count both legs of the deep-ITM rolls as put premium;
  raw put-premium totals overstate bearish intent today.

## Verdict for downstream phases

- **Bias from this phase:** mixed, bearish tilt — the only *persistent*
  directional signal (5/5-session bearish sweep dominance) is bearish; today's
  tape itself is delta-flat and structure-dominated.
- **Conviction:** 2/5
- **Three things later phases must remember:**
  1. Jun-26 285P is a fresh **net-written** line (7,006 vol / 6 OI; $31.0M bid vs
     $7.1M ask) tied to a synthetic-long/financing structure — phase 3 must check
     whether OI confirms and where it sits vs the put walls.
  2. The clean directional prints are small relative to gross: Jun-12 215P
     $3.6M at ask + Jun-18 190P $3.16M block (bearish) vs Jan-27 310C $9.84M
     at mid (bullish, printed at $240.29 pre-slide).
  3. NBIS has been a top-20 bearish-sweep name **five sessions running**
     ($643.6M cumulative) — whatever phase 2/5 say about accumulation, the
     option tape has leaned short all week.
- **Open questions:** Is dark pool absorbing this selling (accumulation) or
  distributing? What was the actual close/range (phase 5)? What news cracked the
  stock ~9.5% intraday with earnings 2 months out (phase 6/7c)?
