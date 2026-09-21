# Phase 1 — Options Flow

**Ticker:** PATH
**As-of date:** 2026-07-13
**Generated:** 2026-07-13T20:16:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

PATH's options tape is genuinely **mixed with a marginal bearish tilt**, and quiet
for the name (per phase-0.5 `[CTX:]` self_pctile_total 17.5). By premium the tape is
call-heavy (call $1.28M vs put $636k), but the aggressor classification is net
**bearish** — bullish $771k vs bearish $938k → **net_flow −$167k**. The single most
persistent, largest-conviction theme is **ATM $12 January-2028 LEAP put buying at
the ask** (the only qualifying ≥$100k sweep is a $149k print there), which reads as
protective hedging given spot ≈ $12, not an outright bearish campaign. Upside is
expressed only in small OTM call buys ($15 Sep/Jan). Conviction is low (2/5): quiet,
two-sided, no smart-money campaign.

## Key signals

- Whole-tape net_flow **−$166,751** (bullish $771,148 − bearish $937,899) `[FLOW:insights_deep_dive]` — mildly bearish aggression on a call-heavy tape (P/C by premium 0.50, by ratio field 0.265).
- Largest single sweep: **$12 PUT Jan-2028 LEAP, ask-side, $149,375** — the only ask sweep ≥$100k `[FLOW:sweeps]`; ATM protective/directional-bearish LEAP.
- Top-25 prints split **put-ask $203,542 vs call-ask $181,898** — balanced-to-slightly-bearish on aggressive buying `[FLOW:top_premium_trades]`.
- **sweep-persistence: PATH 5/5 sessions in top, `dominant_direction = mixed`, $1.32M total** `[FLOW:sweep_persistence]` — persistent activity but NOT one-directional.
- **No smart-money flow** detected for PATH on this date (absent from both bullish and bearish `smart-money-flow` top-10) `[FLOW:smart_money_flow]`.

## Detailed findings

### Whole-tape aggregate `[FLOW:insights_deep_dive]` (read the top-N against this)

| Field | Value |
|-------|-------|
| call_premium | $1,278,744 |
| put_premium | $636,088 |
| bullish_premium | $771,148 |
| bearish_premium | $937,899 |
| **net_flow (derived)** | **−$166,751** (bearish tilt) |
| call_volume | 23,599 |
| put_volume | 6,254 |
| put_call_ratio | 0.265 |
| iv_rank | 40.4 |
| implied_move_perc | 5.3% |

Call-heavy by volume/premium, but the *directional* (aggressor) read is net bearish.
Per phase-0.5 this is a **BUSY_NAME_NORMAL_DAY / quiet-for-PATH** tape → downstream
phases 1–2 confluence capped at `+`.

### Sweeps (ask vs bid)

- **Ask side:** one qualifying sweep ≥$100k — **$12 PUT, exp 2028-01-21, $149,375**. ATM (spot ~$12) long-dated put bought aggressively.
- **Bid side:** none ≥$100k.

### New positioning (unusual vol, vol/OI ≥3)

- $7.5 CALL Jul-17 — vol 122 / OI 3 (vol/OI **40.7**), $54,897 — near-dated lotto, tiny.
- $16 CALL Jul-31 — vol 594 / OI 31 (vol/OI 19.2), $3,564 — cheap far-OTM lotto.
- $16 CALL Aug-07 — vol 162 / OI 52 (vol/OI 3.1), $1,456.
- Openings are trivial premium — no institutional new position of size on the near tape.

### Largest premium prints (top of tape)

| Time (Z) | Type | Strike | Expiry | Premium | Size | Side | Δ |
|----------|------|--------|--------|---------|------|------|---|
| 15:22 | C | $15 | 2026-09-18 | $51,858 | 774 | ask | 0.31 |
| 14:57 | C | $15 | 2027-01-15 | $48,900 | 300 | mid | 0.45 |
| 16:08 | P | $13 | 2026-12-18 | $41,550 | 150 | **bid** | −0.46 |
| 14:16 | P | $12 | 2028-01-21 | $37,500 | 100 | ask | −0.31 |
| 13:51 | P | $12 | 2028-01-21 | $37,500 | 100 | ask | −0.31 |
| 14:38 | P | $12 | 2028-01-21 | $37,000 | 100 | ask | −0.30 |
| 16:08 | P | $12 | 2026-12-18 | $32,850 | 150 | ask | −0.39 |
| 14:32 | C | $12 | 2026-08-21 | $30,000 | 300 | ask | 0.53 |

