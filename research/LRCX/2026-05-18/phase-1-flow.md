# Phase 1 — Options Flow

**Ticker:** LRCX
**As-of date (requested):** 2026-05-18
**Effective as-of date (data):** 2026-05-15
**Underlying price (intraday range observed):** $282.32 – $287.23 (closing area ~$285–286)
**Generated:** 2026-05-18T00:00:00Z
**Upstream phases cited:** phase-0-intake.md

## Summary

Friday 5/15 tape on LRCX was **heavy institutional but directionally mixed**:
$5M+ of call premium hit the BID across May/Jun OTM strikes ($290–$320), and
$1M+ of deep ITM puts also hit the BID — classic **call-overwrite +
put-write** yield-harvest signature, neutral-to-mildly-bearish near-term and
mildly-bullish synthetic medium-term. Persistence is the loudest signal:
`hot_chains_sweep_persistence` puts LRCX in the top sweep tape **5 of 5
sessions** with **$38.6M** in total sweep premium and consistency score 1.0
(max). Sector tape is bearish — `SMH 5/22 500P` shows $48.8M premium with
106k contracts hitting the bid; LRCX-specific tape is more two-sided.

## Key signals

- LRCX **on top sweep board 5/5 sessions, $38.6M** total premium, consistency
  1.0, dominant = mixed [FLOW:hot_chains_sweep_persistence].
- Largest single trade is a **$1.03M Jan'27 260P sold at bid** (delta -0.33,
  ITM put-write — synthetic long bias) [FLOW:top_premium_trades].
- **Four of the top six sweeps are call-side BID prints** (5/22 295C $1.13M,
  5/22 300C $1.05M, 6/18 320C $955k, 5/22 302.5C $742k) — overwrite campaign
  above $290 [FLOW:sweeps].
- Counter-flow long call: **6/5 340C ASK $971k, vol/OI 38.3**, +0.15 delta
  lottery — far-OTM directional call buying [FLOW:unusual_volume, sweeps].
- Sector overlay: **SMH 5/22 500P bid-side $48.8M** premium, net flow
  -106k contracts — broader semi tape is bearish-positioned
  [FLOW:hot_chains_smart_money_flow bearish].

## Detailed findings

### Sweeps (top 10 by premium, $100k+ floor)

| Strike / Expiry | Type | Side | Premium | Size | Avg price | Read |
|-----------------|------|------|---------|------|-----------|------|
| 295 / 2026-05-22 | call | **bid** | $1.13M | 1567 | $7.02 | Call write |
| 260 / 2027-01-15 | put | **bid** | $1.11M | 270 | $41.49 | ITM put write (bullish synth) |
| 300 / 2026-05-22 | call | **bid** | $1.05M | 1652 | $5.15 | Call write |
| 340 / 2026-06-05 | call | **ask** | $0.97M | 2851 | $3.36 | Long OTM call (bullish lotto) |
| 320 / 2026-06-18 | call | **bid** | $0.96M | 934 | $9.91 | Call write |
| 310 / 2026-06-18 | put | **bid** | $0.80M | 212 | $36.66 | ITM put write |
| 302.5 / 2026-05-22 | call | **bid** | $0.74M | 1524 | $4.89 | Call write |
| 290 / 2026-06-18 | call | **bid** | $0.57M | 277 | $20.25 | ITM/ATM call write |
| 310 / 2026-06-18 | call | **ask** | $0.55M | 409 | $13.22 | Long OTM call |
| 260 / 2026-05-22 | put | **ask** | $0.52M | 1624 | $3.00 | Long OTM put (hedge) |

**Net read:** bid-side call premium ~$5.0M vs ask-side call premium ~$1.7M →
**~3:1 call selling**. On puts, ITM put-write premium (~$2.0M) is the largest
single category; ATM/OTM put buying is the smaller $0.5–0.9M downside hedge
bucket. Net flavor: yield-harvest with a ceiling near $300–$320 and a
willingness to own stock around $260–$270.

### New positioning (unusual_volume, vol/OI ≥ 3)

