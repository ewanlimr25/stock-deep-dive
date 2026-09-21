# Phase 1 — Options Flow

**Ticker:** SYM
**As-of date (effective):** 2026-05-21
**Generated:** 2026-05-22T15:05Z
**Upstream phases cited:** phase-0-intake.md

## Summary

SYM trades a thin but persistent tape around ~$50.5 with elevated IV (70–85%
on LEAP calls, ~83% on near-dated puts). The dominant signature is **bid-side
LEAP call activity** (top three trades by premium are all bid-side: $66K
Jan-27 50C, $51K Jan-28 60C, $18K Jan-28 45C) — read as call-writing /
position closing rather than aggressive directional buying. Despite that,
`hot_chains_sweep_persistence` flags SYM in the top-sweep list for 3 of 5
recent sessions with a *bullish* dominant direction and $710K cumulative
sweep premium [FLOW:sweep_persistence], so a small bullish undercurrent
co-exists with bigger LEAP-call supply.

## Key signals

- **Top single trade is bid-side**: 2027-01-15 $50 call, 50 lots @ $13.20,
  $66K premium, IV 79.8%, delta 0.637, at underlying $50.79 [FLOW:top_premium_trades].
  Indicates call supply / yield grab, not call buying.
- **Sweep persistence flags SYM**: 3 of 5 sessions in top sweep list,
  dominant_direction = bullish, total_sweep_premium $710,258
  [FLOW:sweep_persistence]. Small but recurring bullish footprint.
- **Unusual volume — bearish near-term skew**: 2026-06-05 $39 PUT, vol 120 vs
  OI 21 (vol/OI 5.71), avg IV 82.99% [FLOW:unusual_volume]. New put
  opening on a downside strike ~22% below spot.
- **Speculative far-OTM call open**: 2026-07-17 $65 CALL, vol 198 vs OI 57
  (vol/OI 3.47), avg IV 65.6% [FLOW:unusual_volume]. Some lottery-ticket
  call buying ~30% above spot.
- **0DTE put bids at extreme IV**: three 2026-05-22 puts (P60/P62/P65)
  printed at $11K–$11.2K premium with deltas ~-0.78 and IV 3.8x–5.3x
  [FLOW:top_premium_trades]. These are bid-side prints on expiration day —
  likely closing puts (selling-to-close protective puts) rather than fresh
  bearish opens. Synthetic-style IV indicates pin pricing.
- **No SYM rows in `smart_money_flow`** (bullish or bearish, min_volume 100,
  date 2026-05-21) — single-contract conviction in either direction does
  not clear the market-wide top-50 cutoff.

## Detailed findings

### Sweeps — ask vs. bid, premium, persistence

Aggregated sweep table (min_premium $10K, top 20) is mixed but heavily
bid-side on LEAPs and ask-side on near-dated cheap calls:

| Expiry | Type | Strike | Side | Premium | Size | Avg px |
|--------|------|--------|------|---------|------|--------|
| 2027-01-15 | call | 50 | **bid** | $83,677 | 64 | 12.87 |
| 2028-01-21 | call | 60 | **bid** | $51,000 | 30 | 17.00 |
| 2027-01-15 | call | 40 | **bid** | $27,602 | 16 | 17.31 |
| 2026-07-17 | call | 65 | **ask** | $25,593 | 190 | 1.33 |
| 2028-01-21 | call | 45 | **bid** | $24,666 | 11 | 22.31 |
| 2026-08-21 | call | 47.5 | **ask** | $16,896 | 19 | 8.89 |
| 2026-08-21 | call | 50 | bid | $16,760 | 22 | 7.70 |
| 2027-01-15 | call | 55 | ask | $16,407 | 15 | 10.94 |
| 2026-07-17 | call | 45 | bid | $16,000 | 20 | 8.00 |
| 2026-05-22 | put  | 60 | bid | $14,624 | 17 | 8.61 |
| 2027-01-15 | put  | 47.5 | ask | $14,000 | 14 | 9.93 |

Pattern: deep-ITM LEAP calls trading **bid**; cheap OTM near-dated calls
trading **ask**. Reads like an institution rolling ITM LEAPs into OTM short-
dated calls — selling Jan-27 50Cs / Jan-28 60Cs and buying tiny Jul-26 65Cs
/ Aug-26 47.5Cs. Net delta of the bid-side LEAP block ≈ −95 contracts ×
0.64 delta ≈ −60 deltas; the OTM near-dated ask-side calls add back ~190 ×
0.21 ≈ +40 deltas. **Net flow is mildly bearish/neutral on delta,
unambiguously short vega** [FLOW:sweeps + FLOW:greek_screener].

### New positioning (unusual vol / OI)

Only 2 contracts cleared the vol/OI ≥ 3 filter on 2026-05-21:

| Expiry | Type | Strike | Vol | OI | vol/OI | Avg IV | Premium |
|--------|------|--------|-----|----|--------|--------|---------|
| 2026-06-05 | put  | 39 | 120 | 21 | 5.71 | 82.99% | $2,250 |
| 2026-07-17 | call | 65 | 198 | 57 | 3.47 | 65.62% | $26,618 |

Read: one new downside put position (39 strike, ~22% OTM, near-term) and a
speculative OTM call open (65 strike, ~29% OTM, ~2 months out). The put
open is small ($2.3K premium) and far OTM — looks like cheap hedge or
tail-risk speculation. The call open at $26.6K is more meaningful and is
the same 2026-07-17 65 call that shows up ask-side in the sweep table.

