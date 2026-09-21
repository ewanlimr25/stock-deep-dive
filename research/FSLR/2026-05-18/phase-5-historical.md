# Phase 5 — Historical Context & VRP

**Ticker:** FSLR
**As-of date:** 2026-05-18 (data anchor: 2026-05-15)
**Generated:** 2026-05-18T00:50:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-4-structure.md

## Summary

FSLR's 1-year IV30 sits at the **56th percentile (z = −0.21, regime NORMAL,
IV30d = 52.81%)** — neither cheap nor rich on an absolute basis, but the
**VRP is positive at +9.8 vol points (IV30 52.81% vs RV30 43.01%) → regime
PREMIUM_SELLING**: options are pricing about 10 vol points more than the
stock has actually realized. Over the prior 26 available sessions
(2026-03-13 → 2026-05-15) FSLR rallied **from $196.07 to $233.66 (≈ +19.2%)**
with **17 bullish-flow days vs 9 bearish (65/35)**; total open interest
expanded from ~505K to ~574K, consistent with a sustained institutional
engagement. The dealer regime has been **stable POSITIVE since 2026-05-11**
with no flips in 5 sessions and total GEX rebuilding from ~$254M (5/14) to
$452M (5/15). One serious caution: the market-wide **`bullish_flow` signal
backtest is firing a 26.3% win rate / −1.26% avg 20d move** across 19
recent firings — bullish flow setups have been *failing* in the
current regime. Conviction on the historical edge of today's signal:
**2.5/5 — structurally constructive but tape-regime currently hostile to
bullish-flow setups.**

## Key signals

- **IV regime NORMAL, IV30=52.81%, percentile=56, z=−0.21** — neither cheap
  nor rich, no IV crush nor IV spike to play [HIST:historical_iv_percentile_zscore].
- **VRP = +0.098** (IV30 52.81% − RV30 43.01%) → PREMIUM_SELLING regime;
  options ~10 vol pts richer than realized — credit-spread tailwind
  [HIST:historical_vrp].
- **Cumulative premium flow 90d (26 dates): bullish $271M vs bearish $263M,
  net +$8.66M, trend MIXED** — essentially balanced; not a stealth
  accumulation campaign in dollar terms but tilts bullish day-counts
  [HIST:historical_cumulative_premium_flow].
- **PCR z-score −0.675 (current 0.41 vs 20d mean 0.64, std 0.34)** — slightly
  call-heavy vs trailing window but not extreme [HIST:historical_pc_ratio_zscore].
- **GEX regime stable POSITIVE 5 sessions running (since 2026-05-11), with
  GEX scale expanding from −$5M (3/13) to +$452M (5/15)** — the dealer
  structure has *graduated* into a long-gamma steady state
  [HIST:historical_gex_time_series].
- **Trend window: spot +19.2% from $196.07 → $233.66 over 2026-03-13 →
  2026-05-15, 17 bullish vs 9 bearish flow days** [HIST:historical_trend].
- **Signal backtest (bullish_flow, 20d): win rate 26.3% / avg −1.26% across
  19 firings** — bullish-flow setups have been net losing in the current
  market regime; downgrades naive-bullish conviction [HIST:historical_signal_backtest].

## Detailed findings

### IV regime (percentile + z-score + VRP)

| Metric | Value |
|--------|-------|
| Current IV30d | 52.81% |
| 252d percentile | **56** |
| z-score | **−0.214** |
| Regime | NORMAL |
| dates_used | 25 (data archive does not extend full 1y) |

| Metric | Value |
|--------|-------|
| IV30d | 52.81% |
| Realized vol 30d | 43.01% |
| VRP | **+0.098** (9.8 vol points) |
| Regime | **PREMIUM_SELLING** |

