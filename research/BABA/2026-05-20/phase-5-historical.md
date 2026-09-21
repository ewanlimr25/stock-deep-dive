# Phase 5 — Historical Context & VRP

**Ticker:** BABA
**As-of date:** 2026-05-20 (data: 2026-05-19)
**Generated:** 2026-05-20T00:35:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-4-structure.md
**Spot reference:** $135.68 close, 2026-05-19

## Summary

BABA's vol regime is **NORMAL but cheap-to-realized**: 30-day IV at **41.5%
(33rd percentile, z = −0.68)** with **realized vol at 46.6%** producing
**VRP = −5.1pp (PREMIUM_BUYING)** — debit structures (long calls, long
straddles, debit verticals) are statistically favored. **90-day cumulative
premium flow is +$336M net bullish** ($1.36B bullish vs $1.03B bearish) — a
persistent 28-session bull-side accretion that aligns with phase-1's 5-day
sweep persistence. **OI has built for 22 consecutive sessions** (institutional
campaign). However, **two big counter-signals fire**: (1) BABA's 28-day GEX
regime has flipped **13 times** in 28 sessions — exactly the whippy /
high-realized environment the long-gamma readout depends on — and TODAY itself
was a regime flip (NEG → POS); (2) the market-wide **`bullish_flow` signal
backtest from 2026-05-13 → 2026-05-18 shows a 6.7% win rate (1/15) with an
average 20-day move of −1.62%**, meaning institutional bullish positioning over
the past week has overwhelmingly *failed* on lookforward. This forces
heavy de-rating of phase-1's bullish conviction.

## Key signals

- **VRP = −0.0506** (IV 41.5% vs realized 46.6%) → vol cheap, **favor
  premium-buying / debit structures** [HIST:vrp].
- **IV percentile 33.33 / z-score −0.68** → 1Y NORMAL but on the cheap side —
  room for IV expansion ahead of any catalyst [HIST:iv_percentile_zscore].
- **Cumulative 90d premium flow +$336.4M net bullish** ($1.36B bull vs $1.03B
  bear) — persistent multi-week institutional bullish bias [HIST:cumulative_premium_flow].
- **22 consecutive sessions of OI build** — sustained campaign, not a flash
  [HIST:oi_trend].
- **GEX has flipped 13× in 28 sessions** including TODAY (NEG→POS) — the
  long-gamma regime read in phase-4 is **fragile**, not durable
  [HIST:gex_time_series].
- **`bullish_flow` 20-day backtest 2026-05-13 to 2026-05-18: 6.7% win rate,
  avg −1.62%** — recent market-wide bullish-flow signals have failed; sample
  includes TSLA −7.4%, AVGO −4.1%, GOOGL −4.5% [HIST:signal_backtest].
- P/C ratio z-score −0.47 (current 0.32 vs mean 0.40, σ 0.16) → not yet at
  contrarian extreme but tilted call-heavy [HIST:pc_ratio_zscore].

## Detailed findings

### IV regime — current, percentile, VRP

| Field | Value |
|------|------|
| Current IV30d | **0.4153 (41.5%)** |
| IV percentile (252d) | 33.33 |
| IV z-score (252d) | −0.68 |
| Regime tag | NORMAL |
| Realized vol (30d) | 0.4660 (46.6%) |
| **VRP (IV30d − realized30d)** | **−0.0506** |
| VRP regime | **PREMIUM_BUYING** |

Interpretation: implieds are below realized — selling premium here means
under-collecting for the realized vol the underlying is generating. Buying
premium has positive expected value if realized continues at trailing rate.
This **directly supports** phase-1's interpretation that the LEAP risk
reversal and Jun18 OTM call sweeps are sized as conviction buys, not "writing
calls because they look expensive." [HIST:iv_percentile_zscore] [HIST:vrp]

### Cumulative premium flow (28 sessions / 90d window)

| Field | Value |
|------|------|
| `cumulative_bullish` | $1,363,162,557 |
| `cumulative_bearish` | $1,026,750,110 |
| **`net_flow`** | **+$336,412,447** |
| `trend_direction` | **BULLISH** |
| Dates covered | 28 sessions, 2026-03-13 → 2026-05-19 |

The +$336M net bullish premium is **consistent and material**. Combined with
phase-1's 5-day sweep premium of $217M and phase-3's 22-session consecutive
OI buildup, the institutional thesis is **multi-week**, not opportunistic.
[HIST:cumulative_premium_flow]