### Largest premium prints

Top 6 by premium (all calls):

| Time (UTC) | Expiry | Type | Strike | Side | Premium | Size | Px | Delta | IV |
|------------|--------|------|--------|------|---------|------|------|-------|-----|
| 14:03 | 2027-01-15 | call | 50 | **bid** | $66,000 | 50 | 13.20 | 0.637 | 79.8% |
| 14:52 | 2028-01-21 | call | 60 | **bid** | $51,000 | 30 | 17.00 | 0.634 | 80.5% |
| 19:48 | 2028-01-21 | call | 45 | **bid** | $18,000 | 8  | 22.50 | 0.742 | 83.4% |
| 15:00 | 2027-01-15 | call | 40 | **bid** | $17,210 | 10 | 17.21 | 0.748 | 81.6% |
| 15:23 | 2026-07-17 | call | 45 | **bid** | $16,000 | 20 | 8.00  | 0.698 | 69.1% |
| 14:39 | 2026-08-21 | call | 50 | **bid** | $15,200 | 20 | 7.60  | 0.575 | 76.9% |

All six largest prints are **bid-side calls**. The combined bid-side LEAP
notional ($66K + $51K + $18K + $17.2K = ~$152K) dwarfs any ask-side print.

Total grossed premium on SYM today across the top-25 trades ≈ **$390K** —
that is *very small* relative to the IV regime, confirming SYM is a thin
options name even on a busy day.

### IV outliers + Greeks

- `iv_outliers` (min_iv 1.0, min_volume 20): only one contract — the
  2026-05-22 $60 call with avg/max IV 1.39 (139%). Volume 40, premium $40.
  Negligible — pin/expiration pricing noise [FLOW:iv_outliers].
- Greek screener (sort=premium) confirms the LEAP-call bid pattern. Vega on
  the top trades is high (0.15–0.24 per contract) — institutional flow is
  **net short vega** as the bid hits.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__options_flow_sweeps` | symbol=SYM, min-premium=10000, top-n=25, date=2026-05-21 | 21 rows, LEAP-call-bid dominant |
| `mcp__uw-pp__options_flow_unusual_volume` | symbol=SYM, min-vol-oi-ratio=3, top-n=25, date=2026-05-21 | 2 rows: P39 (vol/OI 5.71), C65 (vol/OI 3.47) |
| `mcp__uw-pp__options_flow_top_premium_trades` | symbol=SYM, top-n=25, date=2026-05-21 | 26 rows, top 6 are bid-side calls |
| `mcp__uw-pp__options_flow_iv_outliers` | symbol=SYM, top-n=15, date=2026-05-21, min-volume=20 | 1 row (0DTE C60 IV 139%) |
| `mcp__uw-pp__options_flow_greek_screener` | symbol=SYM, top-n=15, sort-by=premium | 15 rows confirming sweep pattern |
| `mcp__uw-pp__hot_chains_smart_money_flow` | direction=bullish, top-n=50, min-volume=100 | no SYM rows in top-50 |
| `mcp__uw-pp__hot_chains_smart_money_flow` | direction=bearish, top-n=50, min-volume=100 | no SYM rows in top-50 |
| `mcp__uw-pp__hot_chains_sweep_persistence` | symbol=SYM, days=5, top-n=20 | SYM: 3/5 sessions, bullish dominant, $710,258 total sweep premium |
| `mcp__uw-pp__hot_chains_sweep_ratio` | top-n=50, min-volume=100, min-sweep-ratio=0.3 | no SYM rows in top-50 |

## Tool errors

None for 2026-05-21. (Earlier 2026-05-22 attempt errored — handled in phase 0.)

## Verdict for downstream phases

- **Bias from this phase:** mixed — small bullish persistence (sweep tracker) is
  outweighed by clearly bid-side LEAP-call flow (net short vega + slightly short
  delta). Lean **slightly bearish / mean-reversion / vol-selling**, not directional
  longing.
- **Conviction:** 2/5. Aggregate premium is tiny (~$390K top-25, $710K cumulative
  sweep premium over 5 sessions). Conviction is low because the chain is thin —
  not because the signal is genuinely conflicting.
- **Three things later phases should remember:**
  1. **Spot is ~$50.50** on 2026-05-21 (range $49.66–$50.83 across the top
     premium trades). All downstream level math should anchor here.
  2. **IV regime is mid-70s to mid-80s on LEAPs**, ~83% on near-dated puts —
     SYM is a structurally high-vol name; the dark-pool, OI, and structure
     phases should expect heavy gamma and skew effects.
  3. **The dominant institutional footprint is selling LEAP calls / buying
     short-dated OTM calls** — looks like a covered-call roll or
     position-de-risking by a long holder. Phase 2 (dark pool) should test
     whether dark-pool prints corroborate underlying stock distribution by
     the same hands.
- **Open questions:**
  - Is there an earnings catalyst inside the LEAP window that would justify
    a roll-out? (Phase 6 / WebSearch.)
  - Are the 0DTE put bid-side prints closing a hedge that was put on
    earlier in the week? (Phase 3 OI changes.)
  - Does dark-pool tape show net accumulation or distribution of underlying?
    (Phase 2.)