| Strike / Expiry | Type | OI | Volume | vol/OI | Premium | Side dominance |
|-----------------|------|----|--------|--------|---------|----------------|
| 170 / 2026-07-17 | put | 4 | 1006 | **251.5** | $112k | Tail / closing trade |
| 340 / 2026-06-05 | call | 75 | 2873 | 38.3 | $978k | **ask** (long) |
| 295 / 2026-05-22 | call | 148 | 1633 | 11.0 | $1.18M | bid (write) |
| 302.5 / 2026-05-22 | call | 297 | 1592 | 5.36 | $775k | bid (write) |
| 260 / 2026-05-22 | put | 433 | 1716 | 3.96 | $546k | two-sided |
| 330 / 2026-05-22 | call | 179 | 687 | 3.84 | $58k | small |
| 300 / 2026-05-22 | call | 706 | 2179 | 3.09 | $1.34M | bid (write) |

The cleanest new opener is **6/5 340C ask-side $978k**: low OI (75), 2873 new
contracts, +0.15 delta, IV ~66%. This is a **directional long-call lottery**
betting on a ~20% rip within 21 calendar days. Stands out as the only
material ask-side opener.

### Largest premium prints (top 10 by single-trade $)

All from `options_flow_top_premium_trades`, executed 5/15:

| Time (UTC) | Strike / Expiry | Type | Side | Premium | Size | Δ |
|------------|-----------------|------|------|---------|------|---|
| 16:06 | 260 / 2027-01-15 | put | bid | $1.03M | 250 | -0.33 |
| 13:37 | 300 / 2026-05-22 | call | bid | $0.97M | 1496 | +0.33 |
| 16:27 | 295 / 2026-05-22 | call | bid | $0.92M | 1273 | +0.39 |
| 16:24 | 320 / 2026-06-18 | call | bid | $0.89M | 865 | +0.31 |
| 15:04 | 310 / 2026-06-18 | put | bid | $0.76M | 200 | -0.65 |
| 16:27 | 302.5 / 2026-05-22 | call | bid | $0.62M | 1273 | +0.30 |
| 13:37 | 260 / 2026-05-22 | put | ask | $0.48M | 1496 | -0.18 |
| 14:25 | 135 / 2028-01-21 | call | bid | $0.43M | 25 | +0.90 |
| 14:25 | 150 / 2028-01-21 | call | ask | $0.41M | 25 | +0.88 |
| 14:23 | 230 / 2026-05-29 | call | ask | $0.28M | 50 | +0.94 |

Pattern: the 13:37 print pair (300C-bid + 260P-ask, same 1496 size) is a
**risk-reversal short / "short collar"** = sold 300C, bought 260P. Bearish
delta but small notional vs the rest of the day. The 16:27 print pair (295C
+ 302.5C, same 1273 size each) is a **call-write across two adjacent OTM
strikes** — overwriting the curve. The 14:25 print pair (Jan'28 135C bid +
150C ask, same 25 size) is a **bull call vertical roll / diagonal**: sold
deep-ITM Jan'28 135C, bought slightly-less-ITM Jan'28 150C — equivalent to
booking gains on a synthetic long while keeping LEAP exposure.

### IV outliers + Greeks

- IV outliers are non-material: only thin tail-put strikes (5/22 125P at
  188% IV, 6/18 100P at 122% IV), $4k and $259 premium respectively
  [FLOW:iv_outliers]. No volatility tantrum.
- Greek screener confirms the directional read: top-15 by premium is
  dominated by bid-side ~+0.30Δ short-dated calls (theta-positive yield) and
  bid-side -0.30 to -0.65Δ ITM-leaning puts (delta-positive synthetic long).

### Smart money flow (market-wide; LRCX context only)

Neither bullish nor bearish smart_money_flow leaderboards surface LRCX in
the top 25. The semi-sector ETF SMH dominates the bearish list:
**5/22 500P, $48.8M premium, ask/bid ratio 0.116, net flow -105,976**. SMH
500 strike vs current ~$580–$600 SMH is a 14–17% OTM downside hedge or
outright bet. Phase 4 should watch SMH/LRCX correlation — sector dealer
hedging will spill into LRCX gamma.