### P/C ratio z-score

| Field | Value |
|------|------|
| Current P/C | 0.32 |
| 20d mean | 0.397 |
| 20d σ | 0.163 |
| **z-score** | **−0.473** |
| Extreme tag | NORMAL |

Slightly call-heavy vs trailing 20d, but not at an actionable extreme.
Consistent with phase-4's COMPLACENT call-side skew. [HIST:pc_ratio_zscore]

### GEX time series (28 sessions)

Total of **13 regime flips in 28 sessions** — this is exceptionally whippy.
Notable flips:

| Date | From → To | Spot | ZGL | Comment |
|------|-----------|----:|----:|------|
| 2026-05-13 | NEG → POS | 144.00 | 75.05 | rally-day push above ZGL — peak day |
| 2026-05-14 | (stays POS) | 141.51 | 139.81 | tight ZGL = vulnerable |
| 2026-05-15 | POS → NEG | 133.14 | 139.35 | $145 → $133 in 2 sessions; ZGL crossed |
| 2026-05-18 | (NEG) | 133.58 | 134.79 | basing at lower ZGL |
| **2026-05-19** | **NEG → POS** | **135.70** | **135.66** | **TODAY: regime flip back to positive, ZGL within 4 cents of spot** |

Read: the long-gamma regime in phase-4 is **freshly-minted, not entrenched**.
Historical pattern: BABA has *not* held positive-gamma regime for more than
1–2 sessions in the past month before flipping again. Phase 4's read that
"$140 wall acts as ceiling" is correct *for today's chain*, but
empirically the regime is unstable. Phase 9 must size for **regime
fragility**. [HIST:gex_time_series]

### OI trend — consecutive build days

| Field | Value |
|------|------|
| `consecutive_build_days` | **22** |
| Top contracts on most recent day | $145C 5/29 (+2,415), $142C 5/22 (+1,702), $135C 5/22 (+1,438), $136C 5/22 (+1,435), $130P 6/18 (+1,268) |

22 consecutive sessions of net OI build = institutional engagement is
**continuous**, not pulsed. Phase 3's tenor split (near-term writes vs
LEAP buys) is the *composition* of this 22-day build. [HIST:oi_trend]

### Multi-day flow trend (latest 10 of 28 sessions)

| Date | Close | IV30d | IV rank | PCR | Flow direction | Net flow |
|------|-----:|------:|------:|----:|---------------|--------:|
| 2026-05-19 | 135.68 | 41.5% | 41 | 0.32 | bullish | +$1.33M |
| 2026-05-18 | 133.26 | 41.4% | 43 | 0.26 | bearish | −$4.75M |
| 2026-05-15 | 132.57 | 41.4% | 40 | 0.29 | bearish | −$10.27M |
| 2026-05-14 | 141.12 | 43.0% | 49 | 0.25 | bearish | −$10.87M |
| 2026-05-13 | **145.81** | **51.1%** | **83** | 0.21 | bullish | **+$12.58M** |
| 2026-05-12 | 134.78 | 47.6% | 68 | 0.33 | bearish | −$2.35M |
| 2026-05-11 | 137.30 | 46.4% | 63 | 0.30 | bearish | −$6.54M |
| 2026-05-08 | 140.01 | 49.1% | 74 | 0.36 | bearish | −$3.66M |
| 2026-05-07 | 141.00 | 49.6% | 76 | 0.36 | bullish | +$0.55M |
| 2026-05-06 | 141.44 | 49.8% | 78 | 0.26 | bullish | +$18.66M |

Pattern: **2026-05-13 was the peak day** — close $145.81 (matching phase-2
DP cluster), IV rank 83, +$12.6M bullish flow. Since then BABA has bled
$13 / -9% in 2 sessions to $132.57, with IV crushing from 51% to 41.5% (vol
declined as price fell — *consistent with a vanna-driven mechanical sell-off
post-event*, exactly what phase-4 warned about for post-OPEX).

The **bearish 17 vs bullish 11 day count** is mildly bearish balance —
recent sessions have been more often net-distribution than net-accumulation,
even though the *cumulative* premium magnitude favors bullish (+$336M). The
bullish days are larger in size; the bearish days are more numerous.
[HIST:trend]

### Signal backtest — bullish_flow (last 20 trading days)

