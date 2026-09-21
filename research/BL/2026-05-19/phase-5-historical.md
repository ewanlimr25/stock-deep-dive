# Phase 5 — Historical Context & VRP

**Ticker:** BL
**As-of date:** 2026-05-19
**Generated:** 2026-05-19T00:00:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md,
phase-3-positioning.md, phase-4-structure.md

## Summary

Historical context reframes phase 4's "POSITIVE-vs-DEX conflict" decisively:
the gamma stack at $27.5 we see today is **a brand-new structure built over
the last 4 trading days**, not the underlying's baseline. On 2026-05-06 the
total_gex bottomed at **−$1,548,630** with spot at $30.33; by 2026-05-19 it
has flipped to **+$194,349,985** — a **>125× rebuild in 9 sessions**
[HIST:historical_gex_time_series]. Cumulative bullish premium over the
trailing 90 sessions = **$16,023,418**, bearish = **$3,229,350**, **net
+$12,794,068** with `trend_direction=BULLISH`
[HIST:historical_cumulative_premium_flow]. OI is in a **10-day consecutive
build** with `overall_trend=BUILDING`, +24,310 net contracts opened across
the lookback [HIST:historical_oi_trend]. **IV is fundamentally CHEAP vs
realized:** IV30d = **0.678**, realised σ = **0.7668**, `vrp = -0.0889`,
regime **PREMIUM_BUYING** [HIST:historical_vrp]; 1y IV percentile is **70.37**
(NORMAL, z=0.113) [HIST:historical_iv_percentile_zscore]. Counter-evidence:
the market-wide `bullish_flow` signal_backtest from 2026-05-14/15 returned
**win_rate = 0.0% (7/7 down, avg -3.05%)** over the next 20 sessions
[HIST:historical_signal_backtest] — though this sample is market-wide
(MSFT/AAPL/QQQ/SMH/META/AVGO/UPS), not BL-specific, the negative base rate is
**a serious headwind for any pure flow-momentum entry**.

**Net read: VRP says buy premium; OI/GEX/flow says someone is doing exactly
that with size; but recent broad-market bullish_flow backtest has 0% win
rate, so sizing must be conservative until phase 7 confirms.** Conviction
3.5/5 — high on edge-direction, low on near-term timing.

## Key signals

- **GEX flip is recent and violent:** total_gex went from **−$1,548,630** on
  2026-05-06 to **+$194,349,985** on 2026-05-19 — a **>125× rebuild in 9
  sessions**, with the lion's share added in the last two days (May 18 = +$96M,
  May 19 = +$98M additional) [HIST:historical_gex_time_series].
- **Premium flow persistently bullish:** 90d cumulative bullish $16.02M vs
  bearish $3.23M → net **+$12.79M** [HIST:historical_cumulative_premium_flow].
- **OI is in 10-day consecutive build:** `consecutive_build_days=10`,
  `overall_trend=BUILDING`, +24,310 net contracts over 28 sessions
  [HIST:historical_oi_trend].
- **VRP negative → vol is cheap vs realized:** IV30 0.678 < realised 0.7668;
  `vrp=-0.0889`, regime PREMIUM_BUYING [HIST:historical_vrp].
- **Market-wide bullish_flow backtest fired 7×, all losers** (avg
  -3.05%, 20d after firing on 2026-05-14/15)
  [HIST:historical_signal_backtest]. Critical caveat: the 7 names are large-
  cap tech/megacaps — they are NOT BL — but the macro backdrop they failed
  in is the same backdrop BL must rally through.

## Detailed findings

### IV regime [HIST:historical_iv_percentile_zscore,
historical_vrp]

| Metric | Value |
|--------|-------|
| `current_iv30d` | **0.678** (67.8%) |
| `iv_percentile` (252d) | 70.37 |
| `iv_zscore` (252d) | 0.113 |
| `regime` (percentile) | **NORMAL** |
| `realised_vol_30d` | **0.7668** (76.68%) |
| `vrp` = IV − realised | **−0.0889** |
| `regime` (VRP) | **PREMIUM_BUYING** |

**Read:** IV sits at the 70th 1y percentile but the **regime is "vol is
cheap"** because realized has been running hotter than implied. The Dec
$27.5C buyer in phase-1 paid an effective IV of ~78-81% (well above the
67.8% IV30d) — but that's roughly the **realized vol rate**, so they're
paying a fair price by historical realization, not a peak-IV premium. **For
phase 9:** debit structures (long calls, call spreads, debit risk
reversals) are favored by the VRP regime; credit structures (covered
calls, put credit spreads) face headwinds because vol is underpriced
relative to realized.

### Cumulative premium flow (90d)
[HIST:historical_cumulative_premium_flow]

