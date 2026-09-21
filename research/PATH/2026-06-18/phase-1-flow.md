# Phase 1 — Options Flow

**Ticker:** PATH (UiPath Inc.)
**As-of date:** 2026-06-18
**Generated:** 2026-06-20T13:00:42Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

PATH's tape is **mildly bullish once 0DTE delta-one noise is stripped**. The headline
whole-tape aggregate looks flat (bullish $1.00M vs bearish $0.98M = **+$17.8k net**),
but that flatness is an artifact of two-sided deep-ITM **0DTE** call flow (delta ≈ 0.97,
i.e. synthetic-stock / delta-one prints, not directional vol bets). Excluding 0–1DTE,
net directional **delta-notional is +$1.07M long** — bullish via near-term (8–45DTE)
calls and LEAP calls, with a small offsetting bearish pocket in 46–180DTE puts. The
strongest signal is **sweep-persistence: PATH ran a bullish sweep campaign every one
of the last 5 sessions (consistency_score 1.0, $2.27M total sweep premium)**. Tempered
by phase-0.5 `BUSY_NAME_NORMAL_DAY` (conviction capped at `+`).

## Key signals

- **Persistent bullish sweep campaign:** consistency_score **1.0**, sessions_in_top **5/5**
  (2026-06-12→18), dominant_direction **bullish**, total_sweep_premium **$2,272,874**
  [FLOW:sweep_persistence].
- **Net long ex-0DTE:** delta-notional +$1.07M long (call ask +$3.26M − call bid $2.32M
  − put ask $0.98M + put bid $1.11M) [FLOW:aggressor_ex0dte DUCKDB][FLOW:delta_notional DUCKDB].
- **Call-heavy whole tape:** call premium **$1.873M** vs put **$0.670M**; P/C ratio
  **0.335**; call vol 27,552 vs put vol 9,225 [FLOW:insights_deep_dive].
- **Real new directional positioning:** $11 call exp 2026-06-26 bought **ask, 4,745 lots**,
  $61,685 (delta 0.24, gamma 0.33 — speculative weekly); $10 call exp 2026-07-17
  opening **vol 1,788 / OI 422 = 4.24× vol/OI** [FLOW:top_premium_trades][FLOW:unusual_volume].
- **Bull income tilt:** $9 put exp 2026-09-18 **sold on bid**, 998 lots, $76,846 (delta −0.29)
  [FLOW:top_premium_trades]. Offset by small ITM put buys ($20 Aug, $17 Nov — delta-one shorts, ≤41 lots).

## Detailed findings

### Whole-tape aggregate (read top-N against this) — `[FLOW:insights_deep_dive]`

| Field | Value |
|-------|-------|
| bullish_premium | $1,002,311 |
| bearish_premium | $984,512 |
| **net_flow (derived = bull − bear)** | **+$17,799 (flat)** |
| call_premium | $1,872,959 |
| put_premium | $669,968 |
| put_call_ratio | 0.335 |
| call_volume / put_volume | 27,552 / 9,225 |
| implied_move_perc | 2.06% |
| iv_rank | 34.55 |

The flat net_flow is **misleading**: it nets two-sided 0DTE deep-ITM call flow. See DTE split.

### DTE-bucket premium (full tape) — `[FLOW:dte_bucket DUCKDB]`

| DTE bucket | call $M | put $M | read |
|------------|---------|--------|------|
| 0–1DTE | 0.684 | 0.131 | delta-one noise (Δ≈0.97) — discard directionally |
| 8–45DTE | 0.343 | 0.200 | **bullish** (13,583 call contracts; $11 6/26, $10 7/17) |
| 46–180DTE | 0.176 | 0.244 | mildly **bearish** (put pocket: $9 Sep, $17 Nov, $20 Aug) |
| LEAP (>180DTE) | 0.669 | 0.095 | **bullish** institutional (long-dated $8/$10/$15/$20 calls) |

### Aggressor / delta-notional, ex-0–1DTE — `[FLOW:aggressor_ex0dte DUCKDB]`

| type | side | trades | contracts | prem $M | delta-notional $M |
|------|------|--------|-----------|---------|-------------------|
| call | ask | 801 | 10,625 | 0.481 | +3.26 |
| call | bid | 979 | 7,792 | 0.497 | +2.32 |
| put | ask | 446 | 2,272 | 0.232 | −0.98 |
| put | bid | 348 | 2,656 | 0.258 | −1.11 |

Net directional delta-notional (ask=open, bid=sold) ≈ **+$1.07M long**. More call
contracts lifted on ask (10,625) than sold on bid (7,792); puts roughly two-sided.

### Sweeps (≥$100k) — `[FLOW:sweeps]`

Both >$100k "sweeps" today are **0DTE deep-ITM calls** = delta-one, not directional:
- Ask: $5.50 call 0DTE, $127,697, 277 lots, 1 trade, avg $4.61 (≈ intrinsic, Δ0.98).
- Bid: $6.00 call 0DTE, $117,431, 285 lots, 9 trades, avg $4.13 (sold, Δ0.97).