### Sweep persistence (5-day)

```
LRCX  | sessions_in_top: 5  | consistency: 1.0  | direction: mixed
       | total_sweep_premium: $38.6M
```

LRCX is one of the most consistently swept tickers in the tape this week.
Conviction is unambiguous; **direction is the open question** — phase 2
(dark pool absorption) and phase 3 (OI delta) must resolve whether the
multi-day campaign is accumulation or distribution.

## Tool calls (audit trail)

| Tool | Args | Result |
|------|------|--------|
| `mcp__uw-pp__options_flow_sweeps` | symbol=LRCX, min-premium=100000, top-n=25, date=2026-05-15 | 25 rows |
| `mcp__uw-pp__options_flow_unusual_volume` | symbol=LRCX, min-vol-oi-ratio=3, top-n=25, date=2026-05-15 | 7 rows |
| `mcp__uw-pp__options_flow_top_premium_trades` | symbol=LRCX, top-n=25, date=2026-05-15 | 25 rows |
| `mcp__uw-pp__options_flow_iv_outliers` | symbol=LRCX, top-n=15, date=2026-05-15 | 2 rows |
| `mcp__uw-pp__options_flow_greek_screener` | symbol=LRCX, top-n=15, sort-by=premium, date=2026-05-15 | 15 rows |
| `mcp__uw-pp__hot_chains_smart_money_flow` | direction=bullish, top-n=25, min-volume=500, date=2026-05-15 | 25 rows (no LRCX) |
| `mcp__uw-pp__hot_chains_smart_money_flow` | direction=bearish, top-n=25, min-volume=500, date=2026-05-15 | 25 rows (SMH headline) |
| `mcp__uw-pp__hot_chains_sweep_persistence` | days=5, top-n=20, symbol=LRCX | 1 row (LRCX 5/5) |
| `mcp__uw-pp__hot_chains_sweep_ratio` | top-n=25, min-volume=500, min-sweep-ratio=0.3, date=2026-05-15 | 25 rows (no LRCX) |

## Tool errors

(none)

## Verdict for downstream phases

- **Bias from this phase:** **mixed-with-yield-harvest tilt**. Single-name
  tape is neither cleanly bullish nor cleanly bearish; dominant institutional
  behavior is **selling calls above $290 and selling puts below $270**, with
  a small but real long-call lottery on 6/5 340C and a small bearish collar
  via 5/22 300C/260P. Net delta on top-25 sweeps is **modestly negative**
  near-term (call-write dominates), modestly **positive** synthetic via the
  Jan'27 260P write.
- **Conviction (in the flow signal, not direction):** **4/5**. Premium magnitude,
  sweep persistence, and trade-pair coherence are all institutional grade.
  Directional conviction (in any direction) is only **2/5** until phase 2
  resolves whether dark-pool absorption confirms accumulation or
  distribution.
- **Three datapoints downstream must remember:**
  1. **Implied ceiling $300–$320 / floor ~$260** via the call-write +
     ITM-put-write structure. Phase 4 should map this against dealer gamma
     walls.
  2. **6/5 340C ask-side $978k** is the single coherent directional long bet
     on the tape (~21 DTE, +20% strike). Phase 9 sizing must respect this
     as the bull-case marker.
  3. **SMH 5/22 500P $48.8M bid-side** = sector hedging is fully on. LRCX
     beta to SMH will pull it lower if SMH cracks $500.
- **Open questions:**
  - Dark pool: are blocks confirming accumulation in the $280–$290 range, or
    are they distribution prints? (phase 2)
  - OI delta: did 5/22 295C and 5/22 300C OI EXPAND (new writes) or CONTRACT
    (closing)? (phase 3)
  - Gamma: where is the dealer gamma flip and pin? Call walls at 300 / 320
    are obvious candidates. (phase 4)
  - Earnings: is LRCX inside or outside an earnings window through 7/17?
    Tail-put activity (170P) hints at a long-dated catalyst. (phase 5/6)