| Metric | Value |
|--------|-------|
| `cumulative_bullish` | **$16,023,418** |
| `cumulative_bearish` | $3,229,350 |
| `net_flow` | **+$12,794,068** |
| `trend_direction` | **BULLISH** |
| Sessions covered | 28 trading days |

**Read:** Bullish premium dominates by ~5:1 across the trailing window.
However the bulk of this concentrates in the last 4 sessions (especially May
18 net +$7.33M, May 19 net +$4.10M from historical_trend). The 90d framing
is therefore a recency-weighted bullish signal — phase-9 must distinguish
the *trend* (genuine multi-month accumulation, consistent with phase-1's
3-of-5 sweep persistence) from *concentration risk* (most of the firepower
is fresh).

### P/C ratio z-score [HIST:historical_pc_ratio_zscore]

- `current_pc_ratio`: 0.0029 (essentially zero — put volume vanished today)
- `mean_pc_ratio` (18d): 1.5022
- `std_pc_ratio` (18d): 2.5064
- `zscore`: −0.598
- `extreme`: **NORMAL**

**Read:** Z-score is below mean but inside one std — not a sentiment
extreme. The raw current PCR of 0.0029 is striking on its own (calls
dominate puts 350:1 today), but the noisy small-sample mean/std (std > mean)
softens this into "NORMAL". **No contrarian fade trigger.**

### GEX time series [HIST:historical_gex_time_series]

Selected trajectory:

| Date | Spot | Total GEX | Regime | ZGL |
|------|------|-----------|--------|-----|
| 2026-03-23 | 39.42 | 2,972 | FULLY_POSITIVE | n/a |
| 2026-04-27 | 31.04 | 40,635 | FULLY_POSITIVE | n/a |
| 2026-05-01 | 33.44 | −103,015 | FULLY_NEGATIVE | n/a |
| 2026-05-05 | 32.32 | −230,160 | FULLY_NEGATIVE | n/a |
| **2026-05-06** | **30.33** | **−1,548,630** | **FULLY_NEGATIVE** | n/a |
| 2026-05-13 | 24.96 | −566,671 | FULLY_NEGATIVE | n/a |
| 2026-05-14 | 26.80 | +42,361 | FULLY_POSITIVE | n/a |
| 2026-05-15 | 27.53 | **+3,322,190** | POSITIVE | 22.51 |
| 2026-05-18 | 29.94 | **+96,098,036** | POSITIVE | 17.94 |
| **2026-05-19** | **29.85** | **+194,349,985** | **POSITIVE** | **25.00** |

**Read — this is the most important table in phase 5:**

1. **Pre-May regime:** BL was in a quiet "FULLY_POSITIVE" regime through
   March (total_gex single-digit thousands) — illiquid, normal, mean-reverting.
2. **Vol-expansion regime:** May 1-13 sees the stock crash from $33.44 to
   $24.96 (−25%) and total_gex tank to −$1.55M (the dealer book briefly
   went **short gamma** during the panic, which mechanically amplified the
   selloff — consistent with the speed of the drop).
3. **Reversal + rebuild:** May 14 spot bounces, GEX flips back to positive
   at +$42k. **Then the institutional rebuild begins:** $3.3M (May 15) →
   $96M (May 18) → $194M (May 19). **9-session change: ~+126× from the
   May 6 low.**

This trajectory makes a strong case that the buyer is **building a long
gamma structure into the bounce off a panic-flush** — a sequence consistent
with smart-money "buy the capitulation" trades, not chasing strength. **The
$25.81 institutional floor from phase 2 corresponds almost exactly to the
May 13 low of $24.96.** The buyer is positioning above the dip.

ZGL has moved up monotonically over the last 3 days: 22.51 → 17.94 → 25.00.
The May 18 ZGL of 17.94 looks low against spot $29.94 — the rebuild was so
fast that today's spot–ZGL gap (29.85 vs 25.00) is the first time the buyer
has a meaningful gamma cushion below them.

### OI trend (28d) [HIST:historical_oi_trend]

| Metric | Value |
|--------|-------|
| `days_analyzed` | 28 |
| `consecutive_build_days` | **10** |
| `total_net_oi_change` | +24,310 |
| `overall_trend` | **BUILDING** |

Daily concentration (selected):

