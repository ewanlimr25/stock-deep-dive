# Phase 1 — Options Flow

**Ticker:** GRAB
**As-of date:** 2026-05-21
**Generated:** 2026-05-21T20:30:00Z
**Upstream phases cited:** phase-0-intake.md

## Summary

GRAB tape is dominated by sub-$50K-premium prints across 2027–2028 LEAPS at the
$3–$4 strike cluster (underlying ~$3.47–$3.57 intraday). Today's largest
single trade is a $40K opening print on 2027-12-17 $10 calls (deep OTM
moonshot, no_side). However, the most material signal is from
`hot_chains_sweep_persistence`: GRAB recurs in the top sweep list for 5 of 5
sessions (consistency_score = 1.0) with `dominant_direction = bearish` and
`total_sweep_premium = $847,155` [FLOW:sweep_persistence]. Today's same-day
tape is mixed (LEAP $4 puts AND $4 calls both bought at ask), but the
persistent 5-day theme is downside-leaning. Net read: **mixed-bearish, low
conviction**.

## Key signals

- **5/5 sessions in top sweep activity, bearish dominant, $847K cumulative**
  premium over the past 5 trading days [FLOW:sweep_persistence].
- **$28.2K LEAP call** at ask: 2028-01-21 $4C, 300 contracts at $0.94, IV 61%
  [FLOW:top_premium_trades] — bullish 1.5y LEAP buyer.
- **Three near-simultaneous LEAP put prints** at ask: 2028-01-21 $4P, 100x at
  $1.11/$1.12/$1.13 (15:59Z / 16:46Z / 16:48Z), aggregating ~$33.6K
  [FLOW:top_premium_trades] — institutional put accumulator, same trader
  pattern.
- **$40K opening print** on deep-OTM 2027-12-17 $10C, no_side, 2,500 contracts
  at $0.16, IV 59%, delta 0.16 [FLOW:top_premium_trades] — lottery-style
  tail-risk bullish bet (or block cross).
- **No GRAB in market-wide smart_money_flow top 25** (bullish OR bearish) and
  not in `sweep_ratio` top 25 — GRAB's flow is below the market's
  institutional radar today [FLOW:smart_money_flow], [FLOW:sweep_ratio].

## Detailed findings

### Sweeps (ask vs bid, premium, persistence)

Today's sweep table (filtered to GRAB, `min_premium=$5K`, top 25):

| Expiry | Strike | Type | Side | Total prem | Size | Trades | Avg px |
|--------|--------|------|------|------------|------|--------|--------|
| 2027-12-17 | $10  | call | no_side | $40,000 | 2,500 | 1 | 0.16 |
| 2026-07-17 | $4   | put  | **ask** | $34,664 | 606 | 17 | 0.57 |
| 2028-01-21 | $4   | put  | **ask** | $33,600 | 300 | 3 | 1.12 |
| 2028-01-21 | $4   | call | **ask** | $31,284 | 334 | 10 | 0.92 |
| 2026-10-16 | $3   | call | bid     | $25,077 | 320 | 24 | 0.76 |
| 2026-06-18 | $3.5 | call | **ask** | $24,142 | 1,251 | 45 | 0.19 |
| 2026-05-29 | $0.5 | call | **ask** | $23,657 | 77 | 77 | 3.07 (deep ITM) |
| 2026-05-22 | $1.5 | call | bid     | $18,201 | 90 | 90 | 2.02 (deep ITM) |
| 2028-12-15 | $4   | call | bid     | $13,627 | 114 | 14 | 1.20 |
| 2028-01-21 | $12  | call | mid     | $11,808 | 738 | 15 | 0.16 |

Ask-side bias by side aggregation across the top 25 GRAB sweeps:
- Total **ask-side premium**: ~$152K (mix of $4 puts AND $4 calls — split)
- Total **bid-side premium**: ~$96K (mostly $3-$4 calls being sold)
- Total **no_side / mid**: ~$52K (the $10C moonshot + LEAP $12C)

The aggregate ask-side beats bid-side, but the ask-side stack is BOTH puts and
calls at $4 — characteristic of a long straddle / vol buyer at LEAP tenor
rather than directional conviction.

### New positioning (unusual vol, vol/OI ratio)

Only one contract met `min_vol_oi_ratio≥1, min_vol≥50`:

| Expiry | Strike | Type | Vol | OI | V/OI | Premium | Avg IV |
|--------|--------|------|-----|-----|------|---------|--------|
| 2026-06-18 | $3.5 | call | 1,499 | 825 | 1.82 | $28,764 | 47.5% |

Lone new-position signal: short-dated ATM-ish ($3.50 strike vs $3.55 spot)
June call. Modest premium ($28K) and modest V/OI (1.8x). Reads like
short-term lottery rather than institutional.

### Largest premium prints (top 10)

| Time (UTC) | Expiry | Strike | Type | Side | Premium | Size | Delta | IV |
|------------|--------|--------|------|------|---------|------|-------|-----|
| 17:57 | 2027-12-17 | $10 | call | no_side | $40,000 | 2,500 | 0.16 | 59% |
| 17:48 | 2028-01-21 | $4  | call | ask     | $28,200 | 300 | 0.60 | 61% |
| 18:13 | 2026-10-16 | $3  | call | bid     | $11,700 | 150 | 0.75 | 55% |
| 16:48 | 2028-01-21 | $4  | put  | ask     | $11,300 | 100 | -0.48 | 45% |
| 16:46 | 2028-01-21 | $4  | put  | ask     | $11,200 | 100 | -0.48 | 44% |
| 15:59 | 2028-01-21 | $4  | put  | ask     | $11,100 | 100 | -0.47 | 45% |
| 14:28 | 2028-12-15 | $4  | call | bid     | $8,925  | 75 | 0.64 | 62% |
| 16:46 | 2028-12-15 | $1  | call | bid     | $8,100  | 30 | 0.94 | 87% |
| 19:36 | 2026-10-16 | $3  | call | bid     | $7,857  | 97 | 0.74 | 57% |
| 13:37 | 2026-10-16 | $4  | put  | ask     | $7,500  | 100 | -0.64 | 46% |

