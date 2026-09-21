# Phase 1 — Options Flow

**Ticker:** HOOD
**As-of date:** 2026-06-15
**Generated:** 2026-06-16T11:50:00Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

HOOD's tape is **bullish-tilted but genuinely two-sided** — not a clean one-way
sweep day. The whole-tape aggregate is decisively call-skewed (call premium
**$197.9M** vs put **$35.2M**, PCR **0.346**, net call premium **+$10.06M**) and
ask-side call sweeps ($47.0M) outweigh bid-side call sweeps ($37.0M) by ~+$10M, yet
the *net* directional dollar flow is a modest **+$8.68M** (bullish $106.4M − bearish
$97.8M) and the 5-day sweep-persistence read tags HOOD's campaign **"mixed"**
(consistency 1, 5/5 sessions, $488.7M total sweep premium). The single largest print
of the day is a **$85 put exp 2027-01-15 for $5.54M** (delta −0.29) and new
positioning is two-sided — large new near-money puts ($99P 6/18 $448k, $96P 7/10
$351k) alongside new upside calls ($96C 7/31 $516k). Per phase-0.5 this is
GENUINELY_UNUSUAL (no busy-name magnitude cap), but the mixed campaign and big
offsetting put prints keep conviction moderate.

## Key signals

- Whole-tape **call-heavy**: call prem $197.9M vs put $35.2M (5.6:1), PCR 0.346,
  call vol 353,167 vs put 122,323 `[FLOW:insights_deep_dive]`.
- Net flow only **+$8.68M** (bullish $106.4M − bearish $97.8M) — modest net despite
  $233M gross; two-sided `[FLOW:insights_deep_dive]`.
- Ask-side sweeps **$52.3M** (calls $47.0M / puts $5.4M) vs bid-side **$39.3M**
  (calls $37.0M / puts $2.3M) → net ask-side call lean ~**+$10.0M**, plus net put
  buying ~+$3.1M `[FLOW:sweeps]`.
- 5-day sweep campaign **persistent but MIXED**: consistency_score 1, sessions_in_top
  5/5, total_sweep_premium $488.7M, dominant_direction **mixed** `[FLOW:sweep_persistence]`.
- Largest single print: **$85P 2027-01-15 $5.54M** (LEAP hedge/bearish, delta −0.29)
  `[FLOW:top_premium_trades]` — offsets part of the call bullishness.

## Detailed findings

### Whole-tape aggregate (read top-N against this) `[FLOW:insights_deep_dive]`

| Field | Value |
|-------|-------|
| call_premium | $197,892,350 |
| put_premium | $35,225,588 (call:put ≈ 5.6:1) |
| bullish_premium | $106,433,035 |
| bearish_premium | $97,757,295 |
| **net_flow** (derived bull−bear) | **+$8,675,740** |
| net_call_premium / net_put_premium | +$10.06M / +$1.38M |
| call_volume / put_volume | 353,167 / 122,323 |
| put_call_ratio | 0.346 |
| iv_rank | 32.4 (mid/low) |
| implied_move / implied_move_perc | $4.55 / **4.65%** |

Read: the bullish read lives in the **call/put skew** (5.6:1 premium, PCR 0.346),
not the net dollars (+$8.68M is modest; gross is two-sided $233M). Consistent with
phase-0.5 `[CTX:]` — top-decile name, modest net.

### Sweeps (ask vs bid) `[FLOW:sweeps]`

- **Ask-side (top-25):** $52.3M total — calls 23 prints $47.0M, puts 2 prints $5.4M.
- **Bid-side (top-25):** $39.3M total — calls 23 prints $37.0M, puts 2 prints $2.3M.
- Top ask sweeps: $100C 6/18 **$5.02M** (size 17,842 / 3,954 trades), $100C 8/21
  $4.61M, $90C 8/21 $4.30M, $85C 7/17 $3.73M, **$90P 7/17 $3.60M** (10,241 ct),
  $100C 7/17 $3.52M.
- Top bid sweeps: $100C 6/18 **$4.64M** (17,080 ct), $85C 7/17 $3.82M, $105C 7/17
  $2.85M, $140C 2027-01-15 $2.66M, $120C 7/17 $2.54M.
- ⚠️ **Two-way churn:** $100C 6/18 prints ~$5M ask *and* ~$4.6M bid; $85C 7/17 prints
  $3.73M ask *and* $3.82M bid — heavy round-tripping, not clean one-side accumulation.
  This is what drives the "mixed" persistence tag.
- Expiry concentration (ask premium): **7/17 $20M**, 6/18 $12M, 8/21 $8M, 2028 LEAPs $4M.

### New positioning (vol/OI ≥ 3) `[FLOW:unusual_volume]`

Genuinely two-sided new opens:
- **New puts:** $99P 6/18 (233×, $448k), $96P 7/10 (242×, $351k — the phase-0 flag),
  $98P 7/10 (143×), $99P 7/02 (104×). Near-money, short-dated.
- **New calls:** $96C 7/31 (107×, $516k — largest new call), OTM $115–118C 6/26–7/31.
- Read: new put opens are near-the-money/short-dated (hedge or tactical bearish), new
  call opens reach for upside. Mixed intent.

### Largest premium prints `[FLOW:top_premium_trades]`

| Type | Strike | Expiry | Premium | Side | Note |
|------|--------|--------|---------|------|------|
| put | $85 | 2027-01-15 | **$5.54M** | no_side | day's biggest — LEAP hedge/bear, Δ−0.29 |
| call | $85 | 2026-07-17 | $2.07M | no_side | deep-ITM, Δ0.80 (stock replacement?) |
| put | $90 | 2026-07-17 | $1.53M | ask | bought — downside |
| call | $150 | 2027-01-15 | $1.20M | no_side | OTM LEAP call, Δ0.32 |
| call | $60 | 2028-01-21 | $0.83M | ask | deep-ITM LEAP, Δ0.84 |
| call | $85 | 2026-07-17 | $0.70M | ask | bought |
| put | $90 | 2026-07-17 | $0.60M | ask | bought — downside |