The directional conviction is in the **multi-day persistence** (above), not today's single sweeps.

### New positioning (vol/OI ≥ 3) — `[FLOW:unusual_volume]`

| strike/type | expiry | vol | OI | vol/OI | prem |
|-------------|--------|-----|----|--------|------|
| $5.50 call | 2026-06-18 | 557 | 66 | 8.44 | $257,886 (0DTE delta-one) |
| $6.00 call | 2026-06-18 | 617 | 96 | 6.43 | $255,174 (0DTE delta-one) |
| **$10 call** | **2026-07-17** | **1,788** | **422** | **4.24** | **$132,998 (real ATM new long)** |

### IV outliers + Greeks — `[FLOW:iv_outliers][FLOW:greek_screener]`

IV outliers are all 0DTE low-strike calls (avg_iv 1.59 at $4, 1.12 at $5) — meaningless
on delta-one deep-ITM contracts. The genuine gamma names are the $11 6/26 call (gamma 0.33)
and the $10 7/17 calls (gamma 0.22, delta ~0.54 = ATM). No directional put IV cluster.

### Cross-checks that did NOT fire

- `smart-money-flow` (min-vol 500): PATH **not** in bullish or bearish top-10 — its
  ask/bid imbalance isn't among the day's most extreme [FLOW:smart_money_flow].
- `sweep-ratio` (min 0.3): PATH **not** in the top-15 — sweeps aren't unusually
  aggressive as a ratio today [FLOW:sweep_ratio].

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← path | Rows |
|------------------|---------------------|------|
| `insights deep-dive --symbol PATH --date 2026-06-18` | bull 1,002,311 / bear 984,512 / call_prem 1.873M / put_prem 0.670M / pcr 0.335 ← `.uw_screener` | 1 |
| `options-flow sweeps --side ask/bid --min-premium 100000` | both 0DTE ITM calls ($127.7k ask / $117.4k bid) ← `.results[]` | 2 |
| `options-flow unusual-volume --min-vol-oi-ratio 3` | $10 7/17 call vol/OI 4.24 ← `.results[]` | 3 |
| `options-flow top-premium-trades --top-n 25` | $11 6/26 ask 4745 lots; $9 Sep put bid 998 ← `.results[]` | 25 |
| `options-flow iv-outliers --top-n 15` | all 0DTE low-strike calls ← `.results[]` | 15 |
| `options-flow greek-screener --sort-by premium` | deltas confirm 0DTE = Δ0.97 ← `.results[]` | 15 |
| `hot-chains smart-money-flow --direction bullish/bearish --min-volume 500` | PATH absent both | top-10 ea |
| `hot-chains sweep-persistence --days 5 --symbol PATH` | consistency 1.0, 5/5 sessions, $2.27M, bullish ← `.results[]` | 1 |
| `hot-chains sweep-ratio --min-sweep-ratio 0.3` | PATH absent | top-15 |
| DuckDB §A (ex-0DTE aggressor, delta-notional, DTE buckets) | net +$1.07M long delta-notional | full PATH tape |

## Tool errors

- `hot-chains sweep-persistence … --date 2026-06-18` → `Error: unknown flag: --date`.
  Re-run **without** `--date` (trailing tool, anchors to latest = 2026-06-18, our as-of).
  Result above is from the corrected call.

## DATA NOTE / CORRECTION

Headline `net_flow` (+$17.8k, "flat") was re-interpreted, not corrected: the DuckDB
ex-0DTE delta-notional cut (+$1.07M long) shows the flat figure is a 0DTE-delta-one
artifact. All values round-tripped through `jq`/SQL.

## Verdict for downstream

- **Net bias:** mildly **bullish** (lean long; ex-0DTE delta-notional +$1.07M, 5-session
  persistent bullish sweep campaign, call-heavy + LEAP call buying + put selling).
- **Conviction:** **3/5** (capped — `BUSY_NAME_NORMAL_DAY`; today's gross net flow flat;
  PATH not in smart-money/sweep-ratio leaders; magnitudes small in absolute $).
- **Three datapoints later phases must remember:**
  1. Bullish sweep persistence consistency_score **1.0 over 5/5 sessions** — the most
     durable signal; weigh heavily vs the flat single-day net_flow.
  2. Ex-0DTE delta-notional **+$1.07M net long**; bullish 8–45DTE + LEAP calls, small
     bearish 46–180DTE put hedge.
  3. New ATM long: **$10 calls exp 2026-07-17, vol/OI 4.24** — the cleanest dated
     directional position to track.
- **Open questions:** Is dark pool confirming accumulation under this bullish call flow
  (phase 2)? With 31.78% short float (phase 0), is the persistent call bid squeeze-chasing
  or genuine accumulation? Where are the dealer walls vs the $10–$11 call strikes (phase 3/4)?