Pattern: clustered 100-lot LEAP put buys at $4 in 2028-01 (3 trades within
~1hr, identical 100-contract sizing → almost certainly one trader). Same
trader OR an opposing trader is also accumulating 2028-01 $4 LEAP calls on
ask. Net 2028-01-21 $4 strike: $33.6K puts vs $31.3K calls bought at ask —
nearly identical premium → consistent with a straddle buyer.

### IV outliers + Greeks

`iv_outliers` (top 5 ignored — they are 0DTE deep-ITM/OTM noise with avg_iv
>10 which are artifacts of near-zero extrinsic). First "real" IV outliers:

| Expiry | Strike | Type | Vol | Avg IV | Total Prem |
|--------|--------|------|-----|--------|------------|
| 2028-12-15 | $1   | call | 36 | 88%  | $9,780 (deep ITM LEAP) |
| 2026-05-22 | $3.5 | call | 761 | 67% | $4,268 (0DTE pin straddle) |
| 2026-05-22 | $3.5 | put  | 174 | 63% | $773 (0DTE) |
| 2026-05-29 | $4   | put  | 27 | 77% | $1,258 |

`greek_screener` (sorted by premium) confirms the LEAP $4 straddle theme: the
top 7 trades by premium include both 2028-01-21 $4 calls (delta +0.60) and 3x
2028-01-21 $4 puts (delta -0.47 to -0.48). High vega (~0.018) — these are
vega bets as much as directional bets.

### Cross-symbol context (hot_chains_*)

- `hot_chains_smart_money_flow` (bullish, top 25 market-wide): no GRAB.
  Bullish action is dominated by IWM puts (3 of top 3 — broad-market bearish),
  CMCSA, XLB. **Read:** GRAB's bullish flow is too small to crack the
  market-wide top 25.
- `hot_chains_smart_money_flow` (bearish): no GRAB. Dominated by CMCSA call
  sells (-$7.6M premium), EWZ, NVDA put-call rolls.
- `hot_chains_sweep_ratio` (min_sweep_ratio 0.3): no GRAB in top 25. Smallcap
  EQNR, GAP, QS dominate.
- `hot_chains_sweep_persistence` (days=5, filtered GRAB): **5/5 sessions,
  bearish dominant, $847,155 total** — this is the standout multi-day signal.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__options_flow_sweeps` | symbol=GRAB, date=2026-05-21, top_n=25, min_premium=5000 | 25 rows, split ask/bid LEAP $4 strikes dominant |
| `mcp__uw-pp__options_flow_unusual_volume` | symbol=GRAB, top_n=25, min_vol_oi_ratio=1, min_vol=50 | 1 row: Jun-18 $3.50C |
| `mcp__uw-pp__options_flow_top_premium_trades` | symbol=GRAB, top_n=25 | 25 rows, top print $40K @ 2027-12-17 $10C |
| `mcp__uw-pp__options_flow_iv_outliers` | symbol=GRAB, top_n=15, min_iv=0.4, min_vol=25 | 15 rows; top 5 are 0DTE deep-ITM/OTM noise |
| `mcp__uw-pp__options_flow_greek_screener` | symbol=GRAB, top_n=15, sort_by=premium | 15 rows, LEAP $4 straddle structure visible |
| `mcp__uw-pp__hot_chains_smart_money_flow` | direction=bullish, top_n=25, min_vol=100 | no GRAB rows |
| `mcp__uw-pp__hot_chains_smart_money_flow` | direction=bearish, top_n=25, min_vol=100 | no GRAB rows |
| `mcp__uw-pp__hot_chains_sweep_persistence` | symbol=GRAB, days=5, top_n=20 | **GRAB: 5/5 sessions, bearish, $847K** |
| `mcp__uw-pp__hot_chains_sweep_ratio` | top_n=25, min_vol=100, min_sweep_ratio=0.3 | no GRAB rows |

## Tool errors

(none — `min_premium=100000` from default would have returned empty; lowered
to $5K which is appropriate for a thin-options sub-$5 stock per phase-0
caveat)

## Verdict for downstream phases

- **Bias from this phase:** **MIXED-BEARISH** (5-day persistence is bearish;
  today is a straddle / mixed)
- **Conviction:** 2/5 (premium magnitude is small; sweep_persistence is the
  only multi-day-significant signal)
- **Three things later phases should remember:**
  1. The $4 strike (LEAP 2028-01-21) is the dominant institutional level for
     BOTH puts and calls — phase-3 OI build and phase-4 gamma walls likely
     concentrate there.
  2. 5-day bearish sweep persistence ($847K cumulative) is the only signal
     that crossed a market-wide ranking threshold. Phase-5 historical OI
     trend should corroborate or contradict this.
  3. Spot reference: intraday underlying ranged $3.46–$3.57; use ~$3.55 as
     phase-9 spot reference (last print at 19:54Z).
- **Open questions:**
  - Is dark pool tape (phase-2) confirming bearish flow or showing
    accumulation that would invalidate the bearish read?
  - Does the LEAP $4 put accumulator have offsetting long stock (phase-2
     blocks) suggesting hedged-long, not directional short?
  - Is `oi_smart_positioning` (phase-3) detecting the LEAP straddle as a vol
     play vs directional?
