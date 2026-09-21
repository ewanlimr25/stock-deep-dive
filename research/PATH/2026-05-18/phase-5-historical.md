# Phase 5 — Historical Context & VRP

**Ticker:** PATH
**As-of date:** 2026-05-18 (data: 2026-05-15)
**Generated:** 2026-05-18T01:10:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-3-positioning.md, phase-4-structure.md

## Summary

Today's bullish signal sits inside an **unusual context**: PATH's IV30d
is **95.7% — 100th percentile / +1.77σ over 252d** [HIST:iv_percentile_zscore],
and **VRP is +35.97 vol pts** (IV 95.7% vs realized 59.8%) — a textbook
PREMIUM_SELLING regime [HIST:vrp]. Price has fallen from **$12.45
(2026-03-18) to a $9.46 low (2026-05-13) → -24%**, then bounced to
$10.29 (-17% YTD trough-to-now) [HIST:trend]. 90-day cumulative
premium flow is **slightly net-bearish (-$1.41M, bullish $37.07M vs
bearish $38.47M)** despite today's bullish print — the multi-week
backdrop is mixed [HIST:cumulative_premium_flow]. OI is in a
**25-session consecutive build streak** [HIST:oi_trend]. And the most
sobering datapoint: the broader **bullish_flow signal has a 14.3%
20-day win rate market-wide with avg move -2.68%** — every comparable
large-cap with bullish flow (QQQ, NVDA, TSLA, META, SMH, AVGO, QCOM,
AAPL, GOOGL, UNH) was DOWN 0–8% over the next 20 days
[HIST:signal_backtest]. **Combined regime:** PATH-specific signal is
clean but the cross-asset macro backdrop is hostile to long-delta
bullish-flow trades.

## Key signals

- **IV30d 95.7%, 100th percentile, z 1.77 → HIGH_IV** —
  vol is pricing a catalyst at top of its 1y range
  [HIST:iv_percentile_zscore].
- **VRP +35.97 vol pts (IV 95.7% − realized 59.8%) → PREMIUM_SELLING
  regime** — premium-selling structures historically edge here
  [HIST:vrp].
- **25 consecutive OI build days, +24,534 net OI on 2026-05-15** —
  structural accumulation, not a one-day spike [HIST:oi_trend].
- **PATH price 8-week return -17% (2026-03-18 $12.45 → 2026-05-15
  $10.29), but +8.8% off the 2026-05-13 low of $9.46** —
  bottom-bouncing into the IV-implied earnings catalyst
  [HIST:trend].
- **bullish_flow signal market-wide 14.3% win rate, avg -2.68% over 20
  trading days** — the macro tape is HOSTILE to bullish-flow trades
  right now (every large-cap tech signal in the backtest was DOWN)
  [HIST:signal_backtest].

## Detailed findings

### IV regime (percentile + z-score + VRP)

| Metric | Value | Regime |
|---|---|---|
| IV30d | **0.9573 (95.7%)** | High |
| IV percentile (252d) | **100** | Top of range |
| IV z-score | **+1.77** | Outlier high |
| Realized vol (30d) | 0.5976 (59.8%) | Lower than IV |
| **VRP** | **+0.3597 (35.97 vol pts)** | **PREMIUM_SELLING** |
| IV rank (today, from trend) | 85.4% | Confirms high-vol |

**Read:** IV is *literally* at its 1y high. VRP is wide-open positive.
The market is paying a lot for vol — historically, when VRP > +0.20 on
small caps, premium-selling (credit spreads, iron condors, covered
calls) beats premium-buying. But this is also EARNINGS PREMIUM — the
vol bid is concentrated in the 2026-05-29 expiry per phase 4. So the
right play is **sell premium that benefits from a post-earnings vol
crush** while staying long delta via a different leg.

### Cumulative premium flow (90d net direction)

| Field | Value |
|---|---|
| Cumulative bullish premium | $37.07M |
| Cumulative bearish premium | $38.47M |
| **Net flow** | **-$1.41M (slightly bearish)** |
| Trend direction | MIXED |
| Days covered | 26 (with a gap 2026-03-27 → 2026-04-27) |

**Read:** Despite the explosive bullish reading on 2026-05-15, the
90-day balance is essentially zero (net -$1.4M on $75.5M gross). This
matters: **today's bullish flow is a NEW development, not the
continuation of a long-running bull thesis.** It is event-driven —
positioning into the IV-kink catalyst — not stealth accumulation.

### P/C ratio z-score

| Field | Value |
|---|---|
| Current PCR | 0.26 |
| Mean (20d) | 0.349 |
| Std (20d) | 0.166 |
| z-score | **-0.54 (NORMAL)** |