| Field | Value |
|------|------|
| `signal_type` | bullish_flow |
| `lookback_days` | 20 |
| Total signals | 15 |
| Tickers | AMZN, AMD, RCL, MSFT, AAPL, UPS, QQQ, SMH, META, AVGO, TSLA, NVDA, GOOGL, META, QQQ |
| `avg_move_pct` | **−1.62%** |
| **`win_rate`** | **6.7%** (1/15) |

The single winner was AMD (+5.97%). All 14 other recent bullish_flow
signals from May 13–18 produced **negative 20-day moves**:

| Ticker | Signal date | 20d move |
|--------|------------|--------:|
| TSLA | 2026-05-13 | **−7.36%** |
| AVGO | 2026-05-14 | −4.10% |
| GOOGL | 2026-05-13 | −4.53% |
| RCL | 2026-05-18 | −3.24% |
| SMH | 2026-05-14 | −2.81% |
| META | 2026-05-14 | −1.98% |
| META | 2026-05-13 | −1.70% |
| MSFT | 2026-05-15 | −1.24% |
| QQQ | 2026-05-14 | −1.20% |
| UPS | 2026-05-15 | −0.96% |
| QQQ | 2026-05-13 | −0.51% |
| AAPL | 2026-05-15 | −0.43% |
| NVDA | 2026-05-13 | −0.22% |
| AMZN | 2026-05-18 | −0.02% |
| AMD | 2026-05-18 | **+5.97%** |

This is a **systemic counter-signal**. Recent bullish_flow signatures
across mega-cap tech & broad indices have been **fade-the-rally** rather
than continuation. BABA is not in the sample but the **market regime is
hostile to bullish-flow continuation**. Phase 6 (macro) must address
*why* — is this earnings-window vol crush, broad de-risking, or
something else? Phase 9 must use this to discount the headline thesis.
[HIST:signal_backtest]

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `historical_iv_percentile_zscore` | symbol=BABA, lookback=252 | IV 41.5%, pct 33, z −0.68, NORMAL |
| `historical_vrp` | symbol=BABA, realised_window=30 | VRP −5.1pp, PREMIUM_BUYING |
| `historical_cumulative_premium_flow` | symbol=BABA, days=90 | net +$336.4M, BULLISH, 28 sessions |
| `historical_pc_ratio_zscore` | symbol=BABA, lookback=20 | PCR 0.32, z −0.47, NORMAL |
| `historical_gex_time_series` | symbol=BABA, days=30 | 13 regime flips; today NEG→POS |
| `historical_oi_trend` | symbol=BABA, days=30, top_n=10 | 22 consecutive build days |
| `historical_trend` | symbol=BABA, days=30 | bearish 17 vs bullish 11; peak 5/13 |
| `historical_signal_backtest` | signal=bullish_flow, lookback=20 | win_rate 6.7%, avg −1.62% (mkt-wide) |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **mixed** — premium is cheap to realized (favor
  long premium / debit structures) and 90d institutional flow is genuinely
  net-bullish, but the **recent 20-day backtest of bullish_flow** signals
  has been catastrophically negative, and BABA's GEX regime is *unstable*
  (13 flips in 28 sessions).
- **Conviction that today's bullish setup is HISTORICALLY EDGE-POSITIVE:**
  **2 / 5** — the structural signals are present but the recent base-rate
  has been hostile.
- **Three specific data points for downstream:**
  1. **IV percentile 33** + **VRP −5.1pp** → debit structures preferred
     over credit; long-gamma exposure has positive carry vs realized.
  2. **Cumulative net flow +$336M / 90d / 22-day OI build** → the
     institutional campaign is real and persistent.
  3. **`bullish_flow` win rate 6.7% / avg −1.62%** in the 5 trading days
     immediately preceding today → **this is the single biggest risk
     factor for the entire deep dive** and phase 9 must size accordingly
     (smaller, with tight invalidation).
- **Open questions:**
  - Did BABA report earnings on/around May 13 (the peak day, IV rank 83)?
    The IV-rank crush from 83 → 41 in 4 sessions is the signature of an
    earnings reset. Phase 6 catalyst calendar must confirm.
  - Is the macro regime in mid-May 2026 (broad mega-cap fade) cyclical
    or structural? Phase 6 macro must address.
  - Does the BABA-specific 5-day sweep persistence of $217M + 22-day OI
    build give us reason to treat BABA as *different* from the broader
    `bullish_flow` cohort that failed? (Tentative yes — but phase 9 must
    explicitly defend this exemption rather than assume it.)