### IV outliers + Greeks `[FLOW:iv_outliers][FLOW:greek_screener]`

- IV outliers are all **6/18-expiry deep wings** ($55/60/65P 178–235% IV, $70/$200C
  190–256% IV) — 3-DTE lottery/tail noise, not directional signal.
- Greeks confirm the prints: $85P 1/15 Δ−0.29 ($5.54M), $85C 7/17 Δ0.80 ($2.07M),
  $90P 7/17 Δ−0.27 ($1.53M), $150C 1/15 Δ0.32, $60C 2028 Δ0.84. The high-delta ITM
  7/17 calls look like leveraged-long / stock-replacement; the LEAP put is the main
  bearish/hedge weight.
- HOOD **not** in the market-wide smart-money-flow top-10 (either direction) — its
  ask/bid imbalance isn't among the day's most extreme; no per-name confirmation there.
- Only HOOD row in market sweep-ratio: $60P 6/18 sweep_ratio 0.93 but $2,840 premium
  (deep-OTM dust) — ignore.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `uw insights deep-dive --symbol HOOD --date 2026-06-15 --json` | call_prem 197.9M, put_prem 35.2M, bull 106.4M, bear 97.8M, PCR 0.346 ← `.uw_screener.*`; net_flow +$8.68M (bull−bear) | whole-tape |
| `uw options-flow sweeps --symbol HOOD --side ask --min-premium 100000 --top-n 25 --date 2026-06-15` | ask total $52.3M; call $47.0M/put $5.4M ← `group_by(.option_type)` sum `.total_premium` | top-25 |
| `uw options-flow sweeps … --side bid …` | bid total $39.3M; call $37.0M/put $2.3M | top-25 |
| `uw options-flow unusual-volume --symbol HOOD --min-vol-oi-ratio 3 --top-n 25 …` | new puts $99P6/18 448k, $96P7/10 351k; new call $96C7/31 516k ← `.results[].vol_oi_ratio` | top-25 |
| `uw options-flow top-premium-trades --symbol HOOD --top-n 25 …` | $85P 2027-01-15 $5.54M largest ← `sort_by(-.premium)` | top-25 |
| `uw options-flow iv-outliers --symbol HOOD --top-n 15 …` | all 6/18 deep wings 178–256% IV | top-15 |
| `uw options-flow greek-screener --symbol HOOD --top-n 15 --sort-by premium …` | $85P Δ−0.29; $85C Δ0.80 ← `.results[].delta` | top-15 |
| `uw hot-chains sweep-persistence --days 5 --top-n 20 --symbol HOOD --json` | consistency 1, 5/5 sessions, $488.7M, dominant **mixed** ← `.results[]\|select(.ticker=="HOOD")` | top-20 |
| `uw hot-chains smart-money-flow --direction bullish\|bearish --top-n 10 --min-volume 500 --date 2026-06-15` | HOOD not in top-10 either side ← `select(.option_symbol\|test("^HOOD"))` empty | top-10 |
| `uw hot-chains sweep-ratio --top-n 15 --min-volume 500 --min-sweep-ratio 0.3 --date 2026-06-15` | only HOOD row = $60P dust | top-15 |

## Tool errors

- `uw hot-chains sweep-persistence … --date 2026-06-15` → `Error: unknown flag: --date`.
  Re-ran without `--date` (latest available = as-of 2026-06-15, so as-of-correct).
  No value transcribed from the failed call.

## DATA NOTE / CORRECTION

- Sweeps rows carry no `iv`/`avg_iv` field (keys: avg_price, expiry, option_type,
  side, strike, total_premium, total_size, trade_count) — initial print-list jq that
  multiplied `iv` errored `null * 100`; re-listed without IV. No bad value persisted.
- smart-money-flow rows key on `option_symbol` (no `ticker`); HOOD presence checked
  via `option_symbol|test("^HOOD")`.

## Verdict for downstream phases

- **Net bias:** bullish-tilted but **MIXED / two-sided** (lean bullish on the call/put
  skew; tempered by a persistent-mixed sweep campaign and a $5.54M LEAP put).
- **Conviction:** **3 / 5** — call-heavy and 5/5-session persistent, but two-way churn,
  modest net dollars (+$8.68M), and large offsetting downside prints cap it.
- **Three things later phases should remember:**
  1. Bullishness is in the **call/put skew** (call:put prem 5.6:1, PCR 0.346, net call
     +$10M ask-side), **not** the net dollar flow (+$8.68M, modest). Sweep campaign is
     persistent-but-MIXED (5/5 sessions, dominant_direction mixed) — discount one-way reads.
  2. A **$85P 2027-01-15 LEAP at $5.54M** is the day's single biggest print, plus new
     near-money puts ($99P 6/18, $96P 7/10) and $90P 7/17 buying — material downside
     leg. **Phase-2 must test whether these puts hedge accumulated long stock (dark-pool
     accumulation) or are standalone bearish bets.**
  3. Near-term gamma/OI concentrates at **$100 (6/18, churned both sides)** and
     **$85/$90/$100/$105 (7/17)** — hand these strikes to phase-3 (OI walls) and phase-4
     (max-pain/gamma).
- **Open questions:** Is dark pool (phase-2) confirming the call-side bullishness with
  block accumulation, or are the large puts protecting a long? Is the deep-ITM $85C
  7/17 (Δ0.80) stock-replacement bullish positioning?