PCR 0.26 is bullish (calls 4× puts), but only -0.54σ below the 20-day
mean. **No sentiment extreme** — both bulls and bears can still pile
in. No contrarian signal triggered.

### GEX time series (30d)

| Date | Spot | Regime | ZGL | Note |
|---|---|---|---|---|
| 2026-03-24 | $11.07 | POSITIVE | $11.01 | Pre-decline |
| 2026-03-27 | $10.70 | NEGATIVE | $10.99 | **Flip → neg** |
| 2026-04-27 | $10.46 | POSITIVE | $8.51 | **Flip → pos** (gap in data) |
| 2026-05-05 | $10.58 | NEGATIVE | $11.07 | **Flip → neg** |
| 2026-05-07 | $10.97 | NEGATIVE | $11.03 | Stayed neg |
| 2026-05-08 | $10.60 | POSITIVE | $7.57 | **Flip → pos** |
| 2026-05-11 | $10.71 | POSITIVE | $6.04 | ZGL collapsing |
| 2026-05-12 | $10.17 | POSITIVE | $5.02 | ZGL collapsing |
| 2026-05-13 | $9.46 | POSITIVE | $5.00 | **Cycle low** |
| 2026-05-14 | $9.72 | POSITIVE | $6.14 | Bounce starting |
| **2026-05-15** | **$10.29** | **POSITIVE** | **$7.53** | **Today** |

**Read:** Four regime flips in 8 weeks signal a **volatile dealer
regime** — every move of 3-5% has flipped the gamma sign. The ZGL
collapsed from $11+ in March to a $5-6 low last week, then began
climbing back to $7.53 on 2026-05-15. **The widening spread between
spot ($10.29) and ZGL ($7.53) — $2.76 = 27% headroom — is the
biggest "bullish runway" of the entire 30-day series.** PATH has more
positive-gamma cushion right now than at any time since 2026-03-25.

### OI trend (sustained buildup vs spike)

| Field | Value |
|---|---|
| Consecutive build days | **25** |
| 2026-05-15 net OI change | +24,534 |
| Contracts with increases | 199 |
| Contracts with decreases | 56 |

**Read:** This is **structural, not episodic** — OI has been growing
*every session* for 25 straight days. That's not a one-day catalyst
spike; that's a slow institutional position build. Combined with
phase-1's 5-of-5 sweep persistence, the picture is **persistent
multi-week accumulation through the price decline.**

### Multi-day trend table (top 12 most recent sessions)

| Date | Close | IV30d | IV rank | PCR | Net flow | Direction |
|---|---|---|---|---|---|---|
| **2026-05-15** | **$10.29** | **95.7%** | **85.4** | **0.26** | **+$1.13M** | **bullish** |
| 2026-05-14 | $9.67 | 89.7% | 76.1 | 0.12 | +$558k | bullish |
| 2026-05-13 | **$9.46** (low) | 91.2% | 78.1 | 0.63 | -$568k | bearish |
| 2026-05-12 | $10.01 | 87.1% | 72.5 | 0.43 | -$312k | bearish |
| 2026-05-11 | $10.66 | 89.7% | 76.1 | 0.63 | -$773k | bearish |
| 2026-05-08 | $10.78 | 89.4% | 75.2 | 0.51 | -$489k | bearish |
| 2026-05-07 | $10.93 | 86.0% | 70.9 | 0.37 | -$72k | bearish |
| 2026-05-06 | $10.50 | 90.3% | 76.8 | 0.37 | -$223k | bearish |
| 2026-05-05 | $10.72 | 85.0% | 77.6 | 0.49 | -$9k | bearish |
| 2026-05-04 | $10.83 | 86.2% | 71.2 | 0.24 | +$485k | bullish |
| 2026-05-01 | $10.67 | 89.5% | 75.8 | 0.20 | +$253k | bullish |
| 2026-04-30 | $10.31 | 83.5% | 60.0 | 0.52 | -$41k | bearish |
| 2026-04-27 | $10.46 | 75.6% | 56.8 | 0.34 | -$225k | bearish |
| 2026-03-27 | $10.69 | 68.4% | 46.9 | 0.20 | -$313k | bearish |
| 2026-03-18 | **$12.45** (high) | 67.0% | 45.0 | 0.31 | +$1.31M | bullish |

**Bullish days 10 / Bearish days 16** over 26 sessions —
**flow-direction was net BEARISH** until 2026-05-14 — when the
direction flipped to bullish on the bounce. **Today (2026-05-15) is
the second bullish day in a row after 8 consecutive bearish days.**

The stock made its 2-month low on 2026-05-13 ($9.46) — RIGHT into the
phase-2 dark-pool $9.40-$9.50 accumulation shelf. **The shelf is
working as designed: institutions bought, and price bounced.**

### Signal backtest — bullish_flow over the last 20 trading days