Aggressor split (top-25): **put-ask $203,542** (773 contracts, LEAP $12 puts dominate)
vs **call-ask $181,898** (1,804 contracts, OTM $15 calls + $12 Aug call). One put-bid
print ($13 Dec put, $41.5k) is either put-selling (bullish) or a close. The bearish
tilt is real but modest and LEAP-concentrated → hedge-flavored, not urgent directional.

### IV outliers + Greeks

- Extreme IV only on near-dated micro-lotto: $7 & $7.5 Jul-17 calls (IV **285–298%**, vol 122) and $17 Jul-24 call (IV 101%). Noise, not signal.
- Greek screener top rows are the same $15 calls (Δ 0.31–0.45) and $12–13 LEAP puts (Δ −0.30 to −0.46) — consistent with the print tape; no hidden gamma/vega monster.

## Tool calls (audit trail)

| Command | Key value(s) ← `jq` path | Rows |
|---------|--------------------------|------|
| `insights deep-dive --symbol PATH --date 2026-07-13` | net_flow −$166,751 ← `.uw_screener.bullish_premium − .bearish_premium` | whole-tape |
| `options-flow sweeps --side ask --min-premium 100000` | $12 Jan-28 put $149,375 ← `.results[].total_premium` | 1 |
| `options-flow sweeps --side bid --min-premium 100000` | none ← `.results` len 0 | 0 |
| `options-flow unusual-volume --min-vol-oi-ratio 3` | $7.5 Jul-17 C vol/OI 40.7 ← `.results[].vol_oi_ratio` | 3 |
| `options-flow top-premium-trades --top-n 25` | put-ask $203,542 vs call-ask $181,898 ← `sort_by(-.premium)` group | 25 |
| `options-flow iv-outliers` | $7.5 Jul-17 C IV 2.98 ← `.results[].avg_iv` | 3 |
| `options-flow greek-screener --sort-by premium` | $12 Jan-28 P Δ−0.31 ← `.results[].delta` | 15 |
| `hot-chains smart-money-flow --direction bullish/bearish` | PATH absent ← `select(.ticker=="PATH")` | 0/0 |
| `hot-chains sweep-persistence --days 5 --symbol PATH` | mixed, 5/5, $1.32M ← `.results[0].{dominant_direction,sessions_in_top,total_sweep_premium}` | 1 |
| `hot-chains sweep-ratio --min-sweep-ratio 0.3` | PATH absent ← `select(.ticker=="PATH")` | 0 |

## Tool errors

- `hot-chains sweep-persistence … --date 2026-07-13` → `Error: unknown flag: --date`. Re-ran without `--date` (leaf anchors to latest tape) — succeeded. Value used is from the clean re-run.

## DATA NOTE / CORRECTION

- `top-premium-trades` / `greek-screener` premium & size fields are `premium`/`size`,
  NOT `total_premium`/`total_volume` (those keys are null there). First extraction
  showed nulls; re-read against `.premium`/`.size` → values above. All numbers here
  trace to the corrected `jq` paths.

## Verdict for downstream

- **Net bias:** MIXED, marginal bearish tilt (net_flow −$167k; sweep-persistence dominant_direction=mixed).
- **Conviction:** 2/5 — quiet for the name, two-sided, no smart-money campaign.
- **Three things later phases must remember:**
  1. Direction is genuinely **mixed** — net_flow only −$167k and 5-session sweep persistence is *mixed*, so options give no clean directional signal.
  2. The single highest-conviction, most-persistent theme is **ATM $12 Jan-2028 LEAP put buying at ask** ($149k sweep + three 100-lots) — most consistent with a **protective hedge** on a long position; resolve against phase-2 darkpool.
  3. Upside appetite is limited to small OTM $15 Sep/Jan call buys — positioning, not a campaign.
- **Open questions:** Is the 07-09 darkpool print (phase 2) accumulation that these LEAP puts hedge, or is the put buying genuine bearish conviction? Does dealer OI (phase 3) show the $12 strike as a wall?