| Date | Net ΔOI | Top contract Δ |
|------|---------|----------------|
| 2026-05-19 | +13,541 | Dec27.5C +13,016 |
| 2026-05-18 | +2,909 | Dec27.5C +2,899 |
| 2026-05-15 | +336 | Dec27.5C +250 |
| 2026-05-14 | +335 | May15P25 +332 (put closed at OPEX) |
| 2026-05-13 | +741 | **Dec18P22.5 +500** (single put cluster) |
| 2026-05-12 | +337 | May15P27.5 +199 (closing trade prior to OPEX) |
| 2026-05-11..04 | <1k each | mostly OPEX-week closures |
| 2026-04-27 | +227 | May15C30 +99, May15C32.5 +98 |
| 2026-03-23 | +2,885 | **Apr17C42.5 +2,264** (prior cycle's big bet — expired worthless given Apr drop) |
| 2026-03-24 | +1,788 | Apr17C42.5 +1,754 |

**Read:**
- **The Dec18C27.5 buildup is concentrated almost entirely on May 18-19**
  (~16,000 of the 16,178 total OI added in two days). May 15 was the seed
  (+250).
- A **prior, smaller, separate** Dec18P22.5 +500 OI was opened on 2026-05-13
  at the absolute low. This is a put SOLD (a covered or naked write at $22.5)
  — strongly bullish given the buyer's willingness to take pin risk at that
  level — and it dovetails with the institutional floor at $24.90-25.81.
- **A prior bullish thesis FAILED:** the Apr17C42.5 +2,264 / +501 build on
  Mar 23-24 (when spot was $39-40) appears to have expired worthless during
  the late-April/early-May decline (spot ~$30-32 on Apr 17). **Whoever rolled
  through that may be the same buyer — second-time-around — or, more
  cautiously, this name has a history of one-time bullish bets that don't
  pay off.** Phase-9 must size for the possibility that today's bet is also
  premature.

### Multi-day trend (price + flow + IV) [HIST:historical_trend]

Selected last 7 sessions:

| Date | Close | IV30d | IV rank | Flow | Net flow | Bull$ | Bear$ |
|------|-------|-------|---------|------|----------|-------|-------|
| 2026-05-19 | 30.03 | 0.678 | 64.6 | **bullish** | +$4.10M | $4.19M | $87k |
| 2026-05-18 | 29.81 | 0.562 | 50.6 | **bullish** | +$7.33M | $9.47M | $2.15M |
| 2026-05-15 | 27.29 | 0.666 | 60.3 | **bullish** | +$1.46M | $1.54M | $78k |
| 2026-05-14 | 26.84 | 0.618 | 58.2 | **bullish** | +$168k | $171k | $4k |
| 2026-05-13 | 25.23 | 0.668 | 64.9 | bearish | −$19k | $4k | $23k |
| 2026-05-12 | 26.21 | 0.634 | 60.4 | bearish | −$58k | $32k | $90k |
| 2026-05-11 | 27.50 | 0.567 | 51.3 | bullish | +$11k | $20k | $9k |

**Read:**
- **Price arc:** $40 (Mar 23 peak) → $24.96 (May 13 trough) → $30.03 (today)
  — **+20% off the low in 6 sessions**. Buyer is not buying the dip; they are
  buying the **bounce-confirmation**.
- **Flow flipped to bullish on May 14** and has stayed bullish 6 sessions in
  a row, with magnitude expanding (+$168k → +$1.46M → +$7.33M → +$4.10M).
- **IV rank trajectory:** dropped from ~100 (late April) → 49 (May 6) →
  64.6 today. Today's IV (rank 64.6, percentile 70) is **above the realized
  recent mean** but **below the late-April peak** — call buyers are not
  paying the absolute top of the IV range, but they are paying near it.
- bullish_days vs bearish_days over 28 sessions: **13 vs 15** — slightly
  more bearish sessions in count, but bullish sessions carry **5x the
  premium** (cumulative skew). The setup is "lopsided dollar conviction"
  not "lopsided session count."

### Signal backtest [HIST:historical_signal_backtest]

`signal_type = bullish_flow`, `lookback_days = 20`, `top_n = 20`:

| Ticker | Signal date | Price on signal | Price after 20d | Δ% |
|--------|-------------|-----------------|------------------|-----|
| MSFT | 2026-05-15 | 422.05 | 417.42 | −1.10% |
| AAPL | 2026-05-15 | 300.37 | 298.97 | −0.47% |
| UPS | 2026-05-15 | 99.00 | 96.83 | −2.19% |
| QQQ | 2026-05-14 | 719.79 | 701.53 | −2.54% |
| SMH | 2026-05-14 | 578.34 | 543.96 | −5.94% |
| META | 2026-05-14 | 618.43 | 602.61 | −2.56% |
| AVGO | 2026-05-14 | 439.79 | 411.07 | −6.53% |

- `total_signals`: 7
- `win_rate`: **0.0%** (0 of 7 winners)
- `avg_move_pct`: **−3.05%**

**Read — what this means and does NOT mean:**
- **What it means:** every recent firing of the market-wide bullish_flow
  pattern produced a **loss** 20 days later. The macro tape since May 14 has
  been hostile to follow-through on bullish call buying. This is a real,
  current, broad regime headwind.
- **What it does NOT mean:** the sample is **megacap tech + UPS**, names
  with already-rich valuations and macro-sensitivity that diverge from
  small-cap idiosyncratic stories. BL is a $3-5B market-cap accounting
  software name with a unique flow profile (3-of-5 sweep persistence, dark-
  pool aggression, 99% concentrated GEX) that is **not represented in this
  backtest cohort**. The backtest is a regime warning, not a verdict on BL.
- **Phase-9 application:** apply a **conservative haircut** to position size
  (≤50% of Kelly base) and **shorten the time horizon** on entry — do not
  marry a 6-month thesis to a regime where 20-day bullish-flow setups are
  0-for-7. Use option structures (debit spreads, not naked calls) that cap
  premium decay if the regime keeps fading bullish signals.

## Cross-phase confluence

| Datapoint | Echo |
|-----------|------|
| GEX rebuild +126× in 9 sessions | Phase 3: +13,016 OI in one day on Dec 27.5C; Phase 1: $4.14M ask sweeps; Phase 4: $194M total GEX |
| VRP negative (premium-buying) | Phase 1: buyer paid 78-81% IV (above IV30 but at realized) — they're paying fair-by-realized |
| 10 consecutive OI build days | Phase 1: sweep persistence 3-of-5 sessions; Phase 2: 5-day institutional floor cluster $7.7M |
| Spot bounce +20% off 5/13 low ($24.96 → $30.03) | Phase 2: institutional floor exactly at $24.90-25.81; Phase 4: today's ZGL $25 |
| Apr 17 $42.5C campaign (Mar 23-24, 2,264 + 501 contracts) expired worthless | Cautionary — same playbook, same buyer profile, prior loser; phase-9 must size for repeat risk |
| Market-wide bullish_flow backtest 0/7 | Independent of BL but warns this isn't a regime to oversize |

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `historical_iv_percentile_zscore` | `{symbol:BL, lookback-days:252}` | IV30 0.678, percentile 70.37, NORMAL |
| `historical_vrp` | `{symbol:BL, realised-window-days:30, date:2026-05-19}` | VRP −0.0889, **PREMIUM_BUYING** |
| `historical_cumulative_premium_flow` | `{symbol:BL, days:90}` | Net +$12.79M, BULLISH |
| `historical_pc_ratio_zscore` | `{symbol:BL, lookback-days:20}` | PCR 0.003, z=−0.598, NORMAL |
| `historical_gex_time_series` | `{symbol:BL, days:30, dte-max:365}` | 9-session rebuild from −$1.55M → +$194M |
| `historical_oi_trend` | `{symbol:BL, days:30, top-n:10}` | consecutive_build_days 10, BUILDING, +24,310 total |
| `historical_trend` | `{symbol:BL, days:30}` | Today bullish; 13 bull vs 15 bear days, but bull $ = 5× bear $ |
| `historical_signal_backtest` | `{signal-type:bullish_flow, lookback-days:20, top-n:20}` | 7 signals, **0% win rate**, avg −3.05% |

## Tool errors

None.

## Verdict for downstream phases

- **Volatility regime:** **PREMIUM_BUYING** — IV cheap vs realized. Favors
  debit structures.
- **Premium environment:** Bullish-net by 5:1 over 90 days; persistence is
  real but back-loaded in the last 4 sessions.
- **Conviction this signal is HISTORICALLY EDGE-POSITIVE:** **3.5 / 5**
  (downgraded from 5 only by the market-wide bullish_flow backtest 0/7;
  upgraded back from 3 by the VRP and consecutive OI build).
- **Three specific datapoints phase 9 must remember:**
  1. **VRP = −0.0889, regime PREMIUM_BUYING** → debit structure preferred,
     not credit.
  2. **GEX rebuild was 126× in 9 sessions** → the gamma magnet at $27.5 is a
     freshly-built lever, not a baseline feature; it can vanish as fast as it
     was built if the buyer pulls.
  3. **Market-wide bullish_flow backtest 0/7 (avg −3.05% / 20d)** → conservative
     sizing; consider shorter-DTE expression of the long thesis as a hedged-in
     way to participate without paying for the full Dec horizon.
- **Open questions:**
  - **Is there a known earnings date** in the August–December window that
    explains why the buyer chose Dec 18 expiry? → phase 7
    (`insights_earnings_play`, `screener_earnings_catalyst`).
  - **What macro regime** does BL face? Is the 0/7 signal_backtest reflecting
    broad risk-off, sector rotation away from software, or interest-rate
    pressure on small-cap multiples? → phase 6.
  - **Did the same buyer profile drive the Mar 23-24 Apr-17 $42.5C campaign
    that expired worthless?** If yes, this is "same playbook, different
    cycle" and we should expect similar conviction but also accept that the
    cycle's edge has misfired before. → can be partially explored in phase 7
    (`insights_institutional_accumulation`).