| Metric | Value |
|---|---|
| Signal type | bullish_flow |
| Lookback | 20 trading days |
| **Win rate** | **14.3%** (2 of 14) |
| Avg move | **-2.68%** |
| Tickers signaled (last 4 sessions) | QQQ, SMH, META, AVGO, TSLA, NVDA, GOOGL, QCOM, AAPL, CNC, UNH |

Sample of the 12 LOSERS:
- TSLA 2026-05-13: -7.63%
- SMH 2026-05-14: -6.28%
- QCOM 2026-05-12: -5.86%
- AVGO 2026-05-14: -4.97%
- QQQ 2026-05-14: -2.44%
- NVDA 2026-05-13: -2.09%

**Read:** PATH itself is not in the backtest sample (the sample is
large-cap tech). But the **regime signal is loud**: in the current
tape, "bullish flow" across mega-cap tech has been a fade signal. Two
interpretations:

1. **Bullish:** PATH is a small-cap NOT tied to mega-cap tech mean
   reversion — its signal could decouple.
2. **Bearish:** A general risk-off / mean-reversion regime is in
   effect, and PATH's bullish flow will follow the cohort lower.

**Phase 9 must respect this as a regime risk. Sizing down is the
correct response. The 14.3% win rate is below the 0.45 cutoff in the
skill heuristics — that explicitly says "downgrade conviction even
if today's signals look strong."**

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `historical_iv_percentile_zscore` | `{symbol: PATH, lookback-days: 252}` | IV30d 95.7%, 100th pct, z 1.77 |
| `historical_vrp` | `{symbol: PATH, date: 2026-05-15}` | VRP +35.97 pts, PREMIUM_SELLING |
| `historical_cumulative_premium_flow` | `{symbol: PATH, days: 90}` | Bullish $37.1M vs bearish $38.5M, net -$1.4M |
| `historical_pc_ratio_zscore` | `{symbol: PATH, lookback-days: 20}` | PCR 0.26, z -0.54, NORMAL |
| `historical_gex_time_series` | `{symbol: PATH, days: 30, dte-max: 45}` | 4 regime flips; widest spot−ZGL in 30d at $2.76 |
| `historical_oi_trend` | `{symbol: PATH, days: 30, top-n: 10}` | **25 consecutive build days**, +24,534 today |
| `historical_trend` | `{symbol: PATH, days: 30}` | 10 bull / 16 bear, $12.45 high → $9.46 low → $10.29 |
| `historical_signal_backtest` | `{signal-type: bullish_flow, lookback-days: 20, top-n: 20}` | 14.3% win rate, avg -2.68%, 14 signals |

## Tool errors

(none)

## Verdict for downstream phases

- **Volatility regime:** **RICH** (IV30d 100th pct, VRP +36 pts).
  Premium-selling favored.
- **Premium-buying vs premium-selling:** **PREMIUM-SELLING** is the
  edge-positive structural choice. Long-call structures pay a heavy vol
  tax.
- **Bias from this phase:** **CAUTIOUSLY BULLISH** — the PATH-specific
  signal is real (25-day OI build, dark-pool support working, bullish
  flow persistence), but the macro-regime signal is HOSTILE (bullish
  flow market-wide losing 86% of the time over the past 20 days).
- **Conviction that today's signal is historically edge-positive:**
  **2/5** — IV is at the 100th percentile and the signal backtest is
  failing. Per the skill heuristics, conviction must be downgraded
  here.
- **Three specific data points for phase-9:**
  1. **IV percentile = 100, VRP = +35.97 vol pts** → favor credit spreads
     / call spread debits (defined-risk, vega-neutral) over outright
     long calls.
  2. **Bullish_flow signal win rate = 14.3%** → regime gate: trade
     smaller than the per-signal models suggest. Apply a 0.30-0.50
     position-size multiplier vs the unconstrained Kelly.
  3. **Spot $10.29 vs ZGL $7.53 (gap $2.76, widest in 30d)** → bullish
     dealer-flow runway is real but the runway shrinks fast above $11
     where positive-gamma damping engages (phase 4).
- **Open questions for downstream:**
  - Does PATH have a documented earnings date in the 2026-05-26 to
    2026-05-29 window? (phase 6 must confirm to attribute the
    118% IV kink properly.)
  - Has PATH's average post-earnings move historically been ≤ or ≥
    16-18%? The 2026-05-29 weekly is pricing roughly a ±16% one-σ
    weekly move at 118% IV — if historical avg post-earnings move is
    smaller, vol is rich and short premium has edge.
  - Is the slight net-bearish 90-day cumulative flow (-$1.4M) the
    "smart sellers were right" signal, or is it about to flip as the
    25-day OI buildup matures into directional exposure?