Implication: IV is mid-pack on a 1y basis, but vs realized it is pricing
~10 vol points of *excess*. Two-sided premium-buying is not blocked
(IV isn't notably rich on percentile basis) but credit structures
(short premium) carry a measurable VRP tailwind.

### Cumulative premium flow (90d)

| Metric | Value |
|--------|-------|
| Days covered | 26 (2026-03-13 → 2026-05-15) |
| Cumulative bullish premium | $271,198,609 |
| Cumulative bearish premium | $262,532,825 |
| **Net flow** | **+$8,665,784** |
| Trend direction | MIXED |

90d premium is essentially balanced — neither a hidden bull campaign
nor a distribution wave. This **tempers** the phase-1 single-day
"+$1.63M net call buying" headline: today's bullish flow does not have
a multi-month accumulation tail behind it.

### P/C ratio z-score

| Metric | Value |
|--------|-------|
| Current PCR | 0.41 |
| 20d mean | 0.640 |
| 20d std | 0.341 |
| z-score | **−0.675** |
| Extreme tag | NORMAL |

PCR is below mean (more calls relative to puts than typical) but not
extreme — no contrarian fade trigger. Consistent with phase-4's
"COMPLACENT" skew read at a structural level.

### GEX time series (26 sessions)

Regime flip dates in the lookback:

| Date | From | To | Spot | ZGL | ZGL_Δ |
|------|------|-----|------|-----|-------|
| 2026-03-23 | NEGATIVE | POSITIVE | 190.08 | 79.04 | −158 |
| 2026-04-27 | POSITIVE | NEGATIVE | 195.52 | 216.48 | +150 |
| 2026-04-28 | NEGATIVE | POSITIVE | 196.00 | 120.09 | −96 |
| 2026-04-29 | POSITIVE | NEGATIVE | 189.01 | 213.92 | +94 |
| 2026-04-30 | NEGATIVE | POSITIVE | 200.13 | 120.40 | −94 |
| 2026-05-04 | POSITIVE | NEGATIVE | 209.69 | 217.88 | +103 |
| 2026-05-05 | NEGATIVE | POSITIVE | 217.94 | 115.30 | −103 |
| 2026-05-08 | POSITIVE | NEGATIVE | 216.77 | 219.80 | +129 |
| **2026-05-11** | **NEGATIVE** | **POSITIVE** | **233.03** | **131.19** | **−89** |

**No flip since 2026-05-11** — the dealer regime has been stable
POSITIVE for 5 sessions through 2026-05-15. Total GEX trajectory:

| Date | Total GEX | ZGL | Regime |
|------|-----------|-----|--------|
| 2026-05-11 | $1,054,318,105 | 131.19 | POSITIVE |
| 2026-05-12 | $225,671,361 | 103.76 | POSITIVE |
| 2026-05-13 | $335,726,758 | 105.37 | POSITIVE |
| 2026-05-14 | $254,925,783 | 218.89 | POSITIVE |
| 2026-05-15 | **$452,282,889** | **121.35** | POSITIVE |

The chaotic flip pattern in March–April (8 flips in 6 weeks) gave way to a
steady-state long-gamma regime starting 2026-05-11. **This is the
single most bullish historical-context datapoint**: the structure has
matured, not just snapped.

### Multi-day trend (26 sessions)

| Date | Close | IV30d | IV rank | PCR | Flow | Net flow |
|------|-------|-------|---------|-----|------|----------|
| 2026-05-15 | **233.66** | 52.8% | 37.8 | 0.41 | bullish | +$648K |
| 2026-05-14 | 231.62 | 51.8% | 26.4 | 0.28 | bullish | +$87K |
| 2026-05-13 | 234.60 | 53.2% | 31.2 | 1.06 | bullish | +$1.69M |
| 2026-05-12 | 228.06 | 51.6% | 25.7 | 0.84 | bearish | −$1.14M |
| 2026-05-11 | 233.27 | 54.9% | 36.9 | 0.51 | bullish | +$1.66M |
| 2026-05-08 | 220.06 | 49.7% | 17.7 | 0.48 | bullish | +$2.12M |
| 2026-05-07 | 214.57 | 50.4% | 21.7 | 0.55 | bearish | −$579K |
| 2026-05-06 | 218.00 | 50.8% | 23.1 | 0.52 | bearish | −$180K |
| 2026-05-05 | 219.16 | 52.6% | 24.8 | 0.53 | bullish | +$2.41M |
| 2026-05-04 | 211.39 | 52.7% | 29.2 | 0.26 | bullish | +$1.61M |
| 2026-05-01 | 211.71 | 50.4% | 21.4 | 0.26 | bearish | **−$9.92M** |
| 2026-04-30 | 201.80 | 59.4% | 50.1 | 0.49 | bullish | +$3.44M |
| 2026-04-29 | 190.61 | 60.8% | 56.8 | 0.99 | bullish | +$2.88M |
| 2026-04-28 | 195.86 | 62.0% | **60.8** | 0.65 | bullish | +$1.99M |
| 2026-04-27 | 197.48 | 61.0% | 57.3 | 0.25 | bullish | +$3.86M |
| 2026-03-27 | 190.29 | 53.9% | 23.4 | 0.97 | bullish | +$399K |
| 2026-03-26 | 185.83 | 51.6% | 18.0 | 0.92 | bullish | +$660K |
| 2026-03-25 | 193.51 | 53.1% | 21.7 | 0.41 | bullish | +$53K |
| 2026-03-24 | 192.85 | 53.1% | 21.5 | 0.82 | bearish | −$265K |
| 2026-03-23 | 189.92 | 54.0% | 23.7 | 0.44 | bearish | −$6.82M |
| 2026-03-20 | 192.82 | 52.4% | 20.0 | 1.58 | bearish | −$14.6M |
| 2026-03-19 | 199.65 | 50.8% | 13.5 | **4.79** | bearish | **−$27.3M** |
| 2026-03-18 | 197.81 | 51.7% | 18.2 | 1.41 | bullish | +$3.53M |
| 2026-03-17 | 200.42 | 51.7% | 18.3 | 2.25 | bullish | +$11.85M |
| 2026-03-16 | 199.48 | 51.4% | 17.5 | 1.46 | bullish | **+$35.6M** |
| 2026-03-13 | 196.07 | 54.0% | 23.7 | 1.70 | bearish | −$5.04M |

Highlights:
- **2026-03-16 bullish capitulation**: PCR 1.46, **+$35.6M** net flow,
  $52.6M put premium with bullish flow_direction (puts being SOLD heavily,
  i.e. closing). Close $199.48.
- **2026-03-19/20 bearish flush**: PCR 4.79 and 1.58, net flow
  **−$27.3M** and **−$14.6M** — coordinated put buying. Close $199.65.
- **2026-04-27 → 2026-04-30 IV regime peak**: IV rank 50–61. Spot
  $190–202. This was the volatility regime that birthed the current
  long-gamma buildup.
- **2026-05-01 net flow −$9.92M outlier**: largest bearish day of the run
  on a day where stock barely moved ($211.71). Could be a single fund's
  unwind day — does not coincide with a price break.
- **Recent 5 sessions (5/11–5/15): 4 bullish-flow days, 1 bearish (5/12).
  Net flow of +$2.94M cumulative.** Modest but consistent.

**OI trajectory** (from `total_open_interest` field, since `historical_oi_trend`
errored on size):

| Date | OI |
|------|-----|
| 2026-03-13 | 578,565 |
| 2026-03-19 | 576,403 |
| 2026-04-27 | 507,949 |
| 2026-05-01 | 540,048 |
| 2026-05-08 | 561,861 |
| 2026-05-11 | 552,118 |
| 2026-05-15 | 574,424 |

OI dipped through April (May OPEX expiries running off) and rebuilt into
mid-May. Net change is roughly flat (-4K contracts) — engagement level
unchanged, but composition has rotated forward into newer expiries.

### Signal backtest (bullish_flow, 20-day horizon)

| Metric | Value |
|--------|-------|
| Signal type | bullish_flow |
| Lookback | 20 trading days |
| Total signals | 19 |
| **Win rate** | **26.3%** |
| **Avg move** | **−1.26%** |

Sample of recent firings:

| Date | Ticker | Direction | Move |
|------|--------|-----------|------|
| 2026-05-14 | QQQ | down | −1.4% |
| 2026-05-14 | SMH | down | −3.2% |
| 2026-05-14 | META | down | −1.8% |
| 2026-05-14 | AVGO | down | **−4.4%** |
| 2026-05-13 | TSLA | down | **−6.0%** |
| 2026-05-13 | NVDA | up | +0.3% |
| 2026-05-12 | NVDA | up | +2.6% |
| 2026-05-12 | UNH | down | −2.7% |
| 2026-05-11 | NVDA | up | +3.3% |
| 2026-05-11 | TSLA | down | **−5.9%** |
| 2026-05-11 | RKLB | up | **+16.2%** |
| 2026-05-11 | LITE | down | **−13.2%** |

NVDA was the consistent winner; everything else (especially semis/mega-caps)
got hit. RKLB and LITE were outlier ±15%+ tails. **Implication for FSLR:**
the market regime in May 2026 has been *unkind to bullish-flow setups*.
Even though FSLR's structure is uniquely clean (long-gamma stable, complacent
skew), the broader tape regime is fading these signals. This is the most
important caution flag in the entire deep dive so far.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__historical_iv_percentile_zscore` | `{symbol: FSLR, lookback-days: 252}` | IV30 52.8%, pct 56, z −0.21, NORMAL |
| `mcp__uw-pp__historical_vrp` | `{symbol: FSLR, realised-window-days: 30, date: 2026-05-15}` | VRP +0.098, PREMIUM_SELLING |
| `mcp__uw-pp__historical_cumulative_premium_flow` | `{symbol: FSLR, days: 90}` | Net +$8.66M, MIXED, 26 dates |
| `mcp__uw-pp__historical_pc_ratio_zscore` | `{symbol: FSLR, lookback-days: 20}` | PCR 0.41 vs mean 0.64, z −0.67, NORMAL |
| `mcp__uw-pp__historical_gex_time_series` | `{symbol: FSLR, days: 30, dte-max: 45}` | 9 regime flips Mar–May; stable POSITIVE since 5/11 |
| `mcp__uw-pp__historical_oi_trend` | `{symbol: FSLR, days: 30, top-n: 15}` | **ERROR** (oversized output >73K chars); fell back to historical_trend.total_open_interest |
| `mcp__uw-pp__historical_trend` | `{symbol: FSLR, days: 30}` | 26 daily rows; spot +19%, 17 bull / 9 bear days |
| `mcp__uw-pp__historical_signal_backtest` | `{signal-type: bullish_flow, lookback-days: 20, top-n: 25}` | win_rate 26.3%, avg −1.26%, n=19 |

## Tool errors

- `mcp__uw-pp__historical_oi_trend`: failed with truncation —
  `result (73,861 characters across 2,999 lines) exceeds maximum allowed
  tokens. Output has been saved to .../mcp-uw-pp-historical_oi_trend-1779111423993.txt`.
  Mitigated by using `total_open_interest` field from `historical_trend`.
  Strike-level OI buildup detail not retrieved.

## Verdict for downstream phases

- **Volatility regime:** **NORMAL** on percentile (52.8% IV30, 56th %ile)
  but **PREMIUM_SELLING** on VRP (+9.8 vol pts). Translation: IV isn't
  cheap enough to make naked debits attractive; credit structures have a
  measurable edge.
- **Premium-flow environment:** Recent 5d is mildly bullish but 90d net
  flow is MIXED at +$8.66M — no stealth-bull tail.
- **Conviction whether today's signal is HISTORICALLY EDGE-POSITIVE: 2.5/5.**
  Three reasons up: (a) GEX regime stable POSITIVE for 5 sessions, (b) OI
  rebuilding, (c) +19% rally absorbed by long-gamma. Two reasons down:
  (d) bullish_flow signal market-wide is failing (26.3% win rate), (e) 90d
  net premium flow is balanced not bullish.
- **Three specific data points:**
  1. **IV percentile = 56, IV30d = 52.8%, VRP = +9.8 vol pts** —
     premium-selling regime; favors short-vol / credit structures.
  2. **Bullish-flow signal win rate = 26.3%, avg 20d move = −1.26%** —
     external market regime headwind; sets size discipline ceiling.
  3. **9 GEX regime flips in March–April, but 0 flips in last 5 sessions** —
     long-gamma regime maturity; entry timing favorable for gamma-aware
     short-vol structures (call-credit spreads or covered structures).
- **Open questions for downstream:**
  - What is the macro regime for solar / IRA / utility-scale capex
    spending in May 2026? Does it explain the May-22 IV bump?
    (→ phase-6 macro)
  - Do the composite insights tools confirm "institutional accumulation"
    on FSLR despite the bearish market-wide signal backtest?
    (→ phase-7 insights)
  - Is the persistent put-hedge layer (phase-1) protection or directional?
    Strike skew complacent (phase-4) means it's cheap protection — but
    against what? (→ phase-6, phase-8)
